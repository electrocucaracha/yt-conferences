---
type: Video Note
title: "SIG Scheduling Intro & Updates - Kensei Nakada, Independent & Dominik Marciński, Google"
description: "Ken and Dominic, maintainers of the Kubernetes SIG Scheduling group, present an overview of the scheduler’s architecture, recent initiatives, and new features. They explain that the scheduler is responsible for pod placement using plugins a..."
resource: https://www.youtube.com/watch?v=VW8fvA_uq3k
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Ken and Dominic, maintainers of the Kubernetes SIG Scheduling group, present an overview of the scheduler’s architecture, recent initiatives, and new features.
They explain that the scheduler is responsible for pod placement using plugins and extension points, with filtering and scoring phases to select the best node for each pod.
A major focus is improving support for complex workloads, especially AI workloads, by introducing a generic workload API and gang scheduling, which ensures all pods in a workload are scheduled together to meet requirements like topology and all-or-nothing execution.
Recent features include opportunistic pod scheduling for faster placement of similar pods, asynchronous API calls to improve performance, enhancements to the nominated node name for better integration with autoscalers, and new operators for numeric scheduling constraints.
Updates to subprojects like Kueue and the descheduler were also discussed, with ongoing efforts to make custom plugin development easier and to further enhance workload scheduling capabilities.
The session concludes with an invitation to join the SIG’s Slack channel and community meetings for further discussion.
# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session covers scheduler workings, recent initiatives, new features, and subproject updates.                                                                                          |
|   2 | SIG Scheduling maintains Kubernetes scheduler and related subprojects (e.g., Kueue, Scheduler-Estimator, KoK, Extension).                                                             |
|   3 | Scheduler decides pod placement using plugins for features like pod affinity; plugins run at extension points (e.g., filter, score).                                                  |
|   4 | Scheduling process: filter nodes, score remaining nodes, select best node for pod.                                                                                                    |
|   5 | Custom plugins can be created for specific use cases, running at extension points.                                                                                                    |
|   6 | Scheduling cycle determines placement; binding cycle makes API call to bind pod to node; scheduling queue holds pending pods.                                                         |
|   7 | Workflow scheduling initiative aims to better support complex workloads (e.g., AI training/inference) with requirements like gang/all-or-nothing scheduling and topology constraints. |
|   8 | Introduced workload API in 1.35 to model gangs and enable gang scheduling (block binding until all pods are scheduled).                                                               |
|   9 | Future plans: expand workload API, support gang of gangs, topology constraints, workload-level preemption, autoscaling integration, resource reservations, and scheduling simulation. |
|  10 | Gang scheduling ensures all pods in a workload are scheduled before binding/actuation begins.                                                                                         |
|  11 | Opportunistic pod scheduling (beta in 1.35): caches node scores for similar pods to speed up scheduling; uses pod "signature" to determine similarity.                                |
|  12 | Limitations: only one pod per node in fast path; no interpod constraints; ignores latest cluster state changes (short TTL for cache).                                                 |
|  13 | Asynchronous API calls during scheduling now enabled by default in 1.35 to avoid blocking scheduling cycle.                                                                           |
|  14 | NominatedNodeName enhancement: exposes intended pod placement before binding, aiding external components like Cluster Autoscaler.                                                     |
|  15 | Extended toleration operators (alpha): supports numeric comparisons for scheduling decisions.                                                                                         |
|  16 | Scheduling framework types/interfaces moved to staging repo in 1.34 for easier custom plugin development.                                                                             |
|  17 | Queuing hint is GA in 1.3                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=VW8fvA_uq3k)