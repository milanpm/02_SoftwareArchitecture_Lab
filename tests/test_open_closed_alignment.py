"""Verify interchangeable rules and stable evaluator behavior."""

from datetime import datetime
from pathlib import Path
import sys

import pytest


DAY3_PATH = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "03_Open_Closed_Principle"
)
sys.path.insert(0, str(DAY3_PATH))

from alignment_rules import CircularRule, PerAxisRule  # noqa: E402
from ocp_inspection_evaluator import InspectionEvaluator  # noqa: E402


FIXED_TIME = datetime(2026, 9, 23, 12, 0)


@pytest.mark.parametrize(
    ("rule", "expected"),
    [(CircularRule(), "FAIL"), (PerAxisRule(), "PASS")],
)
def test_same_offset_can_have_different_results(rule, expected) -> None:
    result = InspectionEvaluator(rule, lambda: FIXED_TIME).evaluate(
        200, 220, 216, 236, 20
    )
    assert result.status == expected
    assert result.distance == pytest.approx(22.627416998)
    assert result.rule_name == rule.name
    assert result.inspected_at == FIXED_TIME


@pytest.mark.parametrize("rule", [CircularRule(), PerAxisRule()])
def test_boundary_is_included(rule) -> None:
    result = InspectionEvaluator(rule).evaluate(0, 0, 20, 0, 20)
    assert result.status == "PASS"


@pytest.mark.parametrize("rule", [CircularRule(), PerAxisRule()])
def test_invalid_tolerance_is_rejected_before_rule(rule) -> None:
    with pytest.raises(ValueError, match="Tolerance must be greater than zero"):
        InspectionEvaluator(rule).evaluate(0, 0, 1, 1, 0)


def test_new_rule_needs_no_evaluator_change() -> None:
    class HorizontalOnlyRule:
        name = "horizontal-only"

        def passes(self, offset_x, offset_y, tolerance):
            return abs(offset_x) <= tolerance

    result = InspectionEvaluator(HorizontalOnlyRule()).evaluate(0, 0, 1, 100, 2)
    assert result.status == "PASS"
    assert result.rule_name == "horizontal-only"
