---
layout: default
title: How BMW Uses Zuul CI as the Standard Gating System
nav_order: 14
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "BMW utilizes Zuul as its standard CI/CD system to manage the high complexity of software-defined vehicles, scaling to handle over 20,000 job executions per hour and serving more than 15,000 develop..."
resource: "https://www.youtube.com/watch?v=Z8rofKRen3w"
youtube_stats:
  view_count: 411
  like_count: 5
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

BMW utilizes Zuul as its standard CI/CD system to manage the high complexity of software-defined vehicles, scaling to handle over 20,000 job executions per hour and serving more than 15,000 developers.
The presentation highlights significant contributions to the Zuul project, including the implementation of circular dependency support to facilitate integrated automotive development, high-availability scheduling to eliminate downtime, and the introduction of OIDC workload identity federation to enhance security by replacing static secrets with dynamic, short-lived tokens.
Additionally, BMW has optimized cloud resource usage through Fleet API support and centralized cost-data analysis, enabling precise tracking of infrastructure expenses per build.
These efforts, combined with continuous community collaboration and robust monitoring, have resulted in a highly reliable and performant system that supports rapid integration and innovation in the automotive sector.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | BMW uses Zuul as its standard CI/CD system, handling over 20,000 job executions per hour to support software-defined vehicle development.                    |
|   2 | The automotive industry is shifting toward integrated computing units, requiring developers to collaborate on complex, interdependent software changes.      |
|   3 | BMW’s software factory platform includes Architecture Craft, CodeCraft, and Validation Craft, with CodeCraft focusing on development and quality.            |
|   4 | The CI infrastructure is a hybrid of AWS and on-prem OpenStack, supporting over 15,000 developers and 210,000 daily builds.                                  |
|   5 | The system peaks at over 7,000 parallel builds, utilizing more than 100,000 vCPUs simultaneously.                                                            |
|   6 | BMW was an early adopter of Zuul, contributing over 1,000 changes to the upstream project to improve reliability and scalability.                            |
|   7 | A key contribution was adding support for circular dependencies, allowing developers to integrate and validate changes across different source code systems. |
|   8 | The Zuul scheduler was made highly available using ZooKeeper, eliminating downtime during regular updates and reducing outages.                              |
|   9 | The status page UI was improved to provide better overviews for large projects with many repositories and concurrent changes.                                |
|  10 | Fleet API support was implemented to minimize cloud capacity limits by allowing jobs to use multiple instance types.                                         |
|  11 | OIDC workload identity federation was introduced to replace static secrets with short-lived, dynamically generated tokens for improved security.             |
|  12 | The OIDC flow allows Zuul executors to generate tokens that target services verify using public keys, eliminating the need for frequent secret rotation.     |
|  13 | BMW maintains extensive logging, metrics, and alerting systems to identify performance bottlenecks and instabilities in the CI pipeline.                     |
|  14 | Central cost data is collected and tagged to match infrastructure costs with specific pull requests or jobs, enabling cost optimization and right-sizing.    |
|  15 | Future plans include adopting the new node pool in Zuul for pre-validating cloud images and further optimizing scheduling performance.                       |
|  16 | The team emphasizes continuous collaboration with the Zuul community and long-term vision to maintain a reliable, high-performance CI service.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Z8rofKRen3w/hqdefault.jpg)](https://www.youtube.com/watch?v=Z8rofKRen3w)

[Watch on YouTube](https://www.youtube.com/watch?v=Z8rofKRen3w)
