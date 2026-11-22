---
layout: default
title: "Talks - Jeff Glass: Making Your Documentation Interactive with PyScript"
nav_order: 197
parent: PyCon US 2024
type: Video Note
description: "Jeff Glass, a PyScript maintainer, presents a solution to the common problem of static documentation by introducing interactive code cells that run directly in the user's browser."
resource: "https://www.youtube.com/watch?v=TZ0JuRLL0IA"
youtube_stats:
  view_count: 1021
  like_count: 26
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

Jeff Glass, a PyScript maintainer, presents a solution to the common problem of static documentation by introducing interactive code cells that run directly in the user's browser.
He explains that PyScript enables the execution of the actual CPython interpreter client-side using WebAssembly, allowing users to test code snippets without installing packages or setting up virtual environments.
The talk details key concepts such as shared environments for state management, configuration files for loading packages and data, and setup tags for pre-running hidden code to simplify user-facing examples.
Glass demonstrates how to integrate these features into popular documentation builders like Sphinx and MkDocs, highlighting the ease of deployment to static hosts like GitHub Pages.
Finally, he outlines the capabilities and limitations of running Python in the browser, noting that while most standard libraries and scientific stacks work seamlessly, native OS interactions and certain threading models require workarounds or are unavailable.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | PyScript enables running Python code directly in the user's browser within HTML documentation, eliminating the need for local installations or virtual environments.           |
|   2 | The tool uses the Pyodide runtime to compile CPython to WebAssembly, ensuring the actual CPython interpreter runs client-side while keeping data local.                        |
|   3 | PyScript also supports MicroPython for faster execution of slimmed-down Python code, though it lacks compatibility with C-API packages like NumPy.                             |
|   4 | The pi-editor component creates interactive code cells similar to Jupyter notebooks that execute code in worker threads to prevent blocking the browser's main thread.         |
|   5 | Environments in PyScript represent separate copies of the Python interpreter, allowing developers to isolate state or share variables between cells using shared environments. |
|   6 | Configuration files in TOML or JSON format allow the installation of Python packages from PyPI, the Pyodide repository, or direct wheel file URLs.                             |
|   7 | The files configuration key loads external data into a virtual in-memory file system within the browser, enabling libraries like Pandas to read local or remote data sources.  |
|   8 | Setup tags allow developers to pre-run hidden code for imports and object initialization, keeping the visible code cell concise for the user.                                  |
|   9 | Integration with Sphinx is achieved via the sphinx-pyscript extension, which adds directives to convert code blocks into interactive editor cells.                             |
|  10 | The MkDocs integration uses the mkdocs-pyscript plugin to transform Markdown code blocks into interactive cells, with a selective option to opt in specific blocks.            |
|  11 | Deployment to static hosts like GitHub Pages or Read the Docs works seamlessly with the provided plugins, which handle necessary web configurations automatically.             |
|  12 | Raw HTML implementations require manual handling of SharedArrayBuffer security headers, such as Cross-Origin Isolation, to enable worker thread communication.                 |
|  13 | Most of the Python standard library and scientific stack, including NumPy, SciPy, and Pandas, function correctly in the browser environment.                                   |
|  14 | Threading and multiprocessing libraries are limited or unavailable, and native GUI frameworks like Tkinter or Curses do not work natively in the browser.                      |
|  15 | Networking capabilities are restricted, preventing the creation of local servers, though service workers can simulate server-side frameworks like FastAPI or Django.           |
|  16 | PyScript supports reactive frameworks like LTK and Starfire for building widget-based interfaces in Python within the browser.                                                 |
|  17 | An interactive Python terminal can be spawned for users to experiment with code directly on the documentation site.                                                            |
|  18 | The project is maintained by a team including Jeff Glass, and resources are available at jeff.glass and the PyScript documentation.                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TZ0JuRLL0IA/hqdefault.jpg)](https://www.youtube.com/watch?v=TZ0JuRLL0IA)

[Watch on YouTube](https://www.youtube.com/watch?v=TZ0JuRLL0IA)
