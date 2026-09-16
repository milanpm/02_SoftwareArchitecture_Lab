"""
File Name: console_presenter.py
Created Date: 2026-09-16
Author: Alex
Description:
    Displays a formatted inspection report and its saved file path
    on the console without calculating, formatting, or saving data.
"""

from pathlib import Path


class ConsoleInspectionPresenter:
    """Display inspection information on the console."""

    def display(
        self,
        report: str,
        output_file: Path,
    ) -> None:
        """Print a formatted report and its storage location."""

        print(report)
        print(f"Saved to  : {output_file}")
