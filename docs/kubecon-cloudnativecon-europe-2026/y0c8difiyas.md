---
type: Video Note
title: "AI Agents & Platform Engineering: Efficiency Boost... Hasith K, Vincent C, Sara Q, Idit L & Carlos S"
description: "The panel at CubeCon discussed the current state and challenges of integrating AI agents into platform engineering, focusing on whether these technologies boost efficiency or introduce new complexities. Panelists from AWS, Red Hat, NTT Data..."
resource: https://www.youtube.com/watch?v=Y0C8dIfIYAs
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The panel at CubeCon discussed the current state and challenges of integrating AI agents into platform engineering, focusing on whether these technologies boost efficiency or introduce new complexities.
Panelists from AWS, Red Hat, NTT Data, Solo, and Cisco shared that, while there is significant interest and early adoption—especially for read-only tasks like log summarization and observability—fully autonomous, end-to-end AI agents are not yet widely trusted or deployed in production.
Key challenges identified include integrating agentic workflows with existing systems, ensuring security and trust (especially around permissions and identity), managing nondeterminism in AI behavior, and preventing fragmented, shadow IT solutions.
The panel emphasized the importance of strong evaluation frameworks, sandboxing, and starting with clear use cases and data before adopting new technologies.
They recommended leveraging open-source projects, establishing robust guardrails, and gradually expanding AI’s role as trust and understanding grow within organizations.
# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Panel discusses AI agents and platform engineering: efficiency boost or new source of trouble.                                            |
|   2 | Participants: Carlos Santana (AWS), Vincent (Red Hat), Sara (NTT Data), Lavin (Solo), Hasset (Cisco).                                     |
|   3 | AI agents in production are mostly used for read-only tasks (log summarization, querying observability data), not full automation.        |
|   4 | Agentic SDLC (software development lifecycle) is an emerging use case, with challenges in integration and quality standards.              |
|   5 | Telemetry data is being fed into AI ops for proactive automation.                                                                         |
|   6 | Human-in-the-loop remains essential; AI assists rather than replaces humans.                                                              |
|   7 | Debugging and observability are primary AI agent use cases in production.                                                                 |
|   8 | Some organizations plan to run all agents on Kubernetes.                                                                                  |
|   9 | Internal operations and incident management are common AI agent applications at AWS and other companies.                                  |
|  10 | Security and identity management are major challenges, especially with shadow IT and multiple identity providers.                         |
|  11 | Skills for writing effective agents and managing agent orchestration are emerging needs.                                                  |
|  12 | Non-determinism of AI agents challenges reliability and trust; evaluation and statistical reliability are key.                            |
|  13 | Regulated industries (finance, utilities) are cautious, focusing on evaluation and statistical performance over deterministic guarantees. |
|  14 | Sandboxing and limiting agent permissions (RBAC) are critical for safe deployment.                                                        |
|  15 | AI gateways and registries are important architectural components.                                                                        |
|  16 | Community-driven open source projects (e.g., KAgent, Agent Gateway, Registry, Cape) are recommended starting points.                      |
|  17 | Start with use case and data, not technology; define value and integrate data flows.                                                      |
|  18 | Safety of AI and system safety are distinct; both need to be addressed.                                                                   |
|  19 | Observability, cost efficiency, and continuous evaluation are ongoing concerns.                                                           |
|  20 | Advice: treat AI as untrusted automation, apply guardrails, build trust gradually, and leverage community resources.                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Y0C8dIfIYAs)