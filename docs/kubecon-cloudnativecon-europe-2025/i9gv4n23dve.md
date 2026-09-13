---
type: Video Note
title: "How the SIG-Multicluster API Specifications Are Used for Real World... August Simonelli & Ryan Zhang"
description: "The SIG multicluster API specifications are used for real-world multicluster management, and August Simonelli from Red Hat will discuss the standards and their implementation in the open cluster management project (OCM) and Kubby Fleet. The..."
resource: https://www.youtube.com/watch?v=I9GV4N23dvE
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The SIG multicluster API specifications are used for real-world multicluster management, and August Simonelli from Red Hat will discuss the standards and their implementation in the open cluster management project (OCM) and Kubby Fleet.
The OCM project provides a single pane of glass for managing multiple clusters, while Kubby Fleet is a recently contributed CNCF project that offers similar functionality with additional features such as scheduling capabilities and property-based scheduling.
The two projects will demonstrate how to deploy workloads across multiple clusters using the multicluster service API and placement, respectively.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The SIG multicluster API specifications define standards for real-world multicluster management.                                                               |
|   2 | The four basic APIs are:                                                                                                                                       |
|   3 | About API: defines properties for a cluster                                                                                                                    |
|   4 | Multicluster services API: allows different clusters to have the same service name and namespace sameness                                                      |
|   5 | Work API: allows resources to be placed in clusters from the control plane                                                                                     |
|   6 | Cluster profile API: provides a single pane of glass for managing multiple clusters                                                                            |
|   7 | The open cluster management project (OCM) implements these APIs and adds features such as dynamic placement and continuous deployment.                         |
|   8 | Kubby Fleet is a recently contributed CNCF project that builds on OCM's work, adding features like property-based scheduling and continuous deployment.        |
|   9 | Both OCM and Kubby Fleet aim to provide a unified view of multicluster management and make it easier for projects to contribute and integrate with each other. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=I9GV4N23dvE)