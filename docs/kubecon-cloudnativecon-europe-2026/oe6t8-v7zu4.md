---
layout: default
title:
  "Your Models Are Vulnerable: How KitOps Turns KServe Into a Zero-Tru... Brad
  Micklea & Gavrish Prabhu"
nav_order: 407
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presenters discuss the vulnerabilities of AI deployments and introduce
  tools and best practices to enhance security. They explain how KServe simplifies
  serving inference workloads across various runtimes but emphasizes that security
  mea...
resource: https://www.youtube.com/watch?v=OE6t8_V7ZU4
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

The presenters discuss the vulnerabilities of AI deployments and introduce tools and best practices to enhance security.
They explain how KServe simplifies serving inference workloads across various runtimes but emphasizes that security measures, such as model verification and chain of custody, must be implemented by users.
KitOps, a CNCF project, enables OCI-native packaging of AI/ML artifacts—including models, datasets, and documentation—ensuring integrity, provenance, and auditability through cryptographic signatures and attestations.
The workflow involves building, verifying, and deploying model kits, with policies and attestations embedded to control access and deployment, even supporting advanced registry-level quarantine for unverified artifacts.
A live demo illustrates integrating KitOps with KServe to enforce zero-trust inference, where only attested models are deployed, and unverified ones are blocked.
The Q&A addresses practical adoption, integration with existing MLOps tools, handling large datasets, and the importance of starting security at the training phase, highlighting KitOps’ flexibility and growing community support.

# Main Points

|   # | Main point                                                                                                                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Brad Mikley (CNCF maintainer, CEO of Jozu) and Gavish Prabhu (Nutanix, KServe maintainer).                                                                                                                                  |
|   2 | KServe helps deploy inference workloads with any runtime via inference service CR; supports generative and predictive AI.                                                                                                                             |
|   3 | KServe integrates with LLMs, supports autoscaling, networking, and disaggregated inference.                                                                                                                                                           |
|   4 | KServe prioritizes ease of use over security; users must add security measures.                                                                                                                                                                       |
|   5 | Security recommendations: verify model/agent identity, validate signatures and attestations, track datasets, maintain audit-ready evidence and chain of custody.                                                                                      |
|   6 | Zero trust for inference: verify identity and integrity at deploy time, fail closed if verification fails.                                                                                                                                            |
|   7 | KitOps is a CNCF sandbox project for OCI-native packaging of AI/ML artifacts (models, datasets, configs, prompts).                                                                                                                                    |
|   8 | KitOps provides content-addressable storage, SHA-256 digests, and supports chain of custody.                                                                                                                                                          |
|   9 | Current industry practice: artifacts (models, data, code, docs) are scattered; KitOps unifies them for versioning and audit.                                                                                                                          |
|  10 | Example: Large logistics company uses KitOps for unified, secure, and flexible AI/ML operations across global teams and platforms.                                                                                                                    |
|  11 | KitOps workflow: build phase (pack models, data, scripts), verification phase (compliance review, attestations), deploy phase (serving configs, telemetry).                                                                                           |
|  12 | Security levels: 1. Basic verification (SHA, signature check) before deployment. 2. Policy enforcement (security, performance, compliance) before serving. 3. Registry-level quarantine and pull policies to prevent unsafe artifacts from spreading. |
|  13 | Demo: KitOps and KServe integration for zero trust inference; models are attested and verified before deployment; unverified models are blocked.                                                                                                      |
|  14 | KitOps adoption: 250,000+ downloads; used as a gate between development and production.                                                                                                                                                               |
|  15 | Hardening steps: secure packaging/signing, approvals, security scanning, admission policy checks, cryptographically secured audit logs.                                                                                                               |
|  16 | Attestations recommended for policy/evaluation                                                                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OE6t8_V7ZU4)
