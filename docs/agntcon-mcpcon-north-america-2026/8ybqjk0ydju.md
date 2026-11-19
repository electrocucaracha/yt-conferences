---
layout: default
title: "Stop Running Agents as Service Accounts: User-Scoped Access for... - Masato Kozuka, Hitachi, Ltd."
nav_order: 76
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Masahiro Kozuka from Hitachi presents a framework for ensuring that AI agents calling external tools operate strictly within the permissions granted to the user, addressing the critical questions o..."
resource: "https://www.youtube.com/watch?v=8Ybqjk0ydjU"
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

Masahiro Kozuka from Hitachi presents a framework for ensuring that AI agents calling external tools operate strictly within the permissions granted to the user, addressing the critical questions of identifying both the user and the agent in cross-domain scenarios.
He distinguishes between three levels of token identity: service accounts (no user), impersonation (user identified but agent hidden), and delegation (both user and agent identified), noting that current standards often lack a standardized way to name the agent in the token.
To solve the problem of sub-agents calling tools without a user browser session, Kozuka proposes two primary methods: identity chaining, where the tool’s authorization server accepts a grant from the platform’s server, and a token vault approach, where the platform stores pre-authorized tokens linked to users via SSO.
While the token vault allows the platform to enforce agent-specific policies through a central broker, it introduces security trade-offs such as the risk of stolen refresh tokens and the need for manual revocation synchronization.
Kozuka concludes by recommending that organizations start by implementing user identification in tokens and platform-side agent checks, while monitoring ongoing standardization efforts for agent delegation claims.

# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | , Masahiro Kozuka from Hitachi, discusses ensuring AI agents call tools only within the permissions granted to the user. |
|   2 | : identifying which user asked for the action and which agent performed it.                                              |
|   3 | : the user’s platform (with its own Authorization Server) and the external tool’s domain (with its own AS).              |
|   4 | ’s browser for sign-in, such as when a sub-agent makes the call.                                                         |
|   5 | :                                                                                                                        |
|   6 | (Service Account): No user in the `sub` claim; the agent acts as the platform.                                           |
|   7 | (Impersonation): User in `sub`, no agent in `act`; the tool sees only the user.                                          |
|   8 | (Delegation): User in `sub` and agent in `act`; the tool sees both identities.                                           |
|   9 | ’s standard OAuth flow requires a browser for user sign-in, which breaks for sub-agents without browser access.          |
|  10 | , two methods are proposed: Identity Chaining and Token Vault.                                                           |
|  11 | ’s token for a grant accepted by the tool’s AS, requiring the tool owner to trust the platform’s AS.                     |
|  12 | ; the agent retrieves these stored tokens for subsequent calls without new sign-ins.                                     |
|  13 | , the tool can verify user permissions (claims A, B, C) but cannot verify the agent (claim D).                           |
|  14 | (claims E, F, Z) using a routing layer and a policy catalog that checks which agent may call which tool.                 |
|  15 | ’s AS to write the `act` claim, as only the issuing AS can add this trusted identity.                                    |
|  16 | (`act` vs. `client_id`) and what additional context to include.                                                          |
|  17 | , implementing Identity Chaining or Token Vault, and enforcing agent checks on the platform side.                        |
|  18 | , with a development timeline of approximately six months.                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8Ybqjk0ydjU/hqdefault.jpg)](https://www.youtube.com/watch?v=8Ybqjk0ydjU)

[Watch on YouTube](https://www.youtube.com/watch?v=8Ybqjk0ydjU)
