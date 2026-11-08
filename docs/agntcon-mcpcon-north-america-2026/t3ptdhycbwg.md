---
layout: default
title: "Between Intent and Execution - Hemanth hm, PayPal"
nav_order: 92
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Hemanth Acham, a Google Developer Expert at PayPal AI Labs, presents Agentoo, a lightweight agent harness designed to address the complexity and context bloat inherent in building scalable AI agents."
resource: "https://www.youtube.com/watch?v=t3ptdhYCbWg"
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

Hemanth Acham, a Google Developer Expert at PayPal AI Labs, presents Agentoo, a lightweight agent harness designed to address the complexity and context bloat inherent in building scalable AI agents.
He argues that traditional SDKs are often too heavy, proposing instead a descriptive, intuitive framework that allows agents to run directly in the browser without server dependencies.
A core principle of Agentoo is loading tools on demand rather than preloading all available tools into the context, which significantly reduces token usage and improves efficiency by selecting only the necessary tools for specific tasks.
The presentation outlines twelve key lessons for robust agent engineering, emphasizing the isolation of memory per session to prevent data leaks and the implementation of durable execution that allows agents to save state and resume from crashes.
Acham stresses the importance of enforcing permissions in code rather than relying on model decisions, ensuring that tool visibility does not equate to execution authority, and providing exact error messages to facilitate effective retries.
He also advocates for outcome-based testing over simple log verification, separating drafting and auditing roles to avoid self-grading, and using write-ahead logs with idempotency for safe recovery in distributed systems.
To support these practices, Agentoo offers features such as the "Ralph loop" for checklist-driven task completion, structured output generation, and integration with MCP servers.
The framework includes observability tools to track reasoning, costs, and performance, allowing developers to debug why an agent made specific decisions.
Acham demonstrates these capabilities through live browser-based code labs, showing how to build agents with tools, guardrails, and sub-agents, while also highlighting the importance of summarizing long conversations and caching results to optimize performance.
The session concludes with a live demonstration of an agent executing a financial transaction, illustrating the practical application of these agentic engineering principles in a real-world scenario.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , name, context, and tools, but complexity increases as tools scale to hundreds or thousands.                                                                                                                                                                           |
|   2 | (research, triage, draft, review) and must retain context, tool call counts, and failure points for recovery.                                                                                                                                                           |
|   3 | "Agentoo" harness is a lightweight, descriptive framework designed to address the heaviness of existing agent SDKs.                                                                                                                                                     |
|   4 | : Load tools on demand.** Instead of loading all tools into context (e.g., 12K characters), use lazy loading to search for specific tools only when needed, reducing context size significantly.                                                                        |
|   5 | : One agent per session.** Use isolated memory spaces for each agent session to prevent data leakage between agents and simplify context management and recovery.                                                                                                       |
|   6 | : Save each step and resume on crash.** Implement durable execution (e.g., using Redis) to log every step. This allows the agent to resume from the exact point of failure, acting as if it woke up from sleep.                                                         |
|   7 | : Enforce rules in code, not prompts.** Tool visibility in the prompt does not imply execution authority. Use code-level interceptors (e.g., `can_use_tool`) to authorize actions based on read/write permissions, preventing prompt injection and unauthorized access. |
|   8 | : Feed exact errors for retries.** Provide specific field-level error messages (e.g., "refund limit is $140") rather than generic exceptions. Set maximum correction limits to prevent infinite retry loops.                                                            |
|   9 | : Test outcomes, not just logs.** Use agent observers to evaluate whether the customer’s problem was actually solved, not just if the API returned a 200 status. This supports RLHF and debugging.                                                                      |
|  10 | : Block the "legal trifecta."** Prevent a single agent from combining read-private data, passing tickets, and external sending, as this combination poses significant security risks.                                                                                   |
|  11 | : Separate writers from reviewers.** Do not allow the same agent to draft and audit its own work. Use distinct entities for drafting and approval to ensure objective evaluation.                                                                                       |
|  12 | : Log before risky turns.** Create checkpoints before executing risky tool calls to enable branching and recovery. Use `agent.remember` to tag specific branches for context retention.                                                                                 |
|  13 | : Verify checklists (Ralph Loop).** Use a loop that iterates through a checklist of tasks until all items are marked complete, ensuring deterministic goal achievement within a sandboxed environment.                                                                  |
|  14 | : Summarize and consolidate memory.** Regularly consolidate long-running chat histories into facts and summaries. Use smart caching (e.g., BM25) to reduce API calls and improve response speed.                                                                        |
|  15 | : Log the "why" and cost.** Record the reasoning behind agent decisions and track costs per run. This data is crucial for debugging, cost optimization, and understanding agent behavior.                                                                               |
|  16 | , structured outputs, and sub-agent delegation.                                                                                                                                                                                                                         |
|  17 | , supporting top LLM providers and allowing custom persistence layers (e.g., SQL, Redis, OpenTelemetry).                                                                                                                                                                |
|  18 | , including live examples of agent execution and portfolio management.                                                                                                                                                                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/t3ptdhYCbWg/hqdefault.jpg)]("https://www.youtube.com/watch?v=t3ptdhYCbWg")

[Watch on YouTube](https://www.youtube.com/watch?v=t3ptdhYCbWg)
