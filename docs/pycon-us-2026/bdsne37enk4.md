---
layout: default
title: "The Bakery: How PEP810 sped up my bread operations business - Jacob Coffee"
nav_order: 76
parent: PyCon US 2026
type: Video Note
description: "Jacob Coffee, a Python Software Foundation engineer, presents PEP 810, a new feature for Python 3.15 that introduces explicit lazy imports to significantly reduce application startup time and memor..."
resource: "https://www.youtube.com/watch?v=BdSne37enK4"
youtube_stats:
  view_count: 178
  like_count: 2
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

Jacob Coffee, a Python Software Foundation engineer, presents PEP 810, a new feature for Python 3.15 that introduces explicit lazy imports to significantly reduce application startup time and memory usage.
By adding the `lazy` keyword to import statements, developers can defer module loading until the code is actually executed, which is particularly beneficial for large command-line tools, serverless functions, and test suites where eager imports cause unnecessary overhead.
The talk highlights real-world data from companies like Meta and HRT, which reported startup time reductions of 50–70% and memory savings of 30–40% after implementing similar lazy import mechanisms.
Coffee demonstrates the syntax and performance gains using a sample bread-baking CLI, showing that lazy imports create lightweight proxy objects that only trigger the actual import upon first access.
However, he cautions against blindly converting all imports to lazy, as this can hide missing dependencies, break side effects like logging configuration, and complicate debugging of circular imports, recommending instead a selective approach targeting heavy, optional modules.

# Main Points

|   # | Main point                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------- |
|   1 | PEP 810 introduces explicit lazy imports in Python 3.15, allowing imports to be deferred until first access.        |
|   2 | Python startup time is expensive due to the eager import model, which loads all modules immediately even if unused. |
|   3 | Eager imports cause memory bloat and slow down command-line tools, serverless cold starts, and growing test suites. |
|   4 | Meta’s internal fork showed 50-70% startup time reduction and 30-40% memory savings with lazy imports.              |
|   5 | PySide observed a 35% startup improvement, and HRT has used lazy importing for years.                               |
|   6 | The syntax requires adding the `lazy` keyword before the import statement, such as `lazy import httpx`.             |
|   7 | Lazy imports create a lightweight proxy object in the namespace that defers file I/O and code execution.            |
|   8 | The real import occurs only when an attribute of the module is accessed, transparently replacing the proxy.         |
|   9 | This approach keeps commands like `--help` fast because heavy dependencies are not loaded unless needed.            |
|  10 | The feature aligns with Python’s philosophy that explicit is better than implicit.                                  |
|  11 | PEP 810 was accepted and is available in the Python 3.15 beta release.                                              |
|  12 | Real-world benchmarks show 23-26% faster execution for help commands and module imports in demo scenarios.          |
|  13 | Use cases include command-line tools, GUI applications, plugin architectures, and serverless functions.             |
|  14 | Lazy imports eliminate the need for `if TYPE_CHECKING` blocks, cleaning up module code.                             |
|  15 | Test suites benefit from faster discovery phases by importing only necessary modules at runtime.                    |
|  16 | Serverless environments like AWS Lambda and Cloudflare Workers see 50-70% faster cold starts.                       |
|  17 | Memory-constrained environments such as edge devices benefit from reduced memory usage.                             |
|  18 | Developers should not lazy import everything; selective application is recommended for best results.                |
|  19 | Profile existing code to identify heavy imports taking over 50 milliseconds before converting them.                 |
|  20 | Lazy imports can hide missing dependencies or import errors until the module is first accessed in production.       |
|  21 | Side effects like logging configuration or database connections may fail if deferred incorrectly.                   |
|  22 | Circular imports involving lazy modules may only surface as errors when the circular dependency is triggered.       |
|  23 | Lazy imports cannot be used inside function definitions according to the PEP specifications.                        |
|  24 | The reference implementation is available in the CPython mainline beta and a GitHub fork.                           |
|  25 | Design principles include explicit syntax, local scope per import, and granular control over imports.               |
|  26 | Teams should document lazy imports and test both eager and lazy scenarios during migration.                         |
|  27 | Tools like Hyperfine are recommended for benchmarking performance improvements after migration.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BdSne37enK4/hqdefault.jpg)](https://www.youtube.com/watch?v=BdSne37enK4)

[Watch on YouTube](https://www.youtube.com/watch?v=BdSne37enK4)
