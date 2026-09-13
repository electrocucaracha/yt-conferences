---
type: Video Note
title: "Improving Pod Disruption and Node Lifecycle - Filip Křepinský, Lucy Sweet & Ryan Hallisey"
description: "In this presentation, Lucy from Uber, Philip from Red Hat, and Ryan from Nvidia—leads of the Kubernetes node life cycle working group—discuss ongoing efforts to improve pod disruption and node life cycle management in Kubernetes. They intro..."
resource: https://www.youtube.com/watch?v=dpRlhe9EgiY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Lucy from Uber, Philip from Red Hat, and Ryan from Nvidia—leads of the Kubernetes node life cycle working group—discuss ongoing efforts to improve pod disruption and node life cycle management in Kubernetes.
They introduce the eviction request API, which enables a more declarative and observable approach to pod eviction, allowing for complex business logic and coordination among multiple responders before terminating workloads.
The team also addresses challenges in node maintenance, highlighting the fragmented ecosystem of tools and the need for standardized APIs to improve observability and coordination of node states such as draining and maintenance.
Additionally, they discuss the issue of "kublet amnesia" during graceful node shutdowns and their work on specialized life cycle management to address such problems.
The group encourages community involvement and feedback to help shape these evolving features and ensure broad adoption across the Kubernetes ecosystem.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Kubernetes Node Life Cycle Working Group aims to improve node life cycle processes, including node drains, maintenance, and node admission/removal.        |
|   2 | Current processes are reactive; the group is working to make them more proactive and observable.                                                               |
|   3 | Three main projects discussed: Eviction Requests API, Specialized Life Cycle Management (formerly Declarative Node Maintenance), and Graceful Node Shutdown.   |
|   4 | Eviction Requests API allows signaling intent to evict a workload before actual eviction, enabling complex logic and coordination.                             |
|   5 | The API supports custom responders (hooks) to handle application-specific logic before eviction, such as migration or scaling.                                 |
|   6 | Eviction Requests API is declarative, tracks multiple eviction requesters, and supports cancellation/withdrawal of eviction intent.                            |
|   7 | The API is layered above Pod Disruption Budgets (PDBs) and allows for more observable and coordinated pod terminations.                                        |
|   8 | The feature is targeted for Kubernetes 1.37; initial adoption will be optional, with plans for broader integration.                                            |
|   9 | Specialized Life Cycle Management aims to standardize node maintenance and drain processes across the ecosystem.                                               |
|  10 | The ecosystem currently has fragmented tools and approaches for node drain/maintenance; the goal is to create common APIs and states.                          |
|  11 | Three-step approach: improve observability, define meaningful node states, and drive ecosystem adoption.                                                       |
|  12 | Graceful Node Shutdown addresses issues where kubelet may forget it is shutting down ("kubelet amnesia"); improved observability and coordination are planned. |
|  13 | The working group prioritizes focused work on these features to avoid diluting efforts.                                                                        |
|  14 | Community involvement is encouraged via weekly meetings and the Kubernetes Slack channel.                                                                      |
|  15 | Integrators and cloud operators are interested in adopting the new APIs once available.                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dpRlhe9EgiY)