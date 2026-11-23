---
layout: default
title: "Industrial-Grade AI on OpenStack HPC: Real-World Use Cases & Future Roadmaps"
nav_order: 83
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This panel discussion explores the integration of industrial-grade AI with OpenStack, highlighting diverse user needs ranging from sensitive data handling in trusted research environments to batch ..."
resource: "https://www.youtube.com/watch?v=nxwtmRSliRo"
youtube_stats:
  view_count: 82
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

This panel discussion explores the integration of industrial-grade AI with OpenStack, highlighting diverse user needs ranging from sensitive data handling in trusted research environments to batch training via Slurm and interactive Jupyter notebook experiences.
The speakers emphasize the growing hardware diversity, including specialized accelerators and ARM-based systems, and note that while end users often interact with high-level platforms like Kubeflow or MLflow, they rely on OpenStack as the underlying infrastructure for provisioning and resource management.
A key challenge addressed is the efficient sharing of scarce GPU resources, with the Blazar project proposed as a solution for time-bound reservations to prevent resource hoarding and improve availability.
The discussion further distinguishes between inference and training workloads, advocating for shared, long-lived inference services to optimize GPU usage, while training requires dedicated, contiguous hardware blocks.
Finally, the panel stresses the importance of holistic resource optimization, carbon footprint monitoring, and cross-ecosystem collaboration to ensure sustainable and resilient AI deployment on cloud infrastructure.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Open Infra AI working group published a white paper detailing AI use cases on OpenStack, including trusted research environments for sensitive data.   |
|   2 | AI research resources increasingly favor Jupyter notebook-native experiences over Slurm batch workloads to support fast model learning.                    |
|   3 | MLOps platforms like Kubeflow and MLflow are used to encapsulate training templates and track experiments within Kubernetes environments.                  |
|   4 | Hardware diversity is expanding beyond traditional x86 and CUDA, with growth in ARM, AMD, and specialized accelerators like Cerebras and Graphcore.        |
|   5 | AI systems are probabilistic, contrasting with deterministic traditional software, which impacts how trust and safety are managed in critical deployments. |
|   6 | Collaboration with Airbus demonstrated AI models for auto-landing and takeoff trained on Compute Canada, a major OpenStack-based HPC infrastructure.       |
|   7 | OpenStack remains critical for industrial-scale AI deployment, from data collection to inference, despite the need for further upgrades.                   |
|   8 | Researchers often use OpenStack infrastructure without direct awareness, relying on technical departments to provision specific hardware requirements.     |
|   9 | Blazar, an OpenStack project, offers reservation-as-a-service to manage GPU contention by allowing time-bound resource allocation and automatic release.   |
|  10 | Commercial use cases focus on provisioning VMs with specific hardware to deploy composable and reproducible AI solutions across different clouds.          |
|  11 | Shared inference services are gaining traction, allowing multiple users to access long-lived models via APIs while maintaining control over data usage.    |
|  12 | Training workloads require contiguous hardware blocks for low-latency interconnect, whereas inference benefits from shared, cached model instances.        |
|  13 | AI models naturally degrade in performance over time, necessitating periodic retraining to maintain accuracy and prevent wrong predictions.                |
|  14 | Researchers often request excessive resources due to a desire for fast results, leading to inefficiencies and higher carbon footprints.                    |
|  15 | Open-source tools provide better transparency for monitoring carbon footprints and resource usage compared to proprietary industrial solutions.            |
|  16 | Collaboration between OpenStack, Kubernetes, and Slurm is improving through shared innovations like GPU NUMA affinity and Kata containers.                 |
|  17 | Education of end users is essential to optimize resource usage, as researchers often request more GPUs than actually needed for their workloads.           |
|  18 | The industry is moving toward resilient infrastructure that supports trusted execution environments and reduces dependence on untrusted providers.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/nxwtmRSliRo/hqdefault.jpg)](https://www.youtube.com/watch?v=nxwtmRSliRo)

[Watch on YouTube](https://www.youtube.com/watch?v=nxwtmRSliRo)
