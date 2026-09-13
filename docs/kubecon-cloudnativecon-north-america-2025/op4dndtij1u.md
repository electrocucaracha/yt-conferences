---
layout: default
title:
  DRA is GA! Kubernetes WG Device Management - GPUs, TPUs, NICs and More... Kevin
  Klues & Patrick Ohly
nav_order: 49
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The CubeCon North America update meeting for the Kubernetes Device Management
  Working Group focused on recent progress in dynamic resource allocation (DRA), a
  feature now generally available in Kubernetes 1.34. DRA replaces device plugins
  w...
resource: https://www.youtube.com/watch?v=Op4DNDTij1U
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The CubeCon North America update meeting for the Kubernetes Device Management Working Group focused on recent progress in dynamic resource allocation (DRA), a feature now generally available in Kubernetes 1.34.
DRA replaces device plugins with a more flexible system for describing, requesting, and allocating hardware resources—such as GPUs, CPUs, and network devices—using resource claims and attributes, enabling advanced scheduling and configuration options.
The group highlighted new features like easier migration from device plugins, binding conditions for dynamic allocation, and consumable capacity for improved device sharing, as well as the growing ecosystem of DRA drivers and integrations, including support for CPUs, high-performance networking (DRET), and KubeVirt.
Community contributions and participation were encouraged, with resources available for developing new drivers and regular meetings for collaboration.
The Q&A addressed practical concerns about cluster topologies, scheduler compatibility, autoscaling support, and driver development, emphasizing that DRA is designed to work with standard Kubernetes components and is evolving to support more advanced use cases.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CubeCon North America update meeting for the Kubernetes Device Management Working Group focused on dynamic resource allocation (DRA)                                  |
|   2 | DRA is now generally available (GA) in Kubernetes 1.34                                                                                                                |
|   3 | DRA replaces device plugins, offering more flexible and expressive hardware descriptions via resource slices and resource claims                                      |
|   4 | Users can request devices with specific attributes and configuration parameters                                                                                       |
|   5 | Resource claims can be shared between multiple pods and containers                                                                                                    |
|   6 | DRA supports a variety of hardware, including GPUs, network devices, and now CPUs                                                                                     |
|   7 | Migration from traditional device plugins to DRA is supported; workloads can use either API                                                                           |
|   8 | Only one mechanism (device plugin or DRA driver) can provide a hardware type per node                                                                                 |
|   9 | New features include binding conditions (blocking pod binding until allocation is ready) and consumable capacity (dynamic device sharing until capacity is exhausted) |
|  10 | Several new and improved features are targeted for graduation in Kubernetes 1.36                                                                                      |
|  11 | New contributors have driven features like consumable capacity, extended resources, and dynamic device attachment                                                     |
|  12 | Community engagement has increased, with more companies presenting DRA-related talks at CubeCon                                                                       |
|  13 | New DRA drivers: CPU driver (alpha), DRET for high-performance networking (GA), integration with KubeVirt (alpha), and Q integration for quotas                       |
|  14 | DRA enables alignment of CPUs, GPUs, and NICs for performance optimization                                                                                            |
|  15 | Example DRA driver and Go helper package available for third-party driver development                                                                                 |
|  16 | DRA works with mixed clusters (CPU-only and GPU nodes)                                                                                                                |
|  17 | DRA is part of the standard Kubernetes scheduler from 1.34 onward; features are enabled via feature gates                                                             |
|  18 | Cluster autoscaling is supported; integration with cloud vendor-specific autoscalers varies                                                                           |
|  19 | Weekly meetings and active Slack channel for community support and collaboration                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Op4DNDTij1U)
