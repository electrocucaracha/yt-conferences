---
layout: default
title: "One Server, Many Apps: A Composable MCP Architecture... - Shenoy Pratik Gurudatt, AWS OpenSearch"
nav_order: 126
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Kyle Heinslo and Chinmay Prateek from AWS explore the evolving role of dashboards in the agentic era, arguing that while AI agents can investigate issues, human engineers still require visual verif..."
resource: "https://www.youtube.com/watch?v=3TzG9NYlpwo"
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

Kyle Heinslo and Chinmay Prateek from AWS explore the evolving role of dashboards in the agentic era, arguing that while AI agents can investigate issues, human engineers still require visual verification to trust the results.
They introduce MCP apps as a solution that bridges this gap by rendering tool outputs as interactive, server-side visualizations directly within agent clients like Goose or Cloud Desktop, eliminating the context loss associated with switching between chat interfaces and static browser tabs.
The presentation details how they integrated these apps with the OpenSearch observability stack, leveraging existing dashboard APIs to create a composable architecture that shares authentication, context, and telemetry across different investigation tools such as alerts, traces, and metrics.
Through a live demo, they demonstrated how this approach allows SREs to verify root cause analyses by viewing raw data, source queries, and AI interpretations in a unified interface, thereby reducing hallucination risks and improving mean time to resolution.
The speakers conclude that dashboards are not dead but have evolved into an agentic format where MCP apps provide the necessary evidence for human verification, and they encourage the community to adopt these patterns for building more reliable and traceable observability workflows.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , using dashboards primarily to verify agent-proposed Root Cause Analyses (RCAs).                                                                                                     |
|   2 | "3:00 a.m. problem" involves context loss when switching between multiple browser tabs, tickets, and LLM chat sessions, leading to interrupted reasoning and verification challenges. |
|   3 | , discrepancies can arise between agent summaries and static dashboards (e.g., differing downtime durations), creating uncertainty about which data source is accurate.               |
|   4 | ; visual verification is required to trust agent outputs in observability domains.                                                                                                    |
|   5 | , providing the necessary evidence for verification without leaving the agent terminal.                                                                                               |
|   6 | , tool calls, and a UI resource that differentiates it from standard tools by offering a rendered view of the data.                                                                   |
|   7 | , allowing clients like Goose or Cloud Desktop to render interactive, sandboxed iframes that maintain context.                                                                        |
|   8 | (e.g., trace maps, correlated logs) within the MCP App or break out to static dashboards and return without losing investigation context.                                             |
|   9 | , supporting logs, traces, and metrics, with recent releases improving agent trace visualization.                                                                                     |
|  10 | , piggybacking on established authentication and context-passing mechanisms to create a single endpoint for agents and users.                                                         |
|  11 | ; this was solved by making apps composable with shared capabilities.                                                                                                                 |
|  12 | , authentication, and context (such as trace IDs and time ranges) across different investigation stages (e.g., alerting to tracing).                                                  |
|  13 | "App handoff" allows one app to pass context to the next, ensuring continuity in investigations and reducing the need for manual data re-entry.                                       |
|  14 | , ensuring consistent identification of resources (e.g., pod names) across metrics, logs, and traces.                                                                                 |
|  15 | , allowing users to verify the agent's reasoning.                                                                                                                                     |
|  16 | , catching regressions in tool descriptions, and testing against RCA datasets.                                                                                                        |
|  17 | , single sign-on, built-in correlations, and verifiable answers that reduce hallucination risks.                                                                                      |
|  18 | (like OpenSearch dashboards) that handles authentication and context sharing.                                                                                                         |
|  19 | , reducing Mean Time to Resolve (MTTR) and context switching.                                                                                                                         |
|  20 | "agentic era," where they serve as evidence for human verification rather than being replaced entirely by agents.                                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3TzG9NYlpwo/hqdefault.jpg)](https://www.youtube.com/watch?v=3TzG9NYlpwo)

[Watch on YouTube](https://www.youtube.com/watch?v=3TzG9NYlpwo)
