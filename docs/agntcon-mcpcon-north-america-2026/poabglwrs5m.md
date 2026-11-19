---
layout: default
title: "Governing MCP at Scale: Enforcing Agentic Architecture From Code Generation... Marc Daniel Registre"
nav_order: 145
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: Mark presents a solution for governing Model Context Protocol (MCP) at scale by deterministically enforcing architectural boundaries during code generation and merging.
resource: "https://www.youtube.com/watch?v=POAbGlwrS5M"
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

Mark presents a solution for governing Model Context Protocol (MCP) at scale by deterministically enforcing architectural boundaries during code generation and merging.
He argues that relying on probabilistic models to detect architectural drift is insufficient, advocating instead for a machine-readable architecture defined as a schema-validated JSON file that serves as the source of truth.
Using the open standard CALM, teams can define nodes, relationships, and controls to create a verifiable graph of their system’s intended structure.
In a live demonstration, Mark shows how an agent’s proposed code change that violates these predefined architectural rules is automatically detected and flagged as a violation before it can be merged.
This approach ensures that AI-generated code strictly adheres to the team’s established architecture, requiring human intervention only when a deliberate architectural change is proposed, thereby providing deterministic governance rather than probabilistic oversight.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , Mark, presents a solution for governing Model Context Protocol (MCP) at scale, focusing on preventing code drift from code generation to merge.  |
|   2 | , agents extending code boundaries without approval, and unnoticed architectural deviations.                                                       |
|   3 | , Slack, or Markdown files, leading to inconsistencies where different engineers describe the architecture differently.                            |
|   4 | , creating a machine-readable source of truth.                                                                                                     |
|   5 | , Calm, allows users to define nodes (actors, databases, folders) and relationships (connections, interactions) within the architecture.           |
|   6 | , patterns, and flows that enable deterministic enforcement of code changes during generation, ensuring agents adhere to the defined architecture. |
|   7 | , allowing for certainty that code changes align with the intended architecture.                                                                   |
|   8 | : at code generation time (via MCP) and at merge time (via backend checks).                                                                        |
|   9 | , bypassing the checkout service.                                                                                                                  |
|  10 | , which then proposed a code change reflecting the new direct connection.                                                                          |
|  11 | ; if not, it declares a violation.                                                                                                                 |
|  12 | , a human must intervene to decide whether to keep the change, update the architecture, or reject the code.                                        |
|  13 | , removing the AI’s ability to unilaterally decide on architectural deviations.                                                                    |
|  14 | , governing the artifact rather than the model’s reasoning.                                                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/POAbGlwrS5M/hqdefault.jpg)](https://www.youtube.com/watch?v=POAbGlwrS5M)

[Watch on YouTube](https://www.youtube.com/watch?v=POAbGlwrS5M)
