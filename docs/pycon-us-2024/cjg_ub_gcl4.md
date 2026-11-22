---
layout: default
title: "Talks - Pablo Galindo Salgado: Profiling at the speed of light"
nav_order: 145
parent: PyCon US 2024
type: Video Note
description: "Pablo Galindo Salgado presents a deep dive into high-performance profiling for Python, specifically focusing on integrating the Linux kernel’s `perf` tool with the Python interpreter to analyze bot..."
resource: "https://www.youtube.com/watch?v=CjG_Ub_gCL4"
youtube_stats:
  view_count: 731
  like_count: 20
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

Pablo Galindo Salgado presents a deep dive into high-performance profiling for Python, specifically focusing on integrating the Linux kernel’s `perf` tool with the Python interpreter to analyze both Python and C-level code simultaneously.
He begins by debunking the common assumption that shuffling an array slows down NumPy operations due to branch misprediction, using `perf` data to demonstrate that the actual cause is increased memory copying overhead when extracting non-contiguous elements.
To enable `perf` to understand Python functions, the talk details the implementation of JIT interface support in Python 3.12 and 3.13, which allows the profiler to map C stack frames to specific Python function names, thereby generating comprehensive flame graphs that reveal the interaction between interpreted and compiled code.
The presentation also addresses the trade-offs between using frame pointers for fast stack unwinding and DWARF-based backtracing for broader compatibility, noting that while frame pointers offer superior speed, they incur a slight performance penalty and are not universally enabled in standard builds.
Finally, Salgado showcases advanced use cases, such as tracing GIL acquisition and release, monitoring garbage collection triggers, and optimizing specific functions like `statistics.mean`, illustrating how this low-level visibility empowers developers to identify and resolve complex performance bottlenecks in mixed Python and C applications.

# Main Points

|   # | Main point                                                                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | A performance mystery demonstrates that shuffling a NumPy array before filtering and summing values makes the operation 55% slower than using a sorted array.                                                |
|   2 | Standard Python profilers are ineffective for this issue because the bottleneck occurs inside NumPy, which is written in C and other compiled languages.                                                     |
|   3 | The Linux kernel tool `perf` provides low-level hardware counters and detailed CPU metrics but traditionally only displays C-level function names, obscuring Python context.                                 |
|   4 | Python 3.12 and 3.13 introduced support to teach `perf` to recognize Python functions by injecting unique C frames into the call stack.                                                                      |
|   5 | This implementation uses a JIT-like approach where minimal assembly code is copied into memory and registered via a file in `/tmp` to map unique memory addresses to Python function names.                  |
|   6 | Stack unwinding in C can be achieved using frame pointers or DWARF debug information, each with distinct performance and compatibility trade-offs.                                                           |
|   7 | Compiling Python with frame pointers enables fast stack unwinding but results in a performance penalty of approximately 7% in the worst-case scenario.                                                       |
|   8 | DWARF-based unwinding avoids the need for recompilation with frame pointers but requires an extra augmentation step and generates larger result files due to full stack copies.                              |
|   9 | The mystery was solved by using `perf` probes to count function calls, revealing that the slow version called the `contiguous` function many times to copy scattered memory elements.                        |
|  10 | The fast version called `contiguous` only once because the data was already contiguous, allowing NumPy to use efficient vectorized instructions.                                                             |
|  11 | Perf` can be used to trace GIL acquisition and release events to identify which Python functions are causing thread contention in multi-threaded applications.                                               |
|  12 | Probes can be attached to functions like `gc.collect` to identify code paths that frequently trigger garbage collection, allowing for optimization by deactivating the collector during specific operations. |
|  13 | The `perf` ecosystem supports various visualization tools like flame graphs and HotSpot, enabling developers to analyze both Python and C code simultaneously.                                               |
|  14 | Environment variables such as `PYTHON_PERF_SUPPORT` and `PYTHON_PERF_JIT_SUPPORT` or command-line flags like `-X perf` are used to activate these profiling features in Python.                              |
|  15 | This integration allows for high-performance profiling of C extensions and high-performance computing workloads without abandoning the terminal or using slower pure-Python profilers.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CjG_Ub_gCL4/hqdefault.jpg)](https://www.youtube.com/watch?v=CjG_Ub_gCL4)

[Watch on YouTube](https://www.youtube.com/watch?v=CjG_Ub_gCL4)
