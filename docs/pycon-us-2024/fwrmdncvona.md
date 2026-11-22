---
layout: default
title: "Talks - Yury Selivanov: Overcoming GIL with subinterpreters and immutability"
nav_order: 139
parent: PyCon US 2024
type: Video Note
description: Yuri Salanov presents a solution for building fast Python services by leveraging subinterpreters and immutability to overcome the limitations of the Global Interpreter Lock (GIL) and the high laten...
resource: "https://www.youtube.com/watch?v=fwRMdncVOnA"
youtube_stats:
  view_count: 1229
  like_count: 43
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

Yuri Salanov presents a solution for building fast Python services by leveraging subinterpreters and immutability to overcome the limitations of the Global Interpreter Lock (GIL) and the high latency of network-based multiprocessing.
He introduces "Mamhive," a library that enables efficient data sharing between isolated subinterpreters within a single process, avoiding the slow pickling process required for standard inter-process communication.
The core mechanism relies on immutable data structures, specifically Hash Array Mapped Tries (HAMT), which allow for structured sharing of memory; this means that when data is mutated, only the changed nodes are copied, while the rest are shared, resulting in O(log n) complexity for updates.
Benchmarks demonstrate that this approach is significantly faster than pickling, even for small collections, because it minimizes memory copying and eliminates lock contention.
Although the project is currently a prototype with a "do not use in production" warning, it offers a promising path for high-performance Python applications by enabling safe, lock-free access to shared state across multiple CPU cores.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | A single Python process can run 10 asyncio event loops saturating 10 CPU cores while sharing a mapping with 1 million keys.        |
|   2 | Multiprocessing introduces significant network latency, which is a major bottleneck for fast Python services.                      |
|   3 | Multi-threading in Python is complex and difficult to manage safely due to the Global Interpreter Lock (GIL).                      |
|   4 | Python sub-interpreters allow parallel execution with isolated GILs within the same process, sharing the same memory space.        |
|   5 | The library MHiive facilitates efficient data sharing between sub-interpreters using immutable data structures.                    |
|   6 | MHiive provides a three-level API: basic data transfer, high-level queues and synchronization, and an asyncio bridge.              |
|   7 | Python lacks a native immutable mapping, but immutable types like strings and tuples create new objects upon modification.         |
|   8 | Efficient immutability is achieved using Hash Array Mapped Trie (HAMT) algorithms, offering O(log n) complexity for mutations.     |
|   9 | HAMT uses structured sharing, where only modified tree nodes are copied, allowing massive collections to be updated efficiently.   |
|  10 | Because sub-interpreters share memory, immutable collections can be accessed directly without copying or locking.                  |
|  11 | Mutating a shared immutable mapping in a worker sub-interpreter only requires copying the few changed tree nodes.                  |
|  12 | Benchmarks show that structured sharing is significantly faster than pickling, even when modifying a large portion of the data.    |
|  13 | For small collections, structured sharing remains faster than pickling due to lower overhead.                                      |
|  14 | The implementation requires careful management of reference counting to prevent objects from being garbage collected while in use. |
|  15 | MHiive is currently a prototype with an Apache 2.0 license and is not recommended for production use.                              |
|  16 | The project is being developed by HDB to optimize their database's Python components and cloud deployments.                        |
|  17 | Common use cases include running multiple async programs sharing a cache or dispatching CPU-bound tasks to sub-interpreters.       |
|  18 | Iterating over shared structures may be slightly slower due to pointer dereferencing, but the overhead is manageable.              |
|  19 | Mutable objects within shared structures are currently restricted to prevent unsafe state changes across sub-interpreters.         |
|  20 | A mutation API allows temporary mutable access to HAMT structures, which can then be frozen for safe sharing.                      |
|  21 | The HAMT implementation in Python is inspired by the Clojure programming language and is used internally for context variables.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fwRMdncVOnA/hqdefault.jpg)](https://www.youtube.com/watch?v=fwRMdncVOnA)

[Watch on YouTube](https://www.youtube.com/watch?v=fwRMdncVOnA)
