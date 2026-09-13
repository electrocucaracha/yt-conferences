---
layout: default
title:
  "Lightning Talk: Scaling To the Stars: Simulating Massive Clusters With KWOK
  - Soumya Balakrishnan"
nav_order: 183
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker discusses the use of Quark, a tool for simulating large-scale
  clusters on minimal resources, to help manage their large fleet of data centers.
  With 80 production clusters and 50 microservices per cluster, resource crunch is
  sign...
resource: https://www.youtube.com/watch?v=QmUVhzdlMII
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

The speaker discusses the use of Quark, a tool for simulating large-scale clusters on minimal resources, to help manage their large fleet of data centers.
With 80 production clusters and 50 microservices per cluster, resource crunch is significant.
The team initially developed a script to automate deployment but encountered out-of-memory issues when scaling up.
They then used Quark to simulate thousands of nodes, testing the script's functionality and scalability, which enabled them to implement caching, batch API calls, and reduce memory usage, ultimately achieving their goal of always building for scale.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QmUVhzdlMII)
