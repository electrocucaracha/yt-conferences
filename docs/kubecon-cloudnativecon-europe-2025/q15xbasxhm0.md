---
type: Video Note
title: "Encryption, Identities, and Everything in Between; Building Se... Lior Lieberman & Igor Velichkovich"
description: "Leo Lieberman, engineer lead at Google, and Igor Velichkovich, engineer at a stealth startup, discuss the importance of securing Kubernetes networks and identities. They share examples of security breaches, such as Target and Equifax, which..."
resource: https://www.youtube.com/watch?v=Q15XbASxHM0
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Leo Lieberman, engineer lead at Google, and Igor Velichkovich, engineer at a stealth startup, discuss the importance of securing Kubernetes networks and identities.
They share examples of security breaches, such as Target and Equifax, which highlight the need for network segmentation and identity-based security measures.
The duo introduce various solutions, including network policies, admin network policies, and authorization mechanisms like MTLS and certificates, to address these gaps and promote standardization in the Kubernetes ecosystem.
# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Admin network policy can be used to secure the entire cluster, but it's not yet widely adopted.                                                                  |
|   2 | Baseline admin network policy provides a default deny model, but it has limitations.                                                                             |
|   3 | Network policies are namespace-scoped, which can lead to complexity when dealing with large clusters.                                                            |
|   4 | Immutable identity is essential for predictable security, but it requires careful consideration of label changes and pod lifetimes.                              |
|   5 | Service accounts can be used as identities, but they require careful management to prevent unauthorized access.                                                  |
|   6 | External authorization mechanisms, such as OPA, can be used to delegate policy enforcement decisions.                                                            |
|   7 | MTLS (Mutual Transport Layer Security) is being explored for transmitting identities, but it's not yet widely adopted due to its complexity and limited support. |
|   8 | Standardization of identity transmission is essential for improving security and scalability in Kubernetes networks.                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Q15XbASxHM0)