---
type: Video Note
title: "Instrumenting Kueue Scheduling for ML Training - Amy Chen, CoreWeave & Gabriel Saba, Google"
description: "In this talk, Amy and Gabriel introduce Q, a batch job scheduler designed for managing machine learning training workloads in large, multi-tenant GPU clusters. They explain that Q addresses the complex challenge of maximizing resource utili..."
resource: https://www.youtube.com/watch?v=rcrl8-CudVw
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Amy and Gabriel introduce Q, a batch job scheduler designed for managing machine learning training workloads in large, multi-tenant GPU clusters.
They explain that Q addresses the complex challenge of maximizing resource utilization while enforcing quotas, prioritization, and fair sharing among diverse teams, and highlight the difficulty of diagnosing why workloads remain pending—often due to guarantee violations, fragmentation, or scheduling bugs.
The speakers outline a systematic approach to troubleshooting such issues, including checking for guarantee violations, ruling out fragmentation, monitoring admission and preemption rates, and examining logs and system health.
Through real-world bug examples, they demonstrate how issues like slow preemption, zombie pods, and incorrect resource share calculations can impede scheduling, and discuss recent improvements to Q that address these problems.
Finally, they recommend key metrics and dashboard features for monitoring Q’s performance and ensuring efficient, transparent scheduling in machine learning clusters.
# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Q is a batch job dispatcher designed for machine learning training clusters to optimize expensive GPU compute utilization.                                                              |
|   2 | Q addresses complex scheduling, queuing, prioritization, and quota rules in large, multi-tenant environments.                                                                           |
|   3 | Guarantee violations occur when workloads that fit within unallocated quota remain pending, signaling potential scheduling issues.                                                      |
|   4 | Scheduling is computationally hard, especially with many heterogeneous machines and online, multifaceted objectives.                                                                    |
|   5 | Q uses heuristics such as priority queues, sorting, scoring, and fair sharing to manage scheduling complexity.                                                                          |
|   6 | Q’s main functions: quota management (ensuring admitted jobs do not exceed cluster resources) and queuing (deciding which workload runs next).                                          |
|   7 | Resource flavors abstract hardware types; cluster queues define quotas and handle workload queuing; cohorts model organizational hierarchy.                                             |
|   8 | Q’s scheduling cycle: considers pending workloads, simulates resource assignments/preemptions, orders workloads, and admits them if capacity allows.                                    |
|   9 | Fragmentation: occurs when resources are sufficient in total but not in the required shape for a workload; measured by available slot shapes per node.                                  |
|  10 | Three failure tiers: submission layer, Q layer, Kubernetes layer; each can cause workloads to remain pending.                                                                           |
|  11 | Debugging recipe: detect guarantee violation, rule out fragmentation, check admission/preemption rates, verify if Q released workload to Kubernetes, inspect logs, check system health. |
|  12 | Bug 1: Slow admission/preemption due to head-of-queue blocking with pod workload type and long preemption grace periods; fixed by immediate quota release on preemption target marking. |
|  13 | Bug 2: Cluster-wide admission slowdown caused by zombie pods targeted for preemption by multiple cluster queues; fixed by releasing quota after grace period termination.               |
|  14 | Bug 3: Incorrect dominant resource share (DRS) values due to rounding errors led to improper scheduling order; fixed upstream.                                                          |
|  15 | Recommendations: mon                                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=rcrl8-CudVw)