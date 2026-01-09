#!/usr/bin/env python3
"""Deduplicate nomenclature.csv by removing duplicate (Brand, Product Name) keys.

Keeps the first occurrence of each unique key and removes all duplicates.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOMENCLATURE_CSV = REPO_ROOT / "data" / "nomenclature.csv"


def deduplicate_nomenclature() -> int:
    """Remove duplicate entries from nomenclature.csv, keeping first occurrence.
    
    Returns:
        Number of duplicate rows removed
    """
    if not NOMENCLATURE_CSV.exists():
        raise FileNotFoundError(f"File not found: {NOMENCLATURE_CSV}")
    
    # Read all rows
    with NOMENCLATURE_CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        if fieldnames is None:
            raise ValueError("CSV file has no header")
        
        rows = list(reader)
    
    # Track seen keys and keep only first occurrence
    seen_keys = set()
    unique_rows = []
    duplicates_removed = 0
    
    for row in rows:
        try:
            key = (row["Brand"], row["Product Name"])
        except KeyError as e:
            print(f"⚠️  Warning: Missing column {e} in row, skipping")
            continue
        
        if key not in seen_keys:
            seen_keys.add(key)
            unique_rows.append(row)
        else:
            duplicates_removed += 1
    
    # Sort by Brand, then Product Name
    unique_rows.sort(key=lambda r: (r["Brand"], r["Product Name"]))
    
    # Write back to file
    with NOMENCLATURE_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows)
    
    return duplicates_removed


def main() -> None:
    removed = deduplicate_nomenclature()
    print(f"✓ Removed {removed:,} duplicate rows from {NOMENCLATURE_CSV.name}")
    print(f"✓ File saved with unique entries only")


if __name__ == "__main__":
    main()
