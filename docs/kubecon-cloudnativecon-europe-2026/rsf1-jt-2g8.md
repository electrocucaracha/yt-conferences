---
layout: default
title:
  "Keynote: Making Kubernetes for AI Optimized and Reproducible - Nathan Taber
  & Mark Chmarny"
nav_order: 178
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Nathan Taber and Mark Smalley from Nvidia discuss their efforts to simplify
  running Kubernetes for AI workloads by introducing the AI Cluster Runtime Environment
  (ACRE) project. They explain the complexity of configuring AI clusters, which...
resource: https://www.youtube.com/watch?v=RsF1-Jt-2G8
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

Nathan Taber and Mark Smalley from Nvidia discuss their efforts to simplify running Kubernetes for AI workloads by introducing the AI Cluster Runtime Environment (ACRE) project.
They explain the complexity of configuring AI clusters, which involves managing hundreds of configuration values across numerous components, and highlight how Nvidia’s internal expertise has been encapsulated into machine-readable recipes within ACRE.
These recipes are optimized, validated, and reproducible sets of configurations tailored for specific use cases, including constraints and validation tools to ensure cluster readiness and conformance.
ACRE provides both a CLI and a self-hosted REST API, allowing users to generate, deploy, and validate these recipes and bundles in their own environments, with support for tools like Argo CD and Helm.
Nvidia has seeded ACRE with recipes for H100 and GB200 accelerators on EKS and GKE, and the project is open for community contributions, with recent input from Microsoft Azure and Oracle, aiming to expand its capabilities and recipes further.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nathan Taber and Mark Smalley are building Kubernetes at Nvidia, focusing on making Kubernetes easier for AI workloads.                                 |
|   2 | Nvidia has invested in projects like DRA driver, GPU operator, and Kai scheduler.                                                                       |
|   3 | Setting up an AI cluster for Kubernetes requires installing many components and configuring over 250 values across 15+ components.                      |
|   4 | Switching from training to inference involves swapping out 5 components and 40+ configuration values.                                                   |
|   5 | Nvidia’s team manages accelerated Kubernetes infrastructure for various workloads, including world model building and robotics.                         |
|   6 | Optimal cluster tuning knowledge has been internal to Nvidia but is now being shared with the community.                                                |
|   7 | Nvidia introduced the AI Cluster Runtime (ACRE) project to provide machine-readable recipes for configuring AI clusters for GPU training and inference. |
|   8 | ACRE recipes are validated, optimized, reproducible, and version-locked, including dependencies, manifests, and optimized values files.                 |
|   9 | Each recipe includes constraints for minimum cluster requirements and self-contained validations for deployment and CNCF AI conformance readiness.      |
|  10 | ACRE provides both a CLI and a self-hosted REST API for recipe creation and deployment.                                                                 |
|  11 | Users can specify variables such as service, accelerator type, intent (training/inference), and OS type to generate optimized recipes.                  |
|  12 | Recipes can be output as files or OCI images and queried in CI/CD pipelines without external connections.                                               |
|  13 | ACRE generates bundles (artifacts) for cluster deployment, supporting deployers like Argo CD and Helm.                                                  |
|  14 | Bundles are attested during generation, allowing later validation and provenance tracking.                                                              |
|  15 | Validators check component readiness and cluster conformance to CNCF AI standards, and can generate artifacts for CNCF conformance certification.       |
|  16 | Initial ACRE recipes support H100 and GB200 accelerators on EKS and GKE.                                                                                |
|  17 | Nvidia plans to expand ACRE with more recipes and capabilities, inviting community contributions.                                                       |
|  18 | Recent contributions                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RsF1-Jt-2G8)
