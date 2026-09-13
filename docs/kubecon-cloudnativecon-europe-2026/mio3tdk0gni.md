---
layout: default
title:
  "From Static Tokens to Attestation: The Evoluti... Ciprian H, Jack Francis
  M, Josephine P, & Justin B"
nav_order: 126
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The panel discusses the ongoing challenges of secure node joining in
  Kubernetes, highlighting that despite years of effort from major contributors at
  Microsoft, Google, and Red Hat, a standardized, robust solution remains elusive.
  Panelists...
resource: https://www.youtube.com/watch?v=MIO3tDk0GnI
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

The panel discusses the ongoing challenges of secure node joining in Kubernetes, highlighting that despite years of effort from major contributors at Microsoft, Google, and Red Hat, a standardized, robust solution remains elusive.
Panelists recount recurring vulnerabilities, such as over-reliance on instance metadata services and insufficiently locked-down permissions, which can lead to severe security breaches.
They emphasize the complexity introduced by diverse user requirements, hybrid cloud environments, and the lack of unified attestation and registration mechanisms across cloud providers.
The discussion explores potential improvements, including the use of hardware-backed certificates, TPMs, and external attestation servers, but notes the difficulty of implementing consistent solutions given the variability in infrastructure and cloud capabilities.
Ultimately, the panel agrees on the need for an open, standardized, and low-effort approach that balances security with usability, and calls for greater collaboration within the Kubernetes community to define and document best practices for secure node joining.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focused on secure node joining in Kubernetes.                                                                        |
|   2 | Panelists from Microsoft, Google, Red Hat, and IBM introduced themselves and their experience with Kubernetes.                  |
|   3 | The problem of secure node joining remains unsolved despite years of effort.                                                    |
|   4 | Common vulnerabilities include overexposing information in instance metadata services, leading to potential cluster compromise. |
|   5 | RBAC misconfigurations and insecure user data scripts can allow arbitrary code execution on new nodes.                          |
|   6 | Rolling certificates and maintaining security for day-two operations is challenging.                                            |
|   7 | Increasing cluster complexity and multiple node joining methods expand the attack surface.                                      |
|   8 | Lack of a unified approach to node attestation and secure boot in Kubernetes.                                                   |
|   9 | Users often attempt to secure clusters without sufficient expertise, leading to misconfigurations.                              |
|  10 | Node attestation defined as a node's ability to prove its identity to the control plane.                                        |
|  11 | Managed Kubernetes services have more control over node joining; hybrid and multi-cloud scenarios complicate attestation.       |
|  12 | Node registration often uses bootstrap tokens, but their security varies across providers.                                      |
|  13 | Hardware and software attestation layers are both important.                                                                    |
|  14 | IBM Cloud and Carpenter use metadata service and token service for node attestation.                                            |
|  15 | No consistent "bare minimum" for secure node joining across cloud providers.                                                    |
|  16 | Lack of standardization in Kubernetes for node attestation and secure joining.                                                  |
|  17 | Cloud providers offer varying security features (e.g., TPM, attested metadata), but no universal solution.                      |
|  18 | Need for solutions that support both advanced and basic user requirements.                                                      |
|  19 | Suggestions include using certificates or TPMs for node identity, but implementation and validation differ by provider.         |
|  20 | Desire for an open standard and collaboration with Kubernetes SIGs (e.g., sig-auth).                                            |
|  21 | Current solutions are fragmented and lack thorough auditing.                                                                    |
|  22 | Bare metal and low-cost VPS environments present unique challenges due to l                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MIO3tDk0GnI)
