---
layout: default
title: "[Session] From Embeddings to Edges: A Graph Based Approach to Tool Selection"
nav_order: 7
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  The speaker discusses challenges in tool call selection within MCP (Multi-Connector
  Platform) systems, emphasizing that current solutions often require users to explicitly
  specify tool names, which is impractical as the number of tools grow...
resource: https://www.youtube.com/watch?v=5nFOhwAwVGM
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

The speaker discusses challenges in tool call selection within MCP (Multi-Connector Platform) systems, emphasizing that current solutions often require users to explicitly specify tool names, which is impractical as the number of tools grows.
They highlight research showing that large tool sets significantly reduce selection accuracy and explain that issues stem from both the proliferation of low-quality MCP servers and limitations in context window size.
Existing approaches—such as tool sets, search-based methods, and agentic retrieval—have drawbacks like poor user experience, added latency, and increased costs.
To address these, the speaker proposes a graph-based approach, where tools and their relationships are represented as nodes and edges, allowing for more efficient selection strategies based on criteria like cost, speed, or centrality.
By bootstrapping a knowledge graph of tools using LLMs and leveraging algorithms to find optimal paths, this method improves tool call accuracy and user experience, as demonstrated with a ClickUp integration example, and opens up new possibilities for dynamic and scalable tool management.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter became interested in MCP for its automation and integration capabilities.                                            |
|   2 | Main issue identified: tool call selection is difficult and often inaccurate.                                                  |
|   3 | Current solutions require users to specify tool names explicitly, which is not user-friendly.                                  |
|   4 | Tool call selection accuracy drops as the number of tools increases (89% with <10 tools, 32% with 50+ tools).                  |
|   5 | OpenAI limits tool calls to 160 per request; fewer tools improve performance.                                                  |
|   6 | Challenges include poor quality of many MCP servers and limited context window size.                                           |
|   7 | Existing approaches to tool selection:                                                                                         |
|   8 | Tool sets: enabling/disabling tools via CLI flags (not ideal UX).                                                              |
|   9 | Search-based: searching available actions and executing based on results.                                                      |
|  10 | RAG/agentic: using vector DBs and embeddings, often requiring an agent to break down prompts, adding cost and latency.         |
|  11 | Server-side solutions attempt to compensate for client limitations.                                                            |
|  12 | Adding tools mid-function call loop leads to hallucinations and lower KV cache hit rates; tools should be loaded at the start. |
|  13 | Proposes a graph-based approach for tool call selection:                                                                       |
|  14 | Tools and their relationships are modeled as a directed acyclic graph (DAG).                                                   |
|  15 | Enables calculation of shortest, cheapest, or fastest paths to achieve a goal.                                                 |
|  16 | Allows dynamic reranking of tools based on past executions.                                                                    |
|  17 | Bootstrapping the graph involves using an LLM to define nodes and relationships from tool schemas.                             |
|  18 | Graph-based approach reduces per-request latency compared to agentic RAG.                                                      |
|  19 | Graph structure helps LLM select prerequisite tools in correct order, improving user experience.                               |
|  20 | Demonstrated with ClickUp MCP server: graph enables correct tool sequence, reducing user prompts.                              |
|  21 | Graph can be queried for best tool using various algorithms (cosine similarity, clustering).                                   |
|  22 | Code and demo available on GitHub (MC Lenhard/tool graph).                                                                     |
|  23 | Emphasizes the potential and flexibility of graph-based tool call selection.                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5nFOhwAwVGM)
