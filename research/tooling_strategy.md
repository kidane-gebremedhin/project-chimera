# Tooling Strategy — Git-MCP Setup (Project Chimera)

## Purpose
This document defines how **Git-MCP** is configured and used with **Cursor** to:
- Provide real-time repository awareness to the AI
- Enable traceability between specs and code
- Support controlled auto-commit / auto-push workflows

This setup applies to **Project Chimera**, an autonomous influencer system.

---

## MCP Overview

We use **Git-MCP** as the source-of-truth interface for:
- Repository structure
- File diffs
- Commit history
- Branch state

Git-MCP exposes Git as a Model Context Protocol (MCP) server, allowing Cursor to
reason about the repo before generating code.

---

## Git-MCP Server Configuration (Cursor)

Add the following configuration in:

**Cursor → Settings → MCP Servers**

```json
{
    "git": {
        "command": "git-mcp",
        "args": ["serve"]
    },
    "github": {
        "command": "docker",
        "args": ["run", "-i", "--rm", "mcp/github"],
        "env": {
            "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
        }
    }
}
