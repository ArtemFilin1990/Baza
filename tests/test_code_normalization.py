import csv
from pathlib import Path


def test_prefix_codes_have_no_spaces() -> None:
    path = Path("data/iso/prefixes.csv")
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            assert " " not in row["code"]
            assert row["code"] == row["code"].upper()
