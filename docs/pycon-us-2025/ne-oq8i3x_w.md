---
layout: default
title: "What they don't tell you about building a JIT compiler for CPython - Brandt Bucher"
nav_order: 44
parent: PyCon US 2025
type: Video Note
description: "Brandt Booker, a Python core developer at Microsoft, presents a detailed overview of the experimental JIT compiler being developed for CPython, highlighting the practical challenges often overlooke..."
resource: "https://www.youtube.com/watch?v=NE-Oq8I3X_w"
youtube_stats:
  view_count: 3078
  like_count: 120
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

Brandt Booker, a Python core developer at Microsoft, presents a detailed overview of the experimental JIT compiler being developed for CPython, highlighting the practical challenges often overlooked in theoretical discussions.
He explains that the project builds upon the specializing adaptive interpreter introduced in Python 3.11, which has already contributed to a 50% aggregate speedup in Python over the last four years without requiring code changes.
The JIT pipeline translates specialized bytecode into micro-ops for optimization before generating machine code using a "copy and patch" technique that ensures maintainability by deriving assembly templates directly from interpreter definitions.
Booker contrasts method-at-a-time compilation with the tracing JIT approach currently used in CPython, which follows execution paths to create efficient, type-specific code while falling back to the interpreter for dynamic cases.
He also addresses complex engineering hurdles, including memory management with executable data, integration with Python profilers and debuggers, and the need for stack unwinding support.
Looking ahead, the JIT is available as an experimental feature in Python 3.14 binaries, with future work focusing on thread safety for free-threaded builds and improved native debugging capabilities.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Brandt Berge, a Python core developer at Microsoft, presented on the lesser-known aspects of building a JIT compiler for CPython.                              |
|   2 | The Faster CPython project has improved Python performance by approximately 50% over four years without requiring code changes.                                |
|   3 | Python 3.11 introduced specialized bytecode, which rewrites instructions at runtime to create inline fast paths for common type patterns.                      |
|   4 | The JIT compiler pipeline converts specialized bytecode into micro-ops, optimizes them, and translates them into machine code.                                 |
|   5 | Micro-op translation is machine-generated during the build process, ensuring that bugfixes in the interpreter automatically apply to the JIT.                  |
|   6 | Machine code generation uses a copy-and-patch technique with pre-generated templates to reduce manual assembly writing and improve maintainability.            |
|   7 | Region selection determines what, where, when, and why to compile, balancing compilation cost against performance gains.                                       |
|   8 | Method-at-a-time JIT compiles entire functions but struggles with complex control flow and polymorphism, such as handling different iterator types.            |
|   9 | CPython currently uses a tracing JIT that follows execution paths to collect linear traces, allowing for precise type information and aggressive optimization. |
|  10 | Tracing JITs handle dynamic types by falling back to the interpreter for unobserved cases and compiling new traces as those cases become frequent.             |
|  11 | A downside of tracing JITs is code duplication in branchy code, though this can be mitigated with specific optimization techniques.                            |
|  12 | Memory management for JIT code requires using mmap or VirtualAlloc to allocate readable, writable, and executable memory pages.                                |
|  13 | Best practices involve writing code to memory, then changing permissions to read-execute to prevent security vulnerabilities from self-modifying code.         |
|  14 | Python profilers are supported by stopping JIT traces when instrumented bytecode is encountered, allowing the interpreter to handle profiling hooks.           |
|  15 | Validity checks are inserted in JIT code to bail out to the interpreter if a profiler is installed or if global state changes invalidate optimizations.        |
|  16 | Supporting native debuggers like GDB or perf is complex due to the need for stack unwinding and platform-specific debug information registration.              |
|  17 | Python 3.14 includes an experimental JIT in official binaries that can be enabled via an environment variable, though it is not recommended for production.    |
|  18 | Future work for Python 3.15 includes making the JIT thread-safe for free-threading and improving support for native profilers and debuggers.                   |
|  19 | The project relies on community contributions and external expertise to address challenges in debugging, profiling, and concurrency.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NE-Oq8I3X_w/hqdefault.jpg)](https://www.youtube.com/watch?v=NE-Oq8I3X_w)

[Watch on YouTube](https://www.youtube.com/watch?v=NE-Oq8I3X_w)
