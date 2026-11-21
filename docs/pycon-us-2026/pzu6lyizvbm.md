---
layout: default
title: "Free threaded Python  past, present and future - Thomas Wouters"
nav_order: 64
parent: PyCon US 2026
type: Video Note
description: "At PyCon 2026, CPython core developer Thomas Walters presented on the progress of free-threaded Python, a project aimed at removing the Global Interpreter Lock (GIL) to enable true multi-threading ..."
resource: "https://www.youtube.com/watch?v=PZu6LyiZVbM"
youtube_stats:
  view_count: 1115
  like_count: 35
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

At PyCon 2026, CPython core developer Thomas Walters presented on the progress of free-threaded Python, a project aimed at removing the Global Interpreter Lock (GIL) to enable true multi-threading and improve performance on multi-core hardware.
Walters explained that while previous attempts to remove the GIL failed due to significant performance penalties, the current implementation utilizes techniques such as thread-owned objects, deferred reference counting, and a new thread-aware memory allocator to minimize overhead.
The talk highlighted that Python 3.13 introduced experimental support with a 20–40% slowdown, whereas Python 3.14 achieved official support with a reduced 0–10% penalty, and Python 3.15 will feature a stable ABI allowing extension modules to be built once for both GIL and free-threaded builds.
Walters emphasized that migrating existing Python code is generally straightforward, as the language semantics remain consistent, though developers must update C extensions to protect global state and add multi-threaded tests to uncover latent concurrency bugs.
Looking ahead, Walters predicted that free-threaded Python will become the default build option before Python 3.20, eventually leading to the complete removal of the GIL build in the next decade.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Thomas Walters, a CPython core developer and Meta employee, presented on free-threaded Python at PyCon 2026.                                                             |
|   2 | Free-threaded Python removes the Global Interpreter Lock (GIL) to enable true multi-threading and improve performance on multi-core hardware.                            |
|   3 | The GIL was originally added to protect CPython internals and reference counts but limits thread utility and performance.                                                |
|   4 | Alternatives like multiprocessing, sub-interpreters, and asyncio have limitations regarding memory overhead, library compatibility, or single-threaded execution.        |
|   5 | Threads are complex due to shared mutable data, CPU caching, and memory reordering, which complicate data sharing in Python's object model.                              |
|   6 | Previous attempts to remove the GIL, including Greg Stein's patch, PyParallel, and Larry Hastings' GILectomy, failed due to performance penalties or scalability issues. |
|   7 | Sam Gross developed the current approach using techniques like thread ownership, deferred reference counting, and speculative reference count operations.                |
|   8 | The implementation uses quiescent state-based reclamation, fine-grained locks, and a new thread-aware memory allocator called mimalloc.                                  |
|   9 | Critical sections and stop-the-world mechanisms are used to manage state changes and ensure thread safety without relying on the GIL.                                    |
|  10 | Python 3.13 introduced experimental free-threading with a 20-40% performance slowdown, while Python 3.14 reduced this to 0-10% and declared it officially supported.     |
|  11 | Python 3.15 will feature a stable ABI for both free-threaded and GIL builds, allowing extension modules to be built once for both modes.                                 |
|  12 | C extension developers must protect globals, use critical sections for mutable data, and declare free-threading support in the module init function.                     |
|  13 | Migrating Python code is generally straightforward, though existing threading bugs may surface, and scalable containers like FTU tails can help with performance.        |
|  14 | Over half of top PyPI packages with binary wheels already support free-threading, with significant contributions from Meta and Quansight.                                |
|  15 | Free-threading is expected to become the default build option before Python 3.20, eventually replacing the GIL build entirely.                                           |
|  16 | If a non-free-threaded extension is imported, the GIL is re-enabled to maintain compatibility, though this can be overridden for testing.                                |
|  17 | Larry Hastings explained that his earlier GILectomy failed due to unsolvable cross-thread reference counting contention, which modern techniques have since resolved.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/PZu6LyiZVbM/hqdefault.jpg)](https://www.youtube.com/watch?v=PZu6LyiZVbM)

[Watch on YouTube](https://www.youtube.com/watch?v=PZu6LyiZVbM)
