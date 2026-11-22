---
layout: default
title: "GPU Programming in Pure Python - Bryce Adelstein Lelbach"
nav_order: 61
parent: PyCon US 2025
type: Video Note
description: "Bryce Edstrom, a principal architect at NVIDIA, presents a session on GPU programming in pure Python, emphasizing that while parallelism is essential for modern performance, developers should prior..."
resource: "https://www.youtube.com/watch?v=8utSRblGEB0"
youtube_stats:
  view_count: 3321
  like_count: 101
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Bryce Edstrom, a principal architect at NVIDIA, presents a session on GPU programming in pure Python, emphasizing that while parallelism is essential for modern performance, developers should prioritize using existing optimized libraries like CuPy and PyTorch before writing custom kernels.
For cases requiring custom code, he demonstrates how Numba CUDA allows Python developers to write high-performance GPU kernels that match the speed of native CUDA C++, utilizing Numba’s JIT compilation to bypass the Python interpreter for maximum efficiency.
The talk details critical GPU architecture concepts, such as the hierarchy of warps, blocks, and grids, and explains the importance of memory coalescing to minimize latency and maximize bandwidth, contrasting these requirements with CPU-centric thinking.
Edstrom showcases practical implementations of copy, matrix transpose, and softmax kernels using CUDA cooperative primitives, which enable efficient block-wide communication and data movement through shared memory.
Finally, he introduces "Coupile," a new tile-based programming model designed to abstract low-level parallelism and memory management, offering a more Pythonic and portable approach to GPU development while maintaining peak performance.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Parallel programming is essential because modern hardware is inherently parallel, requiring developers to shift from sequential to parallel thinking.                                    |
|   2 | GPUs are optimized for high bandwidth and massive parallelism, handling hundreds of thousands of threads, whereas CPUs are optimized for low latency and powerful individual cores.      |
|   3 | GPU acceleration is most effective for workloads with high operational intensity or large data sizes, such as matrix multiplication or processing gigabytes of data.                     |
|   4 | The primary recommendation is to use existing GPU-accelerated libraries like CuPy, PyTorch, or CuDF before writing custom kernels, as they offer expert-tuned performance.               |
|   5 | Numba CUDA allows writing GPU kernels in pure Python that compile to native code with performance equivalent to CUDA C++.                                                                |
|   6 | Numba uses a non-CPython compilation mode that removes the Python interpreter overhead, enabling direct lowering to native instructions but requiring manual memory lifetime management. |
|   7 | GPU threads are organized into a hierarchy of warps, thread blocks, and thread grids, with warps executing instructions in lockstep.                                                     |
|   8 | Memory coalescing is critical for GPU performance, requiring threads in a warp to access contiguous memory addresses to minimize memory transactions.                                    |
|   9 | GPU memory hierarchy includes fast local registers, shared memory for block-level communication, and slower global memory with hardware caching.                                         |
|  10 | The CuBLAS and CUB libraries provide cooperative parallel primitives for loads, stores, reductions, and scans that can be used within Python kernels.                                    |
|  11 | Using CUB primitives in Python requires explicit shared memory allocation and linking of binary objects, though future updates may automate these steps.                                 |
|  12 | Efficient matrix transposition on GPUs involves splitting data into 2D tiles, using striped loads for coalescing, and local exchanges to transpose within shared memory.                 |
|  13 | Softmax computation requires block-wide reductions for maximum and sum operations, which can be implemented using CUB primitives to ensure numerical stability.                          |
|  14 | Managing device arrays explicitly using Numba CUDA or libraries like CuPy is recommended to avoid implicit synchronization and data transfer overheads.                                  |
|  15 | NVIDIA is developing CuTile, a higher-level tile programming model that abstracts block-level parallelism and memory movement for more Pythonic GPU code.                                |
|  16 | Writing custom kernels remains a tool of last resort, as hardware vendors continuously optimize libraries to maintain speed-of-light performance on new architectures.                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8utSRblGEB0/hqdefault.jpg)](https://www.youtube.com/watch?v=8utSRblGEB0)

[Watch on YouTube](https://www.youtube.com/watch?v=8utSRblGEB0)
