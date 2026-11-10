---
layout: default
title: "Who Watches the On-Call Agent? - Neelakshi Soni, Meta"
nav_order: 141
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Minakshi presents a framework for an AI on-call agent designed to automate root cause analysis for critical alerts, addressing the inefficiency of engineers manually navigating multiple dashboards ..."
resource: "https://www.youtube.com/watch?v=ovEpyYxKJPg"
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

Minakshi presents a framework for an AI on-call agent designed to automate root cause analysis for critical alerts, addressing the inefficiency of engineers manually navigating multiple dashboards and logs during high-stress incidents.
The agent operates by leveraging three core components: memory derived from past incident history and weekly knowledge sharing sessions, access to various system tools such as deployment history and server health metrics, and standardized playbooks that guide its investigation steps.
When an alert is triggered, the agent classifies the issue, retrieves relevant historical data, and analyzes current metrics and recent code changes to synthesize a likely root cause, which it then presents to the on-call engineer with supporting evidence.
To ensure reliability and continuous improvement, the system incorporates comprehensive observability features, including metrics, logs, traces, and evaluation mechanisms that assess the correctness of the agent’s conclusions using both LLM judges and human feedback.
The presentation concludes with key takeaways emphasizing the importance of detailed tracing, connecting data via common identifiers, measuring correctness rather than just completion, and monitoring system quality across releases to ensure the agent remains trustworthy in production environments.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : On-call engineers face significant challenges diagnosing root causes during alerts due to the need to manually aggregate data from disparate sources (dashboards, logs, deployment history, runbooks), leading to high cognitive load and delayed resolution.                                               |
|   2 | : An AI agent automates root cause analysis by classifying alerts, retrieving relevant historical incident data, and checking current system metrics, logs, and deployment changes to present a summarized evidence-based diagnosis to the engineer.                                                          |
|   3 | :                                                                                                                                                                                                                                                                                                             |
|   4 | : Learns from past incident resolutions, on-call handoff notes, and wiki documentation to recognize recurring patterns and apply previously successful resolution steps.                                                                                                                                      |
|   5 | : Access to observability dashboards, logs, deployment history, server/database health, and message capacity metrics.                                                                                                                                                                                         |
|   6 | : Standard Operating Procedures (SOPs) that guide the agent through specific investigation steps for different alert types.                                                                                                                                                                                   |
|   7 | : Specialized sub-agents (e.g., codebase, capacity, infrastructure) can operate in parallel to gather specific evidence, improving speed and depth compared to sequential processing.                                                                                                                         |
|   8 | : To ensure reliability, the agent itself requires observability consisting of four key pillars:                                                                                                                                                                                                              |
|   9 | : Tracks investigation duration, failure rates, and cost per run.                                                                                                                                                                                                                                             |
|  10 | : Captures tool results, errors, decision points, and context at specific moments.                                                                                                                                                                                                                            |
|  11 | : Connects individual steps (model calls, tool invocations) into a complete investigation run, allowing analysis of latency and token usage per step.                                                                                                                                                         |
|  12 | : Assesses the correctness of the agent’s conclusion, distinguishing between a completed investigation and a correct one.                                                                                                                                                                                     |
|  13 | : Correctness is judged by comparing the agent’s proposed root cause against known facts (e.g., recent configuration changes like timeout reductions) using LLM judges or human feedback from on-call engineers.                                                                                              |
|  14 | : Uses common identifiers (Trace ID, Incident ID, Timestamp) to link agent actions to specific incidents. This allows engineers to inspect why an agent took a specific path, identify bottlenecks (e.g., slow synthesis vs. fast metric retrieval), and debug failures.                                      |
|  15 | : Changes to prompts, tools, or models must be monitored for regressions. If accuracy drops, engineers can trace back from aggregate metrics to specific affected traces to identify the failing step.                                                                                                        |
|  16 | : The agent executes investigations via SDKs (e.g., OpenTelemetry), recording spans and events. These are validated, batched, and stored in a time-series database for dashboard querying and historical analysis.                                                                                            |
|  17 | :                                                                                                                                                                                                                                                                                                             |
|  18 | , tool calls, and investigation steps, not just final answers.                                                                                                                                                                                                                                                |
|  19 | , not just completion, as agents can be confidently wrong.                                                                                                                                                                                                                                                    |
|  20 | : To avoid hallucinations and manage large contexts, the agent relies on curated knowledge bases (weekly knowledge sharing sessions) and specific instructions to focus on relevant dependencies (e.g., checking specific database connections for payment APIs) rather than scanning all possible resources. |
|  21 | : While the described implementation targets monolithic architectures, scaling to microservices requires an orchestrator pattern with multiple specialized agents.                                                                                                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ovEpyYxKJPg/hqdefault.jpg)](https://www.youtube.com/watch?v=ovEpyYxKJPg)

[Watch on YouTube](https://www.youtube.com/watch?v=ovEpyYxKJPg)
