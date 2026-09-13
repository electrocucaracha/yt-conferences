---
layout: default
title:
  Enforce VIP Access Only Through Node Attestation - Alice Frosi & Jakob Naucke,
  Red Hat
nav_order: 100
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Alicha Frosi and Jacob N. from Reddit present on confidential computing
  and attestation in cluster environments, likening a secure cluster to an exclusive
  club where only authorized entities can access sensitive data. They explain that
  conf...
resource: https://www.youtube.com/watch?v=3H3n-tZYmlY
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

Alicha Frosi and Jacob N.
from Reddit present on confidential computing and attestation in cluster environments, likening a secure cluster to an exclusive club where only authorized entities can access sensitive data.
They explain that confidential computing protects data in use—an area previously lacking in traditional security—by ensuring computations occur in secure, attested environments, which is crucial for handling regulated or critical data.
The talk details the use of trusted hardware (like TPMs), remote attestation via the Trusty service, and policies that control when resources are unlocked, with a focus on automating complex processes such as node coordination and reference value management.
Through a demo, they show how confidential VMs protect secrets in memory, unlike standard VMs, by encrypting memory and root disks, thus preventing data leaks even if memory is dumped.
The session concludes with a discussion of current challenges, such as trust in cloud provider components and the "chicken and egg" problem of attesting the attestation server itself, and outlines future plans to expand support and further secure cluster bootstrapping and configuration.

# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation by Alicha Frosi and Jacob N. from Reddit on confidential computing and attestation.                                                                                                                   |
|   2 | Confidential computing protects data in use and ensures code runs in a secure environment.                                                                                                                         |
|   3 | Confidential clusters (trusted execution clusters) isolate sensitive data from external threats, including cloud providers.                                                                                        |
|   4 | Each node in the cluster must run on confidential hardware (e.g., AMD SEV-SNP, Intel TDX, ARM).                                                                                                                    |
|   5 | Trust is placed in the cluster administrator, not the cloud provider.                                                                                                                                              |
|   6 | Use cases include secure cloud migration, on-premise data segregation, and regulated data protection.                                                                                                              |
|   7 | Remote attestation validates that a node’s environment is confidential using TPM hardware.                                                                                                                         |
|   8 | Attestation process: TPM signs a quote with measurements; quote sent to remote attestation server (Trusty); server validates and returns an attestation token; token used to unlock secrets (e.g., LUKS disk key). |
|   9 | Trusty is a key broker and attestation service, part of Confidential Containers (CNCF).                                                                                                                            |
|  10 | Policies define successful attestation and resource unlocking.                                                                                                                                                     |
|  11 | Ignition boot config, Clevis pin for Trusty, and Trusty tester are used for node configuration and disk encryption.                                                                                                |
|  12 | Clevis encrypts disks using TPM or remote key sources; Trusty pin enables attestation-based key retrieval.                                                                                                         |
|  13 | PCR extension ensures node identity and prevents impersonation.                                                                                                                                                    |
|  14 | Reference values for attestation must be managed and updated with system changes.                                                                                                                                  |
|  15 | Approved images and expected PCRs are managed via custom resources and the compute-pcrs project.                                                                                                                   |
|  16 | Trusted execution cluster components and operator are written in Rust.                                                                                                                                             |
|  17 | Demo: Confidential VM created with KubeVirt, using TPM and attestation to encrypt root disk.                                                                                                                       |
|  18 | Memory dump attack on regular VM exposes secrets; confidential VM’s memory remains protected.                                                                                                                      |
|  19 | Future work: support for more cloud providers, protecting ignition and kubeconfig, attesting control plane, moving operator in-cluster.                                                                            |
|  20 | Operator orchestrates confidential clusters, deploys secure infrast                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=3H3n-tZYmlY)
