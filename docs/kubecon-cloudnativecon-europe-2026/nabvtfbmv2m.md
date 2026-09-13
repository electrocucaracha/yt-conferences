---
layout: default
title:
  Lessons Learned Orchestrating Multi-Tenant GPUs on OpenShift AI with NVIDIA
  KAI (G/H2... Luca Berton
nav_order: 200
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Luca Berton outlines a practical approach to building
  a multi-tenant, GPU-powered AI platform on bare metal OpenShift, drawing on real-world
  experience with an avionics customer in France. He emphasizes that while run.
resource: https://www.youtube.com/watch?v=nABVTFBmV2M
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

In this presentation, Luca Berton outlines a practical approach to building a multi-tenant, GPU-powered AI platform on bare metal OpenShift, drawing on real-world experience with an avionics customer in France.
He emphasizes that while running GPUs is straightforward, the real challenge lies in sharing them safely, fairly, and efficiently across teams, guided by principles of safety, fairness, and efficiency.
The solution leverages Dell AI servers, Nvidia GPUs, and OpenShift AI, with GitOps (using Argo CD and Kustomize) as the operational backbone to ensure auditability, repeatability, and compliance in a highly regulated, air-gapped environment.
Key lessons include the importance of hardware-aware configuration, robust network isolation, driver compatibility, and per-tenant monitoring for chargeback and observability.
The platform supports different user personas—LLM Ops engineers, administrators, and developers—by providing secure, efficient, and transparent access to GPU resources, with GitOps and standardized templates reducing operational complexity and ensuring reliable, scalable AI infrastructure.

# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Practical blueprint for running multi-tenant GPUs on bare metal OpenShift AI for a sovereign full-stack AI platform                                                                     |
|   2 | Main challenge: sharing GPUs safely, fairly, and efficiently across teams                                                                                                               |
|   3 | Based on Dell AI factory, using bare metal with Red Hat Kubernetes OpenShift AI                                                                                                         |
|   4 | Key components: OpenShift AI, Nvidia GPU and network operator, Grasshopper H200 GPU nodes, Dell AI servers (up to 8 GPUs/node)                                                          |
|   5 | Air-gapped setup with local mirrors; over 2TB of data installed for dependencies                                                                                                        |
|   6 | Operational risks: noisy neighbor, queue starvation, mismatched MIG behavior, driver drift, networking failures (SR-IOV, RDMA)                                                          |
|   7 | Framework for platform decisions: safety (isolation), fairness (deterministic contention), efficiency (outcomes per GPU hour)                                                           |
|   8 | Three personas: end user (fast access, stable latency), LLM ops (repeatable deployments, upgrades, observability), tenant admin (boundaries, cost visibility)                           |
|   9 | GitOps (Argo CD, Kustomize) as single source of truth for operations, infrastructure, and tenant configuration                                                                          |
|  10 | Air-gapped environment: node installation via OpenShift agent ISO, initial handshake with Ansible, then GitOps for day two operations                                                   |
|  11 | Safety enforced by default: namespace isolation, scoped service accounts, least privilege, AD integration, deny-by-default network policies, quotas, limits, admission checks, webhooks |
|  12 | Tenant provisioning via Git pull request; no manual steps                                                                                                                               |
|  13 | Hardware mix matters: different NICs (Nvidia ConnectX v6/v7, Intel) require different operational models; RDMA collision required blacklisting Intel driver                             |
|  14 | Reduced upgrade fragility by moving to open kernel module and DMA buffer drivers                                                                                                        |
|  15 | Fairness enforced via hard GPU caps (Nvidia Kai), priority classes, preemption, GPU-aware scheduling                                                                                    |
|  16 | Efficiency: optimize for workload outcomes (time slicing, MIG, full GPU) per workload type                                                                                              |
|  17 | Upgrade path managed via compatibility matrix in Git, canary pool, Git-based rollback                                                                                                   |
|  18 | Per-tenant monitoring: chargeback, scheduler reports, GPU/hour visibility                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nABVTFBmV2M)
