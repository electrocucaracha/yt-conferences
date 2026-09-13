---
layout: default
title:
  "Cloud Native Theater | Data on Kubernetes Day: From PVC to Mount Point: Dissecting
  a... Vivek Singh"
nav_order: 52
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Vivee, a software engineer at MongoDB, explains the
  process of dynamic volume provisioning in Kubernetes, focusing on how persistent
  volume claims (PVCs) are handled. When a PVC is created, the Kubernetes persistent
  volume...
resource: https://www.youtube.com/watch?v=MY-VaJVJmk0
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

In this session, Vivee, a software engineer at MongoDB, explains the process of dynamic volume provisioning in Kubernetes, focusing on how persistent volume claims (PVCs) are handled.
When a PVC is created, the Kubernetes persistent volume (PV) controller checks for existing volumes that meet the requirements; if none are found, it determines whether to use an in-tree or external provisioner based on the provisioner name.
External provisioners, typically implemented as CSI (Container Storage Interface) plugins, are responsible for provisioning storage by following the CSI specification, which defines required services and RPCs.
The CSI plugin consists of controller and node components, with the controller handling volume creation and attachment, and the node plugin managing the mounting of volumes to pods.
Throughout the workflow, Kubernetes itself does not directly interact with the CSI plugin; instead, sidecar containers monitor resources and trigger the necessary actions, making it crucial to understand each component's role for effective debugging and management of stateful workloads on Kubernetes.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Vivee, a software engineer at MongoDB, discusses dynamic volume provisioning in Kubernetes.                                                  |
|   2 | Stateful workloads in Kubernetes require volumes attached via the Persistent Volume Claim (PVC) API.                                         |
|   3 | Creating a PVC resource triggers the Persistent Volume (PV) controller to find or provision a suitable volume.                               |
|   4 | If no existing volume matches the PVC requirements, the PV controller checks the specified provisioner in the storage class.                 |
|   5 | Provisioners can be "in-tree" (deprecated, shipped with Kubernetes) or "external" (CSI plug-ins).                                            |
|   6 | The PV controller annotates the PVC with the storage provisioner; Kubernetes itself does not provision the volume.                           |
|   7 | An external component, the CSI plug-in, monitors PVCs with its annotation and provisions volumes by communicating with the storage provider. |
|   8 | The CSI specification (CSI spec) defines the required rules and RPCs for CSI plug-ins.                                                       |
|   9 | CSI plug-ins implement three services: identity, controller, and node.                                                                       |
|  10 | CSI plug-in consists of two components: controller plug-in (can run anywhere) and node plug-in (must run on every node).                     |
|  11 | The CSI provisioner sidecar monitors PVCs and calls the create volume RPC on the controller plug-in.                                         |
|  12 | The controller plug-in communicates with the storage provider to create the volume.                                                          |
|  13 | After volume creation, the CSI provisioner sidecar creates a PV resource in Kubernetes.                                                      |
|  14 | When a workload is scheduled, the attach-detach controller creates a volume attachment resource.                                             |
|  15 | The CSI attacher sidecar detects this and calls the controller publish volume RPC to attach the volume to the node.                          |
|  16 | Once attached, kubelet interacts with the node plug-in to mount the volume to the pod’s filesystem.                                          |
|  17 | Node plug-in must be present on all nodes to handle mounting.                                                                                |
|  18 | Kubernetes does not directly communicate with the CSI plug-in; CSI components interact with the API server.                                  |
|  19 | Each step in the volume lifecycle is handled by a specific component, aiding in debugging if issues arise.                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MY-VaJVJmk0)
