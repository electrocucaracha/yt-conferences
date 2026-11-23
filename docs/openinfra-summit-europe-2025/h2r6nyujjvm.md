---
layout: default
title: "Multi-Arch OpenStack in Production: ARM64/x86 Bare Metal and Hypervisors with Kolla-Ansible"
nav_order: 48
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Nathan Harle from Graphcore and his colleague from StackHPC presented their collaborative effort to integrate ARM64 systems into their existing x86-focused OpenStack cloud, which previously treated..."
resource: "https://www.youtube.com/watch?v=H2r6nyujjvM"
youtube_stats:
  view_count: 157
  like_count: 3
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

Nathan Harle from Graphcore and his colleague from StackHPC presented their collaborative effort to integrate ARM64 systems into their existing x86-focused OpenStack cloud, which previously treated ARM hardware as separate, manually managed "second-class citizens." To achieve this, they utilized the Kolla project to build multi-architecture container images, overcoming upstream maintenance gaps and technical hurdles such as missing ARM64 support for certain components and the need for multi-arch manifests to unify image tags across architectures.
The team implemented cross-architecture builds using QEMU emulation initially, later transitioning to bare-metal ARM64 hardware for faster build times, while also fixing critical Ironic and PXE boot configurations to ensure proper provisioning of mixed-architecture nodes.
Graphcore’s primary goal was to establish feature parity between their x86 and ARM64 fleets, ensuring that performance-critical features like SR-IOV and VF-Lag, as well as internal developer tools, were fully supported on the new ARM64 hypervisors.
Key operational tips included explicitly setting the architecture in image names and metadata to avoid confusion, and extending all internal image build pipelines to support both architectures simultaneously, thereby streamlining the development experience for their internal users.

# Main Points

|   # | Main point                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Graphcore and StackHPC collaborated to integrate ARM64 systems into their existing x86-focused OpenStack cloud to eliminate the separation of ARM hardware as second-class citizens.                                        |
|   2 | The project utilizes the Kolla project, which includes Kolla for building container images, Kolla-ansible for deployment and lifecycle management, and Kolla-on-Bifrost for bare-metal provisioning.                        |
|   3 | Initial upstream support for ARM64 was unmaintained and lacked multi-arch manifests, requiring the team to implement fixes for missing components like Heirlang on Red Hat-based systems using Fedora COPR.                 |
|   4 | A critical bug was identified where Prometheus and other components were incorrectly built for x86 within ARM64 containers, necessitating upstream fixes and improved CI testing.                                           |
|   5 | The team developed a multi-arch image build workflow in their open-source Release Train project to generate common tags for both ARM64 and x86 images using Docker manifest creation.                                       |
|   6 | Cross-architecture builds were initially used for speed but were slower than native builds; the team eventually switched to native bare-metal ARM64 builds which proved faster than x86 builds in virtualized environments. |
|   7 | Deployment challenges included fixing PXE boot configurations in Ironic to point to the correct architecture-specific binaries and inspector images for ARM64 hosts.                                                        |
|   8 | Graphcore aimed for feature parity between x86 and ARM64 fleets, ensuring support for SR-IOV, VF lag, and bare-metal capabilities on ARM systems.                                                                           |
|   9 | Operational tips include explicitly setting the architecture on all resources, including architecture in image names for clarity, and extending Packer pipelines to build workload images for both architectures.           |
|  10 | The team plans to explore virtual media solutions based on DMC mounting and continues to work on upstream patches for CI/CD improvements in the Bifrost component.                                                          |
|  11 | Upstream CI for ARM64 was limited to 20 VMs with poor I/O performance, prompting the team to advocate for better hardware donations to the OpenStack community.                                                             |
|  12 | The project emphasizes that all tools and workflows, including the Release Train and multi-arch build scripts, are open source and available for community use.                                                             |
|  13 | Future steps include discussing the integration of Podman and BuildKit support upstream to streamline multi-arch image building processes.                                                                                  |
|  14 | The team encourages participation in Kolla workshops, Release Train sessions, and user forums at the summit to gather input on future development cycles.                                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/H2r6nyujjvM/hqdefault.jpg)](https://www.youtube.com/watch?v=H2r6nyujjvM)

[Watch on YouTube](https://www.youtube.com/watch?v=H2r6nyujjvM)
