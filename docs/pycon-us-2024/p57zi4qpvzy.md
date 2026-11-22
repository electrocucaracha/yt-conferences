---
layout: default
title: "Talks - Ken Jin, Jules Poon: How two undergrads from the other side of the planet are speeding up..."
nav_order: 181
parent: PyCon US 2024
type: Video Note
description: "Ken Jean and Jules Poon presented their work on accelerating CPython, the reference implementation of Python, by developing a new optimization pipeline for Python 3.13 and beyond."
resource: "https://www.youtube.com/watch?v=p57zI4qPVZY"
youtube_stats:
  view_count: 825
  like_count: 18
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

Ken Jean and Jules Poon presented their work on accelerating CPython, the reference implementation of Python, by developing a new optimization pipeline for Python 3.13 and beyond.
They explained that while CPython 3.11 introduced a specializing adaptive interpreter to handle generic bytecode more efficiently, their project extends this by using tracing and optimization to analyze larger regions of code.
The pipeline involves projecting tracers to record straight-line code sequences, breaking them down into micro-operations, and applying optimizations such as guard elimination, function inlining, and deferred object creation.
These techniques, enabled by abstract interpretation and data flow analysis, aim to reduce overheads like type checks and stack operations, with preliminary results showing significant speedups for pure Python workloads.
The speakers also shared their journey as university students who leveraged academic courses in programming language implementation and compiler design to contribute to this complex open-source project, emphasizing the importance of patience and utilizing educational resources.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ken Jean and Jules Poon presented their work on accelerating CPython performance through an experimental Just-In-Time (JIT) compiler pipeline.                                    |
|   2 | CPython is a bytecode stack machine where the interpreter executes generic bytecode that requires dynamic type dispatch, causing overhead.                                        |
|   3 | Python 3.11 introduced a specializing adaptive interpreter that rewrites bytecode into faster, type-specific versions known as tier one bytecode.                                 |
|   4 | Python 3.13 introduces a new optimization pipeline that processes tier one bytecode into traces, optimizes them, and compiles them to machine code.                               |
|   5 | The pipeline begins with projecting tracers, which record straight-line code sequences from loops and break bytecode down into micro-operations.                                  |
|   6 | The optimization stage includes multiple passes, such as promoting globals to constants and performing guard elimination using abstract interpretation.                           |
|   7 | Abstract interpretation analyzes bytecode using abstractions of values, such as types and constants, to enable safe optimizations like removing redundant type checks.            |
|   8 | Function inlining is planned to reduce call overhead by removing frame creation and argument copying, potentially matching C extension function speeds.                           |
|   9 | Deferred object creation, or scalar replacement, aims to avoid creating objects when their values are not strictly needed, improving memory and speed efficiency.                 |
|  10 | Register allocation and top-of-stack caching reduce the cost of stack operations by caching values in local variables.                                                            |
|  11 | The JIT compiler handles side exits and deoptimization, allowing the system to fall back to tier one bytecode or create new traces when assumptions fail.                         |
|  12 | The experimental JIT is not enabled by default in Python 3.13 due to performance inconsistencies and memory usage, with broader improvements targeted for Python 3.14 and beyond. |
|  13 | The speakers emphasized that contributing to CPython as a student benefits from utilizing university resources, such as compiler design and program analysis courses.             |
|  14 | Open source contribution involves more than coding, including documentation, infrastructure, and design, requiring patience and iterative learning.                               |
|  15 | Optimizations are most effective for pure Python workloads, such as data classes, while workloads relying heavily on C extensions like pandas may see limited speedups.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/p57zI4qPVZY/hqdefault.jpg)](https://www.youtube.com/watch?v=p57zI4qPVZY)

[Watch on YouTube](https://www.youtube.com/watch?v=p57zI4qPVZY)
