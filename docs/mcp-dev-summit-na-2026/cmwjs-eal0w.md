---
type: Video Note
title: "Sponsored Session: Who's Driving? Delegation and the Confused Deput... Vitor Balocco & Alvaro Inckot"
description: 'The speaker, a founding identity engineer at Run Layer, discusses the technical challenges of assigning responsibility and authority when AI agents act on behalf of users, focusing on the "confused deputy" problem where legitimate permissio...'
resource: https://www.youtube.com/watch?v=CmWJs_eAL0w
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a founding identity engineer at Run Layer, discusses the technical challenges of assigning responsibility and authority when AI agents act on behalf of users, focusing on the "confused deputy" problem where legitimate permissions are misused due to inadequate delegation and intent binding.
Using the valet key analogy, the talk highlights how current token-based authorization systems lack granularity, audit trails, and mechanisms to track delegation, leading to vulnerabilities such as prompt injection, tool confusion, sub-agent escalation, and session bleed.
The speaker explains that while standards like OAuth 2.1 and MCP acknowledge these issues, they do not fully address them, and emphasizes the need for explicit delegation, intent binding, permission intersection, and comprehensive auditing.
Run Layer’s solution introduces a multi-layered gateway that enforces authentication, delegation, validation, policy checks, and auditing, supporting various identity modes and ensuring that every action by an agent is attributable, revocable, and compliant with emerging standards.
The talk concludes with practical recommendations: audit agent tokens for delegation context, explicitly model delegation, enforce permission intersections, bind credentials per session, and log all actions for accountability.
# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Question posed: When an AI agent acts, who is technically responsible and whose identity is on the hook?                                               |
|   2 | The problem is complex due to current tools and delegation mechanisms.                                                                                 |
|   3 | The "valet key" analogy illustrates scoped access: ideally, tokens should only allow specific actions, but often allow broader access than intended.   |
|   4 | The "confused deputy problem" occurs when legitimate authority is misused for unintended actions.                                                      |
|   5 | Example: AI agent given a token to read emails can be tricked (via prompt injection) into forwarding emails externally if the token's scope allows it. |
|   6 | Current standards (like MCP and OAuth 2.1) acknowledge but do not fully address the confused deputy problem.                                           |
|   7 | Four main gaps identified:                                                                                                                             |
|   8 | Lack of delegation change tracking (who asked the agent to act)                                                                                        |
|   9 | No attenuation of access (cannot narrow token permissions through agent hops)                                                                          |
|  10 | No intent binding (scopes show capability, not purpose)                                                                                                |
|  11 | No audit trail of intent (tokens lack context of user intent)                                                                                          |
|  12 | Attack surfaces include:                                                                                                                               |
|  13 | Prompt injection (malicious instructions in data)                                                                                                      |
|  14 | Tool confusion (agent uses wrong tool)                                                                                                                 |
|  15 | Sub-agent escalation (full token passed to sub-agent)                                                                                                  |
|  16 | Session bleed (proxy scenario where authorization is misapplied)                                                                                       |
|  17 | Industry is converging on solutions:                                                                                                                   |
|  18 | Delegation as a first-class object                                                                                                                     |
|  19 | Intersection of agent and user policies                                                                                                                |
|  20 | Per-service session binding                                                                                                                            |
|  21 | Attenuation (permissions always narrowed, never expanded)                                                                                              |
|  22 | Auditing at every boundary                                                                                                                             |
|  23 | Run Layer's solution includes five layers: authentication, delegation validation, policy validation, security scanning, and auditing.                  |
|  24 | Supports three identity modes: human user, standalone agent, and agent acting on behalf of a user.                                                     |
|  25 | Delegation is tracked as a first-class entity, with immediate revocation and audit logs.                                                               |
|  26 | Uses RFC 8963 (token exchange) to support "on behalf of" authentication.                                                                               |
|  27 | Policy engine ensures agents never have more access than users.                                                                                        |
|  28 | Session grants bind credentials                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CmWJs_eAL0w)