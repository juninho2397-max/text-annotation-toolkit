import pytest

from annotation_toolkit.metrics import cohens_kappa, raw_agreement


def test_raw_agreement():
    assert raw_agreement(["a", "b", "c"], ["a", "x", "c"]) == pytest.approx(2 / 3)


def test_perfect_kappa():
    assert cohens_kappa(["a", "b", "a"], ["a", "b", "a"]) == 1.0


def test_mismatched_lengths():
    with pytest.raises(ValueError):
        raw_agreement(["a"], ["a", "b"])
