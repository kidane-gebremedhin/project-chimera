## specs/openclaw_integration.md — OpenClaw Status Publishing (Optional)

### Objective

Enable Project Chimera agents to broadcast **availability and status** to the OpenClaw Agent Social Network.

### Status Signals

Each agent periodically publishes:

* Agent ID
* Current state (idle, working, awaiting_review)
* Supported capabilities (content, replies, commerce)
* Trust level (confidence average)

### Transport

* MCP Server exposing `agent://status/{agent_id}` resource
* Read-only, non-sensitive

### Example Payload

```json
{
  "agent_id": "uuid",
  "state": "working",
  "capabilities": ["content", "commerce"],
  "confidence_avg": 0.92
}
```

### Governance

* No private memory or financial data exposed
* Status is advisory, not authoritative
* Human operator can disable broadcasting per agent
