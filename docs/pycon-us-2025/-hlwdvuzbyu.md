---
layout: default
title: "How to build a cross-platform graphical user interface with Python - Russell Keith-Magee"
nav_order: 95
parent: PyCon US 2025
type: Video Note
description: "Russell Keith McGee presents a comprehensive guide on building cross-platform graphical user interface applications using the Beware suite, an open-source collection of tools supported by Anaconda."
resource: "https://www.youtube.com/watch?v=-HlWDVuZbYU"
youtube_stats:
  view_count: 24737
  like_count: 706
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

Russell Keith McGee presents a comprehensive guide on building cross-platform graphical user interface applications using the Beware suite, an open-source collection of tools supported by Anaconda.
The core of the presentation focuses on Toga, a toolkit that enables developers to write a single Python codebase that generates native user interfaces for desktop, iOS, and Android platforms, and Briefcase, a packaging tool that compiles these Python applications into standalone, distributable artifacts without requiring end users to have Python installed.
McGee demonstrates the development workflow by bootstrapping a new project with Briefcase, implementing UI elements like text inputs and buttons using Toga’s Pythonic API, and utilizing asynchronous event handlers to maintain application responsiveness during interactions such as displaying dialogues.
The talk further illustrates how to extend the application’s capabilities by integrating platform-specific hardware features, such as GPS location services and map views, while managing necessary permissions and platform-specific dependencies through configuration files.
Finally, the presentation explains the underlying three-layer architecture of Toga, which bridges Python code to native platform APIs, and outlines future developments including improved support for iOS and Android binary wheels and enhanced packaging capabilities for Windows.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Beware is a suite of open-source tools for creating native user interfaces in Python across desktop, iOS, Android, web, and console platforms.                            |
|   2 | Toga serves as the cross-platform GUI toolkit, allowing a single Python codebase to generate native-looking and functionally native applications on each target platform. |
|   3 | Briefcase is the packaging tool that wraps Python applications into standalone units for distribution, supporting deployment to app stores and desktop environments.      |
|   4 | The Briefcase wizard bootstraps new projects by generating configuration files, application icons, and initial code templates for selected GUI frameworks like Toga.      |
|   5 | Briefcase dev provides a developer mode for rapid iteration, installing dependencies and running the app within a local virtual environment.                              |
|   6 | Toga uses a CSS-like styling system called Pack and a layout system based on CSS3 flexbox to manage widget appearance and positioning.                                    |
|   7 | Asynchronous event handlers are supported in Toga to prevent UI freezing, allowing the application to process events and redraw while waiting for user input.             |
|   8 | Briefcase create generates a complete application template by downloading a Python support package, a stub binary, and installing application requirements.               |
|   9 | Briefcase build compiles or signs the application for the specific target platform, such as signing binaries on macOS or compiling stubs on Linux.                        |
|  10 | Mobile deployment for iOS requires macOS due to tooling constraints, while Android builds can be performed on macOS, Linux, or Windows.                                   |
|  11 | Briefcase package produces distribution artifacts like MSI installers on Windows, RPM or deb packages on Linux, and DMG files on macOS.                                   |
|  12 | Toga provides cross-platform APIs for hardware features like location services, requiring explicit permission requests and configuration declarations.                    |
|  13 | Adding platform-specific dependencies, such as OpenStreetMap for Android, requires updating the project configuration and regenerating the application template.          |
|  14 | Toga employs a three-layer architecture consisting of a public interface, a standardized implementation layer, and direct native API calls via language bridges.          |
|  15 | Developers can access native platform APIs directly through the widget_imple.native attribute to extend functionality beyond the standard Toga API.                       |
|  16 | Future developments include support for building iOS and Android binary wheels for PyPI and improved Windows packaging capabilities in Briefcase.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-HlWDVuZbYU/hqdefault.jpg)](https://www.youtube.com/watch?v=-HlWDVuZbYU)

[Watch on YouTube](https://www.youtube.com/watch?v=-HlWDVuZbYU)
