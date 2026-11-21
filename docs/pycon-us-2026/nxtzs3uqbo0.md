---
layout: default
title: "Python at the Speed of Light: A Complete Tour of the CUDA Ecosystem - Daniel Rodriguez"
nav_order: 6
parent: PyCon US 2026
type: Video Note
description: "Daniel Rodriguez, a product manager at Nvidia, presents a comprehensive overview of the CUDA Python ecosystem, emphasizing that Python can be used for all accelerated computing tasks, including AI,..."
resource: "https://www.youtube.com/watch?v=NxTzS3uQBO0"
youtube_stats:
  view_count: 316
  like_count: 4
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

Daniel Rodriguez, a product manager at Nvidia, presents a comprehensive overview of the CUDA Python ecosystem, emphasizing that Python can be used for all accelerated computing tasks, including AI, physical simulations, and data processing.
The talk clarifies that CUDA is a platform for parallel computing on GPUs, which function as distinct devices with their own memory and instruction sets, rather than just a programming language.
Rodriguez demonstrates how to write CUDA kernels using Numba CUDA and explains higher-level abstractions like CuPy and Cutlass Python, which simplify complex operations such as matrix multiplication and linear algebra.
He highlights the importance of kernel fusion and device-to-device communication libraries like NCCL to optimize performance by minimizing data transfer latency between the host CPU and the GPU.
Additionally, the presentation covers the RAPIDS suite, which provides GPU-accelerated versions of popular data science tools like Pandas and scikit-learn, allowing users to run existing code on GPUs with minimal changes.
The session concludes with a Q&A addressing concerns about Python latency compared to C++, noting that the overhead is negligible compared to the benefits of ease of use and the extensive library support available for Nvidia hardware.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Python can be used for all CUDA accelerated computing tasks, including AI, simulations, and data processing. |
|   2 | CUDA is a platform for developing accelerated computing applications, not just a programming language. |
|   3 | A GPU is a distinct system with its own processor, memory hierarchy, and instruction set, separate from the host CPU. |
|   4 | CUDA kernels execute the same function across thousands of threads simultaneously, using indices to access different memory locations. |
|   5 | Numba CUDA allows writing CUDA kernels directly in Python using the @cuda decorator, mirroring C++ syntax. |
|   6 | Modern CUDA development avoids writing low-level kernels from scratch by using higher-level abstractions and libraries. |
|   7 | CuPy provides an idiomatic, NumPy-like API for GPU arrays and operations, simplifying data manipulation. |
|   8 | Cutlass Python introduces a block-level programming paradigm, abstracting thread management for linear algebra operations. |
|   9 | CCCL (CUDA Core Compute Libraries) offers optimized algorithms like transform, scan, reduce, and sort for GPU execution. |
|  10 | CuMATH Python provides access to linear algebra libraries such as cuBLAS, cuFFT, and cuSolver with host and device APIs. |
|  11 | Kernel fusion combines multiple operations into a single kernel to minimize memory transfers and improve performance. |
|  12 | NCCL and BHMem for Py enable efficient communication and data transfer between multiple GPUs in large-scale systems. |
|  13 | RAPIDS is an umbrella of data science libraries, including cuDF for pandas-like dataframes and cuML for machine learning. |
|  14 | CuDF allows running pandas code on the GPU with minimal changes, automatically handling data movement between CPU and GPU. |
|  15 | All Python CUDA libraries are built on foundational bindings like CuPy and cuCIM.Core, ensuring seamless interoperability. |
|  16 | Python introduces minimal latency compared to C++, with the primary performance cost being host-to-device data transfers. |
|  17 | CUDA libraries only run on Nvidia hardware and do not support Apple Metal or other non-Nvidia GPU architectures. |
|  18 | Affordable Nvidia GPUs, such as the RTX 3070, are sufficient for learning and experimenting with CUDA Python libraries. |
|  19 | Libraries like cuVS support vector search for RAG applications, and cuGraph optimizes network analysis algorithms. |
|  20 | The CUDA Python ecosystem supports multi-node computing and advanced features like green contexts for GPU partitioning. |
|  21 | Installation of these libraries is straightforward using pip, making them accessible for developers of varying experience levels. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NxTzS3uQBO0/hqdefault.jpg)](https://www.youtube.com/watch?v=NxTzS3uQBO0)

[Watch on YouTube](https://www.youtube.com/watch?v=NxTzS3uQBO0)
