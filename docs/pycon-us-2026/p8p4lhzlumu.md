---
layout: default
title: "What Python Developers Need to Know About Hardware: A Practical Guide...- Vyas Ramasubramani"
nav_order: 57
parent: PyCon US 2026
type: Video Note
description: "Viqas, a senior software engineer at Nvidia, presents a comprehensive overview of GPU architecture and optimization strategies, emphasizing that while GPUs are often perceived as complex, many unde..."
resource: "https://www.youtube.com/watch?v=P8P4lHzlUMU"
youtube_stats:
  view_count: 511
  like_count: 7
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Viqas, a senior software engineer at Nvidia, presents a comprehensive overview of GPU architecture and optimization strategies, emphasizing that while GPUs are often perceived as complex, many underlying concepts are familiar to Python developers.
He explains that unlike CPUs, which prioritize minimizing latency through features like branch prediction and vectorization, GPUs are designed to maximize throughput by leveraging massive parallelism and high memory bandwidth.
To achieve optimal performance, developers must manage several critical factors: utilizing Just-In-Time (JIT) compilation caches to avoid repeated overhead, employing kernel fusion to reduce expensive CPU-to-GPU launch costs, and maintaining asynchronous execution to keep both CPU and GPU resources busy.
Additionally, the talk highlights the importance of explicit memory management on GPUs, as they lack the automatic latency-hiding mechanisms found in CPUs, and warns that floating-point arithmetic is non-associative, meaning parallel execution can yield slightly different results than sequential processing.
Finally, the presentation concludes with practical advice on structuring data to minimize branching, scheduling concurrent kernels to saturate hardware resources, and benchmarking specific workloads to account for architectural differences, such as those in unified memory systems.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | GPU code translation involves a complex process where Just-In-Time (JIT) compilation is implicitly required at runtime to adapt code to specific GPU architectures.                                  |
|   2 | JIT compilation causes initial execution delays, but enabling persistent caching in libraries like CuPy, Torch, and JAX prevents repeated compilation costs in ephemeral environments.               |
|   3 | Launching CUDA kernels is significantly more expensive than calling CPU functions, with overhead reaching three orders of magnitude higher.                                                          |
|   4 | Kernel fusion allows multiple point-wise operations to be combined into a single kernel, reducing launch overhead and improving performance.                                                         |
|   5 | GPU execution is asynchronous, allowing the CPU to continue processing or launch additional kernels while the GPU is busy, which helps hide latency.                                                 |
|   6 | Synchronization points are expensive and should be minimized to prevent the CPU from stalling while waiting for GPU completion.                                                                      |
|   7 | Unlike CPUs, which handle memory hierarchy automatically, GPUs require explicit management of data transfers and special memory spaces like shared memory.                                           |
|   8 | Manual memory migration is often necessary on GPUs because automatic decisions can lead to significant performance penalties due to high latency and lack of built-in latency hiding.                |
|   9 | GPUs are designed to maximize throughput rather than minimize latency, utilizing massive parallelism to process large volumes of data simultaneously.                                                |
|  10 | Modern GPUs offer significantly higher memory bandwidth and parallel thread counts compared to CPUs, enabling them to utilize large data transfers efficiently.                                      |
|  11 | Branching code is highly inefficient on GPUs because they lack the branch prediction and prefetching hardware optimizations found in CPUs.                                                           |
|  12 | To optimize GPU performance, data should be structured to avoid branching, such as by sorting or chunking data so that all threads follow the same code path.                                        |
|  13 | Floating-point arithmetic is non-associative, meaning parallel execution can produce slightly different results than sequential execution due to the order of operations.                            |
|  14 | Deterministic modes in libraries like Torch and TensorFlow can provide consistent results during prototyping, though these guarantees do not persist across different hardware or software versions. |
|  15 | When scheduling multiple concurrent kernels, developers must calculate resource allocation to ensure the GPU scheduler can execute them in parallel without exceeding hardware limits.               |
|  16 | Unified memory systems reduce the cost of data transfer between CPU and GPU, but peak performance still requires application-specific benchmarking.                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/P8P4lHzlUMU/hqdefault.jpg)](https://www.youtube.com/watch?v=P8P4lHzlUMU)

[Watch on YouTube](https://www.youtube.com/watch?v=P8P4lHzlUMU)
