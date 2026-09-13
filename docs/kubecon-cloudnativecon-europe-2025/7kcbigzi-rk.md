---
layout: default
title:
  Building & Operating a Large-scale HPC AI Cluster on Kubernetes - Kalyan Saladi
  & Chandan Avdhut
nav_order: 32
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The presentation discusses building an AI HPC cluster on top of Kubernetes
  in public cloud, with a focus on researcher experience and reliability. The speaker
  explains how they used Kubernetes to manage infrastructure across multiple cloud...
resource: https://www.youtube.com/watch?v=7KCBigZi_Rk
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

The presentation discusses building an AI HPC cluster on top of Kubernetes in public cloud, with a focus on researcher experience and reliability.
The speaker explains how they used Kubernetes to manage infrastructure across multiple cloud providers, while maintaining a consistent experience for researchers who use Slurm for their workloads.
The team implemented custom solutions, such as a CLI to simplify the research workflow and a monitoring system to track node failures, to ensure reliability and performance.
They also discussed the challenges of scaling HPC workloads in Kubernetes and the importance of observability.

# Main Points

|   # | Main point                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------- |
|   1 | Overview of AI/ML training, infrastructure requirements, node lifecycle management, and storage aspects. |
|   2 | Importance of researcher experience, reliability, and observability in ML research clusters.             |
|   3 | Comparison between on-premises and public cloud environments for ML research clusters.                   |
|   4 | Use of Kubernetes to manage and orchestrate the cluster.                                                 |
|   5 | Custom CLI created for researchers to interact with the cluster without learning Kubernetes.             |
|   6 | Slurm used as a job scheduler within the Kubernetes cluster.                                             |
|   7 | Importance of observability and reliability in the cluster.                                              |
|   8 | Consideration of using open-source Kubernetes operators to manage Slurm.                                 |
|   9 | Potential for hybrid on-premises and public cloud environments.                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7KCBigZi_Rk)
