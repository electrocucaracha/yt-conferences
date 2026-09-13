---
layout: default
title:
  "Observing Chaos: Real-Time Monitoring of AI-Driven Kubernetes Destr... Josh
  Halley & Ricardo Aravena"
nav_order: 226
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this CubeCon session, Josh Halley and Ricardo present their project
  on chaos engineering using cloud native technologies and AI, specifically demonstrating
  a multiplayer Doom deathmatch played by AI agents. They describe an elaborate arc...
resource: https://www.youtube.com/watch?v=KOM-PQNpcjk
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

In this CubeCon session, Josh Halley and Ricardo present their project on chaos engineering using cloud native technologies and AI, specifically demonstrating a multiplayer Doom deathmatch played by AI agents.
They describe an elaborate architecture involving Kubernetes, PyTorch for model training, and various CNCF projects such as OpenTelemetry for observability, Celium and Hubble for network visibility, and Tetragon for process monitoring.
The system uses a chaos monkey framework to introduce failures and test resilience, while each AI player runs in its own pod with a neural network, and their behaviors and interactions—including "trash talk" generated via GPT Mini—are monitored and visualized through dashboards.
The presenters emphasize the iterative nature of training effective AI behaviors, the importance of observability and explainability, and how these techniques can be applied beyond gaming to real-world distributed systems for improved resilience and insight.
The project was developed primarily by the two presenters, leveraging generative AI tools, and serves as both a technical showcase and a playful demonstration of modern cloud native and AI capabilities.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focused on chaos engineering using cloud native technologies at CubeCon                                                                                              |
|   2 | Josh Halley (Cisco, CNCF TOC) and Ricardo led the session                                                                                                                         |
|   3 | Used Chaos Monkey (originally from Netflix) to introduce failures (CPU, GPU, network, etc.) into systems                                                                          |
|   4 | AI Doom players run as models in Kubernetes pods, trained and served by PyTorch                                                                                                   |
|   5 | Model training used Impala (scaling/distributed learning), ResNet (visual perception), LSTM (memory/context), Noisinet (exploration), and dueling heads (value/action evaluation) |
|   6 | OpenTelemetry used for metrics, traces, logs, and observability                                                                                                                   |
|   7 | MCP server in each pod scrapes player metrics; MCP clients aggregate behaviors via a supervisor module                                                                            |
|   8 | Used Cilium (CNI), Tetragon (runtime process awareness via eBPF), and Hubble (network observability)                                                                              |
|   9 | Up to 16 neural networks per pod, each saving best rewards to a distributed IPFS network for adversarial training                                                                 |
|  10 | ZDoom used as the host pod for multiplayer deathmatch; Kubernetes DNS for pod discovery                                                                                           |
|  11 | Observability dashboards show player stats, frags, MCP communications, and neural network health                                                                                  |
|  12 | Each AI player has a persona; communications and "trash talk" between players facilitated by MCP and GPT Mini                                                                     |
|  13 | Iterative training process: 14+ iterations before achieving effective AI gameplay                                                                                                 |
|  14 | Switched from Docker pods to WebAssembly for faster pod restarts after player deaths                                                                                              |
|  15 | Chaos engine built on top of MCP logic; restarts player "souls" (WebAssembly containers) on frag events                                                                           |
|  16 | Randomizer changes neural network temperature to vary player behavior/persona each game                                                                                           |
|  17 | CNCF projects used: Chaos Mesh, Litmus, Cilium, Tetragon, Hubble, OpenTelemetry                                                                                                   |
|  18 | Emphasized importance of observability, explainability, and metric-driven methodology for AI in production                                                                        |
|  19 | Team size: two main contributors, iterative process, leveraged GenAI tools                                                                                                        |
|  20 | Supervisor module also interacts with GPT Mini for generating player banter                                                                                                       |
|  21 | Explored potential for team-based/co-op modes and security (red/blue team) ana                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=KOM-PQNpcjk)
