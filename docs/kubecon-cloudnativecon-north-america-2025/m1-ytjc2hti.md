---
layout: default
title:
  "Karmada in Action: Scaling AI Workloads Across Multi-Clus... Hongcai Ren,
  Tessa Pham & Wei-Cheng Lai"
nav_order: 115
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Tessa Fam and Way Changai from Bloomberg discuss the challenges
  and solutions for scaling AI workloads across multiple Kubernetes clusters using
  Carmada. They explain that running AI workloads on multiple clusters is essential...
resource: https://www.youtube.com/watch?v=M1-yTjC2hTI
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Tessa Fam and Way Changai from Bloomberg discuss the challenges and solutions for scaling AI workloads across multiple Kubernetes clusters using Carmada.
They explain that running AI workloads on multiple clusters is essential for high availability, low latency, scalability, cost efficiency, and infrastructure independence, but it introduces significant operational complexity, such as managing configurations, scheduling, scaling, and hardware heterogeneity.
Carmada addresses these issues by providing a centralized control plane for unified deployment, intelligent workload placement, cross-cluster autoscaling, and failover capabilities, all integrated with Kubernetes.
The speakers detail Carmada’s architecture, policy-driven orchestration, resource interpretation for custom resources, federated resource quotas, global scheduling with Volcano, federated HPA for autoscaling, and fine-grained cluster failover policies.
They also answer audience questions about deployment best practices, interpreter resources, and ongoing improvements for cluster isolation and failover, emphasizing Carmada’s flexibility and active community support.

# Main Points

|   # | Main point                                                                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Chromata (Carmada) helps scale AI workloads across multiple Kubernetes clusters.                                                                                                                                                |
|   2 | Key reasons for multicluster AI: high availability, low latency via geo-distribution, scalability, cost optimization, centralized hardware management, and infrastructure independence.                                         |
|   3 | Main AI use cases: distributed training and global inference serving.                                                                                                                                                           |
|   4 | Multicluster challenges: operational complexity, config drift, deployment/scheduling decisions, lack of unified resource view, difficulty in cross-cluster autoscaling, dependency management, and policy/governance headaches. |
|   5 | AI inference adds unique challenges: strict latency, model versioning, heterogeneous hardware scheduling, and unpredictable spiky demand.                                                                                       |
|   6 | Carmada provides centralized control and unified endpoint for deploying/managing apps across clusters.                                                                                                                          |
|   7 | Features: intelligent multicluster scheduling, automatic failover/rescheduling, cross-cluster autoscaling, Kubernetes interoperability.                                                                                         |
|   8 | Architecture: central control plane (API server, controller manager, scheduler) and member clusters.                                                                                                                            |
|   9 | Resource interpreter translates custom resources (CRDs) for Carmada.                                                                                                                                                            |
|  10 | Policy-driven orchestration: propagation policies (where/how to deploy), override policies (customize per cluster), failover/rescheduling.                                                                                      |
|  11 | Propagation policy fields: cluster affinity, tolerations, dependencies, spread constraints, replica scheduling strategies (duplicate/divide/weighted).                                                                          |
|  12 | Override policy use cases: canary rollouts, hardware-specific configs, model/image path changes, resource requests/limits adjustments.                                                                                          |
|  13 | Federated resource quota: define one quota per namespace, aggregated usage/limits, reduces config drift and manual tuning.                                                                                                      |
|  14 | Federated quota enforcement: global hard limits, fail-fast admission, consistent quota behavior.                                                                                                                                |
|  15 | Volcano global: cross-cluster job scheduling with priority/fairness/capacity for large-scale AI.                                                                                                                                |
|  16 | Federated HPA: aggregates metrics across clusters, enables cross-cluster autoscaling based on demand and policies.                                                                                                              |
|  17 | Clu                                                                                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=M1-yTjC2hTI)
