---
type: Video Note
title: "CRI-O: Faster Pulls, Better Metrics, and a Future Beyond Images - Sohan Kunkerkar & Ayato Tokubi"
description: "In this CubeCon session, San Kerkar and Ayatu Tokobi from Red Hat provide an overview and updates on CRI-O, a Kubernetes container runtime. They discuss recent features such as server-side streaming RPCs to address message size limits in hi..."
resource: https://www.youtube.com/watch?v=en2oz2BWHW8
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this CubeCon session, San Kerkar and Ayatu Tokobi from Red Hat provide an overview and updates on CRI-O, a Kubernetes container runtime.
They discuss recent features such as server-side streaming RPCs to address message size limits in high-density nodes, and the move towards collecting container statistics directly from the runtime instead of CAdvisor to reduce duplication and improve architecture, though this remains in alpha due to outstanding issues in kubelet.
The team introduces the "additional artifact stores" feature, allowing CRI-O to read OCI artifacts from multiple directories, which benefits machine learning workloads, prepopulated caches, and shared storage scenarios.
Security enhancements include configurable TLS settings and the provision of OpenVEX vulnerability reports.
They also detail improvements in memory Quality of Service (QoS), addressing kernel and scheduler gaps to better protect guaranteed and burstable pods.
Finally, the session covers peer-to-peer image distribution using Spiegel, which reduces bandwidth usage for large container images by enabling decentralized sharing across nodes, and discusses future directions such as P2P-aware scheduling to further optimize image distribution in Kubernetes clusters.
# Main Points

|   # | Main point                                                                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | San Kerkar and Ayatu Tokobi introduced themselves as Cryo maintainers and contributors.                                                                                                                                        |
|   2 | Agenda: Introduction to Cryo, Cryo updates, SIG Node work, peer-to-peer image distribution, demo, Q&A.                                                                                                                         |
|   3 | Cryo is a Kubernetes container runtime implementing the Container Runtime Interface (CRI) and supports OCI-compliant images.                                                                                                   |
|   4 | Cryo emphasizes simplicity, upstream feature alignment, and is a CNCF graduated project.                                                                                                                                       |
|   5 | Cryo releases are synchronized with Kubernetes releases.                                                                                                                                                                       |
|   6 | Cryo communicates with kubelet to manage containers and pods on nodes.                                                                                                                                                         |
|   7 | CI List Streaming: Addresses gRPC message size limits by introducing server-side streaming RPCs for listing containers, pods, images, and stats, preventing failures on high-density nodes; entering alpha in Kubernetes 1.36. |
|   8 | CI Stats: Proposes collecting container and pod stats via the runtime instead of cAdvisor to eliminate duplication; remains in alpha due to kubelet still running cAdvisor code path.                                          |
|   9 | Additional Artifact Stores: Introduced in Cryo 1.35 as an experimental feature, allowing read-only directories for OCI artifacts to support ML workloads, prepopulated caches, and shared storage across nodes.                |
|  10 | Security Updates:                                                                                                                                                                                                              |
|  11 | Configurable TLS settings for metrics and streaming endpoints (min version, cipher suites) for compliance.                                                                                                                     |
|  12 | OpenVEX vulnerability reports provided for Cryo releases.                                                                                                                                                                      |
|  13 | Memory QoS:                                                                                                                                                                                                                    |
|  14 | Addresses kernel reclaiming memory from guaranteed pods due to lack of communication of memory requests.                                                                                                                       |
|  15 | Memory protection now uses memory.min for guaranteed pods and QoS class-level protection for burstable pods; best-effort pods have no protection.                                                                              |
|  16 | Prometheus metrics added for observability.                                                                                                                                                                                    |
|  17 | Fixes for unified field updates in container resource changes included in 1.36.                                                                                                                                                |
|  18 | Peer-to-Peer Image Distribution:                                                                                                                                                                                               |
|  19 | Spiegel enables decentralized, peer-to-peer OCI image distribution, reducing bandwidth for large images.                                                                                                                       |
|  20 | Integration with Cryo involves a blob cache layer for compressed layers and metadata tra                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=en2oz2BWHW8)