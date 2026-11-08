---
layout: default
title: "Authorization After OAuth: Controlling Tools on Hosted MCP Servers You Don’t Own - Nick Taylor"
nav_order: 153
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker uses a rugby analogy to introduce the concept of governance and rule enforcement in Model Context Protocol (MCP) environments, highlighting that just as sports have specific rules, MCPs..."
resource: "https://www.youtube.com/watch?v=oGuj56_aOWo"
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

The speaker uses a rugby analogy to introduce the concept of governance and rule enforcement in Model Context Protocol (MCP) environments, highlighting that just as sports have specific rules, MCPs require defined permissions for tool calls.
He notes that while static configurations like read-only modes or coarse-grained OAuth scopes are common, they lack the dynamic, fine-grained control needed for robust security, especially given that a significant portion of remote MCPs currently lack proper authentication.
To address this, he introduces Pomerium, an open-source, self-hosted identity-aware proxy that functions as an MCP gateway by operating at the HTTP layer to handle OAuth and enforce policies without requiring code changes in the MCP server itself.
Through a live demonstration, he shows how Pomerium allows administrators to dynamically update policies—such as denying specific tool calls like merging pull requests—in real-time without redeploying the MCP, thereby providing centralized auditing and zero-trust security.
The session concludes with a promotion of a free, hands-on course where users can build and secure their own MCPs using Pomerium, emphasizing the importance of dynamic authorization and organizational governance for AI agents.

# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (Model Context Protocol) governance, comparing strict game rules to the need for controlled tool access in AI applications.                                                             |
|   2 | , such as read-only URL parameters or static API keys, which do not scale well for organizations.                                                                                       |
|   3 | ; once registered, they grant broad access (e.g., full repository access) without the ability to dynamically restrict specific tool calls.                                              |
|   4 | , with many relying on insecure static tokens or having no auth at all.                                                                                                                 |
|   5 | , allowing for policy enforcement, auditing, and management of multiple MCPs without redeploying individual servers.                                                                    |
|   6 | (IAP), inspired by Google’s Zero Trust model, act as a central point for verification, ensuring that network location does not imply trust and that identity is continuously validated. |
|   7 | (Apache 2.0), self-hosted Identity-Aware Proxy that operates at Layer 7 (HTTP) and functions as an MCP Gateway.                                                                         |
|   8 | , allowing developers to build "naked" MCPs with business logic while the proxy manages authentication and authorization.                                                               |
|   9 | , even if the user has broad OAuth scopes, providing dynamic control without code changes.                                                                                              |
|  10 | ; changes take effect immediately in memory without requiring the MCP server or gateway to be redeployed.                                                                               |
|  11 | , but a specific "merge pull request" tool call was denied after a policy update.                                                                                                       |
|  12 | , showing exactly which email identities were validated and which specific tool calls were allowed or denied.                                                                           |
|  13 | (like GitHub’s) by routing them through the proxy, preventing users from bypassing security controls.                                                                                   |
|  14 | , browser-based lesson on Axiom Use Labs where users can build, secure, and test MCPs with Pomerium without needing an AI subscription.                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/oGuj56_aOWo/hqdefault.jpg)]("https://www.youtube.com/watch?v=oGuj56_aOWo")

[Watch on YouTube](https://www.youtube.com/watch?v=oGuj56_aOWo)
