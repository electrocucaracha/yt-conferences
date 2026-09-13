---
type: Video Note
title: "Beyond the Cloud: Managing Baremetal the Kubernetes Way Using Metal... Ádám Rozmán & Nicolas Belouin"
description: "In this presentation, Adam Rosman from Ericsson and Nicolola Bulwa from Souza introduce the MetaCube project, a Kubernetes-based bare metal lifecycle and cluster management tool designed to address various challenges in managing physical ma..."
resource: https://www.youtube.com/watch?v=pThPIOZ7Nb0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Adam Rosman from Ericsson and Nicolola Bulwa from Souza introduce the MetaCube project, a Kubernetes-based bare metal lifecycle and cluster management tool designed to address various challenges in managing physical machines.
MetaCube offers a modular, extensible architecture that integrates with Cluster API and provides features such as IP address management, machine templating, and automated provisioning through interfaces with baseboard management controllers (BMCs) using protocols like Redfish and IPMI.
The speakers detail how MetaCube is used within Project Silva, a Linux Foundation Europe telco initiative that leverages open-source components and a declarative, GitOps approach to manage edge and central sites, deploying clusters and infrastructure via Helm charts and Flux.
They explain the process of registering and provisioning bare metal hosts, managing firmware settings and updates, and supporting advanced operations like rolling upgrades, node replacement, and self-management.
The session concludes with a Q&A covering switch management integration, support for various operating systems and bootstrap providers, and flexible update strategies for nodes.
# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction by Adam Rosman (Ericsson Software Technology) and Nicolola Bulwa (Souza, Engineering Telco Team)                                     |
|   2 | Presentation topic: Managing bare metal the Kubernetes way using the Metal³ (Metal Cube) project, with Silva project as a use case                |
|   3 | Metal³ is a bare metal lifecycle manager and clustering tool for Kubernetes                                                                       |
|   4 | Architecture includes controllers for multicluster management (above dashed line) and bare metal machine management (below dashed line)           |
|   5 | Integration with Cluster API; modular and extendable via interfaces                                                                               |
|   6 | Provides Cluster API Metal³ provider, IP address manager (Kubernetes-native, DHCP-like logic), and machine/data templating                        |
|   7 | Bare metal operator introduces the BareMetalHost (BMH) custom resource for mapping physical machines into Kubernetes                              |
|   8 | Provisioner interface supports multiple provisioners, including a standalone Ironic image (no OpenStack required)                                 |
|   9 | Ironic standalone operator simplifies configuration for large or geographically distributed deployments                                           |
|  10 | Provisioner communicates with the Baseboard Management Controller (BMC) for full lifecycle management (power, firmware, boot order, etc.)         |
|  11 | Supports managed (agent-based) and unmanaged (ISO-based) provisioning                                                                             |
|  12 | BMC protocols supported: Redfish, ISO, IDRA, IPMI (not IRMC)                                                                                      |
|  13 | Switch management (physical switches) is being developed, leveraging OpenStack's generic switch tool                                              |
|  14 | Minimum requirements for Metal³: boot MAC address, BMC address, BMC credentials, disk image                                                       |
|  15 | Silva project: Linux Foundation Europe telco initiative for cloud software framework for telco/edge, using open source, declarative GitOps (Flux) |
|  16 | Silva architecture: central management site (bare metal/cloud) manages multiple edge sites; uses Helm charts for deployment                       |
|  17 | Supports multiple Kubernetes providers (K3s, kubeadm, OKD, Canonical)                                                                             |
|  18 | Bare metal hosts and Cluster API resources deployed via Silva Helm charts                                                                         |
|  19 | Uses Redfish with virtual media for BMC, simplifying deployment and air-gapped environments                                                       |
|  20 | Bare metal op                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pThPIOZ7Nb0)