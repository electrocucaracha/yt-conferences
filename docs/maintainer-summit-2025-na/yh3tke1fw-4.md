---
layout: default
title: "Node Lifecycle WorkingGroup - Getting Started - Ryan Hallisey, NVIDIA & Filip Křepinský, Red Hat"
nav_order: 15
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "Philip Chapinsky from Red Hat and Ryan Hisy from Nvidia introduced the new Kubernetes Node Life Cycle working group, aiming to improve observability and coordination between pod and node lifecycle ..."
resource: "https://www.youtube.com/watch?v=yh3tkE1fw-4"
tags:
  - maintainer-summit-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T17:23:58+00:00
---

# Summary

Philip Chapinsky from Red Hat and Ryan Hisy from Nvidia introduced the new Kubernetes Node lifecycle working group, aiming to improve observability and coordination between pod and node lifecycle management.
They highlighted significant gaps in the current ecosystem, such as the lack of a canonical way to communicate node states (e.g., drained or under maintenance) and the fragmentation of tools that handle disruptions, evictions, and graceful shutdowns.
To address these issues, the group proposed an Eviction Request API that allows controllers to declaratively manage pod termination through interceptors, enabling more graceful scaling and migration before final deletion.
Additionally, they discussed efforts to standardize declarative node maintenance and specialized lifecycle management to reduce complexity and improve interoperability across various infrastructure projects.
The working group seeks community feedback and use cases to refine these proposals, with the ultimate goal of creating a cohesive, natively supported framework for managing node and pod lifecycles that can accommodate evolving concepts like virtual nodes and device-level resource management.

# Main Points

|   # | Main point                                                                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Node lifecycle working group, led by Philip Chapinsky from Red Hat and Ryan Hisy from Nvidia, aims to improve Pod and Node lifecycle management through better observability and cross-component cooperation.          |
|   2 | Current Pod observability methods, such as Pod phases, are insufficient for representing the full lifecycle, hindering effective interaction between higher-level workloads and the Kubernetes control plane.              |
|   3 | Scheduling issues arise when kube-scheduler lacks complete node information, leading to Pod failures and churn; solutions include adding node information or implementing dynamic rescheduling.                            |
|   4 | Pod disruption mechanisms, such as deletion and API-initiated eviction, are often too late to allow for graceful handling, causing issues with complex scenarios like migration or stateful applications.                  |
|   5 | The Eviction Request API proposal introduces declarative eviction with action interceptors, allowing controllers to manage disruption intent, track progress, and implement graceful termination with deadlines.           |
|   6 | Node lifecycle management faces challenges in observability, such as determining if a node is drained, leading to ecosystem fragmentation with various projects using different methods like labels, annotations, or CRDs. |
|   7 | Real-world scenarios, such as GPU driver failures requiring reboots at scale, highlight the need for a canonical API to coordinate node maintenance and drain states effectively.                                          |
|   8 | The working group is focusing on declarative node maintenance and specialized lifecycle management to provide a unified way to describe node states and enable interoperability between different tools.                   |
|   9 | Community feedback suggests that some lifecycle concepts should be pushed down to generic API machinery, while others remain specific to nodes, to reduce complexity and duplication of effort.                            |
|  10 | The future of node abstraction may evolve to include virtual nodes, clusters of nodes, or decomposed components like devices, requiring lifecycle management to adapt to these changing definitions.                       |
|  11 | The working group seeks more use cases and collaboration from the community to refine proposals and ensure solutions are broadly applicable and natively supported in Kubernetes.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/yh3tkE1fw-4/hqdefault.jpg)](https://www.youtube.com/watch?v=yh3tkE1fw-4)

[Watch on YouTube](https://www.youtube.com/watch?v=yh3tkE1fw-4)
