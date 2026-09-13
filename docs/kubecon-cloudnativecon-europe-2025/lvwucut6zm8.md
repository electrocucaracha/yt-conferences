---
layout: default
title: The Great Sidecar Debate - William Morgan, Buoyant
nav_order: 335
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker, William Morgan, CEO of Buoyant, discusses the concept of
  sidecars in service meshes, particularly in relation to Linkerd. He explains that
  a sidecar is a pattern where a container runs alongside an application container,
  sharing.
resource: https://www.youtube.com/watch?v=lVWUCUt6ZM8
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

The speaker, William Morgan, CEO of Buoyant, discusses the concept of sidecars in service meshes, particularly in relation to Linkerd.
He explains that a sidecar is a pattern where a container runs alongside an application container, sharing the same network space and file system, but isolated from each other.
Sidecars have both benefits, such as adding functionality without changing the application, and drawbacks, like potential performance issues if the sidecar is large or if pods are immutable.
The speaker also compares sidecars to node proxies and ambient, highlighting that while ambient offers more flexibility in terms of proxy placement, it also introduces operational complexity and potential trade-offs in terms of performance and resource usage.
Ultimately, Linkerd continues to favor sidecars as the most suitable approach for its users.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lVWUCUt6ZM8)
