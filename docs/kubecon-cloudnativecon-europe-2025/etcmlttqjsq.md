---
type: Video Note
title: "Trust No One: Secure Storage With Confidential Containers - Aurélien Bombo, Microsoft"
description: "Aurelian Bombo from Microsoft discusses confidential computing, a future of computing where data is protected not only at rest and in transit but also in use. He focuses on storage, specifically enabling secure storage for containers. Confi..."
resource: https://www.youtube.com/watch?v=etCmLttqJsQ
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Aurelian Bombo from Microsoft discusses confidential computing, a future of computing where data is protected not only at rest and in transit but also in use.
He focuses on storage, specifically enabling secure storage for containers.
Confidential containers project aims to protect data from cloud providers by leveraging trusted execution environments (TEs) and security policies.
The project uses Kata containers, which virtualize containers inside VMs, and a CSI driver to create an empty block storage device.
Encryption keys are stored in a key broker service, and the confidential data hub ensures the trustworthiness of the container spec through remote attestation.
Persistent storage is also discussed, with plans to integrate a new API between the kata agent and the container to enable user-controlled key management.
The presentation concludes that confidential computing is crucial for protecting sensitive data from malicious cloud providers.
# Main Points

|   # | Main point                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------- |
|   1 | Confidential computing aims to protect data at rest, in transit, and in use.                                      |
|   2 | The confidential containers project focuses on enabling secure storage and deployment of confidential containers. |
|   3 | Container runtimes like Kata Containers use virtualization to isolate containers from each other and the host.    |
|   4 | The confidential containers project uses a Trusted Execution Environment (TEE) to guarantee confidentiality.      |
|   5 | A security policy is used to enforce trustworthiness of container specifications.                                 |
|   6 | Kubernetes CSI drivers are used to provision storage for confidential containers.                                 |
|   7 | Ephermal storage provides temporary, non-persistent storage for confidential data.                                |
|   8 | Persistent storage requires encryption and key management to protect data at rest.                                |
|   9 | The addition protocol is used to securely retrieve decryption keys for persistent storage.                        |
|  10 | Performance issues may arise from the encryption layer and bootstrapping process.                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=etCmLttqJsQ)