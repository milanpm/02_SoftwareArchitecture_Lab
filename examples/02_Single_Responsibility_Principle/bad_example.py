"""
File Name: bad_example.py
Created Date: 2026-09-16
Author: Alex
Description:
    Demonstrates a class that violates the Single Responsibility
    Principle by calculating, evaluating, formatting, saving,
    and displaying an inspection result.
"""

import json
from datetime import datetime
from math import hypot
from pathlib import Path
from typing import Any


class InspectionProcessor:
    """Perform every inspection-related responsibility in one class."""

    def process(
        self,
        reference_x: float,
        reference_y: float,
        measured_x: float,
        measured_y: float,
        tolerance: float,
        output_file: Path,
    ) -> dict[str, Any]:
        """Calculate, evaluate, format, save, and display an inspection."""

        # Input validation
        if tolerance <= 0:
            raise ValueError("Tolerance must be greater than zero.")

        # Distance calculation
        offset_x = measured_x - reference_x
        offset_y = measured_y - reference_y
        distance = hypot(offset_x, offset_y)

        # PASS/FAIL evaluation
        status = "PASS" if distance <= tolerance else "FAIL"

        # Result creation
        result = {
            "reference_x": reference_x,
            "reference_y": reference_y,
            "measured_x": measured_x,
            "measured_y": measured_y,
            "offset_x": offset_x,
            "offset_y": offset_y,
            "distance": distance,
            "tolerance": tolerance,
            "status": status,
            "inspected_at": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        # Text report formatting
        report = (
            "Center Alignment Inspection\n"
            f"Reference : ({reference_x:.2f}, {reference_y:.2f})\n"
            f"Measured  : ({measured_x:.2f}, {measured_y:.2f})\n"
            f"Offset    : ({offset_x:.2f}, {offset_y:.2f})\n"
            f"Distance  : {distance:.2f} px\n"
            f"Tolerance : {tolerance:.2f} px\n"
            f"Result    : {status}"
        )

        # File-system handling and JSON persistence
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_file.open("w", encoding="utf-8") as file:
            json.dump(
                result,
                file,
                indent=4,
                ensure_ascii=False,
            )

        # Console presentation
        print(report)
        print(f"Saved to  : {output_file}")

        return result


def main() -> None:
    """Run a center-alignment inspection example."""

    processor = InspectionProcessor()

    processor.process(
        reference_x=200.0,
        reference_y=220.0,
        measured_x=210.0,
        measured_y=215.0,
        tolerance=20.0,
        output_file=Path("data/day2_inspection_result.json"),
    )


if __name__ == "__main__":
    main()
