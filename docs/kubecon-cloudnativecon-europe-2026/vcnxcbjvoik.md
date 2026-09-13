---
layout: default
title: Unleashing Event Driven Capabilities With KEDA - Jorge Turrado & Zbynek Roubalik
nav_order: 385
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Horge Dorado and Beign, both maintainers of the KEDA
  project, introduce KEDA (Kubernetes Event-driven Autoscaling), which aims to simplify
  autoscaling in Kubernetes by supporting a wide range of event sources and custom
  met...
resource: https://www.youtube.com/watch?v=VCNxcBjVOIk
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

In this session, Horge Dorado and Beign, both maintainers of the KEDA project, introduce KEDA (Kubernetes Event-driven Autoscaling), which aims to simplify autoscaling in Kubernetes by supporting a wide range of event sources and custom metrics beyond standard CPU and memory.
They explain KEDA’s architecture, including its operator, metric server adapter, and validation webhook, and detail how scaling is managed through scaled objects and scale jobs, allowing for both horizontal scaling and job scheduling based on diverse triggers.
The presenters highlight best practices for configuring scaling behavior, such as managing polling intervals, caching metrics, and using scaling modifiers to combine multiple triggers or apply custom formulas.
They also discuss recent features like dynamic fallback behaviors, expanded scaler support, and new architecture compatibility, as well as future plans for GPU support and scale job suspension.
The session concludes with a demonstration of HTTP-based scaling and a comparison to KNative, emphasizing KEDA’s flexibility and focus on event-driven, secure, and customizable autoscaling solutions for Kubernetes workloads.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Jorge Dorado (Principal Site Reliability Engineer at Digit, KEDA maintainer, CNCF ambassador) and Beign (KEDA maintainer, founder/CTO at Karify).    |
|   2 | Session focuses on KEDA (Kubernetes Event-driven Autoscaling), aiming to make Kubernetes autoscaling simple.                                                     |
|   3 | KEDA community is growing with many contributors and users.                                                                                                      |
|   4 | KEDA is built on top of Kubernetes, reusing components like HPA (Horizontal Pod Autoscaler).                                                                     |
|   5 | Main KEDA components: KEDA operator (manages scaling resources), metric server adapter (sends metrics to Kubernetes API), validation webhook (checks resources). |
|   6 | Scaling from zero to one replica is managed by KEDA operator; scaling from one to N replicas is managed by HPA.                                                  |
|   7 | Scaling metadata is defined in ScaledObject (for horizontal scaling) or ScaleJob (for scheduling jobs).                                                          |
|   8 | ScaledObject: defines target deployment, configuration (min/max replicas), and triggers (signals for scaling).                                                   |
|   9 | KEDA supports multiple triggers and custom metrics beyond CPU/memory (e.g., queue length).                                                                       |
|  10 | ScaleJob: schedules Kubernetes jobs based on metrics, suitable for long-running processes.                                                                       |
|  11 | Security: Use TriggerAuthentication or ClusterTriggerAuthentication for secrets; do not place secrets directly in ScaledObjects/ScaleJobs.                       |
|  12 | Over 70 scalers supported, with new ones added regularly.                                                                                                        |
|  13 | New features: fallback for value metric type, dynamic fallback behaviors, support for S390X architecture.                                                        |
|  14 | Best practices: configure scaling/activation phases, cooldown periods, and HPA behavior, especially for sensitive workloads (e.g., databases).                   |
|  15 | Polling interval: only relevant for scaling from zero to one; HPA handles one to N scaling.                                                                      |
|  16 | Metric caching can reduce load on external services.                                                                                                             |
|  17 | Scaling modifiers allow custom formulas for combining multiple triggers.                                                                                         |
|  18 | Prometheus/DataDog can be used as metric sources, but may not scale well for large deployments due to polling overhead.                                          |
|  19 | Future plans: support for scale suspending jobs, checkpointing/restoring workloads, bett                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=VCNxcBjVOIk)
