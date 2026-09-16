"""
File Name: test_inspection_result_repository.py
Created Date: 2026-09-16
Author: Alex
Description:
    Verifies that the JSON inspection result repository creates
    the expected directory, file, and serialized data.
"""

import json
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
from result_repository import (  # noqa: E402
    JsonInspectionResultRepository,
)


def test_save_inspection_result_as_json(tmp_path: Path) -> None:
    """The repository should save the expected JSON data."""

    output_file = tmp_path / "results" / "inspection.json"

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

    repository = JsonInspectionResultRepository(output_file)

    repository.save(result)

    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as file:
        saved_record = json.load(file)

    assert saved_record == {
        "reference_x": 200.0,
        "reference_y": 220.0,
        "measured_x": 210.0,
        "measured_y": 215.0,
        "offset_x": 10.0,
        "offset_y": -5.0,
        "distance": 11.1803398875,
        "tolerance": 20.0,
        "status": "PASS",
        "inspected_at": "2026-09-16T15:30:00",
    }
