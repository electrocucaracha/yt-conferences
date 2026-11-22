---
layout: default
title: "Talks - Bradley Dice: Hacking `import` for speed: how we wrote a GPU accelerator for pandas"
nav_order: 150
parent: PyCon US 2024
type: Video Note
description: "This presentation introduces cuDF pandas, an open-source library developed by NVIDIA that acts as a drop-in GPU accelerator for the pandas data analysis library."
resource: "https://www.youtube.com/watch?v=ydidRJVNq0g"
youtube_stats:
  view_count: 270
  like_count: 9
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

This presentation introduces cuDF pandas, an open-source library developed by NVIDIA that acts as a drop-in GPU accelerator for the pandas data analysis library.
By leveraging Python’s import machinery to proxy the standard pandas module, cuDF pandas allows users to accelerate existing code with minimal changes, such as adding a single line to load the extension in Jupyter notebooks.
This approach enables queries to run in hundreds of milliseconds rather than seconds, restoring real-time interactivity for data science workflows while automatically falling back to CPU execution for unsupported operations.
The speaker explains the technical complexity of this proxying mechanism, which handles attribute lookups, method chaining, and memory management to ensure compatibility with the broader Python data ecosystem, including libraries like SciPy and PyTorch.
Although there are limitations regarding C API calls and out-of-memory errors, the solution passes over 90% of the pandas test suite and is used by major organizations to significantly improve performance and cost efficiency.
The talk concludes by highlighting the availability of cuDF pandas through standard package managers and Google Colab, encouraging the community to adopt this technology for faster, more interactive data analysis.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CuDF is an open-source library developed by NVIDIA that serves as a drop-in GPU accelerator for pandas.                                        |
|   2 | The library enables data science workflows to run in hundreds of milliseconds rather than seconds, restoring interactive experiences.          |
|   3 | CuDF pandas allows users to accelerate existing pandas code with zero code changes by using a load extension command in Jupyter notebooks.     |
|   4 | The solution leverages Python's import machinery and meta hooks to proxy the pandas module with GPU-accelerated implementations.               |
|   5 | When a function is not supported on the GPU, the system automatically falls back to CPU execution to ensure compatibility.                     |
|   6 | CuDF supports a wide variety of data types and operations, including loading, filtering, aggregating, and joining data frames.                 |
|   7 | Benchmarks indicate that cuDF is generally 10 to 100 times faster than pandas for supported operations.                                        |
|   8 | The library integrates seamlessly with third-party tools such as scikit-learn, XGBoost, Matplotlib, and PyTorch.                               |
|   9 | A profiler is provided to identify which specific functions are running on the GPU versus falling back to the CPU.                             |
|  10 | The proxying infrastructure handles complex cases like attribute lookups, magic methods, and multi-step execution chains.                      |
|  11 | Limitations include difficulty proxying C API calls and potential out-of-memory errors if data exceeds GPU capacity.                           |
|  12 | For workloads larger than a single GPU's memory, users can scale up using Dask cuDF or Apache Spark integrations.                              |
|  13 | CuDF pandas passes over 90% of the entire pandas test suite, ensuring high compatibility with existing codebases.                              |
|  14 | The project is part of the broader RAPIDS ecosystem, which includes libraries for machine learning, graph analytics, and geospatial computing. |
|  15 | RAPIDS is used by major organizations such as Adobe, AstraZeneca, and Walmart for performance improvements and cost savings.                   |
|  16 | Installation is available via conda and pip, with support for Windows Subsystem for Linux and cloud deployment.                                |
|  17 | CuDF is now available for free use in Google Colab, allowing users to test GPU acceleration easily.                                            |
|  18 | The team continues to improve compatibility and performance while collaborating with the Python community on data science standards.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ydidRJVNq0g/hqdefault.jpg)](https://www.youtube.com/watch?v=ydidRJVNq0g)

[Watch on YouTube](https://www.youtube.com/watch?v=ydidRJVNq0g)
