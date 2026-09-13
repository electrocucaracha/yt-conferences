---
layout: default
title: Trino and Data Governance on Kubernetes - Sung Yun & Aki Sukegawa, Bloomberg
nav_order: 346
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=vCfehltPKxk
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

Here is a summary of the video transcript in 3-5 sentences: Bloomberg deployed Trino, a scalable and distributed processing engine, on Kubernetes to centralize its data analytics infrastructure and enable secure data sharing across teams.
The company built a managed Trino as a service platform that applies authorization checks at runtime using Open Policy Agent (OPA) and Kubernetes Custom Resources (CRDs).
This allows data owners to share data access configurations without exposing credentials, while also enabling service owners to control compute access for users.
The platform is designed to support multi-tenancy, scalability, and security, with plans to introduce a Trino gateway to enable intelligent workload balancing and stability during maintenance operations or data center outages.

# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Bloomberg's data environment is massive, with pabyte-scale financial data and 125,000 curated news sources.                                                                                               |
|   2 | The company acquires data from various sources, including real-time streaming data for market insights.                                                                                                   |
|   3 | There's a need to secure data discovery for AI workloads, ensuring only authorized users and applications can access data for specified use cases.                                                        |
|   4 | Trino is a scalable and highly distributed processing engine that optimizes query performance through parallel processing and predicate pushdowns.                                                        |
|   5 | Trino also uses distributed caching to avoid redundant S3 reads and has NISSQL compliance with popular open-source business intelligence tools.                                                           |
|   6 | Bloomberg's managed Trino as a service platform provides:                                                                                                                                                 |
|   7 | Centralized data governance                                                                                                                                                                               |
|   8 | Runtime data access control by enforcing policies that match predefined access control definitions                                                                                                        |
|   9 | Deployment management, scalability, and multi-tenant features                                                                                                                                             |
|  10 | The platform uses Open Policy Agent (OPA) for policy enforcement and authorization checks at runtime.                                                                                                     |
|  11 | OPA is used for both data access control and computation access control.                                                                                                                                  |
|  12 | The platform allows data owners to create Trino catalogs with granular data access policies and enables service owners to create Trino clusters that can mount these catalogs.                            |
|  13 | Catalogs are defined within namespaces, but a centralized catalog management system pulls information from separate namespaces for authorization checks.                                                  |
|  14 | The platform is stable, with existing users having a good experience across all tiers. However, there are challenges with query performance due to the architecture's analytical processing optimization. |
|  15 | To address this, the team is working on introducing stability and addressing issues related to container lifecycle management when Trino goes down or data centers go down.                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vCfehltPKxk)
