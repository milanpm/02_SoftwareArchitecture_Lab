# Software Architecture Lab

A hands-on learning project for understanding software architecture
through implementation, testing, and architectural documentation.

## Project Goal

This project explores how to design software that is:

- understandable
- testable
- maintainable
- replaceable
- extensible

Each topic compares structural problems with an improved design.

## Current Progress

| Day | Topic | Status |
|---:|---|:---:|
| 1 | Architecture Basics and Separation of Concerns | Completed |
| 2 | SOLID: Single Responsibility Principle | Next |

## Day 1 — Architecture Basics

Day 1 compares two patient registration programs that provide the
same functionality but use different structures.

### Bad Example

`bad_example.py` mixes multiple responsibilities in one function:

- console input
- validation
- business rules
- duplicate checking
- JSON persistence
- result presentation

The program works, but it is difficult to test and change.

### Layered Example

The improved example separates the application into four layers.

| Layer | Responsibility |
|---|---|
| Presentation | Console input and output |
| Application | Patient registration workflow |
| Domain | Patient data and business rules |
| Infrastructure | JSON file persistence |

### Dependency Flow

```text
Presentation
     |
     v
Application -----> Domain
     |
     v
Repository abstraction
     ^
     |
Infrastructure
```

The Application Layer depends on the repository abstraction rather
than directly depending on JSON storage.

## Project Structure

```text
02_SoftwareArchitecture_Lab/
├── docs/
│   └── ROADMAP.md
├── examples/
│   └── 01_Architecture_Basics/
│       ├── bad_example.py
│       └── good_example/
│           ├── application/
│           ├── domain/
│           ├── infrastructure/
│           ├── presentation/
│           └── main.py
├── tests/
│   ├── test_json_patient_repository.py
│   ├── test_patient.py
│   └── test_register_patient.py
├── .gitignore
├── pyproject.toml
├── requirements-dev.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Run the Bad Example

```bash
python examples/01_Architecture_Basics/bad_example.py
```

## Run the Layered Example

```bash
python examples/01_Architecture_Basics/good_example/main.py
```

## Run Tests

```bash
pytest
```

## Day 1 Results

- 4 architectural layers
- 1 repository abstraction
- dependency injection
- composition root
- immutable domain entity
- isolated automated tests
- 11 passing tests

## Key Lesson

> Working code is not necessarily well-designed code.

Good architecture separates code according to its responsibilities
and reasons for change.

## Author

Alex
