---
layout: default
title:
  "Thousands of Virtual Kubelets: 1-to-1 Mapping a Supercomputer To Kubernetes
  With... Dennis Marttinen"
nav_order: 344
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Deness, a security and cloud computing master student, discussed bridging
  the gap between high-performance computing (HPC) and cloud ecosystems through Kubernetes.
  He highlighted the differences in assumptions between HPC and cloud computin...
resource: https://www.youtube.com/watch?v=QbR908kgk1Y
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Deness, a security and cloud computing master student, discussed bridging the gap between high-performance computing (HPC) and cloud ecosystems through Kubernetes.
He highlighted the differences in assumptions between HPC and cloud computing, where HPC assumes finite resources and infinite demand, whereas cloud computing assumes infinite resources and finite demand.
With the increasing demand for AI workloads, the lines between HPC and cloud requirements are becoming increasingly similar.
Deness presented his master's thesis project, "Kubernetes," which aims to connect a Kubernetes environment with an HPC environment using virtual cublets.
This allows for seamless integration of HPC and cloud ecosystems, enabling better security, automation, broader ecosystem support, improved utilization, reduced downtime, and lower costs.
The goal is to unite the communities from both HPC and cloud ecosystems, making projects more accessible to everyone.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The difference between cloud and HPC is that cloud workloads are typically bound to a small set of nodes, while HPC workloads may span across the entire system.       |
|   2 | With the increasing demand for AI workloads, the tables have turned, and cloud and HPC requirements look increasingly similar.                                         |
|   3 | Modern HPC and cloud hardware is surprisingly similar, but the software stack differs.                                                                                 |
|   4 | Kubernetes and Slurm are fundamentally similar distributed systems, with differences in API interfaces and node agents.                                                |
|   5 | The main difference between Kubernetes and Slurm lies in their high-level architectures and goals.                                                                     |
|   6 | Kubernetes strengths lie in its versatility and self-healing abilities, while Slurm excels in scheduling large-scale multi-node workloads.                             |
|   7 | A bridge solution is needed to integrate HPC and cloud ecosystems, with Kubernetes being a promising candidate.                                                        |
|   8 | The first reason for integrating HPC and cloud communities was the need for a more efficient way to run AI workloads on Lumi, an AMD-based supercomputer.              |
|   9 | Intermediate steps are necessary to make the transition seamless, including isolating jobs running in Slurm into separate network namespaces and implementing proxies. |
|  10 | A sbatch wrapper could create job sets that can be scheduled by Q, allowing users to integrate their AI training and inference backends with HPC ecosystems.           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QbR908kgk1Y)
