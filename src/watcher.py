"""File watcher module for monitoring inbox directory."""

import logging
import time
from pathlib import Path
from typing import Callable, Optional

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileMovedEvent
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False


class InboxWatcher:
    """Watch inbox directory for new files."""
    
    def __init__(
        self,
        inbox_dir: Path,
        on_file_callback: Callable[[Path], None],
        mode: str = 'poll',
        poll_interval: int = 5,
        logger: Optional[logging.Logger] = None
    ):
        """Initialize watcher.
        
        Args:
            inbox_dir: Directory to watch
            on_file_callback: Callback function to call when file is detected
            mode: Watch mode - 'poll' or 'watch'
            poll_interval: Polling interval in seconds (for poll mode)
            logger: Logger instance
        """
        self.inbox_dir = Path(inbox_dir)
        self.on_file_callback = on_file_callback
        self.mode = mode
        self.poll_interval = poll_interval
        self.logger = logger or logging.getLogger(__name__)
        
        self._running = False
        self._processed_files = set()
        self._observer = None
    
    def start(self, process_existing: bool = True) -> None:
        """Start watching inbox.
        
        Args:
            process_existing: Process existing files on start
        """
        self._running = True
        
        if process_existing:
            self._process_existing_files()
        
        if self.mode == 'watch' and WATCHDOG_AVAILABLE:
            self._start_watchdog()
        else:
            if self.mode == 'watch' and not WATCHDOG_AVAILABLE:
                self.logger.warning("watchdog not available, falling back to poll mode")
            self._start_polling()
    
    def stop(self) -> None:
        """Stop watching."""
        self._running = False
        
        if self._observer:
            self._observer.stop()
            self._observer.join()
    
    def _process_existing_files(self) -> None:
        """Process files that already exist in inbox."""
        files = list(self.inbox_dir.glob('*'))
        files = [f for f in files if f.is_file() and not f.name.startswith('.')]
        
        for file_path in files:
            self._handle_file(file_path)
    
    def _handle_file(self, file_path: Path) -> None:
        """Handle detected file.
        
        Args:
            file_path: Path to file
        """
        # Skip if already processed in this session
        if str(file_path) in self._processed_files:
            return
        
        # Skip hidden files and temp files
        if file_path.name.startswith('.') or file_path.name.endswith('.tmp'):
            return
        
        # Wait a bit to ensure file is fully written
        time.sleep(0.5)
        
        # Check if file still exists (might have been moved)
        if not file_path.exists():
            return
        
        # Mark as processed in this session
        self._processed_files.add(str(file_path))
        
        # Call callback
        try:
            self.on_file_callback(file_path)
        except Exception as e:
            self.logger.error(f"Error in file callback for {file_path}: {e}", exc_info=True)
    
    def _start_polling(self) -> None:
        """Start polling mode."""
        self.logger.info(f"Starting polling watcher (interval: {self.poll_interval}s)")
        
        while self._running:
            try:
                files = list(self.inbox_dir.glob('*'))
                files = [f for f in files if f.is_file() and not f.name.startswith('.')]
                
                for file_path in files:
                    if not self._running:
                        break
                    self._handle_file(file_path)
                
            except Exception as e:
                self.logger.error(f"Error in polling loop: {e}", exc_info=True)
            
            # Sleep with interruptible check
            sleep_start = time.time()
            while self._running and (time.time() - sleep_start) < self.poll_interval:
                time.sleep(0.1)
    
    def _start_watchdog(self) -> None:
        """Start watchdog file system observer."""
        self.logger.info("Starting watchdog file system observer")
        
        event_handler = InboxEventHandler(
            on_file_callback=self._handle_file,
            logger=self.logger
        )
        
        self._observer = Observer()
        self._observer.schedule(event_handler, str(self.inbox_dir), recursive=False)
        self._observer.start()
        
        try:
            while self._running:
                time.sleep(1)
        except KeyboardInterrupt:
            self._observer.stop()
        
        self._observer.join()


class InboxEventHandler(FileSystemEventHandler):
    """Handle file system events for inbox directory."""
    
    def __init__(self, on_file_callback: Callable[[Path], None], logger: logging.Logger):
        """Initialize event handler.
        
        Args:
            on_file_callback: Callback for file events
            logger: Logger instance
        """
        super().__init__()
        self.on_file_callback = on_file_callback
        self.logger = logger
    
    def on_created(self, event):
        """Handle file created event.
        
        Args:
            event: File system event
        """
        if isinstance(event, FileCreatedEvent) and not event.is_directory:
            file_path = Path(event.src_path)
            self.logger.debug(f"File created: {file_path.name}")
            self.on_file_callback(file_path)
    
    def on_moved(self, event):
        """Handle file moved event.
        
        Args:
            event: File system event
        """
        if isinstance(event, FileMovedEvent) and not event.is_directory:
            # File moved into inbox
            file_path = Path(event.dest_path)
            self.logger.debug(f"File moved to inbox: {file_path.name}")
            self.on_file_callback(file_path)
