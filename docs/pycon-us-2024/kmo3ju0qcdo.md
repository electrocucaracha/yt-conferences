---
layout: default
title: "Talks - Brandt Bucher: Building a JIT compiler for CPython"
nav_order: 141
parent: PyCon US 2024
type: Video Note
description: "Brandt Booker, a Python core developer working on Microsoft’s Faster CPython team, presents CPython’s new experimental Just-In-Time (JIT) compiler, which builds upon the specializing adaptive inter..."
resource: "https://www.youtube.com/watch?v=kMO3Ju0QCDo"
youtube_stats:
  view_count: 1871
  like_count: 62
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

Brandt Booker, a Python core developer working on Microsoft’s Faster CPython team, presents CPython’s new experimental Just-In-Time (JIT) compiler, which builds upon the specializing adaptive interpreter introduced in Python 3.11 and the micro-op interpreter in 3.13.
The presentation explains how the system collects runtime profiling data to identify hot code paths, lowers them into micro-ops, and optimizes them by removing unnecessary guards and overhead.
To address the interpretive overhead of the micro-op interpreter, the JIT compiles these optimized traces into machine code using the "copy and patch" technique, which leverages LLVM to generate fast, portable code with minimal runtime dependencies and low implementation complexity.
This approach allows CPython to maintain broad platform support across various operating systems and architectures while sacrificing peak performance for maintainability and ease of deployment.
The experimental JIT in Python 3.13 successfully overcomes the 20% slowdown associated with the micro-op interpreter, providing a baseline for further performance improvements in future releases.

# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Brandt Booker, a Python core developer on Microsoft's faster CPython team, presented CPython's new experimental Just-In-Time (JIT) compiler.                                                     |
|   2 | CPython 3.11 introduced a specializing adaptive interpreter that collects runtime profiling data, such as types and hot code paths, to optimize bytecode.                                        |
|   3 | CPython 3.12 added infrastructure to automatically generate the interpreter from a Domain Specific Language (DSL) specification, reducing boilerplate and enabling multiple execution pipelines. |
|   4 | CPython 3.13 introduced a micro-op interpreter that lowers hot code paths to a new bytecode format, optimizes them, and executes them in a dedicated pipeline.                                   |
|   5 | The micro-op interpreter currently results in a 20% performance slowdown due to increased dispatch overhead and complex instruction decoding compared to the base interpreter.                   |
|   6 | The JIT compiler aims to overcome this overhead by compiling optimized micro-op traces directly to machine code, reducing interpretive costs.                                                    |
|   7 | Key JIT optimizations include burning in constants, moving data from heap memory to registers, and creating straight-line code sequences to eliminate dispatch overhead.                         |
|   8 | Deployment goals for the JIT include broad platform support, few runtime dependencies, and low implementation complexity to ensure maintainability by volunteers.                                |
|   9 | The implementation utilizes the "Copy and Patch" technique, which generates template JIT compilers by extracting instruction bodies from the C interpreter at build time.                        |
|  10 | Copy and Patch works by compiling instruction templates into ELF files, extracting machine code bytes and relocation records, and patching them into executable memory at runtime.               |
|  11 | This approach allows for localized optimizations, such as replacing indirect jumps with fall-throughs and encoding immediate values, resulting in faster code generation and execution.          |
|  12 | The build-time implementation consists of approximately 1,000 lines of Python and 100 lines of C, while the runtime core is about 400 lines of simple C with no external runtime dependencies.   |
|  13 | The JIT supports x86-64, 32-bit Windows, and ARM64 across major operating systems, leveraging LLVM for platform support.                                                                         |
|  14 | In CPython 3.13, the experimental JIT overcomes the 20% micro-op interpreter slowdown, though it currently uses about 10% more memory.                                                           |
|  15 | Users can build the JIT by adding the `--enable-experimental-jit` flag to their build configuration, requiring LLVM 18 to be installed.                                                          |
|  16 | PEP 744 documents the design decisions and background of the JIT compilation feature, while PEP 659 covers the earlier specializing interpreter.                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kMO3Ju0QCDo/hqdefault.jpg)](https://www.youtube.com/watch?v=kMO3Ju0QCDo)

[Watch on YouTube](https://www.youtube.com/watch?v=kMO3Ju0QCDo)
