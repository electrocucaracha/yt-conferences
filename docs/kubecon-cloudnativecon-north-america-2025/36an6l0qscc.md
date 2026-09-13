---
layout: default
title:
  "Unlocking Financial Progress: Credit Karma's AI Assista... Raj Kiran Gupta
  Katakam & Sukanya Moorthy"
nav_order: 333
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speakers, staff machine learning engineers at Credit Karma (part
  of Intuit), discuss the development and deployment of Credit Karma’s financial assistant,
  specifically the “CY solution,” which leverages large language models (LLMs) and...
resource: https://www.youtube.com/watch?v=36aN6L0qSCc
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

The speakers, staff machine learning engineers at Credit Karma (part of Intuit), discuss the development and deployment of Credit Karma’s financial assistant, specifically the “CY solution,” which leverages large language models (LLMs) and Kubernetes to provide personalized financial recommendations and explanations to over 140 million members.
They emphasize the importance of robust guardrails—both before and after LLM calls—to ensure safety, privacy, compliance, and brand protection, using model- and framework-agnostic approaches.
Initially, they adopted a sidecar pattern for rapid MVP deployment, but as scaling challenges emerged (such as overprovisioning and debugging difficulties), they transitioned to Kubernetes-based model serving, enabling independent scaling, cost reduction, and faster iteration.
This evolution allowed them to remain cloud-agnostic and efficiently onboard new models and guardrails, ultimately supporting a complex, multi-cloud ML infrastructure.
Key lessons include starting simple and evolving with scale, ruthlessly separating business logic from model inference, and recognizing that generative AI introduces unique orchestration and compliance challenges compared to traditional ML systems.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Credit Karma’s financial assistant is powered by Kubernetes and LLMs, serving over 140 million members.                                                                                                                                                                                          |
|   2 | The CY solution provides personalized explanations for financial product recommendations, helping members make informed decisions.                                                                                                                                                               |
|   3 | Core principles: leverage member data, ensure reliability, prioritize security and privacy.                                                                                                                                                                                                      |
|   4 | The solution analyzes members’ financial data to explain recommendations, such as why a specific credit card is suggested.                                                                                                                                                                       |
|   5 | Guardrails are implemented before and after LLM calls to address safety, privacy, compliance, brand protection, and user experience.                                                                                                                                                             |
|   6 | Input guardrails detect and filter toxicity, profanity, and anger before sending requests to LLMs.                                                                                                                                                                                               |
|   7 | Output guardrails ensure responses are free from hallucinations, unwanted links, and negative sentiment.                                                                                                                                                                                         |
|   8 | Guardrails are model-agnostic and framework-agnostic, built using diverse frameworks (TensorFlow, Torch, Jax).                                                                                                                                                                                   |
|   9 | ML lifecycle uses Kubernetes and Kubeflow for data collection, preprocessing, model training, evaluation, export, and serving.                                                                                                                                                                   |
|  10 | Model serving evolved from sidecar pattern (business logic in main pod, model serving in sidecars) to Kubernetes-based model services.                                                                                                                                                           |
|  11 | Sidecar pattern enabled rapid MVP launch but led to overprovisioning, costly scaling, velocity constraints, and debugging challenges.                                                                                                                                                            |
|  12 | Transition to Kubernetes-based model services allowed independent scaling, reduced costs, faster iteration, and clearer separation of business logic and model serving.                                                                                                                          |
|  13 | The platform is now model, framework, and cloud agnostic, supporting rapid onboarding and deployment.                                                                                                                                                                                            |
|  14 | CY solution is powered by Intuit’s internal generative AI operating system and safety framework.                                                                                                                                                                                                 |
|  15 | Key lessons: Kubernetes acts as a universal ML platform; start simple and evolve with scale; separate business logic from model inference; generative AI requires orchestration of multiple guardrails per request; compliance and audit needs are higher for generative AI than traditional ML. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=36aN6L0qSCc)
