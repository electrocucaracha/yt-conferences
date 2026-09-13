---
type: Video Note
title: "Project Lightning Talk: Namespace Multi-Tenancy, But All The Problems Related To It - Hristo Hristov"
description: "Christopher, a maintainer of the CNCF sandbox project Capsule, discusses the challenges of scaling Kubernetes environments, particularly around namespace multi-tenancy. As organizations grow, managing hundreds of microservices and namespace..."
resource: https://www.youtube.com/watch?v=-imwG5MP2aw
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Christopher, a maintainer of the CNCF sandbox project Capsule, discusses the challenges of scaling Kubernetes environments, particularly around namespace multi-tenancy.
As organizations grow, managing hundreds of microservices and namespaces becomes complex and costly, often leading to inefficient resource use and high cloud expenses.
Capsule addresses these issues by introducing the concept of a "tenant," which groups multiple namespaces and provides isolated resource pools and configurable policies, enabling effective multi-tenancy without the overhead of managing multiple clusters.
The project leverages Kubernetes primitives, integrates with key CNCF tools like Argo CD, Rancher, and Velero, and supports GitOps workflows.
Capsule is open for collaboration, offers enterprise support through partners, and invites interested users to connect via their pavilion, Slack, website, or GitHub.
# Main Points

|   # | Main point                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------- |
|   1 | Christopher is a project maintainer for Capsule, a CNCF sandbox project launched about 4 years ago.                   |
|   2 | Capsule addresses multi-tenancy, specifically namespace multi-tenancy in Kubernetes.                                  |
|   3 | As companies scale, managing hundreds of microservices and namespaces becomes difficult and slow.                     |
|   4 | RBAC management becomes complex and hard to track.                                                                    |
|   5 | Developers often bypass limitations by creating more namespaces to access more resources.                             |
|   6 | Multi-tenancy at the cluster level (one cluster per team or data) leads to operational complexity and high costs.     |
|   7 | Cloud provider costs increase significantly with multiple clusters.                                                   |
|   8 | Capsule introduces the concept of a "tenant," which wraps multiple namespaces together.                               |
|   9 | Tenants provide isolated boundaries for developers, allowing them to work independently.                              |
|  10 | Resource pools are assigned per tenant, letting developers manage their own resource consumption.                     |
|  11 | Tenant configurations allow administrators to set guidelines for resource usage.                                      |
|  12 | Capsule achieves efficient multi-tenancy with self-service capabilities for developers at a lower cost.               |
|  13 | Capsule uses Kubernetes primitives and configurations to manage permissions, user groups, service accounts, and RBAC. |
|  14 | Network policies from projects like Calico and Cilium are replicated within Capsule.                                  |
|  15 | Recently released resource pools encapsulate tenant resources and enforce quotas.                                     |
|  16 | Tenant owners can define policies and configurations at the tenant level.                                             |
|  17 | Developers can create namespaces within their assigned tenants.                                                       |
|  18 | Capsule integrates with CNCF tools such as Argo CD, Rancher, Velero, and supports GitOps workflows.                   |
|  19 | Local adopters include Odyssey North and Kubermatic.                                                                  |
|  20 | Enterprise support is available from Qualitics and Pixie Labs.                                                        |
|  21 | Capsule team will be available for demos at the project pavilion (Wednesday, 14:00-17:00, P13A).                      |
|  22 | Community can connect via Kubernetes Slack (/capsule), projectcapsule.dev, and GitHub.                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-imwG5MP2aw)