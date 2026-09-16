"""
File Name: inspection_result.py
Created Date: 2026-09-16
Author: Alex
Description:
    Defines an immutable data model representing the result
    of a center-alignment inspection.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal


InspectionStatus = Literal["PASS", "FAIL"]


@dataclass(frozen=True)
class InspectionResult:
    """Represent the completed result of an alignment inspection."""

    reference_x: float
    reference_y: float
    measured_x: float
    measured_y: float
    offset_x: float
    offset_y: float
    distance: float
    tolerance: float
    status: InspectionStatus
    inspected_at: datetime
