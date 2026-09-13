---
layout: default
title:
  Deploying Lightweight AI Agents at the Healthcare Edge With K8s + Ollama -
  Gary Arora & Samarth Shah
nav_order: 58
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Gary Aurora and Samarth Sha, architects specializing in cloud and AI
  solutions for healthcare, discuss the longstanding challenges in healthcare claims
  processing, emphasizing its complexity, high volume, and reliance on outdated, fragmente...
resource: https://www.youtube.com/watch?v=IdAvZKQots0
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

Gary Aurora and Samarth Sha, architects specializing in cloud and AI solutions for healthcare, discuss the longstanding challenges in healthcare claims processing, emphasizing its complexity, high volume, and reliance on outdated, fragmented technology.
They explain that current AI solutions often fail due to the sector’s unique domain requirements, legacy systems, privacy concerns, and the need for continuous learning and adaptation.
Their proposed solution leverages distributed intelligence by deploying local language models and Kubernetes clusters at provider locations, enabling claims adjudication and audit to occur close to the data, thus reducing costs, improving accuracy, and maintaining data privacy.
The system allows clusters to share learnings as vector differences without exposing sensitive information, resulting in faster, more comprehensive audits and payments.
While demonstrated in healthcare, they note this architecture’s applicability to other industries facing similar data privacy and cost challenges, highlighting a trend toward hybrid AI deployments that balance local and cloud resources.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Gary Aurora and Samarth Sha focus on cloud and AI solutions for the healthcare sector.                                                          |
|   2 | The healthcare sector processes around three billion commercial claims annually, leading to significant administrative costs and manual rework. |
|   3 | Claims processing is complex, error-prone, and relies on outdated legacy systems, often using mainframes and COBOL.                             |
|   4 | AI has potential but often fails due to legacy tech, lack of domain-specific models, static models, high costs, and privacy concerns.           |
|   5 | Healthcare data includes unstructured information, handwritten notes, and is subject to strict privacy regulations (PHI).                       |
|   6 | Current AI pilots often fail because they do not adapt to legacy systems or continuously learn from new data.                                   |
|   7 | The proposed solution moves intelligence closer to the data, using edge computing and local LLMs (e.g., Olama) on Kubernetes clusters.          |
|   8 | Local models can now achieve 80-95% of the accuracy of frontier models, with much lower inference costs and no cloud dependency.                |
|   9 | The system uses distributed intelligence: multiple Kubernetes clusters at provider locations process and audit claims locally.                  |
|  10 | Each cluster runs its own pricing, benefit, and audit engines, processing claims rapidly and reducing costs (e.g., $9,600 saved on 20 claims).  |
|  11 | The solution audits 100% of claims, not just samples, increasing accuracy and reducing appeals and delays.                                      |
|  12 | Clusters share learnings as vector differences (not raw data), maintaining privacy and enabling self-learning across the network.               |
|  13 | Payment lock tokens are generated and cryptographically signed, providing traceability and signaling payers to process payments.                |
|  14 | The architecture keeps data at the source, reducing compliance risks and expensive data pipelines.                                              |
|  15 | The approach combines LLMs and rule-based engines for intelligent, adaptive workflows.                                                          |
|  16 | The solution is applicable beyond healthcare, including finance, government, and logistics.                                                     |
|  17 | The trend is toward hybrid architectures, balancing local and cloud AI for                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=IdAvZKQots0)
