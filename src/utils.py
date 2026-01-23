"""Utility functions for file handling, hashing, and normalization."""

import hashlib
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA256 hash of a file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        SHA256 hash as hex string
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_short_hash(full_hash: str, length: int = 8) -> str:
    """Get short version of hash.
    
    Args:
        full_hash: Full hash string
        length: Length of short hash
        
    Returns:
        First N characters of hash
    """
    return full_hash[:length]


def make_safe_filename(text: str, max_length: int = 50) -> str:
    """Convert text to safe filename slug.
    
    Args:
        text: Original text
        max_length: Maximum length of result
        
    Returns:
        Safe filename string
    """
    # Remove extension if present
    name_part = Path(text).stem
    
    # Replace special characters with underscore
    safe = re.sub(r'[^\w\s-]', '_', name_part)
    # Replace whitespace with underscore
    safe = re.sub(r'[\s]+', '_', safe)
    # Remove multiple underscores
    safe = re.sub(r'_+', '_', safe)
    # Strip leading/trailing underscores
    safe = safe.strip('_')
    
    # Truncate if too long
    if len(safe) > max_length:
        safe = safe[:max_length].rstrip('_')
    
    return safe or 'file'


def generate_processed_filename(
    original_name: str,
    n_records: int,
    file_hash: str,
    is_error: bool = False,
    error_code: Optional[str] = None
) -> str:
    """Generate normalized filename for processed files.
    
    Format: YYYYMMDD_HHMMSS__<source>__<n_records>__<sha256_8>[__ERROR__<code>].<ext>
    
    Args:
        original_name: Original filename
        n_records: Number of records processed
        file_hash: File hash (SHA256)
        is_error: Whether this is an error file
        error_code: Error code if applicable
        
    Returns:
        New filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    source = make_safe_filename(original_name)
    short_hash = get_short_hash(file_hash)
    ext = Path(original_name).suffix or '.txt'
    
    parts = [
        timestamp,
        source,
        f"{n_records}",
        short_hash
    ]
    
    if is_error:
        error_suffix = f"ERROR_{error_code}" if error_code else "ERROR"
        parts.append(error_suffix)
    
    return "__".join(parts) + ext


def normalize_text(text: str, config: Optional[Dict[str, Any]] = None) -> str:
    """Normalize text according to configuration.
    
    Args:
        text: Text to normalize
        config: Normalization configuration
        
    Returns:
        Normalized text
    """
    if not isinstance(text, str):
        return str(text) if text is not None else ""
    
    result = text
    
    # Trim
    result = result.strip()
    
    # Collapse multiple spaces
    result = re.sub(r'\s+', ' ', result)
    
    # Remove control characters
    result = ''.join(char for char in result if ord(char) >= 32 or char in '\n\r\t')
    
    # Apply dimension replacements if provided
    if config and 'dimension_replacements' in config:
        for old, new in config['dimension_replacements'].items():
            result = result.replace(old, new)
    
    return result


def normalize_number(value: Any, decimal_sep: str = '.') -> Optional[float]:
    """Normalize numeric value.
    
    Args:
        value: Value to normalize
        decimal_sep: Decimal separator to use
        
    Returns:
        Normalized float or None if cannot convert
    """
    if value is None or value == '':
        return None
    
    if isinstance(value, (int, float)):
        return float(value)
    
    if isinstance(value, str):
        # Remove spaces
        cleaned = value.strip().replace(' ', '')
        # Replace comma with decimal point
        cleaned = cleaned.replace(',', '.')
        
        try:
            return float(cleaned)
        except ValueError:
            return None
    
    return None


def normalize_brand(brand: str, aliases: Dict[str, str], format_type: str = 'upper') -> str:
    """Normalize brand name.
    
    Args:
        brand: Brand name to normalize
        aliases: Brand aliases mapping
        format_type: Format type - 'upper' or 'title'
        
    Returns:
        Normalized brand name
    """
    if not isinstance(brand, str) or not brand:
        return ""
    
    # Trim and normalize spaces
    normalized = normalize_text(brand)
    
    # Check aliases
    if normalized in aliases:
        normalized = aliases[normalized]
    elif normalized.lower() in aliases:
        normalized = aliases[normalized.lower()]
    
    # Apply format
    if format_type == 'upper':
        normalized = normalized.upper()
    elif format_type == 'title':
        normalized = normalized.title()
    
    return normalized


def detect_file_type(file_path: Path) -> str:
    """Detect file type based on extension.
    
    Args:
        file_path: Path to file
        
    Returns:
        File type: 'csv', 'xlsx', 'json', 'txt', or 'unknown'
    """
    ext = file_path.suffix.lower()
    
    if ext == '.csv':
        return 'csv'
    elif ext in ['.xlsx', '.xls']:
        return 'xlsx'
    elif ext == '.json':
        return 'json'
    elif ext in ['.txt', '.md']:
        return 'txt'
    else:
        return 'unknown'


def ensure_directory(path: Path) -> None:
    """Ensure directory exists, create if not.
    
    Args:
        path: Directory path
    """
    path.mkdir(parents=True, exist_ok=True)


def atomic_write(content: str, file_path: Path) -> None:
    """Write content to file atomically.
    
    Args:
        content: Content to write
        file_path: Destination file path
    """
    temp_path = file_path.with_suffix(file_path.suffix + '.tmp')
    
    try:
        # Write to temporary file
        temp_path.write_text(content, encoding='utf-8')
        # Rename (atomic on most systems)
        temp_path.replace(file_path)
    except Exception:
        # Clean up temp file on error
        if temp_path.exists():
            temp_path.unlink()
        raise
