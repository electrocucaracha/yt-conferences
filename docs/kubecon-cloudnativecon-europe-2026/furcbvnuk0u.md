---
layout: default
title: "BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era"
nav_order: 29
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Hushing from Alibaba Cloud introduces Higress, a new Kubernetes gateway
  project that has recently joined the CNCF sandbox, designed to address the retirement
  of NGINX Ingress and its associated challenges such as traffic jitter, load balanc...
resource: https://www.youtube.com/watch?v=FURcBVNuK0U
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

Hushing from Alibaba Cloud introduces Higress, a new Kubernetes gateway project that has recently joined the CNCF sandbox, designed to address the retirement of NGINX Ingress and its associated challenges such as traffic jitter, load balancing issues, and scalability limitations.
Higress, built on Envoy, offers a two-in-one solution as both a traffic and microservices gateway, providing features like zero-downtime configuration reloads, Wasm plugin extensibility, and advanced security capabilities.
It supports seamless migration from NGINX Ingress by maintaining compatibility with existing annotations and the Gateway API, enabling users to transition without code changes.
Higress is production-proven, with case studies showing significant improvements in reload times and resource efficiency, and is adopted by major companies beyond Alibaba.
The project is evolving to meet the needs of AI-native workloads, offering features such as model fallback, token-aware rate limiting, semantic caching, and observability, making it a robust, extensible, and future-ready gateway solution for both traditional and AI-driven cloud environments.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Higris is a new Kubernetes gateway project from Alibaba Cloud, recently joined CNCF sandbox.                                                                                |
|   2 | NGINX Ingress is being retired; no further releases, bugfixes, or security patches.                                                                                         |
|   3 | 50% of global cloud native environments still use NGINX Ingress, creating migration challenges.                                                                             |
|   4 | Key issues with NGINX Ingress: traffic jitter for long-lived connections, gRPC load balancing problems, and scalability limitations during config reloads.                  |
|   5 | Alibaba migrated from NGINX Ingress to Higris, building on Envoy architecture.                                                                                              |
|   6 | Higris launched internally in 2020, proven stable at scale, and open sourced in 2022.                                                                                       |
|   7 | Higris combines traffic gateway and microservice gateway, achieving up to 50% cost reduction.                                                                               |
|   8 | Enhanced features include dynamic certificate management, extended service discovery, dual-stack support for NGINX annotations and Gateway API.                             |
|   9 | Data plane features: protocol translation (e.g., HTTP to Apache Dubbo), Wasm plugin support, native HTTP filters, and advanced telemetry.                                   |
|  10 | Core features:                                                                                                                                                              |
|  11 | Zero downtime configuration reloads.                                                                                                                                        |
|  12 | Wasm extensibility for hot-reloading plugins in multiple languages (Go, Rust, C++, JavaScript).                                                                             |
|  13 | Security features: bot detection, replay protection, IP restriction, rich authentication strategies, and guardrails.                                                        |
|  14 | Migration from NGINX Ingress to Higris supports existing annotations and gradual transition to Gateway API.                                                                 |
|  15 | Case study: COS reduced config reload time from 30 minutes to less than 5 seconds and cut memory usage by 10x after migrating to Higris.                                    |
|  16 | Higris is used by multiple companies, including DJI and Quopay.                                                                                                             |
|  17 | Higris supports AI-native gateway use cases: long-lived connections, payload-aware routing, model fallback, token-aware rate limiting, semantic caching, and observability. |
|  18 | Enables automatic OpenAPI to MCP server conversion for AI agents, simplifying data and reducing hallucination.                                                              |
|  19 | Case studies: Ctrip and Ant Group use Higris for AI gateway needs.                                                                                                          |
|  20 | Roadmap includes more Gateway API inference extension su                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FURcBVNuK0U)
