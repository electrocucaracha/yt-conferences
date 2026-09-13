---
layout: default
title:
  C.A.L.L.I.N.G. Now I'm Calling You, Calling You Now - Mario Macías & Terra
  Tauri, Grafana Labs
nav_order: 38
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker, Terara Tori, discusses the challenges of enriching Kubernetes
  eBPF data and introduces a solution called BA (BPF Agent). Initially, BA ran as
  a demo set on each node, but it caused issues when deployed in production due to
  high...
resource: https://www.youtube.com/watch?v=2BIhTXQd0CI
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

The speaker, Terara Tori, discusses the challenges of enriching Kubernetes eBPF data and introduces a solution called BA (BPF Agent).
Initially, BA ran as a demo set on each node, but it caused issues when deployed in production due to high API request rates.
To solve this, they introduced a centralized cache deployment, which reduces memory utilization and improves performance.
The cache instance acts as an intermediary between the Kubernetes API and the BA instances, providing a more efficient way to retrieve metadata.
This solution is designed to be scalable and maintainable, with options for users to manage it through Helm charts or other means.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2BIhTXQd0CI)
