---
type: Video Note
title: "Talk To Your Dashboards: Using MCP and LLMs To Simplify Observab... Prashant Gupta & Raj Bhensadadia"
description: "In this session, Prashant and Raj, machine learning engineers at Apple, discuss how Model Context Protocol (MCP) and large language models (LLMs) can simplify and enhance observability in complex systems. They highlight the challenges of fr..."
resource: https://www.youtube.com/watch?v=iS4-WC59a9s
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Prashant and Raj, machine learning engineers at Apple, discuss how Model Context Protocol (MCP) and large language models (LLMs) can simplify and enhance observability in complex systems.
They highlight the challenges of fragmented observability stacks, where multiple tools and dashboards create operational silos and inefficiencies.
By introducing MCP, an open standard that enables seamless, context-aware communication between LLM agents and observability tools like Grafana and Perses, they demonstrate how natural language can be used to create, modify, and troubleshoot dashboards across platforms.
The session includes a live demo showing how agents, powered by MCP, automate dashboard management, root cause analysis, and cross-platform interoperability, all while emphasizing the importance of guardrails such as role-based access control and audit trails for safe automation.
The presenters conclude that MCP and LLMs make observability more accessible, collaborative, and efficient, freeing engineers to focus on decision-making rather than manual configuration.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on using Model Context Protocol (MCP) and large language models (LLMs) to simplify observability.                            |
|   2 | Current observability systems are powerful but complex and fragmented across tools like Grafana, Prometheus, Cortex, and OpenSearch.         |
|   3 | Manual dashboard management leads to alert fatigue, slow incident response, and operational debt.                                            |
|   4 | LLM-powered agents can automate investigation, fixes, and insights using natural language, reducing manual work.                             |
|   5 | Agents connect observability data (logs, metrics, traces), LLM reasoning, and actions (insights, fixes).                                     |
|   6 | LLMs evolved from text generators to agents capable of function calls, API use, memory, planning, and tool use.                              |
|   7 | Integration fragility is a challenge due to different schemas, protocols, and authentication methods across tools.                           |
|   8 | MCP is an open standard enabling standardized, bidirectional, context-aware communication between LLM agents and observability systems.      |
|   9 | MCP servers expose tools, resources, and schemas in a self-describing, discoverable way; clients handle reasoning, streaming, and execution. |
|  10 | MCP reduces token usage by exchanging concise summaries, not full data payloads.                                                             |
|  11 | Open source MCP clients and servers exist for tools like Perses and Grafana.                                                                 |
|  12 | Demo showed creating, updating, and fixing dashboards via natural language, including cross-platform interoperability.                       |
|  13 | MCP enables dynamic dashboard creation, variable management, and root cause analysis through conversational interfaces.                      |
|  14 | Guardrails include policy and role-based access control, schema validation, and audit trails for safe automation.                            |
|  15 | MCP and LLMs make observability more accessible, flexible, and collaborative, especially for high-value, time-sensitive systems.             |
|  16 | Open source projects and documentation are available for MCP integration.                                                                    |
|  17 | Future work includes multi-agent frameworks and agent context protocols.                                                                     |
|  18 | Guardrails can be implemented with authentication tokens, role-based access, prompt validation, and explicit p                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=iS4-WC59a9s)