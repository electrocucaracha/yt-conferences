---
layout: default
title:
  "Strengthening Kubernetes Trust: SIG Auth's Latest Se... Anish R, Mo K, Stanislav
  L, Rita Z & Peter E"
nav_order: 293
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The SIGOT deep dive session covered numerous updates and features in
  Kubernetes, focusing on security, authentication, and resource management. Key highlights
  included the introduction of constraint impersonation, which allows more granular...
resource: https://www.youtube.com/watch?v=SqdD9waaeno
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

The SIGOT deep dive session covered numerous updates and features in Kubernetes, focusing on security, authentication, and resource management.
Key highlights included the introduction of constraint impersonation, which allows more granular control over Kubernetes impersonation permissions, and the dynamic resource allocation (DRA) feature that enables flexible allocation and sharing of specialized devices like GPUs, with new admin access controls.
Updates to authentication include structured authenticator configuration, support for multiple JWT authenticators, enhanced validation, and improved metrics.
Security improvements were discussed for CSI drivers, such as moving service account tokens from volume context to secrets to prevent exposure, and updates to the secret store CSI driver for better integration and security.
Additional features presented were workload identity for image pulls, ensuring secret images are only accessible to authorized pods, pod certificates for automated certificate management, and restricted anonymous authentication to limit unauthenticated access.
Other notable changes included pod security admission restrictions to prevent SSRF attacks, external signing of service account tokens for better key management, and a new credential plugin policy and allow list in client-go and kubectl to control which binaries can fetch credentials, enhancing overall cluster security and user control.
The session concluded with a Q&A addressing implementation details and security considerations for these new features.

# Main Points

|   # | Main point                                                                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIGOT deep dive session with multiple tech leads and community members presenting                                                                                                                       |
|   2 | Introduced new "constraint impersonation" in Kubernetes 1.35, allowing more granular scoping for impersonation beyond all-or-nothing                                                                    |
|   3 | Constraint impersonation enables service accounts to have node-specific pod read access, maintaining backward compatibility                                                                             |
|   4 | DRRA (Dynamic Resource Allocation) feature enables flexible allocation and sharing of specialized devices (e.g., GPUs, networking)                                                                      |
|   5 | DR admin access allows admin workloads (metrics, troubleshooting) to access devices already in use, now core in Kubernetes                                                                              |
|   6 | Structured authenticator config (GA in 1.34): supports multiple JWT authenticators, multiple audiences, claim/user validation, and egress selector support; new metrics in 1.35                         |
|   7 | CSI driver update: service account tokens now sent via secrets instead of volume context for improved security and backward compatibility                                                               |
|   8 | Secret Store CSI driver: integrates external secret stores, supports secret rotation, moving to "requires republish" for reduced RBAC permissions, adding filesystem ownership config and new providers |
|   9 | Workload identity for image pulls (beta in 1.34): service account tokens used for pod-specific image pulls, improving security                                                                          |
|  10 | "Ensure secret images" (beta): adds authorization layer in kubelet to restrict access to private images based on credentials used to pull them                                                          |
|  11 | Pod certificates (beta in 1.35): allows mounting certificates in pods via projected volumes and automated certificate requests/signing                                                                  |
|  12 | Restricted anonymous authentication (GA in 1.34): limits unauthenticated user access to specified API endpoints at the authentication layer                                                             |
|  13 | Pod Security Admission (PSA) restrictions for probe host fields: defaults probe host fields to pod IP to reduce SSRF attack surface                                                                     |
|  14 | External signing of service account tokens: enables use of external KMS/vault for signing, supports key rotation without API server restart                                                             |
|  15 | Credential plugin policy and allow list in cli                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SqdD9waaeno)
