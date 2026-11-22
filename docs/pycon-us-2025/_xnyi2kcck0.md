---
layout: default
title: "Writing Extension Modules To Be Interruptible - Zack Weinberg"
nav_order: 19
parent: PyCon US 2025
type: Video Note
description: "Zach Weinberg explains why Python extension modules often fail to respond promptly to Ctrl+C interrupts, a common issue caused by the failure to call the `PyErr_CheckSignals` C API function within ..."
resource: "https://www.youtube.com/watch?v=_XnYI2Kcck0"
youtube_stats:
  view_count: 746
  like_count: 17
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

Zach Weinberg explains why Python extension modules often fail to respond promptly to Ctrl+C interrupts, a common issue caused by the failure to call the `PyErr_CheckSignals` C API function within long-running compiled code.
The talk details how CPython’s signal handling mechanism relies on setting a flag that is only checked in the main interpreter loop, meaning extensions must explicitly check for signals to allow the interpreter to raise a `KeyboardInterrupt` safely.
Weinberg highlights that this requirement is poorly documented and technically challenging, as calling the check function may execute arbitrary Python code, necessitating careful management of the Global Interpreter Lock (GIL) and error propagation.
To mitigate the performance overhead of frequent signal checks, he proposes using time-based throttling and provides a reusable code snippet for developers to implement efficient interruptibility.
Finally, he outlines potential future improvements, including better documentation, modifying the C API to reduce lock contention, and exploring compiler or tooling support to automate these necessary checks.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | CPython extension modules must manually call PyErr_CheckSignals to remain responsive to user interrupts like Control-C.                                                                    |
|   2 | Many extensions, including NumPy, fail to call this function, causing significant delays when users attempt to interrupt long-running calculations.                                        |
|   3 | The delay occurs because the C-level signal handler only sets a flag; the actual KeyboardInterrupt is raised only when the interpreter loop checks this flag.                              |
|   4 | Compiled code extensions bypass the main interpreter loop, so they must explicitly check for signals to allow the interpreter to react to interrupts.                                      |
|   5 | The requirement to call PyErr_CheckSignals is poorly documented, appearing only in a dense section of the C API reference manual rather than the extending guide.                          |
|   6 | Calling PyErr_CheckSignals can execute arbitrary Python code, requiring the Global Interpreter Lock (GIL) to be held, which complicates code that releases the GIL for performance.        |
|   7 | Integrating signal checks into tight inner loops introduces substantial runtime overhead, particularly when the GIL must be reacquired for each check.                                     |
|   8 | Benchmarking shows that releasing the GIL to perform signal checks can make operations three to four times slower compared to holding the GIL throughout.                                  |
|   9 | A more efficient approach involves checking a monotonic clock and only calling PyErr_CheckSignals if a minimum time interval, such as one millisecond, has elapsed.                        |
|  10 | Using a coarse clock source further reduces the overhead of signal checking to a level comparable to the baseline cost of adding the checks.                                               |
|  11 | Short-term recommendations include using a provided helper function that handles GIL management and clock-based throttling for signal checks.                                              |
|  12 | Long-term improvements include updating documentation to clearly state the requirement and modifying PyErr_CheckSignals to acquire the GIL only when necessary.                            |
|  13 | Tooling enhancements could involve having compilers like Cython automatically insert signal checks and handle error propagation in generated C code.                                       |
|  14 | Alternative approaches include mapping Control-C to asynchronous cancellation in FFI libraries like PyO3 for Rust extensions.                                                              |
|  15 | A radical proposal suggests restructuring the CPython virtual machine to use subprocesses, allowing the kernel to handle signal termination without requiring manual checks in extensions. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_XnYI2Kcck0/hqdefault.jpg)](https://www.youtube.com/watch?v=_XnYI2Kcck0)

[Watch on YouTube](https://www.youtube.com/watch?v=_XnYI2Kcck0)
