"""Test CSV file processing."""

import csv
from pathlib import Path

import pytest

from app.catalog import load_catalog
from app.processor import process_file
from app.registry import Registry
from app.report import ReportWriter

# Import fixtures
from tests.test_pipeline_conftest import temp_dir, test_config


def test_csv_processing(temp_dir, test_config):
    """Test processing a CSV file with known columns."""
    # Create a test CSV file
    csv_file = temp_dir / "inbox" / "test_bearings.csv"
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Наименование", "Артикул", "Бренд", "d", "D", "H"])
        writer.writerow(["Подшипник 6205", "6205", "SKF", "25", "52", "15"])
        writer.writerow(["Подшипник 6206", "6206", "NSK", "30", "62", "16"])
        writer.writerow(["Подшипник 6207", "6207", "NTN", "35", "72", "17"])

    # Setup
    import os

    old_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        registry = Registry(temp_dir / "out" / "processed_registry.json")
        report = ReportWriter(temp_dir / "out" / "run_report.ndjson")

        # Process file
        success = process_file(csv_file, test_config, registry, report)

        assert success, "File processing should succeed"

        # Check catalog
        catalog_path = temp_dir / "out" / "catalog_target.csv"
        assert catalog_path.exists(), "Catalog should be created"

        catalog = load_catalog(catalog_path)
        assert len(catalog) == 3, "Catalog should have 3 records"

        # Verify data
        assert catalog.iloc[0]["Артикул"] == "6205"
        assert catalog.iloc[0]["Бренд"] == "SKF"
        assert catalog.iloc[0]["d"] == 25.0
        assert catalog.iloc[0]["D"] == 52.0
        assert catalog.iloc[0]["H"] == 15.0

        # Check that file was moved to processed
        assert not csv_file.exists(), "File should be moved from inbox"
        processed_files = list((temp_dir / "processed").glob("*.csv"))
        assert len(processed_files) == 1, "File should be in processed directory"

    finally:
        os.chdir(old_cwd)


def test_csv_with_alternative_columns(temp_dir, test_config):
    """Test CSV with alternative column names."""
    # Create a test CSV file with alternative column names
    csv_file = temp_dir / "inbox" / "test_alt.csv"
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "part", "brand", "inner", "outer", "width"])
        writer.writerow(["Bearing 6205", "6205", "SKF", "25", "52", "15"])

    # Setup
    import os

    old_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        registry = Registry(temp_dir / "out" / "processed_registry.json")
        report = ReportWriter(temp_dir / "out" / "run_report.ndjson")

        # Process file
        success = process_file(csv_file, test_config, registry, report)

        assert success, "File processing should succeed"

        # Check catalog
        catalog = load_catalog(temp_dir / "out" / "catalog_target.csv")
        assert len(catalog) == 1

        assert catalog.iloc[0]["Артикул"] == "6205"
        assert catalog.iloc[0]["d"] == 25.0

    finally:
        os.chdir(old_cwd)
