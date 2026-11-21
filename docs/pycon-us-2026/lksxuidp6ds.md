---
layout: default
title: "Why you, as a Python developer, should learn Rust - Daniel Szoke"
nav_order: 71
parent: PyCon US 2026
type: Video Note
description: "Daniel, a software engineer at Sentry who transitioned from maintaining the Python SDK to the Rust SDK, presents a compelling case for Python developers to learn Rust."
resource: "https://www.youtube.com/watch?v=lkSxUIdP6Ds"
youtube_stats:
  view_count: 774
  like_count: 11
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

Daniel, a software engineer at Sentry who transitioned from maintaining the Python SDK to the Rust SDK, presents a compelling case for Python developers to learn Rust.
He highlights that Rust’s primary advantage is its strict compile-time error checking, which enforces type and memory safety by requiring explicit handling of potential null values and immutable data, thereby preventing many runtime errors common in Python.
The talk delves into Rust’s unique ownership and borrowing system, which manages memory without a garbage collector and ensures data integrity through strict rules on mutable and immutable references, as well as its robust concurrency safety guarantees.
Additionally, Daniel emphasizes the value of Rust’s tooling, such as the compiler’s detailed error messages and linters like Clippy and Rustfmt, which provide immediate feedback and enforce consistent code style, aiding both human developers and AI coding agents.
Ultimately, he argues that learning Rust cultivates a mindset of rigorous safety and explicit error handling that improves code quality even when returning to Python, while also offering the performance benefits of a compiled language for critical system components.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Rust surfaces many errors at compile time, unlike Python which often reveals them at runtime. |
|   2 | The Rust compiler enforces type and memory safety, requiring explicit handling of potential null values or type mismatches. |
|   3 | In Rust, all values are immutable by default, requiring explicit declaration to allow mutation. |
|   4 | Passing immutable references guarantees that the data will not be changed by the receiving function. |
|   5 | Rust ownership ensures memory safety without a garbage collector by tracking who owns data allocations. |
|   6 | Moving ownership transfers data, preventing the original variable from being used after the move. |
|   7 | Borrowing allows sharing data without transferring ownership, enabling multiple immutable references or a single mutable reference. |
|   8 | Concurrent mutable and immutable borrows are prohibited to prevent data races and invalid memory access. |
|   9 | Rust's compiler checks concurrency safety, forcing the use of types that safely share data across threads. |
|  10 | Rust's compiler provides detailed error messages and suggestions that aid learning and assist coding agents. |
|  11 | Linters like Clippy enforce best practices and simplify code, providing immediate feedback for developers and agents. |
|  12 | Rustfmt is a standardized formatter that ensures consistent code style across Rust projects. |
|  13 | Learning Rust complements Python by offering high performance and systems-level control where Python excels in rapid iteration and data science. |
|  14 | Rust's safety concepts, such as handling all cases and managing shared state, improve coding habits when writing Python. |
|  15 | Python developers must be more careful with error handling and state management since they lack Rust's compile-time safety net. |
|  16 | The Rust compiler's instant feedback loop helps resolve issues quickly, reducing the learning curve for new users. |
|  17 | Rust idioms differ from Python, requiring developers to check safety conditions before executing operations rather than relying on exception handling. |
|  18 | Integrating Python with Rust is possible, though specific infrastructure details may require further research. |
|  19 | CPU-bound tasks can potentially be optimized by writing specific portions of the code in Rust. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/lkSxUIdP6Ds/hqdefault.jpg)](https://www.youtube.com/watch?v=lkSxUIdP6Ds)

[Watch on YouTube](https://www.youtube.com/watch?v=lkSxUIdP6Ds)
