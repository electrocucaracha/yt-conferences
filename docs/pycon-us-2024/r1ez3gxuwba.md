---
layout: default
title: "Talks - Charlie Marsh: Ruff: An Extremely Fast Python Linter and Code Formatter, Written in Rust"
nav_order: 154
parent: PyCon US 2024
type: Video Note
description: "Charlie Marsh from Astral presents Ruff, an extremely fast Python linter, formatter, and code transformation tool written in Rust."
resource: "https://www.youtube.com/watch?v=r1EZ3GXuwBA"
youtube_stats:
  view_count: 4488
  like_count: 118
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

Charlie Marsh from Astral presents Ruff, an extremely fast Python linter, formatter, and code transformation tool written in Rust.
He explains that Ruff’s speed stems from a compiler-like pipeline that tokenizes, parses, and semantically analyzes code once, eliminating the duplication found in running multiple separate tools.
Key performance strategies include leveraging Rust’s memory management to avoid heap allocations for small integers, replacing regular expressions with hand-written lexers for specific tasks, and indexing code by byte offsets rather than line and column numbers to optimize internal data access.
Additionally, the team replaced a generated parser with a handwritten one to improve error recovery, maintainability, and overall speed by up to 40%.
Marsh emphasizes that achieving such performance requires a culture of data-driven decision-making, continuous benchmarking, and treating performance as a first-class concern throughout the development process.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Ruff is a high-performance Python linter, formatter, and code transformation tool written in Rust.                             |
|   2 | The project aims to become a complete static analysis toolchain for the Python ecosystem.                                      |
|   3 | Ruff processes source code through a pipeline of tokenization, parsing, semantic analysis, and diagnostic generation.          |
|   4 | Rust provides a fast baseline and fine-grained memory control, enabling significant performance optimizations.                 |
|   5 | Ruff avoids duplication by tokenizing, parsing, and analyzing code once for all rules, unlike separate tools.                  |
|   6 | Concurrency and parallelism are maximized using Rust's fearless concurrency and SIMD instructions.                             |
|   7 | A culture of performance treats optimization as a first-class concern, grounded in data and continuous benchmarking.           |
|   8 | Integer parsing was optimized by using a small integer representation to avoid heap allocations for common values.             |
|   9 | Suppression comment parsing was sped up by replacing regular expressions with a hand-written lexer.                            |
|  10 | Internal indexing was changed from row and column to byte offsets to improve slicing efficiency and reporting speed.           |
|  11 | The parser was rewritten from a generated grammar to a handwritten implementation to support error recovery and optimization.  |
|  12 | The handwritten parser allowed for better handling of invalid code and significantly improved parsing speed.                   |
|  13 | Performance improvements are validated using continuous benchmarking tools like Criterion and profiling data.                  |
|  14 | Ruff is developed by Astral, a venture-backed company that keeps the tool free and open source.                                |
|  15 | The project prioritizes data-driven decisions, ensuring optimizations are measurable and beneficial.                           |
|  16 | Unsafe code is used sparingly in Ruff to maintain safety while allowing specific low-level optimizations.                      |
|  17 | Benchmarking strategies include micro-benchmarks for specific components and whole-program benchmarks for real-world projects. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/r1EZ3GXuwBA/hqdefault.jpg)](https://www.youtube.com/watch?v=r1EZ3GXuwBA)

[Watch on YouTube](https://www.youtube.com/watch?v=r1EZ3GXuwBA)
