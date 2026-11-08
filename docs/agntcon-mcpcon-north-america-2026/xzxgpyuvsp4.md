---
layout: default
title: "Don't Share the Database: Interface Contracts Between Isolated... - Martin Bliss, At Your Company!"
nav_order: 69
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Martin Bliss argues that isolated AI agents should share structured contracts rather than raw context, drawing a direct parallel to the microservices principle of avoiding shared databases to preve..."
resource: "https://www.youtube.com/watch?v=xZXGPyUVSp4"
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

Martin Bliss argues that isolated AI agents should share structured contracts rather than raw context, drawing a direct parallel to the microservices principle of avoiding shared databases to prevent cascading failures.
He explains that when agents share verbose transcripts, they risk misinterpreting each other’s reasoning, leading to inconsistent states and wasted tokens; instead, agents should communicate via concise, standardized specifications—such as JSON or Markdown tables—that contain only the essential decision data without the underlying "noise" of the agent’s internal deliberation.
To manage this workflow, Bliss introduces the concept of a "foreman" agent, which oversees project progress, monitors context window pressure to prevent hallucinations, and enforces a decision-making protocol where agents are instructed to fail fast if they lack sufficient information rather than guessing.
This approach allows developers to scale parallel agent work without suffering from decision fatigue, as the foreman handles the orchestration and ensures that critical changes, such as data model updates, are explicitly signed off by the human developer.
Ultimately, the goal is to move away from micromanaging chat windows toward a system where agents operate autonomously within defined scopes, using project management tools and strict communication protocols to maintain clarity, reduce token costs, and ensure reliable, scalable software development.

# Main Points

|   # | Main point                                                                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , a software engineer with 25 years of experience, identifies "micromanaging" AI agents as a primary inefficiency, where developers must constantly monitor verbose transcripts and review outputs, preventing scalable parallel work. |
|   2 | : just as microservices should not share a database to avoid cascading failures, AI agents should not share raw context or transcripts to avoid confusion and token waste.                                                             |
|   3 | "context pollution," where agents misinterpret other agents' verbose reasoning, leading to inconsistent decisions, hallucinations, and the need for costly re-derivation of intent.                                                    |
|   4 | , short, and specific contracts (e.g., JSON or simple Markdown tables) that contain only the necessary decision data, such as field changes, scope, and versioning, excluding the reasoning process.                                   |
|   5 | , similar to how microservices maintain isolation by minimizing knowledge of other services' internal states.                                                                                                                          |
|   6 | ’s 1970s principle of information hiding, emphasizing that interfaces should hide implementation details to maintain system integrity.                                                                                                 |
|   7 | , ensuring that downstream agents receive only the essential, validated information without the "noise" of the original agent’s research or deliberation.                                                                              |
|   8 | , the speaker introduces the concept of a "Foreman" agent (named Heimdal), which oversees project progress, monitors context pressure, and directs new sessions when context windows become too full to prevent hallucinations.        |
|   9 | , planning next steps, and ensuring that critical decisions are made by the human developer rather than being buried in verbose AI outputs.                                                                                            |
|  10 | , DTOs, and API specs, while allowing agents to autonomously handle reversible, low-impact implementation details.                                                                                                                     |
|  11 | "fail fast" if they lack necessary information, preventing them from guessing or hallucinating solutions that could become entrenched in the codebase.                                                                                 |
|  12 | (e.g., Jira, GitHub), where agents work asynchronously and report via structured updates, reducing the need for constant human supervision.                                                                                            |
|  13 | , treating agents as isolated microservices, sampling agent outputs rather than reading every line, and treating silent failures or ambiguous defaults in MCP servers as bugs.                                                         |
|  14 | , which still require human intervention, and the challenge of fully trusting agents to deploy changes without oversight.                                                                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xZXGPyUVSp4/hqdefault.jpg)]("https://www.youtube.com/watch?v=xZXGPyUVSp4")

[Watch on YouTube](https://www.youtube.com/watch?v=xZXGPyUVSp4)
