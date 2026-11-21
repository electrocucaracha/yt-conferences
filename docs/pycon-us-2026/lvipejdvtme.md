---
layout: default
title: "Upgrading Python CLIs From Scripts to Interactive Tools - Avik Basu"
nav_order: 36
parent: PyCon US 2026
type: Video Note
description: "The speaker, a staff data scientist at Intuit, presents a comprehensive guide to building effective Command Line Interfaces (CLIs) in Python, emphasizing the transition from verbose standard librar..."
resource: "https://www.youtube.com/watch?v=lVIPEjDVTME"
youtube_stats:
  view_count: 456
  like_count: 7
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

The speaker, a staff data scientist at Intuit, presents a comprehensive guide to building effective Command Line Interfaces (CLIs) in Python, emphasizing the transition from verbose standard libraries like `argparse` to modern, user-friendly frameworks.
The talk highlights the importance of fast, composable, and scriptable CLIs that serve as deterministic contracts for both human users and AI agents, using a custom ML monitoring tool as a running example.
By leveraging Typer for declarative input handling and type-safe validation, and Rich for enhanced visual output including progress bars and styled tables, developers can significantly improve usability and reduce manual validation overhead.
The presentation also explores Textual for creating interactive Terminal User Interfaces (TUIs) suitable for live monitoring, while addressing critical production patterns such as optimizing import times via lazy loading, ensuring cross-platform compatibility through the `platformdirs` package, and implementing a robust configuration hierarchy that prioritizes command-line flags over environment variables and defaults.
Finally, the speaker advises on distribution strategies using tools like `pipx` and recommends JSON output for seamless integration with other command-line tools and automated agents, concluding with a Q&A session that discusses the limitations of TUIs for non-interactive agent workflows and the benefits of Typer’s tight integration with Rich compared to newer alternatives.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is a staff data scientist at Intuit and an editor at BioOpenSci, based in the Bay Area.                                                           |
|   2 | The presentation covers the journey of building Command Line Interfaces (CLIs) in Python, from basic standard libraries to advanced production patterns.      |
|   3 | Great CLIs are fast, composable, scriptable, cross-platform, and define clear contracts for agents using proper help commands and exit codes.                 |
|   4 | The running example is a tool called "shap monitor" for tracking ML model explainability, featuring log, report, and watch commands.                          |
|   5 | Key requirements for a good CLI include distributability, subcommands, type-safe inputs, config hierarchy, fast help commands, and good defaults.             |
|   6 | Argparse is functional but verbose, requiring manual validation and offering only text-only output without built-in config hierarchy.                         |
|   7 | Typer simplifies the input side using type hints for declarative argument definitions, automatic validation, and environment variable overrides.              |
|   8 | Rich enhances the output side with progress bars, styled tables, colored text, and panels to improve user experience and data readability.                    |
|   9 | Typer provides built-in features like automatic help display when no arguments are provided, version checking, and shell completion installation.             |
|  10 | Textual is recommended for building full Terminal User Interfaces (TUIs) requiring live monitoring, keyboard-driven workflows, and auto-refresh capabilities. |
|  11 | Production patterns emphasize composability by supporting JSON output for piping with tools like JQ and for agent consumption.                                |
|  12 | Import optimization is critical for CLI speed; heavy dependencies should be loaded lazily using techniques like local imports or module-level **getattr**.    |
|  13 | Distribution should prioritize global installation methods like pipx or uvx over standard pip install for library-based CLIs.                                 |
|  14 | Config hierarchy follows a priority order: command-line flags override environment variables, which override default values.                                  |
|  15 | File storage should adhere to the XDG base directory spec on Linux, using the platformdirs package for cross-platform compatibility.                          |
|  16 | For simple scripts, use argparse; for scalable applications, use Typer; for rich output, use Rich; and for full TUIs, use Textual.                            |
|  17 | Agents cannot interact with TUIs because they require interactive input, unlike stateless CLI commands that can be automated.                                 |
|  18 | Typer is preferred over newer frameworks like Cyclopts due to its tight integration with Rich, which is essential for structured, readable output.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/lVIPEjDVTME/hqdefault.jpg)](https://www.youtube.com/watch?v=lVIPEjDVTME)

[Watch on YouTube](https://www.youtube.com/watch?v=lVIPEjDVTME)
