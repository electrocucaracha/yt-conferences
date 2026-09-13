---
layout: default
title: "Cloud Native Theater | EnvoyCon: The Future of AI Traffic: What's New in
  Envoy AI Tra... Xiaolin Lin"
nav_order: 62
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Shins from the AI traffic team at Boomber presented on the future of
  AI traffic management and the development of the On AI Gateway, a project built
  atop the Envoy Gateway to address AI-specific challenges such as extracting model
  names fro...
resource: https://www.youtube.com/watch?v=7OkSrMBirmc
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Shins from the AI traffic team at Boomber presented on the future of AI traffic management and the development of the On AI Gateway, a project built atop the Envoy Gateway to address AI-specific challenges such as extracting model names from payloads, managing token usage costs, ensuring smart failover, and supporting multi-provider integration.
The gateway aims to provide a unified API layer for routing and managing AI traffic, automatic failover, robust security, policy frameworks for rate limiting, and strong observability features.
The project began in late 2024, with an initial release in early 2025, and has since expanded to support multiple cloud providers, token-based rate limiting, and production use by several companies.
Recent and upcoming features focus on cost optimization through quota-aware routing, context caching, and batch processing, as well as enhanced API compatibility for agentic workflows, embeddings, and multimodal tasks.
The gateway demonstrates millisecond-level performance and scalability, and the team encourages community participation and feedback.
During the Q&A, a question about listener sets in Envoy Gateway was raised, with the team expressing willingness to investigate further based on user needs.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Shins from Boomber AI traffic team presented on the future of AI traffic and the AI gateway project.                                                    |
|   2 | Traditional AI API gateways face challenges such as extracting model names from payloads, controlling token usage costs, and handling model failover.   |
|   3 | Need for multi-provider integration due to different APIs, authentication, and capacity types.                                                          |
|   4 | Operational ease and governance, including observability and token usage monitoring, are key objectives.                                                |
|   5 | The AI gateway is built on top of Envoy Gateway, focusing on AI-specific workloads.                                                                     |
|   6 | Key features: unified API layer for routing and managing AI traffic, automatic failover, end-to-end security, and a policy framework for rate limiting. |
|   7 | The project is open source, with contributions from a global community.                                                                                 |
|   8 | Timeline:                                                                                                                                               |
|   9 | Late 2024: Proposal and community engagement.                                                                                                           |
|  10 | Feb 2025: Initial release with unified APIs, upstream authentication (Azure, AWS), token-based rate limiting, and traffic management.                   |
|  11 | End of 2025: Production-ready, extended provider support (GCP, Anthropic), observability, and MCP support.                                              |
|  12 | 2026: Focus on cost optimization (quota-aware routing, caching, batch processing).                                                                      |
|  13 | Unified API uses OpenAI format, transforming requests/responses for specific providers.                                                                 |
|  14 | Supports flexible authentication (API keys, OpenID Connect, Azure ID, GCP workload federation).                                                         |
|  15 | Enables cross-provider and region failover for reliability.                                                                                             |
|  16 | Observability tracks token usage per request, model, provider, and application; supports tracing for streaming and non-streaming cases.                 |
|  17 | API CR is at v1 beta, stable and used in production by several companies.                                                                               |
|  18 | Cost optimization pillars: quota-aware routing, context caching, batch processing.                                                                      |
|  19 | Quota-aware routing prioritizes backends with available quota, supports fallback to on-demand.                                                          |
|  20 | Context caching reduces costs by reusing prompt content.                                                                                                |
|  21 | Batch processing leverages provider discounts for non-time-sensitive workloads.                                                                         |
|  22 | New APIs: response API for agentic workf                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7OkSrMBirmc)
