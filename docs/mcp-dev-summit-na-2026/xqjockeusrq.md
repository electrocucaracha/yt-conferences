---
type: Video Note
title: "Evaluate What You Can't See: Measure the Probabilistic Nature of MCP - P. Patel & M.J. Rocabado"
description: 'Bromesh, CEO of MCP Jam, introduces a talk focused on the challenges of evaluating and improving user value in MCP server development, emphasizing the importance of understanding the "XY problem," where developers often address assumed solu...'
resource: https://www.youtube.com/watch?v=XqjOcKEUSRQ
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Bromesh, CEO of MCP Jam, introduces a talk focused on the challenges of evaluating and improving user value in MCP server development, emphasizing the importance of understanding the "XY problem," where developers often address assumed solutions rather than underlying issues.
He illustrates how server logs can appear identical despite vastly different user experiences, highlighting the lack of visibility into user intent and agent reasoning due to system boundaries in MCP architecture.
Bromesh outlines a user value chain with multiple steps where value can be lost, noting that developers typically only have observability over tool calls, not the full user journey.
He discusses strategies for obtaining real user data—such as adding parameters for user intent, leveraging existing chatbot data, using test environments, and instrumenting MCP apps—to inform eval testing and improve workflows.
The talk concludes by introducing MCP Jam’s new sandbox environments, which allow for secure, instrumented testing and user feedback, aiming to operationalize a flywheel of continuous improvement based on real user insights.
# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Bromesh (CEO of MCP Jam) and Marcelo (CTO) presented on evaluating what you can't see in MCP server development.                                                           |
|   2 | Audience roles polled: MP server developers, MP host app developers, managers, tech leads, AI strategy leads.                                                              |
|   3 | Introduced the XY problem: people ask about their assumed solution (Y) instead of their actual problem (X), which narrows solution space and wastes time.                  |
|   4 | Example: "How do I breed a faster horse?" Actual problem is "How do I get my kids from A to B faster?"—solution space broadens when focusing on X.                         |
|   5 | MCP example: Complaints about MCB context window and CLI debates often mask the real problem—inefficient agent workflows and ballooning costs.                             |
|   6 | Solution: Focus on root problems to expand solution options, e.g., progressive disclosure for tools, caching common tools, semantic search.                                |
|   7 | MCP ecosystem is fast-moving; first-mover advantage is important.                                                                                                          |
|   8 | MCP systems are hard to observe; developers only see what hits their server, not user intent or agent reasoning.                                                           |
|   9 | User and agent live inside host applications; server is outside and lacks visibility into user prompts, agent decisions, and selection.                                    |
|  10 | User value chain: connection, discovery, tool selection, correct arguments, tool response, agent reasoning, user value.                                                    |
|  11 | Developers typically only instrument the tool call step, missing much of the value chain.                                                                                  |
|  12 | REST API design targets human developers; MCP targets agents, requiring different design considerations.                                                                   |
|  13 | Evals (nondeterministic tests) help measure if servers deliver value for real user prompts, but most teams aren't instrumenting with evals.                                |
|  14 | Ways to get user data: add parameters for user intent, use existing chatbot data, create test environments/sandboxes, dogfood internally, use MC apps for instrumentation. |
|  15 | Sampling is rarely supported by host apps due to data privacy/monetization concerns.                                                                                       |
|  16 | MC apps and sandboxes allow for better instrumentation and user feedback.                                                                                                  |
|  17 | Flywheel: collect real user data, cluster insights, build e                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XqjOcKEUSRQ)