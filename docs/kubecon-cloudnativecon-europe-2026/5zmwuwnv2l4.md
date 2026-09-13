---
layout: default
title:
  "Securing the AI/ML Lifecycle With MLSecOps: Open Source Best... Bahaulddin
  Shammary & Andrey Shorov"
nav_order: 329
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Baja, a lead AI engineer at Openext, and Andre
  Shoven, a senior security specialist, discuss the growing importance of securing
  AI and machine learning (ML) systems in production as organizations increasingly
  adopt ML...
resource: https://www.youtube.com/watch?v=5ZmWuwnv2l4
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

In this presentation, Baja, a lead AI engineer at Openext, and Andre Shoven, a senior security specialist, discuss the growing importance of securing AI and machine learning (ML) systems in production as organizations increasingly adopt ML technologies.
They highlight that ML systems introduce unique risks—such as data poisoning, model theft, and adversarial attacks—that differ from traditional software vulnerabilities, necessitating an extension of DevSecOps principles into the ML lifecycle, termed ML SecOps.
The speakers introduce a reference architecture that maps nine primary lifecycle stages, emphasizing the need for clear security control points and shared responsibility among various personas, including data scientists, engineers, and security practitioners.
They advocate for using frameworks like the OWASP ML Top 10 to identify and prioritize threats, and recommend integrating open-source tools (e.g., Sigstore, SLSA, Scorecard, GUAC) to address integrity, provenance, and traceability, while noting that many tools require adaptation for ML-specific artifacts.
Key recommendations include automating security processes, embedding security roles from the outset, versioning all assets, and investing in team training and awareness, as ML SecOps is a supplementary layer that must be integrated throughout the ML lifecycle to effectively mitigate evolving risks.

# Main Points

|   # | Main point                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Baja (Lead AI Engineer, Openext) and Andre Shoven (Senior Security Specialist) present on securing AI and machine learning systems in production.                                                      |
|   2 | ML systems introduce new risks not present in traditional software, including data poisoning, model theft/tampering, risks from continuous retraining, and adversarial inputs at inference endpoints.  |
|   3 | DevSecOps principles (automation, shared responsibility, security as code) apply but must be extended for ML; this is the focus of ML SecOps.                                                          |
|   4 | The talk is based on a white paper developed with Dell, Ericsson, and the AI/ML OpenSSF working group.                                                                                                 |
|   5 | Introduced a reference architecture mapping nine primary ML lifecycle stages, from planning/design to monitoring, organized into planning, experimentation/development, and staging/operation domains. |
|   6 | Manual processes (yellow) and automated processes (blue) are distinguished; every artifact movement is a potential security risk.                                                                      |
|   7 | Each lifecycle stage is a control point; security must be embedded at every handoff between people, systems, and stores.                                                                               |
|   8 | Personas involved include data scientists, data engineers, security practitioners, software developers, and MLOps engineers; security is a shared responsibility at every stage.                       |
|   9 | ML systems are non-deterministic, data-dependent, and continuously evolving, making risk assessment and root cause analysis challenging.                                                               |
|  10 | ML-specific threats include data/model poisoning, adversarial inputs, privacy leaks, and supply chain risks (e.g., compromised libraries).                                                             |
|  11 | Used OWASP ML Top 10 as a baseline for threat modeling and prioritizing security controls.                                                                                                             |
|  12 | Supply chain risks are pervasive across all stages; provenance and trust in assets are critical.                                                                                                       |
|  13 | Security controls must be embedded from design through operation, not added at the end (“shift left”).                                                                                                 |
|  14 | Recommended open source tools: Sigstore (signing/verification), SLSA (provenance), Scorecard/Allstar (repository hardening), GUAC (artifact/dependency graphing).                                      |
|  15 | Most open source tools need ext                                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5ZmWuwnv2l4)
