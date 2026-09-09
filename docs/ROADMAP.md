# Software Architecture Expert Roadmap

## Objective

Build practical software architecture skills through small examples,
automated tests, architectural documentation, and existing project
refactoring.

The learning process focuses on explaining:

- component responsibilities
- dependency direction
- architectural decisions
- design trade-offs
- testing strategies
- operational concerns

## Phase 1 — Architecture Foundations

| Day | Topic | Practice |
|---:|---|---|
| 1 | Architecture Basics | Compare mixed and layered structures |
| 2 | Single Responsibility Principle | Separate reasons for change |
| 3 | Open/Closed Principle | Extend behavior without modification |
| 4 | Liskov and Interface Segregation | Design safe, focused interfaces |
| 5 | Dependency Inversion | Replace concrete dependencies |

## Phase 2 — Application Design

| Day | Topic | Practice |
|---:|---|---|
| 6 | Dependency Injection | Constructor and composition-root design |
| 7 | Repository Pattern | Replace JSON with SQLite |
| 8 | Service and Use Case Patterns | Separate workflows from domain rules |
| 9 | Error Handling | Define errors across architectural boundaries |
| 10 | Configuration and Logging | Remove environment details from core logic |

## Phase 3 — Architecture Styles

| Day | Topic | Practice |
|---:|---|---|
| 11 | Layered Architecture | Evaluate dependency and responsibility boundaries |
| 12 | Clean Architecture | Apply entities, use cases, and adapters |
| 13 | Hexagonal Architecture | Design ports and adapters |
| 14 | Modular Monolith | Build independently changeable modules |
| 15 | Event-Driven Architecture | Publish and handle domain events |

## Phase 4 — System Architecture

| Day | Topic | Practice |
|---:|---|---|
| 16 | API Design | Design resource and operation boundaries |
| 17 | Database Architecture | Transactions, consistency, and migrations |
| 18 | Distributed Systems | Latency, failure, and partial availability |
| 19 | Reliability Patterns | Retry, timeout, circuit breaker, and idempotency |
| 20 | Observability | Logging, metrics, tracing, and health checks |

## Phase 5 — Architecture Practice

| Day | Topic | Practice |
|---:|---|---|
| 21 | Quality Attributes | Performance, security, and maintainability |
| 22 | Architecture Decision Records | Document decisions and trade-offs |
| 23 | C4 Model | Document system context and containers |
| 24 | Architecture Evaluation | Identify risks and architectural smells |
| 25 | Capstone Design | Design a medical imaging platform |

## Capstone Direction

The final project will apply the learned concepts to a system related
to Alex's professional experience.

Candidate system:

- medical imaging platform
- DICOM/PACS gateway
- industrial machine-vision platform
- equipment integration and monitoring system

The capstone will include:

1. requirements
2. quality attributes
3. system context
4. component responsibilities
5. dependency rules
6. data and communication flows
7. failure-handling strategy
8. testing strategy
9. Architecture Decision Records
10. deployment and operation plan

## Learning Method

Each day should include:

1. concept
2. structural problem
3. implementation
4. automated tests
5. architecture diagram
6. trade-off analysis
7. short retrospective
8. Git commit
9. blog post
