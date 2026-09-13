---
layout: default
title:
  "From Chaos to Control: A Prescription for Managing Apps on Private Cellular
  Networks - Luis Ariza"
nav_order: 115
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Luis Arisa discusses the evolution of deploying private cellular networks,
  highlighting how the process has shifted from complex, on-premise, and repetitive
  tasks to a much simpler approach enabled by new technologies. He introduces a solut...
resource: https://www.youtube.com/watch?v=lceZtXmIGio
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

Luis Arisa discusses the evolution of deploying private cellular networks, highlighting how the process has shifted from complex, on-premise, and repetitive tasks to a much simpler approach enabled by new technologies.
He introduces a solution that leverages Kubernetes, cloud-native tools, artificial intelligence, and custom resource definitions (CRDs) to allow users—even those without technical expertise—to deploy 4G or 5G private networks using natural language commands or simple YAML files.
The system integrates open-source software, AI-powered 3GPP expertise, and automation to streamline network deployment, monitoring, and self-healing, reducing the need for specialized knowledge and minimizing costs and complexity.
Through live demos, Luis demonstrates that anyone, regardless of age or background, can set up a private cellular network with minimal hardware requirements and a single command, emphasizing the democratization and accessibility of advanced telecom infrastructure.
He concludes by answering questions about hardware needs and clarifying aspects of network connectivity, reinforcing the practicality and scalability of his approach.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Traditional telecom network deployment was complex, repetitive, and required on-premise setup.                                                |
|   2 | New technologies now enable easier deployment of 3GPP-standardized networks.                                                                  |
|   3 | Goal: Simplify private cellular network deployment, making it accessible via natural language.                                                |
|   4 | Luis Arisa from Vtor, with experience in telco, AI, cloud native, and open infra communities, presents the solution.                          |
|   5 | First 5G private solution network built-in 2019 using Kubernetes.                                                                             |
|   6 | Industry challenges: excessive documentation, high memory requirements, costly infrastructure, vendor lock-in, and need for multiple experts. |
|   7 | Diagnosis: Telecom industry is overengineered, over-budget, and inefficient.                                                                  |
|   8 | Prescription: Use cellular CRDs and a single YAML file to deploy private cellular networks.                                                   |
|   9 | Developed a 3GPP telco expert to interpret specifications and assist developers.                                                              |
|  10 | Utilizes open-source software, GitHub, Flux, AI, and MCP to automate deployment.                                                              |
|  11 | CRD maps to any CNCF tool; aims for universal 3GPP cell network blueprint.                                                                    |
|  12 | Deployment process: design/provision (Day 0), deploy/activate (Day 1), observe/optimize (Day 2), self-heal/evolve (ongoing).                  |
|  13 | Supports multiple open-source solutions: OpenAirInterface, Open5GS, Free5GC, etc.                                                             |
|  14 | Solution integrates cloud native, AI, and telco for Kubernetes-based deployments.                                                             |
|  15 | Features self-healing, reduced memory and cost, and EUR compliance.                                                                           |
|  16 | CLI and MCP connect with AI for command execution and real-time deployment visualization.                                                     |
|  17 | Supports multiple AI models (Neotron, Mistral, YAMA); AI assists but does not control.                                                        |
|  18 | Demonstrated full lifecycle deployment, monitoring, and remediation using open-source tools.                                                  |
|  19 | CLI enables network slicing and configuration via natural language.                                                                           |
|  20 | Anyone, regardless of expertise, can deploy a private cellular network using the solution.                                                    |
|  21 | Hardware requirements: minimum 8GB RAM, 8 vCPUs for basic deployment; 16GB RAM and GPU for advanced features.                                 |
|  22 | Solution tested with real mobile phones and supports easy recon                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lceZtXmIGio)
