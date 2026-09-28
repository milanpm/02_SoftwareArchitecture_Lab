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
| 2 | SOLID: Single Responsibility Principle | Completed |
| 3 | SOLID: Open/Closed Principle | Completed |
| 4 | SOLID: Liskov Substitution Principle | Completed |

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

## Day 2 — Single Responsibility Principle

Day 2 applies the Single Responsibility Principle to a
center-alignment inspection program.

### Bad Example

The `InspectionProcessor` class contains multiple responsibilities:

- input validation
- center-offset calculation
- PASS/FAIL evaluation
- text report formatting
- JSON persistence
- console presentation

Although the program works, the class has several independent
reasons to change.

### Refactored Example

The improved version separates those responsibilities.

| Component | Responsibility |
|---|---|
| `InspectionResult` | Represent completed inspection data |
| `InspectionEvaluator` | Calculate displacement and determine PASS/FAIL |
| `InspectionReportFormatter` | Create a readable text report |
| `JsonInspectionResultRepository` | Persist the result as JSON |
| `ConsoleInspectionPresenter` | Display the result on the console |
| `main.py` | Create components and coordinate the workflow |

### Inspection Example

The example compares a reference center with a measured center.

```text
Reference : (200.00, 220.00)
Measured  : (210.00, 215.00)
Offset    : (10.00, -5.00)
Distance  : 11.18 px
Tolerance : 20.00 px
Result    : PASS
```

The distance is calculated as:

```text
distance = sqrt(offset_x² + offset_y²)
```

A result passes when:

```text
distance <= tolerance
```

The equality boundary is included, so a distance of exactly
`20.0 px` passes when the tolerance is `20.0 px`.

### Day 2 Tests

Day 2 adds isolated tests for:

- PASS evaluation
- FAIL evaluation
- equality boundary behavior
- invalid tolerance values
- deterministic inspection time
- report formatting
- JSON persistence
- console presentation

The complete project now contains 19 passing tests.

### Key SRP Lesson

> A module should have one reason to change.

SRP does not mean that every function needs its own class. Behaviors
that change for the same reason may remain together. Behaviors with
different reasons for change should be separated.

## Day 3 — Open/Closed Principle

Day 3 extends the center-alignment example with interchangeable decision
rules. The evaluator calculates offsets and the Euclidean distance, then
delegates PASS/FAIL to an `AlignmentRule`.

| Rule | PASS condition |
|---|---|
| `CircularRule` | `hypot(offset_x, offset_y) <= tolerance` |
| `PerAxisRule` | Both absolute offsets are at most `tolerance` |

For offsets `(16, 16)` and tolerance `20`, the circular rule fails
(distance `22.63`), while the per-axis rule passes. The example prints
the rule name so the result is interpretable even when distance exceeds
tolerance. A new rule implements the small `AlignmentRule` contract;
the evaluator needs no new condition or modification.

```bash
python examples/03_Open_Closed_Principle/main.py
python -m pytest
```

The Day 3 example is separate from Day 2, preserving its original
behavior and tests. The composition code must still select a rule.
This extension point is useful when alignment criteria vary by machine;
it would add needless complexity if there were only one stable rule.

## Day 4 — Liskov Substitution Principle

Day 4 checks whether different evaluation policies can replace one another
without breaking the code that uses them. For scores from 0 to 100,
each policy returns either `PASS` or `FAIL`.

| Policy | Passing score |
|---|---:|
| `BasicPolicy` | 60 or above |
| `StrictPolicy` | 80 or above |
| `SpecialPolicy` | 95 or above |

An earlier `SpecialPolicy` returned `EXCELLENT` or `NORMAL`. The calling
code expected `PASS` or `FAIL`, so it could not handle that policy as a
replacement. The corrected policy keeps its 95-point passing rule while
following the shared return value contract.

The example checks several scores for all three policies and verifies
the 94/95 boundary for `SpecialPolicy`.

```bash
python examples/04_Liskov_Substitution_Principle/day4_lsp.py
```

These checks cover the selected scores and return values. Input validation
and exception behavior would need separate checks if they become part of
the policy contract.

## Project Structure

```text
02_SoftwareArchitecture_Lab/
├── docs/
│   └── ROADMAP.md
├── examples/
│   ├── 01_Architecture_Basics/
│   │   ├── bad_example.py
│   │   └── good_example/
│   ├── 02_Single_Responsibility_Principle/
│       ├── bad_example.py
│       └── good_example/
│           ├── __init__.py
│           ├── console_presenter.py
│           ├── inspection_evaluator.py
│           ├── inspection_result.py
│           ├── main.py
│           ├── report_formatter.py
│           └── result_repository.py
│   ├── 03_Open_Closed_Principle/
│   │   ├── alignment_rules.py
│   │   ├── ocp_inspection_evaluator.py
│   │   └── main.py
│   └── 04_Liskov_Substitution_Principle/
│       └── day4_lsp.py
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

## Run the Day 2 Bad Example

```bash
python examples/02_Single_Responsibility_Principle/bad_example.py
```

## Run the Day 2 Refactored Example

```bash
python examples/02_Single_Responsibility_Principle/good_example/main.py
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
