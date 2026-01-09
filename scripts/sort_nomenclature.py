#!/usr/bin/env python3
"""Sort nomenclature.csv file by Brand and Product Name columns."""

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOMENCLATURE_FILE = REPO_ROOT / "data" / "nomenclature.csv"


def sort_nomenclature(input_file: Path, output_file: Path) -> None:
    """Sort nomenclature CSV by Brand (column 0) and Product Name (column 1)."""
    with open(input_file, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    
    # Sort by Brand (column 0), then Product Name (column 1)
    rows_sorted = sorted(rows, key=lambda r: (r[0], r[1]))
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows_sorted)
    
    print(f"Sorted {len(rows)} rows in {input_file.name}")


def verify_sorting(file_path: Path) -> bool:
    """Verify that nomenclature file is sorted correctly."""
    with open(file_path, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    
    for i in range(1, len(rows)):
        prev_key = (rows[i-1][0], rows[i-1][1])
        curr_key = (rows[i][0], rows[i][1])
        if prev_key > curr_key:
            print(f"ERROR: Sorting violation at line {i+2}: {curr_key} should come before {prev_key}")
            return False
    
    print(f"OK: {file_path.name} is correctly sorted")
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--verify":
        # Verification mode
        if not verify_sorting(NOMENCLATURE_FILE):
            sys.exit(1)
    else:
        # Sort mode
        sort_nomenclature(NOMENCLATURE_FILE, NOMENCLATURE_FILE)
        verify_sorting(NOMENCLATURE_FILE)
