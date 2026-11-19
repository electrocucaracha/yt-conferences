---
layout: default
title: "Cluster Autoscaler Evolution - Kuba Tużnik, Google & Jack Francis, Microsoft"
nav_order: 14
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Cluster Auto Scaler (CA) is a Kubernetes component that dynamically provisions and deletes cloud provider VMs to match pending pod demands, aiming to optimize compute costs while maintaining cluste..."
resource: "https://www.youtube.com/watch?v=wbrdm7N9EfY"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Cluster Auto Scaler (CA) is a Kubernetes component that dynamically provisions and deletes cloud provider VMs to match pending pod demands, aiming to optimize compute costs while maintaining cluster capacity.
Historically, CA has faced significant maintenance challenges due to tight coupling with the Kubernetes scheduler and a monolithic repository structure that complicates innovation and leads to cloud provider forks like GKE and AKS.
To address these issues, recent updates have integrated complex scheduling features such as Dynamic Resource Allocation (DRA) and improved CSI node API handling, alongside new user-facing APIs for capacity buffers and quotas that allow for better cost and latency management.
A major architectural evolution, known as Work at the Scheduler (WAS), is proposed to replace the brittle internal simulation of scheduling logic with new APIs that enable direct communication between the auto scaler and the scheduler, thereby eliminating race conditions and allowing for pluggable scheduler support.
Finally, the project plans to refactor its codebase by extracting core logic into a separate library, upstreaming key features from GKE’s fork, and improving testability to ensure a more maintainable and extensible foundation for the community.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Cluster Auto Scaler (CA) provisions or deletes cloud VMs in response to pending pods to optimize compute costs.                                                               |
|   2 | CA operates by simulating Kubernetes scheduler behavior in an internal in-memory state to determine node requirements.                                                        |
|   3 | CA integrates with cloud provider APIs, the Kubernetes scheduler, and cluster nodes, primarily managing node groups with defined minimum and maximum bounds.                  |
|   4 | Full cluster autoscaling requires coordination with Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA) to adjust pod counts and resource requests.             |
|   5 | Historical tight coupling between CA and core Kubernetes led to maintenance challenges, particularly regarding the vendored kube scheduler.                                   |
|   6 | The monorepo structure containing over 40 cloud provider integrations complicates maintenance, CLI flag management, and documentation discoverability.                        |
|   7 | Cloud providers like GKE and AKS have forked CA to accelerate innovation, introducing features such as node group auto-provisioning and custom compute classes.               |
|   8 | Dynamic Resource Allocation (DRA) integration requires CA to track and modify resource claims, with production readiness targeted for Kubernetes 1.35.                        |
|   9 | CSI node API integration previously relied on workarounds that could cause race conditions, but improved simulation logic was implemented in CA 1.35.                         |
|  10 | New APIs include Capacity Buffer to maintain spare capacity for lower latency and Capacity Quota to restrict resource provisioning for specific node groups.                  |
|  11 | A proposed Template Node Info API aims to improve visibility and control over node templates, especially for scaling from zero nodes.                                         |
|  12 | The Work at the Scheduler (WAS) proposal seeks to replace internal simulation with direct APIs between auto scalers and schedulers to eliminate duplication and corner cases. |
|  13 | WAS introduces Potential Capacity and Preference APIs, allowing schedulers to evaluate potential nodes and express placement preferences.                                     |
|  14 | Architectural refactoring plans involve extracting core CA logic into a new repository to separate it from cloud provider-specific code.                                      |
|  15 | GKE-specific features, including node group auto-provisioning and custom compute classes, are planned for upstreaming into the core CA project.                               |
|  16 | Recent improvements include a new unit test framework, fixed end-to-end tests, and performance benchmarks to enhance testability and stability.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/wbrdm7N9EfY/hqdefault.jpg)](https://www.youtube.com/watch?v=wbrdm7N9EfY)

[Watch on YouTube](https://www.youtube.com/watch?v=wbrdm7N9EfY)
