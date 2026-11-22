---
layout: default
title: "Talks - Josh Wiedemeier: There and Back Again: Reverse Engineering Python Binaries"
nav_order: 143
parent: PyCon US 2024
type: Video Note
description: "Josh Weedem, a PhD student at the University of Texas at Dallas, presents a detailed overview of Python bytecode decompilation, explaining how CPython compiles source code into bytecode and how tha..."
resource: "https://www.youtube.com/watch?v=rZ_YAm9ywuo"
youtube_stats:
  view_count: 367
  like_count: 7
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

Josh Weedem, a PhD student at the University of Texas at Dallas, presents a detailed overview of Python bytecode decompilation, explaining how CPython compiles source code into bytecode and how that process can be reversed.
He outlines the manual decompilation workflow, which involves three key steps: segmentation to identify statement boundaries, statement translation to convert bytecode instructions into source code logic, and control flow reconstruction to reassemble the program structure using a control flow graph.
Weedem highlights the challenges posed by frequent changes in the Python bytecode specification across versions, noting that this requires constant maintenance for traditional decompilers like Uncomp6.
To address these scalability issues, he introduces Bilingual, a neural decompiler that uses Transformer models to learn bytecode semantics from data, thereby automating the segmentation and translation tasks while mechanically handling control flow.
The talk concludes with a demonstration of Bilingual’s ability to detect and correct decompilation errors by verifying the output against the original bytecode, showcasing how manual skills can complement automated tools to ensure accurate source code recovery.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The CPython interpreter compiles source code into bytecode before execution, rather than reading the source directly.                                     |
|   2 | The `py_compile` module can generate `.pyc` files, which are stored in the `__pycache__` directory.                                                       |
|   3 | Python bytecode specifications change frequently, with approximately 10% of opcodes modified or removed in recent versions.                               |
|   4 | Python 3.11 introduced significant changes by replacing the block stack with an exception table for handling exceptions.                                  |
|   5 | A code object hierarchy is formed during compilation, where the main script and each function or class become separate code objects.                      |
|   6 | The Python interpreter operates as a stack machine, using a value stack to manage data during bytecode execution.                                         |
|   7 | Decompiling bytecode by hand involves three main steps: segmentation, statement translation, and control flow reconstruction.                             |
|   8 | Segmentation identifies statement boundaries, often using the line number table, though this can be unreliable or removed.                                |
|   9 | Statement translation involves simulating the interpreter's logic to convert individual bytecode instructions into source code statements.                |
|  10 | Control flow reconstruction uses a control flow graph to identify and condense primitive structures like loops, conditionals, and try-except blocks.      |
|  11 | Function calls are generally omitted from control flow analysis because they either return, raise exceptions, or terminate the program.                   |
|  12 | Uncomp6 is a popular decompiler that uses version-specific parsers but suffers from high maintenance costs and reduced accuracy in newer Python versions. |
|  13 | Bilingual is a neural decompiler that uses Transformer models to learn bytecode semantics for segmentation and translation tasks.                         |
|  14 | Decompilation accuracy is verified by recompiling the generated source code and comparing the resulting bytecode to the original.                         |
|  15 | The magic number at the start of a `.pyc` file indicates the Python version used for compilation.                                                         |
|  16 | Transformer models in Bilingual are trained on data-driven samples to learn bytecode behavior rather than relying solely on documentation.                |
|  17 | Manual decompilation skills allow users to identify and fix errors in automatic decompiler outputs by analyzing specific bytecode instructions.           |
|  18 | The `dis` module is recommended for inspecting bytecode and understanding how the compiler generates code patterns.                                       |
|  19 | Cross-version disassemblers like Xdis help maintain compatibility across different Python versions.                                                       |
|  20 | The maintenance burden of tracking Python updates is a major challenge for traditional decompilers.                                                       |
|  21 | Bilingual's control flow reconstruction is performed mechanically, while its semantic understanding is learned via machine learning.                      |
|  22 | The decompilation process can be applied to each code object independently before stitching them back together into a full source file.                   |
|  23 | Verification of decompilation results assumes the use of a standard CPython compiler without additional obfuscation.                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rZ_YAm9ywuo/hqdefault.jpg)](https://www.youtube.com/watch?v=rZ_YAm9ywuo)

[Watch on YouTube](https://www.youtube.com/watch?v=rZ_YAm9ywuo)
