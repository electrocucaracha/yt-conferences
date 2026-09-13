---
type: Video Note
title: "Project Lightning Talk: How To Run Kubernetes Pods On My Slurm-Based HPC Center - Diego Ciangottini"
description: "The speaker, a researcher at the National Institute of Nuclear Physics in Italy and maintainer of Interlink, introduces Interlink as a tool designed to seamlessly translate Kubernetes pod manifests into jobs that can run on supercomputers m..."
resource: https://www.youtube.com/watch?v=K-Z4l7SOa3o
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a researcher at the National Institute of Nuclear Physics in Italy and maintainer of Interlink, introduces Interlink as a tool designed to seamlessly translate Kubernetes pod manifests into jobs that can run on supercomputers managed by systems like Slurm, without requiring custom resource definitions or administrative network privileges.
Interlink is not intended for running Slurm under Kubernetes or managing Slurm and Kubernetes side by side, but rather for remotely accessing Slurm-based resources from a Kubernetes cluster, which could be located anywhere, including a laptop or cloud environment.
The system requires a recent Kubernetes version, a container runtime, shared file systems across nodes, and specific network capabilities, and is composed of three main components: a virtual kubelet provider for Kubernetes, an Interlink server on the HPC side, and a network plugin for pod communication.
In the demo, the speaker shows how users can define notebook requirements, target specific nodes or supercomputers, and launch pods that are offloaded to the HPC, with full integration and access to logs, ultimately enabling the use of supercomputer GPUs for their workloads.
The speaker invites interested participants to see a live demonstration at the kiosk session.
# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter is a researcher at the National Institute of Nuclear Physics in Italy and a maintainer of Interlink.                                                                                                     |
|   2 | Interlink is a tool designed to translate Kubernetes pod manifests to run on supercomputers managed by different systems, such as Slurm.                                                                           |
|   3 | The goal is to make the process seamless, requiring no CRDs, plain pod definitions, and no root or administrative network privileges.                                                                              |
|   4 | Interlink is not for running Slurm under Kubernetes or managing Slurm and Kubernetes side by side.                                                                                                                 |
|   5 | It enables remote access to Slurm-based HPC resources from Kubernetes, which can run locally or in the cloud.                                                                                                      |
|   6 | Works with both closely remote (same center, network segregated) and distant setups.                                                                                                                               |
|   7 | Requirements include a recent Kubernetes version, ingress with wildcards (for full capabilities), container runtime on nodes, shared file system across nodes, and network capabilities using the unshare command. |
|   8 | Interlink consists of three core components:                                                                                                                                                                       |
|   9 | Virtual Kubelet provider for Interlink installed on the Kubernetes cluster.                                                                                                                                        |
|  10 | Interlink server on the remote HPC side (login node or dedicated edge machine).                                                                                                                                    |
|  11 | Network plugin for pod communication between Kubernetes and HPC.                                                                                                                                                   |
|  12 | Users target the virtual node in their pod definitions as with any normal pod.                                                                                                                                     |
|  13 | Demonstration involved running a Kubeflow notebook on the Leonardo supercomputer in Italy.                                                                                                                         |
|  14 | Users define notebook requirements, target specific nodes or supercomputers, and launch pods.                                                                                                                      |
|  15 | Jobs are created on the HPC login node, with full integration and access to logs via web interface.                                                                                                                |
|  16 | Notebooks can utilize supercomputer GPUs.                                                                                                                                                                          |
|  17 | Live demonstrations are available at the kiosk on Wednesday from 10 to 1:30.                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=K-Z4l7SOa3o)