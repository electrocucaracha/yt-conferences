---
layout: default
title: Building a Kubernetes Distribution for Workday using Zuul
nav_order: 75
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Workday engineers Simon and Shicardan explain how they built a custom Kubernetes distribution for their private cloud to integrate with internal infrastructure components like storage and DNS, whic..."
resource: "https://www.youtube.com/watch?v=VnZQE8RpYCY"
youtube_stats:
  view_count: 95
  like_count: 1
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

Workday engineers Simon and Shicardan explain how they built a custom Kubernetes distribution for their private cloud to integrate with internal infrastructure components like storage and DNS, which pre-built solutions like EKS or OpenShift could not support.
Their architecture utilizes a small service cluster managed by Argo CD to deploy Helm charts to worker clusters, allowing the public cloud team to reuse existing Helm charts in the private environment.
The team leverages Zuul for CI/CD, employing job inheritance to manage multiple Kubernetes profiles and running comprehensive functional, integration, and static tests, including the use of Chainsaw for policy validation.
Key challenges addressed include managing the order of Argo CD syncing to prevent admission issues, ensuring robust cleanup of resources created during testing, and maintaining isolated test jobs to avoid timeouts.
Finally, Yan details the process of operating and upgrading Zuul itself using the Zuul Operator, highlighting the importance of using upstream containers, managing artifacts via external registries, and maintaining a staging environment to safely test updates before production deployment.

# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Workday operates approximately 120,000 VMs across 180 OpenStack clusters, performing around 750,000 VM builds and tear-downs weekly.                                                              |
|   2 | The team developed a custom Kubernetes distribution to integrate with Workday’s proprietary storage and external DNS components, which pre-built solutions like EKS or OpenShift did not support. |
|   3 | The architecture uses a small service cluster installed via Ansible to bootstrap an Argo CD instance, which then deploys the full Kubernetes distribution to worker clusters.                     |
|   4 | The distribution is managed as an Argo CD App of Apps containing configured Helm charts for infrastructure components like DNS and storage.                                                       |
|   5 | Upgrades are performed by updating the version in the App of Apps, allowing Argo CD to sync changes to the worker clusters.                                                                       |
|   6 | Cluster scaling and node management are handled heavily by the Cluster Autoscaler.                                                                                                                |
|   7 | Key lessons learned include the need for strict ordering of Argo CD syncing to prevent admission webhook failures during cluster reboots.                                                         |
|   8 | Robust cleanup scripts are essential because resources created by the Cluster Autoscaler during testing are not managed by NodePool and can leak if jobs fail.                                    |
|   9 | Tests are kept isolated to avoid long-running deploy jobs that hit time limits, ensuring easier maintenance over time.                                                                            |
|  10 | Applications are categorized into infrastructure apps (cluster-scoped, requiring new cluster creation for testing) and regular apps (namespace-scoped, testable via existing drivers).            |
|  11 | Multiple slightly different Kubernetes versions are maintained based on environment, team requirements, and cluster profiles.                                                                     |
|  12 | Platform configuration is divided into three repositories: cluster/environment data, team information, and deployment profiles.                                                                   |
|  13 | Release pipelines are triggered by adding release tags to commits, which merge components into a final App of Apps Helm chart for testing.                                                        |
|  14 | Zuul job inheritance is used to create base jobs for cluster deployment and testing, with specific profiles inheriting from these bases.                                                          |
|  15 | Testing includes conformance tests, policy testing using Chainsaw, functional tests, integration tests, and static linting.                                                                       |
|  16 | The team builds Zuul containers from scratch due to an isolated environment, utilizing OpenDev builders for customization.                                                                        |
|  17 | A generic Helm chart for Zuul is created to allow deployment via Argo CD, ensuring Zuul is treated as a standard application within the platform.                                                 |
|  18 | The pipeline avoids the bootstrap problem by having Argo CD manage Zuul while Zuul manages the Helm charts Argo CD deploys.                                                                       |
|  19 | External artifact repositories are used to age out containers and store test artifacts, reducing the need for temporary registries during jobs.                                                   |
|  20 | The Zuul Operator is used to bootstrap and manage Zuul instances on Kubernetes, with a downstream fork maintained for specific template updates.                                                  |
|  21 | A staging environment is maintained to test changes safely, leveraging the existing multi-cluster infrastructure to minimize resource overhead.                                                   |
|  22 | The team is upgrading from Zuul 4.2 to newer versions to unlock features like Notable and improved Zuul capabilities.                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VnZQE8RpYCY/hqdefault.jpg)](https://www.youtube.com/watch?v=VnZQE8RpYCY)

[Watch on YouTube](https://www.youtube.com/watch?v=VnZQE8RpYCY)
