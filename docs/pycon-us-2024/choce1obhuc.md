---
layout: default
title: "Talks -Toby Ho: Rewind: Python Time-Travel Debugger"
nav_order: 202
parent: PyCon US 2024
type: Video Note
description: 'Toby Ho, a developer at Repet, presents "Py Rewind," a Python time-travel debugger inspired by Brett Victor’s "Inventing on Principle" and the Redux state management framework.'
resource: "https://www.youtube.com/watch?v=ChoCe1OBhUc"
youtube_stats:
  view_count: 628
  like_count: 16
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

Toby Ho, a developer at Repet, presents "Py Rewind," a Python time-travel debugger inspired by Brett Victor’s "Inventing on Principle" and the Redux state management framework.
The core mechanism involves forking CPython to log every state-changing operation into a file, allowing the system to replay these updates offline and reconstruct all historical program states in a database.
This approach eliminates the need for traditional breakpoints and mitigates Heisenbugs by enabling users to step backward and forward through execution, utilizing techniques like "backup and drill down" and starting at the end of a runtime error.
Ho also discusses prior art in deterministic replay, such as Mozilla’s rr, and introduces the concept of "omniscient debugging," which allows for advanced user interfaces like a "zoom debugger" that visualizes program execution hierarchically.
The presentation concludes by reflecting on how significant advances in computer science are often coping mechanisms for difficult debugging, suggesting that solving debugging itself could fundamentally transform computing.

# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Toby Ho from Repet, presents a Python time travel debugger named PyRewind.                                                                                                           |
|   2 | Brett Victor’s talk "Inventing on Principle" inspired the project by demonstrating live code editing with immediate visual feedback and historical state trails.                                  |
|   3 | The Redux framework influenced the design by using pure reducer functions to manage immutable state updates, enabling automatic historical tracking.                                              |
|   4 | Traditional debugging methods like print statements and step debuggers have limitations, including temporary code clutter and the difficulty of placing breakpoints without restarting processes. |
|   5 | Heisenbugs, which disappear when observed, are a major challenge that time travel debugging aims to solve.                                                                                        |
|   6 | PyRewind is a fork of CPython 3.10 that logs every state change to a file rather than storing full intermediate states in memory.                                                                 |
|   7 | The system records bytecode operations, such as dictionary assignments and function calls, allowing offline replay to regenerate all historical states.                                           |
|   8 | A SQLite database stores these historical states in append-only tables for code files, errors, function calls, and variable values.                                                               |
|   9 | The debugger interface allows users to step forward and backward through program execution while inspecting variables and stack frames at any point.                                              |
|  10 | PyRewind can debug itself, demonstrating its reliability by tracing its own event loop and UI interactions.                                                                                       |
|  11 | Key debugging techniques include "backup and drill down" to inspect states without breakpoint anxiety and "start at the end" to trace backward from runtime errors.                               |
|  12 | Deterministic replay is an alternative approach that records non-deterministic inputs to ensure consistent program behavior during debugging.                                                     |
|  13 | Prior art includes Mozilla’s rr debugger for C++ and JavaScript, which uses deterministic replay to eliminate Heisenbugs.                                                                         |
|  14 | Bill Lewis coined the term "omniscient debugging" in 2003, describing debuggers with complete knowledge of program state at all times.                                                            |
|  15 | Lewis’s historical timeline UI displays completed method calls with their outputs, allowing navigation to specific execution points.                                                              |
|  16 | The speaker developed a "zoom debugger" inspired by Google Earth, which unrolls loops and allows panning through execution depth to inspect complex logic like AI algorithms.                     |
|  17 | Time travel debugging reveals hidden complexity in code, such as recursion depth, which can be visualized by printing all snapshots from the database.                                            |
|  18 | The presentation concludes by suggesting that significant advances in computer science are often coping mechanisms for difficult debugging, and solving debugging could transform computing.      |
|  19 | In the Q&A, the speaker notes that infinite loops can be handled by killing the process and regenerating the database from the partial log file.                                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ChoCe1OBhUc/hqdefault.jpg)](https://www.youtube.com/watch?v=ChoCe1OBhUc)

[Watch on YouTube](https://www.youtube.com/watch?v=ChoCe1OBhUc)
