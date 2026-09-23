import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = ("id", "text", "annotator", "label")


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    records = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}") from exc
    return records


def validate(records: list[dict[str, Any]], allowed_labels: set[str]) -> list[str]:
    errors: list[str] = []
    for index, record in enumerate(records, start=1):
        for field in REQUIRED_FIELDS:
            if field not in record or record[field] in (None, ""):
                errors.append(f"Record {index}: missing field '{field}'")
        label = record.get("label")
        if label is not None and label not in allowed_labels:
            errors.append(f"Record {index}: invalid label '{label}'")
    return errors
