---
type: Video Note
title: "LLM Inference at Scale: Orchestrating Prefill-Decode Disaggregation - Zhonghu Xu"
description: "Junhu from Haw Club discusses the challenges and solutions for orchestrating large language model (LM) inference at scale, particularly focusing on prefill-decode (PD) disaggregation. He explains that traditional Kubernetes deployments stru..."
resource: https://www.youtube.com/watch?v=KtnD-wILqb0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Junhu from Haw Club discusses the challenges and solutions for orchestrating large language model (LM) inference at scale, particularly focusing on prefill-decode (PD) disaggregation.
He explains that traditional Kubernetes deployments struggle with LM inference due to the unique resource and scheduling requirements of LMs, such as large memory needs and strict GPU scheduling.
To address interference between the highly parallel prefill stage and the memory-bound decode stage, the industry is moving toward PD disaggregation, where prefill and decode are handled by separate GPU instances.
However, this introduces new challenges in routing, scaling, and network topology, which standard Kubernetes cannot efficiently manage.
To solve these issues, the Volcano community developed Casina, an open-source orchestration tool designed specifically for LM inference, offering intelligent routing, dynamic autoscaling, topology-aware scheduling, and seamless integration with Kubernetes APIs.
Casina enables flexible, efficient, and scalable deployment of disaggregated LM inference workloads, and continues to evolve with new features for heterogeneous hardware support and advanced scheduling.
# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on large language model (LM) inference at scale and orchestration of prefill-decode (PD) disaggregation.                               |
|   2 | Speaker: Junhu from Haw Club, tech leader, Volcano and Kimsh maintainer, open source contributor.                                                           |
|   3 | AI infrastructure is evolving beyond traditional deployment patterns toward efficient, cloud-native systems for distributed inference.                      |
|   4 | Kubernetes excels at stateless microservices but struggles with LM inference due to large model weights, massive KV cache, and strict GPU scheduling needs. |
|   5 | LM inference has two stages: prefill (highly parallel, compute-bound) and decode (memory bandwidth-bound, token-by-token generation).                       |
|   6 | Running prefill and decode on the same GPU causes resource contention, latency spikes, and underutilization.                                                |
|   7 | User experience is measured by TTFT (time to first token) and TPOT (time per output token); coupled architectures force trade-offs between these.           |
|   8 | Solution: Disaggregate prefill and decode stages onto separate GPU instances to eliminate interference.                                                     |
|   9 | XPYD model: X = prefill instances, Y = decode instances; enables symmetric, workload-specific scaling.                                                      |
|  10 | Disaggregation introduces network bottlenecks due to large KV cache transfers between nodes.                                                                |
|  11 | Vanilla Kubernetes is topology-blind, complicating XPYD orchestration, scaling, and efficient scheduling.                                                   |
|  12 | Casina, a subproject of Volcano, is built to orchestrate LM inference with native support for PD disaggregation.                                            |
|  13 | Casina architecture: router (traffic routing) and control manager (workload management) with a simple model serving API.                                    |
|  14 | Three CRDs: model server (inference engine), model router (traffic rules), model serving (workload orchestration).                                          |
|  15 | Supports hierarchical, multi-level scheduling and topology-aware placement for optimal performance.                                                         |
|  16 | Casina enables dynamic, elastic scaling of prefill and decode instances based on stage-specific metrics.                                                    |
|  17 | Supports both homogeneous and heterogeneous autoscaling with built-in optimizers.                                                                           |
|  18 | Casina router prov                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=KtnD-wILqb0)