---
layout: default
title:
  Aligning Enterprise AI Security With MITRE ATLAS Using Op... Doron Caspin &
  Valentina Rodriguez Sosa
nav_order: 13
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this session, Valentina Rodriguez and Dan Kaspin discuss the distinction
  between AI safety and AI security, emphasizing that their focus is on protecting
  AI models from malicious attacks rather than unintended harms. They outline common...
resource: https://www.youtube.com/watch?v=Va45Tx0RifI
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

In this session, Valentina Rodriguez and Dan Kaspin discuss the distinction between AI safety and AI security, emphasizing that their focus is on protecting AI models from malicious attacks rather than unintended harms.
They outline common AI security threats such as data poisoning, input manipulation, privacy leakage, prompt injection, supply chain attacks, and resource jacking, and introduce frameworks like MITRE ATT&CK and MITRE ATLAS for structuring AI security strategies.
The presenters demonstrate how open source tools, including Sigstore for model signing and verification, and StackRox for runtime security and policy enforcement, can be integrated into the AI model development lifecycle on Kubernetes platforms using tools like Kubeflow and Argo CD.
Through a live demo, they show how these tools help ensure model integrity, enforce organizational security policies, and monitor for vulnerabilities and suspicious behaviors.
The session concludes with recommendations to map AI development processes to security controls, implement zero trust and microsegmentation, and leverage community resources for ongoing improvement in AI security practices.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on AI security, not AI safety                                                                                         |
|   2 | Presenters: Valentina Rodriguez (Red Hat, Qflow maintainer) and Dan Kaspin (Treat, security product manager)                          |
|   3 | Agenda includes: AI safety vs. security, MITRE ATT&CK and MITRE ATLAS frameworks, AI risk convergence, open source tooling, and demos |
|   4 | AI safety: addresses unintended harm (e.g., toxic outputs, wrong answers)                                                             |
|   5 | AI security: protects models from malicious attempts, adversarial attacks, and process threats                                        |
|   6 | Seven major AI attack areas:                                                                                                          |
|   7 | Data poisoning (maliciously altering training data)                                                                                   |
|   8 | Input/data modification (incorrect decisions)                                                                                         |
|   9 | Privacy leakage (exposing private data via LLMs/chatbots)                                                                             |
|  10 | Prompt injection (similar to SQL injection)                                                                                           |
|  11 | Supply chain attacks (compromising model development)                                                                                 |
|  12 | Resource jacking (misusing GPUs for unauthorized tasks)                                                                               |
|  13 | Frameworks:                                                                                                                           |
|  14 | NIST AI RMF (CISO-level standard)                                                                                                     |
|  15 | OWASP Top 10 (developer-focused, includes LLMs)                                                                                       |
|  16 | MITRE ATT&CK (baseline for adversary tactics)                                                                                         |
|  17 | MITRE ATLAS (AI-specific threat landscape)                                                                                            |
|  18 | AI and traditional security processes are converging (data prep, training, deployment, monitoring)                                    |
|  19 | Emphasis on validating models, scanning for vulnerabilities, and ensuring bill of materials aligns with deployed code                 |
|  20 | Defense layers:                                                                                                                       |
|  21 | Pipeline integrity and validation (model signing, verification)                                                                       |
|  22 | Vulnerability scanning (tools: Clair, Grype, Trivy)                                                                                   |
|  23 | Workload identity (SPIFFE/SPIRE, MTLS, Falco for runtime monitoring)                                                                  |
|  24 | Input/output validation and guardrails                                                                                                |
|  25 | Demo highlights:                                                                                                                      |
|  26 | Model signing and verification using Sigstore/Six Store                                                                               |
|  27 | Model validation before deployment in Kubernetes                                                                                      |
|  28 | Use of ArgoCD for configuration management                                                                                            |
|  29 | StackRox for runtime security, policy enforcement, and vulnerability management                                                       |
|  30 | Qflow for AI platform management on Kubernetes                                                                                        |
|  31 | Importance of network policies, microsegmentation, and zero trust                                                                     |
|  32 | Open source tools and community resources recommended (Qflow, StackRox, Falco)                                                        |
|  33 | Q&A: Model sandboxing,                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Va45Tx0RifI)
