"""Interchangeable center-alignment decision rules."""

from math import hypot
from typing import Protocol


class AlignmentRule(Protocol):
    """Contract for an alignment decision."""

    name: str

    def passes(self, offset_x: float, offset_y: float, tolerance: float) -> bool:
        """Return whether the offset satisfies this rule."""


class CircularRule:
    """Accept points inside or on a circular tolerance region."""

    name = "circular"

    def passes(self, offset_x: float, offset_y: float, tolerance: float) -> bool:
        return hypot(offset_x, offset_y) <= tolerance


class PerAxisRule:
    """Accept points within tolerance on both axes independently."""

    name = "per-axis"

    def passes(self, offset_x: float, offset_y: float, tolerance: float) -> bool:
        return abs(offset_x) <= tolerance and abs(offset_y) <= tolerance
