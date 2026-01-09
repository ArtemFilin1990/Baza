"""Shared pytest fixtures for all tests."""

import pytest
from pathlib import Path


@pytest.fixture
def repo_root():
    """Return the repository root directory."""
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def data_dir(repo_root):
    """Return the data directory."""
    return repo_root / "data"


@pytest.fixture
def schemas_dir(repo_root):
    """Return the schemas directory."""
    return repo_root / "schemas"
