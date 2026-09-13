---
layout: default
title:
  "Dapr in 2026: Durable Execution and Resilient Eventing for AI Agents - Yaron
  Schneider & Rajesh Iyer"
nav_order: 50
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Ron Schneider, CTO and co-founder of DIG Grid, introduces Dapper as a
  set of APIs designed to help developers focus on business logic rather than infrastructure,
  highlighting its utility for platform teams and its thriving community. He dis...
resource: https://www.youtube.com/watch?v=4I19FPwLCIQ
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Ron Schneider, CTO and co-founder of DIG Grid, introduces Dapper as a set of APIs designed to help developers focus on business logic rather than infrastructure, highlighting its utility for platform teams and its thriving community.
He discusses Dapper’s growing role in AI and agentic frameworks, emphasizing features like service discovery, secure agent identity, PubSub for ambient agents, state management, and a conversation API with prompt caching and PII obfuscation.
Schneider presents Dapper Agents, a framework developed with Nvidia, which addresses common challenges in agentic systems such as failure recovery, parallel execution, secure identity, and seamless integration with various message brokers, while remaining vendor-neutral.
He demonstrates Dapper’s integration with Langraph, showing how Dapper’s state API enables support for over 30 databases, built-in tracing, metrics, resiliency policies, and encryption, all with minimal code changes.
Finally, he shares a case study from JP Morgan Chase, which chose Dapper for workflow orchestration in complex payment processes due to its reliability, state retention, compensating transactions, and suitability for distributed, fault-tolerant applications, and invites the community to participate in ongoing integrations and development.

# Main Points

|   # | Main point                                                                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dapper is a set of APIs enabling developers to focus on business logic instead of infrastructure.                                                                                                       |
|   2 | Dapper is widely used, with a large community, over 8,500 Discord members, and 4,000+ contributors.                                                                                                     |
|   3 | Notable end users include NASA, which uses Dapper on the International Space Station for glove image processing.                                                                                        |
|   4 | Dapper APIs support service discovery, mutual TLS, PubSub for ambient agents, and state management across 30+ databases.                                                                                |
|   5 | The Conversation API provides prompt caching and PII obfuscation for LLM interactions.                                                                                                                  |
|   6 | Agentic frameworks today lack robust PII guardrails, authentication for tool usage, reliable workflows at scale, and easy event-driven ambient agent creation.                                          |
|   7 | Dapper Agents framework, built with Nvidia, adds failure recovery, parallel execution, Spiffy-based identity, multi-agent eventing, and vendor-neutrality.                                              |
|   8 | Dapper Agents simplifies agent communication and recovery, requiring only agent code and message broker configuration.                                                                                  |
|   9 | Upcoming integrations include OpenAI agents, Langraph, Microsoft Agent Framework, AWS Trans, and Langfuse for observability.                                                                            |
|  10 | Dapper’s Langraph integration allows checkpointing to 30+ databases, built-in tracing, metrics, resiliency policies, and client-side encryption.                                                        |
|  11 | Switching databases (e.g., DynamoDB, Azure Cosmos DB) with Dapper requires only a YAML change, not code changes.                                                                                        |
|  12 | Dapper enables event-driven agent workflows and abstracts infrastructure details from developers.                                                                                                       |
|  13 | JP Morgan Chase selected Dapper for saga orchestration in complex payment workflows, valuing its fault tolerance, compensating transactions, rate limiting, workflow state visibility, and reliability. |
|  14 | Dapper is positioned as a generic, reliable workflow engine for multi-step, stateful, and fault-tolerant applications.                                                                                  |
|  15 | Dapper Agents offers demos for secure, reliable multi-agent workflows, including Kubernetes deployments.                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4I19FPwLCIQ)
