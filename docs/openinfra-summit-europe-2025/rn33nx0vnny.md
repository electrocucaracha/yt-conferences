---
layout: default
title: "Transforming Telecom: Kubernetes in Radio Access Network Management"
nav_order: 67
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The Taka team presented a strategy for transforming telecom access network management by extending cloud-native virtualization from core networks to the radio access network (RAN)."
resource: "https://www.youtube.com/watch?v=rn33NX0vnnY"
youtube_stats:
  view_count: 105
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

The Taka team presented a strategy for transforming telecom access network management by extending cloud-native virtualization from core networks to the radio access network (RAN).
This initiative aims to convert thousands of dedicated base stations into small, standard data centers using commercial servers, thereby reducing costs, enhancing agility, and minimizing on-site maintenance through comprehensive automation.
To address the challenges of managing this highly distributed infrastructure, the team proposed a four-layer architecture that leverages open-source technologies, including OpenStack, Kubernetes, and Prometheus, to enable centralized monitoring and automated lifecycle management.
A key component of this solution is the use of Open Tacker and Devtron to implement Service Management and Orchestration (SMO) capabilities, which facilitate multi-vendor integration, automated healing, and the management of both containerized and virtual machine workloads.
The presentation highlighted specific commercial use cases, such as the automated deployment and healing of Open Distributed Units (ODUs) that utilize hardware accelerators like GPUs, while acknowledging ongoing challenges in accelerator management, authentication, and large-scale parallel healing.
Future plans include enhancing automation frameworks for auto-locating resources, integrating AI for intelligent lifecycle management, and fully supporting accelerator-related specifications to achieve a zero-touch operational model.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | NTT DoCoMo is transforming telecom access network management by extending cloud technology from the core network to the radio access network (RAN).                                |
|   2 | The company achieved 100% virtualization of its core network starting in 2015, gaining benefits such as improved agility, operational efficiency, and reduced capital expenditure. |
|   3 | The next step involves containerizing the RAN to handle the massive scale of thousands of cell sites, enabling faster healing and granular automation.                             |
|   4 | Key challenges in RAN virtualization include managing tens of thousands of distributed small data centers, reducing on-site work, and ensuring reliability and security.           |
|   5 | DoCoMo employs a four-layer architecture consisting of public cloud, central on-premise sites, regional sites, and edge sites for comprehensive automation and monitoring.         |
|   6 | The system utilizes OpenStack Tacker for application lifecycle management and Devtron as the Service Management and Orchestration (SMO) component.                                 |
|   7 | OpenStack SX is used for edge cloud management, supporting hardware capabilities like SR-IOV and ADK, while Prometheus handles infrastructure and application monitoring.          |
|   8 | Commercial deployment challenges included out-of-memory issues in stateful sets, massive parallel healing requirements, and UI manageability for 10,000-level network functions.   |
|   9 | The solution supports multi-vendor environments by abstracting vendor-specific differences through unified APIs and standardized lifecycle workflows.                              |
|  10 | Accelerator management, specifically for GPUs used in Open Distributed Units (ODU), is a critical challenge requiring automated configuration and resource assignment.             |
|  11 | Integration challenges among open-source components, particularly authentication management between services, remain significant hurdles in the current implementation.            |
|  12 | The automated workflow allows for automatic healing and scaling when Prometheus detects anomalies and sends alerts to the SMO orchestrator.                                        |
|  13 | Future plans include full support for accelerator resource management, enhanced automation frameworks with auto-arming, and more intelligent lifecycle management using AI.        |
|  14 | The team aims to improve SMO capabilities to manage hybrid workloads involving both virtual machines and containers through a unified interface.                                   |
|  15 | All components used in the architecture, including Tacker, Devtron, and SX, are open-source, allowing for published documentation and reusable implementation scripts.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rn33NX0vnnY/hqdefault.jpg)](https://www.youtube.com/watch?v=rn33NX0vnnY)

[Watch on YouTube](https://www.youtube.com/watch?v=rn33NX0vnnY)
