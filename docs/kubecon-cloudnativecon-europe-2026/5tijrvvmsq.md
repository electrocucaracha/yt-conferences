---
layout: default
title:
  "SIG Scheduling Update: Transition From Pod To Workload Scheduling - Kensei
  Nakada & Maciej Skoczeń"
nav_order: 320
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, the maintainers of SIG Scheduling discussed recent updates
  and future plans for Kubernetes scheduling, focusing on the transition from pod-based
  to pod group (gang) scheduling. They explained the architecture of the schedul...
resource: https://www.youtube.com/watch?v=-5TIJrVvmsQ
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

In this session, the maintainers of SIG Scheduling discussed recent updates and future plans for Kubernetes scheduling, focusing on the transition from pod-based to pod group (gang) scheduling.
They explained the architecture of the scheduler, highlighting key components such as the scheduling cycle, binding cycle, and scheduling queue, and described how scheduling decisions are made using extension points like filter and score.
The team introduced significant changes in version 1.36, including the separation of workload and pod group APIs, atomic scheduling for pod groups to prevent deadlocks, and enhancements to preemption and topology-aware scheduling.
Limitations and future improvements were outlined, such as moving to a pod group-based scheduling queue, better integration with preemption algorithms, and support for multi-layer pod groups.
Updates on related subprojects like Queue and Descheduler were also provided, and the maintainers encouraged community participation and feedback.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session covers updates on scheduling, focusing on transition from pod to pod group (workload) scheduling.                                                                   |
|   2 | Maintainers: Kenta Yamada and Mateusz Scott.                                                                                                                                |
|   3 | Scheduling components maintained include: scheduler (main component), Q (job queuing system), descheduler (reschedules pods), and Quark (simulated clusters).               |
|   4 | Scheduler uses plugins and extension points (e.g., filter, score) for scheduling decisions.                                                                                 |
|   5 | Scheduling cycle: green box (decision-making), yellow box (binding, asynchronous), purple box (scheduling queue for pending pods).                                          |
|   6 | Previous gang scheduling used workload API; all pods in a gang scheduled together or not at all.                                                                            |
|   7 | Old implementation had deadlock issues when some pods in a gang were unschedulable.                                                                                         |
|   8 | In 1.36, APIs split: workload API (policy/specification) and pod group API (runtime instances).                                                                             |
|   9 | Scheduler now focuses on pod groups, not individual pods.                                                                                                                   |
|  10 | Pod group scheduling cycle checks feasibility of entire group atomically, reducing deadlocks.                                                                               |
|  11 | Pod group scheduling allows partial or atomic scheduling based on feasibility and policy.                                                                                   |
|  12 | Limitations: still uses pod-based queue, preemption not fully decoupled, heterogeneous pod groups may not be optimally scheduled, interdependencies partially incompatible. |
|  13 | New workload preemption algorithm: preempts at pod group level, not individual pods; uses priority and disruption modes.                                                    |
|  14 | Disruption modes: "pod" (evict individual pods), "pod group" (evict whole group).                                                                                           |
|  15 | Limitations: default pod-based preemption ignores pod groups; plugins need adjustment for new cycle.                                                                        |
|  16 | Topology scheduling added: define topology constraints (e.g., rack), placement-based algorithm, supports multi-level constraints in future.                                 |
|  17 | Q project: AI workload scheduler, supports gang scheduling, topology, fair sharing, API graduation, balanced placement, cross-cluster authentication.                       |
|  18 | Descheduler: reschedules pods for better spread after initial scheduling, now supports default evictor and pod lifetime plugins.                                            |
|  19 | Community: seeki                                                                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-5TIJrVvmsQ)
