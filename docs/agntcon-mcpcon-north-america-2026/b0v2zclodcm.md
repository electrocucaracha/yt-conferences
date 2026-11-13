---
layout: default
title: "MCP Security, Two Years In - Den Delimarsky, Anthropic"
nav_order: 61
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Dan, a lead maintainer of the Model Context Protocol (MCP), reflects on the evolution of MCP security over the past two years, emphasizing a shift from delegating authorization to developers toward..."
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

Dan, a lead maintainer of the Model Context Protocol (MCP), reflects on the evolution of MCP security over the past two years, emphasizing a shift from delegating authorization to developers toward an opinionated, standardized approach based on OAuth 2.1.
He explains that this standardization ensures consistency across diverse environments and reduces the risk of security misconfigurations, particularly as MCP adoption scales to billions of SDK downloads.
To enforce security, the community has implemented coordinated vulnerability disclosure, strict conformance testing for SDKs, and best practices such as audience validation and per-client consent to prevent token misuse.
Looking ahead, Dan highlights new initiatives like Enterprise Managed Authorization, Workload Identity Federation, and the Workload Authorization Grant (WAG) to support agent-based interactions, where AI agents require secure, short-lived credentials and distinct identities rather than relying on human-in-the-loop consent.
These advancements aim to make it easy for developers to implement secure practices while making it difficult to introduce vulnerabilities, ensuring MCP remains robust as it transitions from human-centric to agent-centric workflows.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : the protocol specification, secure SDKs, and established best practices.                                                                              |
|   2 | , causing inconsistency; the protocol has since become opinionated to ensure uniform security.                                                          |
|   3 | , moving away from custom implementations to leverage existing security standards and RFCs.                                                             |
|   4 | (e.g., Okta, Microsoft Entra ID) rather than building authorization servers from scratch.                                                               |
|   5 | ; the ecosystem now includes SDKs for TypeScript, Python, Go, Java, Rust, and C#.                                                                       |
|   6 | , the maintainers have a high responsibility to coordinate vulnerability disclosure and mitigation across the entire ecosystem.                         |
|   7 | , addressing issues like confused deputy scenarios, token pass-through, and audience/issuer validation to prevent mix-up attacks.                       |
|   8 | , with nearly one-third of the 116 test scenarios being security-oriented.                                                                              |
|   9 | , requiring new authorization mechanisms.                                                                                                               |
|  10 | (EMA), partnered with Okta, allows admins to pre-approve connections, eliminating individual consent prompts for users and agents.                      |
|  11 | (DPoP) binds tokens to specific devices using trusted platform modules, preventing token exfiltration and replay attacks.                               |
|  12 | (WIF) enables MCP servers to use short-lived credentials provided by cloud platforms (AWS, Azure, GCP) instead of static API keys or secrets.           |
|  13 | (WAG) is being developed to provide agents with their own distinct identity, embedding claims like workspace and channel for granular policy decisions. |
|  14 | , ensuring secure, scalable, and consistent authorization for autonomous AI agents.                                                                     |

# Video

This video is no longer available on YouTube.

<!-- resource: https://www.youtube.com/watch?v=b0v2zCLOdcM -->
