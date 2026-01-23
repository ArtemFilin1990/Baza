"""Report writing module for NDJSON format."""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


class ReportWriter:
    """Writer for NDJSON (newline-delimited JSON) reports."""

    def __init__(self, report_path: Path):
        """Initialize report writer.

        Args:
            report_path: Path to NDJSON report file
        """
        self.report_path = report_path
        self.report_path.parent.mkdir(parents=True, exist_ok=True)

    def write_entry(
        self,
        filename: str,
        sha256: str,
        status: str,
        n_rows: int = 0,
        n_added: int = 0,
        n_skipped: int = 0,
        n_conflicts: int = 0,
        error: Optional[str] = None,
        conflicts: Optional[List[Dict]] = None,
    ):
        """Write a single entry to the report.

        Args:
            filename: Source filename
            sha256: SHA256 hash of the file
            status: Processing status ('success', 'error', 'skipped')
            n_rows: Number of rows in source file
            n_added: Number of records added
            n_skipped: Number of records skipped
            n_conflicts: Number of dimension conflicts
            error: Error message if status is 'error'
            conflicts: List of conflict details
        """
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "filename": filename,
            "sha256": sha256,
            "status": status,
            "n_rows": n_rows,
            "n_added": n_added,
            "n_skipped": n_skipped,
            "n_conflicts": n_conflicts,
        }

        if error:
            entry["error"] = error

        if conflicts:
            entry["conflicts"] = conflicts

        # Append to file
        with open(self.report_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
