---
layout: default
title: "Reinventing the Wheel: A Community-Driven Roadmap for Python Packaging"
nav_order: 55
parent: PyCon US 2025
type: Video Note
description: "The Wheel Next initiative, a community-driven effort involving contributors from NVIDIA and the broader Python ecosystem, aims to evolve the Python packaging infrastructure to address emerging chal..."
resource: "https://www.youtube.com/watch?v=1Oki8vAWb1Q"
youtube_stats:
  view_count: 898
  like_count: 26
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

The Wheel Next initiative, a community-driven effort involving contributors from NVIDIA and the broader Python ecosystem, aims to evolve the Python packaging infrastructure to address emerging challenges in scientific computing and AI.
While acknowledging the current success of PyPI, the initiative identifies critical gaps such as package size limits, the lack of support for specialized hardware like GPUs and specific CPU microarchitectures, and the inefficient duplication of native libraries.
To solve these issues without disrupting existing workflows, the project proposes several PEPs, including external wheel hosting, default extras, and improved index resolution, while prioritizing backward compatibility and user experience.
A key innovation is the "wheel variants" prototype, which allows installers to automatically detect the local hardware environment and select the most optimized package build, eliminating the need for manual index selection.
The initiative also seeks to formalize packaging governance through a new council model and invites community participation to refine these proposals, ensuring the packaging ecosystem remains robust and scalable for the next decade.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Wheel Next is a community-driven initiative to evolve the Python packaging ecosystem over the next decade.                             |
|   2 | The project aims to address limitations in the current wheel format, such as size limits and lack of hardware-specific optimization.   |
|   3 | Key problems include difficulty managing GPU and CPU micro-architecture specific packages and large package sizes on PyPI.             |
|   4 | The initiative prioritizes backward compatibility and user experience, pushing complexity into tooling rather than user workflows.     |
|   5 | PEP 759 proposes external wheel hosting to distribute artifacts and reduce the burden on PyPI.                                         |
|   6 | PEP 778 addresses the challenge of supporting symbolic links in wheels for sharing native libraries and DSOs.                          |
|   7 | A proposal for "default extras" allows packages to specify a default backend if the user does not choose one.                          |
|   8 | PEP 772 introduces a formal governance structure with an elected Packaging Council to manage packaging decisions.                      |
|   9 | PEP 766 defines explicit priority choices for resolving packages across multiple indices to improve security and UX.                   |
|  10 | The "Wheel Variants" proposal enables automatic selection of the best package build based on the specific hardware environment.        |
|  11 | A prototype for Wheel Variants is available for testing, supporting PyTorch, NumPy, and XGBoost with automatic platform detection.     |
|  12 | The system uses provider plugins to introspect the environment, allowing users to override or opt out of specific variant resolutions. |
|  13 | Participation is open to the community via the Wheel Next site, GitHub, Discord, and PyCon sprints.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1Oki8vAWb1Q/hqdefault.jpg)](https://www.youtube.com/watch?v=1Oki8vAWb1Q)

[Watch on YouTube](https://www.youtube.com/watch?v=1Oki8vAWb1Q)
