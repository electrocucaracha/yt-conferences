---
layout: default
title:
  The GPUs on the Bus Go ‘Round and ‘Round - Natalie Bandel & Ryan Hallisey,
  NVIDIA
nav_order: 334
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker from NVIDIA discusses their experience with device failures
  in their Kubernetes clusters, particularly with GPUs falling off the bus. They share
  that they have 60,000+ GPUs, 30,000+ nodes, and 40+ clusters worldwide, experiencin...
resource: https://www.youtube.com/watch?v=cLJRh4y4vXg
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

The speaker from NVIDIA discusses their experience with device failures in their Kubernetes clusters, particularly with GPUs falling off the bus.
They share that they have 60,000+ GPUs, 30,000+ nodes, and 40+ clusters worldwide, experiencing between 120-200 GPU failures per 24-hour period.
To address this issue, they developed a custom GPU problem detector, node problem detector, and automated reboot process.
The speaker emphasizes the importance of monitoring GPU health, using node taints and tolerations to prevent scheduling workloads on unhealthy nodes, and prioritizing node maintenance.
They also propose starting a working group with Red Hat to explore how Kubernetes can help solve these challenges, particularly in device management for increasing GPU capacity per node.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cLJRh4y4vXg)
