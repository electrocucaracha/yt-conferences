---
type: Video Note
title: "Strengthening Supply Chain for Kubernetes: Cross-Cloud SLSA Attestation... Feynman Zhou & Dahu Kuang"
description: "Feman from Microsoft Azure and Dahu from Alibaba Cloud introduced the challenges of securing the software supply chain, particularly for Kubernetes deployments and AI workloads. They discussed the importance of enforcing security best pract..."
resource: https://www.youtube.com/watch?v=no3Hg6u80YE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Feman from Microsoft Azure and Dahu from Alibaba Cloud introduced the challenges of securing the software supply chain, particularly for Kubernetes deployments and AI workloads.
They discussed the importance of enforcing security best practices and highlighted the limitations of only validating supply chain metadata at download time, emphasizing the need for enforcement at deployment.
The speakers explained the SALSA framework’s levels for supply chain security, detailing how provenance and attestation can ensure only trusted images are deployed.
They showcased how open source projects like Notary and Ratify, along with plugins such as the SALSA verifier, can be integrated with policy engines like OPA Gatekeeper to enforce compliance in Kubernetes clusters.
A live demo illustrated how these tools block non-compliant images and admit only those meeting higher SALSA levels, demonstrating end-to-end source integrity for AI workflows.
# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Feman (Microsoft Azure, CNCF Notary & Ratify maintainer) and Dahu (Alibaba Cloud, Notary contributor) introduced themselves.                                                       |
|   2 | The session covers real-world software supply chain challenges and open source frameworks like SLSA, Ratify, and Notary.                                                           |
|   3 | Demonstrations focus on securing Kubernetes deployments and AI workloads using these tools.                                                                                        |
|   4 | Security teams enforce best practices and checklists, but vulnerabilities can still occur even with controls in CI/CD pipelines.                                                   |
|   5 | Current validation often checks supply chain metadata (signatures, attestations) at download, but not always at deployment to Kubernetes.                                          |
|   6 | Industry standards like SLSA and container secure supply chain frameworks exist, but security incidents remain frequent.                                                           |
|   7 | SLSA framework defines four levels for supply chain security, focusing on source control, build, and deployment phases.                                                            |
|   8 | SLSA Level 1: Use compliant source control, preserve commit history, verify commits.                                                                                               |
|   9 | SLSA Level 2: Enforce protected branches/tags, ensure all commits are auditable.                                                                                                   |
|  10 | SLSA Level 3: Use provenance files to verify code and images are from trusted identities, include detailed metadata.                                                               |
|  11 | SLSA Level 4: Require two-party reviews for changes to protected branches.                                                                                                         |
|  12 | Notary Project provides PKI-based signing and verification for container images and files, with support from major cloud providers.                                                |
|  13 | Ratify is a verification framework that extends Notary, supports plugins (e.g., SLSA verifier), and integrates with policy engines like OPA Gatekeeper and Kyverno.                |
|  14 | Ratify can be used as an admission controller in Kubernetes, CLI in CI/CD, or with container runtimes.                                                                             |
|  15 | Workflow: Developers sign images, scan for vulnerabilities, generate SLSA provenance, attach metadata, and push to registry; Ratify and Gatekeeper enforce policies at deployment. |
|  16 | Demo: Deploying AI agent workloads in Kubernetes, enforcing SLSA compliance using Ratify and Gatekeeper.                                                                           |
|  17 | Only images compliant with required SLSA levels (e.g., Level 2 or 3) are admitt                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=no3Hg6u80YE)