#!/usr/bin/env python3
"""
Скрипт для проверки и анализа источников данных в репозитории Baza.
Script to check and analyze data sources in the Baza repository.

Usage:
    python scripts/check_data_sources.py
"""

import csv
import os
from pathlib import Path
from typing import Dict, List, Tuple

# Constants for data quality thresholds
SMALL_FILE_THRESHOLD = 10  # Files with fewer records
SMALL_FILE_DISPLAY_THRESHOLD = 50  # Show headers for files with fewer records
LARGE_FILE_THRESHOLD = 50000  # Files that might need splitting


def analyze_csv_structure(file_path: Path) -> Tuple[int, List[str]]:
    """Analyze CSV file structure and return row count and columns."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            row_count = sum(1 for _ in reader)
            return row_count, headers
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return 0, []


def scan_data_directory(data_dir: Path) -> Dict[str, Dict]:
    """Scan data directory and return statistics."""
    results = {}

    for csv_file in data_dir.rglob("*.csv"):
        rel_path = csv_file.relative_to(data_dir)
        row_count, headers = analyze_csv_structure(csv_file)

        results[str(rel_path)] = {
            "rows": row_count,
            "columns": len(headers),
            "headers": headers,
            "size_kb": csv_file.stat().st_size / 1024,
        }

    return results


def print_statistics(stats: Dict[str, Dict]):
    """Print formatted statistics."""
    print("=" * 80)
    print("СТАТИСТИКА ДАННЫХ / DATA STATISTICS")
    print("=" * 80)
    print()

    # Group by category
    categories = {}
    for file_path, data in stats.items():
        category = file_path.split("/")[0] if "/" in file_path else "root"
        if category not in categories:
            categories[category] = []
        categories[category].append((file_path, data))

    total_rows = 0
    total_files = 0

    for category, files in sorted(categories.items()):
        print(f"\n📁 {category.upper()}")
        print("-" * 80)

        category_rows = 0
        for file_path, data in sorted(files):
            print(f"  📄 {file_path}")
            print(f"     Строк/Rows: {data['rows']:,}")
            print(f"     Столбцов/Columns: {data['columns']}")
            print(f"     Размер/Size: {data['size_kb']:.2f} KB")
            if data["rows"] < SMALL_FILE_DISPLAY_THRESHOLD:  # Show headers for small files
                print(f"     Заголовки: {', '.join(data['headers'][:5])}")
            print()

            category_rows += data["rows"]
            total_rows += data["rows"]
            total_files += 1

        print(f"  Итого в категории: {category_rows:,} строк")

    print("=" * 80)
    print(f"ВСЕГО / TOTAL:")
    print(f"  Файлов / Files: {total_files}")
    print(f"  Записей / Records: {total_rows:,}")
    print("=" * 80)


def check_data_quality(stats: Dict[str, Dict]) -> List[str]:
    """Check data quality and return list of recommendations."""
    recommendations = []

    # Check for empty files
    empty_files = [f for f, d in stats.items() if d["rows"] == 0]
    if empty_files:
        recommendations.append(f"⚠️ Найдены пустые файлы / Empty files found: {', '.join(empty_files)}")

    # Check for small files that might need expansion
    small_files = [f for f, d in stats.items() if 0 < d["rows"] < SMALL_FILE_THRESHOLD]
    if small_files:
        recommendations.append(
            f"📝 Файлы с малым количеством данных (могут требовать расширения):\n   " f"{', '.join(small_files)}"
        )

    # Check for very large files that might need splitting
    large_files = [f for f, d in stats.items() if d["rows"] > LARGE_FILE_THRESHOLD]
    if large_files:
        recommendations.append(f"💾 Большие файлы (возможно, стоит разделить):\n   " f"{', '.join(large_files)}")

    return recommendations


def main():
    """Main function."""
    # Find repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    data_dir = repo_root / "data"

    if not data_dir.exists():
        print(f"❌ Директория данных не найдена: {data_dir}")
        return 1

    print(f"🔍 Сканирование директории данных: {data_dir}")
    print()

    # Scan and analyze
    stats = scan_data_directory(data_dir)

    if not stats:
        print("❌ CSV файлы не найдены")
        return 1

    # Print statistics
    print_statistics(stats)

    # Check quality
    print("\n📋 РЕКОМЕНДАЦИИ / RECOMMENDATIONS")
    print("=" * 80)
    recommendations = check_data_quality(stats)

    if recommendations:
        for rec in recommendations:
            print(f"\n{rec}")
    else:
        print("\n✅ Качество данных в норме / Data quality is good")

    print("\n" + "=" * 80)

    return 0


if __name__ == "__main__":
    exit(main())
