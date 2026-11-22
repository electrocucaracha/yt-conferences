---
layout: default
title: "Sponsor Presentations -Tread Lightly When Building and Testing Your Python Project (Sponsor: Fastly)"
nav_order: 34
parent: PyCon US 2024
type: Video Note
description: "At PyCon 24, Kevin Fleming and Charlie Marsh presented a talk on optimizing Python application building and testing to save time and reduce resource consumption."
resource: "https://www.youtube.com/watch?v=hIXUzxmMcAU"
youtube_stats:
  view_count: 514
  like_count: 6
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

At PyCon 24, Kevin Fleming and Charlie Marsh presented a talk on optimizing Python application building and testing to save time and reduce resource consumption.
They emphasized three core strategies: using more efficient tools, leveraging parallelism, and minimizing unnecessary work.
The speakers highlighted the benefits of modern, high-performance tools like Ruff and UV, which are written in Rust and offer significant speed improvements over traditional Python-based alternatives, thereby shortening developer iteration loops and reducing CI execution times.
They also discussed the importance of optimizing CI workflows by using containers instead of virtual machines, implementing effective caching, and restructuring test discovery processes to avoid redundant computations across multiple machines.
Real-world examples from projects like Home Assistant and Airflow demonstrated that these optimizations can drastically reduce build times and compute costs, ultimately benefiting both developers and the broader ecosystem by lowering the environmental impact of software development.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on optimizing Python application building and testing to save time and resources for users, developers, contributors, and the environment.                       |
|   2 | Key strategies include using more efficient tools, parallelizing work, and reducing unnecessary operations.                                                                       |
|   3 | Upgrading to newer Python versions, such as moving from 3.10 to 3.11, can yield significant performance improvements, like a 25% speedup in core benchmarks.                      |
|   4 | For I/O-bound software, using async/await allows code to continue executing while waiting for network or file system operations.                                                  |
|   5 | For CPU-bound tasks involving large datasets, parallelizing work using multiprocessing and divide-and-conquer strategies can reduce wall-clock time.                              |
|   6 | Web applications should avoid launching programs per request; instead, use connection pooling and share configuration to reduce overhead.                                         |
|   7 | Fast developer tools shorten iteration loops, enabling quicker feedback and potentially unlocking local debugging capabilities that were previously too slow.                     |
|   8 | Ruff, a Python linter and formatter written in Rust, is 10 to 1000 times faster than traditional tools, allowing entire codebases to be analyzed in milliseconds.                 |
|   9 | UV, a Python package installer and resolver, offers near-instant virtual environment synchronization compared to pip, significantly improving developer experience.               |
|  10 | Both Ruff and UV leverage concurrency, parallelism, and caching to achieve high performance, with UV specifically optimizing for warm cache scenarios.                            |
|  11 | Improving contributor experience involves moving linting and testing to local pre-commit hooks to provide immediate feedback and reduce CI load.                                  |
|  12 | CI workflows should be optimized by running critical tests first to fail fast, preventing unnecessary resource consumption by other jobs.                                         |
|  13 | Caching dependencies in CI, such as using GitHub Actions to store and restore UV caches, reduces redundant work and improves consistency.                                         |
|  14 | Reducing resource consumption is crucial; for example, Home Assistant saved 215 hours of compute per month by switching to UV for dependency management.                          |
|  15 | Airflow reduced build times significantly by adopting UV, with constraint solving dropping from 5 minutes to 30 seconds.                                                          |
|  16 | Parallelism in CI can be resource-intensive if not managed well; using containers instead of virtual machines reduces startup overhead and resource usage.                        |
|  17 | Building custom container images with pre-installed dependencies allows for faster CI runs and easier local replication of CI environments for debugging.                         |
|  18 | Restructuring CI to perform test discovery once and distribute specific tests to jobs, rather than running discovery on every machine, saves substantial compute time.            |
|  19 | High-volume package downloads from CI platforms, such as 386 million in a day, highlight the need for efficiency to reduce bandwidth and infrastructure costs.                    |
|  20 | Tools like Ruff can be opinionated about code patterns to suggest or apply performance improvements, provided they maintain correctness and offer clear rationale.                |
|  21 | Implementing tools in Rust allows for high performance and efficient Python interoperability, mirroring trends in other ecosystems where non-native languages are used for speed. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hIXUzxmMcAU/hqdefault.jpg)](https://www.youtube.com/watch?v=hIXUzxmMcAU)

[Watch on YouTube](https://www.youtube.com/watch?v=hIXUzxmMcAU)
