---
layout: default
title: "From Desktop to Browser: Crafting Browser-Native Game Engine with Webassembly - Neeraj Pandey"
nav_order: 86
parent: PyCon US 2025
type: Video Note
description: "Niraj Pande’s presentation explores how to create browser-native game engines using WebAssembly, enabling high-performance Python games to run in web environments."
resource: "https://www.youtube.com/watch?v=-BAEnYpsWKc"
youtube_stats:
  view_count: 651
  like_count: 9
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

Niraj Pande’s presentation explores how to create browser-native game engines using WebAssembly, enabling high-performance Python games to run in web environments.
The talk explains that WebAssembly acts as a portable binary format that executes at near-native speed within a secure sandbox, complementing JavaScript to handle computational-intensive tasks like 3D simulations and complex graphics.
To facilitate this, the speaker introduces Pyodide, a CPython interpreter compiled to WebAssembly that allows scientific libraries like NumPy to run directly in the browser, and Pigback, a package manager that bridges Pygame desktop applications to the web by compiling code and managing assets.
The session details the technical adaptations required for this transition, such as converting synchronous game loops into asynchronous functions, using `flip` instead of `update` for efficient rendering, and implementing non-blocking event handling to maintain responsiveness in the single-threaded browser environment.
Finally, the presentation demonstrates the practical application of these concepts by building a simple snake game in Pygame and successfully deploying it to the browser using Pigback, showcasing the seamless integration of Python game development with web technologies.

# Main Points

|   # | Main point                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | WebAssembly is a binary instruction format for a stack-based virtual machine that enables high-performance web applications by translating code from languages like Python, C, and Rust into a compact binary format.        |
|   2 | WebAssembly works in sync with JavaScript to provide interoperability with web APIs, allowing computational-intensive tasks like video games and 3D engines to run in the browser at near-native speeds.                     |
|   3 | The Python execution flow involves compiling source code into bytecode, which is then executed by the Python Virtual Machine, while WebAssembly compiles source code into Wasm bytecode stored in a Wasm module.             |
|   4 | WebAssembly execution occurs in a sandbox environment with linear memory allocation, ensuring security by limiting direct access to system resources and preventing direct interaction with external modules.                |
|   5 | Performance benchmarks for a particle simulation showed that WebAssembly reduced average frame time by half, doubled particle update speed, and decreased CPU usage from 95% to 45% compared to the desktop Python version.  |
|   6 | Key benefits of WebAssembly include high performance, portability across browsers, enhanced security through sandboxing, and seamless integration with existing JavaScript and web APIs.                                     |
|   7 | Pyodide is a port of the CPython interpreter that enables Python to run directly in web browsers without a server, supporting scientific libraries like NumPy and Pandas at near-native speeds.                              |
|   8 | Pyodide operates by compiling CPython to WebAssembly, allowing JavaScript to interact with the Python interpreter, load pre-compiled packages on demand, and execute code with results accessible via web APIs.              |
|   9 | The syntax for using Pyodide involves asynchronous loading of the library, executing Python code via runPython, loading packages like NumPy, and interacting with the DOM by setting global variables.                       |
|  10 | Pygame is a widely used Python library for 2D game development that acts as a wrapper for the SDL library, providing access to low-level audio, keyboard, mouse, and graphics hardware.                                      |
|  11 | Core Pygame features include graphics rendering, sound handling, input manipulation, and the game loop, which processes user input, updates game state, and ensures the application does not hang.                           |
|  12 | In Pygame, the difference between flip and update is that flip swaps the entire screen buffer to prevent flickering, while update allows for partial screen changes without clearing the previous state.                     |
|  13 | Blitting in Pygame refers to block transfer, where images or shapes are drawn onto a surface while preserving the existing state, unlike flipping which replaces the entire buffer.                                          |
|  14 | Collision detection in Pygame uses rectangular or circular strategies to identify when game objects intersect, triggering specific game logic such as score increments or game over states.                                  |
|  15 | Pigback is a package manager that bridges Python game development and the web by using a custom CPython build optimized for games and compiling code to WebAssembly via the Onscriptum toolchain.                            |
|  16 | Pigback creates a virtual file system in the browser for asset management and implements an asynchronous event loop to ensure compatibility with the browser's single-threaded, event-driven environment.                    |
|  17 | To adapt Pygame code for Pigback, developers must replace update functions with flip for efficiency, convert the main game loop to asynchronous functions, and use async sleep to yield control and maintain responsiveness. |
|  18 | The conversion process involves Pigback translating Pygame code into WebAssembly, generating static HTML and JavaScript files, and bundling assets to run the game in the browser without a server.                          |
|  19 | A practical example of this workflow is a snake game where the player moves a rectangle, collects food to increase length, and triggers a game over state upon collision with boundaries.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-BAEnYpsWKc/hqdefault.jpg)](https://www.youtube.com/watch?v=-BAEnYpsWKc)

[Watch on YouTube](https://www.youtube.com/watch?v=-BAEnYpsWKc)
