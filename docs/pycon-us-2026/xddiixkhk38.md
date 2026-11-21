---
layout: default
title: "High Performance LLM Inference in Pure Python with PyTorch Custom Ops - Yineng Zhang"
nav_order: 48
parent: PyCon US 2026
type: Video Note
description: "Yinan Zhang from Tigon AI argues that modern large language model inference systems are no longer defined by a simple choice between Python and C++, but rather by a layered architecture where Pytho..."
resource: "https://www.youtube.com/watch?v=XdDiixKHk38"
youtube_stats:
  view_count: 682
  like_count: 14
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

Yinan Zhang from Tigon AI argues that modern large language model inference systems are no longer defined by a simple choice between Python and C++, but rather by a layered architecture where Python serves as an orchestration layer while heavy computation is offloaded to native GPU kernels.
To achieve performance competitive with highly optimized native runtimes like TensorRT-LLM, the system employs several key strategies: separating CPU-intensive tasks like tokenization into independent processes to avoid blocking the GPU, overlapping CPU scheduling with GPU execution to hide latency, and using CUDA graphs to minimize kernel launch overhead.
The talk highlights that while Python excels at rapid iteration and execution planning, complex state management and scheduling logic are better handled by dedicated C++ components with Python bindings to ensure correctness and resource ownership.
This approach is exemplified by TokenSpeed, an open-source inference engine that combines Python’s flexibility with high-performance native kernels, such as optimized MLA attention, to deliver efficient and scalable inference.
Ultimately, the core lesson is that the future of AI infrastructure lies in choosing the right abstraction boundaries for each layer, allowing different components to be optimized for their specific responsibilities within a heterogeneous system.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Modern LLM inference systems are heterogeneous where Python acts as an orchestration layer rather than executing heavy tensor computations directly.                                     |
|   2 | The primary performance question is determining which components should run in Python versus native code to optimize overall system efficiency.                                          |
|   3 | Multi-process runtime architecture isolates CPU-intensive tasks like tokenization and detokenization into separate processes to prevent GIL contention from blocking GPU work.           |
|   4 | CPU-GPU overlap execution allows the CPU to prepare the next inference step while the GPU executes the current one, effectively hiding scheduling overhead behind GPU execution time.    |
|   5 | CUDA graphs capture and replay stable execution patterns to significantly reduce per-iteration kernel launch and Python dispatch overhead on the critical path.                          |
|   6 | Performance-critical operations are implemented in native kernels such as CUDA, Triton, or vendor-specific libraries, which are exposed to Python via PyTorch custom ops.                |
|   7 | PyTorch serves as the tensor runtime layer handling memory management and stream semantics, while Python coordinates the broader execution plan.                                         |
|   8 | As inference systems scale, complexity shifts from tensor computation to state management, resource ownership, and asynchronous orchestration correctness.                               |
|   9 | Large-scale control planes require strong inference and interface constraints, often implemented in C++ with Python bindings to ensure robust state transition and rollback safety.      |
|  10 | TokenSpeed is an open-source inference engine designed with a layered architecture that separates responsibilities for iteration speed, hardware efficiency, and scheduling correctness. |
|  11 | The TokenSpeed architecture consists of a kernel layer for GPU computation, a Python execution plan layer, a C++ scheduler for state management, and a frontend for API serving.         |
|  12 | TokenSpeed achieves performance competitive with or exceeding TensorRT-LLM by leveraging optimized MLA attention kernels and efficient CUDA graph usage.                                 |
|  13 | The TokenSpeed MLA attention kernel is packaged as a standalone PyPI library and integrated into frameworks like vLLM to benefit the broader AI community.                               |
|  14 | Benchmarking against TensorRT-LLM on Blackwell hardware shows TokenSpeed can be 10% to 20% faster in iteration time due to optimized timeline and kernel selection.                      |
|  15 | The future of AI inference lies in choosing the right abstraction boundaries for each layer rather than competing between Python and native languages.                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XdDiixKHk38/hqdefault.jpg)](https://www.youtube.com/watch?v=XdDiixKHk38)

[Watch on YouTube](https://www.youtube.com/watch?v=XdDiixKHk38)
