---
layout: default
title: "[Session] Asynchronous Tool Calling with Nick Aldridge - Amazon Web Services"
nav_order: 5
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  The speaker discusses challenges with the current synchronous tool-calling
  paradigm in MCP, likening it to micromanagement and highlighting its limitations
  for long-running workflows, such as molecular analysis, code migration, and enterpri...
resource: https://www.youtube.com/watch?v=2Q6o1B-lCew
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses challenges with the current synchronous tool-calling paradigm in MCP, likening it to micromanagement and highlighting its limitations for long-running workflows, such as molecular analysis, code migration, and enterprise automation.
Various companies have implemented ad hoc asynchronous workarounds, but these introduce issues like high latency, reliability problems, scalability constraints, and operational complexity.
To address this, Amazon and the MCP community are developing SEP 1391, which proposes native asynchronous tool-calling semantics, allowing tools to be declared as async and providing task tokens for status and result retrieval via new RPC methods.
This approach aims to standardize async workflows, reduce implementation overhead, and improve reliability and scalability, while remaining compatible with existing monitoring and state management systems.
The speaker invites feedback on SEP 1391 and notes ongoing work to resolve nuances around elicitations, progress notifications, and streaming in asynchronous contexts.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MCP is at a pivotal moment, making it a good time for discussion.                                                                                                   |
|   2 | Current tool calling in MCP is compared to micromanagement, which limits scalability.                                                                               |
|   3 | The synchronous tool call paradigm causes issues, especially for long-running tasks.                                                                                |
|   4 | Companies, including large healthcare organizations, struggle with fitting long molecular analyses into synchronous tool calls.                                     |
|   5 | Enterprise automation and code migration teams face similar challenges with long-running workflows.                                                                 |
|   6 | Workarounds involve creating multiple tools for starting jobs, polling status, and fetching results, leading to orchestration complexity.                           |
|   7 | Problems with current workarounds include high latency, cost, model hallucination, reliability, scalability, and operational complexity.                            |
|   8 | Keeping connections open for long-running tasks leads to failures and scalability issues.                                                                           |
|   9 | SEP 1391 is being developed to introduce asynchronous tool calling semantics in MCP.                                                                                |
|  10 | SEP 1391 will allow tools to be declared as async, returning a task token for asynchronous workflows.                                                               |
|  11 | New RPC methods will be provided to fetch task status and results.                                                                                                  |
|  12 | The schema will include a new invocation mode field and a keep alive time parameter.                                                                                |
|  13 | Async workflows will return a token representing the task.                                                                                                          |
|  14 | Client-side logic can handle async workflows without additional agent orchestration.                                                                                |
|  15 | Benefits include leveraging existing state management systems, preserving monitoring, reducing implementation overhead, and addressing reliability and scalability. |
|  16 | Client polling is preferred over webhooks for simplicity and compatibility.                                                                                         |
|  17 | Open questions remain around elicitations, progress notifications, and streaming in async workflows.                                                                |
|  18 | Task-based semantics are a desired feature extension, with representation in MCP still under consideration.                                                         |
|  19 | Community feedback on SEP 1391 is encouraged, with a sample implementation to be released for testing.                                                              |
|  20 | Links to SEP 1391, Discord, and Amazon's agent core are provided for further engagement.                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2Q6o1B-lCew)
