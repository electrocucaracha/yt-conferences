---
type: Video Note
title: "Least-Privilege for AI: Authorizing Agents and MCP Tools with A... Luc Chmielowski & Nina Polshakova"
description: "In this talk, Nina Pushkova and Luke Miroski discuss the challenges of securing AI agents, particularly those using the MCP protocol, and present a solution that combines Agent Gateway and Kyverno for centralized authorization. They explain..."
resource: https://www.youtube.com/watch?v=tEAkoZpdhSc
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Nina Pushkova and Luke Miroski discuss the challenges of securing AI agents, particularly those using the MCP protocol, and present a solution that combines Agent Gateway and Kyverno for centralized authorization.
They explain that traditional authorization for MCP is often implemented inconsistently across servers, leading to security gaps and duplicated logic, and highlight how Agent Gateway—a high-performance, Rust-based gateway—supports unified authorization, OAuth 2.0 flows, and integrates with Kyverno for policy enforcement.
Through a live demo, they show how Agent Gateway fronts MCP tools, requiring users to authenticate via OAuth and enforcing fine-grained access controls with Kyverno policies, thereby preventing unauthorized actions such as applying dangerous manifests to production clusters.
The demo illustrates how Kyverno policies can parse MCP requests, validate user permissions, and leverage Kubernetes’ native authorization mechanisms to ensure only permitted actions are executed.
The presenters emphasize the importance of reusing existing cloud-native tools and processes, like Kyverno and policy-as-code, to secure AI workloads rather than reinventing security solutions.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Nina Pushkova (Solo, Agent Gateway maintainer) and Luke Miroski (Keano maintainer)                                                                                                                                               |
|   2 | Focus of talk: Securing AI agents using least privilege, MCP protocol, Agent Gateway, and Kyverno                                                                                                                                                          |
|   3 | Problem: AI agents in production can cause issues if not properly secured; authorization is often missing or inconsistent in MCP servers                                                                                                                   |
|   4 | MCP protocol: JSON RPC-based, stateful, includes semantic layer for LLMs, supports capability negotiation, and OAuth 2.0                                                                                                                                   |
|   5 | Traditional proxies are stateless and not suitable for MCP’s stateful, session-based interactions                                                                                                                                                          |
|   6 | Authorization in MCP is typically implemented per server, leading to duplication and lack of centralization                                                                                                                                                |
|   7 | Keano: Policy-as-code engine (YAML, CEL), originally for Kubernetes, now supports edge and HTTP/Envoy servers                                                                                                                                              |
|   8 | Agent Gateway: High-performance AI gateway in Rust, supports Kubernetes Gateway API, inference extensions, unified API for multiple providers, supports MCP and A2A protocols, runs standalone or in Kubernetes, supports external authorization (Kyverno) |
|   9 | AI-specific gateway needs: LLM serving, token-based rate limiting, body-based routing, support for new protocols (MCP, A2A)                                                                                                                                |
|  10 | Agent Gateway implements MCP OAuth 2.0, centralizes authentication/authorization, works with existing IDPs, avoids repeated authentication                                                                                                                 |
|  11 | Demo scenario: Without gateway/authorization, agents can apply manifests directly and cause outages                                                                                                                                                        |
|  12 | With Agent Gateway and Kyverno: OAuth 2.0 login via Keycloak, access to tools is checked by Kyverno policies before execution, unauthorized actions (e.g., applying manifest to production) are blocked                                                    |
|  13 | Demo setup: Kind cluster with Agent Gateway, Keycloak, Kyverno, and MCP tools; Gateway API used for routing and policy attachment                                                                                                                          |
|  14 | Kyverno policies: Use Envoy mode for external authorization, parse MCP requests, fetch and analyze YAML from URLs, create Kubernetes SubjectAccessReview for authorization, allow or deny based on RBAC                                                    |
|  15 | Policies can be fine-tuned per tool and metho                                                                                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tEAkoZpdhSc)