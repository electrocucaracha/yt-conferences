---
type: Video Note
title: 'Enterprise-Ready MCP: Security Patterns and the "4-Legged" Identity Challenge - Paulina Xu'
description: "In this talk, Paulina, CEO of Aentic Fabric, explains the challenges of making MCP (Multi-Component Platform) enterprise-ready, focusing on the increasing complexity of security and identity as systems move beyond local development. She out..."
resource: https://www.youtube.com/watch?v=pJPocx9_kT8
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Paulina, CEO of Aentic Fabric, explains the challenges of making MCP (Multi-Component Platform) enterprise-ready, focusing on the increasing complexity of security and identity as systems move beyond local development.
She outlines how traditional OAuth models, designed for simple, explicit delegation between users, applications, and APIs, break down when agents and MCP servers introduce dynamic, multi-hop delegation chains, leading to issues like identity loss and ambiguous authorization.
Paulina discusses four key RFCs—9728 (resource metadata), 8414 (authorization server metadata), 7591 (dynamic client registration), and 8693 (token exchange)—that together enable agents to securely discover, register, and delegate identity across complex, distributed systems.
She emphasizes that robust security in agentic systems requires layered defenses, including least privilege, encryption, observability, availability, and strict secret management, and illustrates practical solutions such as broker layers for centralized token exchange and policy enforcement.
The session concludes with demonstrations of these concepts in practice and a Q&A addressing token audience changes, revocation, and the need for consistent security across agent-to-agent interactions.
# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MCP enterprise readiness hinges on solving security and identity challenges beyond local development.                           |
|   2 | The "four-legged identity challenge" is the minimum complexity; real-world systems often have longer delegation chains.         |
|   3 | Traditional OAuth (OOTH) was designed for simple, explicit, single-hop delegation: user → application → IDP.                    |
|   4 | Three-legged OAuth flow (user → application → API) maintains clear identity and short delegation.                               |
|   5 | Introducing agents and MCP servers creates multi-hop, dynamic delegation: user → agent → MCP → API.                             |
|   6 | OAuth breaks down in agentic systems due to ambiguity over whose identity is used and audience-bound tokens.                    |
|   7 | Problems include identity loss midchain, over-permission, data leakage, and lack of auditability.                               |
|   8 | Complexity increases with federation, multiple IDPs, and agent-to-agent communication.                                          |
|   9 | Four common patterns for identity in agentic systems:                                                                           |
|  10 | Non-delegating client credentials: easy, but loses user identity.                                                               |
|  11 | Token exchange: preserves identity, but limited RFC 8693 support.                                                               |
|  12 | Pre-injected tokens: requires knowing all dependencies in advance.                                                              |
|  13 | Out-of-band login: secure but adds friction.                                                                                    |
|  14 | Four RFCs needed for agentic OAuth:                                                                                             |
|  15 | RFC 9728: resource metadata (discovery).                                                                                        |
|  16 | RFC 8414: authorization server metadata (how to interact).                                                                      |
|  17 | RFC 7591: dynamic client registration.                                                                                          |
|  18 | RFC 8693: token exchange (delegation).                                                                                          |
|  19 | Identity becomes a process: discovered, established, and transformed as agents move through systems.                            |
|  20 | Security principles for enterprise agentic systems:                                                                             |
|  21 | Least privilege: use tightly scoped, short-lived tokens; revalidate at every hop.                                               |
|  22 | Encryption: encrypt data at rest and in transit; use envelope encryption and secure key management.                             |
|  23 | Observability: log all actions, enable tracing, and implement DLP.                                                              |
|  24 | Availability: design for scaling, failover, and resilience.                                                                     |
|  25 | OAuth hardening and secret management: enforce strict validation, use MTLS, manage secrets via vaults, rotate and audit access. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pJPocx9_kT8)