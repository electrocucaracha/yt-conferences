---
layout: default
title: "Brains and Explosions: A Simple VDB Writer for Python - Joachim Pfefferkorn"
nav_order: 26
parent: PyCon US 2026
type: Video Note
description: "The speaker presents Neurovolume, a lightweight Python library designed to write VDBs (sparse volumetric data structures) for 3D graphics and scientific visualization, addressing the complexity and..."
resource: "https://www.youtube.com/watch?v=a8Fy4kk2xFY"
youtube_stats:
  view_count: 250
  like_count: 5
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

The speaker presents Neurovolume, a lightweight Python library designed to write VDBs (sparse volumetric data structures) for 3D graphics and scientific visualization, addressing the complexity and dependency issues of existing tools like OpenVDB.
Developed by a VFX artist transitioning into software engineering, the library is written in Zig with no external dependencies and uses NumPy as the primary data interface to ensure portability and ease of use.
The project originated from the speaker’s desire to create an accessible fMRI visualization pipeline, which revealed significant friction in integrating scientific data with VFX workflows due to the lack of simple, pip-installable VDB writers.
By implementing features such as sparse tiling, grid management, and temporal interpolation, Neurovolume allows users to efficiently render complex data, including weather simulations and brain activity, directly into standard VFX software.
The talk concludes with a demonstration of a toy fMRI analysis pipeline, highlighting the noise inherent in BOLD responses and advocating for accessible, low-dependency tools that empower scientists and artists to replicate and understand computational discoveries.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Neurovolume is a Python library with a Zig backend that writes VDBs, a sparse volumetric data structure used in 3D graphics. |
|   2 | The project originated from the speaker's background in VFX and a desire to visualize fMRI data for job interviews. |
|   3 | VDBs differ from point clouds and meshes by representing volumetric interiors efficiently, allowing for art-directable rendering of complex phenomena like smoke and water. |
|   4 | The speaker identified a gap in the ecosystem for a lightweight, portable VDB writer that could be installed via pip without complex containerization. |
|   5 | Initial attempts using Go and LLM-generated code resulted in an unmaintainable codebase, prompting a rewrite from first principles in Zig. |
|   6 | The library relies on NumPy as the primary data intermediary to avoid writing parsers for every possible scientific data format. |
|   7 | Tiles are implemented to prune uniform data, reducing file size by up to 40% without visual degradation, while grids allow for separate attribute channels. |
|   8 | The Zig backend was chosen for its speed and lack of opinionated unsafe code, facilitating direct C ABI integration with Python. |
|   9 | The speaker built a toy fMRI analysis pipeline using Blender, Nibabel, and ANTs to demonstrate the library's capabilities. |
|  10 | This pipeline involved skull stripping, extracting BOLD response data, applying Gaussian blur, and rendering the result in Blender. |
|  11 | The final render highlighted the extreme noise in fMRI data, showing activity outside the brain, which aligns with the "dead salmon" study findings. |
|  12 | The project emphasizes accessibility and portability to enable cross-domain collaboration between artists, scientists, and engineers. |
|  13 | The speaker argues that reducing dependencies and abstraction barriers allows non-engineers to replicate and understand scientific visualizations. |
|  14 | Key contributors include Robbie Lyman for the Zig code and Zach Lip for the initial Docker container. |
|  15 | The library supports time interpolation to smooth low-frame-rate data, such as fMRI scans, for playback at standard video rates. |
|  16 | The speaker acknowledges the limitations of their simplified analysis pipeline and the risks of data massaging in scientific visualization. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/a8Fy4kk2xFY/hqdefault.jpg)](https://www.youtube.com/watch?v=a8Fy4kk2xFY)

[Watch on YouTube](https://www.youtube.com/watch?v=a8Fy4kk2xFY)
