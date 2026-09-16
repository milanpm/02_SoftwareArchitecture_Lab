"""
File Name: test_console_presenter.py
Created Date: 2026-09-16
Author: Alex
Description:
    Verifies that the console presenter displays a formatted report
    and its saved file path.
"""

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

from console_presenter import ConsoleInspectionPresenter  # noqa: E402


def test_display_inspection_report(capsys) -> None:
    """The presenter should print the report and output path."""

    presenter = ConsoleInspectionPresenter()
    output_file = Path("data/result.json")
    report = (
        "Center Alignment Inspection\n"
        "Distance  : 11.18 px\n"
        "Result    : PASS"
    )

    presenter.display(report, output_file)

    captured = capsys.readouterr()

    assert captured.out == (
        f"{report}\n"
        f"Saved to  : {output_file}\n"
    )
