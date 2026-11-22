---
layout: default
title: "Talks - Mridul Seth, Erik Welch: NetworkX is Fast Now: Graph Analytics Unleashed"
nav_order: 169
parent: PyCon US 2024
type: Video Note
description: This presentation by Eric Welch from NVIDIA and Mridul Seth from NetworkX introduces a new dispatching system designed to accelerate graph analytics by allowing NetworkX to utilize optimized backen...
resource: "https://www.youtube.com/watch?v=Dh119XXIKi4"
youtube_stats:
  view_count: 770
  like_count: 14
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

This presentation by Eric Welch from NVIDIA and Mridul Seth from NetworkX introduces a new dispatching system designed to accelerate graph analytics by allowing NetworkX to utilize optimized backends without altering its user-friendly API.
The speakers demonstrate that this approach can reduce computation times for algorithms like square clustering and betweenness centrality from minutes to seconds, achieving speedups of up to 700 times on GPU hardware.
By treating NetworkX as a standardized API layer, the project enables various backends, such as NVIDIA’s cuGraph, GraphBLAS, and parallel CPU implementations, to plug in and provide high-performance execution while maintaining zero-code-change compatibility for users.
Additionally, the talk highlights an emerging proof-of-concept integration with ArangoDB, which allows NetworkX to function as a graph database interface, enabling data persistence and CRUD operations through the familiar NetworkX paradigm.
The team emphasizes that this ecosystem is currently experimental but welcomes community feedback, contributions, and the development of new backends to further standardize and enhance graph analytics in Python.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | NetworkX performance improved from 25 seconds to half a second for square clustering on a graph with 90,000 edges using a new backend.                           |
|   2 | Poor performance in libraries like NetworkX has historically prevented graph analytics from becoming a mainstream data science practice.                         |
|   3 | Graph analytics is applicable to diverse fields including fraud detection, recommendation systems, and graph neural networks.                                    |
|   4 | NetworkX is a pure Python library with zero inherent dependencies, making it easy to install and run anywhere Python is supported.                               |
|   5 | The library has approximately 50 million monthly downloads and is nearly 20 years old, originally designed for single-processor environments.                    |
|   6 | A dispatching architecture allows NetworkX to act as a frontend API while delegating computation to optimized backends like GPU or CPU implementations.          |
|   7 | The NVIDIA RAPIDS team developed nx-cugraph, a GPU-accelerated backend that enables low-to-no-code changes for users to access accelerated algorithms.           |
|   8 | Benchmarks on a Quadro RTX 8000 GPU show speedups ranging from 100 to over 1,000 times compared to standard NetworkX for algorithms like betweenness centrality. |
|   9 | Caching graph conversions in NetworkX 3.3 reduces repeated overhead, allowing subsequent algorithm runs to be significantly faster by keeping data on the GPU.   |
|  10 | The backend system facilitates integration with graph databases like ArangoDB, enabling data persistence and CRUD operations through the standard NetworkX API.  |
|  11 | Backend developers benefit from free access to NetworkX's existing documentation, testing suite, and large user base when implementing new algorithms.           |
|  12 | The project aims to establish a standardized graph API layer, similar to the Array API, allowing multiple vendors to provide compatible backend implementations. |
|  13 | Compatibility guarantees for backends are currently experimental, with stability expected to improve as usage grows and documentation matures.                   |
|  14 | Alternative approaches like Rust-based rewrites exist but often require API changes, whereas the dispatching model preserves the original NetworkX interface.    |
|  15 | The community encourages users to test the new dispatching features and provide feedback to help refine the user experience and documentation.                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Dh119XXIKi4/hqdefault.jpg)](https://www.youtube.com/watch?v=Dh119XXIKi4)

[Watch on YouTube](https://www.youtube.com/watch?v=Dh119XXIKi4)
