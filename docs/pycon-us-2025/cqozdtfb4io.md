---
layout: default
title: "🐍 Python meets the crab 🦀 - Friendship at first sight? (Sponsor: Bloomberg)"
nav_order: 68
parent: PyCon US 2025
type: Video Note
description: "Bernard Gabbor presents a comprehensive overview of integrating Rust into Python applications, highlighting the complementary strengths of both languages."
resource: "https://www.youtube.com/watch?v=CqOZdTFb4io"
youtube_stats:
  view_count: 1976
  like_count: 43
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

Bernard Gabbor presents a comprehensive overview of integrating Rust into Python applications, highlighting the complementary strengths of both languages.
He explains that while Python offers ease of use and a rich ecosystem, Rust provides superior performance, memory safety, and concurrency capabilities without a garbage collector.
The talk details the technical workflow using PyO3 as the translation layer and Maturin as the build backend, which compiles Rust code into binary extensions compatible with Python’s import system.
Gabbor demonstrates this by implementing a prime number finder in both languages, showing a significant performance improvement in the Rust version, while also addressing the complexities of type conversion, platform-specific wheel generation, and the steeper learning curve associated with Rust’s ownership model and borrow checker.
He concludes by acknowledging Rust’s debugging challenges and slower compilation times but emphasizes that the resulting reliability and speed make it a valuable tool for performance-critical Python projects.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Rust is a systems programming language created by Mozilla in 2010 and released in 2012, emphasizing speed, strong typing, and concurrency safety through an ownership model.                  |
|   2 | Python is an interpreted, garbage-collected language with optional typing and exception-based error handling, prioritizing readability and ease of use over raw performance.                  |
|   3 | Rust avoids race conditions by making data immutable by default, requiring explicit mutable declarations to modify state, which simplifies concurrent programming.                            |
|   4 | Rust uses Option and Result types for error handling instead of exceptions, where Option represents expected absence of data and Result represents failure cases.                             |
|   5 | PyO3 serves as the translation layer between Python and Rust, handling reference counting, argument parsing, and converting Rust panics into Python BaseExceptions.                           |
|   6 | Maturine is a PEP 517 build backend that compiles Rust code into binary wheels compatible with the Python import system, acting as the primary tool for packaging.                            |
|   7 | Integrating Rust into Python can yield significant performance improvements, such as a 12-fold speed increase in CPU-bound tasks like prime number generation.                                |
|   8 | The Rust ecosystem offers specialized tools like Taibu for TOML parsing and writing, which can be leveraged in Python projects for better code formatting capabilities.                       |
|   9 | Rust code is not platform-independent; it requires the Clang compiler and must be compiled for specific architectures, unlike pure Python code which runs on any interpreter.                 |
|  10 | Distributing Rust-based Python packages requires generating multiple wheels for different operating systems, CPU architectures, and Python versions to avoid requiring users to install Rust. |
|  11 | GitHub Actions can automate the generation of these multi-platform wheels, reducing the manual effort needed to support diverse user environments.                                            |
|  12 | Rust debugging is more challenging than Python due to a less powerful debugger and the need to recompile code for simple changes like adding print statements.                                |
|  13 | The Rust borrow checker enforces strict ownership rules, which can make managing complex data structures like graphs or linked lists difficult for developers.                                |
|  14 | Cython is an alternative to Rust for Python extensions, offering similar performance but lacking Rust's safety guarantees against undefined behavior.                                         |
|  15 | PyO3 manages the Global Interpreter Lock (GIL) by releasing it during Rust execution, allowing Rust code to utilize multiple CPU cores for parallel processing.                               |
|  16 | Type marshalling between Python and Rust requires explicit type definitions in Rust, as Python's dynamic typing does not map directly to Rust's strict integer and data types.                |
|  17 | The Rust community is smaller than Python's but is noted for being helpful, and dependencies can be installed directly from GitHub forks to apply custom fixes.                               |
|  18 | Rust does not publish binary blobs to its registry, meaning all dependencies are compiled from source, which can lead to longer build times but avoids binary compatibility issues.           |
|  19 | Linters like Clippy and formatters like cargo fmt are essential for writing readable and idiomatic Rust code, helping to mitigate the language's syntactic complexity.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CqOZdTFb4io/hqdefault.jpg)](https://www.youtube.com/watch?v=CqOZdTFb4io)

[Watch on YouTube](https://www.youtube.com/watch?v=CqOZdTFb4io)
