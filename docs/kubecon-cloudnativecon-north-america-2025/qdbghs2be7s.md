---
layout: default
title:
  Why Is My Query Slow? Real AI Use Cases With Vitess + Kubernete... Brett Warminski
  & Gourav Khanijoe
nav_order: 343
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Brett Winsky and Gurov from HubSpot discuss how their data
  infrastructure team addressed the recurring challenge of slow database queries and
  operational support at scale. They describe their technical stack, which includes
  AW...
resource: https://www.youtube.com/watch?v=qDBgHS2bE7s
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Brett Winsky and Gurov from HubSpot discuss how their data infrastructure team addressed the recurring challenge of slow database queries and operational support at scale.
They describe their technical stack, which includes AWS, Kubernetes, Vitess, MySQL, and monitoring tools like Prometheus and Grafana, supporting over 1,600 production databases and 1.3 million queries per second with a small team.
To reduce operational load and improve self-service for hundreds of product engineers, they integrated AI and LLMs into their workflows, enabling automated analysis and plain-English explanations of complex query performance data.
They detail the evolution of their AI-powered tools, including prompt engineering and a two-phase LLM filtering system, which significantly improved the quality of automated suggestions and reduced on-call toil.
Additionally, they share how agentic AI systems now assist with support requests, documentation search, and operational reviews, leading to a 25% reduction in support time and increased user satisfaction, and announce plans to open source their prompts and tools for community collaboration.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Only AI-focused talk at the conference, presented by HubSpot's data infrastructure team.                                                                       |
|   2 | Main topic: addressing "Why is my query slow?" and improving database troubleshooting.                                                                         |
|   3 | HubSpot uses AWS, EBS, Kubernetes, CNCF tooling, Vitess for sharding/lifecycle, MySQL, Prometheus, Grafana, Victoria Metrics.                                  |
|   4 | Infrastructure: 1,600+ production databases, 31,000+ pods, 1.3 million queries/sec in North America, ~10 engineers supporting hundreds of product engineers.   |
|   5 | Automation and self-service are essential for scaling; AI and LLMs have been integrated over the past two years.                                               |
|   6 | AI reduces troubleshooting time, repetitive questions, and on-call toil.                                                                                       |
|   7 | Product engineers use self-service tools: Grafana dashboards (keyspace health, query fingerprint), internal log aggregation (log fetch), and MySQL explain UI. |
|   8 | MySQL explain plans are detailed but hard to interpret; engineers struggled despite available tools.                                                           |
|   9 | Introduced an AI-powered UI widget that summarizes query issues and suggests fixes using LLMs.                                                                 |
|  10 | Initial LLM suggestions were only 60% useful; prompt engineering and a two-phase LLM filtering process improved actionable advice to 80%.                      |
|  11 | AI system architecture: UI → genAI service → RAG (retrieves docs, Slack threads, schema, plans) → LLM → second LLM filters for actionable output.              |
|  12 | Result: significant reduction in operational pain, increased user satisfaction, and tool adoption.                                                             |
|  13 | Built AI agents to analyze query patterns in aggregate, using metrics from Prometheus, Grafana, Victoria Metrics.                                              |
|  14 | AI agents can read graphs, analyze trends, and describe findings in plain English.                                                                             |
|  15 | Support workflow improved: from doc search and Slack threads to a help portal with hybrid/vector search and a multimodal agentic system (Claude, Open Web UI). |
|  16 | Engineers now build mini-tools and agent flows first, then specialized UIs if needed.                                                                          |
|  17 | Internal REST endpoints annotated for agent use; tools include access debugging, query analysis, and resource discovery.                                       |
|  18 | Ops review process                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qDBgHS2bE7s)
