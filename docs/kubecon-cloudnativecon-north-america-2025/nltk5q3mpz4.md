---
type: Video Note
title: "Inference Awakens: Tools for the Age of GenAI - Alexa Griffith, Bloomberg & Erica Hughberg, Tetrate"
description: "The transcript features a lively, cinematic-themed discussion about the evolving challenges and solutions in deploying generative AI workloads, particularly large language models, in modern cloud and hybrid environments. The speakers highli..."
resource: https://www.youtube.com/watch?v=nlTk5q3MPZ4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The transcript features a lively, cinematic-themed discussion about the evolving challenges and solutions in deploying generative AI workloads, particularly large language models, in modern cloud and hybrid environments.
The speakers highlight how traditional stateless microservice architectures and legacy gateways are struggling to handle the new, stateful, resource-intensive, and complex traffic patterns introduced by generative AI, which require more intelligent routing, advanced rate limiting, and unified security management.
They present an open-source, Kubernetes-based blueprint using tools like Envoy Gateway and KServe to enable scalable, cost-effective, and observable AI inference across on-premises and cloud infrastructure, emphasizing the importance of open standards, unified APIs, and robust monitoring with tools like OpenTelemetry and Prometheus.
The talk encourages collaboration within the open-source community, inviting participants to contribute use cases and questions, and concludes with introductions to the speakers and their organizations, underscoring the mission to build adaptable, AI-native platforms through open collaboration.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Generative AI introduces fundamentally different workloads, requiring new infrastructure and traffic patterns.                                               |
|   2 | Legacy gateways and tools struggle with GPU demand, context collapse, and complex routing for large language models (LLMs).                                  |
|   3 | New requirements include AI-native logic, intelligent routing based on context (capacity, token usage, cost, model selection), and advanced rate limiting.   |
|   4 | Enterprise security needs unified, managed credential handling across hybrid, multi-provider, and on-prem architectures.                                     |
|   5 | Observability must adapt to evaluate generative AI outputs, not just HTTP status codes.                                                                      |
|   6 | Kubernetes remains a viable platform, evolving to support LLM workloads using existing GPU infrastructure.                                                   |
|   7 | The inference extension to the Gateway API and open-source tools like Envoy and KServe enable advanced routing and scalable model serving.                   |
|   8 | Envoy provides extensible, reliable traffic routing for both on-prem and cloud, supporting failover and MCP routing.                                         |
|   9 | OpenTelemetry, Prometheus, Grafana, and OpenInference integrate for comprehensive monitoring and tracing of inference requests.                              |
|  10 | A tiered gateway architecture (AI gateway and inference gateway) supports unified LLM APIs, upstream authentication/authorization, and observability.        |
|  11 | Open-source solutions provide unified APIs for developers, supporting multiple providers (AWS, GCP, OpenAI) with integrated identity management.             |
|  12 | KServe offers scalable, declarative, production-ready model serving on Kubernetes, with first-class LLM support, multi-node inference, and advanced routing. |
|  13 | Collaboration across open-source projects (Envoy, KServe, OpenInference) is key to addressing new generative AI challenges.                                  |
|  14 | The open-source community encourages participation, contribution, and sharing of use cases to drive innovation.                                              |
|  15 | Contact information and hiring opportunities at Bloomberg and Tetrate were shared, with encouragement to join the open-source alliance.                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nlTk5q3MPZ4)