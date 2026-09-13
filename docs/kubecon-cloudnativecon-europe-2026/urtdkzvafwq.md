---
layout: default
title:
  "Cloud Native Theater | KubeVirt Summit: Achieving 10× Faster VM Migration
  to Kube... Ryosuke Tatsumi"
nav_order: 69
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Ryosuke Tatsumi, chief researcher at Hitachi America, discusses the challenges
  and solutions for migrating virtual machines (VMs) from legacy platforms to Kubevirt,
  especially as enterprises seek both platform replacement and application mo...
resource: https://www.youtube.com/watch?v=uRTdkZVAfWQ
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

Ryosuke Tatsumi, chief researcher at Hitachi America, discusses the challenges and solutions for migrating virtual machines (VMs) from legacy platforms to Kubevirt, especially as enterprises seek both platform replacement and application modernization.
He highlights that large-scale VM migrations are often bottlenecked by slow data transfer, leading to prolonged migration durations, increased costs, and operational complexity due to maintaining parallel infrastructures.
Tatsumi introduces the Forklift open-source tool, which automates much of the migration process but is still limited by host-based data transfer inefficiencies.
To address this, his team developed an "Xcopy volume populator" component that offloads data copying directly to the storage array using the XCOPY SCSI command, bypassing host resource constraints and achieving up to 10 times faster migration speeds.
This pluggable architecture allows storage vendors to integrate their own logic, minimizes workflow disruption, and significantly reduces migration time, cost, and risk, thereby accelerating business transformation and application modernization.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ryosuke Tatsumi is chief researcher at Hitachi America, working on storage plugin solutions for Kubernetes.                                                |
|   2 | Enterprises are re-evaluating virtualization platforms due to changes in the VMware ecosystem and are considering migration and application modernization. |
|   3 | Kubevirt is gaining attention as it allows running VMs while transitioning to cloud-native architecture.                                                   |
|   4 | Large-scale VM migration is challenging due to throughput bottlenecks, especially for enterprises migrating thousands of VMs and petabytes of data.        |
|   5 | Two main concerns: long migration duration (can take 18+ months) and limited maintenance windows requiring VM downtime.                                    |
|   6 | Prolonged migration leads to duplicate infrastructure, increased costs, fragmented resources, operational complexity, and higher risk.                     |
|   7 | Forklift is an open-source tool for orchestrating VM migration from VMware to Kubevirt, automating the workflow.                                           |
|   8 | The VM disk copy step is the most data-intensive and dominates migration time.                                                                             |
|   9 | In typical Forklift migration, all VM disk data is copied through a host-based data path, causing CPU, network, and memory bottlenecks.                    |
|  10 | The solution is to offload data copy to the storage array using XCOPY, a standard SCSI command that copies data within storage without host involvement.   |
|  11 | XCOPY is widely supported in enterprise storage and used in VMware VMDK clone operations.                                                                  |
|  12 | Technical challenge: ESXi must have access to both source and target LUNs, but Kubernetes manages the target LUN, creating a gap.                          |
|  13 | Forklift cannot trigger XCOPY directly due to storage visibility and vendor-specific operations.                                                           |
|  14 | Introduced "Xcopy volume populator" component with a remote XCOPY trigger and storage offload plugin to handle storage-specific operations.                |
|  15 | Pluggable architecture allows vendors to implement their own logic for storage operations.                                                                 |
|  16 | Only the VM disk copy step is replaced; other migration steps remain unchanged.                                                                            |
|  17 | Storage offload achieved up to 20x faster migration for 1TB VM (3 hours reduced to 10                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=uRTdkZVAfWQ)
