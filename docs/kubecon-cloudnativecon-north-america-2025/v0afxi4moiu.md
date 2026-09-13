---
type: Video Note
title: "Not Forking Around: Leveraging NRI To Extend Kubernetes at Scale - Johan Jensen & Wesley Bermbach"
description: "Johan and Wesley, software engineers at Uber, discuss their work on migrating Uber’s stateful container platform to Kubernetes, highlighting the challenges of unifying multiple proprietary and Kubernetes-based platforms. Uber’s stateful wor..."
resource: https://www.youtube.com/watch?v=V0afXi4mOiU
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Johan and Wesley, software engineers at Uber, discuss their work on migrating Uber’s stateful container platform to Kubernetes, highlighting the challenges of unifying multiple proprietary and Kubernetes-based platforms.
Uber’s stateful workloads rely on features like locally attached disks, fine-grained resource controls, and in-place container mutations, many of which are not natively supported by Kubernetes.
To bridge this gap without forking Kubernetes, Uber leveraged the Node Resource Interface (NRI), which allows for powerful, declarative modifications to containers at creation and runtime via plugins and custom resources.
They demonstrated how NRI enabled dynamic resource allocation and environment variable injection, even integrating AI-driven decisions, but noted the risks and complexity of using such low-level tooling.
Ultimately, Uber is moving away from NRI, aiming to upstream necessary features and reduce technical debt, and advises others to carefully weigh the trade-offs before adopting similar approaches.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Johan and Wesley are software engineers at Uber working on the stateful container platform.                                                                                                                                                                                |
|   2 | Uber operates 1.5 million trips per hour in 70 countries, running 8 million containers on over 200,000 hosts.                                                                                                                                                              |
|   3 | Uber has multiple container platforms: stateful (databases, storage), stateless (services, APIs), and batch processing (analytics).                                                                                                                                        |
|   4 | Stateless and batch platforms have migrated to Kubernetes; stateful remains on a proprietary platform.                                                                                                                                                                     |
|   5 | Unifying platforms on Kubernetes aims to reduce fragmentation and enable common tooling, observability, policy, and service mesh.                                                                                                                                          |
|   6 | Proprietary platform supports features not natively available in Kubernetes, especially for stateful workloads.                                                                                                                                                            |
|   7 | Key features needed: locally attached disks for low latency/high throughput, resource mutability, in-place changes, cgroup controls, CPU sets, workload/pod-level resources, dynamic container labels, container runtime policies (e.g., OOM score, scheduler priorities). |
|   8 | Migrating to Kubernetes risks losing critical features relied on by business and stakeholders.                                                                                                                                                                             |
|   9 | Forking Kubernetes is tempting but leads to slower upgrades, technical debt, and community isolation.                                                                                                                                                                      |
|  10 | Best solution is to upstream features, but Uber-specific needs may not align with community priorities.                                                                                                                                                                    |
|  11 | Node Resource Interface (NRI) allows hooking into the container lifecycle to mutate containers before runtime.                                                                                                                                                             |
|  12 | NRI works with containerd, enabling plugins to modify OCI bundles (resources, mounts, cgroups) before container creation.                                                                                                                                                  |
|  13 | Uber built a custom pod extension (CRD) to declaratively specify needed features, such as pod-level resources and CPU sets.                                                                                                                                                |
|  14 | Uber’s scheduler creates pods and pod extension resources; NRI plugin reads these and mutates containers accordingly.                                                                                                                                                      |
|  15 | NRI supports both creation and update flows, allowing out-of-band resource/configuration changes to running containers.                                                                                                                                                    |
|  16 | Demo showed an NRI plugin using OpenAI to dynamically set resources and environment variables for pods.                                                                                                                                                                    |
|  17 | NRI is powerful but                                                                                                                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=V0afXi4mOiU)