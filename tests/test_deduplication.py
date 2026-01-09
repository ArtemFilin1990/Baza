"""Tests for the deduplicate_nomenclature script."""

import csv
from pathlib import Path
import pytest
import tempfile
from scripts.deduplicate_nomenclature import deduplicate_nomenclature


@pytest.fixture
def sample_csv_with_duplicates(tmp_path):
    """Create a sample CSV file with duplicates for testing."""
    csv_file = tmp_path / "test_nomenclature.csv"
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Brand', 'Product Name', 'Product Link', 'Analog Name', 'Analog Link', 'Factory'])
        writer.writeheader()
        writer.writerows([
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Product Link': 'link1', 'Analog Name': 'Analog1', 'Analog Link': 'alink1', 'Factory': 'Factory1'},
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Product Link': 'link2', 'Analog Name': 'Analog2', 'Analog Link': 'alink2', 'Factory': 'Factory2'},  # Duplicate
            {'Brand': 'Brand2', 'Product Name': 'Product2', 'Product Link': 'link3', 'Analog Name': 'Analog3', 'Analog Link': 'alink3', 'Factory': 'Factory3'},
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Product Link': 'link4', 'Analog Name': 'Analog4', 'Analog Link': 'alink4', 'Factory': 'Factory4'},  # Duplicate
            {'Brand': 'Brand3', 'Product Name': 'Product3', 'Product Link': 'link5', 'Analog Name': 'Analog5', 'Analog Link': 'alink5', 'Factory': 'Factory5'},
        ])
    return csv_file


def test_deduplicate_removes_duplicates(sample_csv_with_duplicates, tmp_path):
    """Test that deduplication removes duplicate entries."""
    output_file = tmp_path / "output.csv"
    
    removed_count = deduplicate_nomenclature(sample_csv_with_duplicates, output_file)
    
    assert removed_count == 2
    
    # Verify output file has correct number of rows
    with open(output_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 3


def test_deduplicate_keeps_first_occurrence(sample_csv_with_duplicates, tmp_path):
    """Test that deduplication keeps the first occurrence of each duplicate."""
    output_file = tmp_path / "output.csv"
    
    deduplicate_nomenclature(sample_csv_with_duplicates, output_file)
    
    # Verify the first occurrence is kept
    with open(output_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        brand1_product1 = [row for row in rows if row['Brand'] == 'Brand1' and row['Product Name'] == 'Product1']
        assert len(brand1_product1) == 1
        assert brand1_product1[0]['Product Link'] == 'link1'
        assert brand1_product1[0]['Factory'] == 'Factory1'


def test_deduplicate_no_duplicates(tmp_path):
    """Test that deduplication works correctly when there are no duplicates."""
    csv_file = tmp_path / "test_no_dups.csv"
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Brand', 'Product Name', 'Product Link', 'Analog Name', 'Analog Link', 'Factory'])
        writer.writeheader()
        writer.writerows([
            {'Brand': 'Brand1', 'Product Name': 'Product1', 'Product Link': 'link1', 'Analog Name': 'Analog1', 'Analog Link': 'alink1', 'Factory': 'Factory1'},
            {'Brand': 'Brand2', 'Product Name': 'Product2', 'Product Link': 'link2', 'Analog Name': 'Analog2', 'Analog Link': 'alink2', 'Factory': 'Factory2'},
        ])
    
    output_file = tmp_path / "output.csv"
    removed_count = deduplicate_nomenclature(csv_file, output_file)
    
    assert removed_count == 0
    
    with open(output_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 2


def test_deduplicate_preserves_header(sample_csv_with_duplicates, tmp_path):
    """Test that deduplication preserves the CSV header."""
    output_file = tmp_path / "output.csv"
    
    deduplicate_nomenclature(sample_csv_with_duplicates, output_file)
    
    with open(output_file, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ['Brand', 'Product Name', 'Product Link', 'Analog Name', 'Analog Link', 'Factory']
