---
type: Video Note
title: "Collisions in the Dark: Illuminating the 95% of Kubeflow You Can't... Amine Lahouel & Laura Llinares"
description: "In this talk, Amin and Lara, engineers at CERN, present their work on observability for the Next Generation Triggers (NGT) project, which supports CERN’s high-energy physics experiments by managing vast amounts of collision data. They descr..."
resource: https://www.youtube.com/watch?v=AsPCWEBiR6g
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Amin and Lara, engineers at CERN, present their work on observability for the Next Generation Triggers (NGT) project, which supports CERN’s high-energy physics experiments by managing vast amounts of collision data.
They describe the challenges of providing a scientific computing platform based on Kubeflow and Kubernetes, focusing on the need for detailed metrics to address user questions about training performance, GPU usage, energy consumption, and resource efficiency.
Their observability stack integrates various exporters and tools—such as Prometheus, Grafana, Kepler, and IPMI—to collect and visualize metrics on GPU and CPU utilization, energy consumption, and CO2 emissions, supporting both user troubleshooting and sustainability goals.
They share lessons learned from scaling their monitoring infrastructure, highlight the importance of dashboards for users and administrators, and discuss ongoing efforts to simplify deployment through a Kubeflow observability manifest.
The talk concludes by emphasizing the value of transparency, sustainability, and open-source collaboration in building effective observability solutions for scientific computing workloads.
# Main Points

|   # | Main point                                                                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Amin, software engineer at CERN with nearly a decade of experience; Lara, 25, DevOps engineer at CERN.                                                                                               |
|   2 | CERN is the largest high energy physics laboratory, known for the discovery of the boson using the Large Hadron Collider.                                                                                        |
|   3 | Collider experiments generate up to 40 million collisions per second, producing massive data volumes.                                                                                                            |
|   4 | Trigger systems filter collision data: Level 1 (hardware) and Level 2 (software) each filter ~99% of data before storage.                                                                                        |
|   5 | Current phase: Run 3, moving towards High Luminosity LHC (more data, improved triggers).                                                                                                                         |
|   6 | Project NGT (Next Generation Triggers) focuses on data acquisition, trigger systems, and real-time event processing.                                                                                             |
|   7 | Team manages scientific computing infrastructure for NGT, including hardware/software platforms.                                                                                                                 |
|   8 | Scientific computing platform built for machine learning, based on Kubeflow and open source components.                                                                                                          |
|   9 | Platform provides shared GPU and compute resources for interactive and batch workloads, focusing on ML.                                                                                                          |
|  10 | Users have diverse needs: training speed, energy consumption, GPU allocation.                                                                                                                                    |
|  11 | Default Kubernetes monitoring is limited; additional metrics needed for GPU, power, and efficiency.                                                                                                              |
|  12 | Metrics categories: platform usage (active users, sessions), GPU telemetry (frequency, energy, utilization), resource availability, power consumption, sustainability (CO2 emissions), idle resource monitoring. |
|  13 | Architecture: hardware exporters (Nvidia, AMD, IPMI, Kepler), node and kube exporters, Prometheus for scraping, Grafana for visualization, Alertmanager for notifications.                                       |
|  14 | Metrics are handpicked for relevance; node, container, hardware, and GPU metrics are collected.                                                                                                                  |
|  15 | Energy monitoring uses IPMI (node-level) and Kepler (Kubernetes-level) for energy attribution per workload.                                                                                                      |
|  16 | CO2 emissions calculated by combining energy data with French grid carbon intensity API.                                                                                                                         |
|  17 | Prometheus faced scaling issues; solutions included tuning retention, using PVCs, and remote storage with filtering.                                                                                             |
|  18 | Dashboards: user workloa                                                                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=AsPCWEBiR6g)