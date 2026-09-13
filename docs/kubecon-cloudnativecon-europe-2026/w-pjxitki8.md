---
type: Video Note
title: "Project Lightning Talk: OpenCost: Cost And Resource Management - Rajith Attapattu, Maintainer"
description: "The speaker introduces the OpenCost project, a vendor-neutral CNCF incubating initiative designed to provide unified cost allocation and asset visibility for Kubernetes clusters, including multi-cloud and on-premises environments. OpenCost..."
resource: https://www.youtube.com/watch?v=w-_PJXitKI8
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces the OpenCost project, a vendor-neutral CNCF incubating initiative designed to provide unified cost allocation and asset visibility for Kubernetes clusters, including multi-cloud and on-premises environments.
OpenCost features an extensible plug-in architecture, flexible deployment options, and is working on a Prometheus-less mode to address performance challenges in large clusters.
The project helps users understand and manage cluster costs by modeling overhead, allocation, and resource usage costs, enabling better workload and cluster rightsizing, and supporting internal chargeback calculations.
The speaker also clarifies that OpenCost originated from a donation of KubeCost to CNCF and now serves as the vendor-neutral base for downstream offerings.
A brief demo highlights OpenCost’s API-driven capabilities and emphasizes the importance of its underlying model and APIs over its user interface.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation covers the OpenCost project.                                                                                                                    |
|   2 | OpenCost is a vendor-neutral CNCF incubating project.                                                                                                        |
|   3 | Provides a unified model for allocations and assets.                                                                                                         |
|   4 | Offers visibility into Kubernetes clusters.                                                                                                                  |
|   5 | Supports multi-cloud and on-premises deployments with custom pricing sheets.                                                                                 |
|   6 | Features an extensible plug-in architecture (e.g., Datadog, Snowflake plugins).                                                                              |
|   7 | Flexible deployment model; currently uses Prometheus, with a promless mode in alpha.                                                                         |
|   8 | Community is encouraged to try the promless mode.                                                                                                            |
|   9 | Deep dive session on OpenCost architecture and modes scheduled for tomorrow.                                                                                 |
|  10 | OpenCost helps monitor and control Kubernetes cluster costs and efficiency.                                                                                  |
|  11 | Enables right-sizing of clusters and workloads.                                                                                                              |
|  12 | Many clusters are overprovisioned due to improperly sized workloads.                                                                                         |
|  13 | OpenCost provides visibility into cluster cost makeup: overhead, allocation, and resource usage costs.                                                       |
|  14 | Overhead costs include control plane and extra operational costs.                                                                                            |
|  15 | Allocation costs are billed by cloud vendors for CPU, memory, GPU, and disk.                                                                                 |
|  16 | Resource usage costs are based on activity, including network egress, cross-zone, and cross-region traffic.                                                  |
|  17 | OpenCost data structures can capture network traffic, though open source version lacks network cost calculation.                                             |
|  18 | Container is the smallest unit for allocation and resource usage costs.                                                                                      |
|  19 | Right-sizing containers and clusters reduces resource requests and costs.                                                                                    |
|  20 | Visibility into idle capacity allows manual or automated cluster right-sizing.                                                                               |
|  21 | Supports calculation of unit economics and internal chargebacks.                                                                                             |
|  22 | Difference between Kubecost and OpenCost: Kubecost was donated to CNCF and became OpenCost; vendors like Kubecost and Randoli provide downstream value-adds. |
|  23 | MCP server demo shown; built by an intern via LSF mentorship.                                                                                                |
|  24 | MCP server can answer cost-related queries (e.g., top five expensive namespaces).                                                                            |
|  25 | OpenCost has a UI and APIs; UI is basic but functional.                                                                                                      |
|  26 | Main value lies in the model, APIs, and MCP server.                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=w-_PJXitKI8)