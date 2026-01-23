"""Watcher module for monitoring inbox directory."""

import logging
import time
from pathlib import Path
from typing import Set

from app.config import Config
from app.processor import process_file
from app.registry import Registry
from app.report import ReportWriter

logger = logging.getLogger(__name__)


def watch_polling(config: Config):
    """Watch inbox directory using polling.

    Args:
        config: Configuration object
    """
    inbox_dir = Path(config.paths["inbox"])
    out_dir = Path(config.paths["out"])
    registry_path = out_dir / "processed_registry.json"
    report_path = out_dir / "run_report.ndjson"

    registry = Registry(registry_path)
    report = ReportWriter(report_path)

    interval = config.watcher.get("interval_seconds", 5)
    min_age = config.watcher.get("min_file_age_seconds", 2)

    logger.info(f"Starting polling watcher (interval={interval}s, min_age={min_age}s)")

    processed_in_session: Set[str] = set()

    try:
        while True:
            if not inbox_dir.exists():
                inbox_dir.mkdir(parents=True, exist_ok=True)

            files = sorted(inbox_dir.glob("*"))
            files = [f for f in files if f.is_file()]

            current_time = time.time()

            for filepath in files:
                # Check if file is old enough
                file_age = current_time - filepath.stat().st_mtime
                if file_age < min_age:
                    continue

                # Check if already processed in this session
                if str(filepath) in processed_in_session:
                    continue

                # Process file
                success = process_file(filepath, config, registry, report)
                processed_in_session.add(str(filepath))

            time.sleep(interval)

    except KeyboardInterrupt:
        logger.info("Watcher stopped by user")


def watch_watchdog(config: Config):
    """Watch inbox directory using watchdog library.

    Args:
        config: Configuration object
    """
    try:
        from watchdog.events import FileSystemEventHandler
        from watchdog.observers import Observer
    except ImportError:
        logger.error("watchdog library not installed. Install with: pip install watchdog")
        logger.info("Falling back to polling mode")
        watch_polling(config)
        return

    inbox_dir = Path(config.paths["inbox"])
    out_dir = Path(config.paths["out"])
    registry_path = out_dir / "processed_registry.json"
    report_path = out_dir / "run_report.ndjson"

    registry = Registry(registry_path)
    report = ReportWriter(report_path)

    min_age = config.watcher.get("min_file_age_seconds", 2)

    class InboxHandler(FileSystemEventHandler):
        """Handler for inbox file events."""

        def __init__(self):
            self.processed_in_session: Set[str] = set()

        def on_created(self, event):
            """Handle file creation event."""
            if event.is_directory:
                return

            filepath = Path(event.src_path)

            # Wait for file to stabilize
            time.sleep(min_age)

            # Check if already processed
            if str(filepath) in self.processed_in_session:
                return

            # Process file
            if filepath.exists():
                process_file(filepath, config, registry, report)
                self.processed_in_session.add(str(filepath))

    inbox_dir.mkdir(parents=True, exist_ok=True)

    event_handler = InboxHandler()
    observer = Observer()
    observer.schedule(event_handler, str(inbox_dir), recursive=False)
    observer.start()

    logger.info(f"Starting watchdog watcher on {inbox_dir}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("Watcher stopped by user")

    observer.join()


def watch(config: Config):
    """Watch inbox directory for new files.

    Args:
        config: Configuration object
    """
    mode = config.watcher.get("mode", "polling")

    if mode == "watchdog":
        watch_watchdog(config)
    else:
        watch_polling(config)
