---
layout: default
title: "Better Together: How Types Make Python Fly (Sponsor: Meta)"
nav_order: 100
parent: PyCon US 2026
type: Video Note
description: "Alex Malyshev and Dino Vlieland from Meta’s Python runtime team presented a prototype project that integrates Pyre Fly, a high-speed Rust-based type checker, with Cinder X, a pip-installable extens..."
resource: "https://www.youtube.com/watch?v=NKriJIlpC3c"
youtube_stats:
  view_count: 1320
  like_count: 6
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

Alex Malyshev and Dino Vlieland from Meta’s Python runtime team presented a prototype project that integrates Pyre Fly, a high-speed Rust-based type checker, with Cinder X, a pip-installable extension featuring a JIT compiler and Static Python capabilities.
The core objective is to leverage static type information to generate faster machine code, demonstrated by a benchmark where adding type checking reduced execution time from 3.0 to 2.0 seconds.
Cinder X’s JIT compiler specializes code based on runtime type observations, such as converting generic Python float operations into efficient native double arithmetic, while Static Python uses explicit type annotations to enable primitive types, unboxed storage, and direct CPU dispatch, effectively replacing Cython without requiring a separate build step.
By utilizing Pyre Fly’s JSON type reports, the system can infer types for compilation, though the presenters emphasized that this integration is currently "wildly unsafe" and requires further work to handle edge cases like dynamic collections and type ignore directives.
The team reported that these technologies yield a 10–15% performance improvement in Instagram’s production environment and up to 45% in specific benchmarks, highlighting a future direction where type checkers directly drive runtime optimization for Python code.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Pyre Fly is a fast Rust-based type checker for Python that checks PyTorch in under three seconds and Instagram's codebase in under 14 seconds.                |
|   2 | Pyre Fly reached version 1.0, is production-ready, and supports Pydantic and Django types.                                                                    |
|   3 | Cinder X is a pip-installable extension developed at Meta to improve Python performance, supporting Python 3.14 and later.                                    |
|   4 | Cinder X includes a JIT compiler, a bundled interpreter, a parallel garbage collector, and Static Python features.                                            |
|   5 | The Cinder X JIT is a method JIT that compiles individual functions, unlike CPython's tracing JIT which optimizes hot code traces.                            |
|   6 | Cinder X uses a hand-written code generator and the AsmJit library for efficient assembly generation.                                                         |
|   7 | The Cinder X JIT achieves 10-15% performance improvements in Instagram production environments.                                                               |
|   8 | Static Python leverages type annotations to compile more performant code and adds runtime type enforcement.                                                   |
|   9 | Static Python uses custom bytecode extensions via PEP 523 to implement a custom interpreter loop.                                                             |
|  10 | Static Python introduces primitive types like int64 and double, as well as checked lists and dicts for type safety.                                           |
|  11 | Static Python replaces Cython in Instagram, eliminating the need for a separate build step and improving IDE experience.                                      |
|  12 | The integration of Pyre Fly and Static Python uses Pyre Fly's JSON type reports to guide compilation, reducing the need for internal type analysis.           |
|  13 | Challenges in integration include handling collections with 'any' types and managing Pyre Fly ignore directives that may provide inaccurate type information. |
|  14 | Cinder X supports Linux, macOS, and Windows, with Linux x86 being the most stable platform.                                                                   |
|  15 | The project aims to upstream optimizations to CPython, including code function type watchers and inline comprehensions.                                       |
|  16 | Future work includes expanding Static Python capabilities, improving OSS performance parity, and exploring compatibility with other type checkers.            |
|  17 | Benchmarks show Richards benchmark is 45% faster with Cinder X JIT on Linux x86.                                                                              |
|  18 | Static Python allows for efficient dispatch and primitive operations, significantly speeding up hot code paths.                                               |
|  19 | The team emphasizes that the current integration is a prototype and described as "wildly unsafe" due to ongoing development.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NKriJIlpC3c/hqdefault.jpg)](https://www.youtube.com/watch?v=NKriJIlpC3c)

[Watch on YouTube](https://www.youtube.com/watch?v=NKriJIlpC3c)
