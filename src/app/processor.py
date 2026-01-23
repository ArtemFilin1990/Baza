"""Main file processing logic."""

import logging
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from app.catalog import load_catalog, merge_catalog, write_catalog
from app.config import Config
from app.normalization import normalize_brand, normalize_dimension, normalize_text
from app.parsing import extract_article_from_name, extract_dimensions_from_text, parse_file, recognize_columns
from app.registry import Registry
from app.report import ReportWriter
from app.utils import sha256_file, slugify

logger = logging.getLogger(__name__)


def normalize_row(row: pd.Series, column_mapping: Dict[str, str], config: Config) -> Dict:
    """Normalize a single row to target schema.

    Args:
        row: Input DataFrame row
        column_mapping: Mapping from target columns to actual columns
        config: Configuration object

    Returns:
        Dictionary with normalized values
    """
    result = {
        "Наименование": "",
        "Артикул": "",
        "Аналог": "",
        "Бренд": "",
        "D": None,
        "d": None,
        "H": None,
        "m": None,
    }

    # Map direct columns
    for target_col in ["Наименование", "Артикул", "Аналог", "Бренд"]:
        if target_col in column_mapping:
            actual_col = column_mapping[target_col]
            value = row.get(actual_col, "")
            if pd.notna(value):
                result[target_col] = normalize_text(str(value))

    # Normalize brand
    if result["Бренд"]:
        result["Бренд"] = normalize_brand(result["Бренд"], config)

    # Extract article from name if not present
    if not result["Артикул"] and result["Наименование"]:
        article = extract_article_from_name(result["Наименование"], config)
        if article:
            result["Артикул"] = article

    # Map dimensions
    for dim_col in ["D", "d", "H", "m"]:
        if dim_col in column_mapping:
            actual_col = column_mapping[dim_col]
            value = row.get(actual_col)
            if pd.notna(value):
                result[dim_col] = normalize_dimension(value)

    # Extract dimensions from name if missing
    if result["Наименование"] and (result["d"] is None or result["D"] is None or result["H"] is None):
        extracted = extract_dimensions_from_text(result["Наименование"], config)
        if result["d"] is None:
            result["d"] = extracted.get("d")
        if result["D"] is None:
            result["D"] = extracted.get("D")
        if result["H"] is None:
            result["H"] = extracted.get("H")

    return result


def process_dataframe(df: pd.DataFrame, config: Config) -> pd.DataFrame:
    """Process a DataFrame to target schema.

    Args:
        df: Input DataFrame
        config: Configuration object

    Returns:
        Normalized DataFrame
    """
    # Recognize columns
    column_mapping = recognize_columns(df, config)

    # Normalize each row
    normalized_rows = []
    for _, row in df.iterrows():
        normalized = normalize_row(row, column_mapping, config)
        normalized_rows.append(normalized)

    return pd.DataFrame(normalized_rows)


def generate_processed_filename(
    original_filename: str, n_records: int, sha256: str, error_code: Optional[str] = None
) -> str:
    """Generate normalized filename for processed files.

    Format: YYYYMMDD_HHMMSS__<source>__<n_records>__<sha256_8>[__ERROR__<code>].<ext>

    Args:
        original_filename: Original filename
        n_records: Number of records in file
        sha256: SHA256 hash of the file
        error_code: Optional error code

    Returns:
        Generated filename
    """
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    path = Path(original_filename)
    source = slugify(path.stem)
    sha256_short = sha256[:8]
    ext = path.suffix

    if error_code:
        return f"{timestamp}__{source}__{n_records}__{sha256_short}__ERROR__{error_code}{ext}"
    else:
        return f"{timestamp}__{source}__{n_records}__{sha256_short}{ext}"


def process_file(filepath: Path, config: Config, registry: Registry, report: ReportWriter) -> bool:
    """Process a single file.

    Args:
        filepath: Path to file
        config: Configuration object
        registry: File registry
        report: Report writer

    Returns:
        True if successful, False otherwise
    """
    try:
        # Calculate hash
        sha256 = sha256_file(filepath)

        # Check if already processed
        if registry.is_processed(sha256):
            logger.info(f"File {filepath.name} already processed (sha256={sha256[:8]}), skipping")
            report.write_entry(
                filename=filepath.name, sha256=sha256, status="skipped", n_rows=0, error="Already processed"
            )
            return True

        # Check file size
        max_size_mb = config.limits.get("max_file_size_mb", 50)
        file_size_mb = filepath.stat().st_size / (1024 * 1024)
        if file_size_mb > max_size_mb:
            error_msg = f"File too large: {file_size_mb:.2f}MB > {max_size_mb}MB"
            logger.error(f"File {filepath.name}: {error_msg}")
            report.write_entry(filename=filepath.name, sha256=sha256, status="error", error=error_msg)

            # Move to error
            error_dir = Path(config.paths["error"])
            error_dir.mkdir(parents=True, exist_ok=True)
            new_filename = generate_processed_filename(filepath.name, 0, sha256, error_code="SIZE")
            shutil.move(str(filepath), str(error_dir / new_filename))
            return False

        # Parse file
        logger.info(f"Processing file: {filepath.name}")
        df = parse_file(filepath, config)

        if df.empty:
            error_msg = "No data found in file"
            logger.error(f"File {filepath.name}: {error_msg}")
            report.write_entry(filename=filepath.name, sha256=sha256, status="error", error=error_msg)

            # Move to error
            error_dir = Path(config.paths["error"])
            error_dir.mkdir(parents=True, exist_ok=True)
            new_filename = generate_processed_filename(filepath.name, 0, sha256, error_code="EMPTY")
            shutil.move(str(filepath), str(error_dir / new_filename))
            return False

        n_rows = len(df)

        # Normalize data
        normalized_df = process_dataframe(df, config)

        # Load existing catalog
        out_dir = Path(config.paths["out"])
        catalog_path = out_dir / "catalog_target.csv"
        existing_catalog = load_catalog(catalog_path)

        # Merge
        merged_catalog, stats, conflicts = merge_catalog(existing_catalog, normalized_df, config)

        # Write catalog
        write_catalog(merged_catalog, out_dir)

        # Mark as processed
        registry.mark_processed(sha256)

        # Write report
        report.write_entry(
            filename=filepath.name,
            sha256=sha256,
            status="success",
            n_rows=n_rows,
            n_added=stats["added"],
            n_skipped=stats["skipped"],
            n_conflicts=stats["conflicts"],
            conflicts=conflicts if conflicts else None,
        )

        logger.info(
            f"File {filepath.name} processed: {n_rows} rows, "
            f"{stats['added']} added, {stats['skipped']} skipped, {stats['conflicts']} conflicts"
        )

        # Move to processed
        processed_dir = Path(config.paths["processed"])
        processed_dir.mkdir(parents=True, exist_ok=True)
        new_filename = generate_processed_filename(filepath.name, n_rows, sha256)
        shutil.move(str(filepath), str(processed_dir / new_filename))

        return True

    except Exception as e:
        logger.error(f"Error processing file {filepath.name}: {e}", exc_info=True)
        sha256 = sha256_file(filepath) if filepath.exists() else "unknown"
        report.write_entry(filename=filepath.name, sha256=sha256, status="error", error=str(e))

        # Move to error
        try:
            error_dir = Path(config.paths["error"])
            error_dir.mkdir(parents=True, exist_ok=True)
            new_filename = generate_processed_filename(filepath.name, 0, sha256, error_code="PROC")
            shutil.move(str(filepath), str(error_dir / new_filename))
        except Exception as move_error:
            logger.error(f"Failed to move file to error: {move_error}")

        return False


def process_once(config: Config):
    """Process all files in inbox once.

    Args:
        config: Configuration object
    """
    inbox_dir = Path(config.paths["inbox"])
    out_dir = Path(config.paths["out"])
    registry_path = out_dir / "processed_registry.json"
    report_path = out_dir / "run_report.ndjson"

    registry = Registry(registry_path)
    report = ReportWriter(report_path)

    # Process all files
    if not inbox_dir.exists():
        logger.warning(f"Inbox directory does not exist: {inbox_dir}")
        return

    files = sorted(inbox_dir.glob("*"))
    files = [f for f in files if f.is_file()]

    logger.info(f"Found {len(files)} files in inbox")

    for filepath in files:
        process_file(filepath, config, registry, report)


def rebuild_catalog(config: Config):
    """Rebuild catalog from processed files.

    Args:
        config: Configuration object
    """
    processed_dir = Path(config.paths["processed"])
    out_dir = Path(config.paths["out"])
    catalog_path = out_dir / "catalog_target.csv"

    # Clear existing catalog
    if catalog_path.exists():
        catalog_path.unlink()

    # Clear registry
    registry_path = out_dir / "processed_registry.json"
    if registry_path.exists():
        registry_path.unlink()

    registry = Registry(registry_path)
    report_path = out_dir / "run_report.ndjson"

    # Clear report
    if report_path.exists():
        report_path.unlink()

    report = ReportWriter(report_path)

    # Process all files in processed directory
    if not processed_dir.exists():
        logger.warning(f"Processed directory does not exist: {processed_dir}")
        return

    files = sorted(processed_dir.glob("*"))
    files = [f for f in files if f.is_file() and not f.name.startswith("__ERROR__")]

    logger.info(f"Rebuilding catalog from {len(files)} files")

    # Temporarily move files to inbox for processing
    inbox_dir = Path(config.paths["inbox"])
    inbox_dir.mkdir(parents=True, exist_ok=True)

    temp_files = []
    for filepath in files:
        temp_path = inbox_dir / filepath.name
        shutil.copy(str(filepath), str(temp_path))
        temp_files.append(temp_path)

    # Process files
    for temp_path in temp_files:
        # For rebuild, we don't check registry
        original_registry_check = registry.is_processed
        registry.is_processed = lambda x: False  # Skip registry check

        process_file(temp_path, config, registry, report)

        registry.is_processed = original_registry_check

    logger.info("Catalog rebuild complete")
