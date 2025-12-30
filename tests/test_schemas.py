from pathlib import Path

from scripts.validate.csv_validator import validate_all


def test_all_schemas_pass() -> None:
    errors = validate_all(Path("schemas"))
    assert errors == []
