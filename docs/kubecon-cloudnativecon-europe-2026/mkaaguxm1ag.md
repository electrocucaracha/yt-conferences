---
layout: default
title:
  "Privacy as Infrastructure: Declarative Data Protection of... Joaquin Rodriguez
  & Krishnendu Dasgupta"
nav_order: 246
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Hain Rodriguez and Krishna Dazgupta Kish discuss
  the challenges of protecting sensitive data when using AI and large language models
  (LLMs) in Kubernetes environments, particularly the risks of unintentionally exposing...
resource: https://www.youtube.com/watch?v=mkAaguXm1ag
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

In this presentation, Hain Rodriguez and Krishna Dazgupta Kish discuss the challenges of protecting sensitive data when using AI and large language models (LLMs) in Kubernetes environments, particularly the risks of unintentionally exposing personally identifiable information (PII) and credentials.
They introduce a Kubernetes-first privacy architecture that leverages containerization, policy operators, admission webhooks, and sidecar containers to automatically detect, anonymize, and enforce privacy policies on AI workloads without requiring developers to modify their code.
The system uses open-source tools like Presidio for PII detection, supports detailed audit trails, and enables granular scaling and security through separate pods and tiers.
The presenters also demonstrate an eight-stage pipeline for secure code generation and execution, including privacy checks, static analysis, and sandboxing, and showcase an observability dashboard for monitoring privacy and security events.
The solution is designed for scalability and ease of deployment, with support for various AI models and hardware, and will be released as open source for broader adoption.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Hain Rodriguez (Microsoft, software engineer) and Krishna Dazgupta Kish (Axon Vortex AI, founder)                                                                                        |
|   2 | Topic: Privacy infrastructure and data protection for AI on Kubernetes                                                                                                                               |
|   3 | Problem: AI/LLMs often receive PII without detection, masking, isolation, or audit trails, posing security risks                                                                                     |
|   4 | Example risks: Developers accidentally sharing sensitive data (e.g., social security numbers, credentials) with LLMs                                                                                 |
|   5 | Solution: Need for privacy-focused architecture, not just libraries or filters                                                                                                                       |
|   6 | Proposed architecture: Kubernetes-first, with 23 containers across 7 tiers (infrastructure, privacy, LLM adapters, safety, platform, observability, UI)                                              |
|   7 | Each container/pod has its own port, GPU memory, and scales independently                                                                                                                            |
|   8 | Kubernetes features leveraged: CRDs, admission webhooks (inject privacy sidecar), RBAC, config map volumes (hot reload), GPU scheduling, horizontal pod autoscaler, service DNS, Helm, and Kustomize |
|   9 | Privacy policy operator: Kubernetes object applied via kubectl; defines what to protect (e.g., email, SSN, credit card, phone number) and how (hash, redact, replace)                                |
|  10 | Modes: Audit (logs/analyzes PII), Enforce (blocks requests if anonymization fails)                                                                                                                   |
|  11 | Privacy enforcement: Sidecar container intercepts AI API calls, uses Presidio for PII detection/anonymization, logs events to Postgres/Redis for audit trail                                         |
|  12 | No code changes required for developers; privacy is enforced via labels and sidecar injection                                                                                                        |
|  13 | Eight-stage pipeline: Privacy ingress, task normalization, LLM code generation, privacy/code leak check, static scan, security review, sandbox execution, output reflection                          |
|  14 | Uses open-source models (Quen, Cisco Foundation AI, Llama 3.1) for code generation and security reasoning                                                                                            |
|  15 | Security checks: Scanner runner (AST analysis), security reviewer (CVE checks), foundation reasoning model (trained on CVEs)                                                                         |
|  16 | Telemetry: Redis for caching, volume for logs, Postgres for metrics, 24 Prometheus metrics, observability dashboard                                                                                  |
|  17 | Threat patterns detected: Prompt i                                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mkAaguXm1ag)
