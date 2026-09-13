---
layout: default
title: "Keynote: Live Demo Showcase"
nav_order: 177
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video features presentations on three open-source projects. First,
  Reza and Dimotion introduce Hami, a GPU orchestration solution that enables slicing
  GPUs into virtual devices to improve workload efficiency and reduce costs, with
  suppo...
resource: https://www.youtube.com/watch?v=cTXlkhKXgyE
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video features presentations on three open-source projects.
First, Reza and Dimotion introduce Hami, a GPU orchestration solution that enables slicing GPUs into virtual devices to improve workload efficiency and reduce costs, with support for various accelerators and strong resource isolation features; they highlight real-world case studies and demonstrate Hami’s capabilities in a Kubernetes environment.
Next, Patrick and Ben from Spotify showcase Backstage, a flexible internal developer portal that streamlines service discovery and documentation, and demonstrate new integrations with AI tools and a CLI, emphasizing that AI usage increases engagement with Backstage’s UI rather than replacing it.
Finally, Augustin presents Perses, an observability visualization tool developed by Amadeus, Red Hat, and SAP, which offers open dashboard specifications and reusable components for embedding in custom UIs, supporting a wide range of signals and Kubernetes monitoring dashboards, and enabling dashboard creation in Go.
Each project invites further exploration and community engagement.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Hami is a GPU orchestration solution that slices GPUs into virtual devices, enabling more parallel workloads and reducing cost and time to market.                                 |
|   2 | Example: Hami allows efficient GPU allocation, freeing up extra GPUs compared to traditional methods.                                                                              |
|   3 | Five case studies are available on the CNCF site; Baidu reduced inference task costs by two-thirds using Hami, and SF Express used custom memory isolation for workload stability. |
|   4 | Hami supports heterogeneous system management, including NVIDIA GPU, Huawei Ascend NPU, Cambricon MLU, AWS Neuron, Meta X, Innova, and more.                                       |
|   5 | Hami provides hard resource isolation inside containers via dynamic MIG partitioning and a self-implemented CUDA access layer.                                                     |
|   6 | Hami is Kubernetes-native and transparent to user tasks, with over 3,000 stars and 500 contributors in 17 countries.                                                               |
|   7 | Backstage is a framework for building internal developer portals, supporting extensibility through plugins and customizable entity pages.                                          |
|   8 | Increased AI tool usage correlates with increased Backstage UI usage; AI does not replace the UI.                                                                                  |
|   9 | Backstage integrates plugin actions across web UI, CLI, and AI tools, enabling engineers to use reusable actions in various workflows.                                             |
|  10 | Demo showed CLI integration, catalog search, and AI agent (Claude) using Backstage's MCP server to automate tasks and retrieve API information.                                    |
|  11 | Perses is an observability visualization tool for displaying metrics, logs, traces, and profiling; it's a CNCF project developed by Amadeus, Red Hat, and SAP, funded by the EU.   |
|  12 | Perses provides an open dashboard specification for vendor-agnostic observability and reusable React components for embedding in custom UIs.                                       |
|  13 | Perses supports Kubernetes, Prometheus, Thanos, Tempo, Alert Manager, Istio dashboards, and allows dashboard definition in Go using the Perses Go SDK and PromQL builder.          |
|  14 | Demo included monitoring Kubernetes clusters, displaying logs and traces, and using YAML and Go for dashboard definitions.                                                         |
|  15 | Project information and comm                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cTXlkhKXgyE)
