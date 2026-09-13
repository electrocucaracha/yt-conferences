---
type: Video Note
title: "Project Lightning Talk: Next-Gen AI Orchestration With Volcano On Kubernetes - Zhonghu Xu"
description: "The speaker, a maintainer from Huawei Technology, introduces Volcano, a cloud-native batch system for Kubernetes that manages queueing, scheduling, and supports heterogeneous devices. As AI workloads have evolved, especially with the rise o..."
resource: https://www.youtube.com/watch?v=0vYUzJ7eO8M
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a maintainer from Huawei Technology, introduces Volcano, a cloud-native batch system for Kubernetes that manages queueing, scheduling, and supports heterogeneous devices.
As AI workloads have evolved, especially with the rise of large language models and agent workloads, Volcano has adapted to handle diverse and resource-intensive tasks, aiming to become a unified scheduling platform for AI training, inference, and agent workflows.
Recent updates include the introduction of an agent scheduler for latency-sensitive workloads, enhancements in network topology-aware scheduling through the Hypernode abstraction, and efforts to make Hypernode a first-class Kubernetes entity for better modeling of network domains.
Additionally, two subprojects are highlighted: Casino, a native serving platform with intelligent routing and autoscaling for inference workloads, and Agent Cube, which focuses on AI agent workload scheduling and provides SDKs for building agent tools.
The speaker concludes by encouraging collaboration on these initiatives.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter is from Huawei and a maintainer of Volcano.                                                                                                        |
|   2 | Topic: Next-gen AI orchestration with Volcano on Kubernetes.                                                                                                 |
|   3 | Volcano originated from kube-batch and serves as a cloud-native batch system.                                                                                |
|   4 | Supports queue management, GA scheduling, rich ecosystem, and heterogeneous devices.                                                                         |
|   5 | Shift in cluster workloads: from batch training to large language models and OM training in 2023.                                                            |
|   6 | New workload types: disaggregated OM inference (with different resource needs for prefetch and decode) and bursty, short-lived agent workloads.              |
|   7 | Diverse workloads challenge schedulers.                                                                                                                      |
|   8 | Volcano widely used in AI training since incubation.                                                                                                         |
|   9 | Volcano aims to evolve into a unified scheduling platform for AI training, inference, and agent workflows.                                                   |
|  10 | Roadmap:                                                                                                                                                     |
|  11 | Support for VC jobs and more native workloads.                                                                                                               |
|  12 | Collaboration with communities in reinforcement learning, inference, and agent frameworks.                                                                   |
|  13 | Enhanced support for heterogeneous devices.                                                                                                                  |
|  14 | Improved network architecture features and topology-aware scheduling.                                                                                        |
|  15 | Recent updates:                                                                                                                                              |
|  16 | Introduction of "agent-scheduler" for latency-sensitive, bursty agent workloads, coordinated with the existing batch scheduler.                              |
|  17 | Sharding controller added to manage node CRDs and dynamic node ports.                                                                                        |
|  18 | Network topology-aware scheduling:                                                                                                                           |
|  19 | Large AI clusters lack unified topology abstraction.                                                                                                         |
|  20 | Built "hypernode" to model network domains and improve scheduling precision.                                                                                 |
|  21 | Hypernode creation can be manual or via pluggable auto-discovery (supports NVIDIA FAB, manual, and node label discovery).                                    |
|  22 | Goal to make hypernode a Kubernetes first-class citizen for better network status representation.                                                            |
|  23 | Call for co-creation on the hypernode initiative.                                                                                                            |
|  24 | Two subprojects:                                                                                                                                             |
|  25 | Casino: Native serving platform, supports multiple inference frameworks, autoscaling, intelligent routing, KV cache, and integrates with Volcano scheduling. |
|  26 | Agent Cube: AI agent workload scheduling, built on SIG sandbox, plans for more native agent primitives, broader frame                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0vYUzJ7eO8M)