---
layout: default
title: "Talks - Russell Keith-Magee: Build a data visualization app for your phone"
nav_order: 148
parent: PyCon US 2024
type: Video Note
description: "Russell Keith McGee presents a tutorial on building and deploying a native mobile data visualization app for iOS and Android using only Python, leveraging the BeeWare open-source suite."
resource: "https://www.youtube.com/watch?v=NAANl5uj9ZM"
youtube_stats:
  view_count: 453
  like_count: 7
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

Russell Keith McGee presents a tutorial on building and deploying a native mobile data visualization app for iOS and Android using only Python, leveraging the BeeWare open-source suite.
The demonstration utilizes Toga, a cross-platform GUI toolkit that provides native user interfaces and widgets, and Briefcase, a packaging tool that compiles Python code into standalone applications without requiring end users to have Python installed.
The session walks through creating a simple app that generates random data with NumPy and visualizes it using Matplotlib, incorporating interactive sliders and buttons to adjust parameters.
McGee details the development workflow, including using `briefcase dev` for local iteration and `briefcase create`, `build`, and `run` commands to compile and test the app on iOS and Android emulators.
He also addresses technical considerations such as managing binary dependencies, handling device permissions, and the recent official support for iOS and Android as Tier 3 platforms in Python 3.13, while noting limitations regarding large AI models and specific complex libraries like SciPy.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces building a data visualization app for iOS and Android using only Python via the BeeWare suite.                            |
|   2 | BeeWare is a collection of open-source tools for creating native user interfaces in Python for desktop, mobile, and web platforms.                    |
|   3 | Toga is BeeWare's cross-platform GUI toolkit that allows a single codebase to target multiple platforms with native widgets and capabilities.         |
|   4 | Briefcase is a packaging tool that wraps Python code into standalone applications for end users without requiring Python installation.                |
|   5 | The demo app uses NumPy to generate random data and Matplotlib to render a histogram with interactive sliders for mean and standard deviation.        |
|   6 | Briefcase provides a wizard to bootstrap new projects, generating configuration files and app templates for selected GUI frameworks like Toga.        |
|   7 | The project configuration is managed in pyproject.toml, where app-specific settings override project-level defaults for most parameters.              |
|   8 | Sources, requires, test sources, and test requires are cumulative settings that append to project-level definitions rather than overriding them.      |
|   9 | Platform-specific configurations for iOS and Android can be defined to include unique dependencies or settings for those builds.                      |
|  10 | The app logic is implemented in app.py, utilizing Toga widgets such as boxes, sliders, buttons, and the Toga Chart widget for Matplotlib rendering.   |
|  11 | Event handlers are used to update data and redraw the chart when sliders change or the regenerate button is pressed.                                  |
|  12 | Briefcase Dev mode allows for rapid local iteration by installing dependencies and running the app in a local virtual environment.                    |
|  13 | Deploying to iOS requires Xcode, which Briefcase checks for, and involves creating an application template with a Python support package.             |
|  14 | Briefcase installs application code and dependencies into the application template to create a standalone build independent of the local environment. |
|  15 | The build process compiles the generated Xcode project, signing and packaging binary modules for the target device.                                   |
|  16 | Running the app on the iOS simulator displays native iOS widgets that adapt to screen orientation and size changes.                                   |
|  17 | Android deployment follows a similar process but allows Briefcase to manage the download of Android Studio command-line tools if missing.             |
|  18 | Android emulators can be created via a Briefcase wizard, and physical devices can be targeted via USB with debugging enabled.                         |
|  19 | Briefcase supports updating existing builds with new code or dependencies without recreating the entire project template.                             |
|  20 | The generated apps are standalone installers for desktop platforms and native bundles for mobile, requiring no Python knowledge from the user.        |
|  21 | Pure Python packages work easily on mobile, but binary packages require specific wheels built for iOS and Android, which BeeWare maintains.           |
|  22 | Some complex packages like SciPy and OpenCV are currently unavailable for mobile due to compilation challenges such as missing Fortran compilers.     |
|  23 | Toga provides APIs for accessing device sensors like cameras and GPS, with Briefcase handling cross-platform permission requests.                     |
|  24 | PEP 730 and PEP 738 propose adding iOS and Android as tier-three supported platforms in Python 3.13, enhancing official support.                      |
|  25 | Future work focuses on improving the packaging ecosystem to allow easier building of iOS and Android wheels for the broader community.                |
|  26 | Large AI models face size constraints on mobile app stores, often necessitating API-based access or on-device model optimizations.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NAANl5uj9ZM/hqdefault.jpg)](https://www.youtube.com/watch?v=NAANl5uj9ZM)

[Watch on YouTube](https://www.youtube.com/watch?v=NAANl5uj9ZM)
