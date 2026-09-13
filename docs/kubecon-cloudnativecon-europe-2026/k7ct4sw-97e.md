---
layout: default
title:
  "Choose Your Own Adventure: AI Meets Internal Developer Platform - Whitney
  Lee & Viktor Farcic"
nav_order: 39
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video discusses the evolution from traditional developer tooling
  to AI-powered agents, particularly in the context of platform engineering and Kubernetes.
  The presenters explain how agents work by combining user intent, system context...
resource: https://www.youtube.com/watch?v=k7ct4sW-97E
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

The video discusses the evolution from traditional developer tooling to AI-powered agents, particularly in the context of platform engineering and Kubernetes.
The presenters explain how agents work by combining user intent, system context, and tools, with large language models (LLMs) orchestrating actions through iterative tool calls.
They demonstrate building an agent using the Langraph framework, equipping it with Kubernetes tools, and later enhancing it with semantic search via a vector database (Chroma) to improve information retrieval.
Security and guardrails are emphasized, with permissions and access controls enforced both at the agent and cluster levels.
Observability is addressed through tracing with OpenTelemetry, and the importance of cost management is noted.
The session concludes with a Q&A covering topics like implementing guardrails, choosing between vector databases and context, and evaluating tool call quality.

# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Agents are becoming essential in platform engineering, evolving from previous tools like Backstage.                       |
|   2 | Agents accept user input (intent), combine it with system context (instructions, capabilities), and send it to an LLM.    |
|   3 | LLMs use tools provided by the agent, executing them in a loop until a response is generated.                             |
|   4 | Tools can be LLM-invoked or deterministic (e.g., fetching context, rate limiting, logging, validations).                  |
|   5 | LLMs lack company-specific knowledge, rules, policies, and runbooks; this must be provided.                               |
|   6 | Four pillars for agents: system context, tools, knowledge (semantic search), and observability.                           |
|   7 | System context includes company policies, team conventions, and user preferences; it's generic and limited.               |
|   8 | Tooling is controlled by the agent; some tools are only for deterministic tasks, not LLM-invoked.                         |
|   9 | Demo: Developers use an agent with cluster access to troubleshoot Kubernetes apps without direct cluster access.          |
|  10 | Tools given to the agent: kubectl get, describe, logs.                                                                    |
|  11 | Agent uses tools to diagnose issues, but may not always provide correct solutions without more context.                   |
|  12 | Semantic search enables agents to quickly find relevant information from various sources (docs, repos, cluster data).     |
|  13 | Semantic search uses embeddings stored in a vector database (e.g., Chroma or Qdrant).                                     |
|  14 | Controller syncs Kubernetes resources into the vector database for agent access.                                          |
|  15 | Security is enforced via guardrails: permissions, access control, agent identity, and tool restrictions.                  |
|  16 | Guardrails should be deterministic and can be enforced at tooling and cluster (e.g., RBAC, Kyverno) levels.               |
|  17 | Observability is achieved by capturing logs, metrics, and especially traces (using OpenTelemetry with GenAI conventions). |
|  18 | Traces help understand agent behavior post-execution.                                                                     |
|  19 | Cost is a consideration; agents and supporting infrastructure can be expensive.                                           |
|  20 | Quality of tool/skill calls is hard to measure; user feedback and eval frameworks can help, but input/output is variable. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=k7ct4sW-97E)
