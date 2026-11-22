---
layout: default
title: "Talks - Irit Katriel: CPython's Compilation Pipeline"
nav_order: 171
parent: PyCon US 2024
type: Video Note
description: "Marit Catriel, a Python core developer at Microsoft, presents a refactoring of the CPython compiler pipeline in Python 3.13 that exposes new intermediate stages to Python."
resource: "https://www.youtube.com/watch?v=DfXhywRVgN4"
youtube_stats:
  view_count: 505
  like_count: 15
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

Marit Catriel, a Python core developer at Microsoft, presents a refactoring of the CPython compiler pipeline in Python 3.13 that exposes new intermediate stages to Python.
The primary motivation for this work was to enable effective unit testing of specific compiler components, such as the peephole optimizer, which was previously difficult to test in isolation due to tight coupling and complex data structures.
The new pipeline breaks down the process from an Abstract Syntax Tree (AST) to a code object into distinct steps: AST optimization, code generation into pseudo-instructions, optimization of those instructions, and finally assembly into bytecode.
This modular approach allows developers to test individual stages with precise input and expected output, significantly improving code maintainability and accessibility.
Although these new functions are currently available only in the internal test module, the refactoring paves the way for potential future standard library exposure and greater flexibility for custom compiler implementations.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Marit Catriel, a Python core developer at Microsoft, presented the refactored CPython compiler pipeline in Python 3.13.                                           |
|   2 | The new pipeline exposes intermediate stages to Python, specifically AST optimization, code generation, and instruction sequence optimization.                    |
|   3 | The primary motivation for the refactor was to enable unit testing of the peephole optimizer and other compiler stages.                                           |
|   4 | A secondary motivation was to improve code maintainability by decoupling stages that previously shared complex data structures.                                   |
|   5 | The compilation process now proceeds from source to tokens, AST, optimized AST, pseudo-instructions, optimized pseudo-instructions, and finally bytecode.         |
|   6 | AST optimization simplifies constant expressions, such as calculating 1 + 2 to 3 before code generation.                                                          |
|   7 | Code generation converts the AST into pseudo-instructions, which are similar to bytecode but use logical labels for jumps.                                        |
|   8 | The peephole optimizer refines the pseudo-instruction sequence, such as eliminating redundant jump-to-jump patterns.                                              |
|   9 | The assembler translates optimized pseudo-instructions into actual bytecode, resolving logical labels into relative offsets.                                      |
|  10 | Bytecode requires specific jump directions, so conditional backward jumps are translated into forward conditional jumps followed by unconditional backward jumps. |
|  11 | These new stages are currently accessible via the underscore_test_internal_capi module, which is not part of the official standard library.                       |
|  12 | Exposing these stages officially would require a PEP and discussion on stability guarantees and use cases.                                                        |
|  13 | Previous testing methods relied on disassembling final bytecode, which could not verify if specific optimizations were actually applied.                          |
|  14 | The new testing approach allows developers to run individual stages, such as the optimizer, and assert on the specific pseudo-instruction output.                 |
|  15 | Unit tests for the new pipeline are written in Python using the internal C API hooks.                                                                             |
|  16 | There is no formal catalog of implemented optimizations; developers must read the source code to identify them.                                                   |
|  17 | A GUI tool was created to visualize the compilation stages, though the presenter hopes the community will take over its maintenance.                              |
|  18 | The refactor supports potential future flexibility, such as allowing alternative compilers to hook into specific stages of the CPython pipeline.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/DfXhywRVgN4/hqdefault.jpg)](https://www.youtube.com/watch?v=DfXhywRVgN4)

[Watch on YouTube](https://www.youtube.com/watch?v=DfXhywRVgN4)
