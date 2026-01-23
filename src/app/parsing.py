"""Parsing module for reading CSV/XLSX/JSON/TXT/MD files."""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

from app.config import Config
from app.normalization import normalize_dimension, normalize_text


def recognize_column(header: str, target: str, patterns: Dict[str, List[str]]) -> bool:
    """Check if a column header matches a target column pattern.

    Args:
        header: Column header to check
        target: Target column name (e.g., 'Артикул', 'Бренд')
        patterns: Dictionary of column patterns

    Returns:
        True if header matches any pattern for the target
    """
    if target not in patterns:
        return False

    header_clean = header.strip()
    header_lower = header_clean.lower()

    for pattern in patterns[target]:
        # For exact single-letter matches (d, D, H, B), check directly
        if pattern in ["\\bd\\b", "\\bD\\b", "\\bH\\b", "\\bB\\b"]:
            letter = pattern[2]  # Extract the letter from \bX\b
            if header_clean == letter or header_clean == letter.lower() or header_clean == letter.upper():
                return True
        else:
            # Try regex match (case-insensitive)
            if re.search(pattern, header_lower, re.IGNORECASE):
                return True

    return False


def recognize_columns(df: pd.DataFrame, config: Config) -> Dict[str, str]:
    """Recognize column mappings in a DataFrame.

    Args:
        df: Input DataFrame
        config: Configuration object

    Returns:
        Dictionary mapping target columns to actual column names
    """
    column_patterns = config.parsing_rules.get("column_patterns", {})
    mapping = {}

    target_columns = ["Наименование", "Артикул", "Аналог", "Бренд", "D", "d", "H", "m"]

    # First pass: exact matches (case-sensitive for single letters)
    for target in target_columns:
        if target in ["d", "D", "H", "B", "m"]:
            # For dimension columns, look for exact match first
            for col in df.columns:
                col_str = str(col).strip()
                if col_str == target:
                    mapping[target] = col
                    break

    # Second pass: pattern matches for unmapped targets
    for target in target_columns:
        if target in mapping:
            continue  # Already mapped

        for col in df.columns:
            if col in mapping.values():
                continue  # Column already used

            if recognize_column(str(col), target, column_patterns):
                mapping[target] = col
                break

    return mapping


def extract_dimensions_from_text(text: str, config: Config) -> Dict[str, Optional[float]]:
    """Extract dimensions (d, D, H) from text using pattern matching.

    Args:
        text: Input text (e.g., "Подшипник 20x47x14")
        config: Configuration object

    Returns:
        Dictionary with extracted dimensions
    """
    pattern = config.parsing_rules.get("size_pattern", "")
    if not pattern:
        return {"d": None, "D": None, "H": None}

    match = re.search(pattern, text)
    if match:
        return {
            "d": normalize_dimension(match.group("d")),
            "D": normalize_dimension(match.group("D")),
            "H": normalize_dimension(match.group("H")),
        }

    return {"d": None, "D": None, "H": None}


def extract_article_from_name(name: str, config: Config) -> Optional[str]:
    """Extract article code from name if pattern matches.

    Args:
        name: Product name
        config: Configuration object

    Returns:
        Extracted article or None
    """
    if not config.parsing.get("allow_first_token_as_article", False):
        return None

    pattern = config.parsing_rules.get("article_first_token_pattern", "")
    if not pattern:
        return None

    match = re.match(pattern, name.strip())
    if match:
        return match.group(0)

    return None


def read_csv(filepath: Path, config: Config) -> pd.DataFrame:
    """Read CSV file.

    Args:
        filepath: Path to CSV file
        config: Configuration object

    Returns:
        DataFrame with parsed data
    """
    # Try different encodings
    for encoding in ["utf-8", "cp1251", "latin1"]:
        try:
            df = pd.read_csv(filepath, encoding=encoding)
            return df
        except (UnicodeDecodeError, pd.errors.ParserError):
            continue

    # Fallback to default
    return pd.read_csv(filepath)


def read_xlsx(filepath: Path, config: Config) -> pd.DataFrame:
    """Read XLSX file.

    Args:
        filepath: Path to XLSX file
        config: Configuration object

    Returns:
        DataFrame with parsed data
    """
    return pd.read_excel(filepath, engine="openpyxl")


def read_json(filepath: Path, config: Config) -> pd.DataFrame:
    """Read JSON file.

    Args:
        filepath: Path to JSON file
        config: Configuration object

    Returns:
        DataFrame with parsed data
    """
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    # Handle both list and dict formats
    if isinstance(data, list):
        return pd.DataFrame(data)
    elif isinstance(data, dict):
        # If dict has a key with list of records
        for key in ["data", "records", "items", "bearings"]:
            if key in data and isinstance(data[key], list):
                return pd.DataFrame(data[key])
        # Otherwise treat as single record
        return pd.DataFrame([data])

    return pd.DataFrame()


def read_txt(filepath: Path, config: Config) -> pd.DataFrame:
    """Read TXT file (assume tab or comma separated).

    Args:
        filepath: Path to TXT file
        config: Configuration object

    Returns:
        DataFrame with parsed data
    """
    # Try as CSV first
    try:
        return read_csv(filepath, config)
    except Exception:
        pass

    # Try tab-separated
    for encoding in ["utf-8", "cp1251", "latin1"]:
        try:
            df = pd.read_csv(filepath, sep="\t", encoding=encoding)
            return df
        except Exception:
            continue

    return pd.DataFrame()


def read_md(filepath: Path, config: Config) -> pd.DataFrame:
    """Read Markdown file with tables.

    Args:
        filepath: Path to MD file
        config: Configuration object

    Returns:
        DataFrame with parsed data
    """
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # Look for markdown tables (simple parser)
    # This is a basic implementation - may need improvement
    lines = content.split("\n")
    table_lines = []
    in_table = False

    for line in lines:
        if "|" in line:
            in_table = True
            table_lines.append(line)
        elif in_table and not line.strip():
            break

    if not table_lines:
        return pd.DataFrame()

    # Parse table lines
    rows = []
    headers = None

    for i, line in enumerate(table_lines):
        cells = [cell.strip() for cell in line.split("|")]
        cells = [c for c in cells if c]  # Remove empty cells

        if i == 0:
            headers = cells
        elif i == 1:
            # Skip separator line
            continue
        else:
            if len(cells) == len(headers):
                rows.append(cells)

    if headers and rows:
        return pd.DataFrame(rows, columns=headers)

    return pd.DataFrame()


def parse_file(filepath: Path, config: Config) -> pd.DataFrame:
    """Parse file based on extension.

    Args:
        filepath: Path to file
        config: Configuration object

    Returns:
        DataFrame with parsed data
    """
    suffix = filepath.suffix.lower()

    if suffix == ".csv":
        return read_csv(filepath, config)
    elif suffix in [".xlsx", ".xls"]:
        return read_xlsx(filepath, config)
    elif suffix == ".json":
        return read_json(filepath, config)
    elif suffix == ".txt":
        return read_txt(filepath, config)
    elif suffix == ".md":
        return read_md(filepath, config)
    else:
        raise ValueError(f"Unsupported file format: {suffix}")
