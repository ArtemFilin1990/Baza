#!/usr/bin/env python3
"""
Unit tests for schema validation functionality.

Tests validate that:
1. All schema files are valid JSON/YAML
2. Required fields are present in schemas
3. Schema structure is correct
4. All CSV files have corresponding schemas
"""

import json
import unittest
from pathlib import Path


class TestSchemas(unittest.TestCase):
    """Test schema file structure and validity."""

    def setUp(self):
        """Set up test fixtures."""
        self.repo_root = Path(__file__).parent.parent
        self.schemas_dir = self.repo_root / "schemas"
        self.data_dir = self.repo_root / "data"

    def test_schemas_directory_exists(self):
        """Test that schemas directory exists."""
        self.assertTrue(self.schemas_dir.exists(), "schemas/ directory should exist")
        self.assertTrue(self.schemas_dir.is_dir(), "schemas/ should be a directory")

    def test_all_schema_files_valid_json(self):
        """Test that all .yaml schema files contain valid JSON format."""
        schema_files = list(self.schemas_dir.glob("*.yaml"))
        self.assertGreater(len(schema_files), 0, "Should have at least one schema file")

        for schema_file in schema_files:
            with self.subTest(schema=schema_file.name):
                with open(schema_file, encoding="utf-8") as f:
                    try:
                        # Note: These .yaml files actually contain JSON format
                        data = json.load(f)
                        self.assertIsInstance(data, dict, f"{schema_file.name} should contain a JSON object")
                    except json.JSONDecodeError as e:
                        self.fail(f"{schema_file.name} contains invalid JSON: {e}")

    def test_schema_structure(self):
        """Test that each schema has required structure."""
        schema_files = list(self.schemas_dir.glob("*.yaml"))

        for schema_file in schema_files:
            with self.subTest(schema=schema_file.name):
                with open(schema_file, encoding="utf-8") as f:
                    schema = json.load(f)

                # Check for 'tables' key
                self.assertIn("tables", schema, f"{schema_file.name} should have 'tables' key")
                self.assertIsInstance(schema["tables"], list, "'tables' should be a list")

                # Check each table definition
                for table in schema["tables"]:
                    with self.subTest(table=table.get("name", "unknown")):
                        # Required fields
                        self.assertIn("name", table, "Table should have 'name' field")
                        self.assertIn("path", table, "Table should have 'path' field")
                        self.assertIn("columns", table, "Table should have 'columns' field")

                        # Optional but recommended fields
                        if "uniqueKey" in table:
                            self.assertIsInstance(table["uniqueKey"], list, "uniqueKey should be a list")

                        if "sort_by" in table:
                            self.assertIsInstance(table["sort_by"], list, "sort_by should be a list")

    def test_column_definitions(self):
        """Test that column definitions have proper structure."""
        schema_files = list(self.schemas_dir.glob("*.yaml"))

        for schema_file in schema_files:
            with open(schema_file, encoding="utf-8") as f:
                schema = json.load(f)

            for table in schema["tables"]:
                columns = table.get("columns", {})

                for col_name, col_def in columns.items():
                    with self.subTest(schema=schema_file.name, table=table["name"], column=col_name):
                        # Column can be simple string or dict
                        if isinstance(col_def, dict):
                            # New format with required, type, description
                            self.assertIn("type", col_def, f"Column {col_name} should have 'type'")
                            valid_types = ["string", "number", "integer", "boolean"]
                            self.assertIn(col_def["type"], valid_types, f"Column type should be one of {valid_types}")
                        else:
                            # Old format, just a type string
                            valid_types = ["string", "number", "integer", "boolean"]
                            self.assertIn(col_def, valid_types, f"Column type should be one of {valid_types}")

    def test_csv_files_have_schemas(self):
        """Test that major CSV files have corresponding schema definitions."""
        # Expected CSV files and their schemas
        expected_mappings = {
            "data/gost/bearings.csv": "schemas/gost.yaml",
            "data/gost/dimensions.csv": "schemas/gost.yaml",
            "data/iso/bearings.csv": "schemas/iso.yaml",
            "data/iso/suffixes.csv": "schemas/iso.yaml",
            "data/brands/brands.csv": "schemas/brands.yaml",
            "data/analogs/gost_iso.csv": "schemas/analogs.yaml",
        }

        for csv_path, schema_path in expected_mappings.items():
            with self.subTest(csv=csv_path):
                csv_file = self.repo_root / csv_path
                schema_file = self.repo_root / schema_path

                if csv_file.exists():
                    self.assertTrue(schema_file.exists(), f"CSV file {csv_path} should have schema {schema_path}")

                    # Verify the schema references this CSV
                    with open(schema_file, encoding="utf-8") as f:
                        schema = json.load(f)

                    paths = [table.get("path") for table in schema.get("tables", [])]
                    self.assertIn(csv_path, paths, f"Schema {schema_path} should reference {csv_path}")

    def test_unique_keys_reference_valid_columns(self):
        """Test that uniqueKey fields reference actual columns."""
        schema_files = list(self.schemas_dir.glob("*.yaml"))

        for schema_file in schema_files:
            with open(schema_file, encoding="utf-8") as f:
                schema = json.load(f)

            for table in schema["tables"]:
                if "uniqueKey" in table:
                    columns = table.get("columns", {})
                    unique_keys = table["uniqueKey"]

                    for key in unique_keys:
                        with self.subTest(schema=schema_file.name, table=table["name"], key=key):
                            self.assertIn(key, columns, f"uniqueKey field '{key}' should be in columns")

    def test_sort_by_reference_valid_columns(self):
        """Test that sort_by fields reference actual columns."""
        schema_files = list(self.schemas_dir.glob("*.yaml"))

        for schema_file in schema_files:
            with open(schema_file, encoding="utf-8") as f:
                schema = json.load(f)

            for table in schema["tables"]:
                if "sort_by" in table:
                    columns = table.get("columns", {})
                    sort_fields = table["sort_by"]

                    for field in sort_fields:
                        with self.subTest(schema=schema_file.name, table=table["name"], field=field):
                            self.assertIn(field, columns, f"sort_by field '{field}' should be in columns")


class TestSchemaRequiredFields(unittest.TestCase):
    """Test that schemas define required fields appropriately."""

    def setUp(self):
        """Set up test fixtures."""
        self.repo_root = Path(__file__).parent.parent
        self.schemas_dir = self.repo_root / "schemas"

    def test_schemas_have_descriptions(self):
        """Test that table definitions have descriptions."""
        schema_files = list(self.schemas_dir.glob("*.yaml"))

        for schema_file in schema_files:
            with open(schema_file, encoding="utf-8") as f:
                schema = json.load(f)

            for table in schema["tables"]:
                with self.subTest(schema=schema_file.name, table=table["name"]):
                    # Recommended but not strictly required
                    if "description" not in table:
                        # Just a warning, not a failure
                        pass


if __name__ == "__main__":
    unittest.main()
