---
type: Video Note
title: "SIG Apps Updates: Building the Next Generation of Kubernetes Workloads... Maciej Szulik & Janet Kuo"
description: 'In this SAPS talk, Janet and Mache, co-leads of SIG Apps, discuss recent developments and ongoing work in Kubernetes workload management. They highlight new beta features such as the "maximum available" rollout for StatefulSets, which was t...'
resource: https://www.youtube.com/watch?v=uj2WVzDndt4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this SAPS talk, Janet and Mache, co-leads of SIG Apps, discuss recent developments and ongoing work in Kubernetes workload management.
They highlight new beta features such as the "maximum available" rollout for StatefulSets, which was temporarily disabled due to uncovered edge cases, and a new status field for terminating pods in deployments to improve visibility and control.
The team emphasizes the importance of user feedback in identifying and resolving issues, especially for complex features like pod replacement policies and job management enhancements.
They also describe collaborations with the batch working group to support large-scale and AI/ML workloads, including improvements to job mutability, backoff limits per index, and external job management.
Additionally, the talk introduces subprojects like Agent Sandbox, which provides isolated, stateful environments for agent runtimes and developer sandboxes, and the MCP Lifecycle Operator for managing MCP servers.
The session concludes with an invitation for community contributions, especially in testing, and clarifies the roles of related working groups in handling specialized workloads.
# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Apps focuses on application use cases and owns core workflow APIs (Deployment, StatefulSet, Job, CronJob, DaemonSet).                           |
|   2 | SIG Apps develops application-level tools and standards, including Kubernetes-native standards for AI.                                              |
|   3 | Leadership: Janet (Google), Mache, and Kennet.                                                                                                      |
|   4 | New beta feature in 1.35: "Maximum Available" for StatefulSets to improve rollout speed; currently disabled by default due to uncovered edge cases. |
|   5 | User feedback is crucial for identifying and fixing issues in features.                                                                             |
|   6 | Beta feature: New status field for terminating replicas in Deployments to show how many pods are being terminated.                                  |
|   7 | Ongoing work on Deployment pod replacement policy; implementation changes ReplicaSet and Deployment controllers significantly.                      |
|   8 | Need for more testing and contributors, especially for edge cases in StatefulSet, ReplicaSet, and Deployment.                                       |
|   9 | Batch Working Group spun out of SIG Apps to address missing Kubernetes functionalities for ML/AI and HPC workloads.                                 |
|  10 | Jobs API improvements: now possible to suspend jobs and modify certain fields (CPU, GPU, memory) after termination of pods.                         |
|  11 | Added per-index backoff limit for Jobs, allowing more granular failure handling in large-scale or indexed jobs.                                     |
|  12 | Job success/completion policy allows ignoring failed pods if overall success criteria are met.                                                      |
|  13 | Pod replacement policy for Jobs implemented to better handle fatal vs. temporary failures.                                                          |
|  14 | Q Project: Provides queuing primitives and fair sharing for cluster resources; supports job replication and centralized job management.             |
|  15 | Added "managed by" field in Jobs to allow external controllers to manage job status, with API server validation for consistency.                    |
|  16 | StatefulSet improvements: working on "recreate" update strategy to address stuck deployments; implementation ongoing.                               |
|  17 | Agent Sandbox project: simple controller for isolated, singleton workloads; supports warm pools for faster sandbox creation.                        |
|  18 | MCP Lifecycle Operator: new project for managing MCP server lifecycle in c                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=uj2WVzDndt4)