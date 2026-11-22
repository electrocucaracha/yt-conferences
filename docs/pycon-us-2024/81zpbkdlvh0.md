---
layout: default
title: Python Steering Council Panel
nav_order: 138
parent: PyCon US 2024
type: Video Note
description: "The Python Steering Council, a five-person elected body responsible for the technical direction of the Python language and CPython interpreter, presented an overview of their governance structure a..."
resource: "https://www.youtube.com/watch?v=81ZpbKdlvh0"
youtube_stats:
  view_count: 539
  like_count: 7
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

The Python Steering Council, a five-person elected body responsible for the technical direction of the Python language and CPython interpreter, presented an overview of their governance structure and recent activities at PyCon.
The council, which operates independently from the Python Software Foundation but collaborates closely with it, manages critical decisions such as PEP approvals, Code of Conduct enforcement, and the selection of release managers.
A significant focus of their work involves funding and supporting key roles, including developers in residence, a security developer, and a newly announced secretary to improve communication and project management.
The presentation also detailed the establishment of specialized groups, such as the Documentation Editorial Board, the C API Working Group, and the Typing Council, which handle specific areas of the ecosystem to ensure expert oversight.
Regarding Python 3.13, the release manager highlighted that while there are no major new syntax features, the version includes important changes such as the removal of deprecated standard library modules, extended support timelines, and new platform support for iOS and Android.
A notable addition is a new interactive interpreter with color support and multiline editing, which is enabled by default on supported platforms.
Furthermore, the council outlined a cautious, phased plan for making the Global Interpreter Lock (GIL) optional in CPython, emphasizing that this is not a breaking change akin to Python 4 but rather a gradual transition aimed at improving multithreading performance while strictly maintaining backward compatibility.
The council stressed the importance of community feedback and testing during the experimental phase to ensure the stability and success of this significant architectural change.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Python Steering Council is a five-person elected body responsible for the technical direction of Python, CPython, and the standard library.                   |
|   2 | The current 2024 Council members are Pablo Galindo, Gregory P. Smith, Thomas Wouters, Emily Morehouse, and Barry Warsaw.                                          |
|   3 | The Council meets weekly to discuss agenda items, pronounce on PEPs, enforce the Code of Conduct, and select the release manager.                                 |
|   4 | The Council advises the PSF on funding for developers in residence, security roles, and core developer sprints.                                                   |
|   5 | New funding has secured two additional developers in residence, a security developer in residence, and a new Steering Council secretary.                          |
|   6 | The Documentation Editorial Board was established to oversee CPython documentation, while the docs Working Group manages broader volunteer contributions.         |
|   7 | The C API Working Group was formed to coordinate the development and maintenance of Python's C API and preapprove related PEPs.                                   |
|   8 | The Typing Council was created to ensure the type system remains useful, usable, and stable for static analysis and runtime checking.                             |
|   9 | Python 3.13 will not introduce new syntax or modules but will remove deprecated standard library modules and functions per PEP 594.                               |
|  10 | Python 3.13 extends bugfix support to two years and adds support for iOS and Android platforms.                                                                   |
|  11 | A new interactive interpreter is included in Python 3.13, featuring color support, multiline editing, and paste support.                                          |
|  12 | An optional Just-In-Time (JIT) compiler is available in Python 3.13 but is not enabled by default.                                                                |
|  13 | PEP 703 makes the Global Interpreter Lock (GIL) optional in CPython to enable true parallelism.                                                                   |
|  14 | The removal of the GIL is a phased process starting with an experimental build in Python 3.13, followed by supported builds, and eventually becoming the default. |
|  15 | The Steering Council emphasizes backward compatibility and community feedback to ensure the GIL removal does not cause a disruptive break like Python 2 to 3.     |
|  16 | Users can test the free-threaded build in Python 3.13 by compiling CPython with the --disable-gil option.                                                         |
|  17 | The Council stresses that Python without the GIL is not Python 4 and will maintain compatibility with existing code.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/81ZpbKdlvh0/hqdefault.jpg)](https://www.youtube.com/watch?v=81ZpbKdlvh0)

[Watch on YouTube](https://www.youtube.com/watch?v=81ZpbKdlvh0)
