"""Test dimension conflict detection."""

import csv
from pathlib import Path

import pytest

from app.catalog import load_catalog
from app.processor import process_file
from app.registry import Registry
from app.report import ReportWriter

# Import fixtures
from tests.test_pipeline_conftest import temp_dir, test_config


def test_dimension_conflicts(temp_dir, test_config):
    """Test that dimension conflicts are detected and both records are added."""
    # Create first CSV file
    csv_file_1 = temp_dir / "inbox" / "test_1.csv"
    csv_file_1.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_file_1, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Артикул", "Бренд", "d", "D", "H"])
        writer.writerow(["6205", "SKF", "25", "52", "15"])

    # Setup
    import os

    old_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        registry = Registry(temp_dir / "out" / "processed_registry.json")
        report = ReportWriter(temp_dir / "out" / "run_report.ndjson")

        # Process first file
        success_1 = process_file(csv_file_1, test_config, registry, report)
        assert success_1

        # Check catalog
        catalog_1 = load_catalog(temp_dir / "out" / "catalog_target.csv")
        assert len(catalog_1) == 1

        # Create second CSV file with same article/brand but different dimensions
        csv_file_2 = temp_dir / "inbox" / "test_2.csv"

        with open(csv_file_2, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Артикул", "Бренд", "d", "D", "H"])
            writer.writerow(["6205", "SKF", "25", "52", "18"])  # Different H

        # Process second file
        success_2 = process_file(csv_file_2, test_config, registry, report)
        assert success_2

        # Check catalog - should now have 2 records (conflict)
        catalog_2 = load_catalog(temp_dir / "out" / "catalog_target.csv")
        assert len(catalog_2) == 2, "Catalog should have 2 records due to dimension conflict"

        # Verify both records have same article/brand but different H
        skf_records = catalog_2[catalog_2["Бренд"] == "SKF"]
        assert len(skf_records) == 2
        assert set(skf_records["H"].values) == {15.0, 18.0}

        # Check report for conflict
        with open(temp_dir / "out" / "run_report.ndjson", encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) >= 2

            # Second report entry should have conflict
            import json

            report_2 = json.loads(lines[1])
            assert report_2["n_conflicts"] == 1, "Should report 1 conflict"
            assert "conflicts" in report_2

    finally:
        os.chdir(old_cwd)
