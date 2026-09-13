---
layout: default
title: "[Session] Hidden powers of MCP Gateways: Solving OAuth and Analytics Challenges"
nav_order: 34
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Philip Mlinsy, co-founder of Glass Cube, shares the story behind building
  HyperMCP, an open-source gateway for MCP servers that his team initially did not
  intend to create. The talk outlines the main challenges users face with MCP servers—d...
resource: https://www.youtube.com/watch?v=wIbQp0rJj78
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Philip Mlinsy, co-founder of Glass Cube, shares the story behind building HyperMCP, an open-source gateway for MCP servers that his team initially did not intend to create.
The talk outlines the main challenges users face with MCP servers—difficulty in installation and configuration, lack of analytics and visibility into GCP messages, and complex authentication requirements.
HyperMCP addresses these issues by providing a gateway that simplifies setup, adds authentication and analytics features, and acts as a protocol translator, similar to how Cloudflare protects and manages websites.
Through a live demo, Philip demonstrates how HyperMCP can be easily deployed to add authentication and analytics to MCP servers, and explains the technical approach to integrating prompts and history analytics by modifying tool responses.
He concludes by discussing future plans for deeper IDP integration, enhanced blocking rules for organizational control, and ongoing adaptation to evolving protocol standards, inviting interested users to join the waitlist for HyperMCP.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk discusses the hidden powers of the MCP gateway, specifically Hyper MCP, which was built to solve problems encountered with MCP servers.                                                |
|   2 | Glass Cube, the company behind Hyper MCP, was founded three years ago in Vienna, Austria, and focuses on open-source infrastructure.                                                            |
|   3 | Initial work was in Kubernetes and on-premise deployments, leading to the creation of the open-source tool Dister.                                                                              |
|   4 | MCP servers were found to be difficult to install and use, with common issues including authentication, session management, security, and lack of analytics/observability.                      |
|   5 | Hyper MCP was developed as a gateway to abstract complexity, add authentication, and provide analytics for MCP servers.                                                                         |
|   6 | The gateway can be deployed in front of any MCP server, similar to how Cloudflare sits in front of websites.                                                                                    |
|   7 | Hyper MCP simplifies connecting to MCP servers by detecting client needs and providing appropriate instructions or responses.                                                                   |
|   8 | The platform allows enabling/disabling telemetry and authentication, and provides detailed analytics on prompts, tool responses, and raw GCP messages.                                          |
|   9 | Authentication is implemented via a gateway using DEX as a federated IDP, supporting dynamic client registration and OAuth flows.                                                               |
|  10 | No existing commercial or open-source authentication provider fully supports MCP authentication out of the box.                                                                                 |
|  11 | Hyper MCP enables easy integration of authentication and analytics for MCP servers, requiring minimal configuration.                                                                            |
|  12 | Real-world use case: Context Forge integrated Hyper MCP to add authentication and dynamic client registration for virtual MCP servers.                                                          |
|  13 | Analytics are captured at the gateway layer, providing visibility into all events, including failures, and capturing prompts and tool history by injecting parameters into tool list responses. |
|  14 | The gateway approach is protocol-agnostic and captures more comprehensive metrics than application-layer SDKs.                                                                                  |
|  15 | Future plans include onboarding more users, decoupling from DEX, integrating directly with enterprise I                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wIbQp0rJj78)
