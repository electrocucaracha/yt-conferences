---
layout: default
title: On-Call the Easy Way With Agents - Ryan Tay & Kartikeya Pharasi, Intuit
nav_order: 10
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  In this talk, Karthik and Ryan from Intuit’s service mesh team discuss
  their efforts to reduce the workload of on-call engineers by leveraging AI agents.
  They describe the scale at which Intuit operates—over 350 Kubernetes clusters and
  16 b...
resource: https://www.youtube.com/watch?v=oDli4CBkky8
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Karthik and Ryan from Intuit’s service mesh team discuss their efforts to reduce the workload of on-call engineers by leveraging AI agents.
They describe the scale at which Intuit operates—over 350 Kubernetes clusters and 16 billion daily transactions—and the resulting challenges in debugging complex, interconnected systems.
Their solution involves an AI agent that can independently analyze logs and metrics, utilize internal documentation, and select appropriate tools to assist engineers in diagnosing and resolving incidents.
The agent integrates with various input methods, uses retrieval-augmented generation to provide context-specific assistance, and automates steps from existing runbooks, significantly reducing manual effort and mean time to resolution.
Currently in early deployment, the agent operates in a dry-run mode, with plans to expand its capabilities and usage, while ongoing evaluation focuses on accuracy and efficiency, with future considerations for automation and cost optimization.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation by Karthik and Ryan from the service mesh team at Intuit on reducing on-call engineer toil using AI agents                                                       |
|   2 | Agenda: overview of Intuit's technology, service mesh platform scale, challenges, proposed AI agent solution, agent architecture, example results, benefits, and future goals |
|   3 | Intuit serves over 100 million users across TurboTax, QuickBooks, Mailchimp, and Credit Karma                                                                                 |
|   4 | Operates 350+ Kubernetes clusters, ~2,000 rollouts/deployments, 16B daily transactions, peak 292K DPS                                                                         |
|   5 | Debugging at scale is challenging due to vast data from interconnected services (logs, metrics)                                                                               |
|   6 | Existing dashboards and runbooks help with known issues, but new/complex issues and onboarding new engineers are difficult                                                    |
|   7 | Proposed solution: AI agent to read and analyze high-volume logs/metrics, match to probable root causes, and use predefined tools for resolution                              |
|   8 | AI agent: program that observes, analyzes, and makes decisions to solve problems                                                                                              |
|   9 | Agent workflow: user query triggers agent, orchestration layer communicates with LLM, tools fetch data/perform actions, results returned to user                              |
|  10 | Intuit uses GenoS platform to design, build, and deploy generative AI applications, providing access to models, agents, tools, tracing, memory, and evaluation                |
|  11 | Agent inputs: chat, Slack bot, or alert trigger; typically includes transaction ID or unique identifier                                                                       |
|  12 | Agent gathers context: logs, metrics, change logs, user info                                                                                                                  |
|  13 | Retrieval Augmented Generation (RAG) layer adds company-specific context from internal/public docs, indexed in a vector database                                              |
|  14 | LLM summarizes input/context, selects tools (functions with natural language descriptions), executes tools, and iterates as needed                                            |
|  15 | Tool selection relies on clear, natural language descriptions matching documentation                                                                                          |
|  16 | Tools can be collocated or remote; model context protocol enables agent/tool interoperability and registries                                                                  |
|  17 | Runbooks are translated into agent tools for automated debugging and mitigation steps                                                                                         |
|  18 | Example: agent parse                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oDli4CBkky8)
