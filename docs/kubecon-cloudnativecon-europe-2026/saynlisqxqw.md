---
layout: default
title:
  "REST in Peace: AI Needs to Be Async - Meet Asya - Artem Yushkovskiy, Delivery
  Hero"
nav_order: 304
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Artam introduces a talk on AI orchestration, focusing on the challenges
  of scaling AI pipelines at Delivery Hero, particularly for automatic image improvement
  tasks. He describes how traditional pipeline architectures, using tools like Kube...
resource: https://www.youtube.com/watch?v=SaYnLISqxQw
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

Artam introduces a talk on AI orchestration, focusing on the challenges of scaling AI pipelines at Delivery Hero, particularly for automatic image improvement tasks.
He describes how traditional pipeline architectures, using tools like Kubeflow, become inefficient at scale due to issues like resource contention and complex retry logic, leading to significant engineering overhead.
To address this, his team developed Asia, an open-source tool that treats each pipeline step as an independent actor communicating via messages, with routing information embedded in the messages themselves, enabling greater flexibility, error isolation, and scalability.
The architecture separates concerns between data scientists and platform engineers, allowing pure Python functions for business logic and CRDs for infrastructure, and supports agentic workflows and dynamic routing.
Artam demonstrates the workflow, highlights integration with Kubernetes-native tools, and emphasizes the project's modularity, composability, and minimal abstractions, inviting feedback and contributions from the community.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter: Artam, discussing AI orchestration and the open source tool Asia from async actors, built at Delivery Hero.                                 |
|   2 | Delivery Hero use case: automatic image improvement for food delivery app; challenges with scaling and corner cases.                                   |
|   3 | Scaling issues: pipelines work in demos but fail at scale due to complex retry logic, thread pools, and infrastructure concerns.                       |
|   4 | Initial solution: extracted AI API, deployed models locally, connected via pub/sub queues; still faced pipeline waiting and resource heterogeneity.    |
|   5 | Main problem: managing multiple deployments (Cubeflow, backend servers, request/response over queues) consumed 60-80% of engineering time.             |
|   6 | New approach: flatten pipelines into microservices (actors) that communicate via messages; no central orchestrator, routing info embedded in messages. |
|   7 | Benefits: errors localized to individual actors, system scales efficiently, actors scale based on queue workload (using K autoscaler).                 |
|   8 | Architecture:                                                                                                                                          |
|   9 | CRD defines async actor.                                                                                                                               |
|  10 | Python container (runtime) runs user handler, communicates with Go sidecar over HTTP/Unix socket.                                                      |
|  11 | Optional state proxy sidecar for external memory abstraction.                                                                                          |
|  12 | Gateway translates HTTP requests to messages, tracks status, supports A2A and MCP protocols.                                                           |
|  13 | Code separation: data scientists write pure Python functions; platform engineers manage CRDs.                                                          |
|  14 | Flavors: preconfigured cluster configurations to reduce boilerplate in CRDs.                                                                           |
|  15 | Message structure: payload, headers, routing info; actors can modify routing dynamically.                                                              |
|  16 | Asia SDK: allows defining Python function flows, compiles to flat actor graphs and CRDs for deployment.                                                |
|  17 | Testing: flows can be run as pure functions locally; decorators annotated and mapped to CRD fields.                                                    |
|  18 | Deployment: uses Docker images, scaffold.yaml for mapping, supports customized patches.                                                                |
|  19 | Integration: Kubernetes-native, integrates with OpenTelemetry, Prometheus, Tempo, Loki for tracing and metrics.                                        |
|  20 | Key principles: minimal abstractions (only actor CRD                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SaYnLISqxQw)
