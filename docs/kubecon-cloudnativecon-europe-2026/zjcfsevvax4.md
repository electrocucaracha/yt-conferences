---
type: Video Note
title: "Dragonfly V2.4.0 - Intro, Updates, Data Distribution in AI Infrastructure - Wenbo Qi & Chenyu Zhang"
description: "In this presentation, Gio, the maintainer of Dronefly, introduces the project as an efficient, stable, and secure P2P-powered solution for data distribution and acceleration, particularly suited for cloud-native architectures and large-scal..."
resource: https://www.youtube.com/watch?v=zjCFSEVvaX4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Gio, the maintainer of Dronefly, introduces the project as an efficient, stable, and secure P2P-powered solution for data distribution and acceleration, particularly suited for cloud-native architectures and large-scale clusters.
Dronefly supports rapid delivery of files, container images, AI models, and logs, and includes the Nydus subproject, which enables on-demand container image downloads and deduplication to reduce storage and memory costs.
The system offers three core image acceleration solutions and optimizes file distribution using P2P technology, supporting various protocols and object storage systems, and is increasingly focused on AI infrastructure for efficient model distribution.
Recent updates in version 2.4 include a new transfer protocol, improved scheduling, preheating enhancements, and deprecation of the Go client in favor of Rust, all aimed at reducing download times and preventing overloads.
Gio also demonstrates how Dronefly, integrated with Harbor and Kubernetes, streamlines AI model management and distribution, enabling versioning, access control, and efficient deployment, with ongoing plans to further optimize preheating, RDMA acceleration, lazy loading, and model security scanning.
# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Wimbu (Gio), maintainer of Dronefly                                                                                                                              |
|   2 | Dronefly delivers efficient, stable, and secure data distribution and acceleration using P2P technology                                                                     |
|   3 | Aims to be the standard solution in cloud native architectures                                                                                                              |
|   4 | Improves performance for large-scale cluster delivery of files, container images, OCI artifacts, AI models, cache, and logs                                                 |
|   5 | Two CNCF graduated projects in container registry landscape: Harbor (artifact registry) and Dronefly (image acceleration and file distribution)                             |
|   6 | Nydus is a subproject providing a file system based on RAFS format, enabling on-demand container image downloads and trunk-level deduplication                              |
|   7 | Nydus reduces container image launch time from minutes to seconds                                                                                                           |
|   8 | Dronefly focuses on image acceleration, file distribution, and AI infrastructure                                                                                            |
|   9 | Three image acceleration solutions: 1. Dronefly P2P for large-scale clusters 2. Dronefly + Nydus for faster container launching 3. Nydus alone for fast container launching |
|  10 | Supports HTTP, HDFS, S3, OSS, OBS protocols and object storage                                                                                                              |
|  11 | Accelerates data distribution for AI training and inference; supports Hugging Face model downloads                                                                          |
|  12 | P2P is considered the best solution for distributing AI data and models                                                                                                     |
|  13 | Three core download modes: from origin, from remote peer, from local peer                                                                                                   |
|  14 | Dronefly 2.4 introduces a new TLV-based transfer protocol, reducing large file download times compared to gRPC                                                              |
|  15 | Scheduling improvements: two-stage candidate parent selection, load quality scoring, bandwidth usage optimization                                                           |
|  16 | Optimizations to avoid root peer overloading and improve bandwidth usage                                                                                                    |
|  17 | Enhanced preheating: flexible by IP percentage/count, rate limiting to avoid origin overload                                                                                |
|  18 | Task ID now calculated by image block hash, preventing redundant downloads                                                                                                  |
|  19 | HTTP redirect response caching supported                                                                                                                                    |
|  20 | Go client deprecated, replaced by Rust client                                                                                                                               |
|  21 | AI model management: models as immutable, versioned OCI artifacts, managed in Harbor                                                                                        |
|  22 | Harbor provides versioning, RBAC, lifecycle management, sup                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zjCFSEVvaX4)