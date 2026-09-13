---
layout: default
title:
  "Keynote: Orchestrating Document Data Extraction with Dapr Agents - Fabian
  Steinbach"
nav_order: 179
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Fabian, a software architect at Zeiss, explains the challenges of extracting
  structured optical data from non-standardized documents like handwritten notes and
  forms in various languages, which is crucial for manufacturing precision lenses...
resource: https://www.youtube.com/watch?v=9QXoL0ZYDn8
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

Fabian, a software architect at Zeiss, explains the challenges of extracting structured optical data from non-standardized documents like handwritten notes and forms in various languages, which is crucial for manufacturing precision lenses.
To address this, Zeiss implemented Dapr Agents, focusing on three main requirements: control, reliability, and flexibility.
They constrained AI behavior using a durable workflow that included preprocessing, OCR, and selective use of LLMs or agents, ensuring predictable and reliable results with state persistence to avoid redundant processing.
The system’s flexibility allows for easy integration of new models by changing configurations rather than code.
As a result, Zeiss was able to move from prototype to production in two months without needing labeled training data, achieving recognition results comparable to specialized machine learning systems.

# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Manufacturing precision lenses requires extracting structured optical data from non-standardized documents, such as handwritten notes and typed forms in multiple languages. |
|   2 | Accurate data extraction is critical; errors lead to incorrect lenses.                                                                                                       |
|   3 | An automated, reliable extraction process was needed.                                                                                                                        |
|   4 | Modern models interpret diverse documents well, but production deployment required control, reliability, and flexibility.                                                    |
|   5 | Dapr Agents provided:                                                                                                                                                        |
|   6 | Control: AI was constrained using a durable workflow (preprocessing, OCR, LLM/agent calls) to avoid unpredictable results.                                                   |
|   7 | Reliability: Durable workflow persists state after each step, preventing re-running expensive tasks if a failure occurs, saving time and cost.                               |
|   8 | Flexibility: Workflow remains stable even as models change; new models can be integrated by changing configuration, not code.                                                |
|   9 | Three key takeaways:                                                                                                                                                         |
|  10 | Constrain the AI with workflows rather than allowing fully autonomous operation.                                                                                             |
|  11 | Use specialized models, general LLMs, and deterministic logic appropriately; avoid using LLMs where simpler functions suffice.                                               |
|  12 | Decouple model selection from code by using configuration, enabling easy adoption of new models.                                                                             |
|  13 | The approach enabled moving from prototype to production in two months with zero label training data.                                                                        |
|  14 | Achieved recognition results comparable to specialized machine learning systems.                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9QXoL0ZYDn8)
