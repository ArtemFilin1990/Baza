"""CSV validation helpers aligned with repository schemas."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple


TYPE_CASTERS = {
    "string": str,
    "number": float,
}


@dataclass
class TableSchema:
    """Normalized representation of a table schema."""

    name: str
    path: Path
    columns: Dict[str, str]
    unique: List[str]
    sort_by: List[str]


def _load_schema_file(path: Path) -> List[TableSchema]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    tables: List[TableSchema] = []
    for table in payload.get("tables", []):
        # Extract column types from nested column definitions
        columns = {}
        for col_name, col_def in table["columns"].items():
            if isinstance(col_def, dict):
                columns[col_name] = col_def.get("type", "string")
            else:
                columns[col_name] = col_def
        
        tables.append(
            TableSchema(
                name=table["name"],
                path=Path(table["path"]),
                columns=columns,
                unique=table.get("unique", table.get("uniqueKey", [])),
                sort_by=table.get("sort_by", []),
            )
        )
    return tables


def load_schemas(schema_dir: Path) -> List[TableSchema]:
    """Load all table schemas from a directory."""
    schemas: List[TableSchema] = []
    for schema_file in sorted(schema_dir.glob("*.yaml")):
        schemas.extend(_load_schema_file(schema_file))
    return schemas


def _coerce(value: str, expected_type: str) -> Tuple[bool, str]:
    caster = TYPE_CASTERS.get(expected_type, str)
    if value == "" and expected_type == "string":
        return True, value
    try:
        coerced = caster(value) if value != "" else caster("0") if expected_type == "number" else caster(value)
    except Exception:
        return False, value
    return True, str(coerced) if expected_type == "number" else str(coerced)


def _sort_key(row: Dict[str, str], schema: TableSchema) -> Tuple:
    key_parts: List = []
    for field in schema.sort_by:
        expected_type = schema.columns.get(field, "string")
        if expected_type == "number":
            try:
                key_parts.append(float(row[field]))
            except ValueError:
                key_parts.append(row[field])
        else:
            key_parts.append(row[field])
    return tuple(key_parts)


def validate_table(schema: TableSchema) -> List[str]:
    """Validate a single table against the provided schema."""
    errors: List[str] = []
    if not schema.path.exists():
        return [f"{schema.name}: missing file {schema.path}"]

    with schema.path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return [f"{schema.name}: {schema.path} has no header"]

        expected_fields = list(schema.columns.keys())
        if reader.fieldnames != expected_fields:
            errors.append(
                f"{schema.name}: header mismatch. expected {expected_fields}, found {reader.fieldnames}"
            )

        seen_keys = set()
        prev_key: Tuple | None = None
        for line_number, row in enumerate(reader, start=2):
            # Column completeness and type validation
            for column, expected_type in schema.columns.items():
                if column not in row:
                    errors.append(f"{schema.name}: missing column {column} at line {line_number}")
                    continue
                ok, coerced = _coerce(row[column], expected_type)
                if not ok:
                    errors.append(
                        f"{schema.name}: invalid {expected_type} value '{row[column]}' "
                        f"in column {column} at line {line_number}"
                    )
                row[column] = coerced

            # Uniqueness
            if schema.unique:
                key = tuple(row[col] for col in schema.unique)
                if key in seen_keys:
                    errors.append(f"{schema.name}: duplicate key {key} at line {line_number}")
                seen_keys.add(key)

            # Sorting
            if schema.sort_by:
                current_key = _sort_key(row, schema)
                if prev_key is not None and current_key < prev_key:
                    errors.append(
                        f"{schema.name}: sort order violated at line {line_number} "
                        f"(key {current_key} after {prev_key})"
                    )
                prev_key = current_key

    return errors


def validate_all(schema_dir: Path) -> List[str]:
    """Validate every schema in the directory and aggregate errors."""
    all_errors: List[str] = []
    for schema in load_schemas(schema_dir):
        all_errors.extend(validate_table(schema))
    return all_errors
