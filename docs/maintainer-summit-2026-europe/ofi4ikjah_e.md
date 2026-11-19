---
layout: default
title: "Unconference Session: Node Lifecycle State Needs a Real API"
nav_order: 18
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "The Node Lifecycle Working Group, led by Ryan, Filip, and Lucy, convened to address the lack of a standardized API for managing node lifecycle states in Kubernetes, noting that current reliance on ..."
resource: "https://www.youtube.com/watch?v=ofI4IKjAH_E"
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

The Node Lifecycle Working Group, led by Ryan, Filip, and Lucy, convened to address the lack of a standardized API for managing node lifecycle states in Kubernetes, noting that current reliance on labels, annotations, and taints leads to fragmented, proprietary solutions.
The discussion highlighted critical gaps in handling complex hardware like GPUs, specifically the need for "in-place drain" or suspension capabilities that allow workloads to checkpoint and resume on the same node without breaking multi-pod clustering or releasing hardware.
Participants also debated the limitations of the binary node readiness state, proposing a more granular approach using defined conditions or events to represent various lifecycle stages, such as draining or maintenance, to better support integrators and auto-scalers.
While acknowledging the difficulty of defining universal states, the group emphasized the importance of establishing clear ownership and intent through a declarative Eviction Request API, which aims to facilitate two-way communication between applications and cluster controllers.
The session concluded with a call for broader collaboration, particularly from integrators, to refine these primitives and ensure the proposed APIs are practical, flexible, and capable of solving the most common lifecycle management challenges in the ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Node Lifecycle Working Group aims to establish a standardized API for node lifecycle management to replace fragmented methods like labels, annotations, and taints.                         |
|   2 | Current lifecycle management often requires organizations to build proprietary stacks, creating a need for community-supported primitives in Kubernetes.                                        |
|   3 | Data center complexity, particularly with specialized hardware like GPUs and NVLinks, necessitates robust lifecycle management beyond initial scheduling.                                       |
|   4 | A key use case is "in-place drain" or suspension, allowing pods to checkpoint and resume on the same node without losing hardware placement or breaking multi-pod workload clustering.          |
|   5 | The Eviction Request API is being developed to provide declarative intent for evictions, enabling better coordination between applications and cluster components like the cluster autoscaler.  |
|   6 | There is a need to distinguish between node readiness for general scheduling and readiness for specific workloads, suggesting a spectrum of states rather than a binary ready/not-ready status. |
|   7 | Software dependencies on nodes, such as container networking drivers, require lifecycle awareness to manage downtime and workload migration during upgrades.                                    |
|   8 | Ownership and responsibility for node state changes are currently unclear, requiring a defined contract for node-owning controllers to ensure discoverability and accountability.               |
|   9 | The group prioritizes solving for 90% of use cases with flexible primitives that integrators can build upon, rather than creating a universal, rigid state machine.                             |
|  10 | Prior art from HPC schedulers like Slurm should be investigated to understand state transitions and the distinction between node actions and scheduling layer decisions.                        |
|  11 | An event-based approach, where consumers derive states from observed events, may offer more flexibility than defining fixed universal states.                                                   |
|  12 | Integrators need the ability to predict node states, such as whether a new node will become ready during a zonal outage, to make informed provisioning decisions.                               |
|  13 | The working group encourages feedback from integrators and end users to refine the scope of the API and ensure it addresses real-world operational challenges.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ofI4IKjAH_E/hqdefault.jpg)](https://www.youtube.com/watch?v=ofI4IKjAH_E)

[Watch on YouTube](https://www.youtube.com/watch?v=ofI4IKjAH_E)
