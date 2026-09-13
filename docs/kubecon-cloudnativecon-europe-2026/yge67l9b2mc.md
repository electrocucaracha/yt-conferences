---
type: Video Note
title: "Rook: Intro and Deep Dive With Ceph Storage - Artem Torubarov, Deepika Upadhyay & Niels de Vos"
description: "The presenters introduce Rook, an open-source operator that simplifies deploying and managing Ceph (SE) storage within Kubernetes clusters, automating installation, configuration, and updates using Kubernetes-native patterns. They explain R..."
resource: https://www.youtube.com/watch?v=ygE67l9b2Mc
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters introduce Rook, an open-source operator that simplifies deploying and managing Ceph (SE) storage within Kubernetes clusters, automating installation, configuration, and updates using Kubernetes-native patterns.
They explain Rook’s architecture, highlighting its flexibility to run on cloud, on-premises, or hybrid environments, and its ability to provide unified block, file, and object storage without vendor lock-in.
Key features include customizable replication for data resiliency, efficient handling of small persistent volumes, seamless scaling, and recent enhancements such as improved CSI driver support, NVMe-oF gateway integration, and erasure coding for better storage efficiency.
A case study details SAP’s migration to Rook and Ceph, managing 120 petabytes across 15 regions with robust maintenance and upgrade processes, demonstrating Rook’s reliability and scalability in production.
The talk also covers technical aspects of the Ceph CSI driver, including support for multiple storage backends, encryption, volume snapshots, disaster recovery, and the benefits and trade-offs of erasure coding, with ongoing improvements aimed at further simplifying and optimizing storage management in Kubernetes environments.
# Main Points

|   # | Main point                                                                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Dipika (Clyo, Rook contributor), Artum (Clyo, Rook contributor), Neil Devos (IBM, SEF team, SECI maintainer)                                                                              |
|   2 | Agenda: Introduction to Rook and SE, cluster topology and maintenance, production user study, SE CSI driver features, recent SE enhancement (erasure coding)                                                        |
|   3 | Rook is an operator that brings SE (self storage) to Kubernetes clusters using CRDs, automating deployment, configuration, and updates                                                                              |
|   4 | Rook and SE are open source with Apache 2.0 license                                                                                                                                                                 |
|   5 | Rook architecture: Rook operator deploys/manages SE, CSI layer provisions/mounts storage, applications communicate directly with SE data layer                                                                      |
|   6 | SE is an open-source, distributed, enterprise-grade storage platform for Kubernetes, supporting block (RBD), file (SEFS), and object (RGW) storage                                                                  |
|   7 | Rook can be installed on cloud, virtual machines, bare metal, on-prem, or hybrid/multicloud environments                                                                                                            |
|   8 | Rook and SE address data loss concerns by replicating/distributing data across availability zones with customizable replica counts                                                                                  |
|   9 | SE optimizes data placement, supports many small PVs, avoids vendor lock-in, and is scalable with no downtime for capacity expansion                                                                                |
|  10 | Recent Rook features: SEC CSI operator enabled by default (v1.18), more customization via CRDs, NVMe OF gateway support (experimental in v1.19), NVMe TCP protocol for external clients                             |
|  11 | Maintenance: Cluster topology awareness ensures safe upgrades/maintenance using port disruption budgets; only one zone down at a time                                                                               |
|  12 | Rook keep plugin provides shortcuts for SE operations (status, OSD removal, monitor quorum restore)                                                                                                                 |
|  13 | Case study: SAP cloud infrastructure migrated to Rook+SE, storing 120 PB across 15 regions/26 zones, 10 regions live, 37 PB capacity, monthly OS upgrades, quarterly Kubernetes/Rook upgrades, no customer downtime |
|  14 | SE CSI driver: Container image with RBD, SEFS, NFS, NVMe backends; supports volume expansion, cloning, snapshotting, topology awareness, ephemeral volumes, PVC encryption, group snapshots, block metrics,         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ygE67l9b2Mc)