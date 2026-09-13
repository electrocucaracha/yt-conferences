---
type: Video Note
title: "Project Lightning Talk: kcp: Scaling The Kubernetes Control Plane For The Multi-Clust... Jan Willies"
description: "Jan Viegas from Accenture introduces the KCP project, addressing challenges in Kubernetes related to provisioning isolated environments. Traditional options like namespaces are quick but limited, while full clusters are heavy and slow to pr..."
resource: https://www.youtube.com/watch?v=-GJgzn3pyvM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jan Viegas from Accenture introduces the KCP project, addressing challenges in Kubernetes related to provisioning isolated environments.
Traditional options like namespaces are quick but limited, while full clusters are heavy and slow to provision.
KCP offers a lightweight, open-source, horizontally scalable control plane for Kubernetes-like APIs, providing isolated workspaces that deliver a full Kubernetes API experience without the overhead of nodes, pods, or deployments.
Each workspace is provisioned in seconds, grants cluster admin privileges, and supports familiar Kubernetes tools.
KCP is notable for its advanced handling of Custom Resource Definitions (CRDs), allowing different versions and controllers to coexist, thus simplifying upgrades and API management.
# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Jan Viegas from Accenture                                                                                          |
|   2 | Topic: KCP project                                                                                                            |
|   3 | Problem in Kubernetes:                                                                                                        |
|   4 | Namespaces are quick to provision but limited in isolation                                                                    |
|   5 | Full Kubernetes clusters provide isolation but are heavy and slow to provision                                                |
|   6 | Need for a solution that combines lightweight provisioning with full isolation                                                |
|   7 | Vanilla Kubernetes cluster has around 80 built-in resources, many unnecessary for CRD-focused use cases                       |
|   8 | KCP project:                                                                                                                  |
|   9 | Open source, horizontally scalable control plane for Kubernetes-like APIs                                                     |
|  10 | Provides isolated Kubernetes endpoints called "workspaces"                                                                    |
|  11 | Workspace offers a full Kubernetes API without workload/infrastructure resources (no nodes, pods, deployments)                |
|  12 | Users are cluster admins within their workspace                                                                               |
|  13 | Workspaces can be provisioned in seconds                                                                                      |
|  14 | Supports both namespace and non-namespace resources                                                                           |
|  15 | Compatible with familiar Kubernetes tools (kubectl, helm, client-go)                                                          |
|  16 | Written in Go, compiled as a single binary                                                                                    |
|  17 | Can run locally, as a managed service, or on Kubernetes                                                                       |
|  18 | Supports deployment as a global control plane with multi-region support, caching layers, and aggregate APIs                   |
|  19 | KCP's standout feature: advanced mechanism for handling CRDs and CRD version upgrades                                         |
|  20 | Allows different controllers for different CRD versions (e.g., v1alpha1 vs v1alpha2)                                          |
|  21 | Supports exporting APIs under different names in KCP versus backing clusters                                                  |
|  22 | Additional KCP sessions available at the conference, including one on a discovered CVE and others with deeper project details |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-GJgzn3pyvM)