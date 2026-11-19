---
layout: default
title: "Does Your Project Want a UI in Kubernetes-SIGs/headlamp? - René Dudfield & Santhosh Nagaraj"
nav_order: 2
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Headlamp, now part of the Kubernetes SIG UI, is a vendor-agnostic, multi-cluster user interface designed to simplify the management of Kubernetes and the broader CNCF ecosystem."
resource: "https://www.youtube.com/watch?v=6bIpFX1DlXs"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Headlamp, now part of the Kubernetes SIG UI, is a vendor-agnostic, multi-cluster user interface designed to simplify the management of Kubernetes and the broader CNCF ecosystem.
The tool offers a rich, modern UI with features such as real-time resource mapping, search capabilities, and read-only access options, while supporting deployment via web, in-cluster, or as a desktop application for various operating systems.
A key focus of the project is extensibility, allowing CNCF projects and enterprises to integrate custom plugins, brand the interface, and hook into specific extension points like metrics and resource views without maintaining separate UI infrastructure.
The Headlamp team actively collaborates with project maintainers to reduce development friction, improve accessibility, and ensure that UI extensions accurately reflect how users interact with complex projects, such as Cluster API and HolmesGPT.
By centralizing these efforts and leveraging the Linux Foundation mentorship program, Headlamp aims to provide a consistent, low-friction user experience for a wide range of cloud-native tools, inviting new projects to join their ongoing development cycle.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Headlamp is a rich, modern, and vendor-agnostic user interface for Kubernetes and the CNCF ecosystem, now part of the Kubernetes SIG UI.                                              |
|   2 | The tool supports multicluster environments, real-time updates, and read-only modes, enhancing discoverability through resource maps and object links.                                |
|   3 | Headlamp is deployable as an in-cluster web view or as a desktop application for Mac, Windows, and Linux, with availability in Docker Desktop, Backstage, and major package managers. |
|   4 | The platform is highly extensible, allowing CNCF projects to integrate extensions and companies to customize branding, themes, and logos for internal developer platforms.            |
|   5 | Extension points enable projects like Carpenter to hook into metrics integration and resource maps, displaying relevant data in relation to other Kubernetes objects.                 |
|   6 | Providing a UI reduces user friction, lowers support loads, and helps users discover and correctly utilize project features from the start.                                           |
|   7 | Collaboration with project maintainers is essential to identify useful CRDs, understand user workflows, and distinguish between development, debugging, and obsolete resources.       |
|   8 | Headlamp centralizes UI maintenance, reducing the burden on individual projects to manage separate UIs, certificates, and package distributions.                                      |
|   9 | Current collaborations include the Cluster API plugin, which retains support for older APIs based on maintainer feedback regarding continued user reliance.                           |
|  10 | Other active integrations include Holmes GPT, Radius, and various other CNCF projects, with a focus on projects that have available collaborators.                                    |
|  11 | The team conducts user research and accessibility improvements, utilizing professional testers and translators to enhance the user experience.                                        |
|  12 | Integration is often simplified by leveraging existing CRDs and schemas, though the plugin system also supports CLIs and other APIs like Prometheus.                                  |
|  13 | Headlamp is seeking five new projects for the next cycle and aligns with the Linux Foundation mentorship program to support plugin development.                                       |
|  14 | The onboarding process begins with a proposal defining priority resource types and user jobs, followed by initial releases and iterative feedback loops.                              |
|  15 | The plugin system is built on TypeScript, allowing for extensive customization beyond CRDs, including support for custom API servers and diverse integration methods.                 |
|  16 | Multi-tenancy is supported through namespace-based projects, virtual clusters, and label filtering, allowing teams to access specific resources within a shared cluster.              |
|  17 | Users with role-based access control can create new namespaces or apply labels dynamically, enabling flexible and secure resource management within the UI.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6bIpFX1DlXs/hqdefault.jpg)](https://www.youtube.com/watch?v=6bIpFX1DlXs)

[Watch on YouTube](https://www.youtube.com/watch?v=6bIpFX1DlXs)
