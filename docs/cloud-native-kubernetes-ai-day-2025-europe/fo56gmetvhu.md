---
layout: default
title: "Open Source Tools To Empower Ethical and Robust AI... Vicente Herrera & Alberto Rodríguez Fernandez"
nav_order: 13
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "Ventera and Alberto from Control Plane present a comprehensive overview of open-source tools for enhancing AI safety, security, and robustness, distinguishing between pre-deployment evaluations and..."
resource: "https://www.youtube.com/watch?v=Fo56gmeTvHU"
youtube_stats:
  view_count: 165
  like_count: 5
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

Ventera and Alberto from Control Plane present a comprehensive overview of open-source tools for enhancing AI safety, security, and robustness, distinguishing between pre-deployment evaluations and runtime monitoring.
They highlight key frameworks such as Garak for security probing, LLM Guard for real-time prompt filtering, and the Adversarial Robustness Toolbox (ART) for assessing traditional machine learning models against attacks like data reconstruction.
The speakers also discuss specialized tools for bias mitigation, including AI Fairness 360, and runtime observability solutions like LangKit and NVIDIA’s NeMo Guardrails, which help control LLM behavior and detect hallucinations or jailbreaks.
Emphasizing that standard benchmarks may not reflect performance in specific enterprise environments, they recommend conducting custom evaluations using datasets for toxicity and bias, while noting the importance of continuous monitoring as systems evolve.
The presentation concludes by referencing the Fintech Open Source Foundation’s efforts to establish AI governance standards in regulated industries and encourages practitioners to contribute to existing open-source projects rather than building new tools from scratch.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speakers from Control Plane discuss tools for AI safety, robustness, security, and responsible AI, focusing on open-source projects and libraries.                                      |
|   2 | Pre-deployment evaluations are essential because models may behave differently in specific systems with custom knowledge bases compared to isolated benchmarks.                             |
|   3 | Safety evaluations can be conducted using datasets like RealToxicityPrompts for toxicity, BOLD for demographic bias, and HONEST for harmful sentence completions.                           |
|   4 | Google Colab notebooks are provided to help users run evaluations using libraries like Evaluate, allowing for easy testing and customization of model assessments.                          |
|   5 | Garak is a well-maintained command-line tool for security probes that executes multiple evaluations, though it is slow and nondeterministic, requiring repeated runs to ensure reliability. |
|   6 | LLM Guard is a runtime tool that filters prompts and responses to block unsafe content, acting as a guardrail during live model interactions.                                               |
|   7 | Gizkar creates bespoke datasets tailored to specific model descriptions, focusing on safety and security with a leaner, continuous evaluation approach compared to Garak.                   |
|   8 | Pronius is a tool for comparing models, but it requires users to provide their own evaluation datasets, making it less straightforward to use out of the box.                               |
|   9 | The Adversarial Robustness Toolbox (ART), originally from IBM and now under the Linux Foundation, is a standard Python framework for assessing traditional machine learning model security. |
|  10 | ART covers red teaming attacks, blue teaming defenses, and metrics, including database reconstruction attacks and noise-based misclassification tricks.                                     |
|  11 | AI Fairness 360, backed by IBM, specifically addresses bias and fairness in machine learning models using estimators, metrics, and detectors to identify discrimination.                    |
|  12 | NeMo Guardrails, backed by Nvidia, sits between users and LLMs to control conversations using a custom language for defining rails that block unsafe prompts and responses.                 |
|  13 | NeMo Guardrails supports self-checking, community models, and third-party APIs to assess content safety, security, hallucinations, and fact-checking.                                       |
|  14 | LangKit, backed by Waps, focuses on runtime monitoring and observability, extracting relevant conversation data for visualization via paid platforms or local libraries.                    |
|  15 | Inspect AI, backed by the UK nonprofit Open, is a lightweight benchmark for LLMs that evaluates a wide range of performance aspects beyond just security.                                   |
|  16 | Broken Heel, backed by Vision Fox, performs a single greedy coordinate jailbreak attack but is considered not well-maintained and not ready for production use.                             |
|  17 | The Fintech Open Source Foundation (FENOS) is collaborating on an AI governance framework for highly regulated environments like financial institutions, focusing on risks and mitigations. |
|  18 | Control Plane is developing a reference architecture for an AI proxy security filter that integrates tools like Guardrails to intercept and secure model communications.                    |
|  19 | Users are advised to continuously validate AI systems in their specific environments, as behavior changes with evolving custom prompts, RAG applications, and infrastructure.               |
|  20 | The speakers recommend contributing to existing tools like Garak and LLM Guard rather than building new ones, suggesting adding safety-focused probes to Garak for broader coverage.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Fo56gmeTvHU/hqdefault.jpg)](https://www.youtube.com/watch?v=Fo56gmeTvHU)

[Watch on YouTube](https://www.youtube.com/watch?v=Fo56gmeTvHU)
