#!/usr/bin/env python3
"""
Convert brands.json to CSV format for easier analysis and import.

Usage:
    python sources/brands_json_to_csv.py
    python sources/brands_json_to_csv.py --input sources/brands.json --output sources/brands.csv
"""

import argparse
import csv
import json
import sys
from pathlib import Path


def load_brands_json(filepath: Path) -> list[dict[str, str]]:
    """Load brands data from JSON file."""
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def write_brands_csv(brands: list[dict[str, str]], filepath: Path) -> None:
    """Write brands data to CSV file."""
    if not brands:
        print("Warning: No brands data to write", file=sys.stderr)
        return

    # Get all possible fieldnames from all brand entries
    fieldnames = set()
    for brand in brands:
        fieldnames.update(brand.keys())

    # Sort fieldnames for consistent output, with common fields first
    priority_fields = ["name", "country", "description"]
    other_fields = sorted(fieldnames - set(priority_fields))
    fieldnames = [f for f in priority_fields if f in fieldnames] + other_fields

    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(brands)

    print(f"Wrote {len(brands)} brands to {filepath}")


def main():
    parser = argparse.ArgumentParser(description="Convert brands.json to CSV format")
    parser.add_argument("--input", default="sources/brands.json", help="Input JSON file (default: sources/brands.json)")
    parser.add_argument("--output", default="sources/brands.csv", help="Output CSV file (default: sources/brands.csv)")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist", file=sys.stderr)
        return 1

    try:
        brands = load_brands_json(input_path)
        write_brands_csv(brands, output_path)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code if exit_code is not None else 1)
