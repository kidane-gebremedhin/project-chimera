# OpenClaw Integration Plan

## Objective
Enable Project Chimera agents to broadcast **availability and status** to the OpenClaw Agent Social Network which allows for automated sponsorship bidding.

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

## Implementation Plan
1. **Status Heartbeat:** A background task running in `uv` sends a signed JSON payload every 60 seconds.
2. **Availability Payload:**
   ```json
   {
     "agent_id": "chimera_v1",
     "status": "idle | busy",
     "capabilities": ["video_gen", "twitter_post"],
     "current_bid_price": "0.05 ETH"
   }

### Governance

* No private memory or financial data exposed
* Status is advisory, not authoritative
* Human operator can disable broadcasting per agent
