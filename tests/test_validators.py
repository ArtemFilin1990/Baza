"""Tests for CSV validators."""

import csv
import pytest
from scripts.validate.csv_validator import validate_table, TableSchema


@pytest.fixture
def sample_schema(tmp_path):
    """Create a sample schema for testing."""
    csv_file = tmp_path / "test.csv"
    return TableSchema(
        name="test",
        path=csv_file,
        columns={"Brand": "string", "Product Name": "string", "Price": "number"},
        unique=["Brand", "Product Name"],
        sort_by=["Brand", "Product Name"]
    )


@pytest.fixture
def valid_csv(tmp_path, sample_schema):
    """Create a valid CSV file for testing."""
    with open(sample_schema.path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Brand', 'Product Name', 'Price'])
        writer.writeheader()
        writer.writerows([
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Price': '10.5'},
            {'Brand': 'Brand1', 'Product Name': 'Product2', 'Price': '20.0'},
            {'Brand': 'Brand2', 'Product Name': 'Product1', 'Price': '15.0'},
        ])
    return sample_schema.path


def test_validate_valid_csv(valid_csv, sample_schema):
    """Test that a valid CSV passes validation."""
    errors = validate_table(sample_schema)
    assert errors == []


def test_validate_missing_file(tmp_path):
    """Test validation of a missing file."""
    schema = TableSchema(
        name="missing",
        path=tmp_path / "nonexistent.csv",
        columns={"Brand": "string"},
        unique=[],
        sort_by=[]
    )
    errors = validate_table(schema)
    assert len(errors) == 1
    assert "missing file" in errors[0]


def test_validate_duplicate_key(tmp_path, sample_schema):
    """Test validation detects duplicate keys."""
    with open(sample_schema.path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Brand', 'Product Name', 'Price'])
        writer.writeheader()
        writer.writerows([
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Price': '10.5'},
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Price': '20.0'},  # Duplicate
        ])
    
    errors = validate_table(sample_schema)
    assert len(errors) > 0
    assert any("duplicate key" in error for error in errors)


def test_validate_invalid_number(tmp_path, sample_schema):
    """Test validation detects invalid number values."""
    with open(sample_schema.path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Brand', 'Product Name', 'Price'])
        writer.writeheader()
        writer.writerows([
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Price': 'invalid'},
        ])
    
    errors = validate_table(sample_schema)
    assert len(errors) > 0
    assert any("invalid" in error for error in errors)


def test_validate_sort_order(tmp_path, sample_schema):
    """Test validation detects sort order violations."""
    with open(sample_schema.path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Brand', 'Product Name', 'Price'])
        writer.writeheader()
        writer.writerows([
            {'Brand': 'Brand2', 'Product Name': 'Product1', 'Price': '10.5'},
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Price': '20.0'},  # Out of order
        ])
    
    errors = validate_table(sample_schema)
    assert len(errors) > 0
    assert any("sort order violated" in error for error in errors)
