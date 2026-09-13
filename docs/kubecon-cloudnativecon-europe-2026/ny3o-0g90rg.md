---
layout: default
title:
  "Multi-cluster Orchestration System: Karmad... Hongcai Ren, Tessa Pham, Michas
  Szacillo & Zongqing Li"
nav_order: 221
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The session introduces Karmada, a project designed to manage and schedule
  workloads across multiple Kubernetes clusters without requiring changes to existing
  applications. Over the past year, Karmada has added several key features, includin...
resource: https://www.youtube.com/watch?v=NY3O_0G90rg
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

The session introduces Karmada, a project designed to manage and schedule workloads across multiple Kubernetes clusters without requiring changes to existing applications.
Over the past year, Karmada has added several key features, including stateful application cluster failover with state preservation, federated resource quota enforcement to prevent resource saturation, workload anti-affinity and affinity for high availability, support for multi-component workload scheduling, and priority-based scheduling to ensure critical workloads are handled first.
Bloomberg shares use cases such as model caching and Jupyter notebook scheduling, highlighting Karmada’s ability to fan out resources, aggregate global status, and enable flexible, policy-driven placement.
Trip.com describes how Karmada has streamlined cluster add-on deployment, improved system resilience through high-availability architectures, and enabled smooth, large-scale cross-cluster migrations, significantly reducing operational time and effort.
The community continues to grow, focusing on scalability, dashboard improvements, and enhanced support for AI workloads, while addressing questions about resource quotas, autoscaling, and performance at scale.

# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speakers introduced: Hungai (Huawei, Kamada maintainer), Mihashilo (Bloomberg, streaming platform), Tessa Fam (Bloomberg, AI training/notebooks), Juni (Trip.com, online travel agency)                            |
|   2 | Agenda: Kamada introduction, new features, use cases, community status                                                                                                                                             |
|   3 | Kamada manages multiple Kubernetes clusters, schedules workloads across clusters, supports various workloads (deployments, jobs, Spark, Flink, PyTorch, custom resources), and uses Kubernetes API                 |
|   4 | Quarterly releases with new features developed with the community                                                                                                                                                  |
|   5 | Stateful application cluster failover: since v1.15, supports state preservation during failover using JSON path and alias label in propagation policy                                                              |
|   6 | Federated quota enforcement (v1.14): set resource limits at Kamada control plane, applies quotas per namespace, prevents over-scheduling, ensures failover capacity                                                |
|   7 | Workload anti-affinity: schedule workloads to separate clusters for high availability using group-by label keys; also supports co-location of workloads                                                            |
|   8 | Multiple component workload scheduling: supports CRDs with multiple components, accurately schedules based on component resource requirements                                                                      |
|   9 | Priority-based scheduling: uses Kubernetes priority classes, schedules higher-priority workloads first, FIFO for ties, default priority is zero                                                                    |
|  10 | Bloomberg use cases:                                                                                                                                                                                               |
|  11 | Model cache CRD to cache models on every node/cluster, leverages Kamada’s multicluster federation and propagation policy, global status aggregation, auto-detects/reconciles failures, supports flexible placement |
|  12 | Jupyter notebooks: schedules jobs to clusters with required GPUs, uses Kamada for intelligent placement, global status, rescheduling on failure, potential for priority scheduling                                 |
|  13 | Trip.com use cases:                                                                                                                                                                                                |
|  14 | Unified add-on distribution to 40+ clusters, reduced cluster onboarding from days to <4 hours                                                                                                                      |
|  15 | High-availability architecture: spreads applications across clusters, automatic traffic shift and HPA-based scaling on failure, federation layer can be unavailable for                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=NY3O_0G90rg)
