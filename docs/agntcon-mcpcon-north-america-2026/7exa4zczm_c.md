---
layout: default
title: "Before the Agent Writes Code: Policy-Aware Engines for AI Coding - Nnenna Ndukwe, Qodo"
nav_order: 70
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Nina Indukwe, Developer Relations Lead at Coda, presents "Policy Nym," an open-source MCP server and CLI tool designed to implement a "shift-left" approach in AI coding by injecting engineering pol...'
resource: "https://www.youtube.com/watch?v=7exa4ZcZM_c"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Nina Indukwe, Developer Relations Lead at Coda, presents "Policy Nym," an open-source MCP server and command-line tool designed to implement a "shift-left" approach in AI coding by injecting engineering policies into the planning phase.
The tool allows coding agents to retrieve relevant engineering standards from a library of 26 markdown-based policies, which can be customized with team-specific rules, ensuring that initial code implementations reflect established quality decisions and reduce later rework.
By using vector search and reranking to match coding tasks with specific policy sources, Policy Nym provides agents with cited evidence and constraints, such as keeping secrets out of logs, before code generation begins.
This process enables the creation of testable adherence checks, allowing teams to verify that the generated code strictly follows the retrieved rules across planning, implementation, and review stages.
Indukwe demonstrates this workflow using an authentication logging task, showing how the system ensures safe error handling and secret exclusion, while also discussing the integration of such policy-aware engines into broader software development lifecycle workflows for consistent code quality.

# Main Points

|   # | Main point                                                                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , Developer Relations Lead at Coda, presented "Policy Nym," an open-source MCP server and command-line tool designed to apply engineering policies to AI coding agents before code generation begins.                                                    |
|   2 | "shift-left" approach, bringing quality-driven decisions earlier in the software development lifecycle (SDLC) to reduce rework and ensure initial implementations reflect established team standards.                                                    |
|   3 | , ensuring that generated plans and code adhere to specific constraints such as security, logging standards, and architectural patterns.                                                                                                                 |
|   4 | , but teams can add their own custom policies via a tunnel file and profile configuration.                                                                                                                                                               |
|   5 | , Pydantic for input/output validation, and a local SQLite index with vector search capabilities (SQLite vec) to match coding tasks with relevant policy sections.                                                                                       |
|   6 | : `policy search` for exploring relevant passages, `policy compile` for packaging selected policies, `policy preflight` for returning relevant sources for a specific task, and `policy preflight evidence` for recording the sources and passages used. |
|   7 | , creating embeddings, and using vector search combined with a reranker to identify the most relevant policies for a given coding task.                                                                                                                  |
|   8 | ; Policy Nym retrieved specific logging policies to guide the agent’s plan.                                                                                                                                                                              |
|   9 | , such as injecting fake secrets into errors to verify they do not appear in application logs or security events, ensuring code adherence to the retrieved policies.                                                                                     |
|  10 | , this approach is part of a broader platform that integrates code-based context, engineering rules, and agentic AI code review to maintain consistency across the entire SDLC.                                                                          |
|  11 | , version, and line numbers, allowing developers to inspect the basis for any rule applied by the agent.                                                                                                                                                 |
|  12 | , with recent updates focused on optimizing performance and token usage, though benchmarks indicate marginal latency improvements when using specific models like Jev.                                                                                   |
|  13 | , meaning the MCP server does not make external search calls for policies but rather searches a local index of preloaded Markdown files, ensuring data privacy and speed.                                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7exa4ZcZM_c/hqdefault.jpg)]("https://www.youtube.com/watch?v=7exa4ZcZM_c")

[Watch on YouTube](https://www.youtube.com/watch?v=7exa4ZcZM_c)
