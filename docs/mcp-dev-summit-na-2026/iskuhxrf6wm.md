---
layout: default
title: "Call Now, Fetch Later: MCP Tasks and SEP-1686 - Adam Azzam, Prefect"
nav_order: 6
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Adam from Prefect discusses SEP 1686, which addresses task
  execution and orchestration in the MCP ecosystem. He explains the historical challenges
  of building resilient, reliable task orchestration, such as the risks of colloc...
resource: https://www.youtube.com/watch?v=isKuHXRf6wM
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

In this talk, Adam from Prefect discusses SEP 1686, which addresses task execution and orchestration in the MCP ecosystem.
He explains the historical challenges of building resilient, reliable task orchestration, such as the risks of collocating agents with risky tasks and the lack of standardized client support for background tasks.
SEP 1686 proposes a protocol for assigning task IDs, managing state machines, and retrieving results, but widespread adoption has been hindered by limited client implementation, creating a chicken-and-egg problem between clients and servers.
To work around this, Adam demonstrates using MCP apps and iframes to enable background task execution and polling for results, even with "bad" clients that lack native support.
While this approach is a workaround rather than an ideal solution, it allows for resilient, non-blocking applications and highlights the need for better client support to fully realize the benefits of task orchestration in MCP.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | SEP 1686 focuses on task execution and orchestration in MCP.                                                                                                 |
|   2 | Adam from Prefect presented; Prefect builds durable execution workflow orchestration and fast MCP in Python.                                                 |
|   3 | Orchestration principle: the control plane (state holder) should be isolated from risky, failure-prone tasks.                                                |
|   4 | Early agent designs were brittle, often failing due to resource exhaustion when risky tasks were colocated with agents.                                      |
|   5 | MCP’s appeal: identity-aware, portable protocol for remote tool execution, enabling orchestration patterns.                                                  |
|   6 | Shifting risk from colocated agents to network connections introduced new failure modes (e.g., timeouts, network blips).                                     |
|   7 | Workarounds included keeping long-running tasks client-side or inventing custom orchestrators, leading to fragmentation.                                     |
|   8 | Lack of standardization resulted in inconsistent state machines and tool ontologies across servers.                                                          |
|   9 | Effective task orchestration requires client-side primitives for polling and state/result retrieval.                                                         |
|  10 | SEP 1686 proposes a standard: assign work an ID, manage state via a state machine, provide methods for updates and result retrieval.                         |
|  11 | FastMCP 3.x and Docket (Pythonic task orchestrator) implement SEP 1686 on the server side.                                                                   |
|  12 | Major issue: few clients support SEP 1686, creating a chicken-and-egg problem for adoption.                                                                  |
|  13 | MCP is viewed as a marketplace between client and server capabilities; both must demand features for adoption.                                               |
|  14 | Marketplaces can be bootstrapped by leveraging existing ones, making features valuable in single-player mode, or owning both client and server.              |
|  15 | Tools and MCP apps are the two thriving MCP marketplaces; apps allow embedding iframes with custom runtimes.                                                 |
|  16 | Durable apps (via MCP apps) can background tasks, return control to users, and poll for results in the iframe, enabling resilient, non-blocking experiences. |
|  17 | Demo showed backgrounded long-running queries with persistent, resumable progress in the client via iframes.                                                 |
|  18 | This approach is a workaround for lack of native client support for                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=isKuHXRf6wM)
