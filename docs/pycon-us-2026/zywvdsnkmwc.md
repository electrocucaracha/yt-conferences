---
layout: default
title: "Breaking the Speed Limit: Fast Statistical Models with Python 3.14...- Wenxin Jiang & Jian Yin"
nav_order: 23
parent: PyCon US 2026
type: Video Note
description: "This presentation outlines a rigorous framework for optimizing statistical models in Python, emphasizing that speed must never compromise statistical validity."
resource: "https://www.youtube.com/watch?v=ZywVdsNkMwc"
youtube_stats:
  view_count: 271
  like_count: 1
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

This presentation outlines a rigorous framework for optimizing statistical models in Python, emphasizing that speed must never compromise statistical validity.
The core principle is "speed follows validation," where a baseline implementation is first verified using simulations with known ground truths to ensure correctness before any optimization is attempted.
The authors demonstrate this approach using two distinct workloads: K-means clustering, which involves sequential dependencies and iterative updates, and permutation tests, which involve independent, high-dimensional resampling.
By analyzing the specific computational bottlenecks of each task, they show that different tools are optimal for different scenarios: Numba is effective for CPU-bound loops, NumPy excels at dense linear algebra, and JAX provides GPU acceleration for large, regular workloads.
Additionally, the talk highlights the importance of understanding scaling behaviors and parallelism limits, noting that while free-threaded Python can improve shared-memory scaling, the choice of engine ultimately depends on the specific shape of the computational bottleneck.
The presentation concludes by advocating for a systematic workflow of simulating, validating, identifying bottlenecks, and selecting the appropriate tool, while also stressing that researchers must retain ownership of scientific validity even when using AI coding assistants.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The core principle is that speed must follow validation to ensure statistical validity is not sacrificed for performance.                         |
|   2 | A baseline implementation is created first to serve as a reference, validated using simulations with known ground truth parameters.               |
|   3 | Simulation scenarios test method behavior across various inputs, including outliers, high dimensions, and cluster imbalances.                     |
|   4 | Software testing concepts like unit, property, stress, load, and regression tests are applied to statistical code validation.                     |
|   5 | Python facilitates this process by allowing readable code that closely mirrors mathematical formulas and supports diverse optimization libraries. |
|   6 | K-means clustering is used as a workload example, demonstrating sequential dependencies in iterative assignment and update steps.                 |
|   7 | K-means performance bottlenecks arise from repeated distance calculations with complexity proportional to samples, clusters, and dimensions.      |
|   8 | Validation of K-means involves comparing objective function values and predicted labels against a NumPy reference implementation.                 |
|   9 | Optimization tools for K-means include NumPy with BLAS for dense algebra, Numba for parallelized loops, and JAX for GPU acceleration.             |
|  10 | The choice of optimization engine depends on the specific bottleneck shape, such as scalar loops, dense algebra, or batched GPU work.             |
|  11 | Permutation tests involve repeatedly shuffling labels to build null distributions, creating independent but computationally heavy workloads.      |
|  12 | Optimized permutation tests use batched matrix operations to avoid explicit large matrices, improving efficiency over loop-based references.      |
|  13 | Validation of permutation tests checks p-value differences and calibration of type I error rates against nominal alpha levels.                    |
|  14 | Runtime scaling experiments help identify when performance degrades, informing decisions to use servers or GPUs.                                  |
|  15 | GPU acceleration provides significant speedups for large, regular workloads but may cause memory errors where CPU remains viable.                 |
|  16 | Parallelism offers substantial initial speedups but yields diminishing returns, and excessive workers can worsen performance.                     |
|  17 | Free-threaded Python builds enable better CPU-bound parallelism compared to standard GIL builds for shared memory workloads.                      |
|  18 | Numba is suited for CPU loops, NumPy for dense algebra, and JAX for GPU acceleration, depending on the bottleneck.                                |
|  19 | AI coding tools can assist in translating code between libraries, but researchers must retain ownership of scientific validity and claims.        |
|  20 | The final workflow is to simulate, validate, identify bottlenecks, and then select the appropriate computational tool.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZywVdsNkMwc/hqdefault.jpg)](https://www.youtube.com/watch?v=ZywVdsNkMwc)

[Watch on YouTube](https://www.youtube.com/watch?v=ZywVdsNkMwc)
