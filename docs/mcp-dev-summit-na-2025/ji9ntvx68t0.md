---
layout: default
title:
  "MCP Registry: Designing For Server Discovery Tadas A. (PulseMCP) Alex H.(Block),
  and Toby P.(GitHub)"
nav_order: 2
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  The video introduces the official MCP server registry, aiming to consolidate
  the fragmented ecosystem of MCP server registries by providing a centralized, community-driven
  solution. The presenters, members of the steering committee from var...
resource: https://www.youtube.com/watch?v=jI9NTVX68T0
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video introduces the official MCP server registry, aiming to consolidate the fragmented ecosystem of MCP server registries by providing a centralized, community-driven solution.
The presenters, members of the steering committee from various early MCP projects, explain that the registry addresses three main problems: incomplete server listings due to unreliable web scraping, the burden on server maintainers to update multiple registries, and the lack of a unified source for structured installation instructions.
The official registry will use a standardized server.json file containing metadata, source code references, optional remote URLs, and structured installation instructions, with a command-line tool to facilitate publishing.
Advanced features like source code storage and sophisticated search or ranking are intentionally left out, with the expectation that downstream client apps and third-party registries will build on top of the core registry and enrich the data as needed.
The demo showcases the publishing process and how different clients can leverage the registry and add their own metadata, emphasizing the importance of community feedback and collaboration in shaping the registry’s development.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Announcement of the official MCP server registry launch.                                                                                        |
|   2 | Aim to consolidate fragmented MCP server registries into a central, community-driven registry.                                                  |
|   3 | Main focus: define what is in and out of scope for the official registry.                                                                       |
|   4 | Steering committee includes members from Pulse MCP, Block (Goose), and GitHub.                                                                  |
|   5 | Community contributions highlighted, especially from Avan (GitHub), Connor, and Sandy (Visual Studio Code).                                     |
|   6 | Problems being solved:                                                                                                                          |
|   7 | Third-party registries lack comprehensive server lists due to reliance on web scrapers.                                                         |
|   8 | Fragmented data and incomplete coverage of MCP servers.                                                                                         |
|   9 | Server maintainers must update multiple registries separately, increasing fragmentation.                                                        |
|  10 | Client apps lack a single source of truth for installation instructions, leading to unreliable inference from readmes.                          |
|  11 | Problems not being solved:                                                                                                                      |
|  12 | Source code storage; will reference existing package registries (npm, PyPI, etc.).                                                              |
|  13 | Advanced search, filtering, and ranking; delegated to downstream MCP client marketplaces.                                                       |
|  14 | Solution:                                                                                                                                       |
|  15 | Introduction of a server.json file containing metadata, source code references, optional remote URLs, and structured installation instructions. |
|  16 | Command-line tool for publishing server.json to the registry, similar to npm publish.                                                           |
|  17 | Expectation of an ETL (Extract, Transform, Load) layer between the registry and MCP clients for filtering and enrichment.                       |
|  18 | Downstream consumers (e.g., Visual Studio Code, Smithery, Raycast) can add proprietary data and metrics.                                        |
|  19 | Open questions for community feedback:                                                                                                          |
|  20 | Does server.json capture all necessary data for MCP client apps?                                                                                |
|  21 | Can the API shape be reused in a federated manner by third-party marketplaces?                                                                  |
|  22 | Demo showcased:                                                                                                                                 |
|  23 | Local registry setup with Docker Compose.                                                                                                       |
|  24 | Publishing a server.json using OAuth authentication.                                                                                            |
|  25 | ETL marketplace for Goose and integration with GitHub MCP server.                                                                               |
|  26 | Installation and usage in both Goose and Visual Studio Code clients, each adding their own metadata layers.                                     |
|  27 | Emphasis on ongoing community inv                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jI9NTVX68T0)
