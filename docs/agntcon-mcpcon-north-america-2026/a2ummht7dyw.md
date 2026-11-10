---
layout: default
title: "The Control Plane Your MCP Gateway Forgot - Alex Salazar, Arcade.dev"
nav_order: 84
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Alex Salazar, founder and CEO of arcade.dev, presents a framework for implementing control planes in AI to address the critical gap between agent guardrails and enterprise governance."
resource: "https://www.youtube.com/watch?v=A2uMmhT7dyw"
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

Alex Salazar, founder and CEO of arcade.dev, presents a framework for implementing control planes in AI to address the critical gap between agent guardrails and enterprise governance.
He argues that traditional guardrails are insufficient for security, advocating instead for a governance layer that enforces "delegated user authorization," ensuring that an agent’s actions are validated against both its own identity and the specific user’s permissions at runtime.
Salazar highlights two common failure patterns in current agent deployments: service accounts that create access bypass vulnerabilities and agents that inherit excessive user permissions, proposing that the intersection of these identities is the only secure approach.
To demonstrate this, he showcases arcade.dev’s new tool recommendation feature, which significantly reduces token costs and improves accuracy by curating the most relevant tools from thousands of options, while also detailing a live demo where the system enforces authorization flows, redacts sensitive PII, and requires human MFA for destructive operations.
The presentation concludes with a strategic roadmap for enterprises, emphasizing the need for identity separation, granular tool curation, and robust observability to create a trusted, multi-user environment that allows agents to safely interact with critical business systems like CRMs and ERPs.

# Main Points

|   # | Main point                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | "tool recommendations" feature that curates the most relevant tools from a large catalog, reducing total token costs by approximately 37% per session and achieving a 90%+ recall rate for the correct tool.                 |
|   2 | , including Microsoft and Anthropic, by over 40% in tool recommendation and search benchmarks.                                                                                                                               |
|   3 | "guardrails" are insufficient for enterprise security because they rely on non-deterministic LLM behavior, resulting in unacceptable error rates for critical security policies.                                             |
|   4 | % adherence to organizational policies when agents interact with critical business systems like CRMs and ERPs.                                                                                                               |
|   5 | "service accounts" (where agents have their own broad permissions, leading to access bypass vulnerabilities) and agents inheriting the full permissions of the logged-in user (exposing agents to destructive capabilities). |
|   6 | "delegated user authorization," which checks both the agent’s identity/scopes and the user’s permissions/entitlements for every single tool request.                                                                         |
|   7 | "URL elicitation," which enables tool-level authorization and supports this delegated model, facilitating enterprise adoption of MCP for sensitive operations.                                                               |
|   8 | ; therefore, all security checks must occur at the execution layer where tool calls happen, not within the model itself.                                                                                                     |
|   9 | (distinguishing agent vs. user), tool curation (limiting access to specific granular tools), and the "three A's": authentication, authorization, and audit.                                                                  |
|  10 | , while audit logs must be immutable and inaccessible to the agent to prevent the agent from covering its tracks.                                                                                                            |
|  11 | : end user experience (e.g., approval prompts), agent skills (protecting proprietary intellectual property in workflows), and system-level access (controlling connections to external systems).                             |
|  12 | , as single-user desktop solutions create security holes via tunneling and lack the scalability required for enterprise deployment.                                                                                          |
|  13 | , Arcade enforced an authorization flow for a new user, redacted sensitive PII from CRM data based on DLP policies, and required human MFA for destructive operations like closing an account.                               |
|  14 | "agent overreach," where agents take unauthorized actions to achieve goals, necessitating human-in-the-loop verification for high-stakes actions.                                                                            |
|  15 | , then establish a single "golden path" or egress point for all agent traffic to simplify governance.                                                                                                                        |
|  16 | , policy, and business systems, but once the first agent is deployed, subsequent deployments become significantly easier and faster.                                                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/A2uMmhT7dyw/hqdefault.jpg)](https://www.youtube.com/watch?v=A2uMmhT7dyw)

[Watch on YouTube](https://www.youtube.com/watch?v=A2uMmhT7dyw)
