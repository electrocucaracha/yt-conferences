---
layout: default
title: "Tutorials - Yan Yanchii: Pointers in Python"
nav_order: 22
parent: PyCon US 2024
type: Video Note
description: "In this tutorial, software engineer Yan from K.com guides the audience through implementing pointer-like syntax and functionality within the CPython source code."
resource: "https://www.youtube.com/watch?v=YepFiwhK3d8"
youtube_stats:
  view_count: 2147
  like_count: 22
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

In this tutorial, software engineer Yan from K.com guides the audience through implementing pointer-like syntax and functionality within the CPython source code.
The session begins with an introduction to CPython as the reference implementation of Python, distinguishing it from other implementations like PyPy and explaining the compilation pipeline, which includes tokenization, parsing into an Abstract Syntax Tree (AST), optimization, and bytecode generation.
Participants clone the CPython repository, compile it from source, and apply a series of patches to introduce new tokens (`%` for address-of and `$` for dereference) and corresponding AST nodes.
The tutorial covers the necessary modifications to the tokenizer, parser, and compiler to support these new operations, culminating in the creation of a custom `PyPointerObject` that integrates with Python’s memory management system.
To ensure stability, the implementation addresses critical issues such as reference counting cycles and stack overflows by adding support for the tracing garbage collector and utilizing CPython’s "trash can" mechanism.
Finally, the tutorial demonstrates the practical application of these pointers by allowing users to inspect and manipulate raw memory bytes, including swapping list contents and modifying immutable strings, thereby illustrating the low-level mechanics of Python’s object system and memory layout.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The tutorial covers implementing pointer-like syntax in CPython 3.9 by modifying the source code.                                             |
|   2 | CPython is the reference implementation of Python, distinct from Cython, Jython, or PyPy.                                                     |
|   3 | Python uses a compilation pipeline involving tokenization, parsing into an Abstract Syntax Tree (AST), optimization, and bytecode generation. |
|   4 | The distinction between compiled and interpreted languages is reframed as native versus virtual machine execution.                            |
|   5 | New syntax tokens for address-of and dereference operations are added to the grammar and tokenizer.                                           |
|   6 | The AST optimizer is patched to handle new unary operators to prevent segmentation faults during constant folding.                            |
|   7 | New opcodes are defined in the opcode table and handled in the virtual machine's execution loop.                                              |
|   8 | A new built-in pointer object is created with specific type definitions and memory management logic.                                          |
|   9 | Reference counting is used for memory management, requiring manual increment and decrement of object references.                              |
|  10 | Garbage collection support is added to the pointer object to handle cyclic references that reference counting cannot resolve.                 |
|  11 | The trash can mechanism is implemented to prevent stack overflow during the deallocation of deeply nested pointer chains.                     |
|  12 | Methods are added to the pointer object to read and write raw bytes of the referenced object in memory.                                       |
|  13 | The implementation allows inspecting object memory layouts, such as reference counts and type pointers.                                       |
|  14 | Users can swap data between objects by directly manipulating their underlying memory bytes.                                                   |
|  15 | The tutorial demonstrates modifying immutable strings by writing directly to their memory addresses.                                          |
|  16 | All changes are applied via patches to the CPython repository and require recompilation to take effect.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YepFiwhK3d8/hqdefault.jpg)](https://www.youtube.com/watch?v=YepFiwhK3d8)

[Watch on YouTube](https://www.youtube.com/watch?v=YepFiwhK3d8)
