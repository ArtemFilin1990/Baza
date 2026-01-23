"""Normalization functions for text, brands, and numbers."""

import re
from typing import Optional

from app.config import Config
from app.utils import normalize_spaces


def normalize_text(text: str) -> str:
    """Normalize text by removing extra whitespace.

    Args:
        text: Input text

    Returns:
        Normalized text
    """
    if not text or not isinstance(text, str):
        return ""
    return normalize_spaces(text)


def normalize_brand(brand: str, config: Config) -> str:
    """Normalize brand name using aliases.

    Args:
        brand: Input brand name
        config: Configuration object

    Returns:
        Normalized brand name
    """
    if not brand or not isinstance(brand, str):
        return ""

    brand_clean = normalize_text(brand)
    brand_case = config.normalization.get("brand_case", "upper")

    # Check against aliases
    for canonical, aliases in config.brand_aliases.items():
        if brand_clean in aliases or brand_clean.upper() in [a.upper() for a in aliases]:
            return canonical if brand_case == "upper" else canonical.lower()

    # Return as-is with case normalization
    return brand_clean.upper() if brand_case == "upper" else brand_clean.lower()


def normalize_number(value: str) -> Optional[float]:
    """Normalize numeric value.

    Args:
        value: Input value (may contain comma as decimal separator)

    Returns:
        Float value or None if invalid
    """
    if not value or not isinstance(value, str):
        return None

    # Replace comma with dot for decimal separator
    value = value.strip().replace(",", ".")

    # Try to parse as float
    try:
        return float(value)
    except ValueError:
        return None


def normalize_dimension(value) -> Optional[float]:
    """Normalize dimension value (d, D, H).

    Args:
        value: Input value (string or number)

    Returns:
        Float value or None
    """
    if value is None or value == "":
        return None

    # If already a number, return it
    if isinstance(value, (int, float)):
        return float(value)

    # If string, normalize it
    if isinstance(value, str):
        return normalize_number(value)

    return None
