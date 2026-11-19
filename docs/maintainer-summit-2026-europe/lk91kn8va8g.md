---
layout: default
title: "Guide Us on Next Steps in Kubernetes Device Manage... John B, Janet K, Marlow W, Patrick O & Kevin K"
nav_order: 8
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "This community discussion, led by the Kubernetes Device Management Working Group, reviews the progress of Dynamic Resource Allocation (DRA) and outlines critical priorities for the next year."
resource: "https://www.youtube.com/watch?v=LK91kn8vA8g"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

This community discussion, led by the Kubernetes Device Management Working Group, reviews the progress of Dynamic Resource Allocation (DRA) and outlines critical priorities for the next year.
Key upcoming initiatives include integrating DRA with workload-aware scheduling to enable gang scheduling for multi-pod AI workloads, improving intra-node topology management for efficient device allocation, and addressing day-two operational challenges such as GPU failure detection and recovery.
Panelists emphasized the need to accelerate feature delivery to end users by breaking down large changes into smaller, manageable components and encouraging early adoption of alpha features to gather necessary feedback for graduation to stable status.
Additionally, the group discussed the development of standardized conformance tests for DRA drivers to ensure interoperability and reliability across different hardware vendors, while also exploring how AI conformance can evolve to cover emerging areas like agent sandboxing and non-deterministic workload behaviors.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session focuses on the Kubernetes Device Resource Allocation (DRA) working group, discussing past achievements, current in-flight work, and future challenges for device management. |
|   2 | Key participants include representatives from Intel, NVIDIA, and the Kubernetes AI conformance team, highlighting a collaborative approach to standardizing device scheduling.           |
|   3 | DRA has introduced a device abstraction via the Resource Slice API and a Resource Claim API to enable flexible device requests and scheduling without race conditions.                   |
|   4 | A major priority is integrating DRA with workload-aware scheduling to support gang scheduling of pod groups, which is essential for large-scale AI and HPC workloads.                    |
|   5 | The team is working on intra-node topology management to ensure efficient allocation of devices from different vendors and drivers within a single node.                                 |
|   6 | Future development includes modeling complex devices, such as partitionable GPUs and time-sharing, to support more diverse hardware configurations.                                      |
|   7 | Day-two operations, such as handling GPU failures and performance degradation, are identified as critical areas requiring better detection and reaction mechanisms.                      |
|   8 | NVIDIA’s NVSentinel project is being explored to monitor GPU health and apply device taints, allowing DRA drivers to react to failures without complex internal logic.                   |
|   9 | AI conformance requirements are evolving to include support for gang scheduling and potentially agent sandboxing, distinguishing between mandatory and directional requirements.         |
|  10 | Accelerating feature delivery to end users is a significant challenge, with a goal to reduce the time from alpha to stable by breaking features into smaller, focused capabilities.      |
|  11 | The Kubernetes beta quality bar has been raised to ensure features are nearly ready for GA, requiring full documentation and robust test coverage before graduation.                     |
|  12 | There is a disconnect between upstream functional testing and conformance testing, as conformance tests are basic and may not cover all vendor-specific corner cases.                    |
|  13 | Defining conformance for DRA drivers is complex because device behavior is vendor-specific, making it difficult to create a universal test suite for exclusive device access.            |
|  14 | The community is considering establishing a set of standard attributes and capabilities that DRA drivers must support to ensure interoperability and topology awareness.                 |
|  15 | The example DRA driver is intended to serve as a reference implementation, with a proposal to require feature inclusion in the example driver as a beta graduation criterion.            |
|  16 | Topology-aware scheduling is being advanced through node labels and multi-node logical devices, with plans to support sub-node topologies for rail-aligned workloads.                    |
|  17 | Users are encouraged to provide specific use cases and feedback to help the working group refine the integration of features like consumable capacity and partitionable devices.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/LK91kn8vA8g/hqdefault.jpg)](https://www.youtube.com/watch?v=LK91kn8vA8g)

[Watch on YouTube](https://www.youtube.com/watch?v=LK91kn8vA8g)
