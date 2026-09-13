---
layout: default
title:
  "Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google
  & Evaline Ju, IBM"
nav_order: 18
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Hayen from Google and Evelyn Ju from IBM introduce the
  Kubernetes Agentic Networking subproject, which aims to provide standardized APIs
  for secure, governed communication among AI agents, tools, and language models within...
resource: https://www.youtube.com/watch?v=KXmPxmNN0fc
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

In this session, Hayen from Google and Evelyn Ju from IBM introduce the Kubernetes Agentic Networking subproject, which aims to provide standardized APIs for secure, governed communication among AI agents, tools, and language models within Kubernetes environments.
The project focuses on creating persistent APIs that remain relevant as AI protocols evolve, supporting robust authorization, authentication, and auditable traffic management.
They demonstrate new experimental CRDs—XBackend and XAccessPolicy—that enable fine-grained control over which agents can access specific tools, including allow lists and external authorization integration.
The reference implementation uses Envoy as the data plane and an agentic net controller for configuration, with a live demo illustrating how access policies can restrict or permit agent-tool interactions.
The session also discusses ongoing work on observability and tracing using OpenTelemetry, proposals for standardized telemetry and guardrails to prevent data breaches, and outlines future plans such as deny lists, expanded authorization scenarios, and collaboration with the AI Gateway Working Group, inviting community participation and feedback.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Topic: Agentic networking for securing AI agents on Kubernetes                                                                                                      |
|   2 | Presenters: Hayen (Google), Evelyn Ju (IBM)                                                                                                                         |
|   3 | Cube agentic networking is a SIG Network subproject                                                                                                                 |
|   4 | Goal: Standardized API for secure, governed communication between AI agents, tools, and LLMs                                                                        |
|   5 | Supports ingress, egress, and east-west traffic                                                                                                                     |
|   6 | Focus on user-facing goals, not tied to specific AI protocols                                                                                                       |
|   7 | APIs designed to persist as protocols evolve                                                                                                                        |
|   8 | Security/governance: authorization policies, external auth, authentication, auditable traffic management                                                            |
|   9 | Alignment with existing APIs, protocols, and working groups (e.g., Gateway API, Gateway Inference Extension)                                                        |
|  10 | Personas:                                                                                                                                                           |
|  11 | AI engineer: assign agent identities, audit actions, understand tool call denials/allowances                                                                        |
|  12 | Platform engineer: default-deny agent traffic, control tool access, observe failures/denials                                                                        |
|  13 | Security engineer: pre/post filtering, prevent prompt injection/data breaches                                                                                       |
|  14 | Implementation:                                                                                                                                                     |
|  15 | Kubernetes cluster with AI agent and two MCP servers (local and remote)                                                                                             |
|  16 | By default, agent can access all tools                                                                                                                              |
|  17 | Introduced agentic net gateway and two new CRDs: XBackend and XAccessPolicy (experimental)                                                                          |
|  18 | XBackend defines MCP backend; XAccessPolicy targets backend/gateway with rules (e.g., allow list)                                                                   |
|  19 | Default-deny achieved by empty allow list; allow specific tools by adding to allow list                                                                             |
|  20 | Supports external authorization and common expression language                                                                                                      |
|  21 | Reference implementation uses Envoy as data plane, agentic net controller as control plane                                                                          |
|  22 | Demo: Showed namespace setup, gateway API resources, agent tool access, applying access policies to allow/deny tool calls                                           |
|  23 | Tracing proposal: GenAI OpenTelemetry semantic conventions for tracing agent/gateway/tool calls and policy decisions                                                |
|  24 | Observability: Instrumentation at agent, gateway, tool server levels; spans collected via OpenTelemetry collector; supports multiple backends (e.g., Tempo, Jaeger) |
|  25 | Telemetry policy proposal: Configure signals (traces, metrics, logs) acros                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=KXmPxmNN0fc)
