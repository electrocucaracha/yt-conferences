---
layout: default
title: "From Graveyard to Glory: Production Python in the Browser - Mahmoud Hashemi"
nav_order: 27
parent: PyCon US 2026
type: Video Note
description: "Mahmood, a Python Software Foundation fellow, presents a deep dive into building production-ready Python applications in the browser using Pyodide and WebAssembly."
resource: "https://www.youtube.com/watch?v=YLZ6HrZSBrQ"
youtube_stats:
  view_count: 323
  like_count: 11
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

Mahmood, a Python Software Foundation fellow, presents a deep dive into building production-ready Python applications in the browser using Pyodide and WebAssembly.
He argues that while AI agents can rapidly generate basic prototypes, they often miss critical production requirements such as testing, typed boundaries, telemetry, and robust state management.
The talk highlights the historical evolution of browser-based Python, noting that modern approaches leverage WebAssembly to provide free client-side compute, sandboxing, and access to the vast PyPI ecosystem without sacrificing the performance benefits of best-in-class JavaScript UI frameworks like Svelte.
Mahmood emphasizes that the key to successful agent-assisted development is establishing strong verifiability through tools like Playwright, Comlink, and linters, which allow developers to focus on creative problem-solving while ensuring reliability.
He concludes by advocating for Python in the browser as a viable, "good enough" solution for building responsive, portable applications, noting that the line between prototype and product is blurring as the technology matures and integrates with edge computing.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, a Python Software Foundation fellow, presents a deep dive into building a browser-based Python application using Pyodide.                                  |
|   2 | An AI agent was used to generate a basic regular expression testing app with dark mode, but it missed critical production requirements like tests and state management. |
|   3 | Key reasons for using Python in the browser include free client-side compute, sandboxing for security, and reproducibility of semantics between server and client.      |
|   4 | The Python ecosystem, with nearly one million packages on PyPI, is a major advantage over porting libraries to JavaScript.                                              |
|   5 | Historical attempts like Pyjamas, Silverlight, and PyJS failed due to outdated tech, plugin reliance, or lack of standard library support.                              |
|   6 | Pyodide, created by Mozilla in 2019, compiles CPython to WebAssembly and now supports micro-pip for package installation.                                               |
|   7 | Notable projects built on Pyodide include JupyterLite, Marimo, GradioLite, Streamlit, and PyScript.                                                                     |
|   8 | The agent-generated code lacked tests, a UI framework, typed boundaries, telemetry, and proper worker state management.                                                 |
|   9 | Playwright is recommended for cross-browser testing, and pre-commit hooks help with sanity checks before CI.                                                            |
|  10 | Best-in-class UI frameworks like Svelte or React should handle the interface, while Python handles business logic in Web Workers.                                       |
|  11 | Comlink provides a typed, promise-based interface for communicating with Web Workers, acting as a lightweight abstraction.                                              |
|  12 | Telemetry should be routed through a server tunnel to avoid ad-blockers and ensure error reporting to services like Sentry or PostHog.                                  |
|  13 | Worker state management requires a state machine to handle loading and processing states, avoiding invalid states.                                                      |
|  14 | SharedArrayBuffer enables fast interruption of runaway processes, requiring specific HTTP headers.                                                                      |
|  15 | The future includes CPython Tier 3 WebAssembly support via PEP 816, allowing official wheels on PyPI.                                                                   |
|  16 | Edge computing with Cloudflare Workers offers an alternative to client-side execution for network-bound tasks.                                                          |
|  17 | Verifiability through tests, types, compilers, and linters is essential for effective agent-assisted development.                                                       |
|  18 | Python is described as the "language of good enough," suitable for rapid prototyping and production apps.                                                               |
|  19 | The agent-assisted human is the new unit of production, leveraging agents for code generation while humans provide guardrails.                                          |
|  20 | Pyodide has a limited package index compared to PyPI, requiring careful version pinning to match server-side semantics.                                                 |
|  21 | Micro-pip in Pyodide does not currently support installing from pyproject.toml or Git sources.                                                                          |
|  22 | The speaker advocates for building polished applications around favorite Python libraries using Svelte for UI and Pyodide for logic.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YLZ6HrZSBrQ/hqdefault.jpg)](https://www.youtube.com/watch?v=YLZ6HrZSBrQ)

[Watch on YouTube](https://www.youtube.com/watch?v=YLZ6HrZSBrQ)
