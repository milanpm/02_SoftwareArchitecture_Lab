"""
File Name: main.py
Created Date: 2026-09-09
Author: Alex
Description:
    Acts as the composition root that creates and connects the
    presentation, application, and infrastructure components.
"""

from pathlib import Path

from application.register_patient import RegisterPatientService
from infrastructure.json_patient_repository import JsonPatientRepository
from presentation.console import PatientRegistrationConsole


def main() -> None:
    """Create the application dependencies and start the program."""

    repository = JsonPatientRepository(
        Path("data/layered_patients.json")
    )
    service = RegisterPatientService(repository)
    console = PatientRegistrationConsole(service)

    console.run()


if __name__ == "__main__":
    main()
