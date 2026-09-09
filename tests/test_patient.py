"""
File Name: test_patient.py
Created Date: 2026-09-09
Author: Alex
Description:
    Verifies the Patient domain entity, including successful creation,
    validation failures, and immutability.
"""

from dataclasses import FrozenInstanceError
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

from domain.patient import Patient, PatientValidationError  # noqa: E402


def test_create_valid_patient() -> None:
    """A patient should be created when all values are valid."""

    registered_at = datetime(2026, 9, 9, 21, 30, 0)

    patient = Patient(
        patient_id="P001",
        patient_name="Alex Kim",
        modality="CT",
        registered_at=registered_at,
    )

    assert patient.patient_id == "P001"
    assert patient.patient_name == "Alex Kim"
    assert patient.modality == "CT"
    assert patient.registered_at == registered_at


def test_reject_empty_patient_id() -> None:
    """An empty patient ID should be rejected."""

    with pytest.raises(
        PatientValidationError,
        match="Patient ID is required.",
    ):
        Patient(
            patient_id="",
            patient_name="Alex Kim",
            modality="CT",
            registered_at=datetime.now(),
        )


def test_reject_empty_patient_name() -> None:
    """An empty patient name should be rejected."""

    with pytest.raises(
        PatientValidationError,
        match="Patient name is required.",
    ):
        Patient(
            patient_id="P001",
            patient_name="",
            modality="CT",
            registered_at=datetime.now(),
        )


def test_reject_unsupported_modality() -> None:
    """An unsupported modality should be rejected."""

    with pytest.raises(
        PatientValidationError,
        match="Unsupported modality: US",
    ):
        Patient(
            patient_id="P001",
            patient_name="Alex Kim",
            modality="US",
            registered_at=datetime.now(),
        )


def test_patient_is_immutable() -> None:
    """Patient information should not change after creation."""

    patient = Patient(
        patient_id="P001",
        patient_name="Alex Kim",
        modality="CT",
        registered_at=datetime.now(),
    )

    with pytest.raises(FrozenInstanceError):
        patient.patient_id = "P999"
