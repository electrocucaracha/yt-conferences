---
layout: default
title: "Beyond Static DAGs: Orchestrating AI-Generated Multi-Agent Workflows - Cong Wang, Agentry Inc"
nav_order: 148
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Kungwa, founder and CEO of Agentree, presents a new project designed to enable multi-agent workflows across organizations, specifically targeting complex business-to-business scenarios like supply ..."
resource: "https://www.youtube.com/watch?v=z34nlPEJ_5c"
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

Kungwa, founder and CEO of Agentree, presents a new project designed to enable multi-agent workflows across organizations, specifically targeting complex business-to-business scenarios like supply chain management.
He argues that existing solutions such as Kubernetes, agent frameworks, and protocols like A2A and MCP are insufficient for cross-organizational coordination, as they lack the necessary trust, reliability, and workflow capabilities.
To address this, Agentree introduces a gateway that treats all interactions as messages, utilizing a new protocol called AMTP, which is analogous to email but built for AI agents.
AMTP borrows concepts from email, such as addresses for agent identification, but replaces unstructured SMTP with reliable HTTP and JSON transport, while incorporating domain signatures for security and verification.
The system features three coordination primitives—parallel, sequential, and conditional workflows—that allow for robust plan execution, policy enforcement, and failure handling, ensuring that even if an AI agent makes an error, the gateway can enforce organizational policies.
Agentree is open-source, built on standard HTTP infrastructure for easy integration, and aims to provide a secure, reliable, and standardized way for AI agents to collaborate across organizational boundaries.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | : Agentree is a new project presenting a gateway for multi-agent workflows, targeting cross-organization AI agent deployment, specifically for business-to-business scenarios like purchasing and supply chains.                                                                                                   |
|   2 | : Existing AI agents are mostly deployed within single organizations. Current solutions like Kubernetes, Kubeflow, agent frameworks, A2A, and MCP are insufficient for cross-organizational coordination, lacking dynamic workflows, agent-specific identification, or reliable multi-agent coordination.          |
|   3 | : Agentree acts as a message gateway for organizations, similar to an email gateway. It handles all communication between agents, vendors, and customers, treating every interaction, including workflows, as a message.                                                                                           |
|   4 | : The Agent Message Transfer Protocol (AMTP) is designed for AI agents, analogous to email for humans. It borrows concepts from email (addresses for agent identification, DNS MX records for discovery, domain signatures for verification) but replaces unstructured SMTP with reliable HTTP and JSON transport. |
|   5 | : The gateway guarantees at-least-once delivery and retries. Trust is established through domain signatures, where senders sign messages with private keys and receivers verify them with public keys to ensure authenticity.                                                                                      |
|   6 | : Agentree implements three combinable coordination primitives for workflows:                                                                                                                                                                                                                                      |
|   7 | : For simultaneous tasks, such as collecting quotes from multiple suppliers.                                                                                                                                                                                                                                       |
|   8 | : For ordered processes, such as legal and finance approvals.                                                                                                                                                                                                                                                      |
|   9 | : For logic-based routing, such as requiring additional approval if a budget threshold is exceeded.                                                                                                                                                                                                                |
|  10 | : Workflows are initiated by planner agents (e.g., triggered by low inventory), execute via deployed agents (finance, legal, negotiation), and conclude when deals are closed. The gateway manages failure handling, retries, and agent offline scenarios.                                                         |
|  11 | : The gateway can enforce organizational policies independently of the AI agent. If an agent’s plan violates a rule (e.g., missing required approval), the gateway denies the message, preventing errors from propagating.                                                                                         |
|  12 | : The gateway is positioned to provide shared context between agents across different organizations, a feature currently in progress.                                                                                                                                                                              |
|  13 | : Built on HTTP and JSON, AMTP is easy to integrate for developers familiar with standard web technologies. It is recommended for cross-organizational scenarios, while single-organization use cases may still prefer standard frameworks.                                                                        |
|  14 | : Core features and workflow primitives are available. Future plans include policy checks and an SMTP bridge to allow human-in-the-loop via traditional email. The project is open-source, with the protocol and gateway built-in public.                                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/z34nlPEJ_5c/hqdefault.jpg)](https://www.youtube.com/watch?v=z34nlPEJ_5c)

[Watch on YouTube](https://www.youtube.com/watch?v=z34nlPEJ_5c)
