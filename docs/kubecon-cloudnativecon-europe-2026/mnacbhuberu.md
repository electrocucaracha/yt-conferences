---
layout: default
title:
  "No Shame, Just Pain: How We Migrated Away From Kubernetes. Jannis Relakis
  & Michael Seiwald-McCarty"
nav_order: 224
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Janisle and Michael from Salonus detailed their company’s
  large-scale migration from multiple outdated Kubernetes flavors to a consolidated,
  modern platform. Facing challenges such as six different Kubernetes setups across...
resource: https://www.youtube.com/watch?v=MNAcbHUBERU
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

In this session, Janisle and Michael from Salonus detailed their company’s large-scale migration from multiple outdated Kubernetes flavors to a consolidated, modern platform.
Facing challenges such as six different Kubernetes setups across three cloud providers and 160 clusters, they aimed to standardize on one flavor per provider without requiring application changes.
To enable zero-downtime migrations, they developed a custom cross-cluster service mesh called the "wormhole," allowing seamless communication between old and new clusters.
Applications were categorized as stateless, singleton, or stateful, each with tailored migration strategies, and automation tooling was built to handle the vast number of required changes efficiently and consistently.
Key lessons included minimizing scope changes, reducing environment-specific "snowflakes" to improve repeatability, investing in automation, and continually refining processes to ensure reliability and scalability throughout the multi-year migration.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Salonus migrated away from Kubernetes 1.16 in 2025, consolidating six Kubernetes flavors down to three (one per cloud provider: AWS, Azure, GCP).                                                                                                                                      |
|   2 | Salonus runs 160 clusters across 22 cloud regions, supporting both shared and dedicated environments.                                                                                                                                                                                  |
|   3 | Historical Kubernetes setup included COPS (AWS), Gardner (Azure), and OpenShift (enterprise security).                                                                                                                                                                                 |
|   4 | Lack of consolidation and upgrades led to outdated, hard-to-maintain clusters.                                                                                                                                                                                                         |
|   5 | Migration goals: one flavor per cloud provider, same Kubernetes version, modern, secure, and maintainable clusters.                                                                                                                                                                    |
|   6 | Target platform requirements: multi-cloud support, no application changes, uniform clusters, managed Kubernetes services (EKS, AKS, GKE), infrastructure as code (Terraform, Terragrunt), ArgoCD for cluster add-ons, prioritized cluster upgrades, and Carpenter for node management. |
|   7 | Cluster fleet consists of three clusters: main workloads, machine learning/AI, and query engine, all connected via a shared network.                                                                                                                                                   |
|   8 | Developed a custom cross-cluster service mesh ("wormhole") using Envoy proxies for zero-downtime migration and seamless inter-cluster communication.                                                                                                                                   |
|   9 | Applications classified for migration: 90% stateless (scale up, cut over, scale down), 1% singletons (require downtime), 9% stateful (bespoke migrations).                                                                                                                             |
|  10 | Created a master plan/dependency diagram for environment migration, enabling better scheduling, parallelization, and optimization.                                                                                                                                                     |
|  11 | Migration steps for stateless apps: duplicate and adjust Kustomize overlays, update manifests, scale up, cut over, scale down—each step generated PRs.                                                                                                                                 |
|  12 | Built a CLI migration tool to automate and batch migrations, ensuring consistency, documentation, and speed, enabling more team members to participate.                                                                                                                                |
|  13 | Early migration was slow due to environment heterogeneity ("snowflakiness"); automation and consolidation improved velocity and uniformity.                                                                                                                                            |
|  14 | Key lessons: avoid changing too much at once, beware of scope creep, prioritize repeatability, adapt to ongoing changes, improve runbook                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MNAcbHUBERU)
