---
layout: default
title:
  Intelligent Routing for Optimized Inference - Antonio Berben, Solo.io & Felipe
  Vicens, Telefonica
nav_order: 155
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Philipe Visense from Telefonica and Antonio from
  Solo IO discuss the inefficiency of using a single AI model for all types of queries,
  highlighting the potential for resource waste and increased costs. They propose
  an...
resource: https://www.youtube.com/watch?v=yeGhei0-bDA
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

In this presentation, Philipe Visense from Telefonica and Antonio from Solo IO discuss the inefficiency of using a single AI model for all types of queries, highlighting the potential for resource waste and increased costs.
They propose an open-source, agentic architecture that intelligently routes requests to the most suitable backend model based on factors like latency, cost, and accuracy, particularly in distributed and regulated telco environments.
The solution leverages a specialized agent gateway, intelligent routing, and Kubernetes-based orchestration, integrating various open-source projects and custom agents to dynamically evaluate and select models.
Through a demo, they illustrate how their system registers models, evaluates them for performance and cost (including electricity), and routes requests accordingly, achieving flexible, context-aware optimization.
The presenters also address challenges such as observability, geolocation, and zero trust security, and share lessons learned about the power of agentic workflows, the importance of context, and the need for robust observability in distributed AI systems.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Using the same AI model for all requests wastes resources, especially for simple queries.                                                                                     |
|   2 | Architecture proposed to route requests to the best backend model based on latency, cost, and accuracy using open source tools.                                               |
|   3 | Example: Translating "hello" to Spanish can be done by a large model (GPT-5) or a smaller, cheaper model (Microsoft 53), with up to 27x cost savings using the smaller model. |
|   4 | Telco environments require consideration of distributed infrastructure, regulatory compliance, data sovereignty, and SLAs.                                                    |
|   5 | API-based AI models incur token-based costs that may not scale with revenue.                                                                                                  |
|   6 | Solution involves a gateway to control traffic to LLM backends; Envoy is commonly used but has scaling and performance limitations.                                           |
|   7 | Alternative: Use an agentic gateway written in Rust for better performance and agentic workflows.                                                                             |
|   8 | Architecture uses a control plane, data plane, and intelligent router for agentic, extensible routing.                                                                        |
|   9 | KAgent (CNCF project) is used for declarative deployment of agents and orchestrating workflows.                                                                               |
|  10 | Intelligent router sets headers for routing based on request analysis.                                                                                                        |
|  11 | Explored LMD (on-prem inference), Open Policy Agent (OPA), and BLM Semantic Router; each had limitations for dynamic, real-time data or configuration.                        |
|  12 | Built custom intelligent router to optimize cost, latency, and accuracy in an agentic way.                                                                                    |
|  13 | Data plane handles user requests and header selection; control plane manages configuration via CRDs (LLM backends).                                                           |
|  14 | Agents evaluate models for cost, latency, accuracy, and electricity usage; results stored in CRDs.                                                                            |
|  15 | Registration flow: model registered, CRD created, orchestrator triggers evaluation and updates configuration.                                                                 |
|  16 | Challenges: telemetry for fresh metrics, geolocation for distributed models, enforcing zero trust security.                                                                   |
|  17 | 50+ use cases identified, including thermal/power-aware scheduling and exponential backoff resiliency.                                                                        |
|  18 | Lessons: everything can be agentic; skills enable distributed agent workflows; context and obs                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yeGhei0-bDA)
