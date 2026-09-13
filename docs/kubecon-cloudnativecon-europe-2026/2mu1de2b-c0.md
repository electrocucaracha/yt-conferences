---
layout: default
title:
  "The Shell Awakens: Cloud Native Workflows for Particle Ph... Raulian-Ionut
  Chiorescu & Hannes Hansen"
nav_order: 367
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Hannes and Raul, computing engineers at CERN, present their
  cloud-native platform designed to support the diverse computational needs of particle
  physicists working with data from the Large Hadron Collider. The platform, built...
resource: https://www.youtube.com/watch?v=2MU1de2B_C0
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Hannes and Raul, computing engineers at CERN, present their cloud-native platform designed to support the diverse computational needs of particle physicists working with data from the Large Hadron Collider.
The platform, built on Kubernetes, provides flexible access to heterogeneous hardware resources—including various Nvidia and AMD GPUs and specialized CPUs—along with multiple storage solutions and curated software environments tailored for machine learning and scientific computing.
Users can interact with the system through SSH, Jupyter notebooks, or Visual Studio Code, and leverage tools like Kubeflow, Ray, and MLflow to cover the full MLOps lifecycle, including distributed training, experiment tracking, and model serving.
The team emphasizes user feedback, automation via Kyverno policies, and observability with Prometheus and Grafana, while addressing challenges such as resource scheduling, low-latency networking, and integration with public cloud and HPC resources.
The platform currently serves hundreds of users across multiple CERN experiments, prioritizing user autonomy, reproducibility, and continuous improvement based on community needs.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CERN operates the LHC, producing terabytes of data per second, filtered by a trigger chain using FPGAs, CPUs, and GPUs.                        |
|   2 | Next Generation Triggers project integrates latest machine learning research into data filtering.                                              |
|   3 | Platform runs on Kubernetes with shared compute resources; supports multiple entry points: SSH, Jupyter, Visual Studio Code IDEs.              |
|   4 | Machine learning lifecycle covered with Kubeflow, Ray, Kerf, MLflow for model management, GitLab/GitHub CI.                                    |
|   5 | Heterogeneous cluster: Nvidia GPUs (H100, H200, L40), AMD GPUs (MI300X, Radeon Pro), specialized CPU nodes, Infiniband and RoCE v2 networking. |
|   6 | Storage: high IOPS scratch (MTB), Longhorn for shared PVCs, Ceph for external data extraction.                                                 |
|   7 | Curated container images (30–150GB) with pre-installed ML and physics software; users can build custom images.                                 |
|   8 | Interactive sessions via kubectl or Kubeflow UI; SSH access provided using ContainerSSH; user isolation via namespaces and OIDC/Kerberos.      |
|   9 | Performance optimizations: Kubernetes topology manager for NUMA-aware CPU/memory allocation.                                                   |
|  10 | Distributed ML training supported with Kubeflow and Ray; declarative job submission; supports PyTorch distributed training.                    |
|  11 | Hyperparameter optimization via Kubeflow Katib and Ray Tune; complex workflows orchestrated with Kubeflow Pipelines.                           |
|  12 | Model management and experiment tracking with MLflow; model serving with Kubeflow and KServe.                                                  |
|  13 | GPU direct RDMA enabled via Infiniband/RoCE, Nvidia/AMD operators, UCX/MPI for low-latency GPU communication.                                  |
|  14 | Workload bursting to public cloud and (soon) HPC centers using MultiQ and InterLink.                                                           |
|  15 | GPU scheduling uses binpack strategy for full-node allocation.                                                                                 |
|  16 | Monitoring with Prometheus and Grafana; namespace dashboards for users; power and resource usage tracked.                                      |
|  17 | Kyverno policies automate configuration, enforce resource limits, and simplify user experience.                                                |
|  18 | User feedback loop: familiar interfaces (SSH, storage), rapid iteration, upstream contributions.                                               |
|  19 | Security: Falco for threat detection, Kyverno                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2MU1de2B_C0)
