---
type: Video Note
title: "Lessons Applied Building a Next-generation AI Proxy - John Howard, Solo.io"
description: "John Howard from Solo.io discusses the evolution of network proxies, highlighting the shift from early solutions like Apache and NGINX to Envoy, which addressed the needs of microservices. With the rise of AI workloads, new requirements suc..."
resource: https://www.youtube.com/watch?v=qa5vSE86z-s
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

John Howard from Solo.io discusses the evolution of network proxies, highlighting the shift from early solutions like Apache and NGINX to Envoy, which addressed the needs of microservices.
With the rise of AI workloads, new requirements such as LLM observability, token-based rate limiting, failover across models and providers, and universal API abstraction emerged, prompting Solo.io to develop the Glue AI Gateway by extending Envoy with Python sidecars.
However, the introduction of the Model Context Protocol (MCP) revealed limitations in Envoy’s extensibility, leading to the creation of Agent Gateway—a new proxy built from the ground up in Rust, optimized for Kubernetes and AI-native use cases.
Agent Gateway natively supports leading AI protocols (MCP, LLM, A2A), traditional gateway features, and emphasizes simplicity, performance, and user-centric design by minimizing complexity and aligning internal models with user-facing APIs.
Performance benchmarks show significant improvements over Envoy-based solutions, especially in handling dynamic workloads and AI-specific traffic, and the project is open source under the Linux Foundation.
# Main Points

|   # | Main point                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | John Howard from Solo.io discusses building a next-generation AI proxy.                                                                                                                               |
|   2 | Reviews the evolution of proxies: Apache HTTP Server, NGINX, rise of microservices, and Envoy.                                                                                                        |
|   3 | AI introduces new infrastructure requirements: deep LLM observability, LLM-aware rate limiting (by tokens), LLM failover, universal API abstraction, and support for new protocols like MCP.          |
|   4 | Solo.io launched Glue AI Gateway by extending Envoy with a Python sidecar for AI functionality.                                                                                                       |
|   5 | MCP (Model Context Protocol) enables LLMs to interact with external tools, increasing complexity for networking infrastructure.                                                                       |
|   6 | Envoy was stretched to its limits for AI use cases; MCP requirements led to building a new proxy from scratch: Agent Gateway.                                                                         |
|   7 | Agent Gateway was designed with native MCP support, LLM support, and later added A2A (Agent-to-Agent) protocol support.                                                                               |
|   8 | Maintains standard API gateway features (retries, timeouts, logging, tracing, authorization) alongside AI features.                                                                                   |
|   9 | Built natively for Kubernetes, written in Rust for speed, security, and leveraging modern libraries.                                                                                                  |
|  10 | Incorporates lessons from Envoy and Ztunnel (from Istio) for specialized, efficient proxy design.                                                                                                     |
|  11 | Features include full Gateway API conformance, HTTP and LLM rate limiting, authentication/authorization, universal API, guardrails for LLM content, MCP native auth, and inference extension support. |
|  12 | Emphasizes few building blocks (e.g., using CEL—Common Expression Language) for policy and extensibility, reducing complexity compared to Envoy’s many extension mechanisms.                          |
|  13 | Retains only essential extensibility: external authorization and external processing.                                                                                                                 |
|  14 | Designed APIs and internals from user needs, avoiding “envoyisms” and ensuring a 1:1 mapping between user-facing and internal representations.                                                        |
|  15 | Optimized for real user patterns (frequent pod changes, fewer gateways/routes), enabling efficient, granular updates and reducing control/data plane resource usage by 25–50x compared to Envoy.      |
|  16 | Built all processing natively in o                                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qa5vSE86z-s)