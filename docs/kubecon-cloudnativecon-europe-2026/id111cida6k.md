---
type: Video Note
title: "Confidential Platforms for Regulated Industries - William Rizzo, Mirantis"
description: "The speaker describes an experiment initiated to maximize the utilization of expensive trading hardware, which typically operates for only six hours daily and remains idle otherwise due to regulatory constraints. The solution involved creat..."
resource: https://www.youtube.com/watch?v=id111CIDa6k
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker describes an experiment initiated to maximize the utilization of expensive trading hardware, which typically operates for only six hours daily and remains idle otherwise due to regulatory constraints.
The solution involved creating ephemeral Kubernetes clusters using a hosted control plane pattern, leveraging tools such as Cluster API, Cordant, Kyverno for policy enforcement, Flux for GitOps, and MetalLB for on-prem load balancing.
A mutating admission webhook was developed to transparently inject confidential container runtimes into deployments, ensuring compliance and reducing developer cognitive load.
The system employs a spot scheduling mechanism, allowing teams to donate idle hardware for cluster expansion during off-hours, managed by the open-source FiveSpot project.
Future plans include integrating immutable operating systems with Chyros, trusted boot with TPM, and workload attestation, while current workloads are limited to internal experiments and development rather than production use.
# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Initial challenge: maximize utilization of expensive trading hardware used only ~6 hours/day.                                                                                |
|   2 | Goal: encapsulate K0S Kubernetes engine and related binaries for use on audited systems, then remove encapsulation for audit software before trading.                        |
|   3 | Environment: ~10,000 expensive systems, under strict regulatory audit, mostly idle outside trading hours.                                                                    |
|   4 | Problems addressed: regulatory burden, fragmented tooling, underutilized hardware.                                                                                           |
|   5 | Solution: ephemeral Kubernetes clusters using hosted control plane pattern via Cluster API.                                                                                  |
|   6 | Management cluster hosts control planes for managed clusters as pods.                                                                                                        |
|   7 | Used Mirantis Cordant for platform control plane, state and cluster management, and observability.                                                                           |
|   8 | Cluster API used for cluster lifecycle management.                                                                                                                           |
|   9 | Kyverno used for policy enforcement.                                                                                                                                         |
|  10 | Flux used for GitOps-based configuration management.                                                                                                                         |
|  11 | MetalLB provides on-prem load balancer services for control planes.                                                                                                          |
|  12 | Containerd and Kata Confidential Containers runtime used for confidential workloads.                                                                                         |
|  13 | Transparent runtime injection via custom mutating admission webhook; switches runtime class to Kata for all deployments except certain namespaces (e.g., kube-system, flux). |
|  14 | Policies enforced: image pull from internal registry, resource limits, naming conventions for audit compliance.                                                              |
|  15 | All images and binaries stored in internal registry due to air-gapped, regulated environment.                                                                                |
|  16 | Spot scheduling: after trading hours, teams can donate idle hardware for ephemeral clusters; workloads run overnight, servers drained and released before trading resumes.   |
|  17 | Not currently using Trusted Execution Environments (TEE) due to hardware limitations; uses QEMU hypervisor instead.                                                          |
|  18 | Security and compliance are integrated into the platform, reducing developer cognitive load.                                                                                 |
|  19 | Next phase: use Chyros framework for immutable OS images, TPM-based trusted boot, attestation for OS and workloads.                                                          |
|  20 | Exploring confidential runtime with GPUs (experimental).                                                                                                                     |
|  21 | FiveSpot project enables time-based, g                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=id111CIDa6k)