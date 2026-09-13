---
type: Video Note
title: "Three Shades of Isolation: A Multi-tenancy Fortress - Braulio Dumba & Paolo Dettori, IBM"
description: 'In this presentation, Paulo Detorii and his colleague from IBM Research introduce a new approach to Kubernetes multi-tenancy called "three shades of isolation," which addresses the growing need for secure, efficient, and isolated environmen...'
resource: https://www.youtube.com/watch?v=24E4LDWThAE
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Paulo Detorii and his colleague from IBM Research introduce a new approach to Kubernetes multi-tenancy called "three shades of isolation," which addresses the growing need for secure, efficient, and isolated environments for multiple tenants within a single cluster.
They identify four key requirements for effective isolation: data plane isolation, access boundaries, control plane isolation, and a native Kubernetes user experience.
Their solution leverages four open-source technologies—Kubeflex for control plane provisioning, KubeVirt for running virtual machines as pods, K3s for lightweight Kubernetes control planes, and OVN-Kubernetes for advanced network segmentation—to provide each tenant with dedicated control and data planes as well as isolated networks.
Through a detailed demo, they show how this architecture enables strong separation between tenants, minimizes the noisy neighbor problem, and maintains low performance overhead, with latency increases remaining in the single-digit millisecond range.
The team plans to further evaluate their framework with additional workloads and continue developing tools to make multi-tenancy management more accessible and secure.
# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presented a new approach to Kubernetes multi-tenancy called "three shade of fisolation" focused on multi-tenancy isolation.                                               |
|   2 | Combines control plane, data plane, and networking isolation using open source technologies.                                                                              |
|   3 | Multi-tenancy means sharing cluster resources among multiple tenants (users, teams, applications).                                                                        |
|   4 | Four key isolation requirements: data plane isolation, access boundaries, control plane isolation, and Kubernetes-like user experience.                                   |
|   5 | Motivations for workload isolation: security, performance (noisy neighbor problem), and cluster scope resource conflicts.                                                 |
|   6 | Existing models:                                                                                                                                                          |
|   7 | Cluster as a service: strong isolation, high operational overhead.                                                                                                        |
|   8 | Namespace as a service: shared cluster, limited cluster scope resources, noisy neighbor issue.                                                                            |
|   9 | Control plane as a service: virtual clusters, shared data plane, some security issues remain.                                                                             |
|  10 | Proposed approach targets: easy management, cost-effectiveness, open source, and strong tenant boundaries.                                                                |
|  11 | Uses four CNCF open source technologies: Kubeflex (control plane as a service), KubeVirt (VMs as pods), K3s (lightweight Kubernetes), OVN-Kubernetes (network isolation). |
|  12 | Each tenant gets a dedicated control plane (K3s), dedicated data plane (KubeVirt VMs), and isolated user-defined network (UDN).                                           |
|  13 | Data plane and control plane traffic are decoupled using separate networks.                                                                                               |
|  14 | Architecture allows tenants to interact with standard Kubernetes APIs and resources independently.                                                                        |
|  15 | Minimizes noisy neighbor problem by isolating resources at the VM level.                                                                                                  |
|  16 | Demo showed deployment of two distributed inference workloads (LLMD, VLM production stack) across two tenants.                                                            |
|  17 | External connectivity provided via a third UDN and proxy pod, maintaining network isolation.                                                                              |
|  18 | Experiments measured latency overhead; results showed minimal single-digit millisecond overhead.                                                                          |
|  19 | Ongoing work includes measuring overhead with real GPU workloads and further development of the management console.                                                       |
|  20 | Pattern is based on open source; can                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=24E4LDWThAE)