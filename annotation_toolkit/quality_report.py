from collections import Counter
from typing import Any


REQUIRED_FIELDS = ("id", "text", "annotator", "label")


def generate_quality_report(
    records: list[dict[str, Any]],
    allowed_labels: set[str] | None = None,
) -> dict[str, Any]:
    """Generate a quality summary for a text annotation dataset."""

    total_records = len(records)
    label_distribution: Counter[str] = Counter()
    invalid_records = 0

    for record in records:
        missing_required_field = any(
            field not in record or record[field] in (None, "")
            for field in REQUIRED_FIELDS
        )

        label = record.get("label")
        invalid_label = (
            allowed_labels is not None
            and label not in allowed_labels
        )

        if missing_required_field or invalid_label:
            invalid_records += 1

        if label not in (None, ""):
            label_distribution[str(label)] += 1

    valid_records = total_records - invalid_records
    validity_rate = (
        valid_records / total_records if total_records else 0.0
    )

    return {
        "total_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "validity_rate": round(validity_rate, 4),
        "label_distribution": dict(label_distribution),
    }
