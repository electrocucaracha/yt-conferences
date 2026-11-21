---
layout: default
title: "How many spoons does your environment cost - Dawn Wages"
nav_order: 38
parent: PyCon US 2026
type: Video Note
description: "Don Wages, a community lead for Anaconda, presents a talk at PyCon US exploring the significant cognitive and technical challenges developers face when building Python software environments."
resource: "https://www.youtube.com/watch?v=IenJs6ZO1hA"
youtube_stats:
  view_count: 159
  like_count: 4
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

Don Wages, a community lead for Anaconda, presents a talk at PyCon US exploring the significant cognitive and technical challenges developers face when building Python software environments.
Using the metaphor of "spoon theory" to describe finite mental energy, Wages argues that environment setup is often miscategorized as free overhead, ignoring the substantial invisible labor involved in resolving dependency conflicts and hardware incompatibilities.
Through a series of intentionally broken live code demos, the presentation illustrates how failures arise from complex layers of abstraction, including runtime differences, OS-specific behaviors, and hardware constraints, which collectively impose a heavy "switching tax" on developers.
Wages emphasizes that these issues are not personal failures but systemic ecosystem challenges, urging the audience to recognize the value of sustainable autonomy and deliberate ownership of their technical stacks.
The talk concludes by highlighting ongoing ecosystem improvements, such as PEP 751 for standardized lock files and Docker’s role in reproducibility, while advocating for a greater appreciation of the human effort required to maintain robust software infrastructure.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The presentation explores why building Python software environments is difficult and highlights the cognitive load associated with managing code and processes. |
|   2 | The speaker, Don Wages, shares a personal anecdote about initially underestimating the complexity of Python environments after moving from a Django development role. |
|   3 | Three reasons for underestimating environment challenges are internalized failure, reliance on team support, and the rapid investment in developer experience that obscured underlying complexity. |
|   4 | Spoon theory is used as a metaphor to explain finite cognitive energy and the invisible costs of different tasks, particularly in environment setup. |
|   5 | Environment setup is often miscategorized as free overhead, but it involves significant cognitive effort when dealing with dependency conflicts or broken virtual environments. |
|   6 | The talk includes live demos of failing code to illustrate common issues, encouraging the audience to cheer for broken code to build empathy for developers. |
|   7 | One demo failure involved QP, a NumPy-compatible array library for CUDA GPUs, which does not support Apple Silicon, requiring non-drop-in replacements like MLX or Torch. |
|   8 | Another failure was caused by a naming mismatch in libgo.so.1, where the package installed successfully via pip but failed at import time due to OS dynamic linker differences. |
|   9 | The abstraction layer of software environments includes user intent, runtime, package dependencies, environment isolation, OS interface, hardware abstraction, and physical firmware. |
|  10 | Each layer introduces potential points of failure, such as runtime translation differences, implicit package dependency contracts, and OS-enforced constraints. |
|  11 | A demo failure related to path problems and symbolic links on macOS versus Linux, where a link existed but pointed to a false target, causing runtime errors. |
|  12 | Hardware abstraction layers pretend compute is uniform, but CUDA, MPS, and CPU have different support types, precision guarantees, and failure modes. |
|  13 | Physical firmware is a non-negotiable layer where no amount of correct Python code can resolve the realities of the physical world. |
|  14 | The process of software development is messy, involving false starts, redesigns, and imperfect ecosystem considerations, rather than a linear flow. |
|  15 | Cognitive tasks have limits, and pushing beyond them leads to burnout, as the brain does not have infinite neuroplasticity or elasticity. |
|  16 | The switching tax refers to the time and stress lost when an environment breaks, forcing a task switch that averages 23 minutes to recover from. |
|  17 | Mental overload persists for unfinished tasks, causing developers to return to their original work when given the opportunity. |
|  18 | A Docker-related demo failed due to platform mismatches, memory allocation issues, and the inability to inherit necessary shell environments. |
|  19 | Miscategorization of work as low-cost setup leads to invisible loads, especially when developers assume their local machine setup is sufficient for all workflows. |
|  20 | PEP 751, accepted in 2025, standardized the lock file format for pip as pylock.toml to improve environment reproducibility. |
|  21 | PEP 723, introduced in 2023, added inline script metadata to Python files to simplify dependency management. |
|  22 | Docker and OCI containers address environment reproducibility by capturing the entire OS layer, though platform architecture mismatches can still occur. |
|  23 | Multi-arch builds using tools like docker buildx address architecture mismatches but require explicit effort in CI infrastructure. |
|  24 | The final demo failed due to dependency conflicts, wrong interpreter selection, conda and pip interoperability issues, broken editable installs, and architecture mismatches. |
|  25 | The speaker advocates for sustainable autonomy, where developers own and understand their stack, and deliberate ownership of the ecosystem that supports them. |
|  26 | Understanding the hundreds of thousands of hours invested in the ecosystem helps developers offload the burden of failing infrastructure and environments. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/IenJs6ZO1hA/hqdefault.jpg)](https://www.youtube.com/watch?v=IenJs6ZO1hA)

[Watch on YouTube](https://www.youtube.com/watch?v=IenJs6ZO1hA)
