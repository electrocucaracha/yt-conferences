---
layout: default
title: "Keynote: Shipping Autonomous Agents Safely with Open Standards,... - Rao Surapaneni, Google"
nav_order: 118
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: The speaker emphasizes that enterprises are currently at an inflection point where governance and infrastructure must mature to unlock the full potential of AI agents in production environments.
resource: "https://www.youtube.com/watch?v=7vnPC2dtgNc"
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

The speaker emphasizes that enterprises are currently at an inflection point where governance and infrastructure must mature to unlock the full potential of AI agents in production environments.
To address the complexity and management overhead caused by rapid technological change and agent sprawl, the presentation highlights the release of the Agent Compute Engine, a secure, sandboxed micro-VM infrastructure designed for long-running agents with sub-second hydration capabilities.
Additionally, enhanced agent governance capabilities were introduced to provide a unified view for managing agents across various environments, including Google Cloud, cross-cloud, and self-hosted systems.
These governance features encompass critical components such as identity management, registries for skills and plugins, enterprise policy enforcement, and comprehensive observability to ensure safety, security, and cost control.
The speaker concludes by recommending best practices for enterprise resilience, including demanding standard interfaces, federating identity, owning agent policies enforced via gateways, and implementing evaluations for all agent actions to maintain agility and control.

# Main Points

|   # | Main point                                                                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , marking an inflection point where governance and infrastructure are critical for unlocking enterprise potential.                                                                                                            |
|   2 | , the current AI landscape is capability-first, with models and applications scaling rapidly while governance and safety measures lag behind.                                                                                 |
|   3 | , logarithmic pace of organizational deployment, often due to missing people, technology, or governance layers.                                                                                                               |
|   4 | "agent sprawl" and increased complexity and management overhead due to the variety of supporting platforms, APIs, MCPs, and CLIs.                                                                                             |
|   5 | , including multimodal Gemini applications and the availability of GPT-6 on Model Garden, making it the only hyperscaler with all three frontier models and open-weight models in one place.                                  |
|   6 | , featuring micro VMs with sub-second hydration, secure sandboxing, and operation at planet scale to handle the bursty activity of long-running, dormant agents.                                                              |
|   7 | , cross-cloud, self-hosted, or local environments, addressing safety, security, and cost management in a single pane of glass.                                                                                                |
|   8 | : identity (agent, user, or delegated), registry (for skills, plugins, and agents), enterprise policies (vendor-agnostic), and observability (monitoring runtime actions and costs).                                          |
|   9 | (data plane), which enables the implementation of a kill switch to stop rogue agents.                                                                                                                                         |
|  10 | "homework" drill for organizations is to test the ability to quickly swap models, harnesses, or agents while retaining memory and user context, which serves as a true test of organizational readiness for agentic autonomy. |
|  11 | , enterprises should own the governance layer and control plane while standardizing interactions with models, skills, and agents.                                                                                             |
|  12 | , understanding agent traces, federating identity across interoperating systems, owning and enforcing agent policies via gateways, and implementing evaluations for everything.                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7vnPC2dtgNc/hqdefault.jpg)]("https://www.youtube.com/watch?v=7vnPC2dtgNc")

[Watch on YouTube](https://www.youtube.com/watch?v=7vnPC2dtgNc)
