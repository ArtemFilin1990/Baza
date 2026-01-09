#!/usr/bin/env python3
"""Remove duplicate entries from nomenclature.csv based on unique key (Brand, Product Name)."""

import csv
import os
import sys
import tempfile
from collections import OrderedDict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOMENCLATURE_FILE = REPO_ROOT / "data" / "nomenclature.csv"


def deduplicate_nomenclature(input_file: Path, output_file: Path) -> int:
    """Remove duplicates, keeping first occurrence of each unique key.
    
    Returns:
        Number of duplicates removed
    """
    with open(input_file, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        
        if not header or 'Brand' not in header or 'Product Name' not in header:
            print("ERROR: CSV must have 'Brand' and 'Product Name' columns", file=sys.stderr)
            sys.exit(1)
        
        # Use OrderedDict to preserve first occurrence
        unique_rows = OrderedDict()
        duplicates = []
        
        for line_num, row in enumerate(reader, start=2):
            brand = row.get('Brand', '').strip()
            product_name = row.get('Product Name', '').strip()
            key = (brand, product_name)
            
            if key in unique_rows:
                duplicates.append((line_num, key))
            else:
                unique_rows[key] = row
    
    # Write to a temporary file first, then atomically replace
    fd, temp_path = tempfile.mkstemp(dir=output_file.parent, suffix='.csv', text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(unique_rows.values())
        
        # Atomically replace the original file
        os.replace(temp_path, output_file)
    except Exception:
        # Clean up temp file on error
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        raise
    
    # Report
    total_original = len(unique_rows) + len(duplicates)
    print(f"📊 Статистика дедупликации {input_file.name}:")
    print(f"  Исходных записей: {total_original}")
    print(f"  Уникальных записей: {len(unique_rows)}")
    print(f"  Удалено дубликатов: {len(duplicates)}")
    
    if duplicates:
        print("\n⚠️  Найдены и удалены дубликаты:")
        for line_num, key in sorted(duplicates)[:10]:  # Show first 10
            print(f"  Строка {line_num}: {key}")
        if len(duplicates) > 10:
            print(f"  ... и ещё {len(duplicates) - 10}")
    
    return len(duplicates)


if __name__ == "__main__":
    removed = deduplicate_nomenclature(NOMENCLATURE_FILE, NOMENCLATURE_FILE)
    if removed > 0:
        print(f"\n✅ Файл {NOMENCLATURE_FILE.name} очищен от {removed} дубликатов")
        sys.exit(0)
    else:
        print(f"\n✅ Файл {NOMENCLATURE_FILE.name} не содержит дубликатов")
        sys.exit(0)
