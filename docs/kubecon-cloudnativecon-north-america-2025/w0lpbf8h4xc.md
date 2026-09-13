---
type: Video Note
title: "The Future of Virtualization in Kubernetes: What's Next for KubeVirt - Vladik Romanovsky, Red Hat"
description: "Vlatty Kromanski, a maintainer of the KubeVirt project, provided an update on the project's progress over the past year, highlighting community changes, new features, and future plans. KubeVirt, which extends the Kubernetes API to allow use..."
resource: https://www.youtube.com/watch?v=w0LPBf8H4xc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Vlatty Kromanski, a maintainer of the KubeVirt project, provided an update on the project's progress over the past year, highlighting community changes, new features, and future plans.
KubeVirt, which extends the Kubernetes API to allow users to run virtual machines alongside pods, recently applied for CNCF graduation and has established new special interest groups and working groups to address areas like control plane, confidential computing, and DRA integration.
Major technical advancements include a rearchitected decentralized live migration feature, improvements to migration controllers with priority queues, streamlined declarative hot plug operations, and expanded support for confidential computing technologies such as Intel TDX and AMD SEV-S.
Additional enhancements cover optimized I/O thread tuning, support for user-space network binding (PAST), seamless TCP migration, native OCI image volume mounting, and swap space configuration for VMs.
Looking ahead, the team is working on multiple hypervisor support, plugin mechanisms, incremental backup with CBT, VGPU live migration, PCI NUMA topology awareness, deeper DRA integration, and native VM templates, with opportunities for community involvement through meetings and communication channels.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Vlatty Kromanski is a maintainer of the Cubert project.                                                                                                        |
|   2 | Cubert is an operator that extends the Kubernetes API server to run virtual machines alongside pods using familiar Kubernetes APIs.                            |
|   3 | Virtualization stack runs in an unprivileged pod, subject to standard Kubernetes security policies.                                                            |
|   4 | Cubert applied for CNCF graduation; project started in 2016, joined CNCF in 2019.                                                                              |
|   5 | Adopted Kubernetes concepts like Special Interest Groups (SIGs); established SIGs for compute, storage, networking, and a new control plane SIG.               |
|   6 | Created new working groups for confidential computing and DRA integration.                                                                                     |
|   7 | Annual virtual Cubert summit had 260 attendees (17% increase); 12 sessions from various organizations; next year’s summit will be in-person alongside KubeCon. |
|   8 | Adopted an enhancement proposal process for new features and major code changes, requiring design proposals before development.                                |
|   9 | Central tracker introduced for features, showing design, PRs, issues, documentation, and maturity stage.                                                       |
|  10 | Three releases this year; 1.7 release upcoming.                                                                                                                |
|  11 | Major new feature: decentralized live migration, enabling migration of VMs between namespaces and clusters.                                                    |
|  12 | Migration controllers rearchitected; introduced a synchronizer controller and priority queue for migration operations.                                         |
|  13 | Streamlined hot plug operations to be declarative on VM objects.                                                                                               |
|  14 | Added initial support for confidential computing (IBM Z Secure Execution, Intel TDX, AMD SEV-S); working group created for this domain.                        |
|  15 | Introduced initial DRA support and formed a DRA working group to refine APIs.                                                                                  |
|  16 | Optimized I/O thread tuning API; added support for passthrough network binding and seamless TCP migration with passthrough.                                    |
|  17 | Adopted Kubernetes image volume for native OCI image mounting; transitioned from container disk.                                                               |
|  18 | VMs can now use swap space configured on the node.                                                                                                             |
|  19 | Developing multiple hypervisor support (first target: Microsoft MSHV) and plugin mechanisms for extensibility.                                                 |
|  20 | Working on incremental backup with CBT, V                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=w0LPBf8H4xc)