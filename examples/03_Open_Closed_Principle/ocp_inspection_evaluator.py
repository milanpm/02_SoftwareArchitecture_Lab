"""Center-alignment evaluator whose decision rule is supplied by the caller."""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from math import hypot
from typing import Literal

from alignment_rules import AlignmentRule


@dataclass(frozen=True)
class InspectionResult:
    offset_x: float
    offset_y: float
    distance: float
    tolerance: float
    rule_name: str
    status: Literal["PASS", "FAIL"]
    inspected_at: datetime


class InspectionEvaluator:
    """Calculate offsets and delegate the PASS/FAIL decision."""

    def __init__(
        self,
        rule: AlignmentRule,
        clock: Callable[[], datetime] = datetime.now,
    ) -> None:
        self._rule = rule
        self._clock = clock

    def evaluate(
        self,
        reference_x: float,
        reference_y: float,
        measured_x: float,
        measured_y: float,
        tolerance: float,
    ) -> InspectionResult:
        if tolerance <= 0:
            raise ValueError("Tolerance must be greater than zero.")

        offset_x = measured_x - reference_x
        offset_y = measured_y - reference_y
        return InspectionResult(
            offset_x=offset_x,
            offset_y=offset_y,
            distance=hypot(offset_x, offset_y),
            tolerance=tolerance,
            rule_name=self._rule.name,
            status=(
                "PASS"
                if self._rule.passes(offset_x, offset_y, tolerance)
                else "FAIL"
            ),
            inspected_at=self._clock(),
        )
