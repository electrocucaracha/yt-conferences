---
layout: default
title:
  "The Ultimate Container Challenge: An Interactive Trivia Game on Su... Aurélie
  Vache & Sherine Khoury"
nav_order: 317
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  'The video presents the "Ultimate Kutan Challenge: Secret Chain Edition,"
  an interactive quiz and demo session focused on supply chain security for container
  images. The hosts introduce themselves and guide participants through key concepts...'
resource: https://www.youtube.com/watch?v=n_tkj5KmzzE
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

The video presents the "Ultimate Kutan Challenge: Secret Chain Edition," an interactive quiz and demo session focused on supply chain security for container images.
The hosts introduce themselves and guide participants through key concepts such as image signing, SBOM (Software Bill of Materials) generation, provenance attestation, and vulnerability management.
They demonstrate tools like Cosign, Notation, Trivy, Docker Scout, and ORAS for signing images, generating and attaching SBOMs, and creating provenance attestations.
The session emphasizes the importance of verifying image signatures, understanding SBOM limitations, using VEX files to clarify vulnerability exploitability, and automating policy enforcement in Kubernetes clusters with tools like Kyverno and Gatekeeper.
The presenters conclude by highlighting the evolving nature of supply chain security and the need to combine multiple tools and practices for robust protection.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The event is the "Ultimate Kutan Challenge: Secret Chain Edition," focusing on supply chain security.                                                                                 |
|   2 | Presenters: Developer advocate at OC Cloud (specialized in CI/CD, infra as code, developer experience) and Shireen from Red Hat (works on OpenShift, active in Kubernetes community). |
|   3 | Attendees participate via a Slido quiz using a QR code.                                                                                                                               |
|   4 | The presenters built a Golang app ("Gophers API") and aim to safely take its image to production.                                                                                     |
|   5 | Emphasis on not trusting public registry images blindly; always check for signatures and security scans.                                                                              |
|   6 | Signature indicators: DockerHub (icons), quay.io (shield), Harbor (green check/red cross), SBOM details, vulnerability scan results.                                                  |
|   7 | Tools to sign images: Cosign and Notation (Docker Content Trust is retiring).                                                                                                         |
|   8 | Demo: Signing OCI artifacts with Cosign and Notation, pushing to private registries, and checking signature status in Harbor.                                                         |
|   9 | Images can also be signed with Pman using a sixstar param file.                                                                                                                       |
|  10 | SBOM (Software Bill of Materials) inventories all image components; formats include SPDX and CycloneDX.                                                                               |
|  11 | Different SBOM tools may produce different results for the same image.                                                                                                                |
|  12 | Demo: Generating SBOMs with Trivy, Docker Scout, Pman, and Bomb; attaching SBOMs to registries with oras.                                                                             |
|  13 | Salsa provenance attestation provides verifiable build history; generated in CI, signed, and distributed.                                                                             |
|  14 | Demo: Generating and extracting provenance attestation with Docker and Docker Scout.                                                                                                  |
|  15 | Vulnerabilities: Not all CVEs are exploitable; VEX (Vulnerability Exploitability eXchange) clarifies exploitability status.                                                           |
|  16 | VEX formats: CEF and CycloneDX; OpenVEX by Linux Foundation.                                                                                                                          |
|  17 | Demo: Using Trivy and GoCheck to identify and attest to non-exploitable vulnerabilities; pushing VEX to registry with Cosign.                                                         |
|  18 | Signature and attestation checks can be automated in Kubernetes using Kyverno and OPA+Gatekeeper.                                                                                     |
|  19 | Demo: Enforcing image signature policies in Kubernetes; signed images allowed, unsigned images blocked.                                                                               |
|  20 | Tools used: Cosign, Notation, T                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=n_tkj5KmzzE)
