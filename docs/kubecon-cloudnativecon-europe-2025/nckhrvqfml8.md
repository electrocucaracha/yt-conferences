---
layout: default
title: Reliable K8s Resource Submission & Bookkeeping - Tiancheng Yin & Yao Lin, Bloomberg
nav_order: 282
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker, Yaoin, introduces themselves as part of the workflow orchestration
  team at Bloomberg, working with Kubernetes-based platforms. They discuss the importance
  of data center resiliency and high availability in their platform, which...
resource: https://www.youtube.com/watch?v=NCkHrvqFMl8
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

The speaker, Yaoin, introduces themselves as part of the workflow orchestration team at Bloomberg, working with Kubernetes-based platforms.
They discuss the importance of data center resiliency and high availability in their platform, which executes user-run workloads for various use cases such as machine learning pipelines and financial analysis.
To address these challenges, they propose a solution that separates API and submitter logic, using a message stream to handle complex logic like retries and deadline verification.
The system also includes a syncing service for deployables and a consumer service for post-deployment status tracking, ensuring consistency and disaster recovery across clusters.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=NCkHrvqFMl8)
