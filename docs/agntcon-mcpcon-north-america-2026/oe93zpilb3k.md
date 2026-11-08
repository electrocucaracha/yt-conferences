---
layout: default
title: "One MCP Server, Many Agents: The Identity Gap OAuth Doesn't Close - Mohit Gurnani, Nutanix"
nav_order: 56
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Mohit, a log analytics platform lead at Nutanix, presents a talk addressing the identity gap in autonomous agent architectures where standard OAuth patterns fail to provide proper user attribution ..."
resource: "https://www.youtube.com/watch?v=OE93ZpILb3k"
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

Mohit, a log analytics platform lead at Nutanix, presents a talk addressing the identity gap in autonomous agent architectures where standard OAuth patterns fail to provide proper user attribution and permission scoping.
He illustrates that using shared service accounts for agents leads to "identity collapse" in audit logs and grants agents broader read permissions than the individual user, creating significant security and accountability risks.
To resolve this, he proposes a decision framework for selecting authentication patterns, recommending header or path forwarding (token pass-through) for scenarios requiring user-specific identity, such as on-call triage, where agents inherit the user’s scoped tokens to ensure actions are attributed correctly and permissions are strictly limited.
The talk details how to implement this using the Envoy AI Gateway (now Agent Router), which acts as a secure intermediary to fetch tokens from a vault and inject them into backend requests, preventing agents from directly accessing or harvesting credentials.
Finally, he emphasizes the importance of narrowly scoping tokens to limit the blast radius of potential leaks and highlights the gateway’s role in normalizing traffic across different AI providers while enforcing centralized security boundaries.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** Autonomous agents accessing enterprise tools often lack proper identity attribution, leading to two main issues: agents reading data beyond the user’s specific permissions and "identity collapse" where audit logs only show a shared service account rather than the human initiator. |
|   2 | :** The talk uses a three-agent suite as a case study: a Triage Agent (reads alerts/logs), a Root Cause Agent (performs code analysis/hypothesis), and a Fix/PR Agent (creates hot fixes/pull requests).                                                                                     |
|   3 | :** Using a single service account for all agents is convenient but dangerous. It grants agents broader read access than the individual user has and obscures which specific user initiated an action, making accountability and auditing difficult.                                         |
|   4 | :** Standard OAuth 2.1 requires browser-based user consent. This is structurally unsuitable for autonomous, background agents (e.g., 2:00 AM alerts) that must operate without human interaction.                                                                                            |
|   5 | :** While suitable for machine-to-machine communication, assigning a fixed identity to an agent causes identity collapse. It fails to reflect the changing on-call user (e.g., Alex this week, someone else next week) in audit logs.                                                        |
|   6 | :**                                                                                                                                                                                                                                                                                          |
|   7 | :** Best for human-in-the-loop scenarios like IDEs or CLIs where browser consent is feasible.                                                                                                                                                                                                |
|   8 | :** Ideal for background automations or agents (e.g., evaluation agents) where no human is involved.                                                                                                                                                                                         |
|   9 | :** Useful when multiple systems have different Identity Providers (e.g., Okta to GitHub). A Security Token Service (STS) acts as a broker to exchange tokens, though it requires significant infrastructure.                                                                                |
|  10 | /Path Forwarding:** The recommended solution for resolving identity gaps. It passes the user’s existing credentials through the gateway to the backend, ensuring the agent inherits the user’s specific identity and permissions.                                                            |
|  11 | :**                                                                                                                                                                                                                                                                                          |
|  12 | (e.g., via External Secret Operator) and injects them into requests to the backend.                                                                                                                                                                                                          |
|  13 | , preventing credential harvesting.                                                                                                                                                                                                                                                          |
|  14 | (databases) that do not support OAuth but accept personal access tokens.                                                                                                                                                                                                                     |
|  15 | (Agent Router):**                                                                                                                                                                                                                                                                            |
|  16 | , Kubernetes-native gateway maintained by Bloomberg, Nutanix, and others.                                                                                                                                                                                                                    |
|  17 | (Anthropic, Gemini, etc.).                                                                                                                                                                                                                                                                   |
|  18 | , token-based rate limiting, and MCP tool filtering to restrict access to unsafe tools.                                                                                                                                                                                                      |
|  19 | "Agent Router" and joined the Agent Tech AI Foundation.                                                                                                                                                                                                                                      |
|  20 | :**                                                                                                                                                                                                                                                                                          |
|  21 | :** Tokens must be strictly scoped (e.g., read-only) to limit the blast radius if compromised.                                                                                                                                                                                               |
|  22 | :** Using broad corporate tokens risks "deputy vulnerability," where stolen tokens could be misused for unrelated systems (e.g., payroll).                                                                                                                                                   |
|  23 | :** Always forward tokens only to trusted gateway URLs to prevent leakage to malicious endpoints.                                                                                                                                                                                            |
|  24 | :** Users configure MCPs (e.g., in `mcp.json`) with specific gateway URLs and scoped tokens, allowing the gateway to handle the secure forwarding.                                                                                                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/OE93ZpILb3k/hqdefault.jpg)]("https://www.youtube.com/watch?v=OE93ZpILb3k")

[Watch on YouTube](https://www.youtube.com/watch?v=OE93ZpILb3k)
