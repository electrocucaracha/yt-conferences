---
type: Video Note
title: "When an Agent Acts on Your Behalf, Who Holds the Keys? - Mariusz Sabath & Maia Iyer, IBM Research"
description: "Mario and Maya from IBM Research present their work on securing agentic applications at the platform level, focusing on challenges that arise when agents, rather than users, interact with enterprise systems. They explain that traditional AP..."
resource: https://www.youtube.com/watch?v=kc2NuTUt5Os
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Mario and Maya from IBM Research present their work on securing agentic applications at the platform level, focusing on challenges that arise when agents, rather than users, interact with enterprise systems.
They explain that traditional API key-based authentication is insufficient for multi-tenant, agent-driven workflows due to issues with context, observability, and zero trust enforcement.
To address this, they advocate for a standards-based approach using OAuth 2, Spiffy, and token exchange to provide short-lived, context-rich credentials and workload identity.
Their open-source project, Kajenti, demonstrates how these standards can be integrated into a pluggable platform, with the Obridge component transparently handling identity, authentication, and authorization for agents without requiring changes to application code.
The team also discusses ongoing work to improve attestation of agent attributes, support for dynamic authorization, and handling of advanced scenarios such as human-in-the-loop privilege escalation and independent agent identities.
Audience questions explore local versus remote agent workflows, privilege management, agent autonomy, and the use of gateways and guardrails for fine-grained control.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on security for agentic applications at the platform level.                                                                        |
|   2 | Traditional API key patterns break down in multi-tenant, enterprise agentic workflows.                                                                  |
|   3 | API keys are long-lived, lack context, and hinder zero trust and fine-grained authorization.                                                            |
|   4 | Need for more context and observability in every request involving agents.                                                                              |
|   5 | Best practices combine OAuth2, Spiffy, and OAuth token exchange to replace API keys.                                                                    |
|   6 | OAuth provides short-lived access tokens with user and application context.                                                                             |
|   7 | Token exchange supports nested transactions and context changes between agents and tools.                                                               |
|   8 | Spiffy provides workload identity, replacing static client secrets with dynamic, attestable identities.                                                 |
|   9 | Gateways and Vaults are useful for centralized control and interoperability with non-OAuth apps.                                                        |
|  10 | Project Kajenti built a platform using open source tools for orchestration, networking, security, and observability.                                    |
|  11 | Kajenti is pluggable and standards-based, enabling interoperability and easier adoption.                                                                |
|  12 | Identified and addressed interoperability gaps, e.g., Spire-issued credentials with Keycloak.                                                           |
|  13 | Developed Obridge component for automatic identity, inbound JWT validation, outbound token exchange, and transparency for agent developers.             |
|  14 | Obridge injects sidecars to handle security, removing need for agents to manage auth code.                                                              |
|  15 | Security properties: no static secrets, short-lived tokens, inbound validation, subject preservation, scope-based access control, full auditability.    |
|  16 | Demo showed Kajenti UI, agent registration, token validation, and transparent security flows.                                                           |
|  17 | Obridge reduces operational code and simplifies agent development.                                                                                      |
|  18 | Current/future work: dynamic client registration, Vault integration, authorization pluggability, human-in-the-loop, intent-based access control (IBAC). |
|  19 | Exploring attestation of agent semantic attributes in Spire for richer identity.                                                                        |
|  20 | Need for combining multiple attesters and establishing ground truth for agent attributes.                                                               |
|  21 | Defens                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kc2NuTUt5Os)