---
layout: default
title:
  "Sponsored Keynote: From Pilot to Production: Scaling and Optimizing Agen...
  Idit Levine & Keith Babo"
nav_order: 342
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker discusses the challenges AI developers face in moving from
  pilot projects to production, particularly the lack of agent representation in Kubernetes.
  To address this, Solo developed the K agent project, which treats agents, skil...
resource: https://www.youtube.com/watch?v=45rqVBAlHyQ
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

The speaker discusses the challenges AI developers face in moving from pilot projects to production, particularly the lack of agent representation in Kubernetes.
To address this, Solo developed the K agent project, which treats agents, skills, and tools as first-class entities and supports integration with frameworks like LangChain and CrewAI.
The Agent Gateway provides essential features such as memory management, session optimization, and security, while being efficient and supported by an open-source community under the Linux Foundation.
To improve visibility and management, the Agent Registry offers a unified catalog for all agentic artifacts, supports federation, curation, and integration with multiple runtimes, and helps detect environment drift.
The speaker highlights the growing momentum in these open-source communities and announces the donation of Agent Registry to the CNCF to further address industry gaps.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Rapid AI innovation has increased developer demand to run AI solutions everywhere.                                                                  |
|   2 | Creating and deploying AI solutions anywhere is suitable for pilots and POCs, but not for production.                                               |
|   3 | Solo aims to address the production gap in AI deployment.                                                                                           |
|   4 | Kubernetes lacks direct representation of agents compared to other agentic runtimes.                                                                |
|   5 | The K agent project was created to treat agents, skills, and tools as first-class entities in Kubernetes.                                           |
|   6 | K agent acts as a general-purpose agent harness with declarative agents and supports frameworks like LangChain, ADK, and CrewAI.                    |
|   7 | Agent Gateway provides features for Kubernetes agent deployment, including memory management, session optimization, and human-in-the-loop controls. |
|   8 | Agent Gateway reduces the operational burden for platform teams hosting production-grade agentic infrastructure.                                    |
|   9 | A good gateway must support current and future features, be efficient at scale, and minimize infrastructure resource usage.                         |
|  10 | Agent Gateway's efficiency can be benchmarked publicly in user infrastructure.                                                                      |
|  11 | Agent Gateway is an open-source project under the Linux Foundation with active community contributions.                                             |
|  12 | Real-life users are running Agent Gateway at scale.                                                                                                 |
|  13 | Visibility into deployed agentic platforms is a major industry challenge.                                                                           |
|  14 | Agent Registry provides a single catalog for agents, tools, skills, prompts, and evaluators across environments.                                    |
|  15 | Agent Registry supports imports, federation, curation workflows, and semantic search.                                                               |
|  16 | Agent Registry can integrate with multiple runtimes, including K agent, Vertex, Agent Core, AI Foundry, and Nvidia Nemo Cloud.                      |
|  17 | Agent Registry enables continuous discovery and drift detection to address shadow IT.                                                               |
|  18 | Centralized deployment and aggregation of metrics and tracing are supported via OpenTelemetry.                                                      |
|  19 | Integration with Agent Gateway allows unified security and access policy enforcement.                                                               |
|  20 | K agent is part of CNCF; Agent Gateway is under the Linux Foundation.                                                                               |
|  21 | There has been significant community m                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=45rqVBAlHyQ)
