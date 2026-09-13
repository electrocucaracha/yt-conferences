---
type: Video Note
title: "[Session] OAuth Everywhere: What I Learned Building MCP Clients, Servers, & the Gateway Between Them"
description: "Donnie Adams, a software architect at OTO AI, discusses the team's experience building an MCP gateway with a unique architecture that allows a single URL to be shared across users, each authenticating with their own Outlook account. He outl..."
resource: https://www.youtube.com/watch?v=UjMYWi-tkP0
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Donnie Adams, a software architect at OTO AI, discusses the team's experience building an MCP gateway with a unique architecture that allows a single URL to be shared across users, each authenticating with their own Outlook account.
He outlines technical and user challenges encountered, particularly with OAUTH implementation in MCP, such as handling expired tokens, scope changes, and inconsistencies in client and server behaviors.
Adams highlights improvements coming to the MCP specification, including explicit scope requirements in the www-authenticate header and better flows for handling insufficient scopes, which will enhance user experience by reducing the need for manual credential resets.
He also touches on ongoing issues with authorization server metadata, dynamic client registration, and MCP request IDs, noting the rapid evolution of the MCP spec and the importance of adapting to these changes.
The talk concludes with an invitation to explore OTO AI's open-source projects, Obot and Nanobot, which embody these architectural and protocol learnings.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is Donnie Adams, software architect at OTO AI, presenting joint work with his engineering team.                                                 |
|   2 | OTO AI is building an MCP gateway, similar to other AI/MCP gateways discussed previously.                                                               |
|   3 | OOTH (OAuth) in MCP is still evolving and presents technical and user story challenges.                                                                 |
|   4 | OTO’s approach allows a single Outlook MCP server URL to be shared within a company; each user authenticates and the server is scoped to their account. |
|   5 | This architecture differs from others where each user must set up their own MCP server and URL.                                                         |
|   6 | OTO acts as authorization server, MCP server, and MCP client, proxying requests to the actual MCP server.                                               |
|   7 | Nanobot is used as both client and server in this setup.                                                                                                |
|   8 | MCP specification is rapidly changing; some discussed issues may already be outdated.                                                                   |
|   9 | Authorization flow involves multiple authentications: first with OTO, then with the third-party (e.g., Outlook).                                        |
|  10 | Issues encountered:                                                                                                                                     |
|  11 | Handling requests with expired tokens is inconsistent across clients (e.g., VS Code requires deleting credentials).                                     |
|  12 | Non-initialization requests (e.g., tool calls) with expired tokens are handled differently by clients; Nanobot repeats the flow for user convenience.   |
|  13 | Changing scopes on tokens is problematic; current spec lacks clear guidance.                                                                            |
|  14 | Scopes:                                                                                                                                                 |
|  15 | Scopes define permissions granted to clients.                                                                                                           |
|  16 | MCP spec currently lacks detailed scope handling.                                                                                                       |
|  17 | Both OOTH protected resource metadata and authorization server metadata may list supported scopes, but usage is unclear.                                |
|  18 | Servers may not advertise all supported scopes for security reasons.                                                                                    |
|  19 | Using all scopes from authorization server metadata is not recommended (violates least privilege).                                                      |
|  20 | Some servers behave unexpectedly when using different scope sources.                                                                                    |
|  21 | Upcoming MCP spec will include explicit scope requirements in the www-authenticate header, improving clarity and user experience.                       |
|  22 | New flow will allow clients to recover from insufficient scopes by prompting users to r                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=UjMYWi-tkP0)