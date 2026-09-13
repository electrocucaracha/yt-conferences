---
layout: default
title:
  "From Benchmarks To Business Value: Building a Use-Case Specific Agen... Gaurav
  Saxena & Matvey Kukuy"
nav_order: 26
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this presentation, Gor of Saxa and Metway discuss the challenges of
  evaluating AI agents in real-world, production environments, particularly within
  complex, infrastructure-dependent domains like automotive telemetry and incident
  response...
resource: https://www.youtube.com/watch?v=o7L6_MyOCt0
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Gor of Saxa and Metway discuss the challenges of evaluating AI agents in real-world, production environments, particularly within complex, infrastructure-dependent domains like automotive telemetry and incident response.
They argue that generic model benchmarks fail to capture the nuanced operational constraints—such as specific tool calls, credentials, environment states, and policies—that agents face in production, making it essential to assess agents within realistic scenarios relevant to the target platform.
The team proposes an agent evaluation framework combining three approaches: static validators (rule-based checks on tool usage), sub-agent auditors (agents that assess whether objectives are met), and observer agents (external evaluators analyzing agent traces), each with its own strengths and limitations.
They emphasize the importance of continuous, scenario-specific evaluation and metrics collection to ensure agent reliability, while acknowledging the challenges of environment-specific testing and the risk of blind spots in agent performance data.
The presenters invite the community to contribute to their open-source efforts and further refine these evaluation methods.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Gor of Saxa and Mattway presented on benchmarks to business value, proposing a use case-specific agent evaluation framework.                                                                                                                                |
|   2 | Emphasis on evaluating whether a specific agent can safely operate within real platform constraints (e.g., Kafka backlogs, Kubernetes incidents, Postgres failover).                                                                                        |
|   3 | Automotive industry example: vehicle telemetry and over-the-air update workflows are high-volume, stateful, and operationally sensitive; agent mistakes can cause significant issues.                                                                       |
|   4 | Existing benchmarks measure broad model capability but do not address if an agent can safely operate a specific platform.                                                                                                                                   |
|   5 | Real outcome depends on prompt quality, tool selection, runtime behavior, and stateful environment, not just model score.                                                                                                                                   |
|   6 | Agent performance is variable due to changes in models (e.g., cloud providers updating models) and tool calls.                                                                                                                                              |
|   7 | Tool call tracing should answer causal questions, not just record logs; important to know if a tool call moved the agent closer to resolution or wasted time.                                                                                               |
|   8 | Proposed approach: evaluate agents on real tasks, tools, credentials, and environment state, using realistic scenarios (e.g., Kafka partition under-replication, Kubernetes rollout failures, Postgres failover, schema drift, consumer lag, alert storms). |
|   9 | Mattway introduced their open-source platform focused on large enterprises, composable and pluggable, with agentic guardrails to prevent data exfiltration.                                                                                                 |
|  10 | Three evaluation methods: static validator (cheap, environment-specific), sub-agent auditor (compensates for environment, harder to implement), observer agent (expensive, works on gateway).                                                               |
|  11 | Joint metric combines all three evaluation methods for agent performance visibility.                                                                                                                                                                        |
|  12 | Benchmarks should be run both during agent building and in production to observe agent performance over time.                                                                                                                                               |
|  13 | Metrics are exported (e.g., Prometheus), but relying only on observed traffic can bias results toward frequent prompts, missing rare but critical cases.                                                                                                    |
|  14 | Full reevaluation should be combined with                                                                                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=o7L6_MyOCt0)
