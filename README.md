# Text Annotation Toolkit

A small Python toolkit for validating text-annotation datasets and measuring inter-annotator agreement.

## Features
- JSONL loading and validation
- Required-field and allowed-label checks
- Raw agreement
- Cohen's kappa
- Command-line interface
- Automated tests and CI

## Record format
```json
{"id":"001","text":"Great service","annotator":"reviewer_a","label":"positive"}
```

## Usage
```bash
python -m annotation_toolkit.cli validate examples/sample.jsonl --labels positive negative neutral
python -m annotation_toolkit.cli agreement examples/reviewer_a.jsonl examples/reviewer_b.jsonl
```

## Tests
```bash
pip install -r requirements.txt
pytest -q
```
