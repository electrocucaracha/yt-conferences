---
layout: default
title: "Conquer multithreaded Python with Blanket - Larry Hastings"
nav_order: 83
parent: PyCon US 2026
type: Video Note
description: "The speaker introduces Blanket, a new Python library designed to solve the challenge of achieving 100% test coverage for multi-threaded code by eliminating non-deterministic race conditions."
resource: "https://www.youtube.com/watch?v=S3LUpx0hzkw"
youtube_stats:
  view_count: 662
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

The speaker introduces Blanket, a new Python library designed to solve the challenge of achieving 100% test coverage for multi-threaded code by eliminating non-deterministic race conditions.
By replacing standard threading primitives with deterministic "regulated" versions, Blanket allows developers to act as the scheduler, controlling the exact order in which threads acquire locks or pass through barriers.
The library operates on a core concept of blocking thread execution before and after synchronization calls, enabling users to reproduce specific race conditions on demand for reliable unit testing.
It offers a tiered API ranging from low-level transaction control to high-level abstractions like `relay` and `cycle`, which simplify the process of driving threads through complex synchronization scenarios.
Although the tool introduces performance overhead and is intended strictly for testing rather than production use, it provides a robust mechanism for making concurrent code behavior predictable and fully testable.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Blanket is a Python library designed to make multi-threaded code deterministic for unit testing by replacing non-deterministic threading primitives with controlled versions.                       |
|   2 | The primary motivation is to achieve 100% code coverage by making rare race conditions reproducible on demand, rather than relying on random OS scheduler behavior.                                 |
|   3 | Blanket wraps standard synchronization objects like Lock, RLock, Barrier, and Semaphore, binding them to a central Scenario object that acts as the root controller.                                |
|   4 | The core mechanism involves "parking" threads before and after method calls, allowing the main test thread to act as the scheduler and dictate the exact order of operations.                       |
|   5 | The library uses a three-layer API structure: low-level transaction control, medium-level driver objects, and high-level custom APIs like relay for locks and cycle for barriers.                   |
|   6 | Transactions represent specific method calls on primitives and function as state machines that only move forward, enabling precise inspection and control of thread progress.                       |
|   7 | The Scenario.wait method allows the scheduler to wait for specific signals, such as a thread terminating, a transaction completing, or a specific method being called.                              |
|   8 | Blanket objects masquerade as standard threading objects, passing isinstance checks for threading primitives while failing checks for Blanket-specific types to maintain compatibility.             |
|   9 | The library supports injecting Blanket replacements into existing modules via scenario.inject, allowing control over code that creates its own threading objects.                                   |
|  10 | An injector feature allows modifying Python bytecode to insert synchronization calls into lockless data structures, effectively converting them into deterministic, single-threaded-like execution. |
|  11 | The architecture relies on a single internal "score lock" to synchronize access to the core state, ensuring regularity and determinism at the cost of some performance.                             |
|  12 | Blanket is intended for development and testing environments to reproduce bugs, not for production use, as it intentionally introduces overhead to ensure precise control.                          |
|  13 | The project was developed using AI assistance and evolved through several eras, moving from total object simulation to a simpler model where external scheduling controls internal state.           |
|  14 | High-level APIs like relay and cycle are tailored to specific synchronization idioms, yielding control points that allow the scheduler to interleave other operations between thread steps.         |
|  15 | The library's design philosophy is that tests should be effectively single-threaded, requiring developers to slow down execution to ensure every possible interleaving can be explicitly tested.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/S3LUpx0hzkw/hqdefault.jpg)](https://www.youtube.com/watch?v=S3LUpx0hzkw)

[Watch on YouTube](https://www.youtube.com/watch?v=S3LUpx0hzkw)
