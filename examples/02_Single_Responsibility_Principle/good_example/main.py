"""
File Name: main.py
Created Date: 2026-09-16
Author: Alex
Description:
    Creates and coordinates the single-responsibility components
    required to perform a center-alignment inspection.
"""

from pathlib import Path

from console_presenter import ConsoleInspectionPresenter
from inspection_evaluator import InspectionEvaluator
from report_formatter import InspectionReportFormatter
from result_repository import JsonInspectionResultRepository


def main() -> None:
    """Run the refactored center-alignment inspection example."""

    output_file = Path("data/day2_srp_inspection_result.json")

    evaluator = InspectionEvaluator()
    formatter = InspectionReportFormatter()
    repository = JsonInspectionResultRepository(output_file)
    presenter = ConsoleInspectionPresenter()

    result = evaluator.evaluate(
        reference_x=200.0,
        reference_y=220.0,
        measured_x=210.0,
        measured_y=215.0,
        tolerance=20.0,
    )

    report = formatter.format(result)

    repository.save(result)
    presenter.display(report, output_file)


if __name__ == "__main__":
    main()
