---
layout: default
title:
  Image Snapshotters for Efficient Container Execution in Particle P... Clemens
  Lange & Valentin Volkl
nav_order: 130
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The video discusses image snapshoters, specifically lazy pulling snapshoters,
  which enable efficient data access and reduce the amount of data downloaded from
  registries. The three main snapshoters explored are Starg, Sochi, and CVMFS. These...
resource: https://www.youtube.com/watch?v=Dc6S4vU9GiM
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

The video discusses image snapshoters, specifically lazy pulling snapshoters, which enable efficient data access and reduce the amount of data downloaded from registries.
The three main snapshoters explored are Starg, Sochi, and CVMFS.
These snapshoters work as plugins to containerd and offer various advantages, including almost instantaneous start times and significant reductions in data download.
However, they may struggle with large numbers of small files or specific use cases that require precise control over file access.
The CVMFS snapshot, which uses a separate index artifact, addresses this issue by chunking files in a configurable size.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Dc6S4vU9GiM)
