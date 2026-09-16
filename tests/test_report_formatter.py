"""
File Name: test_report_formatter.py
Created Date: 2026-09-16
Author: Alex
Description:
    Verifies that an inspection result is converted into the expected
    human-readable text report.
"""

from datetime import datetime
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAY2_PATH = (
    PROJECT_ROOT
    / "examples"
    / "02_Single_Responsibility_Principle"
    / "good_example"
)

sys.path.insert(0, str(DAY2_PATH))

from inspection_result import InspectionResult  # noqa: E402
from report_formatter import InspectionReportFormatter  # noqa: E402


def test_format_inspection_report() -> None:
    """The formatter should create the expected report text."""

    result = InspectionResult(
        reference_x=200.0,
        reference_y=220.0,
        measured_x=210.0,
        measured_y=215.0,
        offset_x=10.0,
        offset_y=-5.0,
        distance=11.1803398875,
        tolerance=20.0,
        status="PASS",
        inspected_at=datetime(2026, 9, 16, 15, 30, 0),
    )

    formatter = InspectionReportFormatter()

    report = formatter.format(result)

    assert report == (
        "Center Alignment Inspection\n"
        "Reference : (200.00, 220.00)\n"
        "Measured  : (210.00, 215.00)\n"
        "Offset    : (10.00, -5.00)\n"
        "Distance  : 11.18 px\n"
        "Tolerance : 20.00 px\n"
        "Result    : PASS\n"
        "Inspected : 2026-09-16T15:30:00"
    )
