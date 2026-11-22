---
layout: default
title: "Supercharge your Python library using AST parsing - Adam Glustein"
nav_order: 102
parent: PyCon US 2025
type: Video Note
description: "This presentation by Adam Glostein explores how to optimize high-performance Python libraries by programmatically modifying the Abstract Syntax Tree (AST) of user code."
resource: "https://www.youtube.com/watch?v=A0vR3l1X-CU"
youtube_stats:
  view_count: 6177
  like_count: 162
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

This presentation by Adam Glostein explores how to optimize high-performance Python libraries by programmatically modifying the Abstract Syntax Tree (AST) of user code.
The talk focuses on the open-source library CSP (Composable Stream Processing), which uses a C++ backend for real-time data processing and employs AST transformations to bridge the gap between a user-friendly Python API and a highly efficient compiled implementation.
Key techniques discussed include transforming standard functions into generators to maintain state across multiple invocations, which is essential for stateful nodes in a computation graph.
Additionally, the presentation details how frequently called methods like `ticked` and `output` are substituted with binary or unary operations (such as addition or unary positive) to bypass attribute lookup overhead, resulting in a 1.5 to 2x performance improvement.
A more advanced optimization involves exposing C++ data as local variables in Python by manipulating the AST to map arguments to the fast locals array, allowing for direct memory access without function call indirection.
These strategies enable the library to provide a clean, intuitive interface for users while executing highly optimized, low-level code under the hood, with the speaker noting that while these internal optimizations require careful maintenance across Python versions, they ensure users receive clean stack traces and significant performance gains in critical trading systems.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The talk focuses on using Abstract Syntax Tree (AST) parsing to optimize Python libraries with compiled backends like C++ or Rust.                     |
|   2 | High-performance libraries often use compiled languages for compute-intensive tasks while exposing a Python API via bindings.                          |
|   3 | AST transformations allow modifying user code to fit the compiled implementation better, specifically for hot path functions called frequently.        |
|   4 | These optimizations are practical techniques used in the open-source Composable Stream Processing (CSP) library for real-time data.                    |
|   5 | Python's compilation pipeline involves tokenization, parsing into an AST, and compiling into a code object of bytecode instructions.                   |
|   6 | The AST represents the program structure and can be traversed or modified using standard library tools like ast.NodeVisitor and ast.NodeTransformer.   |
|   7 | Computation graphs are directed acyclic graphs used to execute tasks, with functions as nodes and inputs/outputs as sources/sinks.                     |
|   8 | CSP is a computation graph library where the engine and runtime live entirely in C++, requiring data exposure to Python via the C API.                 |
|   9 | CSP nodes are stateful functions that process time series data, but Python functions are inherently stateless, requiring transformation to generators. |
|  10 | One key AST transformation converts node functions into generators to maintain state variables across multiple invocations in the graph.               |
|  11 | Frequently called member functions like CSP.ticked are optimized by substituting them with unused binary or unary operations on the type object.       |
|  12 | Storing functions in type object slots avoids the load attribute bytecode instruction, resulting in 1.5 to 2 times faster function calls.              |
|  13 | Data living in C++ can be exposed as local variables in Python by mapping them to the fast locals array via AST transformations.                       |
|  14 | This technique allows C++ code to modify Python local variables in place, providing lightning-fast access without function call overhead.              |
|  15 | The resulting bytecode uses load fast instructions for variable access, which is the fastest way to load variables in Python.                          |
|  16 | Users see a clean, high-level API, while the underlying implementation sees optimized, transformed code that is not intended for direct user writing.  |
|  17 | AST stability varies across Python versions, requiring updates to parsing logic when upgrading, such as changes in bytecode instructions.              |
|  18 | Debug information can be corrected using ast.fix_missing_locations to ensure users see accurate line numbers in stack traces.                          |
|  19 | The generator approach for state management is preferred over function attributes to align with the iterator-like nature of graph execution cycles.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/A0vR3l1X-CU/hqdefault.jpg)](https://www.youtube.com/watch?v=A0vR3l1X-CU)

[Watch on YouTube](https://www.youtube.com/watch?v=A0vR3l1X-CU)
