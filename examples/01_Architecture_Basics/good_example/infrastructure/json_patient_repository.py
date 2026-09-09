"""
File Name: json_patient_repository.py
Created Date: 2026-09-09
Author: Alex
Description:
    Implements patient persistence with a JSON file while conforming
    to the repository interface defined by the application layer.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from application.patient_repository import PatientRepository
from domain.patient import Patient


class JsonPatientRepository(PatientRepository):
    """Persist patient information in a JSON file."""

    def __init__(self, file_path: Path) -> None:
        """Initialize the repository with its storage path."""

        self._file_path = file_path

    def exists_by_id(self, patient_id: str) -> bool:
        """Return whether the patient ID already exists."""

        return any(
            patient.patient_id == patient_id
            for patient in self._load_patients()
        )

    def save(self, patient: Patient) -> None:
        """Append a patient and persist the updated collection."""

        patients = self._load_patients()
        patients.append(patient)
        self._write_patients(patients)

    def _load_patients(self) -> list[Patient]:
        """Load patients from the JSON file."""

        if not self._file_path.exists():
            return []

        with self._file_path.open("r", encoding="utf-8") as file:
            records: list[dict[str, Any]] = json.load(file)

        return [
            Patient(
                patient_id=record["patient_id"],
                patient_name=record["patient_name"],
                modality=record["modality"],
                registered_at=datetime.fromisoformat(
                    record["registered_at"]
                ),
            )
            for record in records
        ]

    def _write_patients(self, patients: list[Patient]) -> None:
        """Write patients to the JSON file."""

        self._file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        records = [
            {
                "patient_id": patient.patient_id,
                "patient_name": patient.patient_name,
                "modality": patient.modality,
                "registered_at": patient.registered_at.isoformat(
                    timespec="seconds"
                ),
            }
            for patient in patients
        ]

        with self._file_path.open("w", encoding="utf-8") as file:
            json.dump(
                records,
                file,
                indent=4,
                ensure_ascii=False,
            )
