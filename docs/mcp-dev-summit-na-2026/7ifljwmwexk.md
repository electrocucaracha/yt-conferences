---
layout: default
title:
  "From One MCP Server To an Ecosystem: When MCP Stops Being a Server and Becomes
  a Pla... Vaibhav Tuple"
nav_order: 29
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this session, the speaker from Equinix discusses the journey and challenges
  of scaling MCP servers within a large digital infrastructure company. Initially,
  Equinix started with a single MCP server to automate infrastructure tasks like p...
resource: https://www.youtube.com/watch?v=7iFLJwMWEXk
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

In this session, the speaker from Equinix discusses the journey and challenges of scaling MCP servers within a large digital infrastructure company.
Initially, Equinix started with a single MCP server to automate infrastructure tasks like provisioning connections between clouds, leveraging existing APIs and tools.
As adoption grew, multiple teams wanted to onboard their APIs, leading to governance, domain boundary, and coordination challenges.
The speaker emphasizes the importance of designing domain-first, avoiding "mega" MCP servers, and using tool tags and skills to manage context explosion and agent workflows.
Security, dynamic discovery, and observability are highlighted as critical, with lessons learned around authorization, tool naming, and workflow determinism.
The talk concludes with key takeaways: confining domains, using tags and skills to manage scale and context, and designing MCP servers with ecosystem growth in mind, while addressing questions about breaking up large servers, determinism, agent-to-agent communication, and ROI considerations.

# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on scaling MCP server ecosystems, not building MCP servers.                                               |
|   2 | Presenter is principal engineer at Equinix, leading fabric intelligence initiative.                                       |
|   3 | Equinix operates 280+ data centers, 500,000+ interconnections, thousands of partners.                                     |
|   4 | MCP journey began April 2025; first server for fabric interconnection.                                                    |
|   5 | Initial use case: agents provision connections, view inventory, connect clouds/data centers.                              |
|   6 | Built on existing APIs; started with 5-10 tools.                                                                          |
|   7 | As more teams wanted to expose APIs as MCP tools, governance and coordination challenges arose.                           |
|   8 | Currently, 4-5 public MCP servers, 80+ tools on fabric server, 150+ tools on others, plus internal servers.               |
|   9 | Scaling from one to multiple MCP servers introduces coordination, governance, and domain boundary issues.                 |
|  10 | Key design patterns:                                                                                                      |
|  11 | Design domains first, not just tools.                                                                                     |
|  12 | Avoid creating a mega MCP server; define domain boundaries early.                                                         |
|  13 | Design APIs for agent reasoning and intent-based queries.                                                                 |
|  14 | No cross-server calls at runtime; agent acts as orchestration layer.                                                      |
|  15 | Use domain namespace-based tool naming to avoid confusion.                                                                |
|  16 | Context explosion managed by combining tool tags and skills; only relevant tools are exposed to agents per workflow.      |
|  17 | Security: MCP servers treated as secure API endpoints; OAuth, client ID metadata, DCR for onboarding and authorization.   |
|  18 | Tool tags used for scope-based authorization and autonomy control.                                                        |
|  19 | Dynamic discovery implemented via internal MCP registry; no hardcoded URLs.                                               |
|  20 | Tools are reusable for both internal and external agents; no duplicate work.                                              |
|  21 | Observability is critical: monitor tool call accuracy, failures, and rate limiting.                                       |
|  22 | Operational lessons: session stickiness, stateful MCP for elicitation, human-in-the-loop for infrastructure changes.      |
|  23 | Key takeaways: bounded domains, tags and skills for context control, OAuth for security, ecosystem thinking from day one. |
|  24 | Breaking up mega MCP servers requires customer/agent workflow-centric domain define Ratings (1-5): 3                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7iFLJwMWEXk)
