---
layout: default
title: "The past, present, and future of virtual environments - Zanie Blue"
nav_order: 106
parent: PyCon US 2025
type: Video Note
description: "Zeny Blue, a developer at Astral, presents a comprehensive overview of the evolution of Python virtual environments, arguing that modern tools are increasingly abstracting these mechanisms to reduc..."
resource: "https://www.youtube.com/watch?v=CV8KRvWKYDw"
youtube_stats:
  view_count: 8329
  like_count: 284
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

Zeny Blue, a developer at Astral, presents a comprehensive overview of the evolution of Python virtual environments, arguing that modern tools are increasingly abstracting these mechanisms to reduce cognitive load for developers.
The talk contrasts traditional imperative workflows, such as manually activating environments and installing packages with `pip`, with declarative approaches that prioritize reproducibility and import boundaries.
Blue highlights `uv` as a key example of this shift, demonstrating how it automates dependency resolution, locking, and environment synchronization to ensure that projects and scripts run consistently without requiring users to manage environment state manually.
The presentation also addresses complex scenarios, such as managing build dependencies and external system requirements, proposing future improvements like locking build dependencies and standardizing how editors discover virtual environments.
Ultimately, Blue advocates for a future where best practices are the default, intuitive behavior, allowing Python to remain accessible and efficient as the ecosystem continues to grow.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Virtual environments isolate installed packages to prevent conflicting versions, a fundamental constraint of Python's module system.              |
|   2 | They enforce import boundaries, ensuring scripts only access declared dependencies, which is critical for production stability.                   |
|   3 | Early tools like virtualenv and pip focused on foundational mechanics such as creating environments and installing packages imperatively.         |
|   4 | Pip's imperative interface requires constant awareness of environment state, leading to cognitive overhead and potential version inconsistencies. |
|   5 | Pip-tools improved workflows by adding compile and sync commands to manage locked requirements and remove undeclared packages.                    |
|   6 | UV introduces a declarative project interface where dependencies are resolved, locked, and installed in a single command.                         |
|   7 | The UV run command automatically activates the virtual environment, eliminating the need for manual activation and state tracking.                |
|   8 | UV supports ephemeral dependencies via the with option, layering additional packages into isolated environments for specific invocations.         |
|   9 | Tool management through UV allows installing and running command-line tools in isolated, disposable virtual environments without manual setup.    |
|  10 | PEP 723 enables inline script metadata, allowing scripts to declare dependencies that UV resolves and installs at runtime.                        |
|  11 | Declarative interfaces reduce cognitive load by making best practices the default, ensuring reproducibility and ease of use.                      |
|  12 | Current limitations include imperative workflows for tool installation and complex build isolation scenarios like Flash Attention.                |
|  13 | Build dependencies are currently not included in lockfiles, causing ecosystem-wide breakage when upstream packages release breaking changes.      |
|  14 | Editors struggle to find virtual environments due to lack of standard locations, hindering language features and type checking.                   |
|  15 | Future improvements should include locking build dependencies and standardizing environment discovery for better editor integration.              |
|  16 | Language servers may not require full virtual environments, as they primarily need type information rather than complete package binaries.        |
|  17 | The Python ecosystem must continue investing in user experience to make programming accessible and intuitive for a broader audience.              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CV8KRvWKYDw/hqdefault.jpg)](https://www.youtube.com/watch?v=CV8KRvWKYDw)

[Watch on YouTube](https://www.youtube.com/watch?v=CV8KRvWKYDw)
