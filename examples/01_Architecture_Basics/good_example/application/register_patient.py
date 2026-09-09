"""
File Name: register_patient.py
Created Date: 2026-09-09
Author: Alex
Description:
    Implements the patient registration use case by coordinating
    validation, duplicate checking, and repository persistence.
"""

from collections.abc import Callable
from datetime import datetime

from application.patient_repository import PatientRepository
from domain.patient import Patient


class DuplicatePatientError(ValueError):
    """Raised when a patient ID already exists."""


class RegisterPatientService:
    """Coordinate the patient registration use case."""

    def __init__(
        self,
        repository: PatientRepository,
        clock: Callable[[], datetime] = datetime.now,
    ) -> None:
        """Initialize the service with its external dependencies."""

        self._repository = repository
        self._clock = clock

    def register(
        self,
        patient_id: str,
        patient_name: str,
        modality: str,
    ) -> Patient:
        """Validate, create, and persist a patient."""

        normalized_patient_id = patient_id.strip()
        normalized_patient_name = patient_name.strip()
        normalized_modality = modality.strip().upper()

        if self._repository.exists_by_id(normalized_patient_id):
            raise DuplicatePatientError(
                f"Patient ID {normalized_patient_id} already exists."
            )

        patient = Patient(
            patient_id=normalized_patient_id,
            patient_name=normalized_patient_name,
            modality=normalized_modality,
            registered_at=self._clock(),
        )

        self._repository.save(patient)

        return patient
