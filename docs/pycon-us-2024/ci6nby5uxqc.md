---
layout: default
title: "Talks - James Schmitz: Creative Coding with py5, the Python version of Processing"
nav_order: 189
parent: PyCon US 2024
type: Video Note
description: "Jim Schmidtz presents pi5, a Python library for creative coding that serves as a Pythonic interface to the Processing framework, allowing users to focus on artistic expression rather than low-level..."
resource: "https://www.youtube.com/watch?v=cI6Nby5UXqc"
youtube_stats:
  view_count: 1849
  like_count: 36
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

Jim Schmidtz presents pi5, a Python library for creative coding that serves as a Pythonic interface to the Processing framework, allowing users to focus on artistic expression rather than low-level window management and event handling.
The talk demonstrates pi5’s seamless integration with the Python ecosystem, showcasing its ability to work with NumPy arrays for pixel manipulation, SciPy for image processing, and Trimesh for 3D geometry, while also supporting Shapely for computational geometry.
Schmidtz highlights the library’s performance capabilities, using line profiling to compare vectorized drawing commands against iterative loops, and illustrates its versatility by combining it with OpenCV, Pillow, and Matplotlib for real-time data visualization and texture mapping.
The presentation also covers pi5’s applications in education, data visualization, and art, including a live installation in Detroit that uses real-time environmental data.
Finally, Schmidtz outlines future plans for the project, including expanding educational resources, growing the community, and developing a native PyScript implementation to eliminate the need for a Java runtime.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Pi5 is a Python library for creative coding that abstracts window management, event handling, and rendering to let users focus on creative ideas.                                           |
|   2 | Processing is a Java-based framework started at MIT in 2001 that enabled non-developers to create visual art and data visualizations with minimal boilerplate code.                         |
|   3 | Pi5 connects to Processing Java jars via the JPype library but provides a pure Python experience, ensuring users never encounter Java exceptions.                                           |
|   4 | The library was created by Jim Schmid in March 2020 during the COVID-19 lockdown as a calming creative outlet.                                                                              |
|   5 | Pi5 supports multiple programming modes including Static mode for images, Imported mode for animations, Module mode for standard Python imports, and Class mode for object-oriented design. |
|   6 | The library integrates with the Python ecosystem by working with NumPy pixel arrays, allowing seamless use with SciPy filters like Gaussian blur.                                           |
|   7 | Vectorized drawing commands, such as passing large NumPy arrays to the vertices method, significantly improve performance compared to drawing individual points in loops.                   |
|   8 | Line profiler tools are built into Pi5 to help users identify performance bottlenecks in animated sketches.                                                                                 |
|   9 | Pi5 integrates with Trimesh to load and render 3D GLTF models, supporting features like extrusion and Boolean geometry.                                                                     |
|  10 | The library works with Shapely for computational geometry, enabling complex 2D shape operations like symmetric difference without manual vertex winding management.                         |
|  11 | Pi5 can use Matplotlib for real-time charting and OpenCV for webcam input, applying these as texture maps on 3D objects.                                                                    |
|  12 | The library is designed to run efficiently on modest hardware, such as a 2015 dual-core Mac, making it accessible to a wider audience.                                                      |
|  13 | Pi5 is used in education, data visualization for single-cell RNA sequences, and art installations like the Breath Eaters project in Detroit.                                                |
|  14 | Running Pi5 requires Java 17, and the library includes tools to detect and help resolve common Java installation issues.                                                                    |
|  15 | Future plans include implementing Pi5 in PyScript to remove the Java dependency and expand educational resources for beginners.                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/cI6Nby5UXqc/hqdefault.jpg)](https://www.youtube.com/watch?v=cI6Nby5UXqc)

[Watch on YouTube](https://www.youtube.com/watch?v=cI6Nby5UXqc)
