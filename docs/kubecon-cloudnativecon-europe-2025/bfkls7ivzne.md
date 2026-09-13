---
type: Video Note
title: "Tutorial: Mind Your Pod's Business: Netwo... Surya Seetharaman, Miguel Duarte Barroso & Keith Burdis"
description: "The speaker discusses network segmentation in Kubernetes, highlighting the importance of isolating pods across different networks to ensure compliance and security. They explain how cluster-wide services can be isolated using UDNS (User-Def..."
resource: https://www.youtube.com/watch?v=bFKls7IvzNE
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses network segmentation in Kubernetes, highlighting the importance of isolating pods across different networks to ensure compliance and security.
They explain how cluster-wide services can be isolated using UDNS (User-Defined Networking) and demonstrate its functionality by creating a cluster UDN and virtual machines in separate namespaces.
The speaker also touches on the concept of interconnecting UDNS, which allows for cross-network communication between pods, but notes that it's still an experimental feature.
They conclude by highlighting the availability of UDNS in Kubernetes 1.32 and encouraging attendees to try it out.
# Main Points

|   # | Main point                                                                   |
| --: | ---------------------------------------------------------------------------- |
|   1 | UDN (User-Defined Network) creation without setting a CR (Cluster Resource). |
|   2 | Kubernetes cluster IP range for services and pods.                           |
|   3 | Network policies take precedence over segmentation.                          |
|   4 | Interconnecting UDNS allows for cross-network communication.                 |
|   5 | Cluster-wide service cider shared by all UDNs.                               |
|   6 | Egress to the internet works from within VMs.                                |
|   7 | East-west traffic works as expected.                                         |
|   8 | Live migration of VMs with established TCP connections.                      |
|   9 | IP address persistence using IPM claims.                                     |
|  10 | Colored enterprise networks can be isolated from each other.                 |
|  11 | UDNS is platform-agnostic and available in Kubernetes 1.32.                  |
|  12 | OVN (Open Virtual Network) supports live migration on cloud platforms.       |
|  13 | Labels are used to identify namespaces for UDNs.                             |
|  14 | Finalizers ensure workloads are deleted before network deletion.             |
|  15 | Custom resource definitions can be used to delete finalizers.                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=bFKls7IvzNE)