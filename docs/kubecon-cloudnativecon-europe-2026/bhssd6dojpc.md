---
layout: default
title:
  "Gateway API: Bridging the Gap from Ingress t... Nick Y, James S, Katarzyna
  Ł, Rostislav B & Norwin S"
nav_order: 131
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Mario Sabat and Maya from IBM Research discuss
  their work on securing agentic applications at the platform level, focusing on challenges
  that arise when agents, rather than users, interact with enterprise systems. They...
resource: https://www.youtube.com/watch?v=bHSsd6dojPc
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Mario Sabat and Maya from IBM Research discuss their work on securing agentic applications at the platform level, focusing on challenges that arise when agents, rather than users, interact with enterprise systems.
They explain that traditional API key-based authentication is insufficient for multi-tenant, agent-driven workflows due to issues with context, observability, and zero trust enforcement.
To address this, they advocate for a security blueprint combining OAuth2 for delegation, Spiffy/Spire for workload identity, and token exchange for propagating context through nested agent interactions, all implemented in their open-source project Kajenti.
They introduce Obridge, a component that transparently manages identity, inbound validation, and token exchange for agents, reducing developer burden and enhancing security by eliminating static secrets and enabling full audit trails.
The team also highlights ongoing and future work, such as integrating agent semantic attributes into identity attestation, supporting dynamic privilege elevation, and refining authorization policies, while fielding audience questions about local versus remote agents, independent agent identities, and the use of gateways and guardrails for fine-grained control.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation focuses on security for agentic applications at the platform level.                                                                                                     |
|   2 | Traditional API key patterns break down in multi-tenant, enterprise agent scenarios.                                                                                                 |
|   3 | API keys are long-lived, lack context, and hinder zero trust and fine-grained authorization.                                                                                         |
|   4 | Best practices combine OAuth2, Spiffy, and OAuth token exchange to replace API keys.                                                                                                 |
|   5 | OAuth provides delegation; access tokens carry user, application, and audience context.                                                                                              |
|   6 | Token exchange supports nested transactions and context changes between agents/tools.                                                                                                |
|   7 | Spiffy provides workload identity; attests platform and workload attributes for authentication.                                                                                      |
|   8 | Gateway centralizes control; Vault helps interoperate with non-OAuth applications.                                                                                                   |
|   9 | Project Kajenti built a platform using open source tools for orchestration, networking, security, and observability.                                                                 |
|  10 | Kajenti is pluggable and standards-based, enabling interoperability and easier adoption.                                                                                             |
|  11 | Identified and addressed interoperability gaps, e.g., Spire-issued credentials with Keycloak.                                                                                        |
|  12 | Developed Obridge component for automatic identity, inbound JWT validation, outbound token exchange, and transparent integration for agent developers.                               |
|  13 | Obridge eliminates static secrets, uses short-lived tokens, preserves subject identity, enables scope-based access control, and provides full auditability.                          |
|  14 | Demonstrated Kajenti UI, agent registration, token validation, and transparent security flows.                                                                                       |
|  15 | Obridge reduces operational code and complexity for agent developers.                                                                                                                |
|  16 | Current/future work: MCP gateway integration, dynamic client registration, Vault integration, authorization pluggability, human-in-the-loop, and intent-based access control (IBAC). |
|  17 | Challenges with agent semantic attribute attestation; exploring Spire enhancements for stacking attesters and defining ground truth for agent attributes.                            |
|  18 | Security blueprint involves multiple keys and locks: user, workload, Spiffy (identity), OAuth (delegation), and resource server (authorization).                                     |
|  19 | Local agentic                                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=bHSsd6dojPc)
