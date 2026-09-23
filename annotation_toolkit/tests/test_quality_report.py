from annotation_toolkit.quality_report import generate_quality_report


def test_quality_report_with_valid_and_invalid_records():
    records = [
        {
            "id": "1",
            "text": "Great service",
            "annotator": "reviewer_a",
            "label": "positive",
        },
        {
            "id": "2",
            "text": "Bad experience",
            "annotator": "reviewer_a",
            "label": "negative",
        },
        {
            "id": "3",
            "text": "",
            "annotator": "reviewer_b",
            "label": "positive",
        },
        {
            "id": "4",
            "text": "Unknown label",
            "annotator": "reviewer_b",
            "label": "other",
        },
    ]

    report = generate_quality_report(
        records,
        allowed_labels={"positive", "negative"},
    )

    assert report["total_records"] == 4
    assert report["valid_records"] == 2
    assert report["invalid_records"] == 2
    assert report["validity_rate"] == 0.5
    assert report["label_distribution"] == {
        "positive": 2,
        "negative": 1,
        "other": 1,
    }


def test_quality_report_with_empty_dataset():
    report = generate_quality_report([])

    assert report["total_records"] == 0
    assert report["valid_records"] == 0
    assert report["invalid_records"] == 0
    assert report["validity_rate"] == 0.0
    assert report["label_distribution"] == {}
