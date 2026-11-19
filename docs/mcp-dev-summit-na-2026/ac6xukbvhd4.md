---
layout: default
title: The MCP Gateway Pattern Big Enterprises Are Quietly Adopting
nav_order: 77
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Jake Wilson, a partner in PwC’s analytics practice, presented a real-world example of how Model Context Protocol (MCP) and agent skills orchestration can streamline enterprise procurement."
resource: "https://www.youtube.com/watch?v=aC6xuKBVHD4"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Jake Wilson, a partner in PwC’s analytics practice, presented a real-world example of how Model Context Protocol (MCP) and agent skills orchestration can streamline enterprise procurement.
He described a solution for manufacturing and tech companies where diverse buyers, such as those in robotics or AI research, often struggle to navigate complex legacy ERP and procurement systems.
To address this, PwC developed a GPT app that interfaces with an MCP orchestrator, which uses agent skills to classify requests as either direct or indirect procurement.
The orchestrator then routes these requests to the appropriate backend systems, handling complex data validation and supplier optimization while presenting a simplified user interface.
Wilson also highlighted the importance of MCP gateways for enhancing security, particularly when integrating with systems that rely on less secure API keys, allowing for fine-grained control over tool invocation and user identity management.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jake Wilson, a partner in PwC's analytics practice, presented a real-world example of using AI to streamline enterprise procurement.                                 |
|   2 | The solution addresses the challenge of diverse buyers in research and robotics divisions who avoid using complex legacy ERP and procurement systems.                |
|   3 | The architecture utilizes a GPT app that communicates with an MCP orchestrator to handle user requests for items like GPUs or robotic arms.                          |
|   4 | The MCP orchestrator employs agent skills, following a format published by Anthropic, to classify requests as either direct or indirect procurement.                 |
|   5 | Direct procurement involves materials like robotics arms and GPUs, while indirect procurement covers items such as office furniture.                                 |
|   6 | The system simplifies the user experience by allowing buyers to make requests through a single interface while the backend handles complex orchestration.            |
|   7 | The MCP orchestrator determines if sufficient information is available to trigger downstream calls to specific direct or indirect MCP servers.                       |
|   8 | In the direct procurement flow, a dedicated agent validates supplier details and can identify more optimal suppliers based on timelines and requirements.            |
|   9 | The GPT app uses a standalone React application for its user interface, which loads structured content returned from the backend systems.                            |
|  10 | The MCP orchestrator manages the routing of data back to the GPT app, specifying which UI resources to load based on the agent's response.                           |
|  11 | Security challenges arise when backend systems have different authentication methods, such as OAuth versus less secure API keys.                                     |
|  12 | MCP gateways are recommended to add a layer of security and fine-grained control over who can invoke specific MCP servers and tools.                                 |
|  13 | These gateways allow for policy definitions that restrict tool invocation in specific scenarios, enhancing security for sensitive operations.                        |
|  14 | The presentation highlights a pattern where an MCP orchestrates agents that invoke other MCP servers, creating a layered integration approach.                       |
|  15 | The agent skill standard uses Markdown files to define skills, functioning similarly to tool calling by exposing a list of names and descriptions.                   |
|  16 | This approach enables the MCP orchestrator to enumerate and invoke the correct skills, which in turn trigger agents and further MCP interactions.                    |
|  17 | The overall goal is to facilitate enterprise transformation by simplifying procurement for specialized teams without requiring them to navigate legacy applications. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/aC6xuKBVHD4/hqdefault.jpg)](https://www.youtube.com/watch?v=aC6xuKBVHD4)

[Watch on YouTube](https://www.youtube.com/watch?v=aC6xuKBVHD4)
