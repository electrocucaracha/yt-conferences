---
layout: default
title:
  "Hybrid-Confidential-Cloud: Democratize Secure AI With GPUs and Confidential
  Contain... Zvonko Kaiser"
nav_order: 100
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this session, Kaiser from Nvidia’s cloud native team discusses the
  challenges and solutions for securing AI workloads using confidential containers
  and cloud GPUs. He explains that containers alone do not provide isolation and emphasizes...
resource: https://www.youtube.com/watch?v=afL3PqVEzVo
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this session, Kaiser from Nvidia’s cloud native team discusses the challenges and solutions for securing AI workloads using confidential containers and cloud GPUs.
He explains that containers alone do not provide isolation and emphasizes the need for sandboxing and confidential computing, where workloads are protected from untrusted infrastructure through encrypted memory and state.
The talk outlines a layered security approach: protecting containers, nodes, and ultimately the entire Kubernetes cluster by minimizing shared state, using out-of-band attestation, and establishing strong workload and node identities.
Kaiser describes creating isolated overlays for compute, networking, storage, and control plane, advocating for per-tenant control planes and the elimination of nested virtualization to reduce attack surfaces.
He addresses practical concerns such as performance overhead, identity management, GPU resource sharing, and the importance of reproducible builds for attestation, concluding that confidential containers enable portable, verifiable, and secure AI deployments across hybrid cloud environments, with ongoing work to address supply chain, side-channel, and physical attacks.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Containers are primarily a packaging mechanism, not for isolation; sandboxing is needed for trustworthiness.                           |
|   2 | Confidential compute reverses the threat model: workloads do not trust the infrastructure.                                             |
|   3 | Confidential VMs encrypt memory, state, and registers to protect workloads from infrastructure access.                                 |
|   4 | Full stack attestation is required, from silicon up to the container, using signed images and SBOMs.                                   |
|   5 | Kubernetes is the platform of choice for AI/ML pipelines; protecting the entire Kubernetes cluster is necessary.                       |
|   6 | Private data processing is challenging; 66% of enterprises have over 50% of private data unprotected.                                  |
|   7 | Internal teams may not trust each other, requiring stack protection even within companies.                                             |
|   8 | Kubernetes clusters have a large shared state; compromise of a node can lead to cluster-wide breaches.                                 |
|   9 | Observer tools like eBPF have circular dependency issues; out-of-band attestation is needed.                                           |
|  10 | Minimize shared state, use out-of-band measurements, and establish strong identities for compute, network, storage, and control plane. |
|  11 | Compute overlay uses confidential containers in trusted execution environments (TEE) like SEV, TDX, or CCA.                            |
|  12 | Networking overlay should be identity-based, isolating workloads and avoiding global meshes for confidential data.                     |
|  13 | Confidential storage must be encrypted, integrity-protected, and replay-resistant, with per-tenant isolation.                          |
|  14 | Control plane overlay: per-tenant control planes, possibly running in VMs or confidential containers, to eliminate shared state.       |
|  15 | Avoid nested virtualization for performance and security; use universal launch interfaces for portability.                             |
|  16 | Type 1 hypervisors reduce attack surface; measure and attest every platform stage before releasing keys or certificates.               |
|  17 | Deployment models can be tuned for density or strict isolation, depending on threat model.                                             |
|  18 | Prefer SR-IOV or PF passthrough for network and GPU isolation; storage keys released only after attestation.                           |
|  19 | All components are measured and                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=afL3PqVEzVo)
