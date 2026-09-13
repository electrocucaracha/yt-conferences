---
layout: default
title: Scaling GPU Clusters Without Melting Down! - Alay Patel & Ryan Hallisey, NVIDIA
nav_order: 297
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  NVIDIA engineers Ryan Haly and Olay Patel discuss their experiment to
  scale Kubernetes control plane independently of compute resources, specifically
  with regards to GPU-accelerated workloads. They encountered several challenges,
  including...
resource: https://www.youtube.com/watch?v=dUfp3j1j-mg
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

NVIDIA engineers Ryan Haly and Olay Patel discuss their experiment to scale Kubernetes control plane independently of compute resources, specifically with regards to GPU-accelerated workloads.
They encountered several challenges, including large numbers of list calls to secrets causing API server outages due to memory constraints.
To address this issue, they used API priority and fairness to limit concurrent list calls, resulting in reduced memory utilization.
Additionally, they fine-tuned the Go garbage collector (GC) to make it more aggressive, reducing memory usage across the control plane.
They also implemented a solution for handling skewed memory utilization between API servers, using the "goaway" chance parameter to probabilistically tear down existing connections and create new ones.
The team used Quark, a Kubernetes simulation tool, to scale test their control plane with both topo-aware scheduleuler and DRRA, finding that DRRA resulted in significant improvements in scheduling latency, memory utilization, and API server performance.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dUfp3j1j-mg)
