import csv
from pathlib import Path


def test_suffix_codes_are_uppercase() -> None:
    suffix_path = Path("data/iso/suffixes.csv")
    with suffix_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            assert row["code"] == row["code"].upper()
            assert row["manufacturer"] == row["manufacturer"].upper()


def test_suffix_notes_trimmed() -> None:
    suffix_path = Path("data/iso/suffixes.csv")
    with suffix_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            assert row["notes"].strip() == row["notes"]
