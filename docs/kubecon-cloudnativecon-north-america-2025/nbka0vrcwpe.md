---
type: Video Note
title: "The Future of Debugging Is No Debugging: Observability Is Dead - Jeremy Adams, Neo4j"
description: "In this session, Jeremy Adams welcomes a largely first-time KubeCon audience and introduces key Kubernetes and AI terminology, explaining abbreviations like K8s (Kubernetes), I18N (internationalization), L10N (localization), and others. He..."
resource: https://www.youtube.com/watch?v=nBka0VrCWpE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Jeremy Adams welcomes a largely first-time KubeCon audience and introduces key Kubernetes and AI terminology, explaining abbreviations like K8s (Kubernetes), I18N (internationalization), L10N (localization), and others.
He discusses the evolving landscape of debugging and observability, highlighting the traditional reliance on logs, metrics, and traces, but notes that in AI and LLM-powered systems, traces and evaluations (evals) become increasingly important for understanding agentic reasoning and performance.
Adams emphasizes the need to adapt observability practices for AI applications, suggesting that while logs remain useful, tracing agent behavior and conducting systematic evals are crucial for diagnosing and improving AI-driven systems.
He also introduces the concept of "durable" versus "disposable" code, arguing that while AI can help rapidly generate or iterate on less critical code, foundational systems still require careful, reliable engineering.
The talk concludes by encouraging attendees to embrace new tools and strategies for observability in AI contexts, balancing innovation with the need for robust, maintainable infrastructure.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Majority of attendees are first-time CubeCon participants.                                                                                                                                                                                                       |
|   2 | Explained Kubernetes abbreviation (K8s: K + 8 letters + s) and similar numeronyms (I18N: Internationalization, L10N: Localization, A11Y: Accessibility, A16Z: Andreessen Horowitz, K3S: Lightweight Kubernetes, K9S: Kubernetes dashboard, O11Y: Observability). |
|   3 | Presenter: Jeremy Adams, Developer Advocate at Neo4j, a graph database company used in fraud detection, AI, recommendations, social networks, supply chains, medical research, and NASA projects.                                                                |
|   4 | Session agenda: debugging, observability paradox, toolbox for different code types, and the concept of rewriting vs. debugging.                                                                                                                                  |
|   5 | Debugging defined as locating, understanding, and resolving root causes of unexpected or incorrect behavior.                                                                                                                                                     |
|   6 | Observability tools: logs, metrics, and traces.                                                                                                                                                                                                                  |
|   7 | Logs are widely used but can be overwhelming; metrics are less uniformly used; traces are underused but valuable for distributed systems.                                                                                                                        |
|   8 | Observability paradox: more data (logs/metrics) isn’t always better; too much information can obscure issues.                                                                                                                                                    |
|   9 | For AI/LLM systems, traces become more important than logs; tracing helps follow reasoning paths and agent interactions.                                                                                                                                         |
|  10 | Metrics help measure LLM/agent performance; logs remain useful but less central.                                                                                                                                                                                 |
|  11 | Eval (evaluation) is crucial for LLMs/agents to measure effectiveness, as outputs are stochastic and not deterministic.                                                                                                                                          |
|  12 | Agentic loop: LLMs use tools, take actions, receive feedback, and may delegate to sub-agents.                                                                                                                                                                    |
|  13 | Evaluations (evals) help determine if LLMs/agents perform tasks successfully and guide improvements.                                                                                                                                                             |
|  14 | New toolbox includes agent frameworks, infrastructure tools (Kubernetes, Docker), and durable execution platforms.                                                                                                                                               |
|  15 | Not everyone needs full observability; roles determine which observability data is relevant.                                                                                                                                                                     |
|  16 | AI enables faster iteration and rewriting, but distinction exists between “durable code” (critical systems) and “disposable code” (easily rebuilt, e.g., websites).                                                                                              |
|  17 | AI can assist in understanding and                                                                                                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nBka0VrCWpE)