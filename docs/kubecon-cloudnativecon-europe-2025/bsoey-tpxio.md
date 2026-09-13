---
layout: default
title:
  Efficient Transparent Checkpointing of AI/ML Workloads in Kub... R. Stoyanov,
  A. Reber, V. Spišáková
nav_order: 80
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The presentation discusses efficient transparent checkpointing for AI
  workloads in Kubernetes. The goal is to improve resource utilization and provide
  fault tolerance for GPU-accelerated workloads. Researchers from Czech National Infrastruc...
resource: https://www.youtube.com/watch?v=BSoEY_tpxIo
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

The presentation discusses efficient transparent checkpointing for AI workloads in Kubernetes.
The goal is to improve resource utilization and provide fault tolerance for GPU-accelerated workloads.
Researchers from Czech National Infrastructure, Nvidia, and AMD collaborated on this project.
They identified three key insights: (1) computational nodes are often occupied due to generous requests, but real utilization is low; (2) batch workloads like AlphaFold have fine GPU utilization, but long-running jobs can be problematic for fault tolerance; and (3) interactive workloads like Jupyter notebooks have unpredictable and dynamic GPU utilization.
The team proposes using transparent GPU checkpointing as a solution, which allows for efficient and transparent checkpointing of GPU applications without the application knowing it's being checkpointed or restored.
This approach has been integrated into Kubernetes and has shown promising results in demos, including faster startup times and improved resource utilization.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BSoEY_tpxIo)
