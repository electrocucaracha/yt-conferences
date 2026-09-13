---
layout: default
title: "[Session] Why is MCP Auth Hard and What Are We Planning to Do About It"
nav_order: 36
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  In this talk, Paul, a technical staff member at Anthropic and MCP core
  maintainer, discusses the challenges of implementing OAuth (O) in the context of
  the Model Context Protocol (MCP). He explains that traditional OAuth flows rely
  on stron...
resource: https://www.youtube.com/watch?v=wvtGlur2SdI
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

In this talk, Paul, a technical staff member at Anthropic and MCP core maintainer, discusses the challenges of implementing OAuth (O) in the context of the Model Context Protocol (MCP).
He explains that traditional OAuth flows rely on strong, pre-established trust between clients and servers through manual registration, but MCP aims to enable dynamic, general-purpose clients to access resources they've never seen before, which weakens this trust and introduces new risks such as malicious clients, servers, and man-in-the-middle attacks.
Paul outlines several practical difficulties, including the complexity of implementing numerous RFCs, incompatibility issues, and the limitations of dynamic client registration (DCR), which was not designed for MCP's scale or requirements.
To address these, the team is working on conformance testing, SDK pluggability, improved inspection tools, live examples, and a new approach using client ID metadata documents (SEP 9991) to replace DCR.
He also highlights the need for stronger trust mechanisms, such as moderated registries, and better guidance for handling "second hop" resource access.
Paul concludes by inviting contributors to join the MCP O interest group to help improve specifications, tools, and documentation.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Paul, member of technical staff at Anthropic, MCP core maintainer, works on O working group and TypeScript/Python SDKs                                     |
|   2 | Topic: Why MCP OAuth is hard, common problems, friction in implementation, and solutions                                                                   |
|   3 | In the past, integrating with resources (e.g., Google Calendar) required custom code and pre-registration for each API                                     |
|   4 | LLMs and MCP allow general-purpose clients to connect to new resources with a single integration, even without prior knowledge or trust                    |
|   5 | MCP enables clients to access resources they've never seen before, but lacks pre-existing trust relationships                                              |
|   6 | Challenges arise from weak trust between clients and servers due to dynamic client registration (DCR) instead of pre-registration                          |
|   7 | Risks include: bad clients tricking users, bad servers posing as legitimate, and man-in-the-middle attacks                                                 |
|   8 | OAuth preferred over API keys for flexibility, consent screens, and easier revocation                                                                      |
|   9 | Pre-registration is still a viable option if possible                                                                                                      |
|  10 | Implementing MCP OAuth is complex due to many required RFCs and potential incompatibilities                                                                |
|  11 | Solutions include: conformance testing, SDK pluggability, inspector updates, and live examples                                                             |
|  12 | Conformance testing involves golden servers/clients and trace comparison to ensure consistent implementations                                              |
|  13 | SDK pluggability (e.g., middleware in TypeScript) aims to reduce parallel implementations and inconsistencies                                              |
|  14 | DCR is painful with MCP due to database scaling, lack of expiration semantics, and cluttered client screens                                                |
|  15 | Proposed solution: client ID metadata documents (SEP 9991), where client ID is a URL to metadata, reducing database issues and improving clarity           |
|  16 | More trust needed: registry API and stronger moderation for server URLs, especially in enterprise/internal environments                                    |
|  17 | Second hop problem: MCP servers often access additional resources outside MCP, adding complexity and requiring guidance/examples for secure token handling |
|  18 | Recap: MCP OAuth is hard due to enabling general-purpose clients, implementatio                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wvtGlur2SdI)
