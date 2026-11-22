---
layout: default
title: "Talks - Łukasz Langa: Build in-browser 3D experiences with WebGL and PyScript"
nav_order: 184
parent: PyCon US 2024
type: Video Note
description: This presentation by W.
resource: "https://www.youtube.com/watch?v=NQyzFbYZjHk"
youtube_stats:
  view_count: 646
  like_count: 20
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

This presentation by W.
K.
H.
from the Python Foundation explores the creation of 3D web experiences using Python and WebGL 2.0 via the PyScript platform.
The speaker begins by explaining the fundamental graphics concepts of vertices, triangles, and shaders, demonstrating how to render a basic animated triangle using raw WebGL APIs and Pyodide without external JavaScript libraries.
To facilitate more complex interactive scenes, the talk transitions to using the Three.js library, showcasing how to manage 3D objects, cameras, and lighting through Python’s foreign function interface, including handling asynchronous callbacks and module imports.
Further examples illustrate the integration of high-level Python frameworks like Panel and Param with WebGL to build data-driven applications, such as a reactive map visualizing Manhattan taxi trips.
The session concludes by emphasizing that understanding low-level graphics principles remains valuable and fun, allowing developers to deploy rich, interactive 3D content directly in the browser without requiring user installations.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | WebGL 2.0 is based on OpenGL ES 3.0 and has seen major browser support only since 2022, enabling powerful 3D experiences in web browsers.                                         |
|   2 | Computer graphics fundamentally rely on triangles because they are always planar, avoiding the complexity of non-planar polygons with more than three vertices.                   |
|   3 | Shaders are GPU programs that calculate vertex positions and fragment colors, with vertex shaders defining spatial location and fragment shaders determining appearance.          |
|   4 | PyScript enables running Python in the web browser using either MicroPython for lightweight tasks or Pyodide for full CPython support with pip install capabilities.              |
|   5 | PyScript supports worker threads to prevent UI blocking and provides an interactive terminal for debugging directly within the web page.                                          |
|   6 | Drawing a basic triangle in WebGL requires manually compiling GLSL shaders, creating buffers, and configuring the rendering context without high-level frameworks.                |
|   7 | Animation in PyScript can be achieved using asynchronous loops with asyncio.sleep, leveraging the browser's event loop to update graphics without stalling the interface.         |
|   8 | Three.js is a popular JavaScript library used to implement 3D scenes, cameras, lights, and controls, which can be accessed from Python via PyScript's foreign function interface. |
|   9 | PyScript configuration files allow importing JavaScript modules like Three.js and its plugins, such as TrackballControls, to enable intuitive user interactions.                  |
|  10 | When calling JavaScript from Python, developers must use create_proxy to prevent Python objects from being garbage collected before JavaScript callbacks execute.                 |
|  11 | Loading 3D models and textures involves using loaders for formats like GLTF and HDR, where the browser handles downloading and the Python code processes the loaded assets.       |
|  12 | High-level data visualization is possible using Python frameworks like Panel and Param, which integrate with WebGL to create interactive maps and reactive applications.          |
|  13 | Understanding low-level graphics concepts remains valuable for creating engaging 3D web experiences that run directly in the browser without requiring user installation.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NQyzFbYZjHk/hqdefault.jpg)](https://www.youtube.com/watch?v=NQyzFbYZjHk)

[Watch on YouTube](https://www.youtube.com/watch?v=NQyzFbYZjHk)
