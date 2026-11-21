---
layout: default
title: "How to give your Python code to someone else - Russell Keith-Magee"
nav_order: 67
parent: PyCon US 2026
type: Video Note
description: "Russell Keith McGee, a principal engineer at Anaconda and founder of the BeeWare project, explores the complexities of distributing Python code to end users who may lack a Python environment."
resource: "https://www.youtube.com/watch?v=A2-pcMOVu0c"
youtube_stats:
  view_count: 456
  like_count: 12
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

Russell Keith McGee, a principal engineer at Anaconda and founder of the BeeWare project, explores the complexities of distributing Python code to end users who may lack a Python environment.
He distinguishes between tools and deployed projects, explaining how PEP 723 inline metadata and PEP 621 project-level metadata in `pyproject.toml` allow script runners like `uv` to manage dependencies and Python versions automatically.
While single-file bundling tools like PyInstaller offer a solution, they often face fragility with dynamic imports and platform-specific constraints.
To address these challenges, McGee introduces Briefcase, a BeeWare tool that packages Python applications into native, self-contained installers for Windows, macOS, Linux, iOS, and Android.
This approach ensures that end users can run the application without needing to install Python or manage virtual environments, facilitating distribution through app stores and mobile device management systems.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker is Russell Keith McGee, a principal engineer at Anaconda and founder of the BeeWare project. |
|   2 | BeeWare is an open-source project enabling native cross-platform user interfaces using only Python. |
|   3 | Packaging Python code for distribution is complex due to varying deployment needs and environment dependencies. |
|   4 | Not all Python code is a runnable tool; websites and notebooks require deployment configuration rather than direct execution. |
|   5 | PEP 723 allows inline script metadata to specify minimum Python versions and dependencies. |
|   6 | Script runners like UV, Hatch, and Pex can utilize PEP 723 metadata to manage environments and dependencies. |
|   7 | PEP 338 enables directories with a __main__.py file to be executed as Python objects. |
|   8 | PEP 441 allows zip files containing __main__.py to be executed directly as zip apps. |
|   9 | PEP 621 defines project-level metadata in pyproject.toml, including name, version, and dependencies. |
|  10 | Entry points defined in PEP 621 allow packages to be invoked as command-line scripts without referencing the Python interpreter. |
|  11 | Tools like UVX and Pipx can install and run PyPI packages with entry points in isolated environments. |
|  12 | Requiring users to install Python or specific runtimes creates significant barriers to tool adoption. |
|  13 | Single-file executables via tools like PyInstaller and PyOxidizer offer portability but face issues with dynamic imports and GUI toolkits. |
|  14 | Platform-specific packaging solutions include macOS .app bundles, Windows MSI installers, and Linux Flatpaks or system packages. |
|  15 | Briefcase is a BeeWare tool that packages Python applications into standalone, distributable artifacts for various platforms. |
|  16 | Briefcase supports generating installers for Windows, macOS, Linux, iOS, and Android without requiring users to have Python installed. |
|  17 | Briefcase handles application signing and notarization to ensure security and compatibility. |
|  18 | Self-contained installers facilitate distribution via app stores and mobile device management systems. |
|  19 | The choice of packaging method depends on the target audience's technical expertise and environment constraints. |
|  20 | Briefcase can build Linux packages using Docker containers, allowing cross-distribution builds from a single host. |
|  21 | Building macOS or Windows packages requires the respective native operating systems due to platform-specific build tools. |
|  22 | The BeeWare project welcomes financial support and contributions from the community. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/A2-pcMOVu0c/hqdefault.jpg)](https://www.youtube.com/watch?v=A2-pcMOVu0c)

[Watch on YouTube](https://www.youtube.com/watch?v=A2-pcMOVu0c)
