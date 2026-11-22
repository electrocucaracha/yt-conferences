---
layout: default
title: "Talks - Michael Droettboom: Measuring the performance of CPython"
nav_order: 194
parent: PyCon US 2024
type: Video Note
description: "Michael Droid, manager of the Microsoft CPython performance engineering team, presents a comprehensive overview of how the team measures CPython performance to ensure that optimizations yield genui..."
resource: "https://www.youtube.com/watch?v=XohBvqJEG6I"
youtube_stats:
  view_count: 620
  like_count: 12
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

Michael Droid, manager of the Microsoft CPython performance engineering team, presents a comprehensive overview of how the team measures CPython performance to ensure that optimizations yield genuine improvements.
He explains that while measuring all real-world Python programs is impractical due to uncontrolled variables, the team relies on the PyPerformance suite, which categorizes benchmarks into toy, micro, and application types to balance broad representativeness with specific diagnostic utility.
To address the inherent noise in performance measurements caused by system multitasking, thermal management, and memory layout, the team employs techniques such as CPU pinning, bare-metal hardware, and statistical methods like hierarchical performance testing to isolate meaningful changes from random fluctuations.
The talk highlights the implementation of continuous benchmarking infrastructure, analogous to continuous integration, which allows developers to automatically run benchmarks on pull requests and track performance trends over time, revealing that most recent speedups in Python 3.11 stem from interpreter optimizations.
Droid concludes by calling for community contributions of new benchmarks to better represent diverse workloads and emphasizes the need for future benchmarking suites that can measure the emerging parallel and free-threading capabilities of Python.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CPython is the most popular Python implementation, and performance measurement is critical for optimizing it.                         |
|   2 | The talk focuses on how to measure performance improvements rather than specific code optimization techniques.                        |
|   3 | Measuring all Python programs globally is impractical due to uncontrolled variables, similar to marathon runners affected by weather. |
|   4 | Benchmarking uses controlled variables to isolate the impact of specific changes.                                                     |
|   5 | The PyPerformance suite contains over 100 benchmarks, including toy, micro, application, and kernel benchmarks.                       |
|   6 | Toy benchmarks are simple and easy to analyze but may not represent real-world usage.                                                 |
|   7 | Micro benchmarks measure narrow language features, such as list comprehensions or garbage collection.                                 |
|   8 | Application benchmarks test full production-like code, such as Django CMS, but can be unstable due to dependencies.                   |
|   9 | Kernel benchmarks focus on specific subsystems, like SQL Alchemy, which may break due to CPython internal changes.                    |
|  10 | Different benchmark types serve different purposes: applications show overall speed, while toys help diagnose why changes occur.      |
|  11 | Profiling with Linux perf reveals where time is spent, such as in the interpreter, memory management, or C libraries.                 |
|  12 | Noise in measurements comes from multitasking, thermal throttling, memory layout randomization, and build variations.                 |
|  13 | Techniques to reduce noise include CPU pinning, using bare-metal hardware, and automatic warmup periods.                              |
|  14 | Statistical methods like hierarchical performance testing help distinguish significant changes from noise.                            |
|  15 | Continuous benchmarking infrastructure runs on dedicated bare-metal machines via GitHub Actions to ensure consistency.                |
|  16 | The PyPerformance suite takes about 70 minutes to run, which can be a bottleneck for rapid development cycles.                        |
|  17 | Future improvements include optimizing the benchmark suite itself and creating benchmarks for parallel Python features.               |
|  18 | Contributors are encouraged to submit new benchmarks that represent important workloads to the PyPerformance repository.              |
|  19 | Free-threading and sub-interpreters require new benchmark suites to measure parallel performance effectively.                         |
|  20 | Deterministic replay tools and simulators are potential areas for further exploration to reduce measurement noise.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XohBvqJEG6I/hqdefault.jpg)](https://www.youtube.com/watch?v=XohBvqJEG6I)

[Watch on YouTube](https://www.youtube.com/watch?v=XohBvqJEG6I)
