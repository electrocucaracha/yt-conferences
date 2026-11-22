---
layout: default
title: "Unraveling Community Support For Free-Threaded Python - Lysandros Nikolaou & Nathan Goldbaum"
nav_order: 84
parent: PyCon US 2025
type: Video Note
description: "Developers from Quansite Labs, Lisandro and Nathan Goldbomb, presented on unraveling community support for free-threaded Python, explaining how the removal of the Global Interpreter Lock (GIL) allo..."
resource: "https://www.youtube.com/watch?v=EuU3ksI1l04"
youtube_stats:
  view_count: 1725
  like_count: 44
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

Developers from Quansite Labs, Lisandro and Nathan Goldbomb, presented on unraveling community support for free-threaded Python, explaining how the removal of the Global Interpreter Lock (GIL) allows multiple threads to simultaneously access the CPython C API.
While the core API for attaching and detaching thread states remains identical to the GIL-enabled build, the primary challenge for native extensions is eliminating data races caused by global state, which results in undefined behavior.
To address this, the team outlined a migration strategy involving four levels of support, emphasizing the need for comprehensive documentation, descriptive error handling, and the use of thread-safe primitives such as mutexes, atomics, and thread-local storage.
They also highlighted the importance of using tools like thread sanitizers and parallel testing frameworks to identify and fix concurrency issues in popular packages like NumPy, SciPy, and PyYAML.
Finally, the speakers recommended leveraging modern binding generators like PyO3 and Rust for new extensions, as these technologies offer superior safety and scalability compared to raw C or C++ implementations in a multi-threaded environment.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Python's ability to call native code is mediated by the Global Interpreter Lock (GIL), which limits parallel scaling in multi-threaded programs.                       |
|   2 | In the free-threaded build, the GIL is removed, allowing multiple threads to call the CPython C API simultaneously while still requiring thread state attachment.      |
|   3 | The API for attaching and detaching thread state in the free-threaded build is identical to the GIL-enabled build, simplifying migration for existing C extensions.    |
|   4 | Global state in native extensions is a major source of data races and undefined behavior in free-threaded Python, requiring specific fixes.                            |
|   5 | The ecosystem migration effort involved updating build tools, bindings generators, and major libraries like NumPy, SciPy, and Pandas.                                  |
|   6 | Four levels of free-threading support are defined by PyPI classifiers: unstable, beta, stable, and resilient, based on technical support and documentation.            |
|   7 | Native extensions do not support the free-threaded build out of the box; the GIL is re-enabled at runtime if unsupported extensions are used.                          |
|   8 | Documentation is critical for defining thread safety guarantees, listing unsafe APIs, and providing alternatives for users.                                            |
|   9 | Raising descriptive errors when resources cannot be shared helps users understand limitations and prevents silent failures.                                            |
|  10 | Data races in C and C++ are undefined behavior and must be addressed using tools like ThreadSanitizer and multi-threaded testing.                                      |
|  11 | The pytest-run-parallel package allows running existing test suites in parallel to identify global state issues under free threading.                                  |
|  12 | Focusing on real-world scenarios for multi-threaded tests is more effective than addressing theoretical thread safety issues.                                          |
|  13 | Releasing early with free-threaded support accelerates development by gathering user feedback and preventing GIL re-enablement in dependency trees.                    |
|  14 | Global state issues can be mitigated by making data thread-local in C++, C, Rust, or Python, though portability caveats exist.                                         |
|  15 | Reference counting with borrowed references shared across threads can lead to memory errors if objects are deallocated by other threads.                               |
|  16 | Mutexes can protect global state or wrap thread-unsafe libraries, but they introduce the risk of deadlocks.                                                            |
|  17 | Atomics provide a low-level mechanism to prevent compiler reordering and control timing, though they are complex to implement correctly.                               |
|  18 | Caches can hurt multi-threaded performance; non-critical caches should be disabled, while critical caches require serialization patterns like one-time initialization. |
|  19 | One-time initialization APIs, such as Rust's OnceLock or PyO3's getter_init_py_attached, help serialize state and avoid deadlocks with the interpreter.                |
|  20 | Mutable data structures pose significant challenges, requiring a trade-off between thread safety, scalability, performance, and simplicity.                            |
|  21 | Critical sections offer weaker guarantees than mutexes but are useful for managing internal object state without calling the CPython C API.                            |
|  22 | Native debuggers like LLDB and GDB, along with AddressSanitizer and ThreadSanitizer, are essential for identifying and fixing concurrency issues.                      |
|  23 | Profiling tools like Samply and the Firefox profiler help identify lock contention and scaling issues in multi-threaded Python programs.                               |
|  24 | Replacing critical sections with read-write locks in NumPy improved multi-threaded scaling performance.                                                                |
|  25 | Bindings generators like PyBind11, Cython, and PyO3 are preferred over raw C API calls for writing thread-safe native extensions.                                      |
|  26 | Rust is recommended for new native extensions due to its safety features and ease of writing correct concurrent code.                                                  |
|  27 | Coordination between libraries is needed to manage thread pools and prevent contention, potentially through a central job system.                                      |
|  28 | Redesigning mutable state and the buffer protocol with stronger guarantees, such as borrow checking, is necessary for safer multi-threading.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EuU3ksI1l04/hqdefault.jpg)](https://www.youtube.com/watch?v=EuU3ksI1l04)

[Watch on YouTube](https://www.youtube.com/watch?v=EuU3ksI1l04)
