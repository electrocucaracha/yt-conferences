---
type: Video Note
title: "Keynote: Using MCP for Skills Orchestration and Enterprise Integration - Jacob Wilson"
description: "Jake Wilson, a partner at PwC’s analytics practice, discusses how modern AI and orchestration tools are transforming enterprise procurement processes, particularly for organizations with complex needs like manufacturing and research divisio..."
resource: https://www.youtube.com/watch?v=30WU_6_wplc
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jake Wilson, a partner at PwC’s analytics practice, discusses how modern AI and orchestration tools are transforming enterprise procurement processes, particularly for organizations with complex needs like manufacturing and research divisions.
He describes a solution involving a GPT app integrated with an MCP (Multi-Channel Platform) orchestrator, which leverages agent skills standards to classify and route procurement requests—such as buying GPUs or robotics arms—between direct and indirect procurement systems.
This architecture simplifies the user experience by allowing buyers to make requests through a straightforward interface, while the orchestrator manages backend complexities, including intent classification, supplier validation, and secure system integration.
Wilson also highlights the importance of security and fine-grained access control, achieved through MCP gateways, and notes the broader industry trend toward standardized agent skills for orchestrating enterprise workflows.
Overall, the approach streamlines procurement, reduces friction for end users, and demonstrates a practical application of AI-driven orchestration in enterprise transformation.
# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker: Jake Wilson, partner in analytics at PwC, with background in software engineering and data science.                                   |
|   2 | Consults for AI companies and utility/energy clients building next-gen AI data centers.                                                        |
|   3 | Focus of talk: Improving procurement efficiency in enterprises using MCPs, skills orchestration, and integration with enterprise applications. |
|   4 | Enterprises face challenges with multiple buyers needing to procure items (e.g., GPUs, robotics arms) through complex ERP/procurement systems. |
|   5 | Developed a GPT app that works with an MCP orchestrator using the latest agent skills format (from Anthropic).                                 |
|   6 | MCP orchestrator classifies procurement requests as direct (e.g., robotics arms, GPUs) or indirect (e.g., office chairs).                      |
|   7 | System simplifies user experience by handling complex orchestration and integration with backend ERP and procurement systems.                  |
|   8 | Architecture:                                                                                                                                  |
|   9 | MCP app (standalone React application) interfaces with users.                                                                                  |
|  10 | GPT app makes MCP tool calls to orchestrator.                                                                                                  |
|  11 | Orchestrator classifies intent and routes requests to appropriate direct or indirect MCP servers.                                              |
|  12 | Direct procurement agent validates suppliers and can optimize supplier selection.                                                              |
|  13 | Data and confirmations are returned to the GPT app, which loads the correct UI resource and structured content.                                |
|  14 | Backend systems vary in security (OAuth vs. API key); MCP gateways can add security and fine-grained access control.                           |
|  15 | MCP gateways allow definition of policies to restrict tool/function invocation in specific scenarios.                                          |
|  16 | Pattern: MCP orchestrator invokes agents, which invoke other MCP servers, using the latest agent skills standard (skills in markdown files).   |
|  17 | Approach simplifies procurement for buyers across divisions, removing need to interact with legacy systems.                                    |
|  18 | Emphasizes real-world enterprise transformation using MCPs and agent skills orchestration.                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=30WU_6_wplc)