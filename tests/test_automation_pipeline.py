"""Integration tests for automated bearings catalog pipeline."""

import json
import tempfile
from pathlib import Path

import pandas as pd
import pytest

from src.catalog import CatalogManager
from src.config import Config
from src.parser import DataParser
from src.processor import FileProcessor
from src.registry import Registry
from src.utils import compute_file_hash


@pytest.fixture
def temp_workspace(tmp_path):
    """Create temporary workspace with all required directories."""
    workspace = {
        'inbox': tmp_path / 'inbox',
        'processed': tmp_path / 'processed',
        'error': tmp_path / 'error',
        'out': tmp_path / 'out',
        'logs': tmp_path / 'logs',
        'config': tmp_path / 'config',
    }
    
    for path in workspace.values():
        path.mkdir(parents=True, exist_ok=True)
    
    # Copy config files
    config_src = Path(__file__).parent.parent / 'config'
    for config_file in ['app.yaml', 'brand_aliases.json', 'parsing_rules.json']:
        src_file = config_src / config_file
        dst_file = workspace['config'] / config_file
        if src_file.exists():
            dst_file.write_text(src_file.read_text())
    
    # Update paths in app.yaml to use temp directories
    app_yaml = workspace['config'] / 'app.yaml'
    content = app_yaml.read_text()
    content = content.replace('inbox: "inbox"', f'inbox: "{workspace["inbox"]}"')
    content = content.replace('processed: "processed"', f'processed: "{workspace["processed"]}"')
    content = content.replace('error: "error"', f'error: "{workspace["error"]}"')
    content = content.replace('out: "out"', f'out: "{workspace["out"]}"')
    content = content.replace('logs: "logs"', f'logs: "{workspace["logs"]}"')
    # Also update registry path to be in temp out directory
    content = content.replace(
        'file: "out/processed_registry.json"',
        f'file: "{workspace["out"]}/processed_registry.json"'
    )
    app_yaml.write_text(content)
    
    return workspace


@pytest.fixture
def sample_csv_data():
    """Sample CSV data with clear column names."""
    return pd.DataFrame([
        {
            'Наименование': 'Подшипник радиальный шариковый',
            'Артикул': '6205',
            'Бренд': 'SKF',
            'D': 52,
            'd': 25,
            'H': 15,
            'm': 0.128
        },
        {
            'Наименование': 'Подшипник радиальный роликовый',
            'Артикул': '32205',
            'Бренд': 'FAG',
            'D': 52,
            'd': 25,
            'H': 18,
            'm': 0.154
        }
    ])


@pytest.fixture
def sample_xlsx_data():
    """Sample XLSX data with alternative column names."""
    return pd.DataFrame([
        {
            'product': 'Deep groove ball bearing',
            'part': '6206',
            'brand': 'nsk',
            'outer diameter': 62,
            'inner diameter': 30,
            'width': 16,
            'weight': 0.199
        }
    ])


@pytest.fixture
def processor(temp_workspace):
    """Create configured processor for testing."""
    config = Config(config_dir=temp_workspace['config'])
    from src.logger import LoggerSetup
    logger = LoggerSetup.setup(
        temp_workspace['logs'] / 'app.log',
        'json',
        'INFO'
    )
    return FileProcessor(config, logger)


def test_csv_processing_with_clear_columns(temp_workspace, sample_csv_data, processor):
    """Test 1: CSV with clear column names produces correct catalog."""
    # Create CSV file in inbox
    csv_file = temp_workspace['inbox'] / 'bearings_data.csv'
    sample_csv_data.to_csv(csv_file, index=False, encoding='utf-8')
    
    # Process file
    status, n_records = processor.process_file(csv_file)
    
    # Verify
    assert status == 'success'
    assert n_records == 2
    
    # Check catalog exists
    catalog_csv = temp_workspace['out'] / 'catalog_target.csv'
    assert catalog_csv.exists()
    
    # Load and verify catalog
    df = pd.read_csv(catalog_csv)
    assert len(df) == 2
    assert set(df.columns) == {'Наименование', 'Артикул', 'Аналог', 'Бренд', 'D', 'd', 'H', 'm'}
    
    # Check file was moved to processed
    assert not csv_file.exists()
    processed_files = list(temp_workspace['processed'].glob('*'))
    assert len(processed_files) == 1


def test_xlsx_with_alternative_column_names(temp_workspace, sample_xlsx_data, processor):
    """Test 2: XLSX with alternative column names maps correctly."""
    # Create XLSX file in inbox
    xlsx_file = temp_workspace['inbox'] / 'bearings_data.xlsx'
    sample_xlsx_data.to_excel(xlsx_file, index=False, engine='openpyxl')
    
    # Process file
    status, n_records = processor.process_file(xlsx_file)
    
    # Verify
    assert status == 'success'
    assert n_records == 1
    
    # Load catalog and check mapping
    catalog_csv = temp_workspace['out'] / 'catalog_target.csv'
    df = pd.read_csv(catalog_csv)
    
    assert len(df) == 1
    # Brand should be normalized to uppercase
    assert df.iloc[0]['Бренд'] == 'NSK'
    assert df.iloc[0]['D'] == 62
    assert df.iloc[0]['d'] == 30


def test_duplicate_file_idempotency(temp_workspace, processor):
    """Test 3: Processing the same file twice is idempotent (no duplicate records)."""
    # Use unique data to avoid registry collision with other tests
    unique_data = pd.DataFrame([
        {
            'Наименование': 'Подшипник уникальный 1',
            'Артикул': 'UNIQUE-001',
            'Бренд': 'TEST',
            'D': 100,
            'd': 50,
            'H': 20,
            'm': 0.5
        }
    ])
    
    # Create CSV file
    csv_file = temp_workspace['inbox'] / 'unique_bearings.csv'
    unique_data.to_csv(csv_file, index=False, encoding='utf-8')
    
    # Compute hash before processing
    original_hash = compute_file_hash(csv_file)
    
    # First processing
    status1, n_records1 = processor.process_file(csv_file)
    assert status1 == 'success'
    
    # Load catalog after first processing
    catalog_csv = temp_workspace['out'] / 'catalog_target.csv'
    df1 = pd.read_csv(catalog_csv)
    count_after_first = len(df1)
    
    # Create identical file again
    csv_file2 = temp_workspace['inbox'] / 'unique_bearings_copy.csv'
    unique_data.to_csv(csv_file2, index=False, encoding='utf-8')
    
    # Second processing (same content, different name)
    status2, n_records2 = processor.process_file(csv_file2)
    
    # Should be skipped as duplicate
    assert status2 == 'skipped_duplicate'
    
    # Catalog should have same number of records
    df2 = pd.read_csv(catalog_csv)
    assert len(df2) == count_after_first


def test_dimension_conflict_detection(temp_workspace, processor):
    """Test 4: Dimension conflicts are detected and logged."""
    # Create file with conflicting dimensions for same part
    data = pd.DataFrame([
        {
            'Артикул': '6205',
            'Бренд': 'SKF',
            'D': 52,
            'd': 25,
            'H': 15
        },
        {
            'Артикул': '6205',
            'Бренд': 'SKF',
            'D': 54,  # Different dimension!
            'd': 25,
            'H': 15
        }
    ])
    
    csv_file = temp_workspace['inbox'] / 'conflict_data.csv'
    data.to_csv(csv_file, index=False, encoding='utf-8')
    
    # Process
    status, n_records = processor.process_file(csv_file)
    
    assert status == 'success'
    
    # Both records should be added (as they have different dimensions)
    catalog_csv = temp_workspace['out'] / 'catalog_target.csv'
    df = pd.read_csv(catalog_csv)
    assert len(df) == 2
    
    # Check report for conflict
    report_file = temp_workspace['out'] / 'run_report.ndjson'
    assert report_file.exists()
    
    with open(report_file) as f:
        lines = f.readlines()
        last_report = json.loads(lines[-1])
        # Should have 1 conflict
        assert last_report['n_conflicts'] >= 1


def test_invalid_file_error_handling(temp_workspace, processor):
    """Test 5: Invalid files are moved to error directory."""
    # Create invalid file
    invalid_file = temp_workspace['inbox'] / 'invalid.txt'
    invalid_file.write_text('This is not valid bearing data\nJust random text')
    
    # Process
    status, n_records = processor.process_file(invalid_file)
    
    # Should fail
    assert status == 'error'
    assert n_records == 0
    
    # File should be in error directory
    assert not invalid_file.exists()
    error_files = list(temp_workspace['error'].glob('*'))
    assert len(error_files) == 1
    assert '__ERROR_' in error_files[0].name


def test_json_file_processing(temp_workspace, processor):
    """Test JSON file processing."""
    # Create JSON file
    data = [
        {
            'Артикул': '6207',
            'Бренд': 'FAG',
            'D': 72,
            'd': 35,
            'H': 17
        }
    ]
    
    json_file = temp_workspace['inbox'] / 'bearings.json'
    json_file.write_text(json.dumps(data, ensure_ascii=False))
    
    # Process
    status, n_records = processor.process_file(json_file)
    
    assert status == 'success'
    assert n_records == 1
    
    # Verify catalog
    catalog_csv = temp_workspace['out'] / 'catalog_target.csv'
    df = pd.read_csv(catalog_csv)
    assert len(df) == 1
    # Convert to string for comparison (pandas may read as int)
    assert str(df.iloc[0]['Артикул']) == '6207'
