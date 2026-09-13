---
layout: default
title: Real-World Supply-Chain Security - Alex Leong, Buoyant
nav_order: 306
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Alex Leong, a software engineer at Buoyant and long-time contributor
  to the Linkerd service mesh, discusses practical approaches to supply chain security
  in software development. He explains that supply chain security involves providing
  det...
resource: https://www.youtube.com/watch?v=1Pd28J4kpN8
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

Alex Leong, a software engineer at Buoyant and long-time contributor to the Linkerd service mesh, discusses practical approaches to supply chain security in software development.
He explains that supply chain security involves providing detailed, verifiable information about software artifacts—such as cryptographic signatures, software bills of materials (SBOMs), build attestations, and VEX documents—to empower consumers to assess and respond to vulnerabilities.
Leong outlines how these attestations can be generated, delivered, and managed using tools like cosign, Snyk, Sift, and the OCI registry with referrers, ensuring immutability of images while enabling continuous vulnerability monitoring and policy enforcement through engines like Kyverno.
He emphasizes the importance of clear documentation and streamlined processes to reduce friction for consumers, acknowledges the evolving nature of the ecosystem, and encourages both producers and consumers to adopt and demand robust supply chain transparency.
The session concludes with audience questions about tooling, policy enforcement, and the growing complexity of supply chain requirements, highlighting ongoing challenges and future directions in the field.

# Main Points

|   # | Main point                                                                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Alex Leong, software engineer at Buoyant, creator of Linkerd service mesh, presenting on supply chain security.                                                                                                                     |
|   2 | Linkerd is an open source CNCF graduated project; Buoyant also offers an enterprise distribution (BEL).                                                                                                                             |
|   3 | Enterprise distribution emphasizes supply chain security, important for enterprises.                                                                                                                                                |
|   4 | Supply chain security involves understanding and describing everything influencing software behavior: code, dependencies (direct and transitive), build systems/tools, containers, OS, hardware, networking, Kubernetes, APIs, etc. |
|   5 | Software producers mainly control library dependencies, build tool, and container.                                                                                                                                                  |
|   6 | Impossible to guarantee zero vulnerabilities; best practice is to describe the supply chain in detail for consumers.                                                                                                                |
|   7 | Four main supply chain descriptors:                                                                                                                                                                                                 |
|   8 | Signatures: cryptographically verify software origin and integrity (e.g., using cosign, SIGstore, Notary).                                                                                                                          |
|   9 | SBOMs (Software Bill of Materials): list all dependencies and versions (tools: Sift, Snyk; formats: SPDX, CycloneDX).                                                                                                               |
|  10 | Build attestations: describe how software was built (e.g., SALSA documents).                                                                                                                                                        |
|  11 | VEX documents: provide context on vulnerabilities and their impact on the software.                                                                                                                                                 |
|  12 | All descriptors can and should be signed; collectively called attestations.                                                                                                                                                         |
|  13 | OCI (Open Container Initiative) format allows storing images and attestations in registries.                                                                                                                                        |
|  14 | OCI "referrers" enable adding attestations without changing the image, preserving immutability.                                                                                                                                     |
|  15 | Tools: ORAS discover for querying attestations; cosign for signature verification; Grype for vulnerability scanning; Kyverno for policy enforcement.                                                                                |
|  16 | Consumers should use these tools to verify signatures, check SBOMs, scan for vulnerabilities, and enforce policies.                                                                                                                 |
|  17 | Ecosystem is evolving; documentation and policies help reduce friction for users.                                                                                                                                                   |
|  18 | No widely known GUI tools for verification; policies can automate enforcement.                                                                                                                                                      |
|  19 | SBOMs and attestations are generated per build and stored in registries.                                                                                                                                                            |
|  20 | Future supply chain transparency ma                                                                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1Pd28J4kpN8)
