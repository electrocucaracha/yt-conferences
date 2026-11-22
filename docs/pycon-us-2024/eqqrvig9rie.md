---
layout: default
title: "Talks - Ofek Lev: Hatch: The only tool you need"
nav_order: 200
parent: PyCon US 2024
type: Video Note
description: "Hatch is a comprehensive Python project manager and build backend, designed to streamline developer workflows with a focus on user experience and standards compliance."
resource: "https://www.youtube.com/watch?v=eQqRVig9RIE"
youtube_stats:
  view_count: 1521
  like_count: 28
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

Hatch is a comprehensive Python project manager and build backend, designed to streamline developer workflows with a focus on user experience and standards compliance.
The tool splits into two main components: Hatchling, which serves as a flexible build backend supporting plugins for various targets like wheels and binaries, and the Hatch CLI, which manages environments, scripts, and testing.
A key feature is its environment system, which allows users to define isolated workspaces with specific Python versions, dependencies, and scripts, supporting complex configurations through matrices and overrides.
Hatch also integrates testing via pytest, static analysis using Ruff, and Python version management, while offering a plugin architecture that enables dynamic metadata and build hooks.
Future developments include workspaces for monorepos, improved performance, and support for standardized lockfiles, positioning Hatch as a central tool for modern Python packaging and development.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Hatch is a Python project manager similar to Cargo or npm, designed to centralize development workflows.                                               |
|   2 | The project was rewritten in 2019 after an initial 2017 attempt, leading to its induction into the Python Packaging Authority.                         |
|   3 | Hatch is split into two components: hatchling, the build backend, and the Hatch CLI, with most features implemented as plugins.                        |
|   4 | Key priorities for Hatch include user experience with good defaults and adherence to Python packaging standards.                                       |
|   5 | Major users of Hatch include Project Jupyter, the official Python packaging tutorial, and Visual Studio Code, which supports Hatch environments.       |
|   6 | Installation methods include pip, package managers like Homebrew, official installers for macOS and Windows, or standalone binaries.                   |
|   7 | Hatchling simplifies build configuration by using unambiguous sections for build targets and respecting version control ignore files.                  |
|   8 | Built-in build targets include wheel, source distribution, and self-bootstrapping binaries, with plugins available for other formats.                  |
|   9 | Metadata hooks allow dynamic metadata generation using Python code, similar to setup.py, with plugins for various use cases.                           |
|  10 | Build hooks enable custom build steps, such as creating files for source distributions or compiling Cython extensions.                                 |
|  11 | Versioning plugins support schemes like SemVer and CalVer, allowing command-line version bumps to replace tools like bump2version.                     |
|  12 | Publishing is integrated into Hatch, replacing tools like twine, with a standardized interface for PyPI or other repositories.                         |
|  13 | Environments are a core feature of Hatch, providing isolated workspaces for dependencies and arbitrary commands, distinct from single-command runners. |
|  14 | Users can interact with environments by entering a shell or sending commands directly without entering the environment.                                |
|  15 | Environment configuration allows setting Python versions, dependencies, dev mode, platforms, and environment variables.                                |
|  16 | Scripts in Hatch are shell-based workflows that support recursion, context formatting, and ignoring exit codes.                                        |
|  17 | Matrices allow generating multiple environments from combinations of variables, with options to filter or override settings.                           |
|  18 | Testing is backed by pytest with plugins for parallel execution, retries, and coverage, though other test runners can be used.                         |
|  19 | Static analysis is supported via Ruff, with curated default rules to reduce mental overhead for users.                                                 |
|  20 | Hatch can manage Python installations, supporting CPython and PyPy, and can add them to the system path.                                               |
|  21 | A new PEP allows defining metadata and dependencies in standalone Python scripts, managed by Hatch.                                                    |
|  22 | Upcoming features include workspaces for monorepos, dependency management commands, and performance improvements.                                      |
|  23 | Hatch environments support inheritance, allowing base environments to define common dependencies for child environments.                               |
|  24 | Private repository dependencies are supported by outsourcing package installation to pip or uv.                                                        |
|  25 | Workspaces for managing multiple interdependent projects are planned for implementation.                                                               |
|  26 | Hatch can be used as a task runner for non-Python projects, such as managing JavaScript or C workflows.                                                |
|  27 | Support for custom installation locations for Python distributions is pending review of a contributor PR.                                              |
|  28 | Hatch is suitable for managing non-Python projects with Python dependencies using standalone script metadata.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eQqRVig9RIE/hqdefault.jpg)](https://www.youtube.com/watch?v=eQqRVig9RIE)

[Watch on YouTube](https://www.youtube.com/watch?v=eQqRVig9RIE)
