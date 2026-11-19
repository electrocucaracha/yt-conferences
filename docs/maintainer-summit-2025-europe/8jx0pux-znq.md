---
layout: default
title: "Towards a Standardized Identity-based Authorization in Kubernetes - Keith Mattix & Lior Lieberman"
nav_order: 20
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "Keith and Leor discuss the necessity of moving toward standardized identity-based authorization policies within Kubernetes to address security vulnerabilities that originate from within trusted sys..."
resource: "https://www.youtube.com/watch?v=8JX0PUX-znQ"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

Keith and Leor discuss the necessity of moving toward standardized identity-based authorization policies within Kubernetes to address security vulnerabilities that originate from within trusted systems, rather than just at the network edge.
They explain that current Kubernetes network policies rely on ephemeral IP addresses and label selectors, which suffer from scalability issues, eventual consistency risks, and a lack of true identity-based enforcement.
The presentation highlights the fragmentation in the ecosystem, where tools like Cilium and Istio implement identity differently, creating interoperability challenges and preventing a unified security posture.
To resolve this, the speakers propose a standardized API that defines how identities are derived, encoded, and transmitted across network layers, allowing for consistent east-west traffic authorization.
They conclude by outlining key open questions regarding the composition of Layer 3/4 and Layer 7 policies, the scope of supported entities, and the need for clear trade-offs to enable secure, composable, and standardized identity-based access control in Kubernetes.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Policy traditionally focuses on system edges against external threats like DDoS or scrapers using tools such as WAFs and SSO.                |
|   2 | Access policies define what actions a specific entity can perform under specific conditions.                                                 |
|   3 | Significant security vulnerabilities often originate from within the system, such as disgruntled employees or confused deputy attacks.       |
|   4 | Defense in depth and zero trust philosophies assume previous security layers may fail, requiring layered enforcement.                        |
|   5 | East-west traffic refers to internal service-to-service communication, distinct from north-south traffic entering or leaving the system.     |
|   6 | Internal authorization typically involves machine entities with per-transaction access rather than human users.                              |
|   7 | Kubernetes NetworkPolicy v1 uses IP abstractions and label selectors, which are ephemeral and difficult to scale.                            |
|   8 | Current network policies lack support for cluster-wide admin policies and explicit deny rules, relying on implicit deny.                     |
|   9 | Admin NetworkPolicy introduces cluster-scoped policies and deny rules but still relies on IP-based entities.                                 |
|  10 | Eventual consistency in IP-based policies can lead to permissive security gaps and scalability issues.                                       |
|  11 | Identity-based policies offer stronger security by tying access to stable identities rather than transient IPs.                              |
|  12 | Key questions for identity-based APIs include how to derive, encode, and transmit identity across network layers.                            |
|  13 | Existing solutions like Cilium and Istio use different identity mechanisms, such as labels versus service accounts, lacking standardization. |
|  14 | Cilium derives identity from pod labels, while Istio uses Kubernetes service accounts for one-to-one pod mapping.                            |
|  15 | The lack of standardization makes it difficult to enforce consistent policies across different CNI and mesh implementations.                 |
|  16 | Policy enforcement spans multiple layers including L3/L4, L4 TLS, and L7, often combined confusingly in single CRDs.                         |
|  17 | Current implementations struggle with clear semantics when L7 attributes are present but traffic is L3/L4.                                   |
|  18 | A potential solution involves separate API resources for different network layers to clarify enforcement points.                             |
|  19 | Composition problems arise when determining how L3, L4, and L7 policies interact and avoid double enforcement.                               |
|  20 | TLS-based authentication cannot evaluate connections until after IP-based connections are established, complicating layer interaction.       |
|  21 | Not all traffic is TCP, making mTLS enforcement challenging for protocols like UDP.                                                          |
|  22 | Cilium demonstrates the ability to require encryption directly within network policy definitions.                                            |
|  23 | Standardizing context passing between network layers is necessary for mixed CNI and mesh environments.                                       |
|  24 | The community aims to start a work stream to standardize identity-based authorization policies in Kubernetes.                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8JX0PUX-znQ/hqdefault.jpg)](https://www.youtube.com/watch?v=8JX0PUX-znQ)

[Watch on YouTube](https://www.youtube.com/watch?v=8JX0PUX-znQ)
