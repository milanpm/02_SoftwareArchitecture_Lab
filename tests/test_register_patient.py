"""
File Name: test_register_patient.py
Created Date: 2026-09-09
Author: Alex
Description:
    Verifies the patient registration use case with an in-memory
    repository and a fixed clock.
"""

from datetime import datetime
from pathlib import Path
import sys

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GOOD_EXAMPLE_PATH = (
    PROJECT_ROOT
    / "examples"
    / "01_Architecture_Basics"
    / "good_example"
)

sys.path.insert(0, str(GOOD_EXAMPLE_PATH))

from application.patient_repository import PatientRepository  # noqa: E402
from application.register_patient import (  # noqa: E402
    DuplicatePatientError,
    RegisterPatientService,
)
from domain.patient import Patient, PatientValidationError  # noqa: E402


class InMemoryPatientRepository(PatientRepository):
    """Store patients in memory for application tests."""

    def __init__(self) -> None:
        """Initialize an empty patient collection."""

        self.patients: dict[str, Patient] = {}

    def exists_by_id(self, patient_id: str) -> bool:
        """Return whether the patient ID is already stored."""

        return patient_id in self.patients

    def save(self, patient: Patient) -> None:
        """Store a patient in memory."""

        self.patients[patient.patient_id] = patient


def fixed_clock() -> datetime:
    """Return a deterministic time for tests."""

    return datetime(2026, 9, 9, 22, 0, 0)


def test_register_patient_successfully() -> None:
    """Valid input should create and save a patient."""

    repository = InMemoryPatientRepository()
    service = RegisterPatientService(repository, fixed_clock)

    patient = service.register(
        patient_id=" P001 ",
        patient_name=" Alex Kim ",
        modality=" ct ",
    )

    assert patient.patient_id == "P001"
    assert patient.patient_name == "Alex Kim"
    assert patient.modality == "CT"
    assert patient.registered_at == fixed_clock()
    assert repository.patients["P001"] == patient


def test_reject_duplicate_patient_id() -> None:
    """A duplicate patient ID should not be registered."""

    repository = InMemoryPatientRepository()
    service = RegisterPatientService(repository, fixed_clock)

    service.register("P001", "Alex Kim", "CT")

    with pytest.raises(
        DuplicatePatientError,
        match="Patient ID P001 already exists.",
    ):
        service.register("P001", "Another Patient", "MR")

    assert len(repository.patients) == 1


def test_invalid_patient_is_not_saved() -> None:
    """Invalid domain data should never reach the repository."""

    repository = InMemoryPatientRepository()
    service = RegisterPatientService(repository, fixed_clock)

    with pytest.raises(
        PatientValidationError,
        match="Unsupported modality: US",
    ):
        service.register("P001", "Alex Kim", "US")

    assert repository.patients == {}
