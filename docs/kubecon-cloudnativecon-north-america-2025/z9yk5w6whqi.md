---
layout: default
title:
  "Help! My LLM Is a Resource Hog: How We Tamed Inference With Kubernetes...
  Aditya Soni & Hrittik Roy"
nav_order: 96
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speaker, Sunni, discusses the challenges of inference in Large Language
  Models (LLMs) and how to optimize them. They explain that LLMs require massive parallel
  computation, which is difficult to achieve with CPUs but can be done with GP...
resource: https://www.youtube.com/watch?v=z9yK5W6whQI
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker, Sunni, discusses the challenges of inference in Large Language Models (LLMs) and how to optimize them.
They explain that LLMs require massive parallel computation, which is difficult to achieve with CPUs but can be done with GPUs.
However, increasing GPU utilization is not always effective due to various issues such as KV caching, GPU underutilization, and optimization problems.
To address these challenges, Sunni proposes three solutions: optimizing KV caching, improving GPU utilization through batching and sharing, and observing and profiling the system to identify areas for improvement.
They also discuss the importance of distributed inference across different geol locations and providers, highlighting the need for solutions such as MOE routing and cross-node communication to enable efficient sharing of GPUs.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | LLMs (Large Language Models) are used in various applications, including research cycles, revenue gains, and cost savings.                                  |
|   2 | The basic architecture of LLMs includes a tokenizer, router, batcher, KV caches, and inference.                                                             |
|   3 | The history of LLMs starts from engrams and evolved to transformers, which changed the way everything works.                                                |
|   4 | Transformers require GPUs for parallel computation, but CPUs are not suitable for this task.                                                                |
|   5 | Increasing GPU resources is not always helpful due to GPU shortages and optimization challenges.                                                            |
|   6 | Inference is a critical component of LLMs, and it can be slow due to various issues such as KV caching, GPU underutilization, and latency.                  |
|   7 | KV caching can be optimized using techniques like VLM, LLMD, and tiered caching.                                                                            |
|   8 | GPU utilization can be improved through batching, sharing, and scheduling techniques like time slicing and Kai scheduleuler.                                |
|   9 | Observing and profiling GPU usage can help reduce costs by identifying bottlenecks and optimizing performance.                                              |
|  10 | Distributed inference across geol locations and providers poses challenges such as distributed attention kernels, KV caching, and cross-node communication. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=z9yK5W6whQI)
