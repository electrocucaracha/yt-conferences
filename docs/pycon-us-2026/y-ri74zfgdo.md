---
layout: default
title: "Making Python Faster with Free Threading and Mypyc - Jukka Lehtosalo"
nav_order: 49
parent: PyCon US 2026
type: Video Note
description: "Yugala Sola, a staff engineer at Dropbox and co-founder of TypeSet, presents a technical overview of optimizing Python code through free-threading and the MyPyC compiler."
resource: "https://www.youtube.com/watch?v=Y-ri74ZfGdo"
youtube_stats:
  view_count: 980
  like_count: 18
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

Yugala Sola, a staff engineer at Dropbox and co-founder of TypeSet, presents a technical overview of optimizing Python code through free-threading and the MyPyC compiler.
He explains that free-threading, available in Python 3.13 and later, removes the Global Interpreter Lock to enable true parallelism, though it requires careful management of race conditions and reference count contention.
MyPyC, a ahead-of-time compiler for type-annotated Python, offers significant speedups by compiling code to C extensions, with performance gains ranging from 1.5x to 10x depending on the workload.
Sola demonstrates that combining these technologies can yield substantial improvements, such as an 82x speedup in a Monte Carlo pi calculation, by addressing common bottlenecks like standard library overhead and memory allocation.
He highlights specific optimization strategies, including using thread-local objects to avoid lock contention, replacing standard library modules with MyPyC-optimized alternatives like `libmypyc`, and utilizing packed array types (`vec`) for more efficient memory usage.
The talk concludes with a discussion on the trade-offs of these approaches, noting that while MyPyC is stable for Mypy itself, its broader application is still evolving, and users must balance compatibility with performance gains.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Hardware price increases have renewed interest in code optimization and free-threading to maximize existing CPU and memory resources. |
|   2 | Free-threading in Python 3.13+ removes the Global Interpreter Lock, allowing true parallel execution of CPU-intensive tasks across multiple cores. |
|   3 | Free-threading offers efficient object sharing between threads, reducing memory usage compared to multiprocessing by avoiding duplicate module states. |
|   4 | Key challenges with free-threading include debugging race conditions, limited third-party library support, and a small performance penalty for non-threaded code. |
|   5 | MyPyC is a ahead-of-time compiler that converts type-annotated Python into fast C extensions, typically yielding 1.5x to 10x speedups. |
|   6 | MyPyC maintains compatibility with interpreted Python, allowing seamless integration of compiled and non-compiled modules within the same application. |
|   7 | A significant drawback of MyPyC on free-threaded builds is the lack of automatic memory safety guarantees, requiring developers to manage thread locks correctly. |
|   8 | Global state contention, such as locks in the random module, can negate threading benefits; using thread-local instances resolves this bottleneck. |
|   9 | MyPyC includes libmypyc, a library of optimized replacements for standard library modules like random and struct, which are often performance bottlenecks. |
|  10 | Reference counting contention in free-threading can be mitigated by reusing local references instead of creating new ones in loops. |
|  11 | MyPyC optimizes data structures by compiling floating-point operations to C doubles and using packed array types like vec for memory efficiency. |
|  12 | Custom implementations of data structures, such as heaps and hash maps using vec i32, can outperform standard library versions when compiled with MyPyC. |
|  13 | Combining free-threading and MyPyC can result in multiplicative performance gains, such as 82x speedups in specific Monte Carlo simulations. |
|  14 | Memory bandwidth can become a bottleneck when using excessive threads for I/O-heavy tasks, requiring tuning of thread counts for optimal performance. |
|  15 | MyPyC does not automatically replace standard lists and dicts with optimized types to maintain strict compatibility with interpreted Python semantics. |
|  16 | Python 3.14 is recommended over 3.13 for free-threading due to better stability and reduced single-thread performance penalties. |
|  17 | MyPyC currently lacks full support for custom metaclasses and decorators, limiting integration with certain binding libraries. |
|  18 | The MyPy project is adopting a Rust-based parser to improve infrastructure quality without duplicating existing high-quality work. |
|  19 | MyPy 2.0 and 2.1 introduce parallel type checking, making it competitive with other tools like Ty and Pyright in specific use cases. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Y-ri74ZfGdo/hqdefault.jpg)](https://www.youtube.com/watch?v=Y-ri74ZfGdo)

[Watch on YouTube](https://www.youtube.com/watch?v=Y-ri74ZfGdo)
