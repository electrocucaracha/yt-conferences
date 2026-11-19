---
layout: default
title: "Workshop: Keep Infrastructure Out of Your AI Agents and MCP... - Lin Sun & Christian Posta, Solo.io"
nav_order: 41
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Lin Sun and Christian Posta from Solo.io led an interactive workshop at AgentCon, introducing the Agent Gateway project as a specialized proxy for mediating traffic between AI agents, MCP servers, ..."
resource: "https://www.youtube.com/watch?v=US_aAT7-mUE"
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

Lin Sun and Christian Posta from Solo.io led an interactive workshop at AgentCon, introducing the Agent Gateway project as a specialized proxy for mediating traffic between AI agents, MCP servers, and LLMs.
They explained that while traditional proxies like Envoy are optimized for fast request-response cycles, AI workloads require deep inspection of request bodies, streaming support, and complex policy enforcement, which led to the development of Agent Gateway as a distinct solution now donated to the Linux Foundation.
The session included a hands-on lab where participants configured the gateway to provide critical infrastructure capabilities such as token-based rate limiting, budget control, distributed tracing via Jaeger, and MCP server multiplexing without modifying the underlying agent or server code.
Additionally, the presenters demonstrated advanced security features, including prompt injection guardrails, credential injection for API calls, and MCP authentication using JWTs, highlighting how the gateway centralizes governance, observability, and security to keep AI infrastructure components decoupled from application logic.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : The session, led by Lin Sun (Head of Open Source) and Christian Posta (Global Field CTO) at Solo.io, focuses on the Agent Gateway pattern to mediate traffic between AI agents, MCP servers, and LLMs.                                                               |
|   2 | : Similar to microservices proxies, Agent Gateway keeps infrastructure concerns (security, policy, observability, traffic control) outside of AI agents and MCP servers, allowing them to focus on business logic.                                                     |
|   3 | : Traditional proxies like Envoy were designed for fast request/response cycles. AI traffic requires inspecting large request bodies, handling long-running streaming responses, and managing bidirectional communication (MCP), which standard proxies handle poorly. |
|   4 | : Built from the ground up in Rust to address AI-specific challenges. It was donated to the Linux Foundation and later the Agentic AI Foundation (AAIF), reaching 60–70 million downloads.                                                                             |
|   5 | :                                                                                                                                                                                                                                                                      |
|   6 | : Mediates traffic to local (Llama) or remote (Gemini) models, providing credential injection and unified endpoints.                                                                                                                                                   |
|   7 | & Rate Limiting**: Enforces token limits (e.g., 5,000 tokens) and returns HTTP 429 errors when exhausted, with visibility in the UI.                                                                                                                                   |
|   8 | : Aggregates multiple MCP servers (Trend, Workspace, Publish) into a single endpoint, exposing all tools to the agent.                                                                                                                                                 |
|   9 | : Reduces context bloat by filtering available tools based on authorization policies.                                                                                                                                                                                  |
|  10 | : Integrates with Jaeger for distributed tracing of agent-to-MCP and agent-to-LLM interactions without code changes.                                                                                                                                                   |
|  11 | : Detects and masks prompt injection attempts in responses to prevent malicious agent behavior.                                                                                                                                                                        |
|  12 | : Transforms legacy OpenAPI specifications into MCP tools, including credential injection for authenticated calls (e.g., GitHub rate limits).                                                                                                                          |
|  13 | : Enforces JWT-based authentication and authorization for MCP tools using an IDP (Keycloak/Okta compatible), supporting optional or strict modes.                                                                                                                      |
|  14 | : Recommends avoiding long-lived API keys in favor of identity-based tokens (OAuth/OIDC) and workload identity. Supports RFC 8693 token exchange for "on-behalf-of" scenarios where agents act for users.                                                              |
|  15 | : Uses CEL (Common Expression Language) for dynamic policy enforcement and authorization. Supports external policy engines like OPA or Cedar via dynamic modules.                                                                                                      |
|  16 | : Most policies (rate limiting, auth, routing) are dynamically updatable without restarting the gateway.                                                                                                                                                               |
|  17 | : Uses Python agents, Docker for Jaeger, and a local Llama model or Gemini API. The "Trend Watch" repository provides all necessary configurations and code.                                                                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/US_aAT7-mUE/hqdefault.jpg)](https://www.youtube.com/watch?v=US_aAT7-mUE)

[Watch on YouTube](https://www.youtube.com/watch?v=US_aAT7-mUE)
