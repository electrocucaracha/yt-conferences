---
layout: default
title: "Objection! AI Security Mistakes on Trial With Kubeflow and Confidential... Annie Talvasto & Karl Ots"
nav_order: 10
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: 'In a session themed as a "cloud native courtroom," speakers Annie Tvesto and Carl discuss four critical AI security mistakes: supply chain attacks, hallucinations, AI platform jacking, and prompt i...'
resource: "https://www.youtube.com/watch?v=Y2XPq3BRyrI"
youtube_stats:
  view_count: 126
  like_count: 3
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

In a session themed as a "cloud native courtroom," speakers Annie Tvesto and Carl discuss four critical AI security mistakes: supply chain attacks, hallucinations, AI platform jacking, and prompt injection.
The presentation highlights that traditional software security practices, such as verifying dependencies and managing secrets, must be adapted for AI workflows to mitigate risks like malicious pickle files and hardcoded API keys.
To address hallucinations and prompt injection, the speakers recommend implementing Retrieval-Augmented Generation (RAG), policy guardrails, and robust monitoring using tools like OpenTelemetry.
Additionally, the session introduces CubeFlow for orchestrating secure ML pipelines and Confidential Containers for providing hardware-backed trusted execution environments that protect data even from cloud providers.
The audience voted prompt injection as the most severe offense, and the speakers concluded by encouraging involvement in CNCF working groups and exploring resources like the OWASP Top 10 for LLM applications.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session identifies four major AI security mistakes: supply chain attacks, hallucinations, AI platform jacking, and prompt injection.                          |
|   2 | Supply chain attacks in AI involve vulnerabilities in model packages, such as the use of pickle files which are prone to remote code execution.                   |
|   3 | Trusting third-party data providers without verification can lead to privacy breaches if they change policies to train on user data.                              |
|   4 | Mitigations for supply chain risks include using verified publishers, implementing security bills of materials, and applying DevSecOps practices to ML workflows. |
|   5 | Hallucinations are difficult to detect because false information is presented alongside factually correct output.                                                 |
|   6 | Open-domain hallucinations reference non-existent sources, while closed-domain hallucinations can be verified against specific source materials.                  |
|   7 | Preventing hallucinations involves using Retrieval-Augmented Generation (RAG), closed-domain verification pipelines, and policy constraints via guardrails.       |
|   8 | AI platform jacking occurs when attackers steal API keys or exploit unpatched vulnerabilities to take over AI services.                                           |
|   9 | A recent incident involved a live-streamed developer whose hardcoded secrets were stolen, resulting in the deletion of their work.                                |
|  10 | Unpatched ingress controller vulnerabilities have also been exploited to compromise AI platforms.                                                                 |
|  11 | Best practices for preventing platform jacking include avoiding hardcoded secrets, using key vaults, and adhering to cloud security standards.                    |
|  12 | Prompt injection involves manipulating LLMs through crafted prompts to cause unsafe outputs, disclose sensitive information, or enable remote code execution.     |
|  13 | Direct prompt injection is often referred to as jailbreaking, while indirect injection occurs through external content like files.                                |
|  14 | Mitigation strategies for prompt injection include system message hardening, input/output safety filters, and continuous log monitoring.                          |
|  15 | Tools like NVIDIA NeMo Guardrails and Meta Llama Guard can help classify and filter harmful prompts.                                                              |
|  16 | The audience voted prompt injection as the most severe security mistake among the four discussed.                                                                 |
|  17 | Kubeflow is a cloud-native platform for orchestrating the ML lifecycle, allowing security guardrails to be integrated into pipelines.                             |
|  18 | OpenTelemetry is used for application-specific monitoring and logging to track hallucination rates and detect injection attempts.                                 |
|  19 | Confidential Containers is a CNCF sandbox project that uses hardware-backed trusted execution environments to isolate workloads from the host and cloud provider. |
|  20 | Confidential computing enables secure multi-party collaboration, such as financial institutions sharing data for fraud detection without exposing raw data.       |
|  21 | The demo demonstrated attestation data from a trusted execution environment using Azure Container Instances and Kata Containers.                                  |
|  22 | Resources for further learning include the CNCF Cloud Native AI Working Group, the OWASP Top 10 for LLMs, and related conference sessions.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Y2XPq3BRyrI/hqdefault.jpg)](https://www.youtube.com/watch?v=Y2XPq3BRyrI)

[Watch on YouTube](https://www.youtube.com/watch?v=Y2XPq3BRyrI)
