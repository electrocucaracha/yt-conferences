---
layout: default
title: "Building Agents with Decision Models - Sydney Runkle, LangChain"
nav_order: 55
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Sydney Runckel, a product manager at LangChain, explains how decision models, such as Jev from Type-Safe AI, are transforming agent development by offering structured, fast, and cost-effective alte..."
resource: "https://www.youtube.com/watch?v=DilEiawSCjM"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Sydney Runckel, a product manager at LangChain, explains how decision models, such as Jev from Type-Safe AI, are transforming agent development by offering structured, fast, and cost-effective alternatives to Large Language Models (LLMs).
While LLMs are intelligent but slow and expensive, decision models provide predictable outputs for narrow, structured tasks, making them ideal for real-time processing and high-volume applications.
Runckel highlights six practical use cases, including model routing, progressive disclosure of tools, security guardrails, and automated grading, which allow developers to build "AI-powered software" where code controls the workflow and decision models handle specific judgments.
The presentation emphasizes that effective integration requires rigorous context engineering, breaking down complex problems into focused questions, and calibrating confidence thresholds to ensure reliability.
Ultimately, this approach enables a "cheap by default, frontier by exception" strategy, significantly reducing latency and costs while maintaining high performance in production environments.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , where the harness provides the right context at the right time to ensure task success.                                                                            |
|   2 | , but this process is often slow and expensive due to LLM latency.                                                                                                  |
|   3 | , such as Jev from Type-Safe AI, accept structured inputs (instructions, state, questions) and return rigid, predictable outputs with confidence scores.            |
|   4 | , decision models constrain potential outputs to reduce calculation, resulting in speeds up to 200 times faster and costs up to 400 times lower than frontier LLMs. |
|   5 | , with new entrants from OpenAI, Cloudflare, AWS, and open-source options like Base 10’s Mammoth and Elephant.                                                      |
|   6 | , allowing for features like live chat filtering, bulk trace evaluation, and low-latency guardrails that were previously prohibitive with LLMs.                     |
|   7 | "System 2" (slow, deliberate LLM reasoning) to "System 1" (fast, intuitive decision-making), creating an intermediate state of AI-powered software.                 |
|   8 | , self-consistency, and structured outputs, making them suitable for production environments where reliability is critical.                                         |
|   9 | (selecting appropriate intelligence levels), progressive disclosure (filtering relevant tools/skills), and auto-mode guardrails for risky tool calls.               |
|  10 | , as decision models have finite context windows and suffer from context rot if overloaded.                                                                         |
|  11 | , focused questions and calibrate confidence thresholds based on the stakes of the decision (e.g., 0.5 for low-stakes, 0.9 for high-stakes).                        |
|  12 | "cheap by default, frontier by exception," using decision models for routine tasks and reserving LLMs for complex, high-value reasoning.                            |
|  13 | , while observability remains essential for monitoring downstream impacts.                                                                                          |
|  14 | , offering a "wheels on suitcases" moment by optimizing efficiency for the majority of agent tasks.                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/DilEiawSCjM/hqdefault.jpg)]("https://www.youtube.com/watch?v=DilEiawSCjM")

[Watch on YouTube](https://www.youtube.com/watch?v=DilEiawSCjM)
