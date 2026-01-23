"""Test configuration and fixtures."""

import sys
from pathlib import Path

# Add src to path for imports
repo_root = Path(__file__).parent.parent
src_path = repo_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

import shutil
import tempfile

import pytest

from app.config import Config


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def test_config(temp_dir):
    """Create a test configuration."""
    # Create config directory
    config_dir = temp_dir / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    # Copy config files
    repo_root = Path(__file__).parent.parent
    shutil.copy(repo_root / "config" / "app.yaml", config_dir / "app.yaml")
    shutil.copy(repo_root / "config" / "brand_aliases.json", config_dir / "brand_aliases.json")
    shutil.copy(repo_root / "config" / "parsing_rules.json", config_dir / "parsing_rules.json")

    # Create directories
    for subdir in ["inbox", "processed", "error", "out", "logs"]:
        (temp_dir / subdir).mkdir(parents=True, exist_ok=True)

    # Load config
    import os

    old_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        config = Config()
        yield config
    finally:
        os.chdir(old_cwd)
