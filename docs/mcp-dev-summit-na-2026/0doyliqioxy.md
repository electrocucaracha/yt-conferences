---
layout: default
title:
  "Operating MCP in the Enterprise: From Protocol To Production - Amar Deep Singh
  & Neelabh Tripathi"
nav_order: 70
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Amardep Singh and Nilab, experienced IT and engineering architects, discuss
  the challenges and considerations of moving AI protocols, particularly large language
  models (LLMs) and agentic frameworks, from experimentation to production in en...
resource: https://www.youtube.com/watch?v=0dOYliqioxY
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Amardep Singh and Nilab, experienced IT and engineering architects, discuss the challenges and considerations of moving AI protocols, particularly large language models (LLMs) and agentic frameworks, from experimentation to production in enterprise environments.
They explain that while LLMs can generate insights from trained data, integrating real-time enterprise data and enabling actionable tasks requires additional components like embeddings, vector databases, and agent runtimes, often coordinated through an MCP server.
Unlike traditional, deterministic application flows, agentic systems operate dynamically based on user intent, making decisions and recommendations through tool integrations, which introduces complexities in observability, security, compliance, and integration with legacy systems.
The speakers emphasize the need for robust platform architecture with pillars such as security, governance, observability, model abstraction, and runtime orchestration to ensure operational efficiency, scalability, and compliance.
They conclude that, due to the probabilistic and evolving nature of AI agents, maintaining human oversight, strong governance, and comprehensive observability is essential for safe and effective enterprise deployment.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion on moving from protocol to production in enterprise environments.                                                                                |
|   2 | Speakers: Amardep Singh (GM Financial, IT architecture) and Nilab (Cisco, engineering architect).                                                           |
|   3 | LLMs (Large Language Models) only work on trained data and lack real-time access.                                                                           |
|   4 | Enterprises need to use their own data with LLMs, often via embeddings and vector databases.                                                                |
|   5 | RAG (Retrieval-Augmented Generation) approach helps but is not real-time or action-oriented.                                                                |
|   6 | LLMs alone cannot perform actions (e.g., restart Kubernetes pods); agents are needed for tool calls.                                                        |
|   7 | Agents act as runtimes making tool calls, separating responsibilities from LLMs.                                                                            |
|   8 | Evolution from single-agent runtimes with embedded tools to standardized MCP servers.                                                                       |
|   9 | MCP servers centralize tool access and allow agents to execute tasks in real time.                                                                          |
|  10 | Agentic frameworks differ from traditional application flows; agents focus on intent and outcomes, not static flows.                                        |
|  11 | Agents can provide recommendations and adapt, unlike deterministic traditional flows.                                                                       |
|  12 | Enterprises face challenges: multiple LLM providers, tool gateways, technical debt, redundancy, lack of observability, and integration with legacy systems. |
|  13 | Security, privacy, and compliance are critical due to dynamic agent behavior and sensitive data.                                                            |
|  14 | Need for operational efficiency, CI/CD, centralized security, unified observability, scalability, and resource efficiency.                                  |
|  15 | Governance is essential to prevent redundant or unnecessary agent use and manage costs and API key sprawl.                                                  |
|  16 | Proposed architecture includes four planes: security/governance/observability, model abstraction, runtime/orchestration, and domain/MCP server.             |
|  17 | Human-in-the-loop is necessary for agentic systems due to lack of determinism.                                                                              |
|  18 | Ability to swap models without code changes is important for flexibility and cost management.                                                               |
|  19 | Observability and auditability are mandatory for production deployment.                                                                                     |
|  20 | Maintaining state and session is a challenge when moving from la Ratings (1-5): 3                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0dOYliqioxY)
