"""
File Name: inspection_evaluator.py
Created Date: 2026-09-16
Author: Alex
Description:
    Calculates center displacement and evaluates whether the measured
    center is within the allowed alignment tolerance.
"""

from collections.abc import Callable
from datetime import datetime
from math import hypot

from inspection_result import InspectionResult, InspectionStatus


class InspectionEvaluator:
    """Evaluate center alignment according to a tolerance."""

    def __init__(
        self,
        clock: Callable[[], datetime] = datetime.now,
    ) -> None:
        """Initialize the evaluator with a time provider."""

        self._clock = clock

    def evaluate(
        self,
        reference_x: float,
        reference_y: float,
        measured_x: float,
        measured_y: float,
        tolerance: float,
    ) -> InspectionResult:
        """Calculate displacement and return an inspection result."""

        if tolerance <= 0:
            raise ValueError("Tolerance must be greater than zero.")

        offset_x = measured_x - reference_x
        offset_y = measured_y - reference_y
        distance = hypot(offset_x, offset_y)

        status: InspectionStatus = (
            "PASS" if distance <= tolerance else "FAIL"
        )

        return InspectionResult(
            reference_x=reference_x,
            reference_y=reference_y,
            measured_x=measured_x,
            measured_y=measured_y,
            offset_x=offset_x,
            offset_y=offset_y,
            distance=distance,
            tolerance=tolerance,
            status=status,
            inspected_at=self._clock(),
        )
