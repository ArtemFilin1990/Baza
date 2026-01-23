"""Command-line interface for bearing data processor."""

import argparse
import sys
from pathlib import Path

from .config import Config
from .logger import LoggerSetup
from .processor import FileProcessor
from .watcher import InboxWatcher


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Bearing Data Processing Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Watch mode (default) - continuously monitor inbox/
  python -m src.cli watch
  
  # Process existing files once and exit
  python -m src.cli once
  
  # Rebuild catalog from processed files
  python -m src.cli rebuild
        """
    )
    
    parser.add_argument(
        'mode',
        choices=['watch', 'once', 'rebuild'],
        default='watch',
        nargs='?',
        help='Processing mode (default: watch)'
    )
    
    parser.add_argument(
        '--config-dir',
        type=str,
        default=None,
        help='Path to configuration directory (default: ./config)'
    )
    
    parser.add_argument(
        '--log-level',
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default=None,
        help='Override log level from config'
    )
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        if args.config_dir:
            config_dir = Path(args.config_dir)
        else:
            config_dir = Path(__file__).parent.parent / 'config'
        
        config = Config(config_dir=config_dir)
        
        # Setup logging
        app_config = config.load_app_config()
        log_dir = Path(app_config['paths']['logs'])
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / 'app.log'
        
        log_level = args.log_level or config.get('logging.level', 'INFO')
        log_format = config.get('logging.format', 'json')
        
        logger = LoggerSetup.setup(log_file, log_format, log_level)
        
        # Initialize processor
        processor = FileProcessor(config, logger)
        
        # Execute mode
        if args.mode == 'once':
            logger.info("Running in ONCE mode - processing inbox once")
            n_processed, n_success, n_errors = processor.process_inbox()
            
            logger.info(f"Processing complete: {n_processed} files, {n_success} success, {n_errors} errors")
            
            if n_errors > 0:
                sys.exit(1)
            else:
                sys.exit(0)
        
        elif args.mode == 'rebuild':
            logger.info("Running in REBUILD mode - rebuilding catalog from processed files")
            n_files, n_records = processor.rebuild_catalog()
            
            logger.info(f"Rebuild complete: {n_files} files, {n_records} records")
            sys.exit(0)
        
        elif args.mode == 'watch':
            logger.info("Running in WATCH mode - monitoring inbox for new files")
            
            # Setup watcher
            watcher_mode = config.get('watcher.mode', 'poll')
            poll_interval = config.get('watcher.poll_interval', 5)
            process_on_start = config.get('watcher.process_on_start', True)
            
            watcher = InboxWatcher(
                inbox_dir=processor.inbox_dir,
                on_file_callback=processor.process_file,
                mode=watcher_mode,
                poll_interval=poll_interval,
                logger=logger
            )
            
            logger.info(f"Starting watcher (mode: {watcher_mode}, interval: {poll_interval}s)")
            logger.info(f"Watching directory: {processor.inbox_dir}")
            logger.info("Press Ctrl+C to stop")
            
            try:
                watcher.start(process_existing=process_on_start)
            except KeyboardInterrupt:
                logger.info("Stopping watcher...")
                watcher.stop()
                logger.info("Watcher stopped")
                sys.exit(0)
    
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
