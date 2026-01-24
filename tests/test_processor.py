"""Tests for bearing data processing pipeline."""

import json
import tempfile
from pathlib import Path

import pandas as pd
import pytest

from src.catalog import CatalogManager
from src.config import Config
from src.logger import LoggerSetup, Reporter
from src.parser import DataParser
from src.processor import FileProcessor
from src.registry import Registry
from src.utils import (
    compute_file_hash,
    detect_file_type,
    generate_processed_filename,
    make_safe_filename,
    normalize_brand,
    normalize_number,
    normalize_text,
)


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def config_dir(temp_dir):
    """Create test configuration directory."""
    config_dir = temp_dir / "config"
    config_dir.mkdir()

    # Create app.yaml
    app_config = """
paths:
  inbox: inbox
  processed: processed
  error: error
  out: out
  logs: logs

watcher:
  mode: poll
  poll_interval: 1
  process_on_start: true

limits:
  max_file_size_mb: 50
  max_rows: 100000

normalization:
  brand_format: upper
  dimension_replacements:
    "×": "x"
    "х": "x"
  decimal_separator: "."

logging:
  level: INFO
  format: json

registry:
  file: out/processed_registry.json
"""
    (config_dir / "app.yaml").write_text(app_config)

    # Create brand_aliases.json
    brand_aliases = {"aliases": {"skf": "SKF", "fag": "FAG", "nsk": "NSK"}}
    (config_dir / "brand_aliases.json").write_text(json.dumps(brand_aliases))

    # Create parsing_rules.json
    parsing_rules = {
        "column_mappings": {
            "Наименование": ["наименование", "Наименование", "name"],
            "Артикул": ["артикул", "Артикул", "designation", "part"],
            "Аналог": ["аналог", "Аналог", "analog"],
            "Бренд": ["бренд", "Бренд", "brand"],
            "d": ["d", "inner diameter"],
            "D": ["D", "outer diameter"],
            "H": ["H", "B", "width"],
            "m": ["m", "weight"],
        },
        "required_fields": {"any_of": ["Артикул", "Наименование"]},
    }
    (config_dir / "parsing_rules.json").write_text(json.dumps(parsing_rules))

    return config_dir


class TestUtils:
    """Test utility functions."""

    def test_normalize_text(self):
        """Test text normalization."""
        assert normalize_text("  test  ") == "test"
        assert normalize_text("test   multiple   spaces") == "test multiple spaces"
        assert normalize_text("test×100") == "test×100"

    def test_normalize_number(self):
        """Test number normalization."""
        assert normalize_number(10) == 10.0
        assert normalize_number("10") == 10.0
        assert normalize_number("10.5") == 10.5
        assert normalize_number("10,5") == 10.5
        assert normalize_number("") is None
        assert normalize_number(None) is None

    def test_normalize_brand(self):
        """Test brand normalization."""
        aliases = {"skf": "SKF", "fag": "FAG"}
        assert normalize_brand("skf", aliases, "upper") == "SKF"
        assert normalize_brand("SKF", aliases, "upper") == "SKF"
        assert normalize_brand("nsk", {}, "upper") == "NSK"

    def test_make_safe_filename(self):
        """Test safe filename generation."""
        assert make_safe_filename("test file.csv") == "test_file"
        assert make_safe_filename("Test-File_123") == "Test-File_123"
        assert make_safe_filename("файл@#$.csv") == "файл"

    def test_generate_processed_filename(self):
        """Test processed filename generation."""
        name = generate_processed_filename("test.csv", 100, "a" * 64, is_error=False)
        assert "__test__100__" in name
        assert name.endswith(".csv")

        error_name = generate_processed_filename("test.csv", 0, "a" * 64, is_error=True, error_code="PARSE")
        assert "ERROR_PARSE" in error_name

    def test_detect_file_type(self):
        """Test file type detection."""
        assert detect_file_type(Path("test.csv")) == "csv"
        assert detect_file_type(Path("test.xlsx")) == "xlsx"
        assert detect_file_type(Path("test.json")) == "json"
        assert detect_file_type(Path("test.txt")) == "txt"
        assert detect_file_type(Path("test.xyz")) == "unknown"


class TestRegistry:
    """Test registry management."""

    def test_registry_operations(self, temp_dir):
        """Test registry add and check operations."""
        registry_file = temp_dir / "registry.json"
        registry = Registry(registry_file)

        # Should not be processed initially
        assert not registry.is_processed("hash123")

        # Add entry
        registry.add_entry(
            file_hash="hash123",
            original_name="test.csv",
            processed_name="20240101_120000__test__100__hash123.csv",
            n_records=100,
        )

        # Should now be processed
        assert registry.is_processed("hash123")

        # Get entry
        entry = registry.get_entry("hash123")
        assert entry["original_name"] == "test.csv"
        assert entry["n_records"] == 100


class TestParser:
    """Test data parsing."""

    def test_parse_csv(self, temp_dir, config_dir):
        """Test CSV parsing."""
        # Create test CSV
        csv_file = temp_dir / "test.csv"
        df = pd.DataFrame(
            {"артикул": ["6200", "6201"], "бренд": ["SKF", "FAG"], "d": [10, 12], "D": [30, 32], "H": [9, 10]}
        )
        df.to_csv(csv_file, index=False)

        # Parse
        config = Config(config_dir)
        parser = DataParser(config.load_parsing_rules(), {})

        result = parser.parse_file(csv_file, "csv")
        assert len(result) == 2
        assert "артикул" in result.columns

    def test_normalize_columns(self, config_dir):
        """Test column normalization."""
        config = Config(config_dir)
        parser = DataParser(config.load_parsing_rules(), {})

        df = pd.DataFrame({"part": ["6200"], "brand": ["SKF"], "inner diameter": [10]})

        normalized = parser.normalize_columns(df)
        # Should be mapped to target columns (title case)
        assert "Артикул" in normalized.columns
        assert "Бренд" in normalized.columns
        assert "d" in normalized.columns


class TestCatalog:
    """Test catalog management."""

    def test_add_records_deduplication(self, temp_dir, config_dir):
        """Test adding records with deduplication."""
        catalog_csv = temp_dir / "catalog.csv"
        catalog_json = temp_dir / "catalog.json"

        config = Config(config_dir)
        catalog = CatalogManager(
            catalog_csv=catalog_csv,
            catalog_json=catalog_json,
            brand_aliases=config.load_brand_aliases(),
            normalization_config={"brand_format": "upper"},
        )

        # Add first record
        df1 = pd.DataFrame({"Артикул": ["6200"], "Бренд": ["SKF"], "d": [10], "D": [30], "H": [9]})

        n_added, n_skipped, n_conflicts, _ = catalog.add_records(df1)
        assert n_added == 1
        assert n_skipped == 0

        # Add duplicate - should skip
        n_added, n_skipped, n_conflicts, _ = catalog.add_records(df1)
        assert n_added == 0
        assert n_skipped == 1

    def test_add_records_conflict(self, temp_dir, config_dir):
        """Test adding records with dimension conflicts."""
        catalog_csv = temp_dir / "catalog.csv"
        catalog_json = temp_dir / "catalog.json"

        config = Config(config_dir)
        catalog = CatalogManager(
            catalog_csv=catalog_csv,
            catalog_json=catalog_json,
            brand_aliases=config.load_brand_aliases(),
            normalization_config={"brand_format": "upper"},
        )

        # Add first record
        df1 = pd.DataFrame({"Артикул": ["6200"], "Бренд": ["SKF"], "d": [10], "D": [30], "H": [9]})
        catalog.add_records(df1)

        # Add record with same article/brand but different dimensions
        df2 = pd.DataFrame({"Артикул": ["6200"], "Бренд": ["SKF"], "d": [10], "D": [30], "H": [10]})  # Different!

        n_added, n_skipped, n_conflicts, conflicts = catalog.add_records(df2)
        assert n_added == 1  # Should add as separate entry
        assert n_conflicts == 1  # But mark as conflict


class TestProcessor:
    """Test file processor."""

    def test_process_csv_file(self, temp_dir, config_dir):
        """Test processing a CSV file."""
        # Setup directories
        inbox = temp_dir / "inbox"
        processed = temp_dir / "processed"
        error = temp_dir / "error"
        out = temp_dir / "out"
        logs = temp_dir / "logs"

        for d in [inbox, processed, error, out, logs]:
            d.mkdir()

        # Create test CSV in inbox
        csv_file = inbox / "test.csv"
        df = pd.DataFrame(
            {
                "артикул": ["6200", "6201", "6202"],
                "бренд": ["SKF", "FAG", "NSK"],
                "d": [10, 12, 15],
                "D": [30, 32, 35],
                "H": [9, 10, 11],
            }
        )
        df.to_csv(csv_file, index=False)

        # Setup config to use temp directories
        config = Config(config_dir)
        log_file = logs / "app.log"
        logger = LoggerSetup.setup(log_file, "json", "INFO")

        # Change working directory context
        import os

        old_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            processor = FileProcessor(config, logger)

            # Process file
            status, n_records = processor.process_file(csv_file)

            # Check results
            assert status == "success"
            assert n_records == 3

            # File should be moved to processed
            assert not csv_file.exists()
            assert len(list(processed.glob("*.csv"))) == 1

            # Catalog should exist
            assert (out / "catalog_target.csv").exists()
            assert (out / "catalog_target.json").exists()

            # Report should exist
            assert (out / "run_report.ndjson").exists()

        finally:
            os.chdir(old_cwd)

    def test_idempotent_processing(self, temp_dir, config_dir):
        """Test that processing same file twice doesn't duplicate records."""
        # Setup directories
        inbox = temp_dir / "inbox"
        processed = temp_dir / "processed"
        out = temp_dir / "out"
        logs = temp_dir / "logs"

        for d in [inbox, processed, out, logs]:
            d.mkdir()

        # Create test CSV properly
        csv_file1 = inbox / "test1.csv"
        df = pd.DataFrame(
            {"артикул": ["6200", "6201"], "бренд": ["SKF", "FAG"], "d": [10, 12], "D": [30, 32], "H": [9, 10]}
        )
        df.to_csv(csv_file1, index=False)

        # Setup and process first file
        config = Config(config_dir)
        log_file = logs / "app.log"
        logger = LoggerSetup.setup(log_file, "json", "INFO")

        import os

        old_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            processor = FileProcessor(config, logger)
            processor.process_file(csv_file1)

            # Check catalog
            catalog_df = pd.read_csv(out / "catalog_target.csv")
            assert len(catalog_df) == 2

            # Create identical file with different name
            csv_file2 = inbox / "test2.csv"
            df.to_csv(csv_file2, index=False)

            # Process second file (same content)
            status, _ = processor.process_file(csv_file2)

            # Should be skipped as duplicate
            assert status == "skipped_duplicate"

            # Catalog should still have only 2 records
            catalog_df = pd.read_csv(out / "catalog_target.csv")
            assert len(catalog_df) == 2

        finally:
            os.chdir(old_cwd)


class TestReporter:
    """Test reporter."""

    def test_write_report(self, temp_dir):
        """Test writing NDJSON report."""
        report_file = temp_dir / "report.ndjson"
        reporter = Reporter(report_file)

        reporter.write_report(
            filename="test.csv", file_hash="abc123", status="success", n_rows=10, n_added=8, n_skipped=2, n_conflicts=0
        )

        # Check report exists and is valid NDJSON
        assert report_file.exists()

        with open(report_file) as f:
            line = f.readline()
            data = json.loads(line)

            assert data["filename"] == "test.csv"
            assert data["status"] == "success"
            assert data["n_added"] == 8
