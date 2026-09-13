---
layout: default
title:
  "LMCache: Lower LLM Performance Costs in the Enterprise - Martin Hickey & Junchen
  Jiang"
nav_order: 6
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  The speakers at CubeCon Atlanta discuss the evolution of cloud infrastructure
  and AI workloads, highlighting the shift from concerns about virtual machines to
  the current focus on deploying and optimizing AI inference, particularly large la...
resource: https://www.youtube.com/watch?v=V4CNYLxT9DA
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speakers at CubeCon Atlanta discuss the evolution of cloud infrastructure and AI workloads, highlighting the shift from concerns about virtual machines to the current focus on deploying and optimizing AI inference, particularly large language models (LLMs).
They explain that as LLMs handle increasingly long context windows, both computational delay and cost rise significantly, making efficient management of model memory—specifically KV (key-value) cache—crucial.
KV cache stores reusable runtime memory, allowing models to skip redundant processing when the same context is used across multiple queries, thus improving performance and reducing costs.
The LM Cache open source project, developed by researchers at the University of Chicago, provides a unified library for sharing and offloading KV cache across GPUs, CPUs, and various storage backends, supporting multiple inference engines and enabling asynchronous, efficient cache management.
The talk concludes by emphasizing LM Cache’s role in addressing the challenges of AI inference at scale and inviting the community to contribute and explore the project further.

# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CubeCon Atlanta session focused on AI workloads and KV caching.                                                                                                                                           |
|   2 | AI workloads have shifted from training to inference/model serving as the primary focus.                                                                                                                  |
|   3 | Large language models (LLMs) are now pervasive and present new system challenges, especially with long context inference.                                                                                 |
|   4 | Longer context windows in LLMs increase processing delay (time to first token) and computational cost.                                                                                                    |
|   5 | KV cache is the model's runtime memory, storing attention information as two large tensors in GPU memory.                                                                                                 |
|   6 | KV cache enables models to reuse context information, reducing the need to reprocess the same input for multiple queries.                                                                                 |
|   7 | Reusing KV cache can significantly improve performance and lower costs for AI inference.                                                                                                                  |
|   8 | Traditional ML engines discard KV cache after each query; LM Cache project enables persistent and shareable KV cache storage across CPU, disk, or remote storage.                                         |
|   9 | LM Cache supports sharing KV cache across multiple inference engines and hardware via various network protocols.                                                                                          |
|  10 | LM Cache is an open-source library/framework, part of the PyTorch Foundation, with a permissive license.                                                                                                  |
|  11 | Key LM Cache components: cache engine (manages connections and storage backends), connectors (interface with inference engines), backends (storage options), and workers (manage cache across instances). |
|  12 | LM Cache optimizes memory usage by converting fine-grained memory to coarser chunks for better IO performance.                                                                                            |
|  13 | Supports asynchronous operations to avoid blocking inference processes.                                                                                                                                   |
|  14 | Provides configurable connectors for various storage backends (e.g., Redis, Moon Cake, S3) and allows custom backend extensions.                                                                          |
|  15 | Implements layer-wise pipelining for parallel execution and improved performance.                                                                                                                         |
|  16 | Offers cache management features: locating, moving, deleting, and reusing caches.                                                                                                                         |
|  17 | Community encouraged to contribute, check documentation, and engage with the project.                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=V4CNYLxT9DA)
