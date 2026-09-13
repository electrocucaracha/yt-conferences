---
type: Video Note
title: "Mastering Efficiency in Argo CD: Scaling Smarter, Not Costlier - Alexander Matyushentsev, Akuity"
description: "The speaker discusses the cost of running Argo CD at scale, highlighting that while it's initially free, costs can add up when managing multiple clusters and applications. They share lessons learned from their experience, including optimizi..."
resource: https://www.youtube.com/watch?v=bpsclYlGl2s
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the cost of running Argo CD at scale, highlighting that while it's initially free, costs can add up when managing multiple clusters and applications.
They share lessons learned from their experience, including optimizing compute cost by reducing memory requests in the Radius configuration, enabling concurrent processing in Reposerver, and reusing a single Kubernetes cluster for multiple Argo CDs.
These optimizations resulted in significant savings, with estimates suggesting that running 100 Argo CD instances could save around $300 per day.
The speaker also emphasizes the importance of monitoring application resources and using features like Resource Exclusions to reduce unnecessary traffic.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=bpsclYlGl2s)