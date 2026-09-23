from collections import Counter
from collections.abc import Sequence


def _check_lengths(a: Sequence[str], b: Sequence[str]) -> None:
    if len(a) != len(b) or len(a) == 0:
        raise ValueError("Label sequences must have the same non-zero length")


def raw_agreement(a: Sequence[str], b: Sequence[str]) -> float:
    _check_lengths(a, b)
    return sum(x == y for x, y in zip(a, b)) / len(a)


def cohens_kappa(a: Sequence[str], b: Sequence[str]) -> float:
    _check_lengths(a, b)
    observed = raw_agreement(a, b)
    count_a, count_b = Counter(a), Counter(b)
    labels = set(count_a) | set(count_b)
    n = len(a)
    expected = sum((count_a[label] / n) * (count_b[label] / n) for label in labels)
    if expected == 1:
        return 1.0 if observed == 1 else 0.0
    return (observed - expected) / (1 - expected)
