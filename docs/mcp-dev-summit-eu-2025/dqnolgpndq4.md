---
layout: default
title: "[Session] MCP Registry: The Path To (De-)Centralizing Discovery"
nav_order: 10
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  The video discusses the MCP registry, emphasizing its role in enabling
  decentralized discovery rather than centralizing all MCP server information. Tatis
  and Toby, two of the four maintainers, explain that the registry is a community-led,
  o...
resource: https://www.youtube.com/watch?v=dQnolGPNdQ4
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

The video discusses the MCP registry, emphasizing its role in enabling decentralized discovery rather than centralizing all MCP server information.
Tatis and Toby, two of the four maintainers, explain that the registry is a community-led, open-source REST API project, with contributions from many individuals and organizations.
The core innovation is the standardized server.json file, which provides a consistent way to define server identity, capabilities, location, and configuration, simplifying publication and integration for both server maintainers and MCP client developers.
The architecture supports subregistries, allowing different organizations or products to curate and augment the upstream data for their specific needs, fostering a flexible ecosystem.
A live demo illustrates how publishing a server via CI/CD or command-line tools propagates updates through the registry and into subregistries, streamlining server discovery and configuration across the MCP landscape.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The MCP registry aims to empower decentralized discovery rather than full centralization.                                        |
|   2 | The registry is maintained by a community-led group, not a single company.                                                       |
|   3 | The REST API for MCP servers is open-source and available at registry.modelontextprotocol.io.                                    |
|   4 | There is currently no official UI; community-built UIs may exist.                                                                |
|   5 | A live preview of the registry launched on September 8, with ongoing improvements and breaking changes.                          |
|   6 | The API shape is expected to be mostly frozen within a week, enabling more stable production use.                                |
|   7 | General availability launch will focus on stability and backwards compatibility.                                                 |
|   8 | The registry has 45 contributors, with notable contributions from Adam (Redthropic) and Roto (Stacklo).                          |
|   9 | Server developers publish MCP server information to the registry, typically via CI/CD.                                           |
|  10 | Subregistries can be built on top of the upstream registry, allowing for different augmentations and views.                      |
|  11 | MCP clients consume data from subregistries to surface and install MCP servers.                                                  |
|  12 | Enterprises may use private subregistries with additional governance and security features.                                      |
|  13 | The server.json file is a new standard for defining MCP servers, containing identity, capabilities, location, and configuration. |
|  14 | Identity is based on name and version, using reverse DNS for trust.                                                              |
|  15 | Capabilities include free-form descriptions and implied features.                                                                |
|  16 | Location specifies where to find the server (package registry or URL).                                                           |
|  17 | Configuration details CLI flags, environment variables, query parameters, and headers.                                           |
|  18 | Subregistries allow for tailored discovery and selection of MCP servers for different industries and products.                   |
|  19 | Publishing to the registry enables automatic propagation of updates to all subregistries.                                        |
|  20 | MCP clients benefit from a structured source of truth for server configuration and discovery.                                    |
|  21 | A command-line tool exists for creating and publishing server.json files.                                                        |
|  22 | Subregistries can enhance data with platform-specific information.                                                               |
|  23 | Contributions are                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dQnolGPNdQ4)
