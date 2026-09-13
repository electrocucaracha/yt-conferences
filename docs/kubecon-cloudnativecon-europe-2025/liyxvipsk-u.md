---
layout: default
title:
  TUF-en up Your Software Supply Chain - Marina Moore, Edera & Kairo De Araujo,
  Independent
nav_order: 324
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Kaido and Marina discuss the software supply chain metadata distribution
  problem, focusing on secure software distribution using the Tough Update Framework
  (TU). They explain how TU uses a principle of compromise resilience to protect again...
resource: https://www.youtube.com/watch?v=lIYXVIPsk_U
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

Kaido and Marina discuss the software supply chain metadata distribution problem, focusing on secure software distribution using the Tough Update Framework (TU).
They explain how TU uses a principle of compromise resilience to protect against cascading failures in the system.
The framework involves detach signatures, multi-signature trust, and version numbers to ensure secure distribution and verification of software packages.
TU is designed to be flexible and can be integrated with existing tooling, including Kubernetes and GitHub Actions.
The authors address questions about compatibility with SLSA (Software Landscapes Architecture) and discuss plans for an admission controller in Kubernetes to enforce TU's security policies.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The problem with software supply chain metadata is that it can be tampered with or replaced by attackers.                                              |
|   2 | Signatures can be used to verify the integrity of software, but they have limitations, such as out-of-date metadata and key distribution problems.     |
|   3 | A framework called TUF (Trusted Utility Framework) is designed to protect the freshness and consistency of software being distributed.                 |
|   4 | TUF uses a principle of compromise resilience, which requires multiple signatures and keys to be used in sequence to verify the integrity of software. |
|   5 | The TUF framework includes features such as content integrity, detach signatures, and multi-signature trust.                                           |
|   6 | The framework can be used to secure software supply chains by verifying the integrity of software before it is deployed to production environments.    |
|   7 | TUF has implementations in various programming languages, including Python, Go, Rust, PHP, and Java.                                                   |
|   8 | The framework can be integrated with existing tooling, such as Kubernetes and Argo CD.                                                                 |
|   9 | SLSA (Software Supply Chain Alliance) is a related framework that focuses on build provenance and can be used in conjunction with TUF.                 |
|  10 | R stuff is a sister project to TUF that provides a generic format for attestations and can be used to verify the integrity of software.                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lIYXVIPsk_U)
