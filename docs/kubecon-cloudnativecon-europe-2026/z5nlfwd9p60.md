---
layout: default
title:
  "Project Lightning Talk: Container2Wasm: Running Containers On Wasm Environments
  - Kohei Tokunaga"
nav_order: 257
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Koh Tokunaga from NT Inc. presented recent updates on the Container to
  Wasum (C2W) project, a CNCF sandbox tool that enables running Linux-based containers
  in WASM environments, including WASM runtimes and browsers, using WASM-compiled
  CPU...
resource: https://www.youtube.com/watch?v=z5NlfWd9p60
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Koh Tokunaga from NT Inc.
presented recent updates on the Container to Wasum (C2W) project, a CNCF sandbox tool that enables running Linux-based containers in Wasm environments, including Wasm runtimes and browsers, using WASM-compiled CPU emulators.
A significant improvement is the integration of a QEMU-based JIT compilation backend, which has tripled emulation performance for tasks like gzip compression compared to interpreter-based backends.
The project is also exploring use cases such as running LLM agents fully inside browsers, demonstrated with an experimental Visual Studio Code extension that allows LLMs to create, modify, and test code within Linux containers in-browser, without host execution.
This extension supports features like workspace file access, shell command execution, and distributed inference via WebRTC.
Attendees interested in further details about C2W’s QEMU integration and browser-based LLM agents are invited to visit their booth.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Koh Tokunaga from NT Inc. is a founding maintainer of container2wasm.                                                                                                   |
|   2 | Container2wasm is a CNCF sandbox project since January 2025.                                                                                                            |
|   3 | The tool runs Linux-based containers in Wasm environments, including Wasm runtimes and browsers, using WASM-compiled CPU emulators.                                     |
|   4 | The C2W command converts containers to Wasm blobs, which can be run on Wasm runtimes or inside browsers.                                                                |
|   5 | Recent update: Improved emulation performance by adding a QEMU-based JIT compilation backend for Wasm.                                                                  |
|   6 | The QEMU JIT backend speeds up tasks (e.g., gzip compression) about three times faster than the interpreter backend.                                                    |
|   7 | QEMU community discussions are ongoing for Wasm support; version 10.1 added Wasm compilation support with its interpreter backend, and JIT support is under discussion. |
|   8 | Exploring use case: Running LLM agents fully inside browsers, specifically with Visual Studio Code LLMlet.                                                              |
|   9 | Visual Studio Code LLMlet is an experimental extension for browser-based Visual Studio Code, running LLMs on Wasm or WebGPU inside the browser using llama.cpp.         |
|  10 | The LLM has access to the workspace, allowing it to write files and code.                                                                                               |
|  11 | The extension supports running Linux-based containers inside the browser, enabling the model to run shell commands for code testing.                                    |
|  12 | Supports WebRTC-based distributed inference across browsers.                                                                                                            |
|  13 | Demo: Ran Visual Studio Code for the web with LLMlet, using QN 3.54B.                                                                                                   |
|  14 | In the demo, the model created and tested a mini uname command, accessing the file system and terminal to compile and run code without manual intervention.             |
|  15 | All testing was executed in the container running fully inside the browser using a CPU emulator; no commands were executed on the host.                                 |
|  16 | Invitation to visit the kiosk on Tuesday and Thursday for more information about container2wasm, QEMU integration, and LLM agent in the browser.                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=z5NlfWd9p60)
