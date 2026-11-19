---
layout: default
title: "Beyond MCP: Building an Enterprise Knowledge Layer for... - Jeremy Adams - Casañas, Neo4j"
nav_order: 85
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Jeremy Adams, a senior developer advocate at Neo4j, presents a talk arguing that while the Model Context Protocol (MCP) serves as an essential "USB-C connector" for AI agents, it is insufficient fo...'
resource: "https://www.youtube.com/watch?v=uBNBDNaCuqQ"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Jeremy Adams, a senior developer advocate at Neo4j, presents a talk arguing that while the Model Context Protocol (MCP) serves as an essential "USB-C connector" for AI agents, it is insufficient for complex enterprise tasks due to context window limitations and the lack of semantic guidance.
Using the example of assessing financial exposure to a client, Adams demonstrates that allowing agents to naively access all available MCP tools results in inefficient, stochastic, and often misleading outcomes because the agent lacks specific business definitions and decision-making authority.
To address this, he proposes implementing an enterprise knowledge layer, or context layer, that sits between the LLM agent and the MCP servers to interpret intent, apply organizational ontologies, and enforce access policies.
By leveraging a graph database to map relationships between business concepts, enterprise systems, and organizational hierarchies, this layer enables deterministic workflows, such as automatically escalating decisions based on approval limits.
Adams concludes that this graph-based knowledge layer provides the necessary memory and structure to transform raw tool access into reliable, business-valuable insights, a topic he invites the audience to explore further at the upcoming Nodes conference.

# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | "knowledge layer" or "context layer" as the necessary next step beyond the Model Context Protocol (MCP) for enterprise AI agents.                                                       |
|   2 | "USB-C connector" for connecting agents to enterprise services, it has significant limitations when used in isolation.                                                                  |
|   3 | ; loading hundreds of tool descriptions consumes excessive tokens, increases costs, and degrades agent performance.                                                                     |
|   4 | , making it difficult for them to select the correct tools or understand specific business definitions, such as the precise meaning of "exposure" to a client.                          |
|   5 | , agents may produce stochastic, inconsistent, or misleading results by calling irrelevant tools or failing to correlate data from siloed systems.                                      |
|   6 | "exposure" requires firm, organization-specific definitions tied to actual data sources, rather than relying on LLM-generated interpretations which may lack nuance.                    |
|   7 | , such as wrapping multiple tools into a single "super tool" or using code-based workflows, can improve determinism but create maintenance burdens and limit stakeholder understanding. |
|   8 | , applying organizational ontologies, and enforcing access policies before tool execution.                                                                                              |
|   9 | , such as CRM, finance, and security platforms.                                                                                                                                         |
|  10 | , ensuring that material decisions are escalated to the appropriate approvers.                                                                                                          |
|  11 | (specifically Neo4j) allows for the creation of a "context graph" that records decisions, relationships, and business logic, providing persistent memory for the agent.                 |
|  12 | , such as determining whether to renew a client, by leveraging previously established data and decision records.                                                                        |
|  13 | "map" that guides the LLM agent, while MCP remains the "fabric" or connector to the underlying enterprise systems.                                                                      |
|  14 | , reduced token usage, and auditable decision trails in complex enterprise environments.                                                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/uBNBDNaCuqQ/hqdefault.jpg)](https://www.youtube.com/watch?v=uBNBDNaCuqQ)

[Watch on YouTube](https://www.youtube.com/watch?v=uBNBDNaCuqQ)
