---
layout: default
title:
  SIG-Multicluster Intro and Deep... Jeremy Olmsted-Thompson, Laura Lorenz, Stephen
  Kitt & Ryan Zhang
nav_order: 292
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The SIG Multicluster project aims to provide a standardized way for managing
  multiple clusters across different environments, such as clouds and on-premises
  infrastructure. The project focuses on developing APIs that enable cluster manageme...
resource: https://www.youtube.com/watch?v=-SFVDr3wQ_w
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

The SIG Multicluster project aims to provide a standardized way for managing multiple clusters across different environments, such as clouds and on-premises infrastructure.
The project focuses on developing APIs that enable cluster management, service discovery, and orchestration across multiple clusters.
The multicluster services API is a key component of this effort, allowing services to be exposed across clusters without requiring a service mesh or gateway.
The SIG Multicluster team is working on integrating the multicluster services API with existing Kubernetes APIs and exploring ways to improve its adoption, including providing libraries and tools for implementing the standard.

# Main Points

|   # | Main point                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------- |
|   1 | The approach is diverse, considering various environments (clouds, on-prem, etc.) and topologies.              |
|   2 | The cluster set concept involves a group of clusters governed by a single authority with high trust within it. |
|   3 | Namespace sameness is key in multicluster, ensuring permissions and workload consistency across clusters.      |
|   4 | The cluster profile API provides a way to describe clusters and their properties.                              |
|   5 | The MCS API (Multicluster Services) allows services to be exposed across multiple clusters.                    |
|   6 | ISTTO's service imports and exports are similar to the MCS API.                                                |
|   7 | Gateway is used for east-west traffic, while MCS is used for north-south traffic.                              |
|   8 | There are plans for standardization in gateway and multicluster APIs.                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-SFVDr3wQ_w)
