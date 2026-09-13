---
type: Video Note
title: "Meta’s Kubernetes-based Portable AI Research Environment - Shaun Hopper, Meta & Navarre Pratt"
description: "In this talk, Navar Pratt from CoreWeave and Sean Hopper from Meta describe Meta’s transition to a portable, Kubernetes-based AI research environment in collaboration with CoreWeave. Initially, Meta’s AI training infrastructure was tied to..."
resource: https://www.youtube.com/watch?v=ts7bI51gRCo
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Navar Pratt from CoreWeave and Sean Hopper from Meta describe Meta’s transition to a portable, Kubernetes-based AI research environment in collaboration with CoreWeave.
Initially, Meta’s AI training infrastructure was tied to specific cloud providers and relied on machine images and non-containerized components, making portability and scaling difficult, especially as GPU demand surged.
By adopting Kubernetes and CoreWeave’s “Sunk” (Slurm on Kubernetes) platform, Meta was able to containerize its research clusters, streamline deployment with Helm charts and Flux, and abstract away Kubernetes complexity for researchers, who continue to use familiar Slurm interfaces.
The new architecture enables robust observability and telemetry, with deep integration into both CoreWeave and Meta’s monitoring systems, allowing for full-stack visibility and efficient troubleshooting at scale.
The presenters emphasize the benefits of container-based login environments, the importance of full-stack observability for large-scale AI workloads, and the use of standardized telemetry protocols (OTLP) to maintain portability and integration across diverse cloud environments.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Meta and CoreWeave collaborated to build a portable, Kubernetes-based AI research environment.                                                     |
|   2 | CoreWeave provides large-scale, bare metal Kubernetes clusters with many GPUs, focused on AI workloads.                                            |
|   3 | Meta needed portability due to GPU shortages and existing training platforms being locked to specific cloud providers.                             |
|   4 | Meta’s research clusters use Slurm for job scheduling, now running on Kubernetes for portability.                                                  |
|   5 | Previously, Slurm components ran on machine images; now, most components, including slurmd, run in containers on Kubernetes.                       |
|   6 | Chef-based host configuration was replaced by Kubernetes-driven node state management.                                                             |
|   7 | Architecture uses a two-cluster model: one for fixed ingress/egress and telemetry, one as an isolated HPC cluster.                                 |
|   8 | CoreWeave’s “Sunk” (Slurm on Kubernetes) provides Slurm-based training environments with custom CRDs for scaling, rolling updates, and job safety. |
|   9 | Login pods provide SSH access for researchers, abstracting Kubernetes complexity and maintaining a familiar Slurm CLI experience.                  |
|  10 | Slurm syncer component reconciles job and node states between Slurm and Kubernetes, enabling observability and node management.                    |
|  11 | Deep integration with observability platforms is essential for large-scale AI workloads; metrics and logs are collected from all hardware layers.  |
|  12 | Telecaster product forwards telemetry from CoreWeave clusters to customer environments, supporting private networking and custom endpoints.        |
|  13 | Meta uses OTLP (OpenTelemetry Protocol) to standardize telemetry data, enabling portability and integration with internal systems.                 |
|  14 | Helm and Flux are used for deploying and managing Slurm clusters, allowing customization and CI/CD integration.                                    |
|  15 | Container-based login environments are lighter and easier to manage than VMs, though VMs offer benefits like snapshotting.                         |
|  16 | Node failures are managed by Kubernetes controllers; Slurm handles workload scheduling and draining nodes as needed.                               |
|  17 | Observability includes full stack metrics, logs,                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ts7bI51gRCo)