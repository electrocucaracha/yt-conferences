---
layout: default
title: "WG-Batch Updates: What’s New and What Is Next? - Marcin Wielgus, Google"
nav_order: 362
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The batch working group aims to enhance Kubernetes support for high-performance
  computing, AI, and machine learning workloads. Q is a workload-level scheduler that
  operates on CS and holds, determining when to start or stop workloads, and s...
resource: https://www.youtube.com/watch?v=aWxuaEFSarU
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The batch working group aims to enhance Kubernetes support for high-performance computing, AI, and machine learning workloads.
Q is a workload-level scheduler that operates on CS and holds, determining when to start or stop workloads, and supports gang scheduling semantics.
It also manages resource quotas, maximizes cluster utilization, and supports specialized hardware.
The group has launched several projects, including QCTL for day-to-day operations, APIs for job management, and K jobs for easy submission of batch workflows.
These tools aim to provide a cohesive ecosystem for batch workloads in Kubernetes, making it easier for users to manage complex workflows and leverage the power of Kubernetes.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The goal of the group is to reduce fragmentation in the Kubernetes ecosystem.                                                                     |
|   2 | Q (pronounced "cue") is an AI HPC batch workload level scheduler that operates on workloads, not individual pods.                                 |
|   3 | Q determines when to start, stop, or preempt workloads and supports all-or-nothing scheduling semantics.                                          |
|   4 | Q can run workloads on specific machines with accelerators, reservations, or spot instances.                                                      |
|   5 | The group has bi-weekly meetings in European and West Coast Pacific time zones.                                                                   |
|   6 | Topology-aware scheduling allows for more efficient utilization of cluster resources by grouping pods on the same switch together.                |
|   7 | Fair sharing ensures that unused capacity is distributed fairly among teams based on their historical usage.                                      |
|   8 | QCTL (pronounced "cue-tel") is a tool to perform day-to-day operations on Q, such as creating cues and managing workloads.                        |
|   9 | Job set is an API for managing groups of jobs as a unit, offering unified policies around starting, stopping, and restarting failures.            |
|  10 | K-Jobs are reusable job templates stored in the API server with a command-line interface that transforms them into full YAML files for execution. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aWxuaEFSarU)
