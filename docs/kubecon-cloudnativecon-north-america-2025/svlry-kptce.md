---
layout: default
title:
  "Your Kubernetes Playbook at Your Fingertips: Advanced Troubleshooti... David
  vonThenen & Yash Sharma"
nav_order: 345
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speakers introduced a session focused on integrating AI with Kubernetes
  troubleshooting using a project called KGPT, which leverages large language models
  (LLMs) and retrieval-augmented generation (RAG) to analyze and remediate issues
  i...
resource: https://www.youtube.com/watch?v=SVLrY-KpTcE
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

The speakers introduced a session focused on integrating AI with Kubernetes troubleshooting using a project called KGPT, which leverages large language models (LLMs) and retrieval-augmented generation (RAG) to analyze and remediate issues in Kubernetes clusters.
They demonstrated how to embed organizational runbooks—such as the NSA’s Kubernetes hardening guide—into the AI workflow, allowing the system to provide context-aware troubleshooting and best practice recommendations tailored to specific security policies and operational procedures.
The live demo showed how vector embeddings of documentation enable natural language queries about cluster status and compliance, with the AI agent referencing relevant runbook sections to generate responses.
The presenters discussed security considerations, emphasizing the option to use local LLMs for sensitive environments and the importance of organizational guardrails.
During the Q&A, they addressed extending the approach to broader documentation, differences between RAG and direct context injection, and the necessity of human oversight when automating remediations.

# Main Points

|   # | Main point                                                                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on having a Kubernetes playbook at your fingertips using AI tools.                                                                                                                                                                  |
|   2 | Yash (Digital Ocean, CNCF contributor) and David (NetApp, AI/ML, NLP, Kubernetes background) are the presenters.                                                                                                                                     |
|   3 | The main project discussed is KGPT, which uses AI to troubleshoot and analyze Kubernetes clusters.                                                                                                                                                   |
|   4 | KGPT can use various models (local or cloud, e.g., OpenAI, Amazon Bedrock) and integrates with backend APIs.                                                                                                                                         |
|   5 | Core use case: simplifying Kubernetes troubleshooting and providing actionable suggestions.                                                                                                                                                          |
|   6 | KGPT can be integrated into GitHub workflows for deployment analysis and suggestions.                                                                                                                                                                |
|   7 | The talk demonstrates combining KGPT with RAG (Retrieval-Augmented Generation) and MCP (natural language interface) to create a proof of concept.                                                                                                    |
|   8 | Runbooks (step-by-step guides for troubleshooting/operations) can be embedded into the AI workflow for organization-specific best practices.                                                                                                         |
|   9 | The demo uses a real NSA Kubernetes hardening guide, chunked into vector embeddings for querying.                                                                                                                                                    |
|  10 | The process: ingest the runbook, generate embeddings, start MCP server, connect LLM (Claude), and run a RAG agent.                                                                                                                                   |
|  11 | The system allows querying the cluster in natural language, referencing the runbook for compliance checks (e.g., privilege escalation settings).                                                                                                     |
|  12 | The demo shows successful analysis and compliance reporting using the setup.                                                                                                                                                                         |
|  13 | Security concerns: for sensitive environments, use local LLMs instead of cloud; KGPT supports this.                                                                                                                                                  |
|  14 | Guardrails are a first line of defense, but organizations should follow their own AI security best practices.                                                                                                                                        |
|  15 | The open-source repository and demo code are available for attendees to try.                                                                                                                                                                         |
|  16 | Q&A covers: combining MCP, KGPT, and RAG for self-service portals; differences between RAG and direct Markdown reference; LLM performance/latency; human-in-the-loop for remediation; and rationale for using embeddings over large context windows. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SVLrY-KpTcE)
