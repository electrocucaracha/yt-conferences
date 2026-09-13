---
layout: default
title:
  Automating and Scaling of Threat Modelling for Cloud Native Archit... Hanna
  Papirna & Emma Yuan Fang
nav_order: 23
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Emma and Hannah from EPAM Systems discuss the complexities of threat
  modeling in cloud-native environments, highlighting the challenges posed by numerous
  attack surfaces, dynamic trust boundaries, and distributed microservices. They critiqu...
resource: https://www.youtube.com/watch?v=GGdc0vihJOI
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

Emma and Hannah from EPAM Systems discuss the complexities of threat modeling in cloud-native environments, highlighting the challenges posed by numerous attack surfaces, dynamic trust boundaries, and distributed microservices.
They critique traditional frameworks like STRIDE for their limitations in modern, containerized architectures and propose a block decomposition approach, which breaks systems into manageable security domains to focus on high-risk areas, such as cross-tenant identity and API management.
The speakers demonstrate how to map threat actors to attack vectors, use the DREAD framework for risk evaluation, and emphasize the importance of automating threat modeling through "threat modeling as code" integrated into CI/CD pipelines.
They also showcase an AI-assisted tool, STRIDE GPT, illustrating how block-focused prompting yields more actionable threat models than generic approaches, while noting that some human judgment remains essential.
The session concludes by encouraging further discussion on advancing cloud-native threat modeling practices.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Cloud-native environments have many attack surfaces, making manual threat modeling challenging.                                                                                       |
|   2 | Emma and Hannah from EPAM Systems present solutions for automating and scaling threat modeling.                                                                                       |
|   3 | Key challenges include shared responsibility models, distributed systems, numerous APIs, short-lived workloads, and difficulty identifying all attack surfaces.                       |
|   4 | Proposal: Use AI-assisted approaches and integrate threat modeling into CI/CD pipelines.                                                                                              |
|   5 | Typical threat modeling process: define architecture, trust boundaries, data classification, break down into subsystems, identify threats and actors, evaluate risk, plan mitigation. |
|   6 | DREAD methodology is used for risk evaluation.                                                                                                                                        |
|   7 | Threat modeling as code: codify architecture and data flows in declarative formats (e.g., YAML, Terraform), version control, automate analysis in CI/CD.                              |
|   8 | Existing frameworks like STRIDE are widely used but have gaps in dynamic, cloud-native environments.                                                                                  |
|   9 | Block decomposition approach: break system into manageable security domains, focus on high-risk threats per block.                                                                    |
|  10 | Example architecture: Kubernetes-based cross-tenant identity governance platform with centralized user lifecycle management.                                                          |
|  11 | Four main threat actor types: external attackers, insiders, supply chain actors, bots/scanners.                                                                                       |
|  12 | Threat actor mapping uses STRIDE and MITRE ATT&CK frameworks.                                                                                                                         |
|  13 | Common threat patterns: spoofing at gateways, privilege escalation at service-to-service plane, credential threats at management plane, data disclosure/tampering at data plane.      |
|  14 | DREAD factors used to score and prioritize risks.                                                                                                                                     |
|  15 | Example: GitOps repository compromise scored as high risk, with proposed mitigations.                                                                                                 |
|  16 | Automation: threat modeling as code enables detection of architectural drift, automated scans, and integration with ticketing systems.                                                |
|  17 | Some manual judgment is always required in threat modeling.                                                                                                                           |
|  18 | AI-assisted threat modeling demo using STRIDE GPT: generic prompts yield broad risks, block-focused prompts yield more actionable, specific                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GGdc0vihJOI)
