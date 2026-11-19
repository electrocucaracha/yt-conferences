---
layout: default
title: "Why the Heck Aren't Any Agents Supporting MCP Tasks? - Cornelia Davis, Temporal"
nav_order: 125
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Cornelia Davis presents a technical overview of MCP tasks, highlighting the recent adoption of this protocol by major agents like Claude Code to address long-standing gaps in asynchronous support."
resource: "https://www.youtube.com/watch?v=4v-tltNKHPA"
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

Cornelia Davis presents a technical overview of MCP tasks, highlighting the recent adoption of this protocol by major agents like Claude Code to address long-standing gaps in asynchronous support.
The talk emphasizes the critical durability requirements mandated by the MCP specification, demonstrating through live demos how both clients and servers must persist state to handle network failures, server crashes, and human approval delays without losing progress.
Davis explains the evolution from MCP Tasks V1 to V2, noting that the shift to a stateless protocol removed the server-side task list, thereby shifting the responsibility for persisting task handles and managing elicitation inputs to the client-side.
Using a purchase order and invoice payment use case, she illustrates how internal domain states must be mapped to the protocol’s state machine and how durable storage ensures that processes resume exactly where they left off after interruptions.
Finally, she addresses scalability challenges associated with client-side polling by introducing the new server-to-client notification mechanism in MCP V2, which acts as a webhook to reduce load, and provides a GitHub repository for attendees to explore the implementation details.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , but major agent support was lacking until Claude Code recently announced support for tasks and elicitations.                                                              |
|   2 | , requiring developers to manually handle patterns like progress reporting and polling.                                                                                     |
|   3 | , Cornelia Davis, a technologist at Temporal, presented a use case involving purchase orders where invoice payment is implemented as a long-running, asynchronous MCP task. |
|   4 | , allowing for negotiation between client and server regarding synchronous or asynchronous execution.                                                                       |
|   5 | , ensuring tasks persist and resume correctly despite network failures, server crashes, or client disconnections.                                                           |
|   6 | ’s defined state machine, which includes stages such as pending validation and waiting for approval.                                                                        |
|   7 | , it resumes exactly where it left off upon restart, rather than restarting the process.                                                                                    |
|   8 | , released alongside the stateless MCP V2 protocol, removed the "task list" feature, shifting the durability requirement for maintaining task handles to the client-side.   |
|   9 | , as the protocol no longer provides a mechanism to retrieve in-flight tasks from the server if the connection is lost.                                                     |
|  10 | , allowing clients to request and provide necessary input (such as approvals) more efficiently during polling.                                                              |
|  11 | ; user inputs like approvals must be stored persistently so they can be transmitted to the server once it is back online.                                                   |
|  12 | (e.g., millions of tasks) are being addressed by a new notification mechanism in MCP V2, similar to webhooks, which allows servers to push updates to clients.              |
|  13 | , emphasizing that while the protocol is sound, implementing the necessary state management and persistence remains complex.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/4v-tltNKHPA/hqdefault.jpg)](https://www.youtube.com/watch?v=4v-tltNKHPA)

[Watch on YouTube](https://www.youtube.com/watch?v=4v-tltNKHPA)
