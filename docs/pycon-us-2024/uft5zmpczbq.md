---
layout: default
title: "Talks - Sarah Kaiser: Eternal sunshine of the spotless development environment"
nav_order: 172
parent: PyCon US 2024
type: Video Note
description: "Sarah Kaiser, a Cloud Developer Advocate at Microsoft, presented a session at PyCon on the use of Dev Containers to streamline development environments."
resource: "https://www.youtube.com/watch?v=UFt5zmpCzBQ"
youtube_stats:
  view_count: 300
  like_count: 3
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

Sarah Kaiser, a Cloud Developer Advocate at Microsoft, presented a session at PyCon on the use of Dev Containers to streamline development environments.
She explained that Dev Containers are an open standard that extends Docker by specifying the entire development environment, including code, editor settings, and extensions, to ensure consistency across different machines and tools.
The talk highlighted how this technology solves common collaboration issues, such as "it works on my machine," by allowing developers to share reproducible environments for debugging and open-source contributions.
Kaiser demonstrated practical applications, including using GitHub Codespaces to launch pre-built environments directly from a browser, which serves as a reliable fallback for workshops and teaching scenarios where local setup can be difficult.
She concluded by emphasizing that Dev Containers enhance collaboration, simplify bug reproduction, and make it easier for educators to provide a uniform setup for students, ultimately making the development process more efficient and accessible.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk introduces Dev Containers, an open standard that specifies a complete development environment to solve the "it works on my machine" problem.                         |
|   2 | Unlike standard Docker containers which focus on code execution, Dev Containers include specifications for the editor, tools, and environment surrounding the code.           |
|   3 | The specification is supported by multiple tools including Visual Studio Code, PyCharm, Devbox, and Jiffy, allowing for portable development setups across different editors. |
|   4 | A Dev Container configuration is typically a JSON file that can reference a Dockerfile, Docker Compose files, or pre-made templates from the containers.dev project.          |
|   5 | Features allow users to add specific tools like Azure CLI or AWS CLI to the environment without modifying the main project Dockerfile, though this may slow down builds.      |
|   6 | The customization section of the configuration ensures that editor settings, extensions, and paths are consistent for all users opening the project.                          |
|   7 | Dev Containers are highly beneficial for open source collaboration by providing a reproducible environment for debugging and onboarding new contributors.                     |
|   8 | GitHub Codespaces integrates with Dev Containers, allowing users to launch a pre-configured development environment directly from a browser with free monthly hours.          |
|   9 | For teaching and workshops, Dev Containers serve as a reliable fallback to ensure all students have the exact same setup, reducing time spent on installation issues.         |
|  10 | Prebuilds can be configured in GitHub repository settings to cache the container image, significantly reducing launch times for Codespaces.                                   |
|  11 | Visual Studio Code Live Share can be used in conjunction with Dev Containers to allow multiple users to collaborate in real-time within the same isolated environment.        |
|  12 | A case study with NumPy demonstrated that Dev Containers successfully replaced unmanageable tools for their monthly newcomer sprints, improving the contributor experience.   |
|  13 | The presentation included a live demo showing the launch of a Dev Container via GitHub Codespaces after a local Docker failure, highlighting the cloud-based reliability.     |
|  14 | Users can choose different frontends, such as JupyterLab, when launching Dev Containers through Codespaces to suit specific project needs.                                    |
|  15 | Dev Containers merge with local user settings, allowing for personalized preferences while maintaining the core project environment consistency.                              |
|  16 | The speaker concluded that Dev Containers speed up collaboration, simplify bug reproduction, and make teaching easier by standardizing the development setup.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UFt5zmpCzBQ/hqdefault.jpg)](https://www.youtube.com/watch?v=UFt5zmpCzBQ)

[Watch on YouTube](https://www.youtube.com/watch?v=UFt5zmpCzBQ)
