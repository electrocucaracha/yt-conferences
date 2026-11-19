---
layout: default
title: "From DCR to CIMD: MCP Client Identity in Production - Alvaro Inckot, Runlayer"
nav_order: 63
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Alberic, a founding identity engineer at Run Layer, presents a technical overview of the transition from Dynamic Client Registration (DCR) to Client ID Metadata Documents (CIMD) within the Model Co..."
resource: "https://www.youtube.com/watch?v=uJ_YscSjBXI"
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

Alberic, a founding identity engineer at Run Layer, presents a technical overview of the transition from Dynamic Client Registration (DCR) to Client ID Metadata Documents (CIMD) within the Model Context Protocol (MCP) ecosystem.
He highlights the operational challenges of DCR, such as uncontrolled client registration, rogue clients, and lifecycle management issues, which led to a significant spike in client registrations for a single tenant.
To mitigate these risks, Run Layer implemented strict policies, rate limiting, and an OAuth broker using initial access tokens to ensure the registration endpoint remains manageable and secure.
The talk further details the adoption of CIMD as a more robust alternative, where client identity is derived from the domain rather than a registered secret, simplifying management and reducing the attack surface.
Finally, the speaker outlines critical security considerations for implementing CIMD in enterprise gateways, including preventing Server-Side Request Forgery (SSRF), handling domain takeovers, and managing localhost redirect URIs through emerging attestation standards.

# Main Points

|   # | Main point                                                                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : The speaker, Alberic from Run Layer, discusses production challenges in MCP (Model Context Protocol) client identity, specifically transitioning from Dynamic Client Registration (DCR) to Client ID Metadata Documents (CIMD). |
|   2 | : A single tenant generated 4,228 client registrations in one day without owners, highlighting the unmanageability of DCR in production environments.                                                                             |
|   3 | : The four roles in MCP authentication are the Resource Owner (user), Client (AI agent/MCP client), Authorization Server (IdP), and Resource Server (MCP server).                                                                 |
|   4 | :                                                                                                                                                                                                                                 |
|   5 | : The spec allows unauthenticated registration requests, enabling rogue clients to impersonate legitimate ones.                                                                                                                   |
|   6 | : Run Layer implements policies on the `/register` endpoint, uses Initial Access Tokens to identify tenants, and applies rate limiting to control client volume.                                                                  |
|   7 | & Churn**:                                                                                                                                                                                                                        |
|   8 | : Users frequently delete and re-register clients due to refresh token failures or secret expiration, leading to database bloat and "rogue" clients.                                                                              |
|   9 | : Early MCP clients cached authorization metadata, causing friction when gateway configurations changed.                                                                                                                          |
|  10 | : Implementing a predictable lifecycle with admin-side tools to reset connections and clear invalid clients.                                                                                                                      |
|  11 | :                                                                                                                                                                                                                                 |
|  12 | : External MCP servers often require manual allowlisting of redirect URIs via IT tickets, negating DCR's automation benefits.                                                                                                     |
|  13 | : Run Layer provides a UI for IT admins to easily add specific client URLs (e.g., Cursor sign-in links) to allowlists, reducing setup friction.                                                                                   |
|  14 | :                                                                                                                                                                                                                                 |
|  15 | : CIMD removes the need for client secrets and dynamic registration endpoints. Identity is tied to the domain.                                                                                                                    |
|  16 | : The client sends a URL as the `client_id`; the server fetches the metadata document, validates redirect URIs, and proceeds with authorization.                                                                                  |
|  17 | :                                                                                                                                                                                                                                 |
|  18 | : Servers must be able to reach the client's metadata URL, which may require exposing private network resources.                                                                                                                  |
|  19 | & Security**: Fetching arbitrary URLs poses SSRF risks. Mitigations include enforcing HTTPS, resolving IPs before redirects, blocking special-use IPs, and pinning IPs to prevent DNS rebinding.                                  |
|  20 | : Risks exist if domains change hands or if wildcard subdomain rules are too permissive.                                                                                                                                          |
|  21 | : Handling `localhost` redirect URIs remains an open problem; a draft RFC for software attestation is being monitored as a potential solution.                                                                                    |
|  22 | : Each tenant should maintain its own metadata document to isolate issues and simplify management.                                                                                                                                |
|  23 | : Adoption of CIMD is increasing. Run Layer is also preparing for enterprise standards like AD Join and Cross-App Access Tokens (CAAT) for future OAuth/MCP authentication.                                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/uJ_YscSjBXI/hqdefault.jpg)](https://www.youtube.com/watch?v=uJ_YscSjBXI)

[Watch on YouTube](https://www.youtube.com/watch?v=uJ_YscSjBXI)
