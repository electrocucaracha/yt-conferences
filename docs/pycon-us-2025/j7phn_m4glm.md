---
layout: default
title: "Using Rust in Free-Threaded vs Regular Python 3.13 - David Hewitt"
nav_order: 83
parent: PyCon US 2025
type: Video Note
description: "David Huitt from Pydantic presents a talk on integrating Rust with both regular and freethreaded Python 3.13, highlighting how Rust’s strict memory safety rules can help developers navigate the com..."
resource: "https://www.youtube.com/watch?v=J7phN_M4GLM"
youtube_stats:
  view_count: 2607
  like_count: 65
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

David Huitt from Pydantic presents a talk on integrating Rust with both regular and freethreaded Python 3.13, highlighting how Rust’s strict memory safety rules can help developers navigate the complexities of concurrent programming.
He explains that while Python’s Global Interpreter Lock (GIL) historically masked race conditions by serializing thread execution, the new freethreaded mode removes this lock, exposing data races that require explicit synchronization strategies.
Huitt demonstrates how Rust’s principle of exclusive mutability—where shared data cannot be modified—prevents data races, and shows how the PyO3 library enforces this by using reference counting and atomic integers to manage access to Rust state within Python objects.
He further illustrates practical solutions for multithreaded Python code, such as using immutable data structures, lazy initialization with locks, and atomic operations to ensure thread safety without relying on the GIL.
The talk concludes by encouraging developers to adopt Rust-inspired concurrency patterns, such as read-write locks and careful state management, to build robust, high-performance applications in the future of Python.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | David Huitt from Pydantic presented on using Rust with freethreaded and regular Python 3.13 at PyCon 2025.                                            |
|   2 | Freethreaded Python, new in version 3.13, removes the Global Interpreter Lock (GIL) to allow true parallel execution of threads.                      |
|   3 | The GIL historically ensured only one thread executed Python code at a time, hiding race conditions rather than preventing them.                      |
|   4 | Data races occur when multiple threads access shared memory concurrently, leading to undefined behavior and inconsistent results.                     |
|   5 | Rust prevents data races through its ownership system, enforcing that data is either shared or mutable, but not both simultaneously.                  |
|   6 | Atomic integers in Rust provide internal mutability, allowing safe concurrent updates to shared counters without traditional locks.                   |
|   7 | Python's `count += 1` operation is not atomic, causing race conditions in freethreaded builds, whereas Rust's `fetch_add` guarantees consistency.     |
|   8 | For complex data structures, Rust uses locks to ensure exclusivity during modification, which can introduce latency but prevents corruption.          |
|   9 | PyO3, a library for Rust-Python integration, enforces exclusive access rules by tracking readers and writers on Python objects.                       |
|  10 | In freethreaded Python, PyO3 strategies that worked under the GIL may cause more frequent exceptions due to increased concurrency.                    |
|  11 | PyO3 allows users to opt out of reference tracking by marking objects as immutable, similar to frozen dataclasses.                                    |
|  12 | Developers should apply Rust-inspired principles to Python by first determining if data is shared and then if it is modified.                         |
|  13 | Immutable data structures, such as tuples and frozen sets, are recommended to avoid synchronization issues in multithreaded code.                     |
|  14 | For data modified only once, lazy initialization patterns can be used to compute values under a lock and then serve them without further locking.     |
|  15 | For frequently modified data, developers can use read-write locks, split locks into smaller pieces, or utilize atomic operations.                     |
|  16 | Most Python standard library iterators are not thread-safe, so wrapping them with locks is a defensive strategy for multithreaded code.               |
|  17 | Freethreaded Python enables use cases like multithreaded web servers and real-time applications by reducing latency from thread waiting.              |
|  18 | The speaker recommended using PyO3 to leverage Rust's safe data structures when native Python support for specific concurrency primitives is lacking. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/J7phN_M4GLM/hqdefault.jpg)](https://www.youtube.com/watch?v=J7phN_M4GLM)

[Watch on YouTube](https://www.youtube.com/watch?v=J7phN_M4GLM)
