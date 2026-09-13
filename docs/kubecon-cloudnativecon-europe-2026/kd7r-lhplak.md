---
type: Video Note
title: "Evolving Policy Management with Agentic AI: Kyverno MCP and Kagent for... Shuting Zhao & Dahu Kuang"
description: "The session introduces an evolved solution for managing Kubernetes clusters, moving beyond simple connectivity to intelligent orchestration using tools like Kyverno, Civero, and Open Cloud. The speakers highlight the daily challenges faced..."
resource: https://www.youtube.com/watch?v=kd7R-LhPLak
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session introduces an evolved solution for managing Kubernetes clusters, moving beyond simple connectivity to intelligent orchestration using tools like Kyverno, Civero, and Open Cloud.
The speakers highlight the daily challenges faced by platform engineers, such as managing policies across numerous clusters, verification gaps in policy enforcement, and knowledge silos.
Their approach leverages Kyverno as a policy engine, Open Cloud as an AI-driven orchestration layer that translates natural language into Kubernetes actions, and a shared "skill pool" to centralize expertise.
Through a live demo, they show how Open Cloud integrates with chat applications like Slack to automate policy deployment, compliance checks, and reporting across multiple clusters, reducing manual effort and errors.
The presenters emphasize the importance of strong security practices when using AI agents, such as isolation, identity management, and human oversight, and conclude with updates on Kyverno’s roadmap and an invitation to contribute to the open-source community.
# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session evolved from cluster connection to intelligent orchestration, now called Open Cloud                                                                                              |
|   2 | Focus on managing policies across hundreds of clusters efficiently                                                                                                                       |
|   3 | Speakers: Shooting (Caverno co-author, Namada) and Dahu Kuang (Alibaba Cloud)                                                                                                            |
|   4 | Challenges for platform engineers: managing multiple clusters, manual work, verification gaps, knowledge silos                                                                           |
|   5 | Need for automation and intelligent assistants to simplify cluster management and policy verification                                                                                    |
|   6 | Verification gap: difficulty ensuring policies are enforced and functioning as expected across many clusters                                                                             |
|   7 | Knowledge silos: expertise often trapped with senior engineers, need for shared, accessible knowledge                                                                                    |
|   8 | Solution architecture uses three core components: Caverno (policy engine), Open Cloud (AI orchestration), Shared Brain/App Store (skills repository)                                     |
|   9 | Caverno: CNCF standard, runs as admission controller, validates resources, supports reporting, exemptions, and runs anywhere                                                             |
|  10 | New cell-based policy types using Common Expression Language, applicable to Kubernetes clusters and JSON payloads                                                                        |
|  11 | Open Cloud: AI-native orchestration layer, translates natural language to Kubernetes actions, manages clusters, integrates with chat apps (e.g., Slack)                                  |
|  12 | Shared Brain/App Store: repository of reusable skills for policy governance, accessible to all users                                                                                     |
|  13 | Demo setup: two Kubernetes clusters, Open Cloud gateway, Slack chatbot integration                                                                                                       |
|  14 | Three ways to manage policies: manual (not scalable), Commada (enterprise, stable), AI agent (Open Cloud, intelligent, fast, needs security)                                             |
|  15 | Open Cloud automates policy installation, status checks, skill deployment, and reporting across clusters                                                                                 |
|  16 | Demonstrated deploying policies, scanning for violations, generating reports, and enforcing mutating policies via Open Cloud                                                             |
|  17 | Security risks with AI agents: identity confusion, supply chain attacks, prompt injection; best practices include isolation, network lockdown, sandboxing, human oversight, and auditing |
|  18 | Kivero roadmap: SDK rel                                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kd7R-LhPLak)