---
layout: default
title: "[Session] Improving Agentic Search with MCP Sessions with Matt Dailey - Ref"
nav_order: 8
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Matt from Ref introduces Ref, a startup offering an MTP server designed
  as a documentation search tool for coding agents, which indexes both public and
  private docs to provide agents with only the relevant snippets needed, optimizing
  token...
resource: https://www.youtube.com/watch?v=cGki4V11sPs
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

Matt from Ref introduces Ref, a startup offering an MTP server designed as a documentation search tool for coding agents, which indexes both public and private docs to provide agents with only the relevant snippets needed, optimizing token usage and minimizing context window bloat.
He explains that, unlike traditional search systems evaluated by precision and recall, Ref focuses on recall and token usage to better suit the iterative search behavior of agents, who accumulate context over multiple searches.
Matt describes how Ref leverages MCP sessions to maintain state across searches, enabling features like prefetching, avoiding duplicate links, and chunking large documents to prevent context overload.
He shares that these improvements result in significant token savings—up to 95% compared to other servers—while also discussing challenges with client fragmentation and session management due to differences in how clients handle session IDs.
Matt concludes by encouraging attendees to connect with him, help promote Ref on developer tool pages, and engage in conversation, emphasizing the importance of understanding agent behavior to build effective MCP servers.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ref is a startup offering an MCP server for documentation search, targeting coding agents.                                                                       |
|   2 | Ref indexes both public and private documentation, enabling agents to access relevant snippets without overloading the context window.                           |
|   3 | The talk aims to explain how Ref achieves precise, token-efficient documentation search using MCP sessions.                                                      |
|   4 | Search evaluation at Ref uses recall and token usage as primary metrics, rather than just precision and recall.                                                  |
|   5 | Human and agent search behaviors are similar in their iterative approach but differ in context management: humans use visual fields, agents use context windows. |
|   6 | Token efficiency is crucial due to inference costs and context rot, where large context windows degrade generation quality.                                      |
|   7 | Basic search APIs typically return a fixed number of documents or tokens, often leading to inefficient context usage.                                            |
|   8 | Agents search iteratively, and each iteration with basic APIs adds more data to the context window, increasing costs.                                            |
|   9 | Ref and similar servers use a two-tool approach: a search tool (returns URLs and descriptions) and a read tool (fetches specific documentation chunks).          |
|  10 | MCP sessions enable stateful servers by associating client requests with a session ID, allowing servers to store and utilize state across requests.              |
|  11 | Ref leverages session state to implement three main improvements:                                                                                                |
|  12 | Prefetching likely-to-be-read URLs for faster response (does not impact recall/token usage).                                                                     |
|  13 | Avoiding returning the same link twice, reducing repeated context and speeding up result paging.                                                                 |
|  14 | Extracting only relevant chunks from large documents to prevent context window overload.                                                                         |
|  15 | Ref’s approach saves 50–70% tokens on average (up to 95% in best cases) compared to popular alternatives, resulting in significant cost and efficiency gains.    |
|  16 | Challenges include client fragmentation and session ID management at the transport layer, requiring defensive programming for different client behaviors.        |
|  17 | Action items: connect with Matt on s                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cGki4V11sPs)
