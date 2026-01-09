import csv
from pathlib import Path


def _load_dimensions(path: Path) -> list[tuple[str, float, float, float]]:
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [(row["designation"], float(row["d"]), float(row["D"]), float(row["B"])) for row in reader]


def test_gost_dimensions_sorted() -> None:
    rows = _load_dimensions(Path("data/gost/dimensions.csv"))
    assert rows == sorted(rows, key=lambda item: (item[0], item[1], item[2]))


def test_iso_dimensions_sorted() -> None:
    rows = _load_dimensions(Path("data/iso/dimensions.csv"))
    assert rows == sorted(rows, key=lambda item: (item[0], item[1], item[2]))
