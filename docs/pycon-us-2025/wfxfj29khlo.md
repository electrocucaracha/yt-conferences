---
layout: default
title: "When GPUs Make Python Slower: Patterns and Pitfalls - Kaashif Hymabaccus"
nav_order: 18
parent: PyCon US 2025
type: Video Note
description: "Kashif from Bloomberg presents a talk on common pitfalls that cause GPU-accelerated Python code to perform slower than CPU-based equivalents, focusing on three key anti-patterns."
resource: "https://www.youtube.com/watch?v=WfXfj29KhLo"
youtube_stats:
  view_count: 1054
  like_count: 23
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

Kashif from Bloomberg presents a talk on common pitfalls that cause GPU-accelerated Python code to perform slower than CPU-based equivalents, focusing on three key antipatterns.
The first issue is excessive memory transfer; moving large datasets between CPU RAM and GPU VRAM for simple operations like regular expression matching creates a high fixed cost that outweighs the benefits of parallelism, making such tasks better suited for CPUs.
The second pitfall involves low operational intensity, where algorithms that move large amounts of data but perform minimal computation fail to utilize the GPU’s computational power, as demonstrated by comparing inefficient string searches with highly efficient matrix multiplications.
The third major problem is launching millions of small CUDA kernels, which occurs when naively translating row-by-row pandas loops into GPU code, resulting in severe overhead from kernel launch latency rather than actual computation.
To avoid these issues, the speaker advises minimizing data transfers, maximizing operational intensity by ensuring problems are compute-bound, and leveraging optimized libraries like cuDF to handle complex operations in single, efficient kernels rather than fragmented small tasks.

# Main Points

|   # | Main point                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Minimize memory transfers between CPU RAM and GPU VRAM to avoid high latency costs associated with the PCIe bus.                                                                                      |
|   2 | Maximize operational intensity by ensuring the ratio of computation to data movement is high, as GPUs excel at compute-bound tasks rather than memory-bound ones.                                     |
|   3 | Avoid launching millions of small CUDA kernels, as the overhead of kernel launches can severely degrade performance compared to executing fewer, larger kernels.                                      |
|   4 | Regular expression matching is a poor fit for GPUs because it involves linear operations relative to string length, resulting in low operational intensity and high memory bandwidth usage.           |
|   5 | Matrix multiplication is an ideal GPU workload because it involves cubic operations relative to matrix dimension, leading to high computational density and efficient use of GPU cores.               |
|   6 | Roofline analysis helps identify whether a workload is memory-bound or compute-bound, guiding decisions on whether to use GPU acceleration.                                                           |
|   7 | Nsight Systems and Nsight Compute are essential tools for profiling GPU performance, revealing bottlenecks such as excessive memory transfers or low kernel utilization.                              |
|   8 | Wide-format data processed column-by-column is cache-friendly and efficient on CPUs, while tall-format data processed row-by-row is less efficient due to poor data locality.                         |
|   9 | Naively translating pandas code to cuDF can result in slower performance if the code structure leads to many small kernel launches or inefficient memory access patterns.                             |
|  10 | GroupBy and count operations in cuDF are highly optimized and should be preferred over manual loops that trigger numerous small kernel executions.                                                    |
|  11 | GPU acceleration is most beneficial when data is large and computations are intensive, such as in machine learning or linear algebra, rather than for simple string searches or small datasets.       |
|  12 | Profiling reveals that regular expression matching on GPUs often hits memory bandwidth limits with low compute throughput, whereas matrix multiplication utilizes compute resources more effectively. |
|  13 | Developers should understand the shape of their problem and data size to determine if GPU acceleration will provide a net performance benefit.                                                        |
|  14 | Using cuDF for I/O operations like reading CSV or Parquet files directly to the GPU can significantly improve performance by reducing intermediate CPU memory transfers.                              |
|  15 | The overhead of launching individual CUDA kernels is significant, so batching operations into larger kernels is a critical optimization strategy.                                                     |
|  16 | Benchmarks should be interpreted with caution, as fixed costs like data transfer can dominate performance metrics for small datasets, masking the true computational speed of the GPU.                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WfXfj29KhLo/hqdefault.jpg)](https://www.youtube.com/watch?v=WfXfj29KhLo)

[Watch on YouTube](https://www.youtube.com/watch?v=WfXfj29KhLo)
