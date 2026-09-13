---
layout: default
title: "MCP Gateways: The Control Plane for Agentic Integration - Alex Salazar, Arcade.dev"
nav_order: 55
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker discusses the major challenges facing AI agents in enterprise
  environments, emphasizing the need for robust authorization, tool quality, observability,
  and configuration portability. Current approaches—using service accounts or...
resource: https://www.youtube.com/watch?v=DxZ4mlSRcOc
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses the major challenges facing AI agents in enterprise environments, emphasizing the need for robust authorization, tool quality, observability, and configuration portability.
Current approaches—using service accounts or user credentials—either create security vulnerabilities or limit agent usefulness.
The proposed solution is a control plane, or MCP gateway, that enforces policy by intersecting agent and user permissions on every request, ensuring agents can only perform authorized actions.
This architecture separates the reasoning and action layers, centralizes governance, and enables scalable, secure, multi-user agent deployments.
The speaker demonstrates how this system works in practice, highlighting the importance of centralized policy enforcement, tool curation, and audit trails, and addresses questions about integration, policy management, and future developments in agent control and security.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MCP and working groups prioritized enterprise readiness for agents by 2026, focusing on gateway patterns, audit trails, config portability, and enterprise authorization. |
|   2 | Agents must move beyond simple RAG systems to perform real actions like workflow automation, CRM updates, and sending emails.                                             |
|   3 | Key challenges for production agents: authorization, tool quality, observability, and auditability.                                                                       |
|   4 | Authorization is a major unsolved problem; current models (service accounts, user credentials) have significant flaws.                                                    |
|   5 | Service accounts create authorization bypass vulnerabilities; reducing agent permissions lowers ROI.                                                                      |
|   6 | Using user credentials is more secure but complicates multi-user scenarios and increases error risk.                                                                      |
|   7 | The ideal model is intersectional authorization: agent and user permissions are combined at runtime for each request.                                                     |
|   8 | Existing authentication systems (e.g., Okta, Ping, Entra) solve authentication, not authorization or policy enforcement for agents.                                       |
|   9 | Agents are non-deterministic and cannot be trusted to enforce their own policies; enforcement must occur on every action request.                                         |
|  10 | An actions runtime (MCP gateway) should separate agent and user identity, curate tools, enforce authorization, and provide audit trails.                                  |
|  11 | Centralized control planes are necessary for managing identity, observability, endpoint management, and governance across agents.                                         |
|  12 | MCP tools (agentic connectors) and skills (procedural workflows) should be layered for reusable, centrally managed agent capabilities.                                    |
|  13 | Tool curation, authorization depth, and multi-user support are critical for scalable, secure agent deployment.                                                            |
|  14 | Observability and audit trails are essential for security, compliance, and troubleshooting.                                                                               |
|  15 | Centralized configuration and governance of agent access to business systems is required; agents should not manage connectivity/security details.                         |
|  16 | Policy enforcement should integrate with existing enterprise identity and policy systems, not create new silos.                                                           |
|  17 | Author                                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=DxZ4mlSRcOc)
