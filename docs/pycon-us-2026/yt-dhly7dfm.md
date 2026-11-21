---
layout: default
title: "How to port a Python kernel to Pyodide for a blazingly fast in-browser coding... - Myles Scolnick"
nav_order: 32
parent: PyCon US 2026
type: Video Note
description: "Miles Skulnik, a creator of the open-source reactive notebook Marimo, presented a technical talk at PyCon detailing how the platform was migrated to run entirely in the browser using Pyodide and We..."
resource: "https://www.youtube.com/watch?v=Yt-DhlY7dFM"
youtube_stats:
  view_count: 525
  like_count: 5
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

Miles Skulnik, a creator of the open-source reactive notebook Marimo, presented a technical talk at PyCon detailing how the platform was migrated to run entirely in the browser using Pyodide and WebAssembly.
This architecture eliminates the need for a backend server, offering significant benefits in accessibility, reduced latency, cost efficiency, and security through WebAssembly’s isolation.
To achieve this, the team refactored Marimo’s kernel to replace native processes and threads with an asynchronous event loop, utilizing web workers and `window.postMessage` for communication between the UI and the Python runtime.
Key engineering challenges included implementing cell interruption via shared memory buffers, adapting HTTP requests and package management to browser constraints, and ensuring compatibility with C extensions by compiling them to WebAssembly.
The presentation concluded with performance optimization strategies, such as custom Pyodide builds and background dependency loading, while noting limitations like memory caps and the requirement for pure Python or WebAssembly-compiled dependencies.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Marimo is an open-source reactive Python notebook that runs entirely in the browser using Pyodide, eliminating the need for a server. |
|   2 | Running Python in the browser offers accessibility, lower costs, reduced latency, and enhanced security through WebAssembly isolation. |
|   3 | Pyodide compiles CPython to WebAssembly using Emscripten, allowing scientific Python to run in web environments. |
|   4 | Marimo refactored its codebase to support both native CPython and Pyodide runtimes, sharing the same kernel, parser, and reactive engine. |
|   5 | The migration required replacing processes and threads with an asynchronous event loop, as Pyodide does not support multiprocessing. |
|   6 | Marimo implemented shared protocols for streams, queues, and sessions to abstract differences between native and browser runtimes. |
|   7 | Top-level await support was added to facilitate package installation via micropip within notebook cells. |
|   8 | Interrupts are handled in Pyodide by using a shared array buffer to flip a bit, which triggers a keyboard interrupt between byte operations. |
|   9 | HTTP requests and package downloads were adapted to work within browser constraints by converting networking logic to async and using HTTP instead of sockets. |
|  10 | Marimo uses patches for libraries like Polars and DuckDB to ensure compatibility with WebAssembly environments. |
|  11 | Performance optimizations include trimming wheel sizes, serving custom lock files, and revealing the editor before the kernel is fully ready. |
|  12 | Dependencies are loaded in the background by scraping cell imports or PEP 723 metadata to improve startup speed. |
|  13 | Multiple web workers are used to allow background tasks like auto-saving while cells are executing. |
|  14 | Feature detection at boundaries is recommended to avoid sprinkling conditionals throughout the codebase. |
|  15 | Composition over inheritance is preferred, using parallel classes and shared protocols for cleaner architecture. |
|  16 | Async primitives are favored for compatibility across runtimes, with multiprocessing added only when necessary. |
|  17 | OS-specific concerns like threads, signals, and file systems are abstracted away to ensure portability. |
|  18 | Pyodide has a memory limit of approximately 2 GB due to Emscripten constraints. |
|  19 | Packages must be pure Python or compiled to WebAssembly to run in Pyodide. |
|  20 | Threading is not supported in Pyodide, but concurrency can be achieved using asyncio. |
|  21 | Users can test package compatibility by installing them directly in the Marimo playground. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Yt-DhlY7dFM/hqdefault.jpg)](https://www.youtube.com/watch?v=Yt-DhlY7dFM)

[Watch on YouTube](https://www.youtube.com/watch?v=Yt-DhlY7dFM)
