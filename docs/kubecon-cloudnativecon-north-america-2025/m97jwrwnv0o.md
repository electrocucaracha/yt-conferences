---
type: Video Note
title: "Untangling CSI: Powering Persistent Storage for KubeVirt - Brenda McLaren & Chris Keller, Red Hat"
description: "In this presentation, Brendan McLaren and Chris Keller from Red Hat discuss the role of the Container Storage Interface (CSI) in simplifying and standardizing persistent storage management within Kubernetes, especially when running virtual..."
resource: https://www.youtube.com/watch?v=m97jWRWNv0o
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Brendan McLaren and Chris Keller from Red Hat discuss the role of the Container Storage Interface (CSI) in simplifying and standardizing persistent storage management within Kubernetes, especially when running virtual machines with KubeVirt.
They explain that while Kubernetes made compute agile and scalable, storage introduced complexity due to varying vendor implementations, which CSI addresses by providing a universal API for dynamic provisioning, lifecycle management, and seamless integration across different storage backends.
The speakers detail the architecture of CSI drivers, including controller and node plugins, and emphasize the importance of understanding the differences between drivers, conducting performance testing, and ensuring compatibility and up-to-date versions.
They highlight key features such as dynamic provisioning, snapshots, clones, topology awareness, and high availability, and caution against common pitfalls like assuming all CSI drivers are equal or neglecting scalability and backup considerations.
Looking ahead, they mention upcoming enhancements like change block tracking and improved replication support, advising users to stay current with CSI developments and carefully evaluate vendor capabilities for successful storage integration in Kubernetes environments.
# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes simplifies compute but adds complexity to storage, requiring abstraction layers.                                                                           |
|   2 | Each storage vendor provides its own CSI (Container Storage Interface) driver, which behave differently.                                                              |
|   3 | Adding KubeVirt (virtual machines on Kubernetes) increases storage management complexity, including latency, snapshot, and ReadWriteMany support for live migrations. |
|   4 | CSI acts as a universal translator between Kubernetes and storage providers, standardizing storage management via a consistent API.                                   |
|   5 | CSI enables dynamic provisioning, resizing, snapshotting, cloning, and cleanup of storage volumes.                                                                    |
|   6 | CSI replaced in-tree plugins, decoupling storage integrations from Kubernetes core and improving upgrade independence and security.                                   |
|   7 | CSI drivers consist of vendor-provided components (controller and node plugins) and sidecars (provided by SIG Storage) that bridge drivers and the Kubernetes API.    |
|   8 | Controller plugin handles backend storage provisioning and volume access; node plugin mounts and formats volumes on nodes.                                            |
|   9 | CSI node components typically run as a DaemonSet on all cluster nodes; controller components can run on worker or control plane nodes.                                |
|  10 | Persistent Volume Claims (PVCs) trigger the external provisioner to create volumes via the controller and attach them to nodes.                                       |
|  11 | CSI supports both traditional enterprise storage (SAN/NAS) and software-defined storage, providing a consistent interface.                                            |
|  12 | KubeVirt uses PVCs for VM storage; data volumes specify base OS images and support cloning or downloading images.                                                     |
|  13 | ReadWriteMany volumes are essential for VM live migration, allowing simultaneous mounting on multiple nodes.                                                          |
|  14 | Universal observability and administration are provided across containers and VMs.                                                                                    |
|  15 | Key pitfalls: assuming all CSI drivers are equal, ignoring performance tests, not considering API/scalability limits, and neglecting backup/failover strategies.      |
|  16 | Stay current with CSI drivers and ensure compatibility with Kubernetes versions.                                                                                      |
|  17 | Key CSI capabilities                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=m97jWRWNv0o)