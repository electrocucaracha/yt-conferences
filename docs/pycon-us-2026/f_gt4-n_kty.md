---
layout: default
title: "Building AI Inference Pipelines in Python (Sponsor: NVIDIA)"
nav_order: 96
parent: PyCon US 2026
type: Video Note
description: "Andy, who leads the CUDA Python product group at NVIDIA, presented a sponsored talk at PyCon detailing the evolution of GPU hardware and the new tools available for Python developers to maximize pe..."
resource: "https://www.youtube.com/watch?v=f_Gt4-N_ktY"
youtube_stats:
  view_count: 926
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

Andy, who leads the CUDA Python product group at NVIDIA, presented a sponsored talk at PyCon detailing the evolution of GPU hardware and the new tools available for Python developers to maximize performance.
He explained that modern GPUs, such as the Blackwell architecture, utilize specialized tensor cores and advanced memory hierarchies to achieve significant speedups in AI inference, but extracting this performance requires managing complex data flows and kernel execution.
To address this, NVIDIA has released CUDA Python 1.0, a comprehensive stack that includes high-level libraries like CuPy and cuDF, as well as new kernel authoring frameworks such as Numba CUDA, CuTile, and the CUTLASS DSL.
A key highlight of the presentation was the introduction of CuTile, a tile-based programming model that abstracts away low-level thread and warp management, allowing developers to write high-performance kernels in Python that are comparable to hand-optimized C++ code.
The talk also covered new debugging capabilities, such as CUDA-GDB integration, and performance optimization techniques like CUDA graph building and kernel fusion, which can yield substantial speedups by reducing latency and improving memory access patterns.

# Main Points

|   # | Main point                                                                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Andy from NVIDIA's CUDA Python product group, presented a sponsored talk at PyCon covering GPU hardware, the CUDA Python stack, and kernel programming.                                            |
|   2 | AI inference performance has improved significantly, with NVIDIA's Blackwell chip offering 15x faster performance than previous generations, driven by better energy efficiency and chip-to-chip interconnects. |
|   3 | GPU architecture has evolved from fixed-function accelerators to general-purpose processors with specialized tensor cores, lower precision support, and complex memory hierarchies.                             |
|   4 | Modern data center GPUs feature 96 GB of memory and 125 teraflops of compute, requiring software evolution to utilize new features like sparsity and tensor memory accelerators.                                |
|   5 | Efficient GPU computing requires managing data movement between host and device, utilizing libraries like cuDF and cuPy to bypass CPU bottlenecks and use direct I/O.                                           |
|   6 | Pinned memory and device-side memory management reduce latency by keeping data on the GPU, enabling faster chip-to-chip interactions without returning to the CPU.                                              |
|   7 | The CUDA Python 1.0 stack enables Python programmers to access full hardware capabilities on day one of new CUDA releases, removing the need for C++ toolchains.                                                |
|   8 | Three primary methods for kernel authoring in Python are supported: Numba CUDA for thread-based computing, CuTile for tile-based programming, and CUTLASS DSL for low-level control.                            |
|   9 | NVIDIA provides a suite of libraries including CCCL for parallel algorithms, NVMath Python for linear algebra and transforms, and communication libraries like NCCL and NVShmem.                                |
|  10 | A new MLIR backend for Numba CUDA offers 5x faster launch latencies and improved compilation speed by leveraging modern compiler infrastructure.                                                                |
|  11 | The CUDA graph builder allows users to record and launch sequences of kernels as a single graph, achieving up to 35x speedup by hiding launch and copy latencies.                                               |
|  12 | Fusion operations in CUDA Compute and NVMath Python combine multiple operations into single kernels, reducing memory access overhead and improving performance by up to 5x.                                     |
|  13 | New debugging tools allow setting breakpoints and inspecting variables in GPU kernels directly from Python, integrated with Visual Studio and other IDEs.                                                       |
|  14 | Performance profiling is simplified with a decorator-based interface that visualizes kernel execution and performance metrics within Jupyter notebooks.                                                         |
|  15 | Tile programming in CuTile abstracts thread-level management by operating on blocks of data, mapping them to tensor cores and memory hierarchies automatically.                                                 |
|  16 | This abstraction is necessary because tensor core requirements have changed across generations, making manual warp-level management difficult and error-prone.                                                  |
|  17 | CuTile supports multiple frontends including Python, Julia, Rust, and C++, lowering code to MLIR dialects and then to PTX for execution on NVIDIA hardware.                                                     |
|  18 | The Tile Gym repository provides high-performance reference kernels for AI inference tasks, demonstrating the capabilities of the CuTile programming model.                                                     |
|  19 | CuTile requires CUDA 13.1 and supports Ampere, Ada, or Blackwell GPUs, but does not currently support Turing architectures.                                                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/f_Gt4-N_ktY/hqdefault.jpg)](https://www.youtube.com/watch?v=f_Gt4-N_ktY)

[Watch on YouTube](https://www.youtube.com/watch?v=f_Gt4-N_ktY)
