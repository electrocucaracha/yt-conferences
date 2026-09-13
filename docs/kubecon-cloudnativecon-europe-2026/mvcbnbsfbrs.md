---
layout: default
title:
  "API is the New SSH: Forging a Zero-Trust VM Platform on Kubernetes - Evangelista
  Tragni, Devoteam"
nav_order: 11
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The session focused on running virtual machines (VMs) within Kubernetes
  using KubeVirt, an open-source CNCF project primarily developed by Red Hat. The
  presenter, a Red Hat DevOps lead, explained the motivation for moving VMs into Kubernetes.
resource: https://www.youtube.com/watch?v=mVcBnbSfBrs
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

The session focused on running virtual machines (VMs) within Kubernetes using KubeVirt, an open-source CNCF project primarily developed by Red Hat.
The presenter, a Red Hat DevOps lead, explained the motivation for moving VMs into Kubernetes to reduce vendor lock-in and leverage existing Kubernetes expertise.
He detailed KubeVirt’s architecture, including its main components (virt-api, virt-controller, virt-handler, and virt-launcher), and described how VMs are managed as pods, with YAML configurations specifying resources and devices.
Key features such as device passthrough, persistent storage, networking options (including Multus for multiple interfaces), live migration, and ecosystem integration with tools like Argo CD and Cluster API were discussed, alongside practical limitations like live migration fragility, storage requirements, and challenges with Windows VMs and network configurations.
The presenter emphasized that while KubeVirt is production-ready for some use cases—such as legacy Windows VMs, telco workloads, and ephemeral control planes—there are still technical and organizational hurdles, particularly around networking, disaster recovery, and performance.
The session concluded with a Q&A addressing issues like nested virtualization, IP preservation during migration, CNI choices (Cilium, Kube-OVN, Calico), and resource overcommitment, highlighting that adoption depends on specific workload needs and organizational readiness for change.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter is a Red Hat evangelist and lead DevOps engineer based in Luxembourg, involved in projects in Germany.                                                                                   |
|   2 | Session focuses on virtual machines (VMs), virtualization technology, and creating a VM platform.                                                                                                  |
|   3 | VMware is recognized as a technology leader in virtualization.                                                                                                                                     |
|   4 | KubeVirt, an open source CNCF project, enables running VMs on Kubernetes to reduce vendor lock-in.                                                                                                 |
|   5 | Increasing adoption of open source solutions, with Kubernetes widely used across sectors.                                                                                                          |
|   6 | Running VMs on Kubernetes allows teams skilled in Kubernetes to manage both containers and VMs.                                                                                                    |
|   7 | KubeVirt is developed and maintained by Red Hat.                                                                                                                                                   |
|   8 | KubeVirt is an add-on for Kubernetes, not included by default.                                                                                                                                     |
|   9 | KubeVirt has three main components: virt-api (handles VM requests), virt-controller (manages VM lifecycle), and virt-handler (runs on each node to manage VMs).                                    |
|  10 | Deploying a VM creates a virt-launcher pod, which hosts the VM.                                                                                                                                    |
|  11 | VM configuration is defined in YAML, specifying resources, devices, boot configuration, and storage (using persistent volume claims).                                                              |
|  12 | Distinction between VM object (declaration) and VM instance (running state).                                                                                                                       |
|  13 | KubeVirt features include device passthrough (e.g., GPU), storage via CSI, and networking via default bridge or Multus for multiple interfaces.                                                    |
|  14 | Live migration is supported but currently fragile and requires ReadWriteMany storage.                                                                                                              |
|  15 | Ecosystem integration: supports GitOps tools (Argo CD, Flux, Tekton), Cluster API, and automation.                                                                                                 |
|  16 | Suggested OS-level hardening tools: Talos and Kairos.                                                                                                                                              |
|  17 | Networking options: Cilium (eBPF-based, high performance, but IP not preserved on migration) and Kube-OVN (network engineer-oriented, supports static IPs).                                        |
|  18 | Use cases: legacy Windows VMs, telco workloads, ephemeral control planes, and real production experience at Schwarz Group.                                                                         |
|  19 | Limitations: live migration fragility, storage requirements, Windows migration challenges, node lock-in with passthrough, need for custom disaster recovery, dashboard availability, MAC/IP bindin |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mVcBnbSfBrs)
