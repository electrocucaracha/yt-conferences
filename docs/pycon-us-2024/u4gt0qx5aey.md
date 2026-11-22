---
layout: default
title: "Talks - Neeraj Pandey, Manoj Pandey: Visual Data Storytelling with Blender and Python"
nav_order: 203
parent: PyCon US 2024
type: Video Note
description: "This presentation, delivered by NJ Pand and Manoj Pand at a Python conference, explores visual data storytelling using Python libraries such as Matplotlib, Manim, and Blender."
resource: "https://www.youtube.com/watch?v=U4Gt0qX5aEY"
youtube_stats:
  view_count: 1003
  like_count: 19
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

This presentation, delivered by NJ Pand and Manoj Pand at a Python conference, explores visual data storytelling using Python libraries such as Matplotlib, Manim, and Blender.
The speakers begin by highlighting Matplotlib’s animation capabilities, specifically the `FuncAnimation` class, which allows for dynamic updates of plots to reveal trends and patterns over time, with examples including sine waves, quiver plots, and 3D confusion matrices.
They then introduce Manim, a mathematical animation engine that uses vector graphics to create precise, high-quality educational videos, explaining its workflow where Python code defines scenes that are rendered by Cairo and assembled into video files by FFmpeg.
The session further demonstrates how to integrate Matplotlib charts into Manim scenes for enhanced visualization and introduces Blender’s Python API (`bpy`) for creating complex 3D animations, covering scene management, object manipulation, and data-driven visualizations like 3D bar charts and line graphs.
The talk concludes by emphasizing the complementary strengths of these tools, providing code examples and resources for attendees to replicate the demonstrated animations and apply these techniques to their own data analysis projects.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session covers visual data storytelling using Blender, Python, Matplotlib, and Manim.                                                                       |
|   2 | Matplotlib serves as the foundational library for data visualization in Python, supporting static charts like line plots, scatter plots, and bar charts.        |
|   3 | Matplotlib animations are built using the FuncAnimation and ArtistAnimation classes, with FuncAnimation offering greater flexibility for dynamic updates.       |
|   4 | The animation process involves defining frames, updating plot elements via artist objects, and rendering through external libraries like FFmpeg or ImageMagick. |
|   5 | Matplotlib supports 2D and 3D visualizations, including heatmaps, confusion matrices, and contour plots for airflow simulation.                                 |
|   6 | Manim is a mathematical animation engine that uses vector graphics to create precise, high-quality animations for mathematical concepts.                        |
|   7 | Manim integrates LaTeX equations directly into animations and uses Cairo for 2D rendering and WebGL for 3D rendering.                                           |
|   8 | The Manim workflow involves writing Python code to define scenes, adding Mobject and VMobject elements, and using animations like Create and Transform.         |
|   9 | Manim uses FFmpeg to stitch individual frames rendered by Cairo into a final video file.                                                                        |
|  10 | Basic Manim building blocks include Text, lines, shapes, and Mobjects, which serve as the core classes for animation elements.                                  |
|  11 | Manim can replicate Matplotlib examples, such as sine and cosine waves, using vector-based drawing functions.                                                   |
|  12 | Manim supports linear transformations and coordinate systems, allowing for dynamic visualization of matrices and geometric shapes.                              |
|  13 | Matplotlib and Manim can be combined by saving Matplotlib charts as images and injecting them into Manim scenes using the ImageMobject class.                   |
|  14 | Blender is a 3D animation studio controlled via its Python API (bpy) to automate scene creation and object manipulation.                                        |
|  15 | The Blender API allows for scene management, including setting up cameras, lighting, and switching between different scenes.                                    |
|  16 | Object manipulation in Blender involves adding, deleting, rotating, scaling, and modifying meshes to create complex 3D visuals.                                 |
|  17 | Blender can visualize data structures like confusion matrices by creating 3D cubes where height represents data values.                                         |
|  18 | The presentation provided Jupyter notebooks with code examples for all demonstrated animations and visualizations.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/U4Gt0qX5aEY/hqdefault.jpg)](https://www.youtube.com/watch?v=U4Gt0qX5aEY)

[Watch on YouTube](https://www.youtube.com/watch?v=U4Gt0qX5aEY)
