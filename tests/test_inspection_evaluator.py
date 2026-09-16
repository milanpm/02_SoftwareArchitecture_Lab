"""
File Name: test_inspection_evaluator.py
Created Date: 2026-09-16
Author: Alex
Description:
    Verifies PASS, FAIL, boundary, validation, and time behavior
    of the center-alignment inspection evaluator.
"""

from datetime import datetime
from pathlib import Path
import sys

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAY2_PATH = (
    PROJECT_ROOT
    / "examples"
    / "02_Single_Responsibility_Principle"
    / "good_example"
)

sys.path.insert(0, str(DAY2_PATH))

from inspection_evaluator import InspectionEvaluator  # noqa: E402


FIXED_TIME = datetime(2026, 9, 16, 15, 30, 0)


def fixed_clock() -> datetime:
    """Return a deterministic inspection time."""

    return FIXED_TIME


def test_evaluate_alignment_as_pass() -> None:
    """An offset inside the tolerance should pass."""

    evaluator = InspectionEvaluator(fixed_clock)

    result = evaluator.evaluate(
        reference_x=200.0,
        reference_y=220.0,
        measured_x=210.0,
        measured_y=215.0,
        tolerance=20.0,
    )

    assert result.offset_x == pytest.approx(10.0)
    assert result.offset_y == pytest.approx(-5.0)
    assert result.distance == pytest.approx(11.1803398875)
    assert result.status == "PASS"
    assert result.inspected_at == FIXED_TIME


def test_evaluate_alignment_as_fail() -> None:
    """An offset outside the tolerance should fail."""

    evaluator = InspectionEvaluator(fixed_clock)

    result = evaluator.evaluate(
        reference_x=200.0,
        reference_y=220.0,
        measured_x=245.0,
        measured_y=245.0,
        tolerance=20.0,
    )

    assert result.distance == pytest.approx(51.4781507049)
    assert result.status == "FAIL"


def test_distance_equal_to_tolerance_passes() -> None:
    """A distance exactly equal to the tolerance should pass."""

    evaluator = InspectionEvaluator(fixed_clock)

    result = evaluator.evaluate(
        reference_x=200.0,
        reference_y=220.0,
        measured_x=220.0,
        measured_y=220.0,
        tolerance=20.0,
    )

    assert result.distance == pytest.approx(20.0)
    assert result.status == "PASS"


@pytest.mark.parametrize("tolerance", [0.0, -1.0])
def test_reject_non_positive_tolerance(tolerance: float) -> None:
    """Zero and negative tolerance values should be rejected."""

    evaluator = InspectionEvaluator(fixed_clock)

    with pytest.raises(
        ValueError,
        match="Tolerance must be greater than zero.",
    ):
        evaluator.evaluate(
            reference_x=200.0,
            reference_y=220.0,
            measured_x=210.0,
            measured_y=215.0,
            tolerance=tolerance,
        )
