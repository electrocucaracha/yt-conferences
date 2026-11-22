---
layout: default
title: "Accelerated Python: The Community and Ecosystem (Sponsor: NVIDIA)"
nav_order: 67
parent: PyCon US 2025
type: Video Note
description: "NVIDIA has announced that Python is now a first-class language in the CUDA ecosystem, marking a significant shift to make GPU computing more accessible and interoperable."
resource: "https://www.youtube.com/watch?v=6IcvKPfNXUw"
youtube_stats:
  view_count: 954
  like_count: 21
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

NVIDIA has announced that Python is now a first-class language in the CUDA ecosystem, marking a significant shift to make GPU computing more accessible and interoperable.
The presentation highlights the company's commitment to supporting the open-source community by collaborating with projects like SciPy and scikit-image to integrate GPU acceleration, while also emphasizing the importance of standards like the Data API and DLPack for seamless data exchange between CPU and GPU libraries.
Key technical advancements include the introduction of CuPy for array-oriented computing, MVMath Python for high-performance scientific functions, and CuPy Numeric, which enables zero-code-change scaling across distributed systems using the Legate runtime.
Additionally, NVIDIA introduced a new tile-based programming model to simplify access to tensor cores, allowing developers to write high-level Python code that compiles to optimized hardware instructions, and demonstrated the benefits of free-threaded Python builds for accelerating machine learning data loading.
The session concluded with an overview of NVIDIA’s broader ecosystem support, including the Warp library for differentiable simulation and resources like the Accelerated Computing Hub, reinforcing the goal of lowering the barrier to entry for high-performance GPU computing in Python.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jeremy Tanner and Andy presented on NVIDIA's accelerated Python initiatives and ecosystem collaboration at PyCon.                                        |
|   2 | NVIDIA collaborates with open-source projects like scikit-image to add GPU support, addressing maintainer workload and community requests.               |
|   3 | The team participates in PyCon sprints to facilitate shoulder-to-shoulder collaboration between NVIDIA experts and community developers.                 |
|   4 | NVIDIA supports the Python Software Foundation, NumFOCUS, and the PyTorch Foundation to sustain the Python ecosystem.                                    |
|   5 | CUDA Python is now a first-class language in the CUDA ecosystem, supporting the full stack from host runtime to high-level frameworks.                   |
|   6 | Andy joined NVIDIA in 2023 with the goal of making CUDA 100 times easier to use in Python by reducing complexity.                                        |
|   7 | The CUDA platform emphasizes interoperability, ensuring Python code works seamlessly with other languages and hardware standards.                        |
|   8 | NVIDIA participates in the Data API initiative to standardize array interfaces, enabling zero-copy data exchange between CPU and GPU.                    |
|   9 | CuPy provides a NumPy-compatible array interface for GPUs, while DLPack serves as a protocol for zero-copy data sharing across libraries.                |
|  10 | MVMath Python offers a high-level, Pythonic interface to over 80 optimized scientific libraries, abstracting complex hardware details.                   |
|  11 | MVMath Python features just-in-time compilation and kernel fusion to optimize performance, such as reducing FFT planning overhead.                       |
|  12 | NVIDIA helped the Roman Space Telescope project speed up supernova detection code by over 40x using NumPy, CuPy, and optimized libraries.                |
|  13 | CuPy Numeric enables zero-code-change scaling for distributed computing by building on the Legate runtime from Stanford.                                 |
|  14 | Legate uses a task-based system and unified data abstraction to schedule tasks across nodes without explicit message passing.                            |
|  15 | PyTorch and JAX integrate with NVIDIA's lower-level libraries like cuDNN and cuBLAS for machine learning workloads.                                      |
|  16 | NVIDIA is introducing a Python layer into cuDNN to allow direct access to low-level features like flash attention for inference and training.            |
|  17 | Free-threading builds in Python allow parallel data loading using threads instead of processes, overcoming CUDA context sharing bottlenecks.             |
|  18 | NVIDIA Warp provides differentiable simulation capabilities in Python, supporting geometric processing and physics simulations for science and robotics. |
|  19 | A new tile-based programming model is being developed to simplify tensor core programming, allowing block-level operations similar to NumPy syntax.      |
|  20 | This new compiler, Coupile, aims to reduce code complexity and improve performance, achieving 93% of peak end-to-end performance in Llama 3 tests.       |
|  21 | The accelerated computing hub is an open resource for learning GPU programming, with NVIDIA providing cloud access for community experimentation.        |
|  22 | NVIDIA does not support Metal but provides best-of-class CPU performance using open standards and MKL on x86 architectures.                              |
|  23 | Brev.dev and Google Colab are recommended for accessing GPU resources, with Brev.dev offering flexible, professional-grade notebook environments.        |
|  24 | CUDA bindings and CUDA core provide low-level Python interfaces for memory management and runtime control, supporting advanced use cases.                |
|  25 | The compiler stack includes Numba and MLIR dialects, with plans to upstream the tile IR to the MLIR community for broader adoption.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6IcvKPfNXUw/hqdefault.jpg)](https://www.youtube.com/watch?v=6IcvKPfNXUw)

[Watch on YouTube](https://www.youtube.com/watch?v=6IcvKPfNXUw)
