---
layout: default
title:
  "Skills Vs. MCP Vs. Code Mode: Cutting Through the Hype (and the Rage) - Nikolay
  Rodionov, Alpic"
nav_order: 83
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Nikolai Roda from Alpic discusses recent debates around MCP (Model Capability
  Protocol), skills, code mode, and CLI, clarifying their roles and how they interact.
  He explains that code mode, introduced by Cloudflare, optimizes how MCP tools...
resource: https://www.youtube.com/watch?v=DoedEqfI6Hg
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

Nikolai Roda from Alpic discusses recent debates around MCP (Model Capability Protocol), skills, code mode, and CLI, clarifying their roles and how they interact.
He explains that code mode, introduced by Cloudflare, optimizes how MCP tools are called by reducing context overload but does not replace MCP, as it is built on the same protocol and mainly helps with complex workflows involving many tools.
Skills, introduced by Anthropic, are reusable prompts stored in markdown files that guide models through tasks and can reference scripts or assets, excelling in progressive disclosure and multi-step workflows, but they do not provide tools themselves and are best suited for coding agents with terminal access.
CLI tools are efficient and composable but lack accessibility and standardization for non-technical users.
Roda concludes that MCP is not dead; rather, MCP, skills, and CLI each serve different purposes and are often complementary, with ongoing efforts to integrate skills more closely with MCP for enhanced usability and automation.

# Main Points

|   # | Main point                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nikolai Roda from Alpic presents on recent Twitter debates about MCP, skills, code mode, and CLA.                                                                                         |
|   2 | Code mode was released by Cloudflare to address MCP context overload by allowing execution of scripts calling MCP tools in a sandbox.                                                     |
|   3 | MCP clients initially had to load all tool metadata, leading to large context windows.                                                                                                    |
|   4 | Code mode reduces context pollution by providing a fixed, small set of tools and enabling complex workflows.                                                                              |
|   5 | Drawbacks of code mode: still requires some tokens, needs sandbox access (often only available server-side), kills interactivity, and may decrease task completion rate if not optimized. |
|   6 | Code mode is best for servers with many tools and complex workflows; not necessary for servers with few tools.                                                                            |
|   7 | Code mode did not kill MCP; it is an optimization based on the MCP protocol.                                                                                                              |
|   8 | Antropic and OpenAI now implement client-side tool search, loading only tool names/descriptions at session start.                                                                         |
|   9 | Skills, introduced by Antropic, are reusable prompts stored in markdown files, sometimes including scripts, assets, and references to subskills.                                          |
|  10 | Skills support progressive disclosure, loading only necessary files when needed, making them context-efficient.                                                                           |
|  11 | Skills are easy to create/edit, good for multi-step workflows, but only provide instructions, not tools.                                                                                  |
|  12 | Skills are mainly used in coding agents due to access to terminals.                                                                                                                       |
|  13 | Skills were previously hard to share/install, but marketplaces are emerging.                                                                                                              |
|  14 | Skills did not kill MCP; they serve different purposes—MCP exposes capabilities, skills are recipes for using them.                                                                       |
|  15 | CLI tools are efficient, composable, and familiar to models, but lack standards, are not user-friendly for non-tech users, and lack control/audit features.                               |
|  16 | MCP is best for simple workflows and UI interactions; skills for reusable prompts/content; skills+MCP for complex workflows with external services; skills+CLI for local dev workflows.   |
|  17 | MCP is not dead; it remains healthy and accessible, especially for non-technical users.                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=DoedEqfI6Hg)
