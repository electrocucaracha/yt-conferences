---
layout: default
title: "Talks - Anthony Shaw: Unlocking the Parallel Universe: Subinterpreters and Free-Threading in..."
nav_order: 140
parent: PyCon US 2024
type: Video Note
description: Anthony Shaw presented a talk at PyCon 2024 on unlocking parallelism in Python 3.13 through subinterpreters and free threading.
resource: "https://www.youtube.com/watch?v=Mp5wKOL4L2Q"
youtube_stats:
  view_count: 2030
  like_count: 52
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

Anthony Shaw presented a talk at PyCon 2024 on unlocking parallelism in Python 3.13 through subinterpreters and free threading.
He explained that while Python 3.12 introduced subinterpreters to allow multiple interpreters to run in parallel within a single process, Python 3.13 adds the ability to disable the Global Interpreter Lock (GIL) for true parallel execution of threads.
Shaw demonstrated a web application using subinterpreters to achieve parallelism similar to multiprocessing but with lower overhead and shared memory capabilities.
He also showcased a "ridiculous" demo where he combined subinterpreters with free threading to run parallel tasks within each interpreter, highlighting that both approaches can coexist depending on the workload.
The talk concluded with a discussion on the challenges of C extension compatibility and the practical implications of these new features for real-world applications like web servers and data processing.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Anthony Shaw presented on unlocking parallel universe subinterpreters and free threading in Python 3.13.                               |
|   2 | Parallelism speedups depend on task segmentation and overheads like pickling, not just dividing time by executor count.                |
|   3 | Python offers threads, coroutines, multiprocessing, and subinterpreters, each with different startup times and use cases.              |
|   4 | In Python 3.12, subinterpreters allow multiple interpreters per process, each with its own GIL, enabling full parallelism.             |
|   5 | Subinterpreters act like multiprocessing with less overhead and shared memory capabilities.                                            |
|   6 | Python 3.13 beta 1 allows disabling the GIL (free threading), enabling true parallel execution of threads within a single interpreter. |
|   7 | Free threading requires a new ABI, special wheels, and a specific CPython build for compatibility.                                     |
|   8 | Removing the GIL involves changing the memory allocator, garbage collector, and fixing C code that assumed GIL presence.               |
|   9 | C extensions are the primary challenge for both subinterpreters and free threading due to thread-safety assumptions.                   |
|  10 | Benchmarks show free threading significantly speeds up CPU-intensive tasks like calculating pi compared to GIL-enabled threads.        |
|  11 | Real-world applications often involve I/O, where the GIL is released, making multi-threading effective even with the GIL.              |
|  12 | A demo used Hypercorn to run a Flask app with eight subinterpreters in a single process, achieving parallel request handling.          |
|  13 | Subinterpreters support hot reloading by closing and restarting individual interpreters without stopping the whole process.            |
|  14 | Combining subinterpreters with free threading allows parallel workloads within a single interpreter using thread pools.                |
|  15 | Coroutines do not automatically utilize multiple cores; they require explicit threading for parallel CPU work.                         |
|  16 | Subinterpreters are ideal for long-running workers and web apps needing isolation and hot reloading.                                   |
|  17 | Free threading is better for tasks easily segmented into threads with quick data exchange needs.                                       |
|  18 | The Python ecosystem relied on the GIL for thread safety, so removing it may break C extensions unpredictably.                         |
|  19 | Migration tools for C extensions to support free threading are not yet fully developed.                                                |
|  20 | MarkupSafe is an example of a library minimizing C extension code to improve flexibility and maintenance.                              |
|  21 | Shared memory via memory views allows data exchange between subinterpreters without slow pickling.                                     |
|  22 | The optimal model may involve one subinterpreter per core, each running an async event loop with threads for CPU work.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Mp5wKOL4L2Q/hqdefault.jpg)](https://www.youtube.com/watch?v=Mp5wKOL4L2Q)

[Watch on YouTube](https://www.youtube.com/watch?v=Mp5wKOL4L2Q)
