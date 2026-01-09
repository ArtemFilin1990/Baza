#!/usr/bin/env python3
"""Remove duplicate entries from nomenclature.csv based on unique key (Brand, Product Name)."""

import csv
import sys
from pathlib import Path
from collections import OrderedDict

REPO_ROOT = Path(__file__).resolve().parents[1]
NOMENCLATURE_FILE = REPO_ROOT / "data" / "nomenclature.csv"


def deduplicate_nomenclature(input_file: Path, output_file: Path) -> int:
    """Remove duplicates, keeping first occurrence of each unique key.
    
    Returns:
        Number of duplicates removed
    """
    seen_keys = OrderedDict()
    duplicates_count = 0
    
    with open(input_file, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        
        for row in reader:
            key = (row.get('Brand', ''), row.get('Product Name', ''))
            
            if key not in seen_keys:
                seen_keys[key] = row
            else:
                duplicates_count += 1
                print(f"Duplicate removed: {key}")
    
    # Write deduplicated data
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        
        for row in seen_keys.values():
            writer.writerow(row)
    
    return duplicates_count


def main():
    """Main entry point."""
    if not NOMENCLATURE_FILE.exists():
        print(f"Error: {NOMENCLATURE_FILE} not found", file=sys.stderr)
        sys.exit(1)
    
    print(f"Deduplicating {NOMENCLATURE_FILE}...")
    removed = deduplicate_nomenclature(NOMENCLATURE_FILE, NOMENCLATURE_FILE)
    
    print(f"\n✓ Deduplication complete!")
    print(f"  Duplicates removed: {removed}")
    print(f"  File updated: {NOMENCLATURE_FILE}")
    
    return 0 if removed >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())
