---
layout: default
title:
  "Strengthening Auth in Kubernetes: Image Pulling, DRA Admin Access. Rita Zhang
  & Stanislav Láznička"
nav_order: 321
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Microsoft engineer Rita discusses updates in SIG O for a and authorization,
  including graduated features such as service account token improvements, cluster
  trust bundles, fine-grained cublet API authorization, and external signing for serv...
resource: https://www.youtube.com/watch?v=rVz-vIFGT4k
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Microsoft engineer Rita discusses updates in SIG O for a and authorization, including graduated features such as service account token improvements, cluster trust bundles, fine-grained cublet API authorization, and external signing for service account tokens.
These features aim to improve security, reduce reliance on long-lived secrets, and enhance resource allocation.
The SIG O team has worked on various projects, including the development of a new certificate feature that allows easy minting of client certificates for service accounts.
The team also plans to introduce additional features in future releases, including hardened of cubat 7 set validation and PSA restrictions for probes host fields.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Upcoming features:                                                                                                                   |
|   2 | Service account image pull credential (reduces reliance on long-lived secrets in Kubernetes)                                         |
|   3 | DRA admin access (enables dynamic requesting and sharing of resources like GPUs between pods and containers)                         |
|   4 | External signing for service account tokens (allows Kubernetes API servers to make gRPC calls to external systems for token signing) |
|   5 | P certificates (lets you easily mint client certificates for your service account identities)                                        |
|   6 | Demos: + DRAM admin access feature + Secret pull images demo + Cluster trust bundle demo                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=rVz-vIFGT4k)
