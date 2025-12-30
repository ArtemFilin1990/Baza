"""Normalize datasets and produce reproducible CSV outputs."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.extract.raw_datasets import RAW_DATASETS, DatasetSpec
from scripts.validate.csv_validator import validate_all


def _dedupe(rows: List[Dict[str, str]], unique_keys: List[str]) -> Tuple[List[Dict[str, str]], int]:
    if not unique_keys:
        return rows, 0
    seen = set()
    deduped: List[Dict[str, str]] = []
    removed = 0
    for row in rows:
        key = tuple(row[k] for k in unique_keys)
        if key in seen:
            removed += 1
            continue
        seen.add(key)
        deduped.append(row)
    return deduped, removed


def _sort(rows: List[Dict[str, str]], keys: List[str]) -> List[Dict[str, str]]:
    if not keys:
        return rows
    return sorted(rows, key=lambda item: tuple(item[k] for k in keys))


def _write_csv(dataset: DatasetSpec) -> Tuple[int, int, int]:
    rows = [dict(row) for row in dataset["rows"]]
    deduped, removed = _dedupe(rows, dataset["unique"])
    ordered = _sort(deduped, dataset["sort_by"])

    dataset["output"].parent.mkdir(parents=True, exist_ok=True)
    with dataset["output"].open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=dataset["columns"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(ordered)

    return len(rows), len(ordered), removed


def _aggregate_report() -> Dict[str, int]:
    counts = {"rows_total": 0, "rows_added": 0, "rows_deduped": 0}
    for spec in RAW_DATASETS.values():
        original = len(spec["rows"])
        deduped, removed = _dedupe(spec["rows"], spec["unique"])
        counts["rows_total"] += len(deduped)
        counts["rows_added"] += len(deduped)
        counts["rows_deduped"] += removed
    return counts


def _write_report(path: Path) -> None:
    report_body = {
        "source_name": "normalized_catalog",
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input_files": sorted({row["source"] for spec in RAW_DATASETS.values() for row in spec["rows"] if "source" in row}),
        "output_files": sorted(str(spec["output"]) for spec in RAW_DATASETS.values()),
    }
    report_body.update(_aggregate_report())
    report_body["rows_removed"] = 0
    report_body["errors"] = []

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report_body, ensure_ascii=False, indent=2), encoding="utf-8")


def run(normalize_only: bool, report_path: Path | None) -> None:
    for spec in RAW_DATASETS.values():
        _write_csv(spec)

    if report_path:
        _write_report(report_path)

    if not normalize_only:
        errors = validate_all(Path(__file__).resolve().parent.parent / "schemas")
        if errors:
            raise SystemExit("\n".join(errors))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize bearing datasets.")
    parser.add_argument(
        "--no-validation",
        action="store_true",
        help="Skip schema validations after generating CSV files.",
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip writing a data/reports entry.",
    )
    parser.add_argument(
        "--report-path",
        type=Path,
        default=Path("data/reports") / f"{datetime.now().date()}_source.json",
        help="Override the report path (default: data/reports/YYYY-MM-DD_source.json).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    target_report = None if args.no_report else args.report_path
    run(normalize_only=args.no_validation, report_path=target_report)
