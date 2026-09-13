---
layout: default
title: The Next Generation of DaemonSet Autoscaling - Adam Bernot & Bryan Boreham
nav_order: 340
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=yQQU8vDhj0o
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

Here is a summary of the video transcript in 3-5 sentences: Adam Berno and Brian Borum from Google Cloud discuss how to optimize resource usage for Prometheus, a monitoring system that runs on Kubernetes.
They introduce the concept of "demon sets," which are groups of pods that run on every node in the cluster, and explain how the Vertical Pod Autoscaler (VPA) can be used to manage their resources.
The VPA uses a scope field to determine which nodes to consider when making recommendations, allowing for more efficient resource allocation.
By using the VPA with a customized scope, such as instance type or node pool, users can optimize resource usage and reduce wasted capacity.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yQQU8vDhj0o)
