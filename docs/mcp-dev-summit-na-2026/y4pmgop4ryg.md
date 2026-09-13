---
layout: default
title: Distributing MCP Servers With OCI To Power Agent Skills - Bobby House, Docker
nav_order: 17
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Bobby House from Docker discusses recurring themes from
  recent MCP (Modular Component Platform) talks, particularly the integration of agent
  skills with MCP servers and the use of gateway products. He explains the challenges
  o...
resource: https://www.youtube.com/watch?v=Y4pmgoP4ryg
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Bobby House from Docker discusses recurring themes from recent MCP (Modular Component Platform) talks, particularly the integration of agent skills with MCP servers and the use of gateway products.
He explains the challenges of managing dependencies between agent skills and MCP servers, emphasizing the need for a single, immutable, and configurable dependency that can be reliably referenced and reused.
House demonstrates a pattern where agent skills declare their MCP server dependencies as OCI artifacts, which are then resolved, configured, and loaded dynamically, improving reproducibility and decoupling skill development from server implementation.
He highlights the benefits of this approach, such as leveraging the broader MCP ecosystem, progressive disclosure of dependencies, and improved user experience through gateways, while also noting current limitations like lifecycle management and update propagation.
The session concludes with a discussion on potential improvements and the importance of predictable, version-pinned dependencies for enterprise use cases.

# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | Recurring themes at MCP talks include using agent skills with MCP servers and the importance of gateways.                |
|   2 | Multiple vendors and companies (e.g., Uber, Docker) have developed gateway products for MCP servers.                     |
|   3 | At Docker, focus is on distributing MCP servers along with agent skills as dependencies.                                 |
|   4 | Current ad hoc dependency management can be fragile; skills may fail if required tools are missing.                      |
|   5 | Running evals on skills in MCP servers is common, but changes in server implementation/configuration can affect results. |
|   6 | MCP server dependencies include both the server and its configuration.                                                   |
|   7 | Bundling MCP servers directly with skills can lead to maintenance burdens and forking issues.                            |
|   8 | Ideal dependency management should be: single, addressable, immutable (using a SHA), configurable, and decoupled.        |
|   9 | Existing ecosystem files like MCP.json and server.json are not fully suitable for this dependency pattern.               |
|  10 | Proposed solution: package MCP server dependencies as OCI artifacts, referenced by SHA, and pin them in the skill.       |
|  11 | Skill authors can define some configuration; users can provide additional configuration at runtime.                      |
|  12 | Demo: skill builder finds and pins OCI artifact dependencies, pushes to DockerHub, and prompts for configuration.        |
|  13 | OCI registries provide a convenient way to package and distribute MCP server dependencies.                               |
|  14 | When running a skill, only referenced MCP servers are pulled in, enabling progressive disclosure.                        |
|  15 | Current pattern requires restarting Claude to recognize new dependencies and lacks lifecycle management for MCP servers. |
|  16 | Improved pattern: use a gateway that loads OCI dependencies, spins up servers in containers, and proxies communication.  |
|  17 | Gateway approach avoids persisting unnecessary servers and improves user experience.                                     |
|  18 | Docker’s MCP gateway implements this pattern and is open source.                                                         |
|  19 | Security and reproducibility are enhanced by pinning dependencies with immutable digests.                                |
|  20 | Discussion on distributing agent skills and MCP servers as                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Y4pmgoP4ryg)
