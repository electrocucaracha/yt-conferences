---
type: Video Note
title: "Sponsored Session: The Self-Improving MCP Server: Agents in a Live Development Loop - Enrico Toniato"
description: "The speaker discusses the challenges of developing and maintaining MCP servers, emphasizing that while building these servers has become easier due to mature SDKs and frameworks, testing and ensuring consistent behavior across different cli..."
resource: https://www.youtube.com/watch?v=XMPoyrgClxE
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the challenges of developing and maintaining MCP servers, emphasizing that while building these servers has become easier due to mature SDKs and frameworks, testing and ensuring consistent behavior across different clients and models remains a significant pain point.
Issues such as lack of monitoring, inconsistent user flows, and varying client interfaces make it difficult to iterate and maintain reliable MCP servers, especially as clients and AI models frequently update.
To address this, the speaker introduces a self-improving MCP server approach, where the agent itself can autonomously test and refine the server during development, CI/CD, and production monitoring stages, using open-source tools like MCPUs and an integrated inspector for live debugging and analytics.
This approach aims to save developers time, improve reliability, and provide a better experience for both agents and end users.
The speaker also highlights the open-source nature of their tools, ease of deployment, and support for developers, inviting attendees to try the platform and visit their booth for further engagement.
# Main Points

|   # | Main point                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------- |
|   1 | Main pain point in MCP server development is testing and ensuring correct behavior, not building.                   |
|   2 | SDKs and frameworks for MCP servers are mature; building is fast, but testing and monitoring are lacking.           |
|   3 | After deployment, MCP servers often lack monitoring and analytics, making iteration difficult.                      |
|   4 | Client-side issues are common, especially with rapidly changing clients and AI features.                            |
|   5 | Inconsistent flows across different models and clients due to varying capabilities.                                 |
|   6 | Complex MCP servers with multiple tools face challenges in maintaining consistent user flows.                       |
|   7 | Different clients (e.g., Chat, Cloud, Cursor, VS Code) have varying interfaces, increasing manual testing workload. |
|   8 | Even top MCP servers in the OpenAI marketplace face reliability and consistency issues.                             |
|   9 | Proposal: MCP servers should be able to test and improve themselves automatically.                                  |
|  10 | Agents (not humans) are the primary users of MCP servers, making agent-driven testing logical.                      |
|  11 | Three levels of testing: protocol (functionality), behavior (flow consistency), and visual/UI (widgets).            |
|  12 | MCP apps allow servers to return UI widgets, increasing testing surface.                                            |
|  13 | Testing should occur during development, CI/CD, and continuous monitoring stages.                                   |
|  14 | Inspector tool provides live feedback and autonomous testing during development.                                    |
|  15 | GitHub app enables automatic behavioral testing and improvement suggestions in CI/CD pipelines.                     |
|  16 | Continuous monitoring can be scheduled to test MCP servers across clients and models.                               |
|  17 | Open source SDK (MCPUs) and inspector tool available; supports live debugging and HMR.                              |
|  18 | Easy setup with "npx create-mcpus-app" for boilerplate MCP server and app.                                          |
|  19 | Skill available for cloud or cursor to automate server building.                                                    |
|  20 | Free deployment, analytics, and observability for solo developers on Manif Cloud.                                   |
|  21 | No transcript storage in open source version; hosted version stores conversations for resuming work.                |
|  22 | Dashboard allows specifying test flows and automated checks for MCP servers                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XMPoyrgClxE)