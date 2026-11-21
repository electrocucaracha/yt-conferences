---
layout: default
title: "Lock Free Multi Core Performance with Behavior Oriented Concurrency - Mathew Johnson"
nav_order: 31
parent: PyCon US 2026
type: Video Note
description: "Matthew Johnson, a research software engineer at Microsoft Azure Research, presents Boids Pi, a Python module that introduces behavior-oriented concurrency to solve common challenges in multi-core ..."
resource: "https://www.youtube.com/watch?v=LytoGIXLYkY"
youtube_stats:
  view_count: 444
  like_count: 10
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

Matthew Johnson, a research software engineer at Microsoft Azure Research, presents Boids Pi, a Python module that introduces behavior-oriented concurrency to solve common challenges in multi-core scaling.
The talk highlights how traditional concurrent programming often suffers from data races and deadlocks, using the Boids simulation and the dining philosophers problem as motivating examples.
To address these issues, Boids Pi introduces two core concepts: "cones," which provide unique temporal ownership of shared resources to prevent data races, and "behaviors," which are code snippets scheduled by a system that guarantees deadlock freedom.
This approach allows developers to define shared resources and required actions without manually managing locks or thread synchronization, resulting in safer and more maintainable code.
The module is available for Python 3.10 through 3.15, offering full multi-core performance on versions 3.12 and later by leveraging sub-interpreters and the cross-interpreter data interface.
Johnson also discusses future improvements, including deep immutability and region-based sharing, to further optimize performance and reduce serialization overhead.

# Main Points

|   # | Main point                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Matthew Johnson, a research software engineer at Microsoft Azure Research and Cambridge University, presented the Boids Pi module, a group effort with colleagues at Microsoft and Uppsala University. |
|   2 | The Boids agent-based simulation demonstrates emergent flocking behavior but presents complex computational challenges when scaling to multiple cores due to shared grid cell resources.               |
|   3 | Concurrent programming difficulties primarily stem from data races, such as time-of-check-time-of-use errors, and deadlocks caused by circular waiting for locks.                                      |
|   4 | Behavior-oriented concurrency introduces two new concepts: concurrent ownership (cones) for unique temporal resource access and behaviors for scheduling code snippets on any core.                    |
|   5 | Cones guarantee no data races by ensuring only one thread of execution has read and write access to a resource at any given time.                                                                      |
|   6 | The scheduler guarantees no deadlocks by managing behavior execution, allowing code to run with single-threaded semantics while leveraging multi-core performance.                                     |
|   7 | The Bock Pi module is available for Python 3.10 through 3.15 on Linux, Mac, and Windows, utilizing sub-interpreters and multi-gills for multi-core support.                                            |
|   8 | In Python 3.10 and 3.11, the module runs but offers no concurrency benefits, while Python 3.12 and later provide full multi-core performance.                                                          |
|   9 | The module introduces the when decorator to schedule functions as behaviors and the cone object to wrap Python objects with temporal ownership properties.                                             |
|  10 | The dining philosophers problem illustrates how Bock simplifies concurrency by defining forks as cones and eating as behaviors, allowing the scheduler to determine optimal parallelism automatically. |
|  11 | Unlike traditional threading solutions that require symmetry-breaking tricks to avoid deadlock, Bock requires only the definition of shared resources and required actions.                            |
|  12 | Cones are implemented as C objects in CPython, serializing data at rest using the cross-interpreter data format and deserializing it upon acquisition by an interpreter.                               |
|  13 | Attempting to acquire a cone already held by another interpreter results in a clear exception, preventing crashes and aiding debugging.                                                                |
|  14 | Behaviors can schedule other behaviors, enabling work to fan out over time without blocking the current execution flow.                                                                                |
|  15 | Serialization and deserialization costs via the cross-interpreter data API are a potential bottleneck for Bock, particularly for complex user types with minimal computation.                          |
|  16 | PEP 795 proposes deep immutability and separate garbage collection for immutable objects to allow seamless sharing across interpreters without serialization overhead.                                 |
|  17 | Future work includes introducing regions, which are object graphs with a single incoming edge, allowing shared access via cones without serialization.                                                 |
|  18 | Benchmarks on a 14-core machine show near-linear speedup up to eight cores, after which performance plateaus due to operating system resource contention.                                              |
|  19 | Bock Pi is fully opt-in and compatible with free-threading builds, though it currently uses sub-interpreters for type marshalling in non-free-threading environments.                                  |
|  20 | The scheduler operates using multi-producer multi-consumer work-stealing queues to avoid central synchronization costs and ensure distributed execution.                                               |
|  21 | Bock behaviors execute in sub-interpreters, meaning they can safely call third-party libraries that use threads, provided those threads are well-behaved and join correctly.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/LytoGIXLYkY/hqdefault.jpg)](https://www.youtube.com/watch?v=LytoGIXLYkY)

[Watch on YouTube](https://www.youtube.com/watch?v=LytoGIXLYkY)
