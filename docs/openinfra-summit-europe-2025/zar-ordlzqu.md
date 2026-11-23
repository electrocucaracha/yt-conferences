---
layout: default
title: Bringing Availability Zones up to par
nav_order: 103
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This session discusses the challenges of treating OpenStack availability zones as true failure domains, highlighting issues with cross-zone scheduling, storage isolation, and backup restoration."
resource: "https://www.youtube.com/watch?v=ZAr-OrdLzqU"
youtube_stats:
  view_count: 60
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

This session discusses the challenges of treating OpenStack availability zones as true failure domains, highlighting issues with cross-zone scheduling, storage isolation, and backup restoration.
The participants identify that current Nova scheduling lacks support for anti-affinity across availability zones, which complicates the deployment of resilient services like Octavia and Kubernetes clusters.
A key technical gap is the inability to restore Cinder backups to a different availability zone than where they were created, forcing users to rely on inefficient workarounds like Glance image transfers.
The group proposes extending the server group affinity API to allow policies based on host aggregates or availability zones, enabling better placement of instances across distinct failure domains.
Additionally, they explore improving Glance’s image import mechanisms to ensure images are efficiently distributed across multiple storage backends, reducing latency and dependency on single-zone resources.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session focuses on elevating availability zones (AZs) to a core OpenStack concept to improve scheduling and resilience across multiple data centers.             |
|   2 | Current limitations prevent placing services in server groups with anti-affinity across AZs, impacting projects like Octavia and Kubernetes.                         |
|   3 | Users require the ability to migrate block storage devices between AZs to avoid stretch storage clusters and ensure continuity during failures.                      |
|   4 | Nova currently lacks a native concept for AZs as failure domains, forcing reliance on host aggregates for grouping resources.                                        |
|   5 | The Placement API supports grouping resource providers, but Nova does not fully model non-compute resources like switches or racks within this framework.            |
|   6 | A proposed solution involves extending server group affinity policies to support arbitrary grouping beyond simple host affinity.                                     |
|   7 | Hard anti-affinity is preferred over soft affinity to guarantee workload distribution across AZs for disaster recovery scenarios.                                    |
|   8 | Soft affinities introduce complexity with weighting factors, making it difficult to balance multiple scheduling constraints effectively.                             |
|   9 | Combining soft anti-affinity for AZs with hard anti-affinity for hosts is suggested as a practical approach to prevent resource contention.                          |
|  10 | Implementing group affinity in Nova would simplify integration for other projects like Octavia, which currently require complex patches to handle multi-site setups. |
|  11 | Cinder backups are currently locked to the AZ where they were created, preventing restoration to a different AZ if the original one fails.                           |
|  12 | There is a need for an API override to allow Cinder backup restoration to target a different AZ or storage backend.                                                  |
|  13 | Glance image distribution across isolated AZs is problematic, as standard uploads do not automatically replicate images to all localStorage backends.                |
|  14 | The Glance import API can distribute images across backends, but it is not widely used or enforced by standard workflows like Horizon or Nova.                       |
|  15 | Users often rely on external S3 storage for images, which introduces latency and bandwidth issues when pulling large images across AZs.                              |
|  16 | The discussion concludes that starting with Nova server group policy improvements is the most viable first step to address cross-AZ scheduling challenges.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZAr-OrdLzqU/hqdefault.jpg)](https://www.youtube.com/watch?v=ZAr-OrdLzqU)

[Watch on YouTube](https://www.youtube.com/watch?v=ZAr-OrdLzqU)
