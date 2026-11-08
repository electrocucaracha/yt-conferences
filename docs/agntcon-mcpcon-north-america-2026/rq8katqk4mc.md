---
layout: default
title: "Your Agents Need a Router: One Integration for Every Model and Tool - Varun Talwar, Tetrate"
nav_order: 37
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Varun, co-founder of Tetrate, introduces Agent Router, an open-source project recently donated to the AI Foundation that leverages the Envoy proxy to manage AI traffic."
resource: "https://www.youtube.com/watch?v=rQ8KaTQk4Mc"
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

Varun, co-founder of Tetrate, introduces Agent Router, an open-source project recently donated to the AI Foundation that leverages the Envoy proxy to manage AI traffic.
He explains that while agents should focus on core reasoning, they are often burdened with non-core tasks such as API authentication, error handling, and cost management, which Agent Router offloads to a centralized middleware layer.
This infrastructure addresses the unique challenges of AI workloads, including bursty traffic patterns, rapid model evolution, and the need for strict security and budget controls that traditional HTTP gateways do not handle.
By using Envoy’s dynamic programmability, Agent Router enables features like model virtualization, intelligent routing to local or cloud models for cost efficiency, and granular policy enforcement for tool access.
The talk concludes with practical advice on implementing the router to centralize governance, ensure observability, and maintain system resilience, emphasizing that this approach allows enterprises to manage diverse agent harnesses and models through a single, secure, and cost-effective control point.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Tetrate has donated Agent Router to the AI Foundation (AIF), making it an open-source project built on the Envoy proxy.                                               |
|   2 | : Agent Router offloads non-core logic (API calls, authentication, fallbacks, cost calculation) from agents, allowing agents to focus solely on reasoning.              |
|   3 | :                                                                                                                                                                       |
|   4 | (no weekends/sickness), placing significant pressure on backends and tools.                                                                                             |
|   5 | (every few months), requiring dynamic handling.                                                                                                                         |
|   6 | , often using high-cost models for simple tasks (the "Ferrari" analogy).                                                                                                |
|   7 | :                                                                                                                                                                       |
|   8 | : Routes requests to the most optimal model (cloud, local, or open-weight) based on cost, compliance, or capability.                                                    |
|   9 | : Provides failover, retries, and health-based backend selection to maintain agent availability.                                                                        |
|  10 | & Governance**: Enables budget controls, rate limiting, and spend tracking to prevent quota exhaustion and financial bleed.                                             |
|  11 | & Authorization**: Enforces "deny by default" policies, controlling which users or agents can access specific tools (e.g., restricting finance tools to finance teams). |
|  12 | : Acts as a central point for observing request costs, latency, and traffic patterns.                                                                                   |
|  13 | :                                                                                                                                                                       |
|  14 | , dynamic programmability via XDS.                                                                                                                                      |
|  15 | (Model Context Protocol) servers.                                                                                                                                       |
|  16 | :                                                                                                                                                                       |
|  17 | : Run via CLI (`ai-gateway run`) on a desktop to route local model requests.                                                                                            |
|  18 | : Deploy via Docker images or Helm charts on any machine or Kubernetes cluster.                                                                                         |
|  19 | : Tetrate offers a multi-cloud, multi-tenant enterprise version with advanced features like MCP profiles.                                                               |
|  20 | :                                                                                                                                                                       |
|  21 | , FinOps, and data controls centrally before enabling broad team adoption.                                                                                              |
|  22 | "off-rails" behavior.                                                                                                                                                   |
|  23 | & Tips**:                                                                                                                                                               |
|  24 | (allow-list) rather than blacklisting for tool access.                                                                                                                  |
|  25 | & Future**:                                                                                                                                                             |
|  26 | (like Agent Gateway) primarily by implementation choices and data plane, though capabilities and intent are similar.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rQ8KaTQk4Mc/hqdefault.jpg)]("https://www.youtube.com/watch?v=rQ8KaTQk4Mc")

[Watch on YouTube](https://www.youtube.com/watch?v=rQ8KaTQk4Mc)
