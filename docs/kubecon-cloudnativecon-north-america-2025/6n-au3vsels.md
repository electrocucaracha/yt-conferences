---
layout: default
title:
  "Tutorial: Unlock the Future of Kubernetes and Accelerators With Dynamic Resource
  Alloc... Rey Lejano"
nav_order: 328
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this tutorial, Ray Lano from Red Hat introduces dynamic resource allocation
  (DRA) in Kubernetes, a feature stabilized in version 1.34 that enables more flexible
  and efficient sharing of hardware accelerators like GPUs, FPGAs, and network...
resource: https://www.youtube.com/watch?v=6n_AU3vSels
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this tutorial, Ray Lano from Red Hat introduces dynamic resource allocation (DRA) in Kubernetes, a feature stabilized in version 1.34 that enables more flexible and efficient sharing of hardware accelerators like GPUs, FPGAs, and network devices among pods.
The session includes a hands-on lab where participants use virtual machines to install a Kubernetes cluster, explore DRA resources, and deploy workloads using an example DRA driver.
Lano explains the architecture and workflow of DRA, contrasting it with the older device plugin approach, and demonstrates how DRA allows for fine-grained device selection, sharing, and configuration through resource claims and templates.
The tutorial also reviews vendor-specific DRA drivers from Nvidia, Intel, and Google, and walks through deploying and introspecting these drivers, as well as running AI workloads with resource sharing.
The session concludes with discussion of upcoming DRA features, integration with other Kubernetes components, and resources for further experimentation.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tutorial: "Unlock the Future of Kubernetes and Accelerators with Dynamic Resource Allocation (DRA)"                                                                       |
|   2 | Presenter: Ray Lano, Red Hat, Kubernetes SIGDOCs co-chair, release lead, and security audit organizer                                                                     |
|   3 | Hands-on lab focused on DRA resources in Kubernetes; lab links and handouts provided                                                                                      |
|   4 | DRA is required for Kubernetes AI conformance (v1.0), released in Kubernetes 1.34                                                                                         |
|   5 | DRA enables requesting and sharing resources (e.g., GPUs, NICs, FPGAs) among pods                                                                                         |
|   6 | Devices can be filtered and organized using Common Expression Language (CEL)                                                                                              |
|   7 | DRA allows device categorization (e.g., cost-optimized vs. high-performing)                                                                                               |
|   8 | Device plugins were the previous method for hardware access before DRA                                                                                                    |
|   9 | Node Feature Discovery (NFD) labels nodes for device plugins and DRA                                                                                                      |
|  10 | DRA introduces new features: passing configuration parameters, fine-grained filtering, device sharing, centralized categorization, and improved scheduling                |
|  11 | DRA workflow:                                                                                                                                                             |
|  12 | Cluster admin installs DRA driver (node-local kubelet plugin as DaemonSet, controller as Deployment)                                                                      |
|  13 | ResourceSlice represents devices on a node                                                                                                                                |
|  14 | DeviceClass defines device categories and selection criteria                                                                                                              |
|  15 | ResourceClaim requests devices from a DeviceClass; can be shared or per-pod via ResourceClaimTemplate                                                                     |
|  16 | Scheduler plugin ensures pods are scheduled where resources are available                                                                                                 |
|  17 | Lab walkthrough includes:                                                                                                                                                 |
|  18 | Installing Kubernetes cluster (kind), Helm, Docker, kubectl, jq                                                                                                           |
|  19 | Reviewing DRA resources and introspecting NVIDIA, Intel, and Google DRA drivers                                                                                           |
|  20 | Deploying example DRA driver and workloads (using simulated GPUs)                                                                                                         |
|  21 | Demonstrating resource sharing and allocation with pods and jobs                                                                                                          |
|  22 | DRA supports flexible device allocation, sharing, and configuration                                                                                                       |
|  23 | Example DRA drivers: NVIDIA (Helm chart, uses "compute domain"), Intel (Helm chart), Google DRA net (YAML, for networking), CPU DRA driver (experimental), AMD, Ffiosa AI |
|  24 | DRA is stable in Kubernetes 1.34; many new features in development (e.g., partitioning, access contr                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6n_AU3vSels)
