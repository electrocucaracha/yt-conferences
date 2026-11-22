---
layout: default
title: "Talks - Antonio Cuni: SPy (Static Python) lang: fast as C, Pythonic as Python"
nav_order: 193
parent: PyCon US 2024
type: Video Note
description: "Spy is a new programming language designed by Antonio Kuni to address the performance limitations of standard Python by creating a statically typed, compilable subset that retains the language's fa..."
resource: "https://www.youtube.com/watch?v=hnQ0oJ_yXlw"
youtube_stats:
  view_count: 2972
  like_count: 84
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

Spy is a new programming language designed by Antonio Kuni to address the performance limitations of standard Python by creating a statically typed, compilable subset that retains the language's familiar syntax and high-level features.
Unlike other projects that restrict Python to simple numerical loops, Spy aims to support complex application logic, such as web frameworks and database ORMs, by introducing a three-phase execution model: import time, a "freeze" phase where objects become immutable, and runtime.
This architecture enables a process called "red shift," where partial evaluation optimizes away dynamic lookups, type checks, and other overheads before compilation, resulting in code that is both safe and significantly faster.
The language uses a distinct file extension to avoid confusion with CPython and offers both lazy and eager error reporting modes to balance developer experience with strict type safety.
Ultimately, Spy targets high-performance outputs like WebAssembly and C extensions, allowing developers to write Pythonic code that compiles to efficient machine instructions without sacrificing the expressive power of the original language.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Spy is a static Python variant designed to be fast, safe, and easy to implement by removing dynamic features that hinder compilation.                 |
|   2 | The project aims to preserve Pythonic syntax while enabling compilers to generate efficient code by resolving ambiguities present in standard Python. |
|   3 | Spy introduces a three-phase execution model: import time, freeze phase, and runtime, which allows for static resolution of logic.                    |
|   4 | During the import phase, all modules and dependencies are statically resolved, preventing dynamic imports that complicate compilation.                |
|   5 | The freeze phase locks the state of the program, making objects immutable by default to enable aggressive optimization and partial evaluation.        |
|   6 | A process called "Red Shift" removes dynamic "blue" nodes from the execution graph, leaving only static "red" nodes for the compiler to handle.       |
|   7 | Type annotations are strictly enforced, with options for lazy or eager error reporting to balance developer experience and safety.                    |
|   8 | Operator dispatch is determined by static types rather than dynamic runtime types, allowing for specialized function generation.                      |
|   9 | Generics are implemented by creating specialized copies of functions or classes for specific types, such as int32 or float64.                         |
|  10 | The language uses a new file extension, .spy, to distinguish it from standard Python and avoid compatibility confusion.                               |
|  11 | Spy supports both interpreted mode for debugging and compiled mode for performance, with the compiler generating C code for execution.                |
|  12 | Low-level operations, such as memory access for C-like structures, can be implemented in Python-like syntax and optimized away at compile time.       |
|  13 | WebAssembly is a primary target, enabling efficient interaction with JavaScript by resolving high-level Python calls into low-level operations.       |
|  14 | The project plans to integrate with CPython and Cinder, allowing Spy to emit specialized bytecode compatible with existing Python implementations.    |
|  15 | The design prioritizes steady performance and ease of implementation over chasing complex optimizer behaviors found in other Python JITs.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hnQ0oJ_yXlw/hqdefault.jpg)](https://www.youtube.com/watch?v=hnQ0oJ_yXlw)

[Watch on YouTube](https://www.youtube.com/watch?v=hnQ0oJ_yXlw)
