"""Test XLSX file processing."""

from pathlib import Path

import pandas as pd
import pytest

from app.catalog import load_catalog
from app.processor import process_file
from app.registry import Registry
from app.report import ReportWriter

# Import fixtures
from tests.test_pipeline_conftest import temp_dir, test_config


def test_xlsx_processing(temp_dir, test_config):
    """Test processing an XLSX file."""
    # Create a test XLSX file
    xlsx_file = temp_dir / "inbox" / "test_bearings.xlsx"
    xlsx_file.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "Товар": ["Подшипник 6205", "Подшипник 6206"],
        "Обозначение": ["6205", "6206"],
        "Производитель": ["SKF", "NSK"],
        "Внутр": ["25", "30"],
        "Наруж": ["52", "62"],
        "Ширина": ["15", "16"],
    }

    df = pd.DataFrame(data)
    df.to_excel(xlsx_file, index=False, engine="openpyxl")

    # Setup
    import os

    old_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        registry = Registry(temp_dir / "out" / "processed_registry.json")
        report = ReportWriter(temp_dir / "out" / "run_report.ndjson")

        # Process file
        success = process_file(xlsx_file, test_config, registry, report)

        assert success, "File processing should succeed"

        # Check catalog
        catalog = load_catalog(temp_dir / "out" / "catalog_target.csv")
        assert len(catalog) == 2, "Catalog should have 2 records"

        # Verify column recognition worked
        assert catalog.iloc[0]["Артикул"] == "6205"
        assert catalog.iloc[0]["Бренд"] == "SKF"

    finally:
        os.chdir(old_cwd)
