"""
File Name: test_json_patient_repository.py
Created Date: 2026-09-09
Author: Alex
Description:
    Verifies that the JSON patient repository saves and retrieves
    patient information without modifying the project data directory.
"""

import json
from datetime import datetime
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GOOD_EXAMPLE_PATH = (
    PROJECT_ROOT
    / "examples"
    / "01_Architecture_Basics"
    / "good_example"
)

sys.path.insert(0, str(GOOD_EXAMPLE_PATH))

from domain.patient import Patient  # noqa: E402
from infrastructure.json_patient_repository import (  # noqa: E402
    JsonPatientRepository,
)


def create_patient(patient_id: str = "P001") -> Patient:
    """Create a valid patient for repository tests."""

    return Patient(
        patient_id=patient_id,
        patient_name="Alex Kim",
        modality="CT",
        registered_at=datetime(2026, 9, 9, 22, 30, 0),
    )


def test_save_patient_to_json_file(tmp_path: Path) -> None:
    """Saving a patient should create a valid JSON file."""

    file_path = tmp_path / "data" / "patients.json"
    repository = JsonPatientRepository(file_path)
    patient = create_patient()

    repository.save(patient)

    assert file_path.exists()

    with file_path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    assert records == [
        {
            "patient_id": "P001",
            "patient_name": "Alex Kim",
            "modality": "CT",
            "registered_at": "2026-09-09T22:30:00",
        }
    ]


def test_find_existing_patient_id(tmp_path: Path) -> None:
    """A saved patient ID should be found by the repository."""

    file_path = tmp_path / "patients.json"
    repository = JsonPatientRepository(file_path)

    repository.save(create_patient("P001"))

    assert repository.exists_by_id("P001") is True
    assert repository.exists_by_id("P999") is False


def test_data_survives_repository_recreation(tmp_path: Path) -> None:
    """A new repository instance should read previously saved data."""

    file_path = tmp_path / "patients.json"

    first_repository = JsonPatientRepository(file_path)
    first_repository.save(create_patient("P001"))

    second_repository = JsonPatientRepository(file_path)

    assert second_repository.exists_by_id("P001") is True
