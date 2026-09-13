---
type: Video Note
title: "Dapr in the AI Era: Orchestrating Complex Multi-agent Workflows With Automatic... Yaron Schneider"
description: "Yaron Schneider, CTO and co-founder of Dapr Grid, introduces the Dapr project and its role in making AI agents reliable and production-ready by addressing distributed systems challenges such as state management, workflow durability, and sec..."
resource: https://www.youtube.com/watch?v=9gejXxl5JzE
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Yaron Schneider, CTO and co-founder of Dapr Grid, introduces the Dapr project and its role in making AI agents reliable and production-ready by addressing distributed systems challenges such as state management, workflow durability, and secure agent communication.
He explains that while popular agent frameworks like LangChain and LangGraph focus on reasoning and tool integration, they lack robust mechanisms for reliability, failure recovery, and security at scale.
Dapr provides a set of APIs and building blocks—including workflows, pub/sub, state management, and conversation APIs—that enable agents to persist state across failures, communicate securely, and integrate with over 30 databases.
Schneider demonstrates Dapr Agents, a framework contributed by Nvidia, which ensures agents can resume exactly where they left off after crashes, unlike traditional checkpointing approaches.
He also showcases multi-agent collaboration using Dapr’s pub/sub system and highlights observability features like audit logs and traceability, emphasizing Dapr’s open-source, cloud-native, and vendor-neutral approach to building resilient AI systems.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yaron Schneider is CTO and co-founder of Dapr Grid, co-creator of Dapr, and chair of the workflow working group in the Agenda KI Foundation. |
|   2 | Focuses on making agents run reliably in production, preventing state loss and unnecessary repeated LLM calls.                               |
|   3 | Dapr is a set of APIs for developers to focus on business logic, not infrastructure; donated to CNCF, graduated in 2021.                     |
|   4 | Dapr supports multiple building blocks: workflows, pub/sub, state management, conversation API, observability, security, and resiliency.     |
|   5 | Workflows enable reliable, resumable agentic workflows, preventing full restarts after failures.                                             |
|   6 | Pub/sub allows agent discovery and communication across processes and pods, with at-least-once delivery guarantees.                          |
|   7 | State management supports over 30 databases, enabling easy migration and integration without code changes.                                   |
|   8 | Conversation API provides LLM abstraction and enterprise features like PII data obfuscation.                                                 |
|   9 | Dapr enforces access policies and trust domains for agent governance and security.                                                           |
|  10 | Dapr building blocks can be integrated into AI workloads for reliability and security.                                                       |
|  11 | AI introduces non-determinism and increases attack surface due to MCP servers and agent interactions.                                        |
|  12 | Reliability is a key concern; Dapr is used by companies like Nvidia for reliable, large-scale workflows.                                     |
|  13 | Dapr Agents framework (contributed by Nvidia) provides durable, cloud-native, vendor-neutral agents with 1.0 release.                        |
|  14 | Dapr Agents require minimal setup: Docker build, Dapr, and a database.                                                                       |
|  15 | Dapr Agents automatically connect agents, distribute traffic, and recover from failures without manual intervention.                         |
|  16 | Dapr workflows guarantee exactly-once execution, automatic failure detection, and recovery.                                                  |
|  17 | Existing agent frameworks rely on checkpointing, which lacks robust recovery and coordination.                                               |
|  18 | Dapr provides workflow integrations for popular agent frameworks; community contributions are encouraged.                                    |
|  19 | Multi-agent collaboration is supported with simple pub/sub conf                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9gejXxl5JzE)