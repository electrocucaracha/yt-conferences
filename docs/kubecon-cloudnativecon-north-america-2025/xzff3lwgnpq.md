---
type: Video Note
title: "Project Lightning Talk: Learn Kubernetes Best Practices With OpenCost - Matt Bolt , Maintainer"
description: "Matt Bolt, a co-creator and maintainer of OpenCost, introduces the CNCF incubating project designed to provide detailed visibility into Kubernetes spending by mapping cloud provider cost data to various Kubernetes resources. He emphasizes t..."
resource: https://www.youtube.com/watch?v=xzff3lWGnPQ
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Matt Bolt, a co-creator and maintainer of OpenCost, introduces the CNCF incubating project designed to provide detailed visibility into Kubernetes spending by mapping cloud provider cost data to various Kubernetes resources.
He emphasizes the importance of managing Kubernetes resource costs to optimize spending, avoid waste, and enable reinvestment in areas like security and scalability.
OpenCost supports major cloud providers, custom stacks, and measures costs across resources, including per-container network costs, allowing organizations to allocate expenses by namespace or team for use cases like chargebacks.
The project is open source, easily installed via Helm or manifests, and has received contributions from major industry players.
Recently, OpenCost integrated AI-driven analysis features, enabling users to receive automated cost insights and savings recommendations, further enhancing its utility for Kubernetes cost management.
# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Matt Bolt, co-creator and maintainer of OpenCost, principal engineer at IBM, presented at KubeCon Atlanta.                       |
|   2 | OpenCost is a CNCF incubating project providing visibility into Kubernetes spend.                                                |
|   3 | The project maps cloud provider cost data to all Kubernetes primitives, not just node-based costs.                               |
|   4 | Supports major cloud providers, Oracle, custom stacks for airgapped and on-prem environments.                                    |
|   5 | Measures anything that incurs cost in Kubernetes, including per-container network costs via a daemonset.                         |
|   6 | Use cases include:                                                                                                               |
|   7 | Differentiating costs between production (cost of goods) and development (R&D) namespaces.                                       |
|   8 | Allocating costs in shared cloud accounts by team using namespaces or resource labels.                                           |
|   9 | Enabling chargeback to specific teams.                                                                                           |
|  10 | OpenCost is the only open source project in the CNCF continuous optimization category.                                           |
|  11 | The project has been growing since 2019 with contributions from major cloud providers, Kubecost, Randoli, Adobe, and others.     |
|  12 | Installation is available via GitHub, Helm chart, standalone manifests, and other chart options (Kubecost Free, Randoli).        |
|  13 | Recent AI integration allows analysis and cost-saving recommendations using an MCP server and AI tools.                          |
|  14 | AI-generated insights include markdown guides for right-sizing containers and implementing savings plans based on OpenCost data. |
|  15 | Attendees encouraged to scan the QR code for more information and to connect after the talk.                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=xzff3lWGnPQ)