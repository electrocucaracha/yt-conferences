---
layout: default
title:
  "[Session] Beyond API Wrappers: Workflow-Based MCP Servers with Elicitation
  and Sampling"
nav_order: 20
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  In this talk, Tom McLolin from Tomorrow AI discusses moving beyond the
  traditional approach of treating MCP servers as simple API wrappers, advocating
  instead for building workflow-oriented servers that focus on specific user outcomes.
  He e...
resource: https://www.youtube.com/watch?v=JuPoDQwmYMU
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

In this talk, Tom McLolin from Tomorrow AI discusses moving beyond the traditional approach of treating MCP servers as simple API wrappers, advocating instead for building workflow-oriented servers that focus on specific user outcomes.
He explains that the API wrapper model leads to tool redundancy, context confusion for LLMs, and difficulty for end users in selecting the right tools, as complexity is frontloaded into the LLM context.
By contrast, workflow servers are designed around actual user tasks, selecting only the necessary tools and leveraging advanced MCP features like elicitation and sampling to enable progressive disclosure and human-in-the-loop decision-making.
Tom demonstrates this approach with a workflow that transforms a hand-drawn sketch into a game-ready, rigged 3D asset, illustrating how complexity is shifted into the server runtime and how elicitation and sampling can streamline user interactions.
He concludes by emphasizing that effective workflows are discovered through close collaboration with domain experts and that this method better mirrors real-world processes, ultimately making MCP servers more useful and intuitive for end users.

# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on moving beyond viewing MCP servers as simple API wrappers.                                                |
|   2 | Advanced MCP spec features can improve server functionality.                                                                 |
|   3 | The "API wrapper problem" includes:                                                                                          |
|   4 | Hitting tool limits due to tool proliferation per server.                                                                    |
|   5 | Context confusion for LLMs when many similar tools are loaded.                                                               |
|   6 | Difficulty for end users to identify which tools to use for specific tasks.                                                  |
|   7 | Abstraction mismatch occurs when generic tools are bundled in servers, leading to redundancy and unused tools.               |
|   8 | Proposed solution: focus on user outcomes and workflows rather than tools or endpoints.                                      |
|   9 | Build opinionated, specific MCP servers with only necessary tools and resources for targeted workflows.                      |
|  10 | Workflow: a sequence from input to desired outcome, not just a set of tools.                                                 |
|  11 | Example workflow: transforming a hand-drawn sketch into a game-ready character asset.                                        |
|  12 | Shifting complexity from LLM context (API wrapper approach) to server runtime (workflow approach) is beneficial.             |
|  13 | Workflow servers reduce LLM context complexity by exposing only relevant tools and resources.                                |
|  14 | Workflows are discovered by observing domain experts and understanding their processes.                                      |
|  15 | Elicitation (from the MCP spec) enables progressive disclosure of information and keeps humans in the loop.                  |
|  16 | Elicitation allows servers to request context at the right time, not all upfront.                                            |
|  17 | Sampling lets servers use LLM inference for tasks like unstructured-to-structured data, summarization, and branch selection. |
|  18 | Demo: MCP server in Cursor client converts a dragon sketch into a colored image, then a 3D model, and finally a rigged mesh. |
|  19 | Elicitation used for user choices (e.g., color selection, previewing steps).                                                 |
|  20 | Sampling could be used for interpreting sketches and guiding coloring.                                                       |
|  21 | Final output is a fully rigged 3D asset, ready for further animation and integration into a game environment.                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JuPoDQwmYMU)
