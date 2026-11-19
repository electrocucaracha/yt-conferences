---
title:
  "Streamlined Efficiency: Unshackling Kubernetes Image Volumes for Rapid A...
  Esteban Rey & Yifan Yuan"
type: Video Note
description:
  The presentation discusses how to speed up loading of large data sets
  into Kubernetes clusters using image volumes from OCI registries. The current state
  of efficiency in starting up images has improved with artifact streaming, but packaging.
resource: https://www.youtube.com/watch?v=XqL5lh32lr8
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: "2026-09-12T00:00:00+00:00"
---

# Summary

The presentation discusses how to speed up loading of large data sets into Kubernetes clusters using image volumes from OCI registries.
The current state of efficiency in starting up images has improved with artifact streaming, but packaging and accessing large data sets remains a challenge.
To address this, the Enink solution is introduced, which creates a mount point for accessing remote data through OCI artifacts without repackaging them.
This allows for efficient loading of large data sets, including those with over 700,000 files, in under two minutes compared to four hours using traditional packaging methods.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XqL5lh32lr8/hqdefault.jpg)](https://www.youtube.com/watch?v=XqL5lh32lr8)

[Watch on YouTube](https://www.youtube.com/watch?v=XqL5lh32lr8)
