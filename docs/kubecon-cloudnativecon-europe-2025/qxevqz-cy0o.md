---
layout: default
title:
  "Securing AI Workloads: Building Zero-Trust Architecture for LLM Appl... Rohit
  Ghumare & Joinal Ahmed"
nav_order: 299
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker discusses securing AI workloads, specifically LLM applications,
  and building a zero-trust architecture. They highlight various security risks associated
  with model running and inference, including unauthorized access, data leaka...
resource: https://www.youtube.com/watch?v=qXEvqZ_cY0o
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses securing AI workloads, specifically LLM applications, and building a zero-trust architecture.
They highlight various security risks associated with model running and inference, including unauthorized access, data leakage, adversarial attacks, insider threats, supply chain vulnerabilities, and identity compromise.
To mitigate these risks, the speaker recommends implementing authentication, authorization, and identity verification; input validation and threat detection; securing deployment and isolation layers using Kubernetes service meshes and container sandboxing; and monitoring models for data confidentiality.
They also showcase their own project, MCP server for Cube, which allows remote control of local data sources with a web API.

# Main Points

|   # | Main point                                                                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | LLMs (Large Language Models) are becoming part of software supply chains, making them vulnerable to attacks.                                                                                                                                     |
|   2 | Security incidents:                                                                                                                                                                                                                              |
|   3 | Nvidia container toolkit vulnerability                                                                                                                                                                                                           |
|   4 | Omnipping's data sold on bridge forums                                                                                                                                                                                                           |
|   5 | Truffle Hog found 12,000 exposed deep-se API keys                                                                                                                                                                                                |
|   6 | Malicious actors uploaded fake DeepSe packages                                                                                                                                                                                                   |
|   7 | Deployment options for LLMs:                                                                                                                                                                                                                     |
|   8 | Serverless                                                                                                                                                                                                                                       |
|   9 | Hybrid cloud                                                                                                                                                                                                                                     |
|  10 | Local servers                                                                                                                                                                                                                                    |
|  11 | Cloud APIs (e.g., OpenAI, SageMaker)                                                                                                                                                                                                             |
|  12 | On-premise deployments (e.g., DJX server)                                                                                                                                                                                                        |
|  13 | Decentralized deployments (e.g., P2P peer-to-peer)                                                                                                                                                                                               |
|  14 | AI gateways:                                                                                                                                                                                                                                     |
|  15 | Manage access to LLMs                                                                                                                                                                                                                            |
|  16 | Protect against unauthorized access and data leakage                                                                                                                                                                                             |
|  17 | Implement security policies and enforcement                                                                                                                                                                                                      |
|  18 | Security risks associated with model running and inference:                                                                                                                                                                                      |
|  19 | Unauthorized access to model endpoints                                                                                                                                                                                                           |
|  20 | Data leakage via inference output                                                                                                                                                                                                                |
|  21 | Adversarial attacks on model integrity                                                                                                                                                                                                           |
|  22 | Insider threats                                                                                                                                                                                                                                  |
|  23 | Supply chain vulnerabilities                                                                                                                                                                                                                     |
|  24 | Top 10 security concerns for LLMs (OASP):                                                                                                                                                                                                        |
|  25 | Prompt injection                                                                                                                                                                                                                                 |
|  26 | Runtime security                                                                                                                                                                                                                                 |
|  27 | Model artifacts and supply chain vulnerabilities                                                                                                                                                                                                 |
|  28 | Authorization and identity verification                                                                                                                                                                                                          |
|  29 | Input validation and threat detection                                                                                                                                                                                                            |
|  30 | Data confidentiality and monitoring                                                                                                                                                                                                              |
|  31 | Zero-trust architecture for LLMs: + Access control and authentication + Input validation and threat detection + Runtime enforcement with OPA + Observability with tracing tools (e.g., LangChain, LangKit) + Data confidentiality and monitoring |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qXEvqZ_cY0o)
