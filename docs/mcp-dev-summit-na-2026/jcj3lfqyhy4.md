---
type: Video Note
title: "Sponsored Session: Agents and MCP @ Google Scale - Alan Blount & Vaibhav Katkade, Google Cloud"
description: "In this presentation, Alan Blunt, a technical product manager at Google Cloud AI, and his colleague Bob provide an overview of how Google extensively uses MCP (Model Control Protocol) across its infrastructure and products. Alan describes t..."
resource: https://www.youtube.com/watch?v=jCJ3LfqyHy4
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Alan Blunt, a technical product manager at Google Cloud AI, and his colleague Bob provide an overview of how Google extensively uses MCP (Model Control Protocol) across its infrastructure and products.
Alan describes the broad integration of MCP in agent development, highlighting tools like the open-source ADK framework, Gemini Enterprise, and various MCP-enabled services that support agent building, governance, and deployment.
He emphasizes the flexibility and openness of Google’s platform, allowing developers to use MCP alongside other tools, and notes the importance of infrastructure, security, and governance in scaling agentic applications.
Bob then details the security and governance features built into Google’s MCP servers, such as authentication, fine-grained access control, AI guardrails, and logging, as well as the use of Envoy proxies to manage and secure agent protocol traffic.
The session concludes with an invitation to further discussions and learning opportunities about building secure, scalable, and governed agentic systems using MCP within Google’s ecosystem.
# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Google uses MCP extensively across many teams and products.                                                                                                     |
|   2 | Presentation covers a broad overview of Google’s agent platform and infrastructure.                                                                             |
|   3 | Google Cloud AI provides a high-level application agent platform, leveraging extensive infrastructure, tools, and research from teams like DeepMind.            |
|   4 | Platform supports building, scaling, governing, and optimizing agents, using specialized services and tools.                                                    |
|   5 | ADK (Agent Development Kit) is open source, maintained by Google, and used internally by hundreds of teams for agentic products.                                |
|   6 | MCP support was included in ADK from day one.                                                                                                                   |
|   7 | Developers can wire MCP servers into their IDEs and agents for experimentation and production.                                                                  |
|   8 | Gemini Enterprise is an application layer for deploying agents, supporting governance, administration, and integration of Google, user, and third-party agents. |
|   9 | Gemini Enterprise for Customer Experience and Agent Studio also use ADK and MCP.                                                                                |
|  10 | MCP toolbox for databases enables easy interaction and templated queries with various databases.                                                                |
|  11 | Gemini CLI is widely used for agent development and is facilitated through MCP.                                                                                 |
|  12 | Chrome team is developing web MCP to extend browser capabilities via MCP as a bridge.                                                                           |
|  13 | A2UI is a declarative generative UI spec, with experiments to facilitate ATUI over MCP.                                                                         |
|  14 | Many Google products now natively expose hosted MCP servers, deployable via Cloud Run, GKE, or Compute Engine.                                                  |
|  15 | Remote MCP servers are available as HTTP endpoints for Google services, supporting OAuth authentication and access control.                                     |
|  16 | Fine-grained access control and AI security guardrails (e.g., Model Armor) are integrated, with support for third-party security solutions.                     |
|  17 | Vortex AI provides a tools registry for governance and discovery of MCP tools.                                                                                  |
|  18 | Security and governance include authentication, authorization, human-in-the-loop for sensitive actions, auditing, and logging.                                  |
|  19 | Envoy proxy is extended to support MCP and agent protocols, enabling policy enforcement and security at the protocol                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jCJ3LfqyHy4)