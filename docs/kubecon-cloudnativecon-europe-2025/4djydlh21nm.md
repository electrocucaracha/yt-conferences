---
layout: default
title:
  "Resilient Multi-Cloud Strategies: Harnessing Kubernetes, Cluster API, and...
  T. Rahman & J. Mosquera"
nav_order: 283
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=4DjydLH21nM
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

Here is a summary of the video transcript in 3-5 sentences: New Relic, a company providing intelligent observability platforms, has implemented a cellular architecture to manage its Kubernetes infrastructure across multiple cloud providers.
This architecture consists of self-contained units called "cells" that can be scaled independently and have limited blast radius in case of incidents.
The cells are managed using a combination of cluster API, carpenter, and custom tools, which enable features such as automated node creation, scheduling classes, and cell routing based on customer ID and data type.
This architecture allows for greater scalability, flexibility, and reliability, while also reducing the complexity of managing multiple cloud providers.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | New Relic has a multi-cloud Kubernetes infrastructure with 280 clusters, 5,000 pots, and 21,000 nodes across multiple cloud providers.             |
|   2 | The company uses a cellular architecture to scale out workloads while limiting blast radius for incidents.                                         |
|   3 | Each cell is an independent unit with its own resources and components, and they are interconnected to provide complex functions.                  |
|   4 | The cellular architecture is based on the concept of cells in biology, where each cell can live independently but also exchange energy and matter. |
|   5 | New Relic uses a custom-built cluster API and Carpenter for compute management.                                                                    |
|   6 | The company has developed a bootstrapping process for Kubernetes clusters using a command and control cell.                                        |
|   7 | Developers can provision nodes for their applications using machine pools and Helm charts.                                                         |
|   8 | Scheduling classes are used to express scheduling requirements for applications without requiring node labels and taints.                          |
|   9 | Cluster API and Carpenter are used to manage cluster life cycles, including upgrades and node refreshes.                                           |
|  10 | The company has implemented a checkpointing process to track the state of cluster creation and ensure consistency.                                 |
|  11 | Cells can be ephemeral or stateful, depending on the workload and traffic characteristics.                                                         |
|  12 | Cell routing is based on analyzing customer traffic patterns and data types, and redirecting traffic to specific cells accordingly.                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4DjydLH21nM)
