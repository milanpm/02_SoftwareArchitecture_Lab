"""
File Name: report_formatter.py
Created Date: 2026-09-16
Author: Alex
Description:
    Converts a completed inspection result into a human-readable
    text report without performing evaluation or persistence.
"""

from inspection_result import InspectionResult


class InspectionReportFormatter:
    """Format inspection results as readable text."""

    def format(self, result: InspectionResult) -> str:
        """Return a text report for an inspection result."""

        return (
            "Center Alignment Inspection\n"
            f"Reference : "
            f"({result.reference_x:.2f}, {result.reference_y:.2f})\n"
            f"Measured  : "
            f"({result.measured_x:.2f}, {result.measured_y:.2f})\n"
            f"Offset    : "
            f"({result.offset_x:.2f}, {result.offset_y:.2f})\n"
            f"Distance  : {result.distance:.2f} px\n"
            f"Tolerance : {result.tolerance:.2f} px\n"
            f"Result    : {result.status}\n"
            f"Inspected : "
            f"{result.inspected_at.isoformat(timespec='seconds')}"
        )
