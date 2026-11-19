---
layout: default
title: "Stop Vibe-Testing: Run Real Agent Evals - Laurie Voss, Arize AI"
nav_order: 96
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Laurie Voss, Head of Developer Relations at Arise AI, presents a data-driven approach to evaluating AI agents, arguing against "vibes-based" shipping in favor of rigorous testing.'
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

Laurie Voss, Head of Developer Relations at Arise AI, presents a data-driven approach to evaluating AI agents, arguing against "vibes-based" shipping in favor of rigorous testing.
She distinguishes between three types of evaluations: deterministic code evals for format checks, LLM-as-a-judge for assessing semantic accuracy and tone, and human experts for calibrating the other two.
Voss emphasizes that agents require specific metrics like "pass-at-k" for development and "pass-to-k" for production reliability, while cautioning that LLM judges have inherent biases and must be validated against a golden dataset of human-labeled data.
To build effective evaluations, she advises reading production traces to define clear success criteria, structuring judge prompts with explicit roles and binary constraints, and grading outcomes rather than specific execution paths.
Ultimately, the goal is to create a closed-loop system where evaluation feedback drives automated improvements, allowing teams to replace subjective opinions with actionable, trackable numbers that ensure agent quality and consistency.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** Testing GitHub tasks showed MCP and CLI had equal correctness, but MCP was six times more expensive and five times slower on complex tasks.                                   |
|   2 | :** CLIs are developer tools using API keys, while MCP is a consumer/enterprise tool using OAuth, making it the only practical option for broad-scale agent access.               |
|   3 | :** The debate between MCP and CLI should be resolved using actual evaluation data rather than "vibes-based" opinions.                                                            |
|   4 | :** Traces are logs recording AI actions (spans, inputs, outputs, costs), while evals are tests that judge the quality of those actions.                                          |
|   5 | :** Relying on manual checks ("looks good to me") fails to catch regressions, does not scale, and prevents running tests in CI.                                                   |
|   6 | :** Evals provide trackable numbers, enable safe model switching, and prevent prompt changes from breaking other functionalities.                                                 |
|   7 | :**                                                                                                                                                                               |
|   8 | :** Deterministic, cheap, and fast; used for formats and required fields.                                                                                                         |
|   9 | :** Understands meaning and accuracy; costs money and is non-deterministic.                                                                                                       |
|  10 | :** The gold standard for calibration and novel failures; slow and expensive.                                                                                                     |
|  11 | :** Agents have many steps where early errors cascade; they are non-deterministic and can be "confidently wrong" (e.g., answering about Nikola Tesla instead of the car company). |
|  12 | :**                                                                                                                                                                               |
|  13 | @K:** Succeeded at least once in K tries (good for demos/coding agents).                                                                                                          |
|  14 | :** Succeeded every time (required for production/customer support).                                                                                                              |
|  15 | :**                                                                                                                                                                               |
|  16 | :** Test new features; expect ~50% pass rate to identify areas for improvement.                                                                                                   |
|  17 | :** Ensure existing features still work; expect 100% pass rate.                                                                                                                   |
|  18 | :** Reading production traces is the highest-value step to understand failure modes and define what "good" looks like before writing evals.                                       |
|  19 | :** Distinguish between retrieval failure, reasoning errors, hallucinations, and scope violations to apply correct fixes.                                                         |
|  20 | :** Prioritize fixes based on frequency times severity.                                                                                                                           |
|  21 | :**                                                                                                                                                                               |
|  22 | :** Define the judge's expertise (e.g., "expert financial analyst").                                                                                                              |
|  23 | :** Define specific good/bad traits rather than vague terms like "accurate."                                                                                                      |
|  24 | :** Use XML tags to separate instructions from data.                                                                                                                              |
|  25 | :** Provide examples to guide behavior, but monitor for overfitting.                                                                                                              |
|  26 | :** Use binary (good/bad) or ternary (good/bad/N/A) choices instead of numeric scores, which LLMs handle poorly.                                                                  |
|  27 | :** Grade the final result and system state (e.g., database refund) rather than the specific tool-call trajectory, as agents may find creative paths.                             |
|  28 | :** Agent judges agree with expert consensus ~90% of the time, compared to ~70% for plain LLM judges.                                                                             |
|  29 | :** Validate LLM judges against a "golden dataset" created by human experts to ensure they optimize for the correct definition of quality.                                        |
|  30 | :** LLM judges prefer longer, confident answers and their own model's output; use cross-model judging to mitigate this.                                                           |
|  31 | :** Use LLM judge explanations to feed feedback into coding agents, allowing them to automatically fix issues and rerun evals for continuous improvement.                         |

# Video

This video is no longer available on YouTube.

<!-- resource: https://www.youtube.com/watch?v=1kP4dQtUT50 -->
