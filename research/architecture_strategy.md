# Architecture Strategy: Project Chimera Autonomous Influencer Network

## Agent Pattern: Hierarchical Swarm (FastRender)
We have selected the **Hierarchical Swarm** pattern over a sequential chain to ensure system resilience and high-volume throughput.

* **The Planner (The Brain):** Decomposes high-level campaign goals into a task-based DAG (Directed Acyclic Graph).
* **The Workers (The Muscle):** Specialized, stateless agents (Content Creator, Engagement Bot, Financial Auditor) that execute atomic tasks via MCP.
* **The Judge (The Filter):** An independent agent that validates all outputs against the `SOUL.md` persona and ethical safety rails.



## Human-in-the-Loop (HITL) Safety Layer
To maintain brand safety while allowing autonomy, we use a **Confidence-Based Escalation** model:

| Confidence Score | Action Type | Human Involvement |
| :--- | :--- | :--- |
| **0.90 - 1.00** | Auto-Approve | None (Logged only) |
| **0.70 - 0.89** | Review Required | Human must "Thumbs Up" in Dashboard |
| **< 0.70** | Reject/Retry | Auto-regenerated with feedback |

## Data Strategy: High-Velocity Hybrid Model
Storing video metadata and agent memories requires a two-tier approach:

* **NoSQL/Vector (Weaviate):** Used for "Episodic Memory." High-velocity video metadata and past interactions are stored as vectors to allow agents to "remember" context through semantic search.

## System Architecture Diagram

```mermaid
graph TD
    subgraph "Orchestration Layer"
        P[Planner Agent] -->|Assigns| W[Worker Swarm]
        W -->|Submits| J[Judge Agent]
    end

    subgraph "Safety & State"
        J -->|Conf < 0.9| HITL[Human Review]
        J -->|Conf > 0.9| DB[(PostgreSQL)]
        HITL -->|Override/Approve| DB
    end

    subgraph "External World (MCP)"
        DB -->|Trigger| MCP[MCP Server]
        MCP -->|API| TW[Twitter/X]
        MCP -->|On-Chain| CB[Coinbase AgentKit]
    end