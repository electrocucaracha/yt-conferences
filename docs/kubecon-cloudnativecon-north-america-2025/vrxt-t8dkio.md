---
type: Video Note
title: "Maximizing Global Potential: Cost-Op... Wei Jiang, Jingkang Jiang, Michael McCune & Praseeda Sathaye"
description: "The session discusses strategies for cost-optimized, resilient GPU workload scheduling across multiple cloud providers and regions using open-source technologies like Kubernetes, Cluster API, Carpenter, and Karmada. The speakers introduce t..."
resource: https://www.youtube.com/watch?v=VrXt_T8DkIo
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session discusses strategies for cost-optimized, resilient GPU workload scheduling across multiple cloud providers and regions using open-source technologies like Kubernetes, Cluster API, Carpenter, and Karmada.
The speakers introduce themselves and outline the main challenges in GPU provisioning, including capacity shortages, high costs, regional limits, and the complexity of managing resources across clouds.
Their solution treats all cloud providers as a unified GPU resource pool, leveraging Kubernetes-native tools to automate cluster deployment, node scaling, and workload distribution.
They address specific challenges such as traffic routing proportional to replica distribution, balancing cost and reliability with a mix of on-demand and spot instances, dynamic adjustment of workloads based on real-time capacity and pricing, and handling spot interruptions.
The team demonstrates their approach and acknowledges current limitations, such as setup complexity and limited provider support, while outlining future improvements for greater simplicity and broader compatibility.
The Q&A highlights ongoing challenges in networking, security, and authentication across clouds, as well as the potential for integrating on-premises resources, emphasizing that while the approach is complex and evolving, it is increasingly in demand and under active development.
# Main Points

|   # | Main point                                                                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on cost-optimized, multi-region, multi-cloud GPU workload scheduling using open source tools like Carpenter and Karmada.                                                                  |
|   2 | Speakers: JK (Cloud Pilot AI, GCP Carpenter maintainer), Michael McCune (Red Hat, SIG cloud provider, Carpenter/Cluster API maintainer), Prashida Sartier (Amazon, product manager for internet ingress). |
|   3 | Key challenges in GPU provisioning: capacity shortages, high cost, regional limits, and unreliability of spot instances.                                                                                  |
|   4 | No single cloud provider guarantees capacity and cost efficiency at scale.                                                                                                                                |
|   5 | Solution: treat all cloud providers as a global GPU resource pool, distributing workloads across clouds and regions.                                                                                      |
|   6 | Managing such a pool is complex: requires cross-cloud scheduling, failover handling, spot interruption management, and performance consistency.                                                           |
|   7 | Kubernetes-native tools used: Cluster API (infrastructure management), Carpenter (automated node provisioning and upgrades), Karmada (multi-cluster workload scheduling).                                 |
|   8 | Architecture: hub-spoke topology with a management cluster (running Cluster API and Karmada) creating and managing spoke clusters on AWS, GCP, etc., each running Carpenter.                              |
|   9 | Five main challenges addressed:                                                                                                                                                                           |
|  10 | Traffic routing proportional to replica distribution across clusters.                                                                                                                                     |
|  11 | Cost-effective GPU provisioning balancing spot and on-demand instances.                                                                                                                                   |
|  12 | Smart initial replica distribution based on real-time GPU availability.                                                                                                                                   |
|  13 | Handling spot interruptions with automated rescheduling.                                                                                                                                                  |
|  14 | Dynamic adjustment of replica distribution based on spot node lifetimes and availability.                                                                                                                 |
|  15 | Implementation includes a global load balancer controller that adjusts backend weights based on replica counts per cluster.                                                                               |
|  16 | Workloads split into static (on-demand, stable) and adaptive (spot, cost-efficient) parts.                                                                                                                |
|  17 | Adaptive replicas are dynamically redistributed based on recent spot node lifetimes and cluster health.                                                                                                   |
|  18 | Demo showed deployment and failover across AWS and GCP clusters.                                                                                                                                          |
|  19 | Current limitations: complex setup,                                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=VrXt_T8DkIo)