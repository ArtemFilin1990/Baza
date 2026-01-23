"""Main data processing module."""

import logging
import shutil
import time
from pathlib import Path
from typing import Tuple

from .catalog import CatalogManager
from .config import Config
from .logger import Reporter
from .parser import DataParser
from .registry import Registry
from .utils import compute_file_hash, detect_file_type, generate_processed_filename


class FileProcessor:
    """Process bearing data files."""
    
    def __init__(self, config: Config, logger: logging.Logger):
        """Initialize processor.
        
        Args:
            config: Configuration instance
            logger: Logger instance
        """
        self.config = config
        self.logger = logger
        
        # Get paths from config
        app_config = config.load_app_config()
        self.inbox_dir = Path(app_config['paths']['inbox'])
        self.processed_dir = Path(app_config['paths']['processed'])
        self.error_dir = Path(app_config['paths']['error'])
        self.out_dir = Path(app_config['paths']['out'])
        
        # Ensure directories exist
        for dir_path in [self.inbox_dir, self.processed_dir, self.error_dir, self.out_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize components
        brand_aliases = config.load_brand_aliases()
        parsing_rules = config.load_parsing_rules()
        normalization_config = app_config.get('normalization', {})
        
        self.parser = DataParser(parsing_rules, normalization_config)
        
        self.catalog = CatalogManager(
            catalog_csv=self.out_dir / 'catalog_target.csv',
            catalog_json=self.out_dir / 'catalog_target.json',
            brand_aliases=brand_aliases,
            normalization_config=normalization_config
        )
        
        registry_file = Path(config.get('registry.file', 'out/processed_registry.json'))
        self.registry = Registry(registry_file)
        
        self.reporter = Reporter(self.out_dir / 'run_report.ndjson')
        
        # Get max file size limit
        self.max_file_size = config.get('limits.max_file_size_mb', 50) * 1024 * 1024
    
    def process_file(self, file_path: Path) -> Tuple[str, int]:
        """Process a single file.
        
        Args:
            file_path: Path to file to process
            
        Returns:
            Tuple of (status, n_records)
        """
        start_time = time.time()
        filename = file_path.name
        
        self.logger.info(f"Processing file: {filename}")
        
        try:
            # Check file size
            file_size = file_path.stat().st_size
            if file_size > self.max_file_size:
                raise ValueError(f"File too large: {file_size} bytes (max: {self.max_file_size})")
            
            # Compute file hash
            file_hash = compute_file_hash(file_path)
            
            # Check if already processed
            if self.registry.is_processed(file_hash):
                self.logger.info(
                    f"File already processed (hash: {file_hash[:8]}), skipping",
                    extra={'file': filename, 'sha': file_hash[:8], 'status': 'skipped'}
                )
                
                # Move to processed directory anyway
                existing_entry = self.registry.get_entry(file_hash)
                n_records = existing_entry.get('n_records', 0) if existing_entry else 0
                
                processing_time = time.time() - start_time
                self.reporter.write_report(
                    filename=filename,
                    file_hash=file_hash,
                    status='skipped_duplicate',
                    n_rows=n_records,
                    n_added=0,
                    n_skipped=n_records,
                    n_conflicts=0,
                    processing_time=processing_time
                )
                
                # Move to processed with existing name
                dest_name = existing_entry.get('processed_name', filename) if existing_entry else filename
                dest_path = self.processed_dir / dest_name
                
                if dest_path.exists():
                    # Add timestamp to avoid collision
                    dest_path = self.processed_dir / f"{dest_path.stem}_dup{dest_path.suffix}"
                
                shutil.move(str(file_path), str(dest_path))
                
                return 'skipped_duplicate', n_records
            
            # Detect file type
            file_type = detect_file_type(file_path)
            if file_type == 'unknown':
                raise ValueError(f"Unsupported file type: {file_path.suffix}")
            
            # Parse file
            df = self.parser.parse_file(file_path, file_type)
            n_rows = len(df)
            
            self.logger.info(f"Parsed {n_rows} rows from {filename}")
            
            # Normalize columns
            df = self.parser.normalize_columns(df)
            
            # Validate required fields
            df = self.parser.validate_required_fields(df)
            n_valid_rows = len(df)
            
            if n_valid_rows == 0:
                raise ValueError("No valid rows found (missing required fields)")
            
            # Add to catalog
            n_added, n_skipped, n_conflicts, conflicts = self.catalog.add_records(df)
            
            # Save catalog
            self.catalog.save()
            
            # Log conflicts
            for conflict in conflicts:
                self.logger.warning(
                    f"Dimension conflict for {conflict['артикул']} ({conflict['бренд']})",
                    extra={'file': filename, 'conflict': conflict}
                )
            
            # Generate processed filename
            processed_name = generate_processed_filename(
                original_name=filename,
                n_records=n_valid_rows,
                file_hash=file_hash,
                is_error=False
            )
            
            # Move to processed directory
            dest_path = self.processed_dir / processed_name
            shutil.move(str(file_path), str(dest_path))
            
            # Add to registry
            self.registry.add_entry(
                file_hash=file_hash,
                original_name=filename,
                processed_name=processed_name,
                n_records=n_valid_rows,
                status='success'
            )
            
            # Write report
            processing_time = time.time() - start_time
            self.reporter.write_report(
                filename=filename,
                file_hash=file_hash,
                status='success',
                n_rows=n_rows,
                n_added=n_added,
                n_skipped=n_skipped,
                n_conflicts=n_conflicts,
                processing_time=processing_time
            )
            
            self.logger.info(
                f"Successfully processed {filename}: {n_added} added, {n_skipped} skipped, {n_conflicts} conflicts",
                extra={
                    'file': filename,
                    'sha': file_hash[:8],
                    'status': 'success',
                    'n_rows': n_rows,
                    'n_added': n_added,
                    'n_skipped': n_skipped,
                    'n_conflicts': n_conflicts
                }
            )
            
            return 'success', n_valid_rows
            
        except Exception as e:
            # Handle error
            error_msg = str(e)
            self.logger.error(f"Error processing {filename}: {error_msg}", exc_info=True)
            
            # Move to error directory
            try:
                file_hash = compute_file_hash(file_path)
            except Exception:
                file_hash = 'unknown'
            
            error_name = generate_processed_filename(
                original_name=filename,
                n_records=0,
                file_hash=file_hash,
                is_error=True,
                error_code='PARSE_ERROR'
            )
            
            dest_path = self.error_dir / error_name
            
            try:
                shutil.move(str(file_path), str(dest_path))
            except Exception:
                self.logger.error(f"Failed to move error file: {filename}")
            
            # Write error report
            processing_time = time.time() - start_time
            self.reporter.write_report(
                filename=filename,
                file_hash=file_hash,
                status='error',
                n_rows=0,
                n_added=0,
                n_skipped=0,
                n_conflicts=0,
                error_message=error_msg,
                processing_time=processing_time
            )
            
            return 'error', 0
    
    def process_inbox(self) -> Tuple[int, int, int]:
        """Process all files in inbox.
        
        Returns:
            Tuple of (n_processed, n_success, n_errors)
        """
        files = list(self.inbox_dir.glob('*'))
        files = [f for f in files if f.is_file() and not f.name.startswith('.')]
        
        n_processed = 0
        n_success = 0
        n_errors = 0
        
        for file_path in files:
            status, _ = self.process_file(file_path)
            n_processed += 1
            
            if status == 'success':
                n_success += 1
            elif status == 'error':
                n_errors += 1
        
        self.logger.info(
            f"Inbox processing complete: {n_processed} files, {n_success} success, {n_errors} errors"
        )
        
        return n_processed, n_success, n_errors
    
    def rebuild_catalog(self) -> Tuple[int, int]:
        """Rebuild catalog from processed files.
        
        Returns:
            Tuple of (n_files, n_records)
        """
        self.logger.info("Rebuilding catalog from processed files...")
        
        n_files, n_records = self.catalog.rebuild_from_processed(
            self.processed_dir,
            self.parser
        )
        
        self.logger.info(f"Catalog rebuilt: {n_files} files, {n_records} records")
        
        return n_files, n_records
