---
layout: default
title: "How two teams are working together to make Python better for all - Michael Droettboom, Dino Viehland"
nav_order: 108
parent: PyCon US 2025
type: Video Note
description: "This presentation by Michael Dudboom and Dino Van Rossum details the collaborative efforts of the Faster CPython and Free Threading teams to enhance Python’s performance in both single-threaded and..."
resource: "https://www.youtube.com/watch?v=-MVih3km4G4"
youtube_stats:
  view_count: 1843
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

This presentation by Michael Dudboom and Dino Van Rossum details the collaborative efforts of the Faster CPython and Free Threading teams to enhance Python’s performance in both single-threaded and multi-threaded environments.
The Faster CPython team focuses on optimizing single-threaded speed through a specializing adaptive interpreter and a just-in-time compiler that utilizes micro-opcodes to eliminate redundant type checks and optimize bytecode execution.
Simultaneously, the Free Threading team works to remove the Global Interpreter Lock (GIL) to enable true parallelism, employing techniques such as biased reference counting, lock-free container reads, and the Mimalloc allocator to manage memory safely without contention.
The teams have successfully integrated these initiatives by implementing per-thread bytecode copies to ensure thread-safe specialization and developing stack references to reduce the overhead of reference counting in free-threaded builds.
Beyond technical implementation, the speakers emphasize the importance of shared benchmarks, synchronous communication, and consensus-driven development to navigate the complexities of upstreaming these changes into core CPython while avoiding the pitfalls of maintaining incompatible internal forks.

# Main Points

|   # | Main point                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The Faster CPython team focuses on single-threaded performance via a specializing adaptive interpreter and JIT compiler, while the free-threading team removes the Global Interpreter Lock to enable multi-core scaling. |
|   2 | The specializing adaptive interpreter optimizes bytecode by replacing generic operations with type-specific ones, such as integer multiplication, to eliminate runtime type checking overhead.                           |
|   3 | A tier-2 interpretation system uses micro-opcodes to allow further optimizations, such as removing redundant guards when input types are guaranteed to remain consistent.                                                |
|   4 | The Global Interpreter Lock is removed to allow concurrent execution, requiring new mechanisms to manage shared state and memory safety without data races.                                                              |
|   5 | Biased reference counting allows the owning thread to modify local reference counts without atomic operations, while cross-thread access requires atomic updates to shared counts.                                       |
|   6 | Core data structures like lists and dictionaries use lock-free read algorithms to prevent contention, relying on complex memory management to handle concurrent mutations safely.                                        |
|   7 | The mimalloc allocator replaces the default allocator to provide thread-safe, largely lock-free memory management in free-threaded builds.                                                                               |
|   8 | Lock-free reads from containers involve verifying object ownership and shared reference counts to ensure objects are not freed by other threads during access.                                                           |
|   9 | Mutable interpreter state, including bytecode, inline caches, and type versions, requires thread-safe protection because the specializing interpreter mutates bytecode at runtime.                                       |
|  10 | To resolve bytecode mutation conflicts, each thread maintains its own copy of the bytecode, allowing independent specialization without locking overhead.                                                                |
|  11 | Shared key dictionaries and inline dictionaries for object attributes introduce additional mutable state that must be managed thread-safely during attribute access.                                                     |
|  12 | Type mutations use a global type lock to invalidate class hierarchies and update inline caches atomically, ensuring consistency across threads.                                                                          |
|  13 | Stack references track borrowed and owned references within the interpreter loop, reducing reference counting overhead and improving performance in both build types.                                                    |
|  14 | Performance benchmarks show that free-threaded builds with the specializing interpreter enabled are only 1% to 10% slower than GIL-enabled builds on some platforms.                                                     |
|  15 | Standard benchmark suites are currently single-threaded, and there is a need to develop benchmarks that measure scalability and concurrency performance.                                                                 |
|  16 | Large tech companies previously maintained incompatible internal Python forks, but both Microsoft and Meta now prioritize upstream contributions to benefit the broader community.                                       |
|  17 | Effective collaboration between teams relies on shared goals, standard benchmarks, synchronous weekly meetings, and consensus-driven development processes within the CPython community.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-MVih3km4G4/hqdefault.jpg)](https://www.youtube.com/watch?v=-MVih3km4G4)

[Watch on YouTube](https://www.youtube.com/watch?v=-MVih3km4G4)
