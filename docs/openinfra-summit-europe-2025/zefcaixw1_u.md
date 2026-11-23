---
layout: default
title: "GAIA: CINECA’s large-scale HPC Cloud infrastructure for scientific and technological research"
nav_order: 61
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker from the Italian non-profit consortium Cineca presents Gaia, a new large-scale HPC cloud infrastructure designed to combine high performance with flexibility for scientific and technolo..."
resource: "https://www.youtube.com/watch?v=ZefCAIXw1_U"
youtube_stats:
  view_count: 119
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

The speaker from the Italian non-profit consortium Cineca presents Gaia, a new large-scale HPC cloud infrastructure designed to combine high performance with flexibility for scientific and technological research.
As the fourth iteration of Cineca’s open-tech HPC cloud, Gaia is intended to host diverse workloads, including general-purpose virtual machines, trusted research tasks, and complex Kubernetes-based applications, while maintaining ISO 27001 certification standards.
The system, originally planned for the Casalecchio data center, was relocated to the Technoborg data center in Bologna due to loading issues, where it will operate alongside other flagship systems like Leonardo and Lisa.
Gaia comprises 500 compute nodes, including 200 CPU-only nodes and 80 GPU nodes equipped with 256 NVIDIA GPUs (A30, L40S, and H100), all connected by a 100 GbE network and supported by 50 PB of multi-protocol VAST storage for disaster recovery and shared data access.
To ensure stability before production launch at the end of the year, the team is conducting rigorous load testing using Rally, simulating over 1,000 users and 14,000 concurrent virtual machines to validate the system’s resilience and performance under real-world conditions.

# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker presents Gaia, a new large-scale HPC cloud infrastructure installed by Cineca, a non-profit Italian consortium.                 |
|   2 | Cineca provides IT and HPC services to academic and research institutions, with a focus on high-performance computing.                      |
|   3 | Gaia is the first HPC cloud infrastructure in Italy dedicated to scientific and technological research.                                     |
|   4 | The system combines flexibility and high performance, supporting both general-purpose use cases and trusted research workloads.             |
|   5 | Gaia is planned to host Kubernetes on top of OpenStack, complex workloads with GPU or CPU nodes, and cloud-cluster bridging services.       |
|   6 | The tender for Gaia was released in October 2023 and awarded in the first half of 2024.                                                     |
|   7 | Due to loading issues at the Casalecchio data center, Gaia was relocated to the Technoborg data center in Bologna.                          |
|   8 | Gaia consists of 24 racks, including 18 for the HPC cloud part, 50 petabytes of storage, and a prototype rack.                              |
|   9 | The infrastructure includes 500 compute nodes, with 256 GPUs of three types: Ampere A30, L40S, and Hopper H100.                             |
|  10 | CPU nodes total 420 with 120,000 Intel cores, while GPU nodes total 80 with 256 GPUs.                                                       |
|  11 | The system features 100 GbE network connectivity and 10 petabytes of Ceph storage for the cluster.                                          |
|  12 | A 50-petabyte VAST data lake supports multi-protocol access and disaster recovery between Bologna and Naples.                               |
|  13 | The controller partition includes 25 nodes with additional storage to avoid single points of failure.                                       |
|  14 | Gaia will support ISO 27001 certification for trusted workloads, similar to the existing Ada system.                                        |
|  15 | The virtualization layer uses OpenStack, with installation support from Start HPC and partners like Kube and Colans.                        |
|  16 | Load testing will use Rally to simulate over 1,000 users and 14,000 virtual machines simultaneously.                                        |
|  17 | Two test tasks are planned: "Task Services" for sequential service stability and "Task Production" for real-world user behavior simulation. |
|  18 | Task Production involves a custom Rally plugin with randomized actions and FIO benchmarks inside virtual machines.                          |
|  19 | The system aims to host 20,000 volumes and 14,000 VMs concurrently, with tests scheduled before production launch.                          |
|  20 | Gaia is integrated with other Cineca systems like Leonardo, Lisa, and Marco for a unified research ecosystem.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZefCAIXw1_U/hqdefault.jpg)](https://www.youtube.com/watch?v=ZefCAIXw1_U)

[Watch on YouTube](https://www.youtube.com/watch?v=ZefCAIXw1_U)
