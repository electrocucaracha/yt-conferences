---
layout: default
title:
  "Rules Are Not Suggestions: A History of MCP Non-Compliance - Sterling Dreyer,
  Arcade.dev"
nav_order: 78
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Serling, a founding engineer at Arcade, discussed his experience integrating
  MCP into their product, highlighting unexpected challenges due to inconsistencies
  and rapid changes in the MCP ecosystem. He described how Arcade manages OAuth and...
resource: https://www.youtube.com/watch?v=EcgYMY4eUTo
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

Serling, a founding engineer at Arcade, discussed his experience integrating MCP into their product, highlighting unexpected challenges due to inconsistencies and rapid changes in the MCP ecosystem.
He described how Arcade manages OAuth and governance for agentic tools, provides evaluation suites, and hosts MCP servers.
During integration, Serling encountered issues with server and client compliance, prompting the development of internal tools—MCP Debugger for live server testing and Toolbench for static code analysis—which revealed that 94% of tested servers failed at least one compliance check.
He emphasized that while many servers function, non-compliance can introduce security risks and reliance on fallbacks, often due to incomplete framework support or rapid spec evolution.
Serling advocated for better promotion and expansion of MCP’s conformance testing, improved SDKs and frameworks to enforce compliance, and stricter registry standards, all aimed at lowering barriers for users and ensuring reliable interoperability.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Serling is a founding engineer at Arcade, working on core product, infrastructure, and MCP integration.                                                                             |
|   2 | Arcade manages OAuth and governance for Agentic tools, provides evaluation suite and hosting for MCP servers.                                                                       |
|   3 | Integrating MCP was more complex and time-consuming than expected.                                                                                                                  |
|   4 | Initial integration issues included inconsistent server/client compatibility and unclear error sources.                                                                             |
|   5 | Arcade analyzed the MCP ecosystem, testing both production and nonproduction servers from public registries and GitHub.                                                             |
|   6 | Two internal tools were built: MCP Debugger (live server tests, spec compliance, remediation links) and Toolbench (static code analysis, spec compliance, functionality, metadata). |
|   7 | 94% of servers tested failed some kind of compliance test; only 6% fully complied.                                                                                                  |
|   8 | 85% of servers failed two or more checks; 9% failed one check.                                                                                                                      |
|   9 | Common issues: missing origin header validation, missing www-authenticate header.                                                                                                   |
|  10 | Spec versions were considered in compliance checks to avoid penalizing older servers for new requirements.                                                                          |
|  11 | MCP spec evolves rapidly, with large changes in each release, making version support challenging.                                                                                   |
|  12 | Lack of comprehensive conformance testing tools; existing conformance suite is limited and not widely used.                                                                         |
|  13 | 19% of tools scanned had input schema issues, often due to SDK bugs or lack of enforcement.                                                                                         |
|  14 | API keys are not part of the MCP spec; OAuth is more secure and supported in v2, but API keys are still widely used for simplicity.                                                 |
|  15 | Most developers use SDKs, but frameworks often require manual implementation of compliance details.                                                                                 |
|  16 | Suggested solutions: frameworks should enforce compliance, guided setups, templates, registry gatekeeping, client-side rejection for non-compliance.                                |
|  17 | Goal: lower barriers for users, make developer experience easier, and ensure reliable standards.                                                                                    |
|  18 | MCP Debugger and Toolbench are free to use, no account required.                                                                                                                    |
|  19 | Issues discussed were discovered during Arcade's MCP integration, not foundational to Arcade's creati                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=EcgYMY4eUTo)
