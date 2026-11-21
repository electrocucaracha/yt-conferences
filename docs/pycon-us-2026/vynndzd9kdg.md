---
layout: default
title: "Text2SQL  From Academic Benchmarks to Self Service Analytics (Sponsor: JetBrains)"
nav_order: 106
parent: PyCon US 2026
type: Video Note
description: "Artyom from JetBrains presents a critical analysis of text-to-SQL systems, arguing that high benchmark accuracy, such as the 90% achieved on Spider 2.0, is insufficient for production use because i..."
resource: "https://www.youtube.com/watch?v=VynNDZd9Kdg"
youtube_stats:
  view_count: 780
  like_count: 1
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Artyom from JetBrains presents a critical analysis of text-to-SQL systems, arguing that high benchmark accuracy, such as the 90% achieved on Spider 2.0, is insufficient for production use because it fails to address the "trust problem" where business users cannot distinguish plausible but incorrect results from accurate ones.
He explains that traditional benchmarks measure translation tasks with fully scoped problems, whereas real-world scenarios involve ambiguity, lack of discovery, and the high cost of errors, which can lead to a loss of user trust and slower workflows compared to human analysts.
To solve this, he advocates for shifting from raw SQL generation to using semantic layers, which define trusted, callable business metrics with deterministic formulas, thereby moving validation from a post-query step to a pre-deployment requirement.
However, acknowledging that building comprehensive semantic layers is expensive and time-consuming, he proposes a self-learning approach where the system lazily generates new metrics for novel questions and routes them for human validation, effectively crowdsourcing the semantic layer over time.
This architecture, which includes a kickstart phase to bootstrap initial metrics and a continuous feedback loop, ensures that the system maximizes trustworthy answers rather than just answering volume, ultimately positioning semantic layers as the essential foundation for reliable AI-driven data analytics.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | JetBrains began working on text-to-SQL approximately 1.5 years ago and has significantly evolved its approach to the task. |
|   2 | The core problem involves translating natural language business questions into SQL to reduce reliance on data analysts. |
|   3 | State-of-the-art benchmarks like Spider 2.0 and Bird show high accuracy rates, often exceeding 80-90%. |
|   4 | Benchmark questions are typically well-formulated, have pre-specified databases, and include external knowledge, unlike real-world scenarios. |
|   5 | Achieving top benchmark results requires extensive context engineering, generating multiple candidate answers, and using voting mechanisms. |
|   6 | High benchmark accuracy does not guarantee production readiness because benchmarks lack discovery, ambiguity resolution, and conversational context. |
|   7 | A major issue in production is the trust problem, where 10% of incorrect but plausible results can erode user confidence. |
|   8 | Business users cannot easily distinguish correct from incorrect SQL results, leading to slower workflows and loss of trust in the system. |
|   9 | The removal of the human validation layer in text-to-SQL systems increases the cost of errors and shifts accountability to the system. |
|  10 | Semantic layers provide trusted, deterministic metric definitions that allow systems to answer questions without generating arbitrary SQL. |
|  11 | Metrics in semantic layers include definitions, formulas, and dimensions, enabling deterministic SQL compilation without AI. |
|  12 | Using semantic layers shifts the validation step from post-query to pre-deployment, ensuring only trusted business abstractions are used. |
|  13 | Building and maintaining semantic layers is expensive and time-consuming, similar to writing comprehensive documentation for evolving data. |
|  14 | A self-learning approach allows semantic layers to be built lazily by generating metrics for new questions and sending them for human validation. |
|  15 | This crowdsourcing method reduces the need for constant human validation of every question, as the number of unique metrics is smaller than the number of questions. |
|  16 | The system can kickstart the semantic layer by introspecting the database and generating initial metrics for likely questions. |
|  17 | JetBrains ranks first on the Spider DBT track benchmark and offers an open-source Python agent for breaking benchmarks. |
|  18 | The company built a product called Data Bew, which includes a CLI for semantic layer building and a Slack bot for business users. |
|  19 | Disambiguation mechanisms are used to distinguish between similar metrics, such as revenue versus revenue growth. |
|  20 | Semantic layers are continuously validated by executing associated questions to detect changes in data models or schemas. |
|  21 | Dashboards serve as a valuable source for generating initial semantic layer metrics, reducing the time required for setup. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VynNDZd9Kdg/hqdefault.jpg)](https://www.youtube.com/watch?v=VynNDZd9Kdg)

[Watch on YouTube](https://www.youtube.com/watch?v=VynNDZd9Kdg)
