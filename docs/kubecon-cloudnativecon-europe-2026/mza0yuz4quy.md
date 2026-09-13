---
layout: default
title:
  "Volcano: Orchestrating the Full AI Lifecycle – From Training To Inferen...
  Chen Zicong & Hajnal Máté"
nav_order: 390
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation introduces Volcano, a unified batch scheduling platform
  that has evolved from a simple batch scheduler to orchestrate the full AI lifecycle,
  including training, inference, and bursty agent workloads. The speakers, Matty Hel...
resource: https://www.youtube.com/watch?v=mzA0yuZ4QuY
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

The presentation introduces Volcano, a unified batch scheduling platform that has evolved from a simple batch scheduler to orchestrate the full AI lifecycle, including training, inference, and bursty agent workloads.
The speakers, Matty Hel and Jesse, outline Volcano’s integration with various AI frameworks, its advanced queue management, support for heterogeneous devices, and unique features like workload collocation and multicluster scheduling.
Recent developments include the introduction of the Agentuler for latency-sensitive workloads, dynamic sharding for efficient resource allocation, and enhanced network topology-aware scheduling using hypernodes.
The session also highlights subprojects such as Casina (an LLM serving platform), Agent Cube (for AI agent workloads), and Volcano Global (for multicluster scheduling), each addressing specific needs in AI workload management.
The team emphasizes ongoing work to further integrate with cloud providers and open-source projects, and calls for community contributions to advance Volcano as a comprehensive, unified scheduling solution for diverse AI workloads.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Volcano orchestrates the full AI lifecycle, from training to inference and bursty agent workloads.                                                     |
|   2 | Speakers: Jesse (R&D engineer, Volcano maintainer, Huawei) and Matty Hel (Senior ML engineer, Movio).                                                  |
|   3 | Volcano evolved from a simple batch scheduler (Kube-batch) to a unified batch scheduling platform.                                                     |
|   4 | Became a CNCF project in 2020, reached incubating status in 2022, aiming for graduated status in 2026.                                                 |
|   5 | Supports diverse workloads: TensorFlow, MPI, Spark, and more.                                                                                          |
|   6 | Features include multi-level queue management, workload collocation (online/offline separation), and multicluster scheduling via Volcano Global.       |
|   7 | Supports heterogeneous devices: GPUs, MPUs, TPUs, etc.                                                                                                 |
|   8 | Offers numerous scheduling policies: beam pack, network topology-aware, gang, NUMA, device share, and task topology scheduling.                        |
|   9 | AI workloads are rapidly evolving: batch training, distributed LLM training, disaggregated LLM inference, and bursty agentic workloads.                |
|  10 | Introduced agentuler in v4.14 for fast, parallel scheduling of latency-sensitive, bursty agentic workloads.                                            |
|  11 | Agentuler and batch scheduler coordinate via a new sharding mechanism managed by the sharding manager and node shard CRD.                              |
|  12 | Dynamic, pluggable sharding strategies allow horizontal and vertical partitioning for resource optimization and workload isolation.                    |
|  13 | Workload collocation enables dynamic resource oversubscription and improved cluster utilization, managed by the SLO agent.                             |
|  14 | CPU burst feature allows pods to temporarily exceed CPU limits for short periods.                                                                      |
|  15 | Full cgroup v2 integration and collocation configuration via CRD.                                                                                      |
|  16 | Hypernode-based topology-aware scheduling abstracts network topology, supports auto-discovery, subgroup constraints, and hypernode-level beam packing. |
|  17 | Integrates with various network protocols and device managers (e.g., Nvidia, Infiniband, Rocky).                                                       |
|  18 | Subprojects:                                                                                                                                           |
|  19 | Casina: Kubernetes-native LLM serving platform with auto-scaling, intelligent routing, and perf/decode disaggregation.                                 |
|  20 | Agent Cube: Ku                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mzA0yuZ4QuY)
