---
layout: default
title: "Agent Governance Lives in the OS - Alexander Sklar & Roberth Karman, Microsoft"
nav_order: 30
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "At the governance conference, Robert Karman and Alexander Sklar argue that operating systems must serve as the primary enforcers of security policies for AI agents, rather than relying on the agent..."
resource: "https://www.youtube.com/watch?v=QcRXgSNsgb4"
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

At the governance conference, Robert Karman and Alexander Sklar argue that operating systems must serve as the primary enforcers of security policies for AI agents, rather than relying on the agents to self-police their behavior.
They propose a model where IT administrators define strict boundaries and resource limits, which the OS then enforces at the kernel level to prevent agents from accessing sensitive data like SSH keys, regardless of the agent's intent or instructions.
This approach requires that agents possess non-spoofable identities and that sandbox permissions remain immutable and never broaden over time, ensuring that child processes inherit the same restrictions as their parent.
The speakers emphasize that this governance framework applies to all execution paths, including when agents operate within their own processes, and they have introduced Microsoft Execution Containers (MXC) as a cross-platform technology to facilitate these secure, governed environments.
Finally, they call for a collaborative ecosystem where OS vendors, AI gateways, agent developers, and IT administrators work together to establish standardized primitives, aiming to create trustworthy agentic workflows that can be safely deployed in production environments.

# Main Points

|   # | Main point                                                                                                                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                                                                            |
|   2 | • Users on devices now include agents acting on behalf of humans, requiring governance of agent actions                                                                                                                                                 |
|   3 | • Agents should choose how to work, but policies on what they can do must be decided externally, not by agents                                                                                                                                          |
|   4 | • Operating systems should enforce governance through resource boundaries without the agent deciding its own authority level                                                                                                                            |
|   5 | • Governance requires three principles: agent identity, delegation metadata for attribution, and policies from outside the agent                                                                                                                        |
|   6 | • When agents ask for permissions, the OS can deny requests that violate policies and agents can adjust their approach                                                                                                                                  |
|   7 | • Sandboxes have two failure points: creation (OS can block overly permissive sandboxes) and runtime (sandbox enforces restrictions on tool access)                                                                                                     |
|   8 | • Sandbox permissions must never change during execution; additional permissions require creating a new sandbox                                                                                                                                         |
|   9 | • Child processes must inherit parent sandbox restrictions; cannot escape to gain wider permissions                                                                                                                                                     |
|  10 | • Agent identity must be unforgeable and combine agent type with the user on whose behalf it works                                                                                                                                                      |
|  11 | • Policies must apply regardless of execution method (sandbox or direct file access in agent's own process)                                                                                                                                             |
|  12 | • Microsoft released MXC (Microsoft Execution Containers), a cross-platform sandbox technology for macOS, Linux, and Windows                                                                                                                            |
|  13 | • Identity must persist across boundaries and cannot change from one agent-user combination to another                                                                                                                                                  |
|  14 | • Ecosystem roles: OS providers implement enforcement primitives; AI gateway providers use those primitives; agent providers request minimum scope; tool providers define requirements; IT administrators create policies based on organizational needs |
|  15 | • Goal is better-governed agent workflows for production environments, not just better-governed containers                                                                                                                                              |
|  16 | • Collaboration needed across industry to build this governance framework                                                                                                                                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/QcRXgSNsgb4/hqdefault.jpg)]("https://www.youtube.com/watch?v=QcRXgSNsgb4")

[Watch on YouTube](https://www.youtube.com/watch?v=QcRXgSNsgb4)
