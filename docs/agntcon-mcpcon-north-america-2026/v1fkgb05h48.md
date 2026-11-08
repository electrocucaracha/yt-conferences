---
layout: default
title: "LLMs Are a Commodity. Choice and Control Aren't - Matt Meeboer, Safe Software"
nav_order: 86
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Matt Mayborn from Safe Software presents a solution for the "hard 20%" of data integration challenges, where MCP standardizes tool discovery but fails to address governed execution for sensitive, o...'
resource: "https://www.youtube.com/watch?v=v1FKGB05h48"
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

Matt Mayborn from Safe Software presents a solution for the "hard 20%" of data integration challenges, where MCP standardizes tool discovery but fails to address governed execution for sensitive, on-premise, or proprietary data.
He argues that while MCP easily connects to common sources like Slack or Google Docs, it struggles with legacy databases, geospatial formats, and regulated data that cannot leave the building.
Safe Software’s FME platform, with over 30 years of experience in spatial data integration, serves as the foundational layer that ingests, transforms, and orchestrates complex data from over 500 formats, exposing only controlled, generalized outputs to AI via MCP.
In a live demonstration using Microsoft Co-Pilot, FME securely queried crime data by generalizing precise locations to neighborhood blocks and stripping sensitive victim details, ensuring that only necessary insights were shared while keeping raw data and credentials within the secure execution plane.
The presentation concludes with three key rules for secure AI integration: expose tools rather than raw systems, keep authority and execution close to the data, and define clear schemas and contracts to maintain predictable and governed interactions between AI agents and enterprise data.

# Main Points

|   # | Main point                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , particularly for data that cannot leave the building.                                                                                                                                                                 |
|   2 | "easy 80%" of MCP integrations (e.g., Slack, Google Docs) is largely solved, but the "hard 20%" involves legacy databases, geospatial/GIS formats, CAD/BIM models, real-time data, on-prem systems, and regulated data. |
|   3 | ’s FME platform has spent over 30 years solving the "hard data" problem, focusing on representation, locality, computation, and authority for data that cannot or should not move.                                      |
|   4 | , offering significant breadth in spatial data (vector, raster, 3D/BIM) ingestion, transformation, and validation.                                                                                                      |
|   5 | (authoring), FME Flow (serving MCP servers and web apps), and FME Realize (augmented reality experiences).                                                                                                              |
|   6 | , while MCP serves only as the exposure point, allowing existing workflows to be reused as MCP tools for any AI client.                                                                                                 |
|   7 | , air-gapped, in the cloud, or in hybrid configurations, ensuring execution stays close to the data.                                                                                                                    |
|   8 | (credentials, system details) hidden from AI; only narrow request parameters and bounded, generalized results cross the boundary via MCP.                                                                               |
|   9 | , stripping sensitive attributes, and serving results as maps or PDF reports via Microsoft Teams.                                                                                                                       |
|  10 | "hard 20%" include exposing tools rather than raw systems, keeping authority and execution close to the data, and defining clear schemas and contracts for AI interactions.                                             |
|  11 | ; developers must explicitly define tools, and FME maintains detailed audit logs of tool calls and returned data.                                                                                                       |
|  12 | , even if data naming is inconsistent.                                                                                                                                                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/v1FKGB05h48/hqdefault.jpg)]("https://www.youtube.com/watch?v=v1FKGB05h48")

[Watch on YouTube](https://www.youtube.com/watch?v=v1FKGB05h48)
