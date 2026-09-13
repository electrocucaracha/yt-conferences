---
layout: default
title:
  "Project Lightning Talk: Five Minutes by CloudNativePG River - Gabriele Quaresima,
  Contributor"
nav_order: 261
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Gabriel Quarisima, a staff engineer and CloudNativePG contributor, introduces
  CloudNativePG, an open-source operator designed to manage PostgreSQL workloads on
  any supported Kubernetes cluster. He explains that CloudNativePG, a CNCF sandbox...
resource: https://www.youtube.com/watch?v=Cwz7WAOtr6w
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

Gabriel Quarisima, a staff engineer and CloudNativePG contributor, introduces CloudNativePG, an open-source operator designed to manage PostgreSQL workloads on any supported Kubernetes cluster.
He explains that CloudNativePG, a CNCF sandbox project, defines a new Kubernetes CRD called "cluster," representing a PostgreSQL cluster with a primary instance and multiple replicas, typically deployed across three worker nodes in different availability zones for high availability.
The operator offers features such as direct Kubernetes API integration, high availability, scalable replica management, declarative configuration, backup and recovery via volume snapshots or object stores, and a kubectl plugin for cluster management.
Recent enhancements include declarative databases, logical replication, support for custom backup systems, major PostgreSQL upgrades, and declarative loading of extensions.
Gabriel invites the community to join CloudNativePG on various platforms and attend related talks and events.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Gabriel Quarisima is a staff engineer and CloudNativePG contributor.                                                                                                                                                                                                |
|   2 | The session discusses running data on Kubernetes.                                                                                                                                                                                                                   |
|   3 | CloudNativePG is an open-source operator for managing PostgreSQL workloads on Kubernetes clusters.                                                                                                                                                                  |
|   4 | It is a CNCF sandbox project and has applied for incubation.                                                                                                                                                                                                        |
|   5 | CloudNativePG has an active community and multiple repositories for contribution.                                                                                                                                                                                   |
|   6 | It introduces a new Kubernetes CRD named "cluster" to represent a PostgreSQL cluster.                                                                                                                                                                               |
|   7 | A PostgreSQL cluster consists of a single primary and multiple replica instances.                                                                                                                                                                                   |
|   8 | Suggested architecture uses a shared-nothing approach with three worker nodes in different availability zones.                                                                                                                                                      |
|   9 | Each Kubernetes worker node hosts its own instance with local persistent volumes.                                                                                                                                                                                   |
|  10 | Services are provided for read/write (primary) and read-only (replicas) access.                                                                                                                                                                                     |
|  11 | Key features include:                                                                                                                                                                                                                                               |
|  12 | Direct integration with Kubernetes API as the source of truth.                                                                                                                                                                                                      |
|  13 | High availability and scalability (scale up/down, arbitrary number of replicas).                                                                                                                                                                                    |
|  14 | Declarative management of PostgreSQL configuration via CRD spec.                                                                                                                                                                                                    |
|  15 | Backup and recovery using volume snapshot CRD and object store (Barman Cloud).                                                                                                                                                                                      |
|  16 | kubectl plugin for cluster management, log retrieval, and performance monitoring.                                                                                                                                                                                   |
|  17 | Cluster referencing for debugging or shutting down clusters to save costs.                                                                                                                                                                                          |
|  18 | Recent features: declarative databases, logical replication, CMPGI interface for custom backup systems, major PostgreSQL upgrades, declarative foreign data management, quorum-based failover, and declarative loading of PostgreSQL extensions via OCI containers. |
|  19 | Community is accessible via CNCF site, GitHub, Slack, and at the event kiosk.                                                                                                                                                                                       |
|  20 | Two related talks are scheduled, including one on data sovereignty and another by Gabriel Bolini and Lauren Parody.                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Cwz7WAOtr6w)
