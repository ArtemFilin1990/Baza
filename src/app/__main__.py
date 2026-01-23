"""Main entry point for the automation pipeline."""

import logging
import sys
from pathlib import Path

from app.config import Config
from app.processor import process_once, rebuild_catalog
from app.watcher import watch

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


def setup_logging(config: Config):
    """Setup file logging.

    Args:
        config: Configuration object
    """
    log_dir = Path(config.paths["logs"])
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    logging.getLogger().addHandler(file_handler)


def main():
    """Main entry point."""
    # Parse command line arguments
    mode = "watch"
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    # Load configuration
    try:
        config = Config()
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)

    # Setup logging
    setup_logging(config)

    logger.info(f"Starting automation pipeline in '{mode}' mode")

    try:
        if mode == "watch":
            watch(config)
        elif mode == "once":
            process_once(config)
        elif mode == "rebuild":
            rebuild_catalog(config)
        else:
            logger.error(f"Unknown mode: {mode}")
            logger.info("Available modes: watch, once, rebuild")
            sys.exit(1)
    except Exception as e:
        logger.error(f"Pipeline error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
