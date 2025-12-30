"""CLI entrypoint for validating CSV datasets."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate.csv_validator import validate_all


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    schema_dir = repo_root / "schemas"
    errors = validate_all(schema_dir)
    if errors:
        for message in errors:
            print(message)
        return 1
    print("All datasets validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
