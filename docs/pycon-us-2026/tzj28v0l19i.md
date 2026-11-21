---
layout: default
title: "GPU Communications for Python - Benjamin Glick, Michael Yh Wang"
nav_order: 118
parent: PyCon US 2026
type: Video Note
description: "This presentation introduces the CUDA Python ecosystem, focusing on libraries that enable multi-GPU programming and high-performance kernel development directly in Python."
resource: "https://www.youtube.com/watch?v=TZj28v0L19I"
youtube_stats:
  view_count: 1099
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

This presentation introduces the CUDA Python ecosystem, focusing on libraries that enable multi-GPU programming and high-performance kernel development directly in Python.
The speakers explain fundamental concepts such as the distinction between host code running on the CPU and device code executing on the GPU, as well as the use of CUDA streams to manage parallelism and data dependencies.
They detail the NCCL library for collective communications like all-reduce and point-to-point transfers, and introduce NVMe (NVIDIA Shared Memory), which facilitates GPU-centric communication by allowing direct data exchange between GPUs without CPU intervention through symmetric memory allocation.
Additionally, the talk covers writing custom CUDA kernels in Python using Numba CUDA for just-in-time compilation and CuTe DSL for accessing tensor cores and inline assembly.
The session concludes with an overview of the underlying compiler stacks that bridge Python APIs to CUDA driver calls, emphasizing NVIDIA’s commitment to providing robust, high-performance Python interfaces for AI and HPC workloads.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The CUDA Python ecosystem includes multiple libraries, with a focus on Nickel for Pi and NVMe for Pi for multi-GPU programming.                |
|   2 | Host code runs on the CPU using standard Python, while device code runs on the GPU and requires separate compilation.                          |
|   3 | Host and device code can coexist in a single Python file, but they interact with different memory spaces: CPU memory and GPU memory.           |
|   4 | Data transfer between host and device memory requires explicit copying, facilitated by helper functions in the CUDA Core library.              |
|   5 | Pinned memory resources are used to allocate host memory that is optimized for faster transfers to the GPU.                                    |
|   6 | CUDA streams act as work queues for GPU actions, allowing linear execution within a stream and potential parallelism across different streams. |
|   7 | Streams enable overlapping of data copies and computations to hide latency and improve GPU utilization.                                        |
|   8 | Multi-GPU programming utilizes data parallelism, where data is split across GPUs, and collectives are used to synchronize partial results.     |
|   9 | Collectives involve all participating GPUs in a single communication operation to resolve data dependencies.                                   |
|  10 | Nickel is an NVIDIA collective communications library offering both host and device APIs for operations like all-reduce and send/receive.      |
|  11 | All-reduce aggregates data from multiple GPUs and broadcasts the reduced result to all participants.                                           |
|  12 | NVMe for Pi enables GPU-centric communications by bypassing the CPU for data transfers between GPUs and networks.                              |
|  13 | NVMe uses a Partition Global Address Space (PGAS) model to create symmetric memory blocks with identical shapes and addresses on all GPUs.     |
|  14 | The nvm.core.array function allocates symmetric memory, allowing direct GPU-to-GPU access without CPU intervention.                            |
|  15 | NVMe put operations are one-sided, meaning only the sender initiates the transfer, and the receiver passively receives data.                   |
|  16 | Data transfers in NVMe go directly from source GPU memory to destination GPU memory via network interfaces, keeping CPUs idle.                 |
|  17 | Python bindings for CUDA libraries are built using Cython and native C extensions, with high-level wrappers for user-friendly APIs.            |
|  18 | Numba CUDA is a JIT compiler that allows writing CUDA kernels in pure Python, compiling them just before launch.                               |
|  19 | Numba CUDA kernels use specific syntax for launch configurations and can interact with other Python array objects.                             |
|  20 | CuTe DSL is a Python dialect for high-performance tensor core operations, requiring explicit compilation of kernels.                           |
|  21 | CuTe DSL separates host code (compiled to C++ driver calls) and device code (using NVMe/Nickel APIs) within the same program.                  |
|  22 | The compiler stack for Numba and CuTe converts Python code into intermediate representations and links against device libraries.               |
|  23 | NVMe Python APIs are not fully compatible with the entire C++ service area but aim to keep Python features at par where possible.              |
|  24 | Runtime conditionals in JIT-compiled Python kernels are supported and translate to standard CUDA runtime checks.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TZj28v0L19I/hqdefault.jpg)](https://www.youtube.com/watch?v=TZj28v0L19I)

[Watch on YouTube](https://www.youtube.com/watch?v=TZj28v0L19I)
