---
layout: default
title: "Baremetal could not be easier: using Metal3 and Ironic for rapid provisioning"
nav_order: 7
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation demonstrates a streamlined approach to bare metal provisioning using the Metal Cube project, which leverages Kubernetes to manage physical machines through the Ironic open-source ..."
resource: "https://www.youtube.com/watch?v=3AyQuAguNf8"
youtube_stats:
  view_count: 826
  like_count: 19
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

This presentation demonstrates a streamlined approach to bare metal provisioning using the Metal Cube project, which leverages Kubernetes to manage physical machines through the Ironic open-source tool.
The speakers outline a simplified workflow that avoids complex configuration files by utilizing virtual media, a method that allows direct ISO image attachment to a machine’s Baseboard Management Controller (BMC) without requiring a dedicated provisioning network or PXE setup.
The technical setup involves deploying a local Kubernetes cluster using Kind, installing the Ironic Standalone Operator and Bare Metal Operator, and configuring necessary certificates and credentials via Custom Resource Definitions.
The provisioning process itself is reduced to five key steps: identifying the BMC address and credentials, creating a Bare Metal Host resource to trigger hardware inspection, selecting a root device from the generated hardware data, defining an image URL with a checksum, and applying a patch to initiate the deployment.
A live demo confirms that this entire process, from cluster installation to a fully provisioned and SSH-accessible machine, can be completed in approximately 30 minutes, highlighting the ease of use and efficiency of the Metal Cube ecosystem for managing bare metal infrastructure.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation showcases Metal Cube, a project that simplifies bare metal provisioning using Kubernetes.                                    |
|   2 | Metal Cube uses the Ironic project, an OpenStack component written in Python, to manage the lifecycle of physical machines.                   |
|   3 | The system consists of three main components: the Bare Metal Operator, the Ironic Standalone Operator (ARSO), and the Ironic container image. |
|   4 | The Bare Metal Operator translates Ironic APIs into Kubernetes API calls, while ARSO manages Ironic services, deployments, and upgrades.      |
|   5 | Users interact with the system by creating Custom Resource Definitions (CRDs) for the Bare Metal Operator and Ironic.                         |
|   6 | The demo uses a local Kubernetes cluster created with Kind to simulate the environment.                                                       |
|   7 | Exposing specific ports for the Ironic API and HTTP/HTTPS services is required in the Kind configuration.                                     |
|   8 | Certificate management is handled using cert-manager to generate TLS certificates for Ironic.                                                 |
|   9 | The Ironic Custom Resource requires defining credentials, certificate issuers, and external IP addresses.                                     |
|  10 | The Bare Metal Operator installation requires compatible versions, such as version 0.11 for the operator and 32 for the Ironic image.         |
|  11 | Virtual media provisioning is used to simplify the process, eliminating the need for PXE boot and complex network configurations.             |
|  12 | Virtual media allows connecting an ISO image directly to the machine's BMC for booting.                                                       |
|  13 | Prerequisites for provisioning include the BMC URL, credentials, and a supported MAC address.                                                 |
|  14 | The provisioning process begins by creating a Bare Metal Host custom resource with BMC details.                                               |
|  15 | The system performs an inspection by booting a RAM disk to collect hardware data, such as storage information.                                |
|  16 | Deployment requires specifying an image URL, checksum, root device hint, and a cloud-init configuration secret.                               |
|  17 | Patching the Bare Metal Host resource with these details triggers the cleaning and provisioning states.                                       |
|  18 | The entire demo process, including installation and provisioning, takes approximately 30 minutes.                                             |
|  19 | Metal Cube supports advanced features like firmware upgrades, live ISO booting, and adopting existing hosts.                                  |
|  20 | The project is a CNCF incubating project with documentation available at metalq.io.                                                           |
|  21 | Additional talks on project updates and firmware settings are scheduled for the following day.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3AyQuAguNf8/hqdefault.jpg)](https://www.youtube.com/watch?v=3AyQuAguNf8)

[Watch on YouTube](https://www.youtube.com/watch?v=3AyQuAguNf8)
