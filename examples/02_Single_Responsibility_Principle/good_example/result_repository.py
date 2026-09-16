"""
File Name: result_repository.py
Created Date: 2026-09-16
Author: Alex
Description:
    Persists a completed inspection result as JSON without performing
    inspection evaluation, report formatting, or presentation.
"""

import json
from pathlib import Path
from typing import Any

from inspection_result import InspectionResult


class JsonInspectionResultRepository:
    """Persist an inspection result in a JSON file."""

    def __init__(self, output_file: Path) -> None:
        """Initialize the repository with an output path."""

        self._output_file = output_file

    def save(self, result: InspectionResult) -> None:
        """Serialize and save an inspection result."""

        self._output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        record: dict[str, Any] = {
            "reference_x": result.reference_x,
            "reference_y": result.reference_y,
            "measured_x": result.measured_x,
            "measured_y": result.measured_y,
            "offset_x": result.offset_x,
            "offset_y": result.offset_y,
            "distance": result.distance,
            "tolerance": result.tolerance,
            "status": result.status,
            "inspected_at": result.inspected_at.isoformat(
                timespec="seconds"
            ),
        }

        with self._output_file.open("w", encoding="utf-8") as file:
            json.dump(
                record,
                file,
                indent=4,
                ensure_ascii=False,
            )
