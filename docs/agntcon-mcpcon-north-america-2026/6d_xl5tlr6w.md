---
layout: default
title: "Harness Engineering: From MAST's Failure Taxonomy to MCP-Native... - Jay Mehta, Cygnet Infotech LLC"
nav_order: 65
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Jay Mehta, a Principal Solutions Architect, presents a session on harness engineering and the application of the MAST-F framework to improve multi-agent system reliability."
resource: "https://www.youtube.com/watch?v=6D_xl5Tlr6w"
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

Jay Mehta, a Principal Solutions Architect, presents a session on harness engineering and the application of the MAST-F framework to improve multi-agent system reliability.
He explains that while 86.7% of multi-agent systems fail, these issues often stem from system design flaws rather than model limitations, as identified by UC Berkeley’s MAST-F taxonomy which categorizes failures into system design, inter-agent alignment, and task verification.
Mehta illustrates this through two production cases: a support agent where unvalidated tool calls corrupted hundreds of tickets, and a pre-sales assistant where an unending loop between a drafter and reviewer agents consumed excessive resources.
To address these, he advocates for a "harness" approach using components like Pydantic for structure, MCP for safe tool calls, LangGraph for state management, verification gates, and observability tools like Opic.
The recommended adoption process involves capturing traces, applying deterministic code-based checks over prompt-driven logic, using LLMs as judges for annotation, and measuring performance improvements before and after implementing these structural safeguards.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : A multi-agent system failure taxonomy developed by UC Berkeley, analyzing 1,642 execution traces across seven frameworks to identify 14 distinct failure modes.                                                                                                                                                                 |
|   2 | : 86.7% of multi-agent system failures are attributed to system design rather than model capabilities, categorized into system design (44%), inter-agent alignment (32%), and task verification (23%).                                                                                                                            |
|   3 | : Defined as the structural components surrounding the model (the "engine"), including tool calls, execution limits, decision-making points, and verification gates, rather than the model itself.                                                                                                                                |
|   4 | :                                                                                                                                                                                                                                                                                                                                 |
|   5 | : Clear roles, handoffs, and contracts defined using Pydantic for type structure.                                                                                                                                                                                                                                                 |
|   6 | : Safe tool calls utilizing MCP (Model Context Protocol) or enterprise-specific tools with defined boundaries.                                                                                                                                                                                                                    |
|   7 | : Agentic frameworks like LangGraph that maintain state and manage the agentic loop.                                                                                                                                                                                                                                              |
|   8 | : Deterministic checks to validate task completion, limits, and permissions.                                                                                                                                                                                                                                                      |
|   9 | : Observability tools (e.g., Opic) for tracing spans, nodes, and flags.                                                                                                                                                                                                                                                           |
|  10 | (Support Agent)**: A bad tool call sent null status and non-numeric priority to Zendesk, corrupting over 100 tickets. Resolved by implementing "Anchor" harnesses with MCP tool boundaries and schema validation to prevent invalid inputs.                                                                                       |
|  11 | (Pre-Sales Assistant)**: An unending loop between a Drafter and Reviewer agent occurred over 800 times, causing high compute costs and requiring manual termination. Resolved by implementing "Belay Device" and "Verify Gate" harnesses with max iteration limits, repeated state signature detection, and time/token budgeting. |
|  12 | : A six-step process starting with trace logging, applying cheap deterministic checks, using LLM-as-a-Judge for automated labeling, conducting human review (targeting Kappa score >0.85), prioritizing code over prompts for determinism, and establishing CI/CD gates to measure improvement.                                   |
|  13 | : Issues included valid tool calls with wrong intent, guards misfiring on legitimate drafts, and increased costs from additional verification checks. Mitigations involved re-annotating traces with ground truth data and adjusting guard limits to allow necessary agent exploration.                                           |
|  14 | : Structure is more critical than model intelligence. Organizations should start by securing traces, defining their own failure labels, mapping specific harness components to identified failures, and rigorously measuring performance before and after harness implementation to ensure ROI.                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6D_xl5Tlr6w/hqdefault.jpg)](https://www.youtube.com/watch?v=6D_xl5Tlr6w)

[Watch on YouTube](https://www.youtube.com/watch?v=6D_xl5Tlr6w)
