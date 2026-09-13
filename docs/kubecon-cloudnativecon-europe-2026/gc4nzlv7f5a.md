---
type: Video Note
title: "Buildpacks: Towards 1.0, AI and Other Things - Aidan Delaney, Bloomberg"
description: "In this talk, Aiden, a maintainer of the Buildpacks project, introduces the audience to cloud native buildpacks, highlighting their role in transforming application source code into OCI images through a simple and repeatable process. He dem..."
resource: https://www.youtube.com/watch?v=Gc4NZlv7F5A
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Aiden, a maintainer of the Buildpacks project, introduces the audience to cloud native buildpacks, highlighting their role in transforming application source code into OCI images through a simple and repeatable process.
He demonstrates how buildpacks can be used to build both standard and machine learning applications, emphasizing that the workflow remains consistent regardless of complexity or language, and showcases a live demo using a Java application.
Aiden explains the benefits for both application developers, who can focus on code while infrastructure teams manage build logic and compliance through custom builders, and platform operators, who gain centralized control over base images, supported runtimes, and security updates.
He discusses recent and upcoming features, such as image extensions, multi-architecture support, and the move toward a stable 1.0 API, which promises long-term reliability and easier integration.
The talk concludes with an invitation to contribute to the open-source project and a Q&A covering topics like rapid base image rebasing for security and image signing practices.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter is Aiden, a build packs maintainer with 20 years of industry experience, mainly focused on documentation.                                          |
|   2 | Build packs project received the CNCF Laura Mipum award for documentation.                                                                                   |
|   3 | Bloomberg, Aiden’s employer, supports his work on build packs and is hiring globally.                                                                        |
|   4 | Talk covers the road to build packs 1.0 and AI/machine learning use cases.                                                                                   |
|   5 | Build packs process is the same for fast API apps and machine learning models.                                                                               |
|   6 | Live demo uses a Java application with a custom builder to illustrate build packs concepts.                                                                  |
|   7 | About half the audience has experience with cloud native build packs, up from 10% four years ago.                                                            |
|   8 | Build packs can be used via the pack CLI, Spring Boot’s build image feature, or the KPAC Kubernetes operator.                                                |
|   9 | Demo shows building a Java 25 machine learning app using pack build, resulting in a runnable OCI image.                                                      |
|  10 | Build packs transform source code into OCI images via a repeatable, multi-vendor process.                                                                    |
|  11 | Build packs are a CNCF incubating project; spec is maintained at buildpacks.io.                                                                              |
|  12 | Production-level build packs are provided by Heroku, Paketo, Google, or can be custom-built.                                                                 |
|  13 | Supported stacks include .NET, Python, Ruby, Java, PHP, TypeScript; build packs are interoperable.                                                           |
|  14 | Platform operators can create custom builders to control base images, supported languages, runtimes, and security policies.                                  |
|  15 | Custom builders centralize build logic, enable easy updates, and enforce compliance.                                                                         |
|  16 | AI/ML workloads require GPU drivers (e.g., CUDA), large frameworks, and reproducible environments; build packs can help manage this complexity.              |
|  17 | Build packs support multiple builders for different platforms and image extensions for advanced customization.                                               |
|  18 | Automatic base image updates (rebase) allow fast security patching without rebuilding applications.                                                          |
|  19 | Build packs 1.0 aims for stable APIs, removal of deprecated features, improved shell handling, multi-arch support, better error messages, and observability. |
|  20 | Build packs provide first-class SBOM and s                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Gc4NZlv7F5A)