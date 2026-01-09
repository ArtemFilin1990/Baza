"""Tests for CSV validators."""

import csv

import pytest


@pytest.fixture
def sample_valid_csv(tmp_path):
    """Create a sample valid CSV file."""
    csv_file = tmp_path / "valid.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        f.write("Brand,Product Name,Price\n")
        f.write("Brand1,Product1,100\n")
        f.write("Brand2,Product2,200\n")
    return csv_file


@pytest.fixture
def sample_invalid_csv(tmp_path):
    """Create a sample invalid CSV file (missing required column)."""
    csv_file = tmp_path / "invalid.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        f.write("Brand,Price\n")  # Missing 'Product Name'
        f.write("Brand1,100\n")
    return csv_file


def test_valid_csv_has_required_columns(sample_valid_csv):
    """Test that a valid CSV has all required columns."""
    with open(sample_valid_csv, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
    
    assert "Brand" in header
    assert "Product Name" in header


def test_invalid_csv_missing_columns(sample_invalid_csv):
    """Test detection of missing required columns."""
    with open(sample_invalid_csv, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
    
    assert "Brand" in header
    assert "Product Name" not in header


def test_csv_row_count(sample_valid_csv):
    """Test counting rows in CSV."""
    with open(sample_valid_csv, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    assert len(rows) == 2


def test_csv_field_validation(sample_valid_csv):
    """Test that CSV fields can be accessed correctly."""
    with open(sample_valid_csv, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        first_row = next(reader)
    
    assert first_row["Brand"] == "Brand1"
    assert first_row["Product Name"] == "Product1"
    assert first_row["Price"] == "100"


def test_empty_csv(tmp_path):
    """Test handling of empty CSV file."""
    empty_csv = tmp_path / "empty.csv"
    with open(empty_csv, "w", encoding="utf-8", newline="") as f:
        f.write("Brand,Product Name,Price\n")
    
    with open(empty_csv, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    assert len(rows) == 0
