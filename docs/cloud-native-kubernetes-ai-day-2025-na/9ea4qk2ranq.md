---
layout: default
title:
  "Beyond Chat: Bringing Agents To Kubernetes - Nimisha Mehta, Confluent & Nina
  Polshakova, Solo.io"
nav_order: 1
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  In this presentation, Nimisha and Nina introduce Kagent, a Kubernetes-native
  framework for building, running, and managing AI agents, emphasizing its declarative,
  cloud-native design and integration with Kubernetes features like security, s...
resource: https://www.youtube.com/watch?v=9EA4Qk2RaNQ
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Nimisha and Nina introduce Kagent, a Kubernetes-native framework for building, running, and managing AI agents, emphasizing its declarative, cloud-native design and integration with Kubernetes features like security, scaling, and observability.
They demonstrate how Kagent can automate infrastructure operations by deploying agents that interact with tools such as GitHub and Argo to identify and fix misconfigurations in real time, using a live demo to showcase its capabilities and challenges.
The speakers explain Kagent's architecture, including its use of custom resources for agents, model configurations, and tools, and highlight its flexibility to support both built-in and externally developed agents.
They discuss best practices for defining agents, the benefits of observability, and how Kagent enables complex, multi-agent workflows while remaining customizable and easy to integrate with other CNCF projects.
The talk concludes with an overview of the project's history, community involvement, and its complementary relationship with other projects like Kgateway, inviting attendees to explore further and participate in the community.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nimisha (Confluent) and Nina (Solo) introduced their talk on bringing AI agents to Kubernetes.                                                      |
|   2 | Both are members of the cloudnative AI working group and have worked on security white papers and agentic standards.                                |
|   3 | Audience survey showed widespread use of LLMs (e.g., ChatGPT, Claude) for debugging code and infrastructure, especially with Kubernetes and Helm.   |
|   4 | Mixed audience opinions on whether AI agents for infrastructure are underrated or overhyped.                                                        |
|   5 | Chatbots have limited value in infra operations due to lack of real-time context; autonomous agents can enrich context using live infra data.       |
|   6 | Introduced Kagent: a Kubernetes-native, declarative framework for building, running, and managing AI agents using custom resources and controllers. |
|   7 | Kagent leverages Kubernetes features like security, scaling, and observability.                                                                     |
|   8 | Demo: Used Kagent to detect and fix a misconfiguration in a microservices app via an agent with access to Kubernetes, Argo, and GitHub.             |
|   9 | Agents in Kagent are defined by a system prompt, model config (e.g., provider, temperature), and a list of tools (e.g., MCP server, other agents).  |
|  10 | Four main custom resources: MCP server, remote MCP server, model config, and agent.                                                                 |
|  11 | Agent chat sessions are stored in a relational database; resources can be managed via UI or CLI.                                                    |
|  12 | Kagent supports bring-your-own-agent (BYO) using different frameworks (e.g., Google ADK, Langraph, Curi).                                           |
|  13 | Kagent is cloudnative, declarative, supports RBAC, version control, and easy integration with CNCF projects.                                        |
|  14 | Supports complex multi-agent setups, event-driven invocations (Khook), and integration with external apps.                                          |
|  15 | Best practices: keep tool lists focused, use config maps for prompts, choose models wisely, leverage observability features.                        |
|  16 | Kagent emits logs/traces for visibility and supports Kubernetes benefits like RBAC and MTLS.                                                        |
|  17 | Kagent and Kgateway are separate but complementary projects; can be used together or independently.                                                 |
|  18 | Community resources: GitHub repository, CNCF                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9EA4Qk2RaNQ)
