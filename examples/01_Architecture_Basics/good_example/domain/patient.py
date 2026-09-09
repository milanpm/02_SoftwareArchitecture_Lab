"""
File Name: patient.py
Created Date: 2026-09-09
Author: Alex
Description:
    Defines the Patient domain entity and the business rules
    required to create valid patient information.
"""

from dataclasses import dataclass
from datetime import datetime


SUPPORTED_MODALITIES = frozenset({"CT", "MR", "CR", "DX"})


class PatientValidationError(ValueError):
    """Raised when patient information violates a domain rule."""


@dataclass(frozen=True)
class Patient:
    """Represent valid patient information."""

    patient_id: str
    patient_name: str
    modality: str
    registered_at: datetime

    def __post_init__(self) -> None:
        """Validate the patient immediately after creation."""

        if not self.patient_id.strip():
            raise PatientValidationError("Patient ID is required.")

        if not self.patient_name.strip():
            raise PatientValidationError("Patient name is required.")

        if self.modality not in SUPPORTED_MODALITIES:
            raise PatientValidationError(
                f"Unsupported modality: {self.modality}"
            )
