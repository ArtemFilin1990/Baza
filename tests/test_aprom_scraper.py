#!/usr/bin/env python3
"""
Unit tests for aprom_table_scraper.py

Run tests with:
    python -m pytest tests/test_aprom_scraper.py -v
    
Or with standard unittest:
    python -m unittest tests.test_aprom_scraper
    
Or from tests directory:
    cd tests && python test_aprom_scraper.py
"""

import sys
import unittest
from pathlib import Path


def _import_aprom_scraper():
    """Import aprom_table_scraper module with proper path handling."""
    # Add sources directory to path if not already there
    sources_path = str(Path(__file__).parent.parent / "sources")
    if sources_path not in sys.path:
        sys.path.insert(0, sources_path)
    
    from aprom_table_scraper import (
        TableCell, extract_tables, derive_headers,
        table_to_records, clean_text, normalize_url,
    )
    return TableCell, extract_tables, derive_headers, table_to_records, clean_text, normalize_url


# Import the module components
TableCell, extract_tables, derive_headers, table_to_records, clean_text, normalize_url = _import_aprom_scraper()


class TestCleanText(unittest.TestCase):
    """Test text cleaning functionality"""

    def test_collapse_whitespace(self):
        self.assertEqual(clean_text("hello   world"), "hello world")
        self.assertEqual(clean_text("hello\n\nworld"), "hello world")
        self.assertEqual(clean_text("hello\t\tworld"), "hello world")

    def test_strip_surrounding_spaces(self):
        self.assertEqual(clean_text("  hello  "), "hello")
        self.assertEqual(clean_text("\nhello\n"), "hello")

    def test_empty_string(self):
        self.assertEqual(clean_text(""), "")
        self.assertEqual(clean_text("   "), "")


class TestNormalizeUrl(unittest.TestCase):
    """Test URL normalization"""

    def test_query_param_sorting(self):
        url1 = "http://example.com/page?b=2&a=1"
        url2 = "http://example.com/page?a=1&b=2"
        self.assertEqual(normalize_url(url1), normalize_url(url2))

    def test_fragment_removal(self):
        url = "http://example.com/page#section"
        normalized = normalize_url(url)
        self.assertNotIn("#", normalized)

    def test_empty_query(self):
        url = "http://example.com/page"
        self.assertEqual(normalize_url(url), url)


class TestExtractTables(unittest.TestCase):
    """Test HTML table extraction"""

    def test_simple_table(self):
        html = """
        <table>
            <tr><th>Header1</th><th>Header2</th></tr>
            <tr><td>Cell1</td><td>Cell2</td></tr>
        </table>
        """
        tables = extract_tables(html)
        self.assertEqual(len(tables), 1)
        self.assertEqual(len(tables[0]), 2)  # 2 rows
        self.assertEqual(tables[0][0][0].text, "Header1")
        self.assertTrue(tables[0][0][0].is_header)
        self.assertEqual(tables[0][1][0].text, "Cell1")
        self.assertFalse(tables[0][1][0].is_header)

    def test_no_tables(self):
        html = "<div>No tables here</div>"
        tables = extract_tables(html)
        self.assertEqual(len(tables), 0)

    def test_nested_tables(self):
        html = """
        <table>
            <tr><td>Outer</td></tr>
        </table>
        """
        tables = extract_tables(html)
        self.assertEqual(len(tables), 1)

    def test_empty_cells_ignored(self):
        html = """
        <table>
            <tr><td>Value</td><td>   </td><td></td></tr>
        </table>
        """
        tables = extract_tables(html)
        # Empty cells should be ignored
        self.assertEqual(len(tables[0][0]), 1)


class TestDeriveHeaders(unittest.TestCase):
    """Test header derivation from table"""

    def test_explicit_headers(self):
        table = [
            [
                TableCell(text="Name", is_header=True),
                TableCell(text="Country", is_header=True),
            ],
            [TableCell(text="SKF", is_header=False), TableCell(text="Sweden", is_header=False)],
        ]
        headers = derive_headers(table)
        self.assertEqual(headers, ["name", "country"])

    def test_no_headers(self):
        table = [
            [TableCell(text="Value1", is_header=False), TableCell(text="Value2", is_header=False)],
        ]
        headers = derive_headers(table)
        self.assertEqual(headers, ["column_1", "column_2"])

    def test_empty_table(self):
        headers = derive_headers([])
        self.assertEqual(headers, [])

    def test_header_normalization(self):
        table = [
            [
                TableCell(text="Brand Name", is_header=True),
                TableCell(text="Country/Region", is_header=True),
            ],
        ]
        headers = derive_headers(table)
        self.assertEqual(headers, ["brand_name", "country_region"])


class TestTableToRecords(unittest.TestCase):
    """Test conversion of table to records"""

    def test_simple_conversion(self):
        table = [
            [TableCell(text="Name", is_header=True), TableCell(text="Age", is_header=True)],
            [TableCell(text="Alice", is_header=False), TableCell(text="30", is_header=False)],
            [TableCell(text="Bob", is_header=False), TableCell(text="25", is_header=False)],
        ]
        records = table_to_records(table)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0], {"name": "Alice", "age": "30"})
        self.assertEqual(records[1], {"name": "Bob", "age": "25"})

    def test_skip_all_header_rows(self):
        table = [
            [TableCell(text="Name", is_header=True), TableCell(text="Age", is_header=True)],
            [TableCell(text="Section", is_header=True), TableCell(text="Data", is_header=True)],
            [TableCell(text="Alice", is_header=False), TableCell(text="30", is_header=False)],
        ]
        records = table_to_records(table)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["name"], "Alice")

    def test_empty_table(self):
        records = table_to_records([])
        self.assertEqual(records, [])

    def test_missing_cells(self):
        table = [
            [TableCell(text="A", is_header=True), TableCell(text="B", is_header=True)],
            [TableCell(text="1", is_header=False)],  # Missing second cell
        ]
        records = table_to_records(table)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0], {"a": "1", "b": ""})


if __name__ == "__main__":
    unittest.main()
