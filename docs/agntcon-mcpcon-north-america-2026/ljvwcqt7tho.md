---
layout: default
title: "Making Swarm Work: Coordination Primitives for Decentralized Multi-Agent... - Jodee Varney, Cisco"
nav_order: 22
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker presents Mycelium, an open-source project developed by Outshift to facilitate peer-to-peer agent collaboration, distinct from traditional orchestrator-sub-agent models."
resource: "https://www.youtube.com/watch?v=lJVWCQt7Tho"
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

The speaker presents Mycelium, an open-source project developed by Outshift to facilitate peer-to-peer agent collaboration, distinct from traditional orchestrator-sub-agent models.
The system is designed to address challenges in long-running tasks and multi-party scenarios by implementing three core principles: shared intent, shared context, and shared reasoning.
To achieve this, Mycelium provides foundational "plumbing" such as shared rooms, task boards, and persistent memory, alongside specialized coordination engines.
Key among these are the Accord and Concord protocols, which use deterministic code rather than AI models to ensure agents align on task definitions and negotiate decisions through structured voting and iterative refinement.
The speaker demonstrates these capabilities using a contract renewal scenario, showing how agents with conflicting objectives can reach a consensus that all parties accept.
While the project remains experimental and assumes trusted agents, it offers a practical starting point for building scalable, decentralized agent swarms, with the team actively inviting community contributions to expand its coordination primitives.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                   |
|   2 | • Speaker is Product Manager at Outshift (Cisco); works on internet of Cognition project and Mycelium open-source project built by Julia Valenti                                               |
|   3 | • Focus on agent swarms that function as peers rather than hierarchical subagents with central coordinator                                                                                     |
|   4 | • Mycelium is a testbed/playground for deploying and testing coordination primitives for multi-agent systems                                                                                   |
|   5 | • Three fundamental requirements for agent collaboration: shared intention, shared context, shared reasoning                                                                                   |
|   6 | • Three common failure modes in multi-agent systems: agents assuming unasked goals, unverified facts propagating, false consensus                                                              |
|   7 | • Peer-to-peer agent model differs from orchestrator model (where one agent delegates to subagents); peers coordinate directly without central control                                         |
|   8 | • Swarms appropriate when: representing multiple stakeholders, legitimately conflicting objectives, partial knowledge distribution, flexible membership, or crossing organizational boundaries |
|   9 | • Mycelium infrastructure includes: rooms with members, task tracking boards, shared state, shared memory in Markdown, mentions and turns for waking agents                                    |
|  10 | • Three coordination engines built into Mycelium: Accord protocol (aligning task understanding), Concord protocol (negotiation/decision-making), Aligner tool                                  |
|  11 | • Conductor executes fixed scripts with deterministic steps; agents provide content but code determines process flow and next steps                                                            |
|  12 | • Concord decision rule: choose option with highest minimum score across all agents, preventing majority from overriding single dissenting agent                                               |
|  13 | • All coordination results saved to shared memory for permanent reference                                                                                                                      |
|  14 | • Open questions: token efficiency, agent trust/authentication, scalability, need for additional coordination primitives                                                                       |
|  15 | • Mycelium is open-source; accepts contributions via pull requests and issues                                                                                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/lJVWCQt7Tho/hqdefault.jpg)]("https://www.youtube.com/watch?v=lJVWCQt7Tho")

[Watch on YouTube](https://www.youtube.com/watch?v=lJVWCQt7Tho)
