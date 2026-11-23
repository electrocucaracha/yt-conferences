---
layout: default
title: "Mission: AI-Possible – Red Hat’s Next-Gen Infrastructure with OpenStack Services on OpenShift"
nav_order: 109
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Red Hat’s annual session outlines the modernization of OpenStack into a Kubernetes-native microservices architecture, enabling faster feature delivery and unified management of both virtualized and..."
resource: "https://www.youtube.com/watch?v=_fpfFu38GQ0"
youtube_stats:
  view_count: 56
  like_count: 2
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Red Hat’s annual session outlines the modernization of OpenStack into a Kubernetes-native microservices architecture, enabling faster feature delivery and unified management of both virtualized and container-native workloads.
The presentation highlights key innovations such as live kernel patching to address security vulnerabilities without downtime, the "Watcher" smart scheduler for cost and performance optimization, and distributed zones for low-latency multi-region orchestration.
Additionally, Red Hat introduced an open-source migration toolkit leveraging Ansible to facilitate seamless workload transfers from VMware and other OpenStack distributions.
The company’s AI strategy centers on providing an enterprise-grade, sovereign platform that supports heterogeneous GPU management, model training, and inference across any cloud footprint.
Finally, the session demonstrated the integration of Red Hat OpenShift Lightspeed, an LLM assistant that uses Model Context Protocols (MCP) to offer real-time incident detection, anomaly analysis, and operational insights directly within the OpenStack and OpenShift environments.

# Main Points

|   # | Main point                                                                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Red Hat modernized OpenStack by packaging services like Neutron and Nova as microservices on Kubernetes and OpenShift to enable independent versioning and lifecycle management.                                      |
|   2 | The platform unifies OpenStack and Kubernetes workloads, allowing shared repositories and node movement between environments while supporting 4G LTE and 5G telco workloads.                                          |
|   3 | Feature releases are delivered every four months, enabling non-disruptive updates and new capabilities like distributed zones and GPU live migrations without waiting for major releases.                             |
|   4 | Live kernel patching is introduced for OpenStack to apply security fixes in memory without rebooting nodes, addressing the increased volume of cyberattacks and vulnerabilities.                                      |
|   5 | Watcher is modernized as a native operator microservice on OpenShift to optimize workload scheduling for cost and performance, supporting day-two operations like region evacuation and hardware introduction.        |
|   6 | Distributed zones allow enterprise customers to orchestrate low-latency zones across different racks or regions using a single OpenStack endpoint, similar to cloud region management.                                |
|   7 | The VMware migration toolkit, based on the open-source OS Migrate framework, supports live migration of VMs from VMware or other OpenStack distributions using Ansible automation for scalability.                    |
|   8 | Red Hat’s AI strategy focuses on an open platform for developing, deploying, and managing AI workloads across any footprint, accelerator, and model, emphasizing data integrity and sovereign AI capabilities.        |
|   9 | Red Hat AI 3 unifies products under one umbrella, offering SDKs for data ingestion, synthetic data generation, and RAG improvements, while integrating partner models and bringing your own data.                     |
|  10 | OpenStack provides horizontal management of heterogeneous GPUs from vendors like Nvidia and AMD, offering multi-tenancy, quota management, over-subscription control, and unified telemetry in the OpenShift console. |
|  11 | GPU-as-a-Service capabilities allow slicing high-memory GPUs for specific tenant needs, enabling time-bound access for training or inference with secure teardown and reallocation.                                   |
|  12 | Red Hat OpenShift Lightspeed, an LLM assistant, is integrated into OpenStack to provide natural language queries for configuration, incident detection, and root cause analysis using machine learning.               |
|  13 | Model Context Protocol (MCP) integration allows the LLM to connect to additional data sources and services, centralizing answers from Red Hat products and user data within a single interface.                       |
|  14 | Future AI capabilities include anomaly detection and trend analysis, shifting the center of gravity from CLI and consoles to the LLM for centralized platform interaction and debugging.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_fpfFu38GQ0/hqdefault.jpg)](https://www.youtube.com/watch?v=_fpfFu38GQ0)

[Watch on YouTube](https://www.youtube.com/watch?v=_fpfFu38GQ0)
