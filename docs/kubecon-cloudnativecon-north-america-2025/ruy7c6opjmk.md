---
type: Video Note
title: "Offline, Not Off-Limits: Edge Fleet Management With Argo CD - Alexander Matyushentsev, Akuity"
description: "In this talk, Alexander Matense, co-creator of Argo CD, discusses strategies for managing Kubernetes clusters at the edge using Argo CD, particularly in environments with limited connectivity and resources. He describes challenges faced by..."
resource: https://www.youtube.com/watch?v=rUy7c6OpjMk
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Alexander Matense, co-creator of Argo CD, discusses strategies for managing Kubernetes clusters at the edge using Argo CD, particularly in environments with limited connectivity and resources.
He describes challenges faced by customers running many small, resource-constrained clusters—such as those in retail, vehicles, or even airplanes—where traditional Argo CD setups are impractical due to connectivity and resource limitations.
To address these, the team adopted Argo CD Core, a lightweight distribution that omits unnecessary components, and leveraged ApplicationSets with an opinionated Git directory structure to declaratively manage applications, group-specific overrides, and cluster-specific configurations.
Visibility into deployments was achieved using Argo CD notifications integrated with Git commit statuses, while local Git servers with git-sync ensured clusters could access updates even when intermittently disconnected.
The Q&A session covered topics like compliance, group promotion strategies, upgrade paths, scalability, caching, and air-gapped deployments, with Matense emphasizing that while Argo CD was not originally designed for edge management, it has proven to be a suitable and adaptable solution for these scenarios.
# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Argo CD is used to manage Kubernetes clusters at the edge with limited connectivity and resources.                                                                  |
|   2 | Typical edge clusters are small, resource-constrained, and often have unreliable or low-bandwidth network connections.                                              |
|   3 | Customers use Kubernetes at edge locations such as retail stores, vehicles, planes, drones, and smart collars.                                                      |
|   4 | Teams manage many small clusters as cattle, not pets, using a single Git repository to represent cluster state.                                                     |
|   5 | Clusters are grouped for different customer needs, with flexibility for per-cluster overrides and experimentation.                                                  |
|   6 | Standard Argo CD multi-cluster management is unsuitable due to lack of inbound connectivity to edge clusters.                                                       |
|   7 | Solution: Install Argo CD directly on each managed cluster using Argo CD Core, a lightweight distribution without unnecessary components (e.g., UI, DEX, HA Redis). |
|   8 | Argo CD Core reduces resource usage and allows CLI and local UI access for administrators.                                                                          |
|   9 | ApplicationSet and an opinionated directory structure in Git are used to declaratively manage applications, group overrides, and cluster-specific configurations.   |
|  10 | ApplicationSet uses base directories for common apps, group directories for overrides, and cluster directories for specific overrides.                              |
|  11 | Visibility is achieved using Argo CD Notifications to update Git commit status or send webhooks on deployment success/failure.                                      |
|  12 | To handle connectivity loss, an in-cluster Git server with git-sync is used to cache manifests locally, ensuring clusters can apply changes when reconnected.       |
|  13 | Resource protection feature in Argo CD 3.0.0 requires human approval before deleting critical resources like namespaces.                                            |
|  14 | ApplicationSet applies overrides in parallel across clusters; no promotion pools or ceremonies are used.                                                            |
|  15 | Performance is not an issue for small clusters; improvements like limiting Git remote calls and using repo-server caching were made for scale.                      |
|  16 | For airgapped environments, each cluster uses a local Git repo; multiple upstream repos must be                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=rUy7c6OpjMk)