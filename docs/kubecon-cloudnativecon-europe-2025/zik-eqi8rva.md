---
layout: default
title: SIG Scheduling Intro & Updates - Maciej Skoczeń, Google; Kensei Nakada, Tetrate.io
nav_order: 290
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The Google team is working on improving the performance and efficiency
  of the Kuberenetes scheduler, specifically the Scheduleuler component. Recent updates
  include "queing hints" to handle unschedulable parts by retrying them after a certa...
resource: https://www.youtube.com/watch?v=ZIk_EqI8rVA
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

The Google team is working on improving the performance and efficiency of the Kuberenetes scheduler, specifically the Scheduleuler component.
Recent updates include "queing hints" to handle unschedulable parts by retrying them after a certain period, allowing for more efficient use of resources.
Another update is "async preemption," which enables higher priority parts to preempt lower priority ones, improving scheduling throughput.
Additionally, the team has introduced features such as partitionable devices and prioritized device requests, enabling more flexible resource allocation.
The Scheduleuler simulator allows users to test custom plugins and configurations without affecting their production clusters.

# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | The future extension point allows programs to reject nodes that shouldn't run a part.                                    |
|   2 | The score extension point allows programs to score nodes based on their preference.                                      |
|   3 | The scheduling cycle schedules parts one by one and evaluates all nodes to determine the best node for each part.        |
|   4 | The queuing hint feature reduces unnecessary scheduling rituals by allowing progress across events.                      |
|   5 | Async preemption allows higher priority parts to preempt lower priority parts to make way for them.                      |
|   6 | Partitionable devices allow ports to request partitioning of larger devices.                                             |
|   7 | Future challenges include attaching devices dynamically and handling cross-node dependencies.                            |
|   8 | The scheduleuler simulator can be connected to a real cluster, allowing users to test custom plugins and configurations. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZIk_EqI8rVA)
