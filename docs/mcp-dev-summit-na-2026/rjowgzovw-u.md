---
type: Video Note
title: "When MCP Becomes a Product - Gautam Baghel, HashiCorp & Roy Derks, IBM"
description: "In this session, the speakers from IBM discussed their experiences transitioning MCP (Model Control Plane) servers from internal demos to production-ready products. They highlighted the evolution of MCP from a niche advantage to an industry..."
resource: https://www.youtube.com/watch?v=RjOWGzovw_U
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, the speakers from IBM discussed their experiences transitioning MCP (Model Control Plane) servers from internal demos to production-ready products.
They highlighted the evolution of MCP from a niche advantage to an industry expectation, emphasizing the challenges of scaling from prototypes—often built by passionate individuals—to robust, customer-facing solutions.
Key topics included the importance of designing tools for specific use cases to avoid context window bloat, strategies for tool discovery and planning, and the need for consistent architecture and robust API testing as MCP servers mature.
They also stressed the significance of telemetry, evaluation, and thoughtful release strategies, noting that productizing MCP servers requires both technical rigor and adaptability to rapid changes in AI and MCP specifications.
The session concluded with practical advice on maintaining consistency, enabling telemetry, and preparing for general availability, while inviting further questions from the audience.
# Main Points

|   # | Main point                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------ |
|   1 | Session focused on transitioning MCP from a demo project to a product.                                       |
|   2 | MCP servers have shifted from a competitive advantage to an expected product feature.                        |
|   3 | Early MCP servers were prototypes, often stitched together with minimal resources.                           |
|   4 | Building an MCP server for internal use is different from deploying in production for customers.             |
|   5 | Production deployment requires collaboration with legal, security, and other organizational teams.           |
|   6 | Early MCP development involved experimentation and manual testing.                                           |
|   7 | Reading the spec is helpful, but building a simple MCP server is recommended for understanding.              |
|   8 | Experimenting with MCP features like elicitation and sampling is encouraged during prototyping.              |
|   9 | Initial MCP servers often wrapped existing APIs and SDKs with minimal changes.                               |
|  10 | Tool context bloating is a challenge; too many tools or large descriptions can overwhelm the context window. |
|  11 | Tool descriptions are important for model effectiveness.                                                     |
|  12 | Multi-step tool chaining can be more effective than providing many generic tools.                            |
|  13 | Designing tools for specific use cases or outcomes is recommended.                                           |
|  14 | Layered tool design involves discovery, planning, and execution phases.                                      |
|  15 | OpenAPI to MCP conversion can lead to too many tools; context management is crucial.                         |
|  16 | The landscape is evolving rapidly; engineers need dedicated time to keep up with changes.                    |
|  17 | Tool search and dynamic tool enabling help manage context bloating.                                          |
|  18 | Not every spec change is important for every MCP product.                                                    |
|  19 | Solid understanding of architecture is necessary as MCP matures.                                             |
|  20 | Robust API testing strategy is essential for production MCP servers.                                         |
|  21 | Consistent folder structures and programming languages matter in enterprise environments.                    |
|  22 | Implement tools first; advanced features may lag in client support.                                          |
|  23 | Enable telemetry to monitor usage and errors.                                                                |
|  24 | Evaluation (eval) is critical for MCP server quality.                                                        |
|  25 | Release strategy, cadence, and support versions must be defined.                                             |
|  26 | Removing tools after GA is di                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RjOWGzovw_U)