---
layout: default
title:
  'Taming Complexity: Building Observable Workflows... Mauricio "Salaboy" Salatino
  & Kasper Borg Nissen'
nav_order: 352
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, the presenters discuss the growing complexity of modern
  distributed systems, particularly as architectures evolve from monolithic and microservices
  to agentic, AI-driven workflows. They highlight the challenges of building and...
resource: https://www.youtube.com/watch?v=XVEPKb0aCx8
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

In this talk, the presenters discuss the growing complexity of modern distributed systems, particularly as architectures evolve from monolithic and microservices to agentic, AI-driven workflows.
They highlight the challenges of building and observing such systems, using a demo of a pizza ordering application with multiple interacting agents (store manager, drinks, cooking, delivery) orchestrated via protocols like MCP and A2A, and supported by frameworks such as Dapr and LangChain4j.
The speakers emphasize the importance of observability, noting that traditional tracing methods struggle with the nondeterministic and asynchronous nature of agentic workflows, and advocate for the adoption of open standards like OpenTelemetry to collect and analyze telemetry data across diverse languages, protocols, and tools.
They share practical insights on instrumenting applications, propagating context, and handling new complexities introduced by skills and scripts, while acknowledging current limitations and the need for further standardization and maturity in observability tooling.
The session concludes with encouragement for continued community collaboration to improve the developer experience and reliability of these complex systems.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on building observable workflows and managing complexity in modern distributed systems.                                                                              |
|   2 | Shifted from asynchronous workflows to agentic architectures involving agents, MCP servers, skills, and LLMs.                                                                         |
|   3 | Presenters: Casper (principal developer advocate at Zero, Cloud Native Nordics) and Salatino (ecosystem engineer at Diagrid, Dapper project).                                         |
|   4 | As applications and infrastructure grow in complexity, proper observability tools are essential.                                                                                      |
|   5 | Architectures have evolved from monoliths to microservices, event-driven, and now agentic systems.                                                                                    |
|   6 | Business agents perform critical business operations and are more user-facing; coding agents like Gemini/Codex are out of scope.                                                      |
|   7 | Key considerations for agentic applications: agentic frameworks, agent-to-agent protocols, LLM providers/models, tooling, MCP, and skills.                                            |
|   8 | MCP protocol standardizes LLM interactions with tools/services; agent-to-agent (A2A) protocol enables agent communication, focusing on enterprise needs like security and resiliency. |
|   9 | Skills (introduced Dec 2023) define agent capabilities via MD files and scripts, adding complexity to observability.                                                                  |
|  10 | Demo: Pizza store app with four agents (store manager, drinks, cooking, delivery), multiple microservices, and LLMs via MCP.                                                          |
|  11 | Dapper workflows ensure reliable, auditable, and resumable long-running processes in agentic systems.                                                                                 |
|  12 | Observability challenges: context propagation, nondeterministic workflows, multiple protocols, and languages.                                                                         |
|  13 | OpenTelemetry is becoming the de facto standard for observability; supports auto/manual instrumentation and works across languages.                                                   |
|  14 | Instrumentation can be injected via sidecars (Go) or agents (Java); context propagation is critical for meaningful traces.                                                            |
|  15 | Traditional tracing struggles with agentic workflows due to broken context and complex reasoning steps.                                                                               |
|  16 | Semantic conventions for agentic telemetry are emerging but not yet standardized.                                                                                                     |
|  17 | Observing agent reasoning and tool interactions is challenging; AI c                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XVEPKb0aCx8)
