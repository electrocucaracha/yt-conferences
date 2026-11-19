---
layout: default
title: "ID-JAG: Solving OAuth Sprawl for Enterprise AI... - Aaron Parecki, Okta & Den Delimarsky, Anthropic"
nav_order: 20
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Dan from Anthropic and Aaron Parecki from Okta explain the emerging ID Jag standard, which streamlines secure authentication for MCP tools in enterprise environments."
resource: "https://www.youtube.com/watch?v=k8PVWNbnKQs"
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

Dan from Anthropic and Aaron Parecki from Okta explain the emerging ID Jag standard, which streamlines secure authentication for MCP tools in enterprise environments.
By leveraging existing trust relationships with enterprise Identity Providers (IDPs), ID Jag replaces the cumbersome process of manual OAuth consent prompts with a pre-authorized flow managed by administrators.
This approach significantly enhances security and usability by eliminating "prompt fatigue," preventing accidental connections to personal accounts, and enabling agents to operate autonomously without user presence.
The standard utilizes JSON Web Tokens to bridge trust domains, allowing MCP clients to exchange ID Jag grants for short-lived access tokens, thereby simplifying token revocation and centralizing audit logs.
As an IETF standard that is not exclusive to MCP, ID Jag is already supported by major platforms like Claude and Okta, offering a scalable solution for secure API access across various enterprise applications.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (Identity Assertion, JSON Web Token, Authorization Grant) is an emerging standard designed to streamline secure MCP tool usage in enterprise contexts.        |
|   2 | , which require manual user consent for every server connection, leading to "prompt fatigue" and security risks like accidental personal account connections. |
|   3 | , allowing agents to access multiple MCP servers without repeated user interaction.                                                                           |
|   4 | (IDP) and the MCP server’s authorization server to bridge different trust domains.                                                                            |
|   5 | ; the agent then requests an ID Jag from the IDP, which validates admin policies and issues a signed token.                                                   |
|   6 | ’s authorization server, requiring no changes to existing token validation infrastructure.                                                                    |
|   7 | , user identity, and optional scopes (e.g., read-only vs. read-write access).                                                                                 |
|   8 | , improving both security and user experience.                                                                                                                |
|   9 | (e.g., 1 hour) because the agent can automatically refresh them via the IDP without user presence.                                                            |
|  10 | ; disabling a user there immediately prevents new ID Jag issuance, effectively cutting off agent access.                                                      |
|  11 | , not unique to MCP, and can be applied to any OAuth-protected API.                                                                                           |
|  12 | (CNF claim) to mitigate token theft and authorization details for more granular, dynamic access control.                                                      |
|  13 | (Enterprise MCP Authorization) is a stable MCP extension supporting ID Jag, already integrated into Claude and supported by Okta and other vendors.           |
|  14 | , with ongoing adoption across the ecosystem.                                                                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/k8PVWNbnKQs/hqdefault.jpg)](https://www.youtube.com/watch?v=k8PVWNbnKQs)

[Watch on YouTube](https://www.youtube.com/watch?v=k8PVWNbnKQs)
