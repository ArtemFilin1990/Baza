"""Logging and reporting module."""

import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


class LoggerSetup:
    """Setup and manage logging."""
    
    @staticmethod
    def setup(log_file: Path, log_format: str = 'json', log_level: str = 'INFO') -> logging.Logger:
        """Setup logger with file and console handlers.
        
        Args:
            log_file: Path to log file
            log_format: Format type - 'json' or 'text'
            log_level: Log level
            
        Returns:
            Configured logger
        """
        logger = logging.getLogger('bearing_processor')
        logger.setLevel(getattr(logging, log_level.upper()))
        
        # Remove existing handlers
        logger.handlers = []
        
        # File handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(getattr(logging, log_level.upper()))
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, log_level.upper()))
        
        # Set formatter
        if log_format == 'json':
            formatter = JsonFormatter()
        else:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger


class JsonFormatter(logging.Formatter):
    """JSON log formatter."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON.
        
        Args:
            record: Log record
            
        Returns:
            JSON formatted log string
        """
        log_data = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }
        
        # Add extra fields if present
        if hasattr(record, 'file'):
            log_data['file'] = record.file
        if hasattr(record, 'sha'):
            log_data['sha'] = record.sha
        if hasattr(record, 'status'):
            log_data['status'] = record.status
        if hasattr(record, 'n_rows'):
            log_data['n_rows'] = record.n_rows
        if hasattr(record, 'n_added'):
            log_data['n_added'] = record.n_added
        if hasattr(record, 'n_skipped'):
            log_data['n_skipped'] = record.n_skipped
        if hasattr(record, 'n_conflicts'):
            log_data['n_conflicts'] = record.n_conflicts
        
        return json.dumps(log_data, ensure_ascii=False)


class Reporter:
    """NDJSON reporter for processing results."""
    
    def __init__(self, report_file: Path):
        """Initialize reporter.
        
        Args:
            report_file: Path to NDJSON report file
        """
        self.report_file = report_file
        self.report_file.parent.mkdir(parents=True, exist_ok=True)
    
    def write_report(
        self,
        filename: str,
        file_hash: str,
        status: str,
        n_rows: int = 0,
        n_added: int = 0,
        n_skipped: int = 0,
        n_conflicts: int = 0,
        error_message: Optional[str] = None,
        processing_time: Optional[float] = None
    ) -> None:
        """Write processing report entry.
        
        Args:
            filename: Processed filename
            file_hash: File SHA256 hash
            status: Processing status (success, error, skipped)
            n_rows: Number of rows in file
            n_added: Number of rows added to catalog
            n_skipped: Number of rows skipped
            n_conflicts: Number of conflicts detected
            error_message: Error message if failed
            processing_time: Processing time in seconds
        """
        report_entry = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'filename': filename,
            'sha256': file_hash,
            'status': status,
            'n_rows': n_rows,
            'n_added': n_added,
            'n_skipped': n_skipped,
            'n_conflicts': n_conflicts,
        }
        
        if error_message:
            report_entry['error'] = error_message
        
        if processing_time is not None:
            report_entry['processing_time_sec'] = round(processing_time, 3)
        
        # Append to NDJSON file
        with open(self.report_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(report_entry, ensure_ascii=False) + '\n')
