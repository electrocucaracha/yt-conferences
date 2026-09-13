---
layout: default
title:
  Optimizing Metrics Collection & Serving When Autoscaling LLM Workloads - Vincent
  Hou & Jiří Kremser
nav_order: 213
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker, Vincent Ho, discusses the challenges of autoscaling large
  language model workloads in Kubernetes. He explains that existing solutions often
  rely on CPU and memory metrics, which don't accurately reflect GPU usage. To address
  th...
resource: https://www.youtube.com/watch?v=lefjb4Vnd8k
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

The speaker, Vincent Ho, discusses the challenges of autoscaling large language model workloads in Kubernetes.
He explains that existing solutions often rely on CPU and memory metrics, which don't accurately reflect GPU usage.
To address this, he introduces Keta, an open-source project that allows for custom metric collection and serving.
The system uses Open Telemetry to collect metrics from the workload itself, and Hotel Add-on to process and scale the model based on those metrics.
A demo is shown, where a cluster is scaled up in response to increased load, using a stabilization window to ensure that nodes are not killed prematurely.
The speaker also discusses the importance of data locality and the use of machine deployments to manage scaling.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lefjb4Vnd8k)
