---
type: Video Note
title: "Datadog Built 100 AI Agents. Here's What Broke."
description: "The speaker discusses their experience building AI agents at Data Dog, highlighting the development of the first hundred agents and strategies for scaling to thousands. They describe three main focus areas: AI agents for Data Dog, Data Dog..."
resource: https://www.youtube.com/watch?v=Naty_iFtITM
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses their experience building AI agents at Data Dog, highlighting the development of the first hundred agents and strategies for scaling to thousands.
They describe three main focus areas: AI agents for Data Dog, Data Dog for AI, and AI agent infrastructure, and detail current production agents such as Bits AI SR for autonomous alert investigation, Bits AAI dev for code generation and error resolution, and a security analyst agent for automating security investigations.
Key lessons include designing agent-friendly interfaces, prioritizing proactive and autonomous agents over reactive ones, ensuring robust evaluation and monitoring systems, and maintaining model and framework agnosticism to adapt to rapid advancements.
The speaker emphasizes the importance of treating agents as users, automating tasks traditionally done by humans, and preparing for a future where agents are increasingly independent, multimodal, and capable of learning on the job.
They conclude by encouraging ongoing experimentation and adaptation as the field evolves.
# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussed building the first 100+ agents at Data Dog and preparing for scaling to 1,000+                                                      |
|   2 | Data Dog focuses on automating DevSecOps tasks using AI agents                                                                                |
|   3 | Three focus areas: AI agents for Data Dog, Data Dog for AI and AI agents, AI agent infrastructure                                             |
|   4 | Current production agents:                                                                                                                    |
|   5 | Bits AI SR: autonomously investigates alerts to reduce human intervention                                                                     |
|   6 | Bits AAI dev: code generation product proposing code fixes for errors and latency issues                                                      |
|   7 | Security analysts: automates security investigations and checklists                                                                           |
|   8 | AI models are improving rapidly: faster, better, larger context windows, longer runtimes                                                      |
|   9 | Automation potential is increasing; intelligence is no longer the bottleneck                                                                  |
|  10 | Building agents that operate autonomously is crucial; need for monitoring agents                                                              |
|  11 | Key learnings:                                                                                                                                |
|  12 | Code and agent first: design interfaces to be agent-friendly, not just human-friendly                                                         |
|  13 | Proactive over reactive: agents should run in the background, be event-driven, and durable                                                    |
|  14 | Use container sandboxes and appropriate storage for agent safety and flexibility                                                              |
|  15 | Evaluation (eval) is essential: offline, online, and continuous eval systems required                                                         |
|  16 | Make eval and improvement tools automatable and accessible to agents                                                                          |
|  17 | Keep agent harnesses simple; expect to rewrite as models change                                                                               |
|  18 | Stay model and framework agnostic; use good memory systems for portability                                                                    |
|  19 | Multiplayer now means human-human, human-agent, and agent-agent collaboration; ensure proper communication channels                           |
|  20 | New product: dispatch agents.ai encodes these learnings                                                                                       |
|  21 | Looking ahead: agents will learn on the job, become more independent, run longer, and support multimodal capabilities (e.g., computer vision) |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Naty_iFtITM)