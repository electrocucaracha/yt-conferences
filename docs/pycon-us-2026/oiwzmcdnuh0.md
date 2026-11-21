---
layout: default
title: "The Art of Extending Python with other languages - Cristián Maureira-Fredes"
nav_order: 82
parent: PyCon US 2026
type: Video Note
description: "Christian, a CPython extension developer from Chile, presents a talk aimed at demystifying the creation of Python extensions to encourage developers to overcome their fear of the process."
resource: "https://www.youtube.com/watch?v=OIWzMcDNUh0"
youtube_stats:
  view_count: 276
  like_count: 4
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

Christian, a CPython extension developer from Chile, presents a talk aimed at demystifying the creation of Python extensions to encourage developers to overcome their fear of the process.
He highlights the increasing reliance on compiled languages like C++, Rust, and Zig within popular Python libraries such as PyTorch and Pydantic, noting that these languages provide necessary performance improvements and access to low-level system features.
The speaker demonstrates that creating basic extensions in C and C++ involves manageable boilerplate code, while also introducing binding generators like PyBind11, nanobind, and PyO3 that significantly simplify the integration of these languages with Python.
He further explores the Zig programming language, praising its safety, built-in testing, and cross-compilation capabilities as a viable alternative to C.
By comparing performance benchmarks and discussing the evolving Python ecosystem, Christian argues that learning to extend Python with other languages fosters community growth, bridges technical gaps, and allows developers to optimize critical bottlenecks effectively.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Christian, aims to demystify CPython extensions and encourage developers to try creating them.                                               |
|   2 | Python's evolution has been marked by milestones including scripting, web development with Django, scientific computing, and AI.                          |
|   3 | Many popular Python libraries like PyTorch, Pydantic Core, DuckDB, and UV rely heavily on C++, Rust, or other compiled languages for performance.         |
|   4 | Learning other programming languages offers familiarity with new technologies, access to legacy software, and improved performance.                       |
|   5 | Python has multiple implementations such as RustPython, CircuitPython, PyPy, and Cinder, though CPython remains the standard.                             |
|   6 | Creating a basic CPython extension involves defining new functionality, module definitions, and initialization using boilerplate code from documentation. |
|   7 | Modern build tools like pyproject.toml and the build package simplify the installation of CPython extensions.                                             |
|   8 | C++ is widely used in frameworks and offers features like generics and low-level memory access, with recent versions becoming more Python-like.           |
|   9 | Rust emphasizes performance, reliability, and productivity, using structures instead of classes for object-oriented programming.                          |
|  10 | Zig provides a safer alternative to C with built-in testing, compile-time evaluation, and strong C integration.                                           |
|  11 | Other languages like Gleam, Lua, Carbon, TypeScript, and PHP offer various ways to interact with or extend Python ecosystems.                             |
|  12 | Binding generators like PyBind11, nanobind, Shiboken, PyO3, and CPython simplify the process of creating extensions.                                      |
|  13 | Shiboken allows defining bindings via XML files without modifying source code, which is useful for large frameworks like Qt.                              |
|  14 | PyO3 provides a fantastic API for Rust developers to create Python extensions using procedural macros.                                                    |
|  15 | Exposing compiled languages to Python is complex due to differences in data types, memory management, pointers, and threading.                            |
|  16 | Benchmarks show that C++ implementations can sometimes outperform Rust versions due to lower overhead from binding generators.                            |
|  17 | Extensions are not a solution for every problem but are useful for addressing specific performance bottlenecks.                                           |
|  18 | The Qt framework uses PySide for Python bindings, highlighting the need for efficient cross-language interaction.                                         |
|  19 | Specialized implementations like PyPy, RustPython, Mojo, and Codon offer alternative approaches to Python execution.                                      |
|  20 | Extending Python with other languages keeps the community active and fosters collaboration between Python and Rust communities.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/OIWzMcDNUh0/hqdefault.jpg)](https://www.youtube.com/watch?v=OIWzMcDNUh0)

[Watch on YouTube](https://www.youtube.com/watch?v=OIWzMcDNUh0)
