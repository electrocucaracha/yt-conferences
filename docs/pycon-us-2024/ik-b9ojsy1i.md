---
layout: default
title: "Sponsor Presentations - Python in Cloudflare Workers – Running Pyodide on the Edge"
nav_order: 35
parent: PyCon US 2024
type: Video Note
description: "At PyCon, Cloudflare engineers Hood Chatham and Garrett introduced Python Workers, a new capability that allows developers to write and deploy web applications in Python across Cloudflare’s global ..."
resource: "https://www.youtube.com/watch?v=ik-B9ojsy1I"
youtube_stats:
  view_count: 1255
  like_count: 27
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

At PyCon, Cloudflare engineers Hood Chatham and Garrett introduced Python Workers, a new capability that allows developers to write and deploy web applications in Python across Cloudflare’s global network.
By leveraging the Pyodide interpreter and WebAssembly, this solution enables serverless applications to run with low latency and infinite scalability, overcoming previous limitations that restricted Workers to JavaScript or WebAssembly.
The presentation detailed key technical optimizations, including a custom in-memory file system for rapid package installation and memory snapshots that significantly reduce cold start times by preserving interpreter state.
Additionally, the speakers discussed future enhancements such as stack switching to bridge synchronous Python APIs with asynchronous runtime operations, improved Foreign Function Interface (FFI) abstractions for a more Pythonic experience, and support for popular frameworks like FastAPI.
A live demo of a pet-voting application showcased the platform’s reliability and speed, while the Q&A session addressed topics like garbage collection, package versioning, and the long-term backward compatibility strategy for Python on the edge.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Python Workers allow developers to write and deploy web applications globally using Cloudflare’s network with low latency and infinite scalability.        |
|   2 | The implementation runs the Pyodide interpreter within the Cloudflare Workers runtime to enable Python support.                                            |
|   3 | Cloudflare’s network spans 310 cities and 120 countries, connecting over 13,000 networks and powering over 20% of global internet traffic.                 |
|   4 | Cloudflare Workers is a serverless platform that isolates applications using V8 isolates rather than processes, improving efficiency and reducing costs.   |
|   5 | A demo application was built using Cloudflare’s D1 serverless database and Workers AI inference platform to validate pet inputs.                           |
|   6 | The demo utilized FastAPI and ASGI to handle API endpoints, simplifying backend development compared to raw JavaScript bindings.                           |
|   7 | Pyodide compiles CPython to WebAssembly using the Emscripten toolchain to run Python in JavaScript runtimes like browsers and Cloudflare Workers.          |
|   8 | WebAssembly is a portable, secure binary instruction format that relies on host imports for system calls, as it lacks standard APIs.                       |
|   9 | Emscripten provides a Unix-like host environment, including a JavaScript-implemented file system and dynamic linking support.                              |
|  10 | Pyodide includes a foreign function interface (FFI) that allows Python code to access JavaScript global scope functions like fetch.                        |
|  11 | Package installation is optimized by pre-processing wheel files into an in-memory format, reducing installation time from 30 seconds to under one second.  |
|  12 | Memory snapshots are used to speed up cold starts by saving the Python interpreter state after initialization, cutting startup time by 80-90%.             |
|  13 | Memory snapshots require careful synchronization of JavaScript and WebAssembly states, including file system and FFI states.                               |
|  14 | Randomness at import time is disabled to ensure memory snapshots work correctly, preventing static random seeds in reused states.                          |
|  15 | Future improvements include abstracting the FFI to make Python code more natural and less dependent on JavaScript syntax.                                  |
|  16 | Stack switching in WebAssembly is being implemented to allow synchronous Python APIs to call asynchronous JavaScript functions.                            |
|  17 | Support for synchronous HTTP libraries like requests and urllib3 is being developed by shimming socket operations to use JavaScript APIs.                  |
|  18 | Server frameworks like Flask, Django, and FastAPI will work by implementing WSGI and ASGI interfaces, abstracting away raw socket handling.                |
|  19 | Cloudflare aims to support Python for five years, aligning with upstream Python end-of-life policies rather than offering infinite backward compatibility. |
|  20 | Users can structure Python workers as standard packages with multiple files, though mixed JavaScript and Python workers are not yet supported.             |
|  21 | Package versioning is managed through periodic bundle releases, allowing security patches to be applied via the runtime without redeployment.              |
|  22 | The project acknowledges contributions from the Pyodide, Emscripten, and Python communities for enabling WebAssembly support.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ik-B9ojsy1I/hqdefault.jpg)](https://www.youtube.com/watch?v=ik-B9ojsy1I)

[Watch on YouTube](https://www.youtube.com/watch?v=ik-B9ojsy1I)
