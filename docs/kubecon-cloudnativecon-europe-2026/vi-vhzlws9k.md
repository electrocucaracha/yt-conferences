---
type: Video Note
title: "Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution... Mingshan Zhao & Zhen Zhang"
description: "The speakers, developers from Alibaba Cloud’s container service team, discuss the challenges and solutions for deploying AI agent applications on Kubernetes, particularly as more AI scientists—often new to Kubernetes—seek large-scale, low-l..."
resource: https://www.youtube.com/watch?v=vi_VhZLWs9k
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speakers, developers from Alibaba Cloud’s container service team, discuss the challenges and solutions for deploying AI agent applications on Kubernetes, particularly as more AI scientists—often new to Kubernetes—seek large-scale, low-latency deployments.
They introduce the Open Cruise Agent, a container-based agent sandbox solution that extends Kubernetes with custom resources for managing sandbox lifecycles, including states like pause, resume, and checkpoint, to address issues of data security, isolation, scalability, and cost control.
The Open Cruise Agent integrates with community standards such as E2B and MCP, supports rapid sandbox provisioning through warm pools, and enables dynamic storage mounting and in-place image updates to efficiently handle diverse workloads.
Key technologies include secure container runtimes, sandbox gateways for network security, and mechanisms for pausing, resuming, and checkpointing sandboxes to optimize resource usage and support robust state management.
The team emphasizes ongoing collaboration with the community to standardize sandbox lifecycle APIs and outlines future plans for universal sandbox runtimes and improved cost efficiency.
# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Alibaba Cloud container service team has been helping users deploy AI agent applications on Kubernetes.                                                              |
|   2 | Many new users are AI scientists unfamiliar with Kubernetes.                                                                                                         |
|   3 | Key business challenges for agent sandbox with containers: data security, massive agent scale, state management, and cost control.                                   |
|   4 | Data security is critical as agents access and run user code, which must be isolated to prevent malicious actions.                                                   |
|   5 | The number of agents is growing exponentially, requiring scalable solutions.                                                                                         |
|   6 | Sandboxes have varying lifecycles; keeping them alive is costly, so efficient state management is needed.                                                            |
|   7 | Sandbox lifecycle divided into six states: pending, running, complete (Kubernetes-native), plus pause, resume, and checkpoint for cost and state management.         |
|   8 | Regular Kubernetes pods cannot directly handle sandbox requirements.                                                                                                 |
|   9 | Open Cruise Agent is introduced as a custom resource to manage sandboxes, extending Kubernetes capabilities.                                                         |
|  10 | Open Cruise Agent supports integration with community standards like E2B and MCP.                                                                                    |
|  11 | Platform developers can use custom resources: SandboxClaim and SandboxSet, supporting dynamic updates and volume mounts.                                             |
|  12 | Open Cruise Agent is open source, originating from Alibaba’s large-scale practices.                                                                                  |
|  13 | Core capabilities: sandbox manager compatible with E2B and MCP, sandbox lifecycle management, and warm pool to reduce cold start time.                               |
|  14 | Future features: checkpoint and restore for efficient sandbox reuse and parallelism.                                                                                 |
|  15 | Open Cruise Agent design is driven by real-world requirements for large-scale, low-latency AI agent workloads.                                                       |
|  16 | Ecosystem integration includes reinforcement learning (e.g., VI training framework) and OpenCL deployment acceleration.                                              |
|  17 | Key technologies: warm pool of sandboxes, in-place image update, dynamic storage mounting, pause/resume, checkpoint/restore, and sandbox gateway for secure traffic. |
|  18 | Warm pool reduces cold start latency to ~20ms, supporting high QPS and rapid sandbox provisioning.                                                                   |
|  19 | Pause/resume deletes idle pods                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vi_VhZLWs9k)