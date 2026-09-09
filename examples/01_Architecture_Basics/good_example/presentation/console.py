"""
File Name: console.py
Created Date: 2026-09-09
Author: Alex
Description:
    Provides the console-based user interface for patient registration
    without containing business rules or persistence logic.
"""

from application.register_patient import (
    DuplicatePatientError,
    RegisterPatientService,
)
from domain.patient import PatientValidationError


class PatientRegistrationConsole:
    """Handle console input and output for patient registration."""

    def __init__(self, service: RegisterPatientService) -> None:
        """Initialize the console with the registration service."""

        self._service = service

    def run(self) -> None:
        """Collect input, execute the use case, and display its result."""

        patient_id = input("Patient ID: ")
        patient_name = input("Patient Name: ")
        modality = input("Modality (CT/MR/CR/DX): ")

        try:
            patient = self._service.register(
                patient_id=patient_id,
                patient_name=patient_name,
                modality=modality,
            )
        except (PatientValidationError, DuplicatePatientError) as error:
            print(f"Error: {error}")
            return

        print()
        print("Patient registered successfully.")
        print(f"Patient ID : {patient.patient_id}")
        print(f"Name       : {patient.patient_name}")
        print(f"Modality   : {patient.modality}")
        print(
            "Registered : "
            f"{patient.registered_at.isoformat(timespec='seconds')}"
        )
