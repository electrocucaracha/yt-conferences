---
layout: default
title: "Talks - Tian Gao: What makes a Python debugger possible and how can we make it 100x faster"
nav_order: 165
parent: PyCon US 2024
type: Video Note
description: "Tian Ga explains that Python debuggers like `pdb` rely on the `sys.settrace` mechanism to intercept execution events, such as line and call events, allowing users to inspect local variables, call s..."
resource: "https://www.youtube.com/watch?v=3UbVs18SBzo"
youtube_stats:
  view_count: 474
  like_count: 14
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

Tian Ga explains that Python debuggers like `pdb` rely on the `sys.settrace` mechanism to intercept execution events, such as line and call events, allowing users to inspect local variables, call stacks, and execute dynamic code.
However, this approach suffers from significant performance overhead because `sys.settrace` operates globally, forcing the interpreter to trigger events for every single line and function call, even those irrelevant to the user's breakpoint, resulting in a slowdown of approximately 100x.
To address this, the presentation introduces `sys.monitoring`, a newer, lower-cost mechanism that allows for fine-grained, local control over which specific events are fired, enabling debuggers to disable unnecessary events and achieve near-zero overhead.
While `sys.monitoring` offers substantial speed improvements and is already being adopted by tools like PyCharm and coverage.py, it has not yet replaced `pdb` due to challenges involving increased code complexity and backward compatibility issues with the existing `bdb` interface.

# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | A Python debugger requires the ability to stop execution at arbitrary positions, examine local variables and call stacks, execute dynamic code, and control execution flow.                       |
|   2 | The presentation focuses on in-process debuggers, such as pdb, which run within the same process as the target program.                                                                           |
|   3 | The core mechanism enabling Python debuggers is sys.settrace, which allows setting a callback function to trigger on specific events like calls, returns, line executions, and exceptions.        |
|   4 | Sys.settrace operates globally, meaning it is impossible to selectively enable or disable events for specific functions without affecting the entire program.                                     |
|   5 | The finest granularity available with sys.settrace is the function level, where all events within a function must be either fully enabled or fully disabled.                                      |
|   6 | Pdb.set_trace is a standard library function that manually sets the trace function on the current frame and all frames above it to initiate debugging.                                            |
|   7 | Information examination in Python debuggers relies on frame objects provided by CPython, which contain local variables, line numbers, and code object details without requiring additional magic. |
|   8 | Code execution within a debugger, such as evaluating expressions, utilizes built-in functions like eval and exec to convert strings into executable code.                                         |
|   9 | Execution control commands like step, next, and return are implemented by pdb deciding whether to stop or continue based on line events triggered before each line executes.                      |
|  10 | Using sys.settrace causes significant performance overhead, with benchmarks showing approximately a 100x slowdown when debugging recursive functions like Fibonacci.                              |
|  11 | The primary cause of this overhead is the triggering of irrelevant call and line events for functions and loops that do not contain the target breakpoint.                                        |
|  12 | Sys.monitoring is a new low-cost monitoring system that allows events to be set locally on specific code objects rather than globally.                                                            |
|  13 | Unlike sys.settrace, sys.monitoring enables selective activation of any subset of events and allows disabling events on arbitrary lines after they have fired.                                    |
|  14 | This selective event handling allows debuggers to achieve near-zero overhead by only firing events when necessary, potentially resulting in a 100x speed improvement.                             |
|  15 | Adopting sys.monitoring introduces challenges, including increased code complexity and backward compatibility issues with the existing bdb interface used by pdb.                                 |
|  16 | While not yet integrated into the official pdb, tools like PyCharm, Visual Studio Code, and coverage.py are already experimenting with sys.monitoring to improve performance.                     |
|  17 | The new mechanism does not reduce the granularity of debugging features; users can still step into functions and inspect variables with the same precision as before.                             |
|  18 | Sys.monitoring has potential applications beyond debugging, such as improving the efficiency of code coverage tools and production monitoring.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3UbVs18SBzo/hqdefault.jpg)](https://www.youtube.com/watch?v=3UbVs18SBzo)

[Watch on YouTube](https://www.youtube.com/watch?v=3UbVs18SBzo)
