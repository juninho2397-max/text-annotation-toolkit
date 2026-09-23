import argparse

from annotation_toolkit.core import load_jsonl, validate
from annotation_toolkit.metrics import cohens_kappa, raw_agreement


def main() -> None:
    parser = argparse.ArgumentParser(description="Text annotation quality toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path")
    validate_parser.add_argument("--labels", nargs="+", required=True)

    agreement_parser = subparsers.add_parser("agreement")
    agreement_parser.add_argument("first")
    agreement_parser.add_argument("second")

    args = parser.parse_args()

    if args.command == "validate":
        errors = validate(load_jsonl(args.path), set(args.labels))
        if errors:
            print("\n".join(errors))
        else:
            print("Dataset is valid.")
    else:
        first = load_jsonl(args.first)
        second = load_jsonl(args.second)
        first_labels = [row["label"] for row in first]
        second_labels = [row["label"] for row in second]
        print(f"raw_agreement={raw_agreement(first_labels, second_labels):.4f}")
        print(f"cohens_kappa={cohens_kappa(first_labels, second_labels):.4f}")


if __name__ == "__main__":
    main()
