---
layout: default
title: "Your #1 Docs Audience Isn't Human: Dev Ed's MCP Strategy at Apollo - Daniel Abdelsamed"
nav_order: 88
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Daniel Abdal-Samad, a staff software engineer at Apollo, explains how the company’s documentation strategy has evolved to address a dual audience of humans and AI agents, noting that over 40% of tr..."
resource: "https://www.youtube.com/watch?v=Hw668yuvkAo"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Daniel Abdal-Samad, a staff software engineer at Apollo, explains how the company’s documentation strategy has evolved to address a dual audience of humans and AI agents, noting that over 40% of traffic is now agentic.
He details the transition from initial MCP tools that required multiple search and read calls, which resulted in high token usage, to a purpose-built "research docs" tool designed for efficiency.
This new approach utilizes an automated pipeline that semantically chunks documentation using AI, stores embeddings, and retrieves exact content chunks to minimize context window consumption.
To validate these improvements, Abdal-Samad describes a rigorous end-to-end testing framework using executor and scoring agents within a sandbox environment, employing binary rubrics and statistical analysis to ensure consistent, high-quality results.
The final implementation demonstrates a 70% reduction in tool calls and a 50% decrease in token usage while maintaining the same output quality, proving the effectiveness of the optimized agentic content source.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Over 40% of Apollo documentation traffic is now agentic, including AI user agents, crawlers, and direct tool usage.                          |
|   2 | Agentic audiences prefer direct, pattern-based content and code examples, unlike human readers who seek context and narratives.              |
|   3 | The Model Context Protocol (MCP) enables agents to interface directly with documentation remotely.                                           |
|   4 | Initial MCP tools for searching and reading docs resulted in high token usage, with single answers consuming up to 25,000 tokens.            |
|   5 | A new "research docs" tool was developed to accept an array of questions and context, returning exact documentation chunks in a single call. |
|   6 | An automated pipeline uses AI to semantically chunk documentation based on page-specific instructions in front matter.                       |
|   7 | Embedding models generate vector arrays to represent semantic meaning, utilizing cosine similarity to measure relevance.                     |
|   8 | To improve retrieval accuracy, the system generates hypothetical user questions at build time to enhance embedding coverage.                 |
|   9 | End-to-end MCP testing employs a direct executor agent and an isolated scoring agent within a shared sandbox environment.                    |
|  10 | The executor agent must mirror the user's environment, including model, tools, and temperature settings, to ensure valid comparisons.        |
|  11 | Scoring uses a static binary rubric rather than floating-point scores to improve accuracy and consistency in evaluating task completion.     |
|  12 | Statistical methods, such as Fisher's theorem, are applied to test results to guarantee confidence in performance improvements.              |
|  13 | The new research tool achieved 70% fewer tool calls and 50% fewer tokens compared to the previous search-and-read approach.                  |
|  14 | Live demonstrations confirmed that the single-call research tool outperforms the multi-call legacy tools in efficiency.                      |
|  15 | The project highlights the importance of treating AI models as statistical entities requiring repeated testing for reliable metrics.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Hw668yuvkAo/hqdefault.jpg)](https://www.youtube.com/watch?v=Hw668yuvkAo)

[Watch on YouTube](https://www.youtube.com/watch?v=Hw668yuvkAo)
