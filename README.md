## Project Chimera

Project Chimera is an **autonomous influencer system**: a network of AI-driven agents that can perceive trends, generate content, and operate on social platforms with minimal human oversight while preserving strong safety and governance guarantees.

The system is built to be **spec-first**, **test-driven**, and **governed by clear contracts** so that both humans and AI agents can collaborate safely.

---

## High-Level Goals

- **Autonomous content lifecycle**  
  From trend discovery to publication, agents can plan, create, and distribute short-form content.

- **Safety and governance by design**  
  Every action passes through a Planner–Worker–Judge hierarchy, with structured decisions and audit trails.

- **Agentic interoperability**  
  Agents expose clear APIs and integrate with external ecosystems (e.g., via MCP and OpenClaw) without leaking private state.

---

## Core Concepts

- **Agents**  
  Long-lived digital entities operating under personas and constraints, not one-off scripts.

- **Skills** (`skills/`)  
  Modular capabilities (fetching trends, generating scripts/videos, publishing) that agents invoke via well-defined contracts.

- **Specs** (`specs/`)  
  - `technical.md` – API contracts, data schemas, and ER diagrams  
  - `functional.md` – user stories and behavioral requirements  
  - `_meta.md` – vision and hard constraints

- **Tasks, Results, Decisions**  
  Planner → Worker → Judge interactions are represented as structured messages and persisted in the database for traceability.

---

## Architecture & Tooling (High Level)

- **Language & Runtime**: Python (>= 3.12)  
- **Dependency & Environment Management**: `uv` (project + dev dependencies)  
- **Testing**: `pytest` with **TDD-first** approach (tests may intentionally fail while contracts are being defined)  
- **Containerization**: Dockerfile encapsulating the dev/test environment  
- **Automation**: `Makefile` for standard workflows (`make setup`, `make test`, `make spec-check`)  
- **CI & AI Governance**:  
  - GitHub Actions workflow (`.github/workflows/main.yml`) runs tests and spec checks on every push/PR  
  - `.coderabbit.yaml` configures AI code review to enforce spec alignment, contract adherence, security checks, and scope control

---

## Working With the Project (Overview)

- **Run tests locally**  
  Use `uv` and `pytest` as described in `tests/README.md`. Early stages assume red tests while interfaces are being designed.

- **Inspect specs and contracts**  
  Start from `specs/technical.md` and `skills/README.md` to understand the expected behavior and data shapes before writing code.

- **Extend capabilities**  
  New skills and behaviors must be added **spec-first**, with contracts in `specs/` and tests in `tests/` before implementations under `skills/` or other modules.

No secrets, credentials, or environment-specific values are stored in this README. Configuration details should be managed via environment variables or secure secret stores. 
