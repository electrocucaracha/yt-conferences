---
layout: default
title: "High-Performance Python: Faster Type Checking and Free Threaded Execution (Sponsor: Meta)"
nav_order: 65
parent: PyCon US 2025
type: Video Note
description: "Sam Gross presents Free Threaded Python, an experimental CPython build that removes the Global Interpreter Lock (GIL) to enable true multi-threaded parallelism."
resource: "https://www.youtube.com/watch?v=ZTSZ1OCUaeQ"
youtube_stats:
  view_count: 5156
  like_count: 127
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

Sam Gross presents Free Threaded Python, an experimental CPython build that removes the Global Interpreter Lock (GIL) to enable true multi-threaded parallelism.
By implementing biased reference counting, per-instance locks, and deferred reference counting, the project addresses thread safety and scaling bottlenecks while maintaining single-threaded performance within a 10–15% regression target.
Python 3.13 introduced this feature experimentally, and Python 3.14 significantly improves its performance by re-enabling the specializing interpreter and optimizing garbage collection.
Neil Schemenauer then introduces PyreFly, a new open-source, Rust-based Python type checker developed by Meta that prioritizes speed, parallelism, and IDE integration.
PyreFly is designed to be 35 times faster than its predecessor, Pyre, by leveraging module-level parallelism and advanced type inference to provide real-time feedback in environments like Visual Studio Code.
Both projects aim to enhance Python’s ecosystem by improving multi-core utilization and developer productivity through robust, high-performance tooling.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Free-threaded Python is an experimental CPython build that removes the Global Interpreter Lock (GIL) to allow parallel thread execution.            |
|   2 | The GIL was introduced in 1992 to simplify implementation, improve single-threaded efficiency, and avoid deadlock hazards.                          |
|   3 | Modern multi-core hardware makes the GIL a bottleneck, preventing Python from fully utilizing available CPU cores.                                  |
|   4 | PEP 703 was accepted in October 2023, leading to the first official free-threaded release in Python 3.13.                                           |
|   5 | Python 3.14 significantly improves free-threaded performance by enabling the specializing interpreter and implementing deferred reference counting. |
|   6 | Biased reference counting splits reference counts into local and shared fields to reduce atomic operation overhead.                                 |
|   7 | Immortalization and deferred reference counting techniques minimize reference count modifications to improve multi-threaded scaling.                |
|   8 | Collection thread safety is achieved using lightweight per-instance locks based on WebKit design principles.                                        |
|   9 | A new Python critical sections API implicitly releases locks to prevent deadlocks in mutable collections and modules.                               |
|  10 | Python 3.13 free-threaded builds had memory leak hacks and were 40% slower on single-threaded tasks due to a disabled specializing interpreter.     |
|  11 | Python 3.14 free-threaded builds are generally less than 10% slower than GIL-enabled builds on Intel CPUs, meeting steering council criteria.       |
|  12 | Future plans for Python 3.15 include auditing the standard library for thread safety and creating a stable ABI for C extensions.                    |
|  13 | PyreFly is an open-source, standards-compliant Python type checker developed by Meta using Rust.                                                    |
|  14 | PyreFly is designed for high performance, achieving approximately 1.8 million lines per second on large codebases.                                  |
|  15 | It is 35 times faster than Pyre and 14 times faster than Pyright and MyPy in benchmark tests.                                                       |
|  16 | PyreFly uses module-level parallelism and incrementality to maintain sub-100-millisecond response times in large projects.                          |
|  17 | The tool prioritizes type inference for function returns, local variables, and containers to reduce annotation burden.                              |
|  18 | PyreFly is IDE-first, featuring an LSP server, Visual Studio Code extension, and in-memory transactional state for concurrent operations.           |
|  19 | The project is open-source under the MIT license, with active community contribution and issue resolution.                                          |
|  20 | PyreFly operates in three phases: resolving module exports, analyzing statement bindings, and determining expression types.                         |
|  21 | The team chose Rust for cross-platform compatibility and speed, avoiding OCaml's limitations on Windows and threading.                              |
|  22 | PyreFly handles complex typing features like generics, overloads, and recursion from the initial prototype stage.                                   |
|  23 | Variance inference is not yet implemented, but standard covariant, invariant, and contravariant annotations are supported.                          |
|  24 | The tool aims to balance type safety with Python's simplicity, allowing users to adopt types gradually without maximalist requirements.             |
|  25 | PyreFly is being rolled out internally at Meta and is available for public use via pip and the Visual Studio Code marketplace.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZTSZ1OCUaeQ/hqdefault.jpg)](https://www.youtube.com/watch?v=ZTSZ1OCUaeQ)

[Watch on YouTube](https://www.youtube.com/watch?v=ZTSZ1OCUaeQ)
