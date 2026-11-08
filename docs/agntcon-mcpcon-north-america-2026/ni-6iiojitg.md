---
layout: default
title: "Agent Autonomy vs. Capability vs. Security: How to Pick All 3 - Kim Maida, Keycard"
nav_order: 81
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'The video addresses the "trilemma" facing AI agent developers, who often must sacrifice capability, autonomy, or security when granting agents access to resources.'
resource: "https://www.youtube.com/watch?v=NI-6iiojItg"
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

The video addresses the "trilemma" facing AI agent developers, who often must sacrifice capability, autonomy, or security when granting agents access to resources.
The speaker demonstrates how over-privileged agents using static API keys can cause severe incidents, such as leaking customer PII or dropping production databases, because they lack granular, task-specific controls.
To resolve this, the presentation introduces a solution based on the OAuth 2.0 token exchange standard, which enables single-use, down-scoped access tied to specific tasks rather than broad, standing permissions.
This approach utilizes a Security Token Service (STS) and intent-based authorization to verify both the agent’s identity and the user’s delegated permissions before allowing actions, ensuring that agents can only perform tasks explicitly approved by policy and the user.
By implementing this delegated authorization model, organizations can achieve a balance where agents retain the capability to use necessary tools and the autonomy to act independently, while maintaining strict security boundaries that prevent unauthorized or harmful actions.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , autonomy, and security, often forcing a sacrifice of one to achieve the others.                                                                                                                    |
|   2 | , such as exposing customer PII, dropping production databases, or taking servers offline without proper authorization.                                                                              |
|   3 | , gateways, and sandboxes are insufficient because they often grant standing credentials that outlive specific tasks or fail to restrict external access effectively.                                |
|   4 | (extending OAuth 2.0) to provide single-use, down-scoped access tied to specific tasks.                                                                                                              |
|   5 | , ensuring accountability and identity preservation.                                                                                                                                                 |
|   6 | (IBA) is introduced to check the agent's intended mission (goal, allowed actions, limits) before action, distinguishing between low-risk auto-approvals and high-risk actions requiring user review. |
|   7 | (STS) evaluates requests against governance policies, issuing ephemeral tokens that expire within minutes and are never stored.                                                                      |
|   8 | , the agent successfully acknowledges and reads tickets using its own identity but is blocked from accessing customer data rows or deleting databases due to policy restrictions.                    |
|   9 | (the user) is not permitted to do, such as restarting production servers without the required SRE admin role.                                                                                        |
|  10 | , the STS issues a token allowing the agent to execute the task on the user's behalf, resolving the incident securely.                                                                               |
|  11 | , autonomy through independent agent identity, and security through task-level delegated authorization.                                                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NI-6iiojItg/hqdefault.jpg)]("https://www.youtube.com/watch?v=NI-6iiojItg")

[Watch on YouTube](https://www.youtube.com/watch?v=NI-6iiojItg)
