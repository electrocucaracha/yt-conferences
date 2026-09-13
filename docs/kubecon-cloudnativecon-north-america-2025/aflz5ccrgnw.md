---
layout: default
title: SIG Autoscaling Projects Update - Jack Francis, Microsoft & Jason Deal, AWS
nav_order: 265
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Jack Francis from Microsoft and Jason Deal from AWS present an overview
  of Kubernetes autoscaling, highlighting the community-driven efforts within SIG
  Autoscaling and expressing gratitude to contributors. They explain the roles of
  cluster...
resource: https://www.youtube.com/watch?v=aflZ5ccrgnw
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

Jack Francis from Microsoft and Jason Deal from AWS present an overview of Kubernetes autoscaling, highlighting the community-driven efforts within SIG Autoscaling and expressing gratitude to contributors.
They explain the roles of cluster autoscaler and Carpenter, noting that cluster autoscaler manages node pool replicas based on pod demand, while Carpenter provisions infrastructure dynamically and supports advanced scheduling constraints.
The talk details recent Carpenter updates, including the introduction of reserved capacity, node overlay for custom pricing and resource adjustments, and static capacity for maintaining fixed node counts.
Updates to cluster autoscaler include enhancements to horizontal and vertical pod autoscalers, custom tolerance, in-place vertical scaling, and ongoing work to integrate Device Resource Assignment (DRA) features.
The speakers also discuss Carpenter’s roadmap for DRA support, the growing provider ecosystem for both autoscalers, and encourage community involvement through meetings, GitHub, and Slack channels.

# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Jack Francis (Microsoft) and Jason Deal (AWS) presented on Kubernetes autoscaling, focusing on SIG Autoscaling, Cluster Autoscaler, and Carpenter.                                               |
|   2 | SIG Autoscaling is maintained by a small group of active leads and relies heavily on community volunteers.                                                                                       |
|   3 | Autoscaling responsibilities include cluster/node autoscaling (Cluster Autoscaler, Carpenter) and workload/pod autoscaling (Horizontal Pod Autoscaler, Vertical Pod Autoscaler, Add-on Resizer). |
|   4 | Ongoing collaboration with SIG Scheduling and SIG Node Device Management on frontier concepts: workload, device, and topological autoscaling.                                                    |
|   5 | Cluster Autoscaler monitors pending pods, adjusts node pool replicas, and removes underutilized nodes via proactive simulations.                                                                 |
|   6 | Carpenter provisions infrastructure dynamically, supports standard scheduling constraints, and is a scale-from-zero autoscaler.                                                                  |
|   7 | Horizontal Pod Autoscaler (HPA) adjusts pod replicas based on metrics; it is the canonical trigger for autoscaling events.                                                                       |
|   8 | Vertical Pod Autoscaler (VPA) adjusts pod resource sizes, is a separate component, and widely adopted.                                                                                           |
|   9 | Carpenter project updates:                                                                                                                                                                       |
|  10 | Core APIs (node pool, node claim) graduated to v1 (August 2024).                                                                                                                                 |
|  11 | Introduced "reserved" capacity type for pre-purchased capacity, alongside on-demand and spot.                                                                                                    |
|  12 | Node overlay CRD allows user-defined pricing/capacity adjustments for nodes.                                                                                                                     |
|  13 | Static capacity feature (alpha in v1.8) allows maintaining a fixed number of nodes.                                                                                                              |
|  14 | Cluster Autoscaler updates:                                                                                                                                                                      |
|  15 | HPA custom tolerance graduated to beta in 1.35.                                                                                                                                                  |
|  16 | In-place vertical scaling graduated to GA in 1.35.                                                                                                                                               |
|  17 | Ongoing DRA (Device Resource Assignment) integration and optimizations.                                                                                                                          |
|  18 | Buffers API proposal for static capacity input.                                                                                                                                                  |
|  19 | Node readiness gate and pod conditions for node autoscaling in development.                                                                                                                      |
|  20 | Carpenter is actively developing DRA support, focusing on structured parameters, scheduling, and node claim lifecycle integration.                                                               |
|  21 | Ecosystem growth: new providers for Carpenter (AWS, AKS, IBM, clust                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aflZ5ccrgnw)
