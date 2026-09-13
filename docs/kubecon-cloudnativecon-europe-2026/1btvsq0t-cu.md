---
layout: default
title: The Road To Strimzi 1.0 - Jakub Scholz, Cloudera & Paolo Patierno, IBM
nav_order: 365
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Paulo and Jakob, core maintainers of the StreamZ project, shared their
  journey toward the upcoming StreamZ 1.0 release, highlighting its eight-year development
  and the contributions of over 300 collaborators. The 1.0 release, planned for Ap...
resource: https://www.youtube.com/watch?v=1BtVSQ0t-CU
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

Paulo and Jakob, core maintainers of the StreamZ project, shared their journey toward the upcoming StreamZ 1.0 release, highlighting its eight-year development and the contributions of over 300 collaborators.
The 1.0 release, planned for April, finalizes the transition to a new v1 API introduced in earlier versions, removes deprecated features such as Zookeeper support and outdated authentication APIs, and provides an API conversion tool to ease user upgrades.
They emphasized flexibility in the upgrade path, allowing users to transition at their own pace, and explained the rationale behind the lengthy timeline, mainly due to waiting for Kafka’s shift away from Zookeeper.
Looking ahead, they outlined major upcoming features, including support for Kafka’s dynamic quorum, integration with cert-manager for certificate lifecycle management, enhanced auto-rebalancing with anomaly detection, and Gateway API support following the deprecation of the NGINX controller.
The session concluded with an invitation to the community to participate in the upcoming StreamZ conference and to engage through various channels for support and collaboration.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Paulo (IBM, co-founder of StreamZy) and Jakob (Cloudera, StreamZy maintainer) presented their journey to the StreamZy 1.0 release.   |
|   2 | StreamZy project has over 300 contributors and recently celebrated its 8th anniversary.                                              |
|   3 | The 1.0 release is almost ready, with some minor delays; the v1 API was introduced in the 0.49 release.                              |
|   4 | 1.0 will remove old APIs, including deprecated features related to Zookeeper and stateful sets.                                      |
|   5 | Specific APIs for configuring authentication/authorization (Keycloak, OPA) are removed; replaced by more flexible, type-custom APIs. |
|   6 | An API conversion tool was created to help users migrate custom resources and CRDs to the new v1 API.                                |
|   7 | Users must migrate from Zookeeper-based clusters to Kraft before upgrading.                                                          |
|   8 | Upgrade path: move from older versions (e.g., 0.48) to 0.49/0.50/0.51, then to 1.0+ using the conversion tool.                       |
|   9 | The conversion tool supports converting files, in-cluster resources, and CRD upgrades.                                               |
|  10 | StreamZy has had 51 minor releases and nearly 7,000 PRs merged.                                                                      |
|  11 | Delay to 1.0 was due to waiting for Zookeeper removal from Kafka, not production readiness.                                          |
|  12 | StreamZy is used in production by major companies and vendors (Cloudera, Red Hat, IBM).                                              |
|  13 | Upcoming features:                                                                                                                   |
|  14 | Support for Kraft dynamic quorum with automated scaling and migration from static to dynamic quorum.                                 |
|  15 | Integration with cert-manager for certificate lifecycle management.                                                                  |
|  16 | Improved auto-rebalancing with anomaly detection via Cruise Control.                                                                 |
|  17 | Gateway API integration to replace deprecated NGINX Ingress Controller, supporting TLS passthrough and termination.                  |
|  18 | Proposals for new features are open for community feedback.                                                                          |
|  19 | StreamZy virtual conference is upcoming in June; call for proposals is open for one more week.                                       |
|  20 | Community engagement encouraged via site, GitHub, social media, YouTube, and community calls.                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1BtVSQ0t-CU)
