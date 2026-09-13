---
layout: default
title:
  "Project Lightning Talk: Envoy Today: What’s New In Managing Cloud-Native And
  AI Workl... Karol Szwaj"
nav_order: 258
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker celebrates the 10th anniversary of the Envoy project, highlighting
  its evolution from a proxy at a lift company to a foundational component in the
  cloud-native networking ecosystem. The core Envoy proxy serves as a high-performa...
resource: https://www.youtube.com/watch?v=g3CHzGl2zS0
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

The speaker celebrates the 10th anniversary of the Envoy project, highlighting its evolution from a proxy at a lift company to a foundational component in the cloud-native networking ecosystem.
The core Envoy proxy serves as a high-performance Layer 7 proxy used in service meshes, API gateways, and edge proxies, while subprojects like Envoy Gateway and Envoy AI Gateway extend its capabilities for Kubernetes integration and AI traffic management, respectively.
The talk details how AI traffic differs from traditional HTTP, requiring advanced observability and management features, and outlines ongoing roadmap developments such as native protocol support, inference improvements, and enhanced telemetry.
Adoption metrics are impressive, with millions of Helm chart and image pulls, thousands of GitHub stars, and hundreds of contributors.
The speaker invites attendees to learn more through a curated calendar of Envoy-related talks and encourages participation in the 10-year anniversary celebrations and ongoing community discussions.

# Main Points

|   # | Main point                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Envoy project celebrates its 10th anniversary, originating as a proxy at Lift and now a key component in cloud-native networking.                                                                        |
|   2 | Core Envoy Proxy is a high-performance L7 proxy, foundational for service mesh, API gateway, and edge proxy use cases.                                                                                   |
|   3 | Envoy Gateway is a Kubernetes-native control plane, simplifying Envoy proxy adoption and managing infrastructure proxies via Gateway API.                                                                |
|   4 | Envoy AI Gateway is a new subproject, extending data and control plane for managing AI/ML traffic using processors and internal CRDs for inference.                                                      |
|   5 | AI traffic differs due to long-lived streaming inference calls, token-based requests, variable costs, and complex workflows across multiple backends.                                                    |
|   6 | Enhanced observability is needed to track model performance, token usage, and costs in AI workflows.                                                                                                     |
|   7 | Roadmap includes moving AI traffic management features into core Envoy Proxy, such as native protocol support (MCP, agent-to-agent), inference improvements (request buffering, cross-service failover). |
|   8 | Envoy Gateway adds extensibility points and filter integrations to support diverse use cases.                                                                                                            |
|   9 | AI Gateway is progressing from alpha to beta, aiming for general availability, and supports OpenAI standard agents, token budgets, rate limits, and richer telemetry for LLM backends.                   |
|  10 | Focus on Gateway API v1.5 conformance and new load balancing features in Envoy Gateway.                                                                                                                  |
|  11 | Adoption metrics: Envoy Gateway reached 2.1 million Helm chart pulls in 30 days, 5 million image pulls, core Envoy Proxy has over 27,000 GitHub stars, and 300+ unique contributors.                     |
|  12 | Luma calendar available for all Envoy-related talks and end-user performance details.                                                                                                                    |
|  13 | 10-year anniversary celebration and opportunities to meet maintainers at the project pavilion (P11A) from Tuesday to Thursday.                                                                           |
|  14 | Invitation to join Envoy Slack for feature and user discussions.                                                                                                                                         |
|  15 | Speaker: Kosi, software engineer at Kubernatic and Envoy Gateway maintainer.                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=g3CHzGl2zS0)
