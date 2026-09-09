"""
File Name: bad_example.py
Created Date: 2026-09-09
Author: Alex
Description:
    Demonstrates a poorly structured patient registration program
    in which user input, validation, business rules, file storage,
    and output presentation are mixed in a single function.
"""

import json
from datetime import datetime
from pathlib import Path


def register_patient() -> None:
    """Receive, validate, save, and display patient information."""

    # User input
    patient_id = input("Patient ID: ").strip()
    patient_name = input("Patient Name: ").strip()
    modality = input("Modality (CT/MR/CR/DX): ").strip().upper()

    # Validation
    if not patient_id:
        print("Error: Patient ID is required.")
        return

    if not patient_name:
        print("Error: Patient name is required.")
        return

    allowed_modalities = {"CT", "MR", "CR", "DX"}

    if modality not in allowed_modalities:
        print(f"Error: Unsupported modality: {modality}")
        return

    # Business data creation
    patient = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "modality": modality,
        "registered_at": datetime.now().isoformat(timespec="seconds"),
    }

    # File-system handling
    data_directory = Path("data")
    data_directory.mkdir(exist_ok=True)

    output_file = data_directory / "patients.json"

    if output_file.exists():
        with output_file.open("r", encoding="utf-8") as file:
            patients = json.load(file)
    else:
        patients = []

    # Duplicate checking
    for saved_patient in patients:
        if saved_patient["patient_id"] == patient_id:
            print(f"Error: Patient ID {patient_id} already exists.")
            return

    # Data persistence
    patients.append(patient)

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(patients, file, indent=4, ensure_ascii=False)

    # Result presentation
    print()
    print("Patient registered successfully.")
    print(f"Patient ID : {patient_id}")
    print(f"Name       : {patient_name}")
    print(f"Modality   : {modality}")
    print(f"Saved to   : {output_file}")


if __name__ == "__main__":
    register_patient()
