---
type: Video Note
title: "The Accidental Platform Team: Kubernetes Operators at Swisscom - Fabian Schulz & Jelena Malic"
description: "In this talk, the Swisscom team describes their journey from building Kubernetes operators to becoming an accidental platform team tasked with modernizing the automation of their 5G mobile data core. Initially, deploying new network functio..."
resource: https://www.youtube.com/watch?v=OgE9X1uBfGo
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, the Swisscom team describes their journey from building Kubernetes operators to becoming an accidental platform team tasked with modernizing the automation of their 5G mobile data core.
Initially, deploying new network functions was a complex, manual process requiring extensive cross-domain knowledge and coordination, often involving Excel sheets, multiple interfaces, and days of work.
By introducing Kubernetes operators to automate tasks such as IP management and router configuration, they shifted the complexity into software, enabling network engineers to define high-level intents in YAML, which the platform then translates into actionable configurations.
The team adopted a gradual rollout, focusing on early adopters, providing user-friendly interfaces, investing in observability and traceability, and fostering a supportive community to address user concerns and ease the transition.
As a result, they reduced deployment times from days or weeks to hours, improved reliability, and empowered engineers to focus on higher-value tasks, while acknowledging ongoing challenges such as balancing automation with necessary manual steps and exploring future integration of AI.
# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Swisscom team transitioned from building Kubernetes operators to becoming a platform team for 5G mobile data core automation.                                                  |
|   2 | The 5G core runs fully on Kubernetes, with ~2,000 pods per dev environment across 32 servers and 3-4 Swiss data centers.                                                       |
|   3 | Previously, 5G network engineers manually created networks using Excel, Netbox, Ansible, and various UIs, requiring extensive cross-domain knowledge and taking days to weeks. |
|   4 | Manual process involved IP assignments, inventory population, router/switch configuration, and integration testing.                                                            |
|   5 | The team introduced Kubernetes operators to automate network creation, moving cross-domain knowledge into the operators.                                                       |
|   6 | Engineers now define high-level network intent in YAML, which operators translate into lower-level intents and configurations.                                                 |
|   7 | Automation reduced manual steps, enabled drift detection, and improved adaptability.                                                                                           |
|   8 | Gradual adoption approach: started with automating routers and IP management, involved early adopters, iterated based on feedback.                                             |
|   9 | Provided multiple UIs (CRD wizard, Headlamp, custom map view) to ease transition for users accustomed to graphical interfaces.                                                 |
|  10 | Invested in observability and traceability: metrics dashboards, Git-based intent storage for audit/compliance, and easier troubleshooting.                                     |
|  11 | Established direct communication channels and a user community for support and feedback.                                                                                       |
|  12 | Created Kubernetes workshops and team-rotation initiatives to upskill network engineers and spread platform knowledge.                                                         |
|  13 | Automation reduced network deployment from days/weeks to hours, with continuous testing and observability.                                                                     |
|  14 | Main benefits: time savings, error reduction, increased trust and stability, freeing engineers to focus on higher-value tasks.                                                 |
|  15 | Recognized that full automation may not be possible; partial automation already yields significant gains.                                                                      |
|  16 | Ongoing exploration of integrating imperative systems and AI, while maintaining user trust and system determinism.                                                             |
|  17 | Success attributed to empowering us                                                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OgE9X1uBfGo)