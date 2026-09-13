---
layout: default
title:
  'Keynote: Context is More Than Tools - Why the "C" in MCP is More Relevant
  Than Ever - Ryan Cooke'
nav_order: 41
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Ryan, an engineering lead at Work OS, discusses how his team leverages
  MCP concepts and protocol primitives to enhance the effectiveness of internal agents.
  Rather than focusing solely on authentication, he explains their development of
  a "...
resource: https://www.youtube.com/watch?v=685yFOg3aEo
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Ryan, an engineering lead at Work OS, discusses how his team leverages MCP concepts and protocol primitives to enhance the effectiveness of internal agents.
Rather than focusing solely on authentication, he explains their development of a "context engine," a multi-layered pipeline that injects task-specific context into agents before they interact with large language models (LLMs).
This engine comprises three layers: identity (determining who the agent represents and scoping authorization), per-integration context (both static and dynamic instructions tailored to tools and user roles), and a semantic layer (consistent definitions and language across agents).
These mechanisms ensure agents have precise, relevant context, enabling secure, auditable, and efficient tool usage while preventing context overload or insufficiency.
Ryan illustrates these concepts with examples from their internal applications, which generate temporary, interactive mini-apps for support and sales teams, and hints at an upcoming public launch based on this technology.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ryan, engineering lead at Work OS, speaking at MCP event.                                                                                                                                                                                                                                                                                                                                                                                                      |
|   2 | Work OS hosts MCP Night in San Francisco, bringing engineers and enthusiasts together.                                                                                                                                                                                                                                                                                                                                                                         |
|   3 | Work OS provides infrastructure for customers to secure MCP servers in production.                                                                                                                                                                                                                                                                                                                                                                             |
|   4 | Focus of talk: using MCP concepts and protocol primitives internally to empower company agents.                                                                                                                                                                                                                                                                                                                                                                |
|   5 | Tools enable models and LLMs to interact with the real world (e.g., create issues, query data, send messages).                                                                                                                                                                                                                                                                                                                                                 |
|   6 | Scaling tools within agents presents challenges: oversight, tool registries, and context management.                                                                                                                                                                                                                                                                                                                                                           |
|   7 | Managing the context window is crucial for agent effectiveness; too much or too little context causes issues.                                                                                                                                                                                                                                                                                                                                                  |
|   8 | Work OS built a "context engine"—a pipeline injecting task-specific context before LLM calls (pre-reasoning pipeline).                                                                                                                                                                                                                                                                                                                                         |
|   9 | Tool-first approach gives models a menu of tools, leading to uncertainty.                                                                                                                                                                                                                                                                                                                                                                                      |
|  10 | Context-first architecture resolves identity, resources, and injects semantic tool information for precise context.                                                                                                                                                                                                                                                                                                                                            |
|  11 | Context engine has three layers: 1. Identity: Uses OAuth to identify the user the agent represents; session scoping for short-lived authorization; auditability of agent actions. 2. Per-integration information: Static knowledge (system prompt) and dynamic context (task-specific, fetched as needed, disposed after use). 3. Semantic layer: Definitions and information specific to Work OS, enabling agents to use consistent language and definitions. |
|  12 | Example: Cloud code creates a project in Linear; mutation actions require human approval and short-lived session authority.                                                                                                                                                                                                                                                                                                                                    |
|  13 | Static instructions guide tool usage (e.g., pagination, identifier formats).                                                                                                                                                                                                                                                                                                                                                                                   |
|  14 | Dynamic context provides per-integration, per-identity instructions, fetched lazily to avoid context window bloat.                                                                                                                                                                                                                                                                                                                                             |
|  15 | Semantic understanding layer standardizes definitions (e.g., "sales transaction") across systems and agents.                                                                                                                                                                                                                                                                                                                                                   |
|  16 | Internal app built for support and sales teams generates interactive, short-lived applications for real-time company/customer info.                                                                                                                                                                                                                                                                                                                            |
|  17 | A                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=685yFOg3aEo)
