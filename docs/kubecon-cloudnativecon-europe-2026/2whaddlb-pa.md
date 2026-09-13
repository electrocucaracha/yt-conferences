---
type: Video Note
title: "Beyond Image Pull-Time: Ensuring Runtime Integrit... Toddy Mladenov, Flora Taagen & Dallas Delaney"
description: "The presentation introduces enhancements to the Notary Project, a CNCF initiative focused on supply chain security for container images. Traditionally, Notary signs and verifies container images at the manifest level during the pull phase..."
resource: https://www.youtube.com/watch?v=2WhADdlb_pA
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation introduces enhancements to the Notary Project, a CNCF initiative focused on supply chain security for container images.
Traditionally, Notary signs and verifies container images at the manifest level during the pull phase, but this leaves a security gap: after images are pulled, individual cached layers can be tampered with on disk without detection, especially in multi-tenant environments.
To address this, the team proposes per-layer image signing combined with Linux’s DM-Verity, enabling continuous integrity verification at both runtime and at rest.
The solution involves generating a DM-Verity root hash and signing it for each image layer, storing these signatures as OCI artifacts alongside the image, and configuring the container runtime (e.g., containerd with the EOFS snapshotter) to verify these signatures and enforce DM-Verity protections.
Demonstrations show that this approach prevents tampered layers from being executed, even if an attacker modifies cached files after pull, thus significantly reducing the attack surface and providing kernel-level, non-bypassable protection for container images.
The solution is being integrated into upcoming containerd releases and can be used in both rootful and rootless environments.
# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Notary Project is a CNCF project focused on supply chain security.                                                                         |
|   2 | Two main tools: Notation CLI (for signing OCI artifacts) and Ratify (external data provider for OPA Gatekeeper for admission control).     |
|   3 | Notary Project is used by companies like Microsoft, AWS, and Alibaba Cloud.                                                                |
|   4 | Current signing process:                                                                                                                   |
|   5 | Image is built (e.g., with Docker or GitHub Actions).                                                                                      |
|   6 | Notary Project signs the image manifest digest, creating a cryptographic signature.                                                        |
|   7 | Signature is stored as a separate OCI artifact in the registry.                                                                            |
|   8 | At pull time, signature is verified to ensure image integrity and trusted origin.                                                          |
|   9 | Limitation: Only manifest is signed and verified at pull time; individual image layers are not continuously reverified after pull.         |
|  10 | Security risk: Post-pull tampering of cached image layers can go undetected, especially in multi-tenant environments.                      |
|  11 | Example attack scenario:                                                                                                                   |
|  12 | Image is signed and verified.                                                                                                              |
|  13 | Attacker gains host access and modifies a cached image layer.                                                                              |
|  14 | Modified layer is mounted at container start without further verification, allowing malicious code execution.                              |
|  15 | OCI image layers are identified by content address digests and cached on disk.                                                             |
|  16 | DM-Verity (device mapper verity) is a Linux kernel feature providing block-level, read-only protection using Merkle trees and root hashes. |
|  17 | At runtime, DM-Verity checks every read against the expected root hash; mismatches block access.                                           |
|  18 | Solution: Extend Notary Project with per-layer image signing backed by DM-Verity for continuous integrity at runtime and at rest.          |
|  19 | Build-time steps:                                                                                                                          |
|  20 | Generate EROFS images for each OCI layer.                                                                                                  |
|  21 | Create DM-Verity Merkle trees and root hashes.                                                                                             |
|  22 | Sign root hashes with private key; package with certificate in PKCS7 envelopes.                                                            |
|  23 | Store artifacts in OCI registry attached to the image.                                                                                     |
|  24 | Runtime steps:                                                                                                                             |
|  25 | Container runtime (e.g., containerd with EROFS snapshotter) pulls images and new artifacts.                                                |
|  26 | PKCS7 envelope is sent to kernel for certificate and signature va                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2WhADdlb_pA)