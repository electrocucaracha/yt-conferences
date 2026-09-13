---
layout: default
title:
  Managing Netflix’s Compute Infrastructure With Kubernetes and Dynamic... Charles
  Zheng & Nick Parker
nav_order: 162
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Charles and Nick from Netflix's compute platform
  team explain how they manage Netflix’s large-scale infrastructure using Kubernetes,
  with a focus on their custom Titus API, which abstracts Kubernetes complexities
  for d...
resource: https://www.youtube.com/watch?v=vaTOiXR2KSM
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

In this presentation, Charles and Nick from Netflix's compute platform team explain how they manage Netflix’s large-scale infrastructure using Kubernetes, with a focus on their custom Titus API, which abstracts Kubernetes complexities for developers and has remained largely unchanged through migrations from Mesos to Kubernetes.
Their architecture spans multiple cloud regions, organizing clusters into service, batch, and trough (preemptible) categories to optimize for different workload patterns and resource utilization.
They built a lightweight, custom federation layer to route jobs and manage capacity across clusters, prioritizing simplicity, reliability, and high throughput over complex optimizations.
Capacity management is handled through a tiered system—reserved, elastic, and trough—with custom autoscaling, disruption budgets, and node defragmentation processes to balance cost, launch latency, and disruption tolerance.
Throughout, they emphasize that following Kubernetes best practices and keeping the system straightforward has enabled them to efficiently support Netflix’s massive workloads without overengineering, and they share lessons learned about right-sizing, bin packing, and evolving their approach as needs change.

# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Netflix uses Kubernetes to manage compute infrastructure, with dynamic capacity management.                                                                                                                        |
|   2 | All container workflows are launched via Titus, Netflix’s custom API, not directly through Kubernetes.                                                                                                             |
|   3 | Titus abstracts Kubernetes concepts, focusing on job/container launch for developers.                                                                                                                              |
|   4 | Netflix’s cloud infrastructure spans multiple regions, each with fleets of Kubernetes clusters.                                                                                                                    |
|   5 | Clusters are categorized as service (long-running), batch (short-lived), and trough (temporary, preemptible).                                                                                                      |
|   6 | No unified entry point across regions; users specify region for workload placement.                                                                                                                                |
|   7 | Cross-cluster trough mechanism utilizes spare capacity from service clusters.                                                                                                                                      |
|   8 | System architecture: Requests go through Titus API gateway → federation control plane → meta Kubernetes control plane → cellular API gateway → Titus job coordinator → Kubernetes pods.                            |
|   9 | Cassandra is used for persistent job data storage due to reliability and scalability.                                                                                                                              |
|  10 | Capacity management uses resource pools and an in-house fleet management controller for scaling and defragmentation.                                                                                               |
|  11 | Architecture prioritizes reliability, ease of use, and minimal operational overhead.                                                                                                                               |
|  12 | Cluster federation is custom-built for high throughput and dynamic capacity management; routes workflows and manages resource capacity based on real-time usage and traffic prediction.                            |
|  13 | Federation service is stateless, leveraging Titus API for job status caching.                                                                                                                                      |
|  14 | In-cluster scheduling uses open-source Kubernetes scheduler with custom plugins and profiles (e.g., bin packing for services).                                                                                     |
|  15 | Capacity management balances cost efficiency, launch latency, and disruption tolerance via three priority tiers: reserved (pre-scaled), elastic (scales as needed), and trough (preemptible, uses spare capacity). |
|  16 | Autoscaling uses a two-stage node scaling down process, allowing trough pods on scaling-down nodes and reversible taints.                                                                                          |
|  17 | Custom disruption budgets and batch job time limits inform scheduling and node teardown.                                                                                                                           |
|  18 | Scaling up is triggered by reser                                                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vaTOiXR2KSM)
