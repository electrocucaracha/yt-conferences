---
type: Video Note
title: "Securing AI Agent Infrastructure: AuthN/AuthZ Patterns for MCP and A2A - Yoshiyuki Tabata"
description: "Yoshik Tabata’s session focuses on securing AI agent infrastructure through practical authentication and authorization patterns, specifically for MCP (agent-to-tool communication) and A2A (agent-to-agent communication). He explains how MCP..."
resource: https://www.youtube.com/watch?v=S6qF0N5D1tM
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Yoshik Tabata’s session focuses on securing AI agent infrastructure through practical authentication and authorization patterns, specifically for MCP (agent-to-tool communication) and A2A (agent-to-agent communication).
He explains how MCP and A2A standardize interactions among AI agents, reducing integration complexity and improving security, with MCP relying on OAuth 2.1 authorization code flow and A2A supporting various credential types.
Drawing on principles from an upcoming CNCF white paper, he outlines two security patterns—basic (suitable for limited exposure and non-sensitive data) and advanced (for sensitive data and public networks, enforcing zero trust with mutual TLS and token exchange).
Tabata demonstrates implementing these patterns using open-source tools Keycloak (for identity and access management) and SPIRE (for workload identity), showing how robust authentication and authorization can be achieved in cloud-native environments.
The session concludes with a Q&A discussing challenges in enterprise scenarios, such as token forwarding and integrating external services.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter: Yoshik Tabata from Joso, senior consultant at Hitachi, specializing in API and identity security.                                                                                                                                                       |
|   2 | Session topic: Securing AI agent infrastructure with authentication and authorization patterns for MCP and A2A.                                                                                                                                                    |
|   3 | Focus: Practical patterns grounded in CNCF IAM white paper, mapped to real-world implementations using Keycloak and Spire.                                                                                                                                         |
|   4 | MCP (Managed Control Plane): Standardizes agent discovery and context exchange with external tools/services.                                                                                                                                                       |
|   5 | MCP requires agents to use OAuth 2.1 authorization code flow to obtain access tokens.                                                                                                                                                                              |
|   6 | MCP authorization flow: agent sends request without token → receives 401 → retrieves resource metadata → obtains authorization server metadata → dynamic registration (if needed) → uses OAuth 2.0 code flow to get access token → accesses MCP server with token. |
|   7 | A2A (Agent-to-Agent): Standardizes agent discovery and communication; supports OAuth tokens, API keys, and other credentials; simpler flow than MCP.                                                                                                               |
|   8 | MCP is typically for agent-to-tool communication; A2A for agent-to-agent.                                                                                                                                                                                          |
|   9 | Security risk: A2A with weaker credentials (e.g., API keys) can be a weak link; should align with OAuth 2.1 assurance.                                                                                                                                             |
|  10 | CNCF IAM white paper: Defines authentication/authorization requirements for cloud-native environments; introduces basic and advanced security patterns.                                                                                                            |
|  11 | Authentication requirements: user and workload authentication; based on standards like OAuth 2.0, OIDC, SPIFFE, NIST SP 800-63.                                                                                                                                    |
|  12 | API security risks: Broken authentication/authorization are top threats per OWASP API Security Top 10.                                                                                                                                                             |
|  13 | Basic pattern: Trusts all workloads inside cluster; security enforced at perimeter; suitable for limited exposure/nonsensitive data.                                                                                                                               |
|  14 | Advanced pattern: Zero trust; mutual TLS (mTLS) between workloads; token exchange; authorization at each workload; suitable for sensitive data/public exposure.                                                                                                    |
|  15 | Five key IAM principles: mutual TLS, OAuth token exchange, OIDC client authentication with SPIFFE, OAuth access token validation, PDP-based authorization.                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=S6qF0N5D1tM)