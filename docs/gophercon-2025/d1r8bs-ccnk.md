---
layout: default
title: "GopherCon 2025: Go Faster: Integrating CUDA in Go for GPU Acceleration - Sam Burns"
nav_order: 5
parent: GopherCon 2025
type: Video Note
description: "Sam Burns, a software architect and application security specialist, presents a technical overview of integrating CUDA GPU programming with Go applications."
resource: "https://www.youtube.com/watch?v=d1R8BS-ccNk"
youtube_stats:
  view_count: 1745
  like_count: 35
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Sam Burns, a software architect and application security specialist, presents a technical overview of integrating CUDA GPU programming with Go applications.
The talk begins by contrasting CPU and GPU architectures, explaining that while CPUs excel at complex, low-latency tasks, GPUs are optimized for massive parallelism in simple calculations, a capability that has driven advancements in graphics, machine learning, and physics simulations.
Burns details the CUDA ecosystem, including its C-like syntax, the hierarchical thread model of grids, blocks, and threads, and the various memory types such as registers, shared memory, and global memory.
He demonstrates the practical integration of these technologies using CGo, showing how Go code can invoke C functions that launch CUDA kernels to perform parallel operations like array increments and matrix multiplications, while addressing critical memory management considerations between Go’s garbage collector and C’s manual memory management.
Finally, the presentation covers performance optimization strategies, recommending the use of NVIDIA’s Nsight Systems and Nsight Compute tools to profile system-wide timelines and analyze specific kernel bottlenecks, respectively, to maximize the efficiency of GPU-accelerated Go applications.

# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sam Burns, a software architect and application security specialist, presented on integrating CUDA and GPU programming into Go applications at GopherCon.                                                 |
|   2 | The talk covered GPU architecture, CUDA basics, high thread count programming, Go/CGo/CUDA integration, a linear algebra example, and performance optimizations.                                          |
|   3 | CPU cores offer low latency and strong caching but are limited in count, while GPU cores provide massive parallelism suitable for simple calculations and graphics.                                       |
|   4 | The history of GPU computing includes programmable shaders in the early 2000s and the creation of CUDA by Nvidia in 2006 to enable arbitrary mathematics on GPU hardware.                                 |
|   5 | In 2012, researchers at the University of Toronto used CUDA for machine learning, demonstrating that neural networks benefit from the same massive parallelism as graphics.                               |
|   6 | CUDA is a C-like programming language for GPUs that sits above PTX and shader assembly, allowing developers to transfer data between host and device and orchestrate threads.                             |
|   7 | Key CUDA applications include graphics programming, image processing, machine learning inference and training, physics simulations, password cracking, and cryptocurrency mining.                         |
|   8 | The CUDA thread model consists of threads grouped into blocks, which form a grid; threads within a block can synchronize using shared memory, while threads in different blocks cannot.                   |
|   9 | A warp is a group of 32 threads managed by the hardware scheduler, and performance depends on how well code aligns with this structure.                                                                   |
|  10 | GPU memory types include registers (fastest, per-thread), local memory (off-chip DRAM), shared memory (on-chip, per-block), and global memory (large, high-latency, grid-visible).                        |
|  11 | Accessing global memory is slower than shared memory, and data transfer between host and device via the PCIe bus is significantly slower than on-device operations.                                       |
|  12 | Integrating Go with CUDA requires using CGo to call C functions that invoke CUDA kernels, with specific compiler flags and library paths defined in CGo annotations.                                      |
|  13 | Go's garbage collector requires careful handling of pointers passed to C; using runtime.KeepAlive prevents the GC from freeing memory that C code still references.                                       |
|  14 | A simple example demonstrated incrementing an array using a CUDA kernel, where each thread calculates its index based on block and thread position to ensure unique element processing.                   |
|  15 | The extern C keyword in CUDA code disables C++ name mangling, allowing CGo to link to functions by their exact symbol names.                                                                              |
|  16 | Data transfer from host to device and back is a bottleneck, so optimization involves minimizing copied data and maximizing computation on the device.                                                     |
|  17 | A practical example implemented matrix multiplication using a 16x16 grid of threads, demonstrating that 256 matrix multiplications could run in parallel on consumer hardware.                            |
|  18 | Performance profiling is recommended using the NVIDIA Nsight suite, specifically Nsight Systems for end-to-end timeline analysis and Nsight Compute for detailed kernel-level metrics.                    |
|  19 | Nsight Systems helps identify bottlenecks in memory transfers and kernel launches, while Nsight Compute provides automated suggestions and roofline views to classify kernels as memory or compute bound. |
|  20 | The recommended workflow is to use Nsight Systems to locate hot kernels and then switch to Nsight Compute for deep-dive analysis and optimization guidance.                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/d1R8BS-ccNk/hqdefault.jpg)](https://www.youtube.com/watch?v=d1R8BS-ccNk)

[Watch on YouTube](https://www.youtube.com/watch?v=d1R8BS-ccNk)
