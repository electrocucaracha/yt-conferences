---
layout: default
title:
  "Kyverno Everywhere: Simplifying Unified Policy as Code - Jim Bugwadia & Charles-Edouard
  Brétéché"
nav_order: 145
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Kivero aims to simplify Kubernetes policy and governance by providing
  a native, frictionless way for developers, operators, and security teams to manage
  and enforce policies as code within Kubernetes environments. The project, started
  in 20...
resource: https://www.youtube.com/watch?v=N5Lw9Mj_uW8
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Kivero aims to simplify Kubernetes policy and governance by providing a native, frictionless way for developers, operators, and security teams to manage and enforce policies as code within Kubernetes environments.
The project, started in 2019 by contributors from Nermata, has evolved to support the full lifecycle of resource management—including validation, mutation, generation, deletion, and image verification—through declarative policies that operate continuously, not just at admission.
Kivero distinguishes itself by adopting the Common Expression Language (CEL) for policy definitions, modularizing policy types, and enabling off-cluster policy testing and reporting.
Beyond Kubernetes, Kivero now extends its policy engine to other domains like Terraform and authorization systems, offering a generic, programmable authorization server compatible with protocols such as Envoy and HTTP.
The project continues to innovate with new features, improved modularity, and an SDK for embedding policy control in custom applications, while preparing for further CNCF graduation and broader use cases.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Kivero's mission is to simplify Kubernetes policy and governance.                                                                                |
|   2 | Kivero was created to address friction and low adoption in existing Kubernetes policy engines by making policies native and easy to use.         |
|   3 | Kivero covers the full lifecycle of resource management: validation, mutation, generation, deletion, and image validation.                       |
|   4 | Kivero acts as an admission controller, optimizing for low latency and high performance.                                                         |
|   5 | Kivero CLI allows policy testing and application both in-cluster and off-cluster, supporting open reports for observability.                     |
|   6 | Kivero has evolved to use CEL (Common Expression Language) as its policy language, replacing JMESPath.                                           |
|   7 | Policy types are now separated into their own CRDs for modularity and easier management.                                                         |
|   8 | Kivero supports five main policy types: validating, mutating, generating, deleting, and image validating.                                        |
|   9 | Kivero enables background scanning and continuous monitoring, not just admission-time validation.                                                |
|  10 | Kivero policies can be tested and applied off-cluster, supporting policy-as-code workflows.                                                      |
|  11 | Kivero extends beyond Kubernetes, supporting policy enforcement for Terraform and authorization use cases.                                       |
|  12 | Kivero authorization integrates with Envoy and HTTP, using dedicated CEL libraries for different protocols.                                      |
|  13 | Policies can fetch external data (e.g., JSON Web Key Sets), decode tokens, and make authorization decisions.                                     |
|  14 | Kivero can run as a sidecar or central server, supports observability, and loads policies from various sources.                                  |
|  15 | The Kivero SDK allows embedding the engine in other applications, supporting extensibility and custom integrations.                              |
|  16 | Upcoming plans include new features, OCI support, off-cluster operation, migration tools, and deprecation of older policy types in version 1.18. |
|  17 | Community engagement and support are encouraged through events and project booths.                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=N5Lw9Mj_uW8)
