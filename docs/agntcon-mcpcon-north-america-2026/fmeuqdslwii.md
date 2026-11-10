---
layout: default
title: "Rethinking CI/CD Release Gates for Agent-native Software - Prathmesh Patel, MCPJam"
nav_order: 72
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Roth Mash, CEO of MCP Jam, presents a framework for building, testing, and releasing agent-native software with confidence, arguing that as AI accelerates code generation, the cost of bad code incr..."
resource: "https://www.youtube.com/watch?v=FmeuQdSLWiI"
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

Roth Mash, CEO of MCP Jam, presents a framework for building, testing, and releasing agent-native software with confidence, arguing that as AI accelerates code generation, the cost of bad code increases due to the difficulty of testing and changing it.
He introduces the "User Value Chain," a six-stage model spanning connection, discovery, tool selection, tool call, tool response, and user value, emphasizing that significant failures often occur on the client-side within agentic applications like ChatGPT or Claude, where issues such as unselected tools or failed UI interactions do not appear in server logs.
To address these challenges, Mash advocates for "Evals" as the new product requirements documents, suggesting that developers must treat tool descriptions as critical source code and use differential testing to ensure changes do not regress existing user behaviors.
He recommends a "tracer bullet" approach, starting with a single user workflow to map out checks across the entire client-server interaction before integrating them into CI/CD pipelines.
Finally, he highlights MCP Jam as an open-source platform that uses agent personas to simulate user interactions across various clients, providing the necessary feedback loops and evidence for developers to maintain reliable, high-quality software in an agent-driven ecosystem.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , necessitating "agent-native" CI/CD practices to ensure reliable delivery.                                                                                 |
|   2 | ; software that is hard to test or change prevents teams from leveraging AI benefits.                                                                       |
|   3 | "software factory" concept involves handing off the development lifecycle to agents, but quality still depends on testing, monitoring, and rollout.         |
|   4 | ; bringing evidence closer to developers through short iteration loops is essential for confident releases.                                                 |
|   5 | "Evals" (evaluations) are the new PRDs, serving as contracts that define user interactions and expected software outcomes.                                  |
|   6 | , Claude, or Microsoft Copilot.                                                                                                                             |
|   7 | (e.g., UI rendering, state persistence, tool selection) and do not appear in server logs.                                                                   |
|   8 | "User Value Chain" framework breaks down the request flow into six stages: Connection, Discovery, Tool Selection, Tool Call, Tool Response, and User Value. |
|   9 | (protocol, OAuth) and semantic checks (behavioral evaluations) across these stages.                                                                         |
|  10 | ; they must be managed with the same rigor as source code.                                                                                                  |
|  11 | , clickable dev server or client environment to effectively verify their work.                                                                              |
|  12 | ,000 developers using it to test MCP servers, skills, and CLIs.                                                                                             |
|  13 | , find edge cases, and map results to the User Value Chain.                                                                                                 |
|  14 | , updated regularly to reflect changing user prompting patterns and client capabilities.                                                                    |
|  15 | (tracer bullet approach) to build end-to-end testing capabilities before scaling.                                                                           |
|  16 | /CD pipelines should include gates that verify software reliability across different client environments before deployment.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/FmeuQdSLWiI/hqdefault.jpg)](https://www.youtube.com/watch?v=FmeuQdSLWiI)

[Watch on YouTube](https://www.youtube.com/watch?v=FmeuQdSLWiI)
