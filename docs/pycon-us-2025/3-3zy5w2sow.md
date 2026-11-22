---
layout: default
title: 'Marimo: A Notebook that "Compiles" Python for Reproducibility and Reusability - Akshay Agrawal'
nav_order: 58
parent: PyCon US 2025
type: Video Note
description: "MIMO is an open-source Python notebook that addresses the reproducibility and maintainability issues of traditional Jupyter notebooks by representing code as a data flow graph."
resource: "https://www.youtube.com/watch?v=3-3zy5W2SOw"
youtube_stats:
  view_count: 3774
  like_count: 122
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

MIMO is an open-source Python notebook that addresses the reproducibility and maintainability issues of traditional Jupyter notebooks by representing code as a data flow graph.
Unlike standard notebooks, MIMO files are pure Python scripts that ensure code and outputs remain synchronized through reactive execution, where changing a variable automatically updates dependent cells.
This architecture allows MIMO notebooks to be reused in three distinct ways: as interactive computational notebooks, as standard Python scripts, or as deployable web applications without code modifications.
The system relies on static analysis of variable definitions and references rather than runtime tracing, which enforces constraints such as prohibiting variable redefinition and cycles to guarantee a clear dependency structure.
By leveraging Python’s AST module for parsing and semantic analysis, MIMO provides a maintainable, version-control-friendly environment that is agnostic to data types and supports features like module hot-reloading and self-contained dependency management.

# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MIMO is an open-source Python notebook that compiles code for reproducibility and reusability without Jupyter dependencies.                 |
|   2 | Notebooks are stored as maintainable Python files with reproducible execution semantics where code and outputs remain in sync.              |
|   3 | MIMO notebooks can be reused as computational notebooks, Python scripts, or interactive web apps without code changes.                      |
|   4 | The system uses a reactive model where changing a variable automatically reruns dependent cells to prevent hidden state issues.             |
|   5 | A 2019 study found that only 4% of Jupyter notebooks on GitHub reproduced their serialized outputs due to code-output desynchronization.    |
|   6 | Traditional notebooks stored as JSON files create large Git diffs and are difficult to reuse compared to pure Python files.                 |
|   7 | MIMO represents notebooks as data flow graphs where edges indicate variable dependencies between cells.                                     |
|   8 | The data flow graph is constructed statically by analyzing variable definitions and references without runtime tracing.                     |
|   9 | Mutations of objects like lists are not tracked, ensuring the dependency structure remains simple and predictable for users.                |
|  10 | The graph must be a directed acyclic graph, prohibiting cycles, variable redefinition across cells, and deletion of other cells' variables. |
|  11 | Violating these constraints results in polite error messages, encouraging users to write cleaner, more modular code.                        |
|  12 | Parsing is implemented using Python's built-in ast module to convert code into abstract syntax trees.                                       |
|  13 | Semantic analysis resolves variable scopes using a stack of symbol tables to distinguish local and global variables.                        |
|  14 | The implementation is written in Python rather than Rust, utilizing specialized visitors for AST node traversal.                            |
|  15 | The reactive runtime uses the graph to keep outputs in sync, prune state, and handle control flow like mode.stop.                           |
|  16 | Interactive UI elements trigger reactive execution by sending IDs to the backend, which then runs dependent cells.                          |
|  17 | MIMO supports embedding other languages like SQL and Markdown through specialized library functions and parsers.                            |
|  18 | Module hot reloading uses the graph to identify and rerun only the cells affected by changes in imported modules.                           |
|  19 | Jupyter notebooks can be automatically converted to MIMO notebooks by fixing multiple definition errors.                                    |
|  20 | A caching system keys on source code and reference values to enable persistent local or remote caching.                                     |
|  21 | Functions defined in notebooks can be imported directly into other Python modules if they are pure.                                         |
|  22 | MIMO was inspired by Pluto.jl, Observable, Jupyter, and the concept of spreadsheets as reactive tools.                                      |
|  23 | The project was funded by Stanford's SLAC National Accelerator Laboratory for two years.                                                    |
|  24 | MIMO is used by various companies and universities for data science, machine learning, and presentations.                                   |
|  25 | The presentation itself is a live demo of a MIMO notebook, showcasing its capability for creating interactive slides.                       |
|  26 | Dependency management can be serialized in the notebook file to create self-contained environments.                                         |
|  27 | MIMO can replace Streamlit dashboards by rerunning only necessary code rather than the entire script.                                       |
|  28 | The system is agnostic to data types and works with GPU tensors by analyzing source code only.                                              |
|  29 | Self-hosting is supported via SSH port tunneling and authentication tokens, with compatibility for Jupyter Hub.                             |
|  30 | Complex control flow and heavy mutation of state are not fully supported, encouraging functional programming styles.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3-3zy5W2SOw/hqdefault.jpg)](https://www.youtube.com/watch?v=3-3zy5W2SOw)

[Watch on YouTube](https://www.youtube.com/watch?v=3-3zy5W2SOw)
