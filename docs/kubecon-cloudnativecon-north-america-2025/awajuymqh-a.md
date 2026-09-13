---
layout: default
title:
  In AI We Trust? Securing the Future, One Agent... Lin S, Yuval K, Hannah F,
  Andrew M & Ricardo A
nav_order: 101
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The panel at CubeCon, moderated by Lensa from solo.io, focused on the
  adoption and security challenges of AI agents in organizations. Panelists from various
  backgrounds discussed how companies are increasingly using existing AI agents like...
resource: https://www.youtube.com/watch?v=AWajuymQH-A
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

The panel at CubeCon, moderated by Lensa from solo.io, focused on the adoption and security challenges of AI agents in organizations.
Panelists from various backgrounds discussed how companies are increasingly using existing AI agents like Copilot and cloud code, often customizing them for specific tasks, and highlighted the growing trend of automating internal processes and enhancing customer service through AI.
They shared personal experiences with favorite AI agents, including custom-built tools for workflow automation and personal data analysis.
The discussion emphasized significant security concerns, such as unclear data provenance, identity management, and the risks posed by non-technical users granting excessive access to agents.
As organizations experiment with multi-agent orchestration across environments, the panelists noted the complexity of securing these dynamic systems, the need for new risk management approaches to address issues like prompt injection, and the importance of designing agents with minimal necessary privileges.
Audience engagement brought further questions about formalizing security standards and practical strategies for limiting agent access, with consensus that careful design and ongoing education are crucial as the field evolves.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Panel moderated by Lensa, head of open source at solo.io and author of "AI Agents in Kubernetes"                                                                |
|   2 | Panelists: Andy Martin (Control Plane), Hannah Foxwell (Mindu Guard), Ricardo Aravina (AI infra lead), Yuval Kohjavi (Solo.io)                                  |
|   3 | Organizations are adopting AI agents primarily for coding (e.g., Copilot, cloud code, Cursor, Warp), automating simple tasks, and improving internal efficiency |
|   4 | AI agents are used for both internal process optimization and customer-facing innovation                                                                        |
|   5 | Panelists' favorite agents include Copilot, Cursor, Warp, custom scoring agents, Claude Flow, and self-built personal data analysis agents                      |
|   6 | Security concerns include regulatory uncertainty, lack of clear frameworks, and insufficient threat modeling in AI agent deployment                             |
|   7 | Non-technical users experimenting with AI agents pose new security challenges due to lack of awareness and over-granting access                                 |
|   8 | Provenance and identity of agents and data are unclear, especially with multiple MCP servers and chained agents                                                 |
|   9 | Organizational chaos exists as teams independently deploy agents without standardized controls or accountability                                                |
|  10 | Key risks: agent identity management, access control, code execution, and potential for unintended destructive actions                                          |
|  11 | Multi-agent, multi-cloud orchestration increases complexity and risk; securing dynamic agent meshes is challenging                                              |
|  12 | Zero trust and workload identity approaches are being considered, but standards are still evolving                                                              |
|  13 | Prompt injection and hallucination are inherent LLM risks; current risk management and threat modeling may be insufficient                                      |
|  14 | Need for new, possibly AI-driven, risk management models to address scale and complexity of AI agent threats                                                    |
|  15 | Principle of least privilege, decomposing agent responsibilities, and intentional design are recommended for security                                           |
|  16 | Tools and cryptographic guarantees are needed to ensure agents do not exceed intended permissions                                                               |
|  17 | Audience engagement encouraged; open standards and governance frameworks highlighted as                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=AWajuymQH-A)
