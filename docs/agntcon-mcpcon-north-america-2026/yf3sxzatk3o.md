---
layout: default
title: "What Your MCP Server Does When Nobody's Looking - Austin Parker, honeycomb.io"
nav_order: 62
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Austin Parker, a co-founder of OpenTelemetry and former Director of AI Strategy at Honeycomb, shares key lessons on building observability for their MCP server, noting that over 60% of weekly activ..."
resource: "https://www.youtube.com/watch?v=YF3SxZAtK3o"
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

Austin Parker, a co-founder of OpenTelemetry and former Director of AI Strategy at Honeycomb, shares key lessons on building observability for their MCP server, noting that over 60% of weekly active users are now AI agents.
He highlights the challenge of interpreting JSON-RPC errors, which often return HTTP 200 status codes, necessitating robust internal tracing to distinguish between successful and failed operations.
By analyzing local agent transcripts and production traces, the team discovered that consolidating multi-step API workflows into single tools significantly improved agent comprehension, while also identifying that agents frequently struggle with Honeycomb’s custom query syntax and context window limitations.
To address these issues, they implemented OpenTelemetry tracing to capture detailed tool call attributes and built an automated feedback loop where agents analyze traces to identify errors, such as hallucinated column names, and propose fixes.
Parker emphasizes that optimizing response formats—such as using ASCII art charts instead of raw JSON—reduced token usage by 90% while maintaining accuracy, and he advises developers to use OpenTelemetry, identify "desire paths" in agent behavior, and prioritize slim, context-efficient responses to enhance MCP server performance.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , making it difficult to identify failures in standard logs.                                                                                                                             |
|   2 | % of Honeycomb’s weekly active users are now agents, highlighting the critical need for MCP observability.                                                                               |
|   3 | , making traditional UI-based observability tools ineffective for tracking agent behavior.                                                                                               |
|   4 | , as they cannot see the prompts or internal reasoning of third-party agents.                                                                                                            |
|   5 | (e.g., "run query") significantly improves agent comprehension and success rates.                                                                                                        |
|   6 | (70k–80k tokens) consume excessive context window space, causing issues for agents with limited context.                                                                                 |
|   7 | ; overly verbose instructions can improve performance for some models while degrading it for others.                                                                                     |
|   8 | (e.g., derived columns) without explicit UI-like affordances or clear definitions provided in the tool schema.                                                                           |
|   9 | , allowing teams to identify specific failure points and latency bottlenecks.                                                                                                            |
|  10 | , dispatching coding agents to fix issues.                                                                                                                                               |
|  11 | "Desire paths" in agent behavior, such as hallucinating column names, were identified through trace analysis and addressed by returning likely candidates to reduce errors.              |
|  12 | , which served as a heuristic to distinguish between interactive agent sessions and deterministic scripted API usage.                                                                    |
|  13 | , harnesses, and prompting styles, requiring continuous testing against production data.                                                                                                 |
|  14 | "Shape beats precision" is a key takeaway; providing high-level visual summaries allows agents to identify outliers effectively, with raw data available via URLs for detailed analysis. |
|  15 | , analyzing agent "desire paths" to improve tools, and keeping responses slim to conserve context windows.                                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YF3SxZAtK3o/hqdefault.jpg)](https://www.youtube.com/watch?v=YF3SxZAtK3o)

[Watch on YouTube](https://www.youtube.com/watch?v=YF3SxZAtK3o)
