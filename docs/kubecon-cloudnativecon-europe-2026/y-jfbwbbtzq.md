---
type: Video Note
title: "Unifying Inner & Outer Loops To Bridge the Gaps Between Devs... Laurent Broudoux & Mathieu Benoit"
description: "In this session, the presenters address the common challenge of ensuring smooth transitions between development and production environments, aiming to reduce cognitive load and resource consumption for developers and platform engineers. The..."
resource: https://www.youtube.com/watch?v=Y_jfBWbBTZQ
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, the presenters address the common challenge of ensuring smooth transitions between development and production environments, aiming to reduce cognitive load and resource consumption for developers and platform engineers.
They introduce a demo application based on a microservices architecture and explain the difficulties developers face when managing numerous dependencies and configurations across different environments.
The talk focuses on two open-source tools: Score, which provides an abstraction layer for defining workload specifications agnostic of the underlying platform, and Microx, which enables the mocking of API dependencies using contract-based simulations.
By integrating Score and Microx, developers can selectively mock unavailable or resource-intensive services, reducing the need to run all dependencies locally or in staging, while maintaining consistent configurations and minimizing configuration drift.
The approach also supports automated contract testing to ensure API compliance, streamlining development workflows and improving productivity across various stages of the software lifecycle.
# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session addresses the "it works on my machine" problem and aims to ease transitions from local development to production.                                                 |
|   2 | Focus on reducing cognitive load and resource consumption for developers and platform engineers.                                                                          |
|   3 | Demo application: Trader Hicks, a microservices-based banking app with many components and dependencies.                                                                  |
|   4 | Challenges: complex architecture, resource-heavy local development, configuration drift between environments, and dependency access issues.                               |
|   5 | Introduction of two CNCF sandbox projects: Score and Microx.                                                                                                              |
|   6 | Score: a workload specification tool allowing developers to describe application intent and dependencies in an abstract, platform-agnostic way.                           |
|   7 | Score implementations can generate Docker Compose or Kubernetes manifests from the same Score file, reducing the need for developers to manage platform-specific configs. |
|   8 | Platform engineers define how dependencies (e.g., databases) are provisioned per environment.                                                                             |
|   9 | Microx: a tool for mocking API dependencies using API contracts (OpenAPI, Postman collections, GraphQL, gRPC, etc.).                                                      |
|  10 | Microx enables developers to simulate unavailable or resource-heavy services, reducing local resource usage and speeding up development.                                  |
|  11 | Microx supports advanced mocking features: templating, scripting, stateful mocks, and observability via OpenTelemetry.                                                    |
|  12 | Seamless integration: Score and Microx together allow selective deployment of real services and mocking of others without changing Score files.                           |
|  13 | Developers can run only necessary services locally; dependencies are mocked automatically, lowering resource consumption.                                                 |
|  14 | Microx provides a UI for inspecting, observing, and fine-tuning mocks.                                                                                                    |
|  15 | Mocking can be used in various environments (dev, staging, QA) to reduce provisioning needs and costs.                                                                    |
|  16 | Microx supports contract testing, automatically generating test suites to ensure API implementations conform to contracts.                                                |
|  17 | The approach bridges the gap between local and production environments, reduces configuration dri                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Y_jfBWbBTZQ)