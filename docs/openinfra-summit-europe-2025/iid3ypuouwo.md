---
layout: default
title: "So Long and Thanks for All the Nodes: New Tools for Managing Test Resources in Zuul"
nav_order: 74
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "James Blair, founder of the Zuul project, presented a talk on the deprecation of NodePool in favor of a new, integrated Zuul launcher service."
resource: "https://www.youtube.com/watch?v=IId3yPuouWo"
youtube_stats:
  view_count: 96
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

James Blair, founder of the Zuul project, presented a talk on the deprecation of NodePool in favor of a new, integrated Zuul launcher service.
The primary motivation for this transition is to align image management with Zuul’s Git-driven philosophy, moving configuration from static files to Git-managed jobs to improve visibility, testability, and self-service capabilities.
Under the new system, image builds are executed as standard Zuul jobs, allowing for speculative testing and gating, while a cooperative daemon handles the reliable upload of images to various cloud providers.
This architecture introduces new configuration concepts such as images, flavors, labels, sections, and providers, enabling more flexible and scalable resource management across heterogeneous environments.
The Zuul launcher also offers significant performance improvements, including cooperative horizontal scaling and the ability to fulfill requests using multiple provider types simultaneously.
Although the work is nearly complete and has been successfully piloted by OpenDev, the feature is currently behind flags and not yet recommended for general use, with a gradual transition path available for existing NodePool users.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | James Blair, founder of the Zuul project and Acme Gating, presented the transition from NodePool to the new Zuul Launcher.                                                                  |
|   2 | Zuul is a Git-driven CI/CD system that emphasizes testing changes as they will appear when merged, a concept known as gating.                                                               |
|   3 | NodePool, the oldest Zuul component, originally managed test resources via VMs in OpenStack but has expanded to support AWS, GCP, Azure, IBM Cloud, Kubernetes, and OpenShift.              |
|   4 | The NodePool builder uses diskimage-builder to create VM images, a process that predates Zuul itself and originated as a Jenkins job.                                                       |
|   5 | The primary motivation for replacing NodePool is to move configuration into Git, improving visibility, maintainability, and alignment with Zuul's Git-driven philosophy.                    |
|   6 | Image building will shift to Zuul jobs, allowing users to see build progress and integrate image builds into the gating pipeline to prevent broken images from merging.                     |
|   7 | Image uploads will remain handled by a daemon to ensure reliability, as clouds are unreliable and users do not need visibility into the upload process.                                     |
|   8 | A caching strategy for image builds uses a "snake eating its tail" approach, where the first built image contains the cache needed to build subsequent images efficiently.                  |
|   9 | The new Zuul Launcher is a cooperative service that allows horizontal scaling, unlike the standalone NodePool launchers which could conflict if multiple instances were run.                |
|  10 | Rendezvous hashing enables multiple Zuul Launchers to distribute work without direct communication, improving performance and allowing heterogeneous providers to fulfill a single request. |
|  11 | New Zuul configuration objects include images, flavors, labels, sections, and providers to support flexible resource management.                                                            |
|  12 | Labels combine an image and a flavor, defining the specific test resource type available to jobs.                                                                                           |
|  13 | Sections represent parts of a cloud, often mapping to regions, and support inheritance to manage complex cloud structures.                                                                  |
|  14 | Providers are responsible for launching and accounting for nodes, attaching labels to sections to make resources available.                                                                 |
|  15 | The transition allows NodePool and Zuul Launcher to coexist, with Zuul preferring its own labels and falling back to NodePool for others.                                                   |
|  16 | OpenDev has been running the new system for three months, transitioning labels gradually to ensure stability.                                                                               |
|  17 | The project is currently behind feature flags in the main line of development, with major configuration changes still in progress.                                                          |
|  18 | The static driver is the final major component to be finalized before broad community testing begins.                                                                                       |
|  19 | Backwards compatibility with NodePool is expected to be maintained for approximately one year to allow for a smooth migration.                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/IId3yPuouWo/hqdefault.jpg)](https://www.youtube.com/watch?v=IId3yPuouWo)

[Watch on YouTube](https://www.youtube.com/watch?v=IId3yPuouWo)
