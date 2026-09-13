---
type: Video Note
title: "AI'm at the Gate! Introducing the AI Gateway Working G... Morgan Foster, Nir Rozenbaum & Shachar Tal"
description: 'The talk introduces a new working group focused on developing an "AI gateway," which extends traditional gateway capabilities to better support AI inference use cases. Unlike standard gateways that route requests based on headers or paths...'
resource: https://www.youtube.com/watch?v=JiQJcXvvajg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The talk introduces a new working group focused on developing an "AI gateway," which extends traditional gateway capabilities to better support AI inference use cases.
Unlike standard gateways that route requests based on headers or paths, an AI gateway enables routing and policy decisions based on the request and response payloads, such as model selection, prompts, and other AI-specific fields.
The group aims to standardize AI traffic management at the gateway layer in Kubernetes by creating new declarative APIs and composable, customizable architectures, while leveraging existing standards and community input.
Key proposals include introducing payload processors that can inspect, mutate, and make routing decisions based on the full HTTP payload, supporting ordered and scalable processing, and addressing failure modes and bidirectional processing.
The group also discusses the need for new backend and egress gateway resources to overcome current limitations in Kubernetes Gateway API, enabling more flexible and reusable policy attachments, especially for complex AI workloads, and invites community feedback to refine these designs.
# Main Points

|   # | Main point                                                                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of a new AI Gateway working group focused on building an AI gateway.                                                                                                                                          |
|   2 | AI gateway extends traditional gateway capabilities for AI use cases, enabling policies and routing based on request and response payloads.                                                                                |
|   3 | Key use cases include token-based rate limiting, fine-grained access control, payload inspection, semantic caching, semantic routing, guardrails, and AI-specific protocols.                                               |
|   4 | The group does not build new gateway implementations or define model serving behavior.                                                                                                                                     |
|   5 | Mission: Standardize AI traffic management at the gateway layer, develop declarative APIs and standards for AI workload networking in Kubernetes.                                                                          |
|   6 | Architecture goals: composable, pluggable, customizable, ordered execution of payload processing pipelines, leverage existing standards, and community collaboration.                                                      |
|   7 | Example flow: User sends AI request → authentication/authorization → quota check → payload processing (e.g., guardrails, semantic routing) → routing to in-cluster or out-of-cluster model → response processed similarly. |
|   8 | Payload processing proposal: Standard declarative mechanism for processing full HTTP payload (headers and body) in gateway API.                                                                                            |
|   9 | Properties: declarative configuration, ordered/concurrent execution, scalable, routing-capable, configurable failure modes, bidirectional (request/response), and rejection capability.                                    |
|  10 | Implementation: Payload processors as filters in HTTP route rules, with support for inline and reusable forms, can run in or outside the cluster.                                                                          |
|  11 | Open questions: wire protocol for processors, interaction with existing filters, execution order, gateway vs. route-level processors, processing loops, and community input needed.                                        |
|  12 | L7 egress gateway needed due to current gateway API focus on ingress and producer-centric primitives.                                                                                                                      |
|  13 | Problems with current egress solutions: vendor fragmentation, DNS/TLS policy issues, lack of consumer-focused primitives.                                                                                                  |
|  14 | Need for backend resource to attach default policies, support both internal/external backends, an                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JiQJcXvvajg)