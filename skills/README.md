# Chimera Agent Skills (Runtime)

## Overview

In Project Chimera, a **Skill** is a modular, runtime-executable capability that an autonomous agent can invoke to perform a well-defined task. Skills are:

* **Composable**: chained or orchestrated by higher-level agent planners
* **Contract-driven**: strict input/output schemas
* **Observable**: every execution emits metadata for audit and learning
* **Replaceable**: implementations can evolve without breaking agents

This document defines the initial **critical skill set** required to operate an Autonomous Influencer Network, based on the SRS and referenced research.

---

## Skill Design Principles

1. **Pure Interfaces First**
   Skills expose contracts before implementation.
2. **Side Effects Are Explicit**
   Network calls, storage, and publishing are declared.
3. **Machine-to-Machine Ready**
   Inputs/outputs are designed for agent consumption, not humans.
4. **Failure Is a First-Class Output**
   Skills return structured errors, never silent failures.

---

## Skill 1: `skill_fetch_trends`

### Purpose

Fetches real-time or near-real-time trending topics from external platforms (e.g., social media, news, or platform APIs) to inform content ideation.

### Inputs

```json
{
  "platform": "string",
  "region": "string",
  "category": "string | null",
  "limit": "number"
}
```

### Outputs

```json
{
  "trends": [
    {
      "topic": "string",
      "score": "number",
      "source": "string",
      "observed_at": "ISO-8601 timestamp"
    }
  ],
  "metadata": {
    "platform": "string",
    "fetched_at": "ISO-8601 timestamp"
  }
}
```

### Failure Modes

* API unavailable
* Rate limited
* Invalid region or category

---

## Skill 2: `skill_generate_script`

### Purpose

Transforms trends or prompts into a short-form video script aligned with the agent’s persona, tone, and safety constraints.

### Inputs

```json
{
  "trend_topic": "string",
  "persona_id": "string",
  "target_duration_seconds": "number",
  "language": "string"
}
```

### Outputs

```json
{
  "script": {
    "text": "string",
    "estimated_duration_seconds": "number"
  },
  "safety_flags": ["string"],
  "confidence_score": "number"
}
```

### Failure Modes

* Safety policy violation
* Low confidence score
* Unsupported language

---

## Skill 3: `skill_generate_video`

### Purpose

Generates a short-form video asset from an approved script using templates, avatars, or media generation backends.

### Inputs

```json
{
  "script_text": "string",
  "persona_id": "string",
  "video_style": "string",
  "aspect_ratio": "string",
  "language": "string"
}
```

### Outputs

```json
{
  "video_asset_id": "string",
  "duration_seconds": "number",
  "preview_url": "string",
  "generation_metadata": {
    "engine": "string",
    "generated_at": "ISO-8601 timestamp"
  }
}
```

### Failure Modes

* Generation backend unavailable
* Unsupported style or aspect ratio
* Safety or content filter rejection

---

## Skill 4: `skill_publish_video`

### Purpose

Publishes finalized video content to a target platform and reports delivery status back to the agent.

### Inputs

```json
{
  "platform": "string",
  "video_asset_id": "string",
  "caption": "string",
  "hashtags": ["string"],
  "schedule_time": "ISO-8601 timestamp | null"
}
```

### Outputs

```json
{
  "publication_status": "SUCCESS | FAILED | SCHEDULED",
  "platform_post_id": "string | null",
  "published_at": "ISO-8601 timestamp | null",
  "error": {
    "code": "string",
    "message": "string"
  } | null
}
```

### Failure Modes

* Authentication expired
* Asset not found
* Platform rejection

---

## Skill Lifecycle

1. **Registered** – Skill contract is known to the agent
2. **Selected** – Planner chooses the skill
3. **Executed** – Runtime invocation
4. **Observed** – Metrics and outcomes logged
5. **Learned From** – Results feed future planning

---

## Forward Compatibility

Future skills may include:

* `skill_edit_video`
* `skill_clone_voice`
* `skill_negotiate_brand_deal`
* `skill_publish_availability` (OpenClaw)

All new skills must follow the same contract-first approach defined here.
