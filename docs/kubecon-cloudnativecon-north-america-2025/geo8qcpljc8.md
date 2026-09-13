---
type: Video Note
title: "Using Buildpacks To Boost Developer Productivity - Joe Kutner, Salesforce & Joey Brown, Heroku"
description: "In this talk, Joey Brown and Joe Cutner discuss how standardizing application builds with cloud native buildpacks can significantly boost developer productivity. They explain that buildpacks automate the process of packaging source code int..."
resource: https://www.youtube.com/watch?v=GeO8qCPlJC8
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Joey Brown and Joe Cutner discuss how standardizing application builds with cloud native buildpacks can significantly boost developer productivity.
They explain that buildpacks automate the process of packaging source code into container images, allowing developers to focus on writing application code rather than managing complex build instructions or system dependencies, as is often required with Dockerfiles.
Buildpacks provide modularity and logical mapping of components to image layers, enabling efficient caching and simplifying updates through features like rebase, which allows base image updates without full rebuilds.
While buildpacks impose some constraints compared to Dockerfiles, they restore the separation of concerns between platform engineers and application developers, promoting specialization and reducing the operational burden on developers.
The speakers emphasize that standardization through buildpacks benefits both platform engineers and developers by streamlining workflows, improving security, and enabling more consistent, maintainable application builds.
# Main Points

|   # | Main point                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------- |
|   1 | Buildpacks standardize application builds, improving productivity at build and runtime.                   |
|   2 | Heroku leverages buildpacks to build hundreds of thousands of apps daily.                                 |
|   3 | Cloud Native Buildpacks inspect source code and package it into runnable images.                          |
|   4 | Buildpacks abstract away the need for developers to write detailed build instructions.                    |
|   5 | Components are logically mapped to image layers, enabling modularity and organization.                    |
|   6 | Many vendors and platforms (Salesforce, Google Cloud, Heroku) have adopted buildpacks.                    |
|   7 | Platform engineers must implement buildpack support before developers can use them.                       |
|   8 | Dockerfiles offer autonomy but require developers to manage base OS, packages, and lack modularity.       |
|   9 | Buildpacks allow developers to focus on application code, not infrastructure.                             |
|  10 | Multiple adoption options: KPAC (Kubernetes), pack CLI, Jenkins, GitHub Actions, Tecton, Spring Boot.     |
|  11 | Off-the-shelf buildpacks are available from Heroku, Paketo, and Google.                                   |
|  12 | Inline buildpacks provide developer autonomy similar to Dockerfiles via project.toml configuration.       |
|  13 | Inline buildpacks can be written as scripts in project.toml, supporting custom build steps.               |
|  14 | The pack CLI builds images using buildpacks, producing standard OCI/Docker images.                        |
|  15 | Buildpacks support metadata inspection and image composition with multiple buildpacks.                    |
|  16 | Rebasing allows updating base images without rebuilding application layers.                               |
|  17 | Buildpacks provide efficient, logical caching, reducing developer effort for optimized builds.            |
|  18 | Logical mapping of layers enables fast security updates via rebase, minimizing developer disruption.      |
|  19 | Buildpacks impose some constraints (e.g., no root access), but simplify and optimize app image builds.    |
|  20 | Standardization via buildpacks restores separation of concerns between developers and platform engineers. |
|  21 | Standardization boosts productivity for both platform engineers and application developers.               |
|  22 | Buildpacks reduce the need for developers to manage system-level concerns, lettin                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GeO8qCPlJC8)