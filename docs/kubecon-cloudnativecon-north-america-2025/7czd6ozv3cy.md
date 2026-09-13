---
layout: default
title:
  "The Next Decoupling: From Monolithic Cluster, To Control-Pl... Justin Santa
  Barbara & Ciprian Hacman"
nav_order: 314
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Cyprian Hackman from Microsoft and Justin Santa Barbara
  from Google discuss evolving approaches to Kubernetes cluster lifecycle management,
  focusing on separating control plane and node management into distinct responsibilitie...
resource: https://www.youtube.com/watch?v=7czd6oZV3CY
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

In this talk, Cyprian Hackman from Microsoft and Justin Santa Barbara from Google discuss evolving approaches to Kubernetes cluster lifecycle management, focusing on separating control plane and node management into distinct responsibilities with potentially different tooling.
They explain that traditional installers manage both components together, which is simple but introduces challenges for upgrades, scalability, and cloud portability.
The speakers highlight emerging projects like Carpenter and Cluster API, which use Kubernetes-native APIs (CRDs) to enable more dynamic, programmable, and application-driven node management, allowing users or applications to create and manage nodes directly within the cluster.
They outline plans for KOPS to focus on control plane management while leveraging tools like Carpenter and Cluster API for node management, aiming to simplify workflows, improve flexibility, and enable advanced use cases such as proactive scaling and application-specific node provisioning.
The session concludes with a Q&A addressing implementation details, security considerations, and the potential for improved debugging and upgrade processes through this new model.

# Main Points

|   # | Main point                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Cyprian Hackman (Microsoft) and Justin Santa Barbara (Google) are maintainers of KOPS and contributors to Kubernetes cluster lifecycle projects.                                                      |
|   2 | The talk focuses on evolving Kubernetes cluster lifecycle management, not just KOPS.                                                                                                                  |
|   3 | Historically, installers managed both control plane and nodes together, making initial setup easy but causing friction for upgrades, scalability, and portability.                                    |
|   4 | There is a trend toward separating control plane and node management, possibly using different tools for each.                                                                                        |
|   5 | Control plane: complex, hard to build/maintain/scale, includes etcd, kube-apiserver, kube-controller-manager, kube-scheduler, kube-dns, cloud controller manager, workload identity, and autoscaling. |
|   6 | Nodes: focus on dynamic, unpredictable resource demands, many machine types, high scale, less concern for individual node failure.                                                                    |
|   7 | KOPS manages clusters via CLI and object storage; node creation/topology is controlled by cluster administrators, not users.                                                                          |
|   8 | Cluster Autoscaler is reliable but limited: works at node group level, reactive only, lacks per-node control, unpredictable placement, and not Kubernetes API-native.                                 |
|   9 | Newer projects embrace Kubernetes APIs and CRDs:                                                                                                                                                      |
|  10 | Carpenter: in-cluster, CRD-based node management, enables applications/operators to create nodes, not yet widely adopted, not all clouds supported.                                                   |
|  11 | Cluster API: CRDs for control planes and nodes, more monolithic, typically runs in a management cluster, not directly accessible to applications.                                                     |
|  12 | KOPS aims to focus on control plane management, enabling tools like Carpenter and Cluster API to manage nodes.                                                                                        |
|  13 | Users should be able to dynamically create nodes/groups from inside the cluster using Kubernetes APIs.                                                                                                |
|  14 | Separation of concerns: one tool for control plane, another for nodes; nodes can be created via CRDs (e.g., machine deployment or node pool).                                                         |
|  15 | Control plane and nodes remain part of the same logical cluster; physical placement is flexible.                                                                                                      |
|  16 | Security and permissions for node creation c                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7czd6oZV3CY)
