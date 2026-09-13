---
type: Video Note
title: "Durable, Asynchronous, and Tricky: Implementing MCP Tasks in Practice - Cornelia Davis, Temporal"
description: "The speaker introduces MCP tasks and the new asynchronous protocol, noting that few in the audience have implemented them. Drawing on extensive experience in developer platforms and workflow systems, the speaker uses a concrete invoice proc..."
resource: https://www.youtube.com/watch?v=CD0DlPaVdN8
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces MCP tasks and the new asynchronous protocol, noting that few in the audience have implemented them.
Drawing on extensive experience in developer platforms and workflow systems, the speaker uses a concrete invoice processing example to illustrate both pre- and post-November 2025 approaches to MCP.
Initially, the workflow was made durable using existing tools, but the process was awkward due to the lack of native async support, requiring workarounds for long-running operations.
With the introduction of the MCP task protocol, tools can now be invoked asynchronously, returning a handle for status polling, result retrieval, or cancellation, and—crucially—tasks must be durable, surviving client or server failures.
The speaker demonstrates this durability through live demos, showing how tasks persist and resume after interruptions, and explains the protocol’s architecture, message types, and state management.
The talk concludes with enthusiasm for the new async protocol, while acknowledging the complexity of implementing async over stateful transports and expressing hope for future stateless protocol developments.
# Main Points

|   # | Main point                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Few attendees have implemented MCP tasks or the new async protocol.                                                                                                                                      |
|   2 | Presenter has a background in computer science, development, operations, and cloud platforms.                                                                                                            |
|   3 | Agenda: concrete invoice processing use case, pre-Nov 2025 MCP approach, new tasks protocol, protocol overview, implementation demos, focus on durability.                                               |
|   4 | Invoice processing workflow: validate invoice against ERP, wait for human approval, pay line items.                                                                                                      |
|   5 | Initial demo: durable, long-running process using Temporal; workflow waits for human approval, then pays line items.                                                                                     |
|   6 | Pre-Nov 2025 MCP implementation: used fast MCP, created tools for submitting, approving/rejecting, and checking invoice status; tools were stateful but only supported request-response, not true async. |
|   7 | Limitation: tunneling async workflows over request-response tools; lack of protocol-level async task processing.                                                                                         |
|   8 | November 2025: MCP spec introduced tasks—tools can now be synchronous or asynchronous.                                                                                                                   |
|   9 | Tasks protocol: tools can be invoked asynchronously, returning a handle for polling status, results, cancellation, or listing tasks.                                                                     |
|  10 | Key feature: tasks are durable state machines; must survive client/server/network failures.                                                                                                              |
|  11 | Five task-related messages: tools/call (with async metadata), get, result, cancel, list.                                                                                                                 |
|  12 | Task semantics: task IDs set by client; tasks have states (working, waiting for input, finished); time-to-live can be set; input required handled via long-running connection and elicitation.           |
|  13 | Protocol mostly uses request-response; only task result uses long-running connection for input elicitation.                                                                                              |
|  14 | Implementation: single MCP tool (invoice processor), protocol handlers for get, result, cancel, list; mapping between task and workflow states.                                                          |
|  15 | No off-the-shelf agents support the task protocol yet; presenter built a custom client.                                                                                                                  |
|  16 | Final demo: demonstrated durability by killing/restarting client and server; tasks persisted and resumed as required by spec.                                                                            |
|  17 | Each line item payment is a child workflow for independent d                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CD0DlPaVdN8)