---
layout: default
title: "Agentic Messaging Primitives in MCP - Caitie McCaffrey, Microsoft"
nav_order: 60
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Katie McCaffrey, a core maintainer of the Model Context Protocol (MCP), outlines the protocol’s evolution from a synchronous request-response system to one supporting complex agentic messaging patt..."
resource: "https://www.youtube.com/watch?v=h4ZvZpkdslc"
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

Katie McCaffrey, a core maintainer of the Model Context Protocol (MCP), outlines the protocol’s evolution from a synchronous request-response system to one supporting complex agentic messaging patterns.
She defines key concepts such as synchronous request-response, multi-round trip interactions, and asynchronous mechanisms like subscribe-notify, tasks, and events, emphasizing that these patterns are independent of transport and data.
The presentation highlights the introduction of the "events" extension, which enables true asynchronous messaging with durable subscriptions and flexible delivery methods including polling, streaming, and webhooks to optimize for serverless environments and sporadic updates.
McCaffrey identifies three critical areas for future development to support autonomous agents: managing long-running task lifecycles, establishing a canonical method for reporting progress and intermediate results, and enabling fine-grained steering of agents during execution.
She concludes by inviting the community to participate in the tasks and events working group to help rationalize these primitives, ensuring they are composable and interoperable rather than creating a single rigid pattern for all agent types.

# Main Points

|   # | Main point                                                                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | & Context**: Katie McCaffrey, core MCP maintainer and Microsoft technical staff, discusses MCP messaging patterns and the roadmap for agentic messaging primitives.                                              |
|   2 | : Defines the shape and direction of communication (e.g., client-to-server order), independent of transport or data content.                                                                                     |
|   3 | :                                                                                                                                                                                                                |
|   4 | : Causal link where the initiator waits for a response (request-response); ensures consistency but can block.                                                                                                    |
|   5 | : Fire-and-forget events; producer and consumer lifecycles are decoupled; no strict time binding or causal link.                                                                                                 |
|   6 | :                                                                                                                                                                                                                |
|   7 | : Basic synchronous pattern (e.g., `get_tools`, `call_tool`).                                                                                                                                                    |
|   8 | : New in 726 release; synchronous with strict order for elicitation (server requests more data from client).                                                                                                     |
|   9 | : Async events (e.g., tool list changes); requires persistent connection; no guarantee on timing.                                                                                                                |
|  10 | : Official extension for long-running operations; async lifecycle management akin to promises; allows status polling without holding open connections.                                                           |
|  11 | : Experimental (soon official); true async messaging with durable subscriptions; supports multiple delivery methods.                                                                                             |
|  12 | :                                                                                                                                                                                                                |
|  13 | : Traditional JSON-RPC return.                                                                                                                                                                                   |
|  14 | : Client pulls status (used in Tasks); can be costly in serverless environments.                                                                                                                                 |
|  15 | : Persistent channel for high-frequency events (e.g., notifications, video).                                                                                                                                     |
|  16 | : Server-sent push events; ideal for sporadic events and serverless cost savings.                                                                                                                                |
|  17 | : MCP aims to standardize these patterns to replace bespoke integration code, ensuring consistent interop across agents and applications.                                                                        |
|  18 | : Current implementations have gaps (e.g., Tasks lack webhook/streaming delivery; Subscriptions only support persistent connections). Work is ongoing to rationalize these patterns.                             |
|  19 | :                                                                                                                                                                                                                |
|  20 | : Managed via Tasks extension for lifecycle and status without open connections.                                                                                                                                 |
|  21 | & Intermediary Results**: Currently lacks a canonical method; multiple inconsistent approaches exist (notifications, events, resources). Goal is to define a concrete pattern for consistent progress reporting. |
|  22 | & Adjustment**: Ability to modify agent behavior mid-task (beyond simple cancellation). Requires extending Tasks and integrating Events for fine-grained control.                                                |
|  23 | : MCP will not add a specific "agent" row to the protocol table. Instead, it provides composable primitives (sync/async, delivery types) that developers combine to build diverse agent types.                   |
|  24 | : Work is happening in the Tasks and Events working group. Developers are encouraged to join Discord, share feedback, and contribute scenarios to refine these patterns.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/h4ZvZpkdslc/hqdefault.jpg)]("https://www.youtube.com/watch?v=h4ZvZpkdslc")

[Watch on YouTube](https://www.youtube.com/watch?v=h4ZvZpkdslc)
