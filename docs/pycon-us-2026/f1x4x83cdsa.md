---
layout: default
title: "Tachyon: Python 3.15's sampling profiler is faster...- Pablo Galindo Salgado, Laszlo Kiss Kollar"
nav_order: 50
parent: PyCon US 2026
type: Video Note
description: "This presentation introduces Takon, a new sampling profiler shipping with Python 3.15, designed to profile applications at full production speed without the significant overhead associated with tra..."
resource: "https://www.youtube.com/watch?v=f1x4X83CDSA"
youtube_stats:
  view_count: 1408
  like_count: 41
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

This presentation introduces Takon, a new sampling profiler shipping with Python 3.15, designed to profile applications at full production speed without the significant overhead associated with traditional tracing profilers like cProfile.
Developed by Pablo Galindo and Lazaro, Takon utilizes system calls to read memory from running processes, employing advanced optimizations such as code object caching, page-level memory copying, and a frame cache mechanism to achieve sampling rates exceeding one million samples per second.
The tool offers multiple capture modes, including running scripts, attaching to live processes, and dumping snapshots, while providing diverse visualization options such as pstats, live terminal views, flame graphs, heat maps, and differential flame graphs for performance analysis.
Additionally, the speakers introduce Kronon, a more advanced commercial profiler that extends these capabilities to include native stack profiling and supports multi-threaded and multi-process environments, with plans to open-source it later in the year.
The session concludes by clarifying that Takon complements existing third-party profilers rather than replacing them, ensuring a robust ecosystem for Python performance monitoring.

# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Takon is a sampling profiler shipping in Python 3.15 that runs externally to keep the target program at full speed.                      |
|   2 | Unlike cProfile, Takon uses process_vm_readv to copy bytes from the target process and reinterprets them statistically.                  |
|   3 | The profiler addresses issues where previous external profilers broke with each Python release due to lack of stable APIs.               |
|   4 | A secret test added in Python 3.12 ensures external inspection capabilities are not broken by interpreter changes.                       |
|   5 | PEP 768 allows external debuggers to attach to the interpreter, providing infrastructure for Takon.                                      |
|   6 | Takon is currently the fastest publicly released Python profiler, achieving sampling rates exceeding one million samples per second.     |
|   7 | Performance optimizations include caching code objects using a generation counter to handle address reuse by lambdas.                    |
|   8 | Memory copying is optimized by reading entire pages instead of individual bytes to amortize kernel locking overhead.                     |
|   9 | Frame copying is reduced by leveraging contiguous memory chunks for frames introduced in Python 3.12.                                    |
|  10 | A frame cache mechanism uses process_vm_writev to track the last profiled frame, allowing zero-copy samples when the stack is unchanged. |
|  11 | The new profiling package in Python 3.15 groups all profilers, including cProfile, under a unified interface.                            |
|  12 | Takon supports capture modes for running scripts, attaching to live processes, dumping snapshots, and replaying data.                    |
|  13 | Default output uses pstats for terminal visualization, compatible with existing CPython profiling tools.                                 |
|  14 | The d-live mode provides a top-like terminal view for real-time debugging of production processes.                                       |
|  15 | Flame graph output is provided as a self-contained HTML file with zoom, search, and dark mode features.                                  |
|  16 | Heat map visualization displays source code with intensity indicators to identify lines needing optimization.                            |
|  17 | Opcode profiling reveals CPython bytecodes and specialized adaptive interpreter instructions in reports.                                 |
|  18 | Differential flame graphs compare performance changes, using color coding to show improvements or regressions.                           |
|  19 | Data can be exported to JSON for use with the Firefox Profiler visualizer, showing GIL and GC states.                                    |
|  20 | Binary mode saves sampling data for efficient replay into various visualization formats without re-running the profile.                  |
|  21 | Kronon is a commercial profiler by HRT that extends Takon's features to profile native frames and core files.                            |
|  22 | Kronon supports streaming mode, Python API control, and asynchronous unwinding for high-speed native profiling.                          |
|  23 | Takon supports asynchronous code by visualizing all running tasks rather than just the event loop.                                       |
|  24 | Multi-threaded and multi-process profiling is supported, with Takon forking itself to handle multiple processes.                         |
|  25 | The profiler uses qualified names to correctly identify decorated functions and methods in reports.                                      |
|  26 | External profilers like Py-Spy remain viable and can adopt Takon's techniques to improve performance and stability.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/f1x4X83CDSA/hqdefault.jpg)](https://www.youtube.com/watch?v=f1x4X83CDSA)

[Watch on YouTube](https://www.youtube.com/watch?v=f1x4X83CDSA)
