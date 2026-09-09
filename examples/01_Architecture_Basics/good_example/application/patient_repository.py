"""
File Name: patient_repository.py
Created Date: 2026-09-09
Author: Alex
Description:
    Defines the repository abstraction required by the patient
    registration use case without depending on a storage technology.
"""

from abc import ABC, abstractmethod

from domain.patient import Patient


class PatientRepository(ABC):
    """Define patient persistence operations required by the application."""

    @abstractmethod
    def exists_by_id(self, patient_id: str) -> bool:
        """Return whether a patient with the given ID already exists."""

    @abstractmethod
    def save(self, patient: Patient) -> None:
        """Persist a patient."""
