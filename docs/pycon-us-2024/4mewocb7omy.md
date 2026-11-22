---
layout: default
title: "Talks - Saksham Sharma: A low latency deepdive of Python with Cython"
nav_order: 192
parent: PyCon US 2024
type: Video Note
description: "San Sharma, a quantitative trader, presents a deep dive into Python performance optimization using Cython, aiming to provide concrete nanosecond-level benchmarks rather than vague speed comparisons."
resource: "https://www.youtube.com/watch?v=4mEWoCB7oMY"
youtube_stats:
  view_count: 1065
  like_count: 45
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

San Sharma, a quantitative trader, presents a deep dive into Python performance optimization using Cython, aiming to provide concrete nanosecond-level benchmarks rather than vague speed comparisons.
He explains that CPython’s interpreter overhead, which involves dynamic type checking and object management, makes simple operations like addition significantly slower than raw CPU capabilities, whereas external I/O operations are inherently slower due to hardware limitations.
By using Cython to generate low-level C code and explicitly defining types, such as C integers, developers can bypass the interpreter’s dynamic dispatch, reducing the cost of basic arithmetic from tens of nanoseconds to just a few.
In a case study involving NumPy array lookups, Sharma demonstrates that using typed memory views and moving loops into Cython code can achieve a 30x speedup, bringing access times down to approximately 5 nanoseconds.
He concludes that while Cython offers a flexible middle ground between Python’s ease of use and C++’s raw speed, it is best suited for optimizing inner loops and business logic, whereas ultra-low-latency trading systems may still require direct C++ implementations to minimize variance.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CPython is a compiled C program that executes Python bytecode, maintaining internal state via PyObjects.                                                                                 |
|   2 | Interpreted Python code incurs significant overhead compared to raw CPU capabilities, which can perform basic arithmetic in under 1 nanosecond.                                          |
|   3 | Adding two integers in Python takes approximately 528 CPU instructions due to type checking, object creation, and interpreter overhead.                                                  |
|   4 | Cython allows developers to generate low-level C code from Python-like syntax, bypassing the interpreter for specific functions.                                                         |
|   5 | Using Cython without type declarations still results in high instruction counts because the interpreter must verify object types at runtime.                                             |
|   6 | Declaring variables with C types (e.g., cdef int) in Cython enables the compiler to generate direct machine instructions, reducing loop overhead to roughly 3 nanoseconds per iteration. |
|   7 | Compiler optimizations can further reduce execution time by recognizing patterns, such as converting a summation loop into the mathematical formula n*(n-1)/2.                           |
|   8 | Accessing a single value in a NumPy array via Python takes approximately 8 microseconds, which is significantly slower than basic arithmetic operations.                                 |
|   9 | Using Cython memory views (e.g., np.int64[:]) provides a typed, safe abstraction for accessing raw array data, improving lookup speed by 30x to 180 nanoseconds.                         |
|  10 | Moving loops into Cython code eliminates the overhead of repeated Python function calls, which typically cost 100 to 150 nanoseconds per invocation.                                     |
|  11 | Combining typed memory views with typed loop variables in Cython reduces array lookup time to approximately 5 nanoseconds while retaining bounds checking.                               |
|  12 | Cython can be tuned to match the performance of direct C API usage, offering a better balance between ease of use and speed.                                                             |
|  13 | For low-latency trading applications, Cython is best used as a thin wrapper to convert Python objects to C/C++ structures, minimizing variance in the core logic.                        |
|  14 | Cython allows explicit release of the Global Interpreter Lock (GIL) using the nogil directive, enabling true parallelism for CPU-bound tasks.                                            |
|  15 | The hw module used for benchmarking in the talk is a custom, non-open-source wrapper around Intel PMU instructions for measuring CPU cycles.                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/4mEWoCB7oMY/hqdefault.jpg)](https://www.youtube.com/watch?v=4mEWoCB7oMY)

[Watch on YouTube](https://www.youtube.com/watch?v=4mEWoCB7oMY)
