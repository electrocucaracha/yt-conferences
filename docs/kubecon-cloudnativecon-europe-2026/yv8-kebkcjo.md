---
layout: default
title:
  "Sponsored Session: Performance at Enterprise Cloud Scale: Coupa’s Ku... Peter
  Irwin & Carl Baumcratz"
nav_order: 346
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Peter from ScaleOps and Carl from Koopa discuss
  the challenges of managing Kubernetes at enterprise scale, particularly as dynamic
  workloads and multiple development teams increase complexity and inefficiency. Koopa,
  a...
resource: https://www.youtube.com/watch?v=yV8_keBkCJo
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

In this presentation, Peter from ScaleOps and Carl from Koopa discuss the challenges of managing Kubernetes at enterprise scale, particularly as dynamic workloads and multiple development teams increase complexity and inefficiency.
Koopa, an AI-driven spend management platform, faced issues with manual resource tuning, inefficient node and pod packing, and escalating costs as their environment grew to 140 clusters.
By implementing ScaleOps’ automation solutions, Koopa streamlined workload right-sizing, improved pod placement, and facilitated a smooth migration from Cluster Autoscaler to Carpenter, ultimately reducing vCPU usage by 30% and saving $2.26 million to date.
The automation not only cut costs but also saved thousands of engineering hours, enabled proactive resource management, and fostered cross-team alignment, allowing developers to focus on innovation rather than infrastructure maintenance.
The partnership with ScaleOps continues to evolve, emphasizing ongoing cost avoidance and operational efficiency as Koopa scales its platform.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focused on running Kubernetes at enterprise cloud scale and related challenges.                                                                             |
|   2 | Key challenges include managing dynamic environments, inefficient node and pod packing, and manual resource tuning.                                                    |
|   3 | Koopa's environment has rapidly expanded, with 140 clusters and increasing workloads and customers.                                                                    |
|   4 | Koopa uses a GitOps approach for cluster and configuration delivery.                                                                                                   |
|   5 | Cost management was initially reactive, relying on reports; goal was to shift cost control earlier in the pipeline.                                                    |
|   6 | Traditional autoscaling with static thresholds is insufficient, leading to fragmentation and inefficiency.                                                             |
|   7 | Manual intervention for pod and node issues was time-consuming and reactive.                                                                                           |
|   8 | Koopa evaluated build vs. buy for optimization solutions; selected ScaleOps for ease of use and minimal issues.                                                        |
|   9 | Phase one: Implemented workload right-sizing and pod placement with ScaleOps, starting in dev/test, then production.                                                   |
|  10 | Achieved cost savings even as 37% of workloads were scaled up.                                                                                                         |
|  11 | Strategy emphasized automation by default and developer buy-in.                                                                                                        |
|  12 | Migrated from Cluster Autoscaler to Carpenter, facing challenges with workload requirements and risk of misconfiguration.                                              |
|  13 | ScaleOps aided migration, provided transparent UI, and supported node pool configuration.                                                                              |
|  14 | Implemented node consolidation with ScaleOps to reduce fragmentation and improve efficiency, especially during downtimes.                                              |
|  15 | Exploring predictive replica scaling to maintain SLOs by autoscaling before demand spikes.                                                                             |
|  16 | Results: $2.26 million saved to date, $260,000/month, 30% vCPU reduction, and thousands of engineering hours saved.                                                    |
|  17 | Shifted focus from cost cutting to ongoing cost avoidance and compounding savings.                                                                                     |
|  18 | Multi-team engagement bridged priorities between finance, development, and platform teams.                                                                             |
|  19 | Key takeaways: manual tuning doesn't scale, automation unlocks ROI, cross-functional alignment accelerates adoption, and automation frees teams for higher priorities. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yV8_keBkCJo)
