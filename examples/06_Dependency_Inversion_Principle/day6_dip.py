# =============================================================================
# File        : day6_dip.py
# Project     : 02_SoftwareArchitecture_Lab
# Day         : 6
# Topic       : Dependency Inversion Principle (DIP)
# Author      : Alex
# Created     : 2026-10-16
# Description : Depend on the ResultWriter abstraction and inject a concrete
#               writer to change how inspection results are recorded.
# Execution   : Run from the repository root:
#               python examples/06_Dependency_Inversion_Principle/day6_dip.py
# Output      : day6_inspection_results.txt
#               Appended to the current working directory.
# =============================================================================

from abc import ABC, abstractmethod


class ResultWriter(ABC):
    """Define a common interface for recording inspection results."""

    @abstractmethod
    def write(self, result: str) -> None:
        pass


class ConsoleResultWriter(ResultWriter):
    """Print inspection results to the console."""

    def write(self, result: str) -> None:
        print(f"[CONSOLE] {result}")


class FileResultWriter(ResultWriter):
    """Append inspection results to a text file."""

    def __init__(self, path: str):
        self.path = path

    def write(self, result: str) -> None:
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(result + "\n")

        print(f"[FILE] {result} -> {self.path}")


class InspectionService:
    """Evaluate object size and record the inspection result."""

    def __init__(self, writer: ResultWriter):
        self.writer = writer

    def inspect(self, measured_size: float) -> str:
        # Accept sizes within 150 +/- 8, including both boundaries.
        result = "PASS" if 142 <= measured_size <= 158 else "FAIL"
        self.writer.write(result)
        return result


def main() -> None:
    print("=== Scenario 1: Console output ===")
    console_service = InspectionService(ConsoleResultWriter())
    console_service.inspect(150)

    print("\n=== Scenario 2: File output ===")
    file_service = InspectionService(
        FileResultWriter("day6_inspection_results.txt")
    )
    file_service.inspect(170)


if __name__ == "__main__":
    main()
