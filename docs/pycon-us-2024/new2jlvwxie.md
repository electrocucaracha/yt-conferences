---
layout: default
title: "Tutorials - Russell Keith-Magee: Build a cross-platform app with BeeWare"
nav_order: 30
parent: PyCon US 2024
type: Video Note
description: "In this tutorial, Russell Keith McGee introduces Beeware, a suite of open-source tools for building native GUI applications in Python, focusing on the Briefcase packaging tool and the Toga GUI tool..."
resource: "https://www.youtube.com/watch?v=New2JLvWxiE"
youtube_stats:
  view_count: 4212
  like_count: 92
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

In this tutorial, Russell Keith McGee introduces Beeware, a suite of open-source tools for building native GUI applications in Python, focusing on the Briefcase packaging tool and the Toga GUI toolkit.
The session guides participants through the complete lifecycle of a cross-platform application, starting with creating a virtual environment and using the `briefcase new` wizard to bootstrap a project with Toga.
Attendees learn to configure the `pyproject.toml` file, run the app in development mode, and package it for distribution as native desktop installers for Windows, macOS, and Linux.
The tutorial further demonstrates how to deploy the same Python codebase to mobile devices (iOS and Android), the web via WebAssembly, and the terminal using the Textual backend, highlighting the flexibility of the Beeware ecosystem.
Key technical concepts include managing dependencies with `briefcase run -r`, handling asynchronous operations to prevent UI freezing, and integrating third-party libraries like `httpx` and `numpy`.
The presentation also covers customizing app icons, declaring device permissions for hardware access like cameras, and running test suites on different platforms.
By emphasizing that Beeware apps are standard Python code, the tutorial encourages developers to leverage existing Python knowledge while utilizing native OS features for a seamless user experience across all supported platforms.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session introduces Beeware, a suite of open-source tools for building native GUI applications in Python across desktop, mobile, web, and console platforms.                    |
|   2 | Briefcase is a packaging tool that bundles Python code, dependencies, and an interpreter into standalone installers for Windows, macOS, Linux, iOS, and Android.                   |
|   3 | Toga is a cross-platform GUI toolkit designed with Python idioms, ensuring apps use native OS widgets and adhere to platform-specific UI guidelines.                               |
|   4 | The tutorial demonstrates creating a new project using the `briefcase new` wizard, which generates a `pyproject.toml` configuration file and a basic Toga application.             |
|   5 | Developers can run applications in development mode using `briefcase dev` to iterate on code within a local virtual environment.                                                   |
|   6 | The `briefcase create` command generates a platform-specific application template, while `briefcase build` compiles the app and `briefcase run` executes the packaged version.     |
|   7 | Briefcase package` creates distributable artifacts such as MSI, DMG, or system packages, allowing end users to install the app without needing a Python environment.               |
|   8 | The same source code can be deployed to iOS and Android simulators by appending the target platform to briefcase commands, such as `briefcase run ios`.                            |
|   9 | Web deployment is achieved by running `briefcase run web`, which uses PyScript to execute Python code in the browser via WebAssembly.                                              |
|  10 | Console applications can be created by installing the `toga-textual` backend and setting the `TOGA_BACKEND` environment variable to `toga.textual`.                                |
|  11 | Adding third-party libraries like `httpx` requires declaring them in the `requires` section of `pyproject.toml` and using `briefcase run -r` to install them into the app bundle.  |
|  12 | Asynchronous programming is essential in Toga to prevent UI freezing; event handlers should use `async def` and `await` for blocking operations like network requests or sleeps.   |
|  13 | Binary wheels for mobile platforms are not available on standard PyPI; Beeware maintains private repositories with pre-compiled wheels for packages like NumPy and Pandas.         |
|  14 | Customizing app icons involves adding an `icon` key to the configuration and providing a set of platform-specific image files in an `icons` directory.                             |
|  15 | Device hardware access, such as the camera, requires declaring permissions in `pyproject.toml` and using asynchronous Toga APIs to request access and capture images.              |
|  16 | Testing can be performed in both development and packaged environments using `briefcase dev --test` or `briefcase run --test` to validate code on simulators or devices.           |
|  17 | Beeware is not an Anaconda product but an independent open-source project, with Anaconda providing financial support and employing developers to work on it full-time.             |
|  18 | The build directory is considered ephemeral and should be treated as disposable; significant configuration changes often require deleting the build folder and recreating the app. |
|  19 | For advanced native API access beyond Toga's scope, developers can use libraries like Rubicon-ObjC, PyObjC, or Chaquopy to call platform-specific functions directly.              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/New2JLvWxiE/hqdefault.jpg)](https://www.youtube.com/watch?v=New2JLvWxiE)

[Watch on YouTube](https://www.youtube.com/watch?v=New2JLvWxiE)
