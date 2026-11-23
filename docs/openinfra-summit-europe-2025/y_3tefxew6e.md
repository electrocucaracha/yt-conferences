---
layout: default
title: "Podman Desktop: Streamlining Container Management for Open Infrastructure Development"
nav_order: 84
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Alex, a representative from Red Hat, presents Podman Desktop as a seamless, open-source tool designed to bridge the gap between local development and production environments."
resource: "https://www.youtube.com/watch?v=Y_3tefxEw6E"
youtube_stats:
  view_count: 81
  like_count: 2
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

Alex, a representative from Red Hat, presents Podman Desktop as a seamless, open-source tool designed to bridge the gap between local development and production environments.
He explains that Podman Desktop offers a graphical interface for building, running, and managing OCI containers and lightweight Kubernetes clusters, supporting multiple operating systems including Windows, macOS, and Linux.
During the live demonstration, Alex showcases how to easily create containers and pods, generate necessary YAML manifests, and deploy applications to local Kind clusters or single-node OpenShift instances with just a few clicks.
He highlights the tool’s ability to integrate with external production clusters and its extensive plugin ecosystem, which includes support for AI models and confidential containers.
The presentation concludes by emphasizing that Podman Desktop simplifies the workflow for developers, allowing them to test applications in a production-like environment on their laptops before migrating them to enterprise infrastructure.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Podman Desktop is a free, open-source, secure, Linux-native tool designed to find, run, build, share, and deploy OCI containers and images.                  |
|   2 | The tool addresses the gap between local development on a laptop and production deployment, ensuring applications work across the entire ecosystem.          |
|   3 | Podman Desktop supports Windows, macOS, and Linux, providing a GUI to create, build, manage, and debug containers, pods, and Kubernetes clusters.            |
|   4 | Users can install lightweight Kubernetes clusters such as Kind, MicroK8s, or single-node OpenShift directly on their laptops.                                |
|   5 | The platform includes plugins for Kind, Lima, Docker, OpenShift, AI, and internal registry storage to facilitate development.                                |
|   6 | Podman Desktop recently reached millions of downloads, highlighting its adoption in the developer community.                                                 |
|   7 | The dashboard allows users to manage pods, images, and storage, with options to prune, load, import, or pull images.                                         |
|   8 | Users can create bootable containers and access a catalog of open-source LLMs and SMLs for AI integration.                                                   |
|   9 | Creating a lightweight Kubernetes cluster, such as Kind, is simplified to a single button click without complex configuration files.                         |
|  10 | Containers can be created via the GUI by selecting an image, naming the container, and configuring ports and security parameters.                            |
|  11 | The interface provides logs, JSON specifications, and YAML configurations for containers to facilitate migration to Kubernetes.                              |
|  12 | Podman Compose can be used to create pods consisting of multiple containers, such as a Redis and HTTP container pair.                                        |
|  13 | Applications running locally can be migrated to a Kubernetes cluster using the "Point to Kubernetes" feature, which generates the necessary YAML manifests.  |
|  14 | Single-node OpenShift clusters can be provisioned as virtual machines on the host, emulating a production environment for testing.                           |
|  15 | On Linux, users can customize the system more easily, such as creating systemd files, compared to macOS where everything is virtualized.                     |
|  16 | Performance on Apple Silicon ARM-based Macs is optimized with native libraries, and the tool is primarily developed with macOS users in mind.                |
|  17 | Users can connect Podman Desktop to external Kubernetes or OpenShift clusters by selecting the available context in the dashboard.                           |
|  18 | The OpenShift dashboard can be accessed via the console URL, and the confidential containers operator can be installed for specific workloads.               |
|  19 | Podman Desktop allows users to manage namespaces, create pods, and deploy applications directly from the GUI without needing command-line tools.             |
|  20 | The tool supports integration with various container engines, including Docker, allowing users to migrate workloads to different Kubernetes infrastructures. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Y_3tefxEw6E/hqdefault.jpg)](https://www.youtube.com/watch?v=Y_3tefxEw6E)

[Watch on YouTube](https://www.youtube.com/watch?v=Y_3tefxEw6E)
