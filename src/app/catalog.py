"""Catalog management module."""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from app.config import Config
from app.normalization import normalize_brand, normalize_dimension, normalize_text
from app.utils import atomic_write


TARGET_COLUMNS = ["Наименование", "Артикул", "Аналог", "Бренд", "D", "d", "H", "m"]


def make_base_key(row: pd.Series) -> Tuple:
    """Create base key for conflict detection (without dimensions).

    Args:
        row: DataFrame row

    Returns:
        Tuple key for conflict detection
    """
    article = str(row.get("Артикул", "")).strip()
    brand = str(row.get("Бренд", "")).strip()

    if brand:
        return (article, brand)
    else:
        return (article,)


def make_dedup_key(row: pd.Series) -> Tuple:
    """Create deduplication key from a row.

    Key logic:
    - If brand is filled: (Артикул, Бренд, D, d, H)
    - If brand is empty: (Артикул, D, d, H)

    Args:
        row: DataFrame row

    Returns:
        Tuple key for deduplication
    """
    article = str(row.get("Артикул", "")).strip()
    brand = str(row.get("Бренд", "")).strip()
    d = row.get("d")
    D = row.get("D")
    H = row.get("H")

    if brand:
        return (article, brand, d, D, H)
    else:
        return (article, d, D, H)


def load_catalog(catalog_path: Path) -> pd.DataFrame:
    """Load existing catalog from CSV.

    Args:
        catalog_path: Path to catalog CSV file

    Returns:
        DataFrame with catalog data
    """
    if not catalog_path.exists():
        return pd.DataFrame(columns=TARGET_COLUMNS)

    df = pd.read_csv(catalog_path, dtype=str, keep_default_na=False)

    # Ensure all target columns exist
    for col in TARGET_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    # Convert dimension columns to float
    for dim_col in ["D", "d", "H", "m"]:
        df[dim_col] = pd.to_numeric(df[dim_col], errors="coerce")

    return df[TARGET_COLUMNS]


def merge_catalog(
    existing: pd.DataFrame, new_data: pd.DataFrame, config: Config
) -> Tuple[pd.DataFrame, Dict[str, int], List[Dict]]:
    """Merge new data into existing catalog with deduplication.

    Args:
        existing: Existing catalog DataFrame
        new_data: New data DataFrame
        config: Configuration object

    Returns:
        Tuple of (merged_df, stats, conflicts)
        - merged_df: Merged DataFrame
        - stats: Dictionary with 'added', 'skipped', 'conflicts' counts
        - conflicts: List of conflict records
    """
    stats = {"added": 0, "skipped": 0, "conflicts": 0}
    conflicts = []

    # Ensure new_data has all target columns
    for col in TARGET_COLUMNS:
        if col not in new_data.columns:
            new_data[col] = ""

    new_data = new_data[TARGET_COLUMNS].copy()

    # Build index of existing records by both base key and full key
    existing_keys = {}  # Full dedup key -> index
    existing_base_keys = {}  # Base key -> list of indices

    for idx, row in existing.iterrows():
        key = make_dedup_key(row)
        base_key = make_base_key(row)
        existing_keys[key] = idx

        if base_key not in existing_base_keys:
            existing_base_keys[base_key] = []
        existing_base_keys[base_key].append(idx)

    # Process new records
    rows_to_add = []

    for _, new_row in new_data.iterrows():
        new_key = make_dedup_key(new_row)
        new_base_key = make_base_key(new_row)

        if new_key in existing_keys:
            # Exact duplicate - skip
            stats["skipped"] += 1
        elif new_base_key in existing_base_keys:
            # Same article+brand but different dimensions - potential conflict
            has_conflict = False

            # Check if any existing record with same base key has different dimensions
            for existing_idx in existing_base_keys[new_base_key]:
                existing_row = existing.iloc[existing_idx]

                for dim_col in ["D", "d", "H"]:
                    existing_val = existing_row[dim_col]
                    new_val = new_row[dim_col]

                    # Check if both are non-null and different
                    if pd.notna(existing_val) and pd.notna(new_val) and existing_val != new_val:
                        has_conflict = True
                        break

                if has_conflict:
                    break

            if has_conflict:
                # Add the new record
                rows_to_add.append(new_row)
                stats["conflicts"] += 1
                # Use the first existing record for comparison in the conflict report
                existing_row = existing.iloc[existing_base_keys[new_base_key][0]]
                conflicts.append(
                    {
                        "article": str(new_row.get("Артикул", "")),
                        "brand": str(new_row.get("Бренд", "")),
                        "existing_d": float(existing_row.get("d")) if pd.notna(existing_row.get("d")) else None,
                        "existing_D": float(existing_row.get("D")) if pd.notna(existing_row.get("D")) else None,
                        "existing_H": float(existing_row.get("H")) if pd.notna(existing_row.get("H")) else None,
                        "new_d": float(new_row.get("d")) if pd.notna(new_row.get("d")) else None,
                        "new_D": float(new_row.get("D")) if pd.notna(new_row.get("D")) else None,
                        "new_H": float(new_row.get("H")) if pd.notna(new_row.get("H")) else None,
                    }
                )
                # Update indices
                new_idx = len(existing) + len(rows_to_add) - 1
                existing_keys[new_key] = new_idx
                existing_base_keys[new_base_key].append(new_idx)
            else:
                # Same article+brand with same dimensions - skip
                stats["skipped"] += 1
        else:
            # New record
            rows_to_add.append(new_row)
            new_idx = len(existing) + len(rows_to_add) - 1
            existing_keys[new_key] = new_idx
            if new_base_key not in existing_base_keys:
                existing_base_keys[new_base_key] = []
            existing_base_keys[new_base_key].append(new_idx)
            stats["added"] += 1

    # Concatenate
    if rows_to_add:
        merged = pd.concat([existing, pd.DataFrame(rows_to_add)], ignore_index=True)
    else:
        merged = existing.copy()

    return merged, stats, conflicts


def write_catalog(catalog_df: pd.DataFrame, output_dir: Path):
    """Write catalog to CSV and JSON files.

    Args:
        catalog_df: Catalog DataFrame
        output_dir: Output directory
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV
    csv_path = output_dir / "catalog_target.csv"
    csv_content = catalog_df.to_csv(index=False, encoding="utf-8")
    atomic_write(csv_path, csv_content, mode="w", encoding="utf-8")

    # Write JSON
    json_path = output_dir / "catalog_target.json"
    records = catalog_df.to_dict(orient="records")

    # Convert NaN to None for JSON
    for record in records:
        for key, value in record.items():
            if pd.isna(value):
                record[key] = None

    json_content = json.dumps(records, ensure_ascii=False, indent=2)
    atomic_write(json_path, json_content, mode="w", encoding="utf-8")
