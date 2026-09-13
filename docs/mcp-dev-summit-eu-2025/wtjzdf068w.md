---
layout: default
title:
  "[Session] Secure from Day One Building Production Ready MCP Servers with Nick
  Taylor - Pomerium"
nav_order: 35
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Nick, a developer advocate at Primarium, presents on building production-ready
  MCP servers with security from the outset, focusing on zero trust security principles.
  He explains that zero trust means never implicitly trusting any request, a...
resource: https://www.youtube.com/watch?v=_wtJzDf068w
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

Nick, a developer advocate at Primarium, presents on building production-ready MCP servers with security from the outset, focusing on zero trust security principles.
He explains that zero trust means never implicitly trusting any request, always verifying identity and context through a policy engine, and ensuring every access attempt is validated, regardless of network location.
Nick discusses how identity-aware proxies, such as Primarium's open core solution, can provide fine-grained access control, auditing, and OAuth flows without requiring developers to implement OAuth themselves.
Through demos—despite some technical issues—he illustrates how developers can use these tools to secure MCP servers during both development and production, enabling secure, public access without relying on VPNs and ensuring a smoother transition to production environments.
The approach offers centralized management of authentication, observability, and tool-level policy enforcement, making it easier for teams to adopt robust security practices from day one.

# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on building production-ready MCP servers with security from day one.                                     |
|   2 | Main topics: zero trust security, its application to MCP, OAUTH scopes vs. tool-level policies, demo, and workflow takeaways. |
|   3 | Zero trust security principles:                                                                                               |
|   4 | No implicit trust, even inside the network.                                                                                   |
|   5 | Strong identity verification and context-aware access.                                                                        |
|   6 | Every request is verified through a policy engine.                                                                            |
|   7 | No reliance on VPN; can be implemented at the network edge.                                                                   |
|   8 | Identity-aware proxy components:                                                                                              |
|   9 | Identity provider (e.g., Google, Entra, Keycloak, GitHub).                                                                    |
|  10 | Dynamic policy engine.                                                                                                        |
|  11 | Proxy that controls access regardless of user location.                                                                       |
|  12 | Zero trust ensures all resources are publicly accessible but protected by login and policy checks.                            |
|  13 | Requests are validated before reaching resources; denied requests never reach the resource.                                   |
|  14 | Latency from zero trust is minimal (milliseconds).                                                                            |
|  15 | Benefits for MCP:                                                                                                             |
|  16 | Fine-grained policies possible (beyond OAUTH’s coarse scopes).                                                                |
|  17 | Visibility and auditing are built-in.                                                                                         |
|  18 | OTEL traces supported.                                                                                                        |
|  19 | MCP security best practices recommend proxies and align with zero trust.                                                      |
|  20 | OAUTH scopes (e.g., GitHub’s “repo”) are broad; zero trust allows finer tool-level controls.                                  |
|  21 | Primarium’s identity-aware proxy is open core and handles OAUTH flows, reducing implementation burden.                        |
|  22 | Upstream OAUTH flows (e.g., Google) are managed via configuration; tokens never leave the gateway.                            |
|  23 | MCP clients receive short-lived JWTs, not long-lived tokens.                                                                  |
|  24 | Works with standard MCP clients (Claude, ChatGPT, Goose, VS Code).                                                            |
|  25 | Clients don’t need to manage OAUTH; receive short-lived tokens.                                                               |
|  26 | Demo showed configuring MCP servers with identity-aware proxy, applying policies, and auditing access.                        |
|  27 | Developers can do local dev with security and OAUTH flows in place.                                                           |
|  28 | Uniform security posture is possible during development and in production.                                                    |
|  29 | No VPN required; zero trust is more suitable for securing MCP servers.                                                        |
|  30 | Auditing and observability a                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_wtJzDf068w)
