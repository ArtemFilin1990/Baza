"""Tests for the deduplicate_nomenclature script."""

import csv

import pytest

from scripts.deduplicate_nomenclature import deduplicate_nomenclature


@pytest.fixture
def sample_csv_with_duplicates(tmp_path):
    """Create a sample CSV file with duplicate entries."""
    csv_file = tmp_path / "test_data.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        f.write("Brand,Product Name,Description\n")
        f.write("Brand1,Product1,Desc1\n")
        f.write("Brand1,Product1,Desc2\n")  # Duplicate
        f.write("Brand2,Product2,Desc3\n")
        f.write("Brand1,Product1,Desc4\n")  # Another duplicate
        f.write("Brand3,Product3,Desc5\n")
    return csv_file


def test_deduplication_removes_duplicates(sample_csv_with_duplicates, tmp_path):
    """Test that deduplication removes duplicate entries."""
    output_file = tmp_path / "output.csv"
    removed = deduplicate_nomenclature(sample_csv_with_duplicates, output_file)
    
    assert removed == 2, "Should remove 2 duplicates"
    
    with open(output_file, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    assert len(rows) == 3, "Should have 3 unique rows"
    
    # Verify the first occurrence is preserved
    assert rows[0]["Brand"] == "Brand1"
    assert rows[0]["Product Name"] == "Product1"
    assert rows[0]["Description"] == "Desc1"


def test_deduplication_preserves_first_occurrence(sample_csv_with_duplicates, tmp_path):
    """Test that deduplication keeps the first occurrence of duplicates."""
    output_file = tmp_path / "output.csv"
    deduplicate_nomenclature(sample_csv_with_duplicates, output_file)
    
    with open(output_file, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # First duplicate should have Desc1 (not Desc2 or Desc4)
    brand1_row = next(r for r in rows if r["Brand"] == "Brand1")
    assert brand1_row["Description"] == "Desc1"


def test_deduplication_empty_file(tmp_path):
    """Test deduplication with an empty CSV file."""
    empty_csv = tmp_path / "empty.csv"
    with open(empty_csv, "w", encoding="utf-8", newline="") as f:
        f.write("Brand,Product Name,Description\n")
    
    output_file = tmp_path / "output.csv"
    removed = deduplicate_nomenclature(empty_csv, output_file)
    
    assert removed == 0, "Should remove 0 duplicates from empty file"


def test_deduplication_no_duplicates(tmp_path):
    """Test deduplication when there are no duplicates."""
    csv_file = tmp_path / "no_dupes.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        f.write("Brand,Product Name,Description\n")
        f.write("Brand1,Product1,Desc1\n")
        f.write("Brand2,Product2,Desc2\n")
        f.write("Brand3,Product3,Desc3\n")
    
    output_file = tmp_path / "output.csv"
    removed = deduplicate_nomenclature(csv_file, output_file)
    
    assert removed == 0, "Should remove 0 duplicates"
    
    with open(output_file, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    assert len(rows) == 3, "All rows should be preserved"
