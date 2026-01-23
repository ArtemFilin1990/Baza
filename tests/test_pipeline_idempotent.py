"""Test idempotent file processing."""

import csv
from pathlib import Path

import pytest

from app.catalog import load_catalog
from app.processor import process_file
from app.registry import Registry
from app.report import ReportWriter
from app.utils import sha256_file

# Import fixtures
from tests.test_pipeline_conftest import temp_dir, test_config


def test_idempotent_processing(temp_dir, test_config):
    """Test that processing the same file twice is idempotent."""
    # Create a test CSV file
    csv_file = temp_dir / "inbox" / "test_bearings.csv"
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Артикул", "Бренд", "d", "D", "H"])
        writer.writerow(["6205", "SKF", "25", "52", "15"])

    # Setup
    import os
    import shutil

    old_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        registry = Registry(temp_dir / "out" / "processed_registry.json")
        report = ReportWriter(temp_dir / "out" / "run_report.ndjson")

        # Calculate SHA256
        sha256_1 = sha256_file(csv_file)

        # Process file first time
        success = process_file(csv_file, test_config, registry, report)
        assert success

        # Check catalog
        catalog = load_catalog(temp_dir / "out" / "catalog_target.csv")
        assert len(catalog) == 1

        # Copy the file back to inbox (simulate re-upload of same file)
        processed_files = list((temp_dir / "processed").glob("*.csv"))
        assert len(processed_files) == 1

        csv_file_2 = temp_dir / "inbox" / "test_bearings_copy.csv"
        shutil.copy(processed_files[0], csv_file_2)

        # Verify SHA256 is the same (content hasn't changed)
        sha256_2 = sha256_file(csv_file_2)
        assert sha256_1 == sha256_2, "SHA256 should be the same for identical content"

        # Process file second time
        success_2 = process_file(csv_file_2, test_config, registry, report)
        assert success_2  # Should succeed (skipped)

        # Catalog should still have 1 record
        catalog_2 = load_catalog(temp_dir / "out" / "catalog_target.csv")
        assert len(catalog_2) == 1, "Catalog should not have duplicate records"

    finally:
        os.chdir(old_cwd)
