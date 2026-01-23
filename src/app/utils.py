"""Utility functions for the automation pipeline."""

import hashlib
import os
import re
import tempfile
from pathlib import Path
from typing import Union


def sha256_file(filepath: Union[str, Path]) -> str:
    """Calculate SHA256 hash of a file.

    Args:
        filepath: Path to the file

    Returns:
        Hexadecimal SHA256 hash
    """
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def slugify(text: str) -> str:
    """Convert text to a URL-safe slug.

    Args:
        text: Input text

    Returns:
        Slugified text
    """
    # Convert to lowercase and replace spaces with underscores
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "_", text)
    return text.strip("_")


def atomic_write(filepath: Union[str, Path], content: Union[str, bytes], mode: str = "w", encoding: str = "utf-8"):
    """Write to a file atomically using temp file and rename.

    Args:
        filepath: Destination file path
        content: Content to write
        mode: Write mode ('w' for text, 'wb' for binary)
        encoding: Text encoding (used only for text mode)
    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Create temp file in the same directory
    fd, temp_path = tempfile.mkstemp(dir=filepath.parent, prefix=".tmp_", suffix=filepath.suffix)

    try:
        if "b" in mode:
            os.write(fd, content)
        else:
            os.write(fd, content.encode(encoding))
        os.close(fd)

        # Atomic rename
        os.replace(temp_path, filepath)
    except Exception:
        os.close(fd)
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise


def normalize_spaces(text: str) -> str:
    """Normalize whitespace in text.

    Args:
        text: Input text

    Returns:
        Text with normalized whitespace
    """
    if not text:
        return ""
    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)
    # Strip leading and trailing whitespace
    return text.strip()
