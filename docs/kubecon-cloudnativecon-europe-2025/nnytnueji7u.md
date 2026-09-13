---
layout: default
title:
  "Tutorial: Workshop: Developing as a Team for Kubernetes With Nix an... Leigh
  Capili & Tanja Ulianova"
nav_order: 354
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker is discussing the Nyx package manager, which allows for declarative
  software builds in a hermetic way. They introduce Flux, an open-source project that
  uses Nyx to create reproducible environments for development and deployment...
resource: https://www.youtube.com/watch?v=NnYtnUeJi7U
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker is discussing the Nyx package manager, which allows for declarative software builds in a hermetic way.
They introduce Flux, an open-source project that uses Nyx to create reproducible environments for development and deployment.
The speaker demonstrates how to use Flux to build a Go application with Postgres database, showcasing the benefits of using Nyx and Flux for collaborative development and deployment.
They also discuss the importance of GitOps and shifting it left to include machine management, highlighting the potential for Flux to automate infrastructure updates and ensure consistent versions across teams.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | GitOps is a collaboration platform that enables declarative changes to infrastructure and applications.                            |
|   2 | Flux is an open-source project that provides a usability layer on top of Nyx, making it easier to use and collaborate with others. |
|   3 | Flocks is a tool that helps manage environments and dependencies for Nyx-based projects.                                           |
|   4 | The speaker uses Flux and Flocks to create a reproducible environment for their Go application.                                    |
|   5 | They demonstrate how to containerize the application using Docker and Nyx packages.                                                |
|   6 | The speaker talks about the benefits of using GitOps, including declarative changes and version locking.                           |
|   7 | They discuss the importance of shifting GitOps left to include development environments and collaboration platforms.               |
|   8 | The speaker showcases a new feature in Flux that allows for auto-updating of flux instances with a tagged release scheme.          |
|   9 | They demonstrate how to use this feature to manage flux instances and create a namespace for their app.                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=NnYtnUeJi7U)
