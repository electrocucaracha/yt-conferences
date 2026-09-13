---
layout: default
title:
  "The Hidden Risks in AI/ML Supply Chains: How To Secure Your Workloads - Yash
  Pimple, Chainguard"
nav_order: 310
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speaker discusses the hidden risks in the machine learning (ML) supply
  chain, emphasizing how its complexity and unique dependencies create a larger attack
  surface compared to traditional software supply chains. They highlight recent in...
resource: https://www.youtube.com/watch?v=3lcyFfA1Wbk
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

The speaker discusses the hidden risks in the machine learning (ML) supply chain, emphasizing how its complexity and unique dependencies create a larger attack surface compared to traditional software supply chains.
They highlight recent increases in supply chain attacks, such as the SolarWinds incident, and explain how vulnerabilities can arise at various stages, including data poisoning during preprocessing, compromised model hubs, and unverified third-party dependencies.
To address these risks, the speaker introduces several open-source tools and community initiatives: Software Bill of Materials (SBOMs) for transparency, AI-specific BOMs and model cards for documenting model provenance and limitations, model scanning tools to detect vulnerabilities, and model signing for verifying authenticity.
While these tools improve transparency, integrity, and authenticity in the ML workflow, challenges remain, particularly in certifying training data provenance and preventing data poisoning.
The session concludes with a demonstration of scanning and signing a model, and a Q&A addressing current limitations and ongoing developments in securing the ML supply chain.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on hidden risks in the ML/AI supply chain and securing them using open source tools.                            |
|   2 | Traditional software supply chains involve developers, source code, third-party dependencies, artifact building, and deployment. |
|   3 | ML supply chains are similar but have additional subcomponents and a larger, less understood attack surface.                     |
|   4 | Key risks in ML supply chains include:                                                                                           |
|   5 | Data poisoning during data processing.                                                                                           |
|   6 | Blind trust in pre-trained models from cloud providers without validating their pipelines or datasets.                           |
|   7 | Compromised model hubs or repositories.                                                                                          |
|   8 | Use of unauthenticated third-party modules and dependencies.                                                                     |
|   9 | Outsourcing model training without knowledge of the underlying infrastructure.                                                   |
|  10 | Attackers increasingly target package dependencies and transitive dependencies in Python-based ML projects.                      |
|  11 | Security principles for ML supply chains: transparency, integrity, and authenticity.                                             |
|  12 | Key tools and strategies discussed:                                                                                              |
|  13 | SBOMs (Software Bill of Materials) for transparency about dependencies, vulnerabilities, and licenses.                           |
|  14 | AI BOMs (AI Bill of Materials) for model-specific components (still under development).                                          |
|  15 | Model Cards for standardized documentation of model details, datasets, pipelines, and limitations.                               |
|  16 | Model Scan, an open-source tool to scan models (e.g., pickle files) for vulnerabilities and tampering.                           |
|  17 | Model Signing (e.g., using Sigstore) to cryptographically sign models, ensuring authenticity and traceability.                   |
|  18 | GitOps for packaging and deploying signed models.                                                                                |
|  19 | Demonstrated scanning and signing a model, then verifying its authenticity on Hugging Face.                                      |
|  20 | Some tools (e.g., bombctl) are emerging for generating AI BOMs.                                                                  |
|  21 | Certificate authorities for model signing can be public (e.g., Fulcio/Sigstore) or privately hosted.                             |
|  22 | Current solutions do not fully address data poisoning or certify ethical training data.                                          |
|  23 | No existing tools for debugging ML models at the logic/weight level or certifying training datasets' et                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=3lcyFfA1Wbk)
