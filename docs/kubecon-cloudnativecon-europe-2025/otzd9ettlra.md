---
layout: default
title:
  "Beyond the Limits: Scaling Kubernetes Controllers Horizontally - Tim Ebert,
  STACKIT"
nav_order: 27
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker discusses how Kubernetes controllers are not scalable horizontally
  due to leader election, which prevents multiple instances from reconciling objects
  simultaneously. To address this, they introduce a sharding mechanism that appl...
resource: https://www.youtube.com/watch?v=OTzd9eTtLRA
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

The speaker discusses how Kubernetes controllers are not scalable horizontally due to leader election, which prevents multiple instances from reconciling objects simultaneously.
To address this, they introduce a sharding mechanism that applies consistent hashing principles to distribute objects across multiple controller instances.
This design allows for horizontal scalability, with the capacity of the system increasing linearly with each added instance.
The speaker has implemented and tested this solution in their master's thesis and is now sharing it with the audience, providing reusable components and guidance on how to integrate sharding into existing controllers.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OTzd9eTtLRA)
