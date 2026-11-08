---
layout: default
title: "Data Agents over S3: Build the Missing Semantic Layer for Files - Dmitry Petrov, DataChain"
nav_order: 130
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "This presentation discusses the challenges of using AI agents to analyze unstructured data, such as video and sensor logs, stored in object storage systems like S3."
resource: "https://www.youtube.com/watch?v=0o93aKBvuYQ"
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

This presentation discusses the challenges of using AI agents to analyze unstructured data, such as video and sensor logs, stored in object storage systems like S3.
The speaker identifies three primary obstacles: the inability to fit massive datasets into LLM context windows, the high computational cost and resource management required for data extraction, and the difficulty of trusting previously computed results that may be outdated or incorrect.
To address these issues, the talk introduces a semantic layer or knowledge base that dynamically aggregates metadata and past query results, allowing agents to retrieve insights in minutes rather than hours or days of recomputation.
A live demonstration shows how this approach reduces query time by leveraging cached information while still verifying data integrity to handle duplicates and changes.
The speaker concludes that while current agents struggle with efficiency and trust in large-scale storage environments, building a robust context layer with proper resource management and verification mechanisms is essential for making AI workflows productive and cost-effective.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , a founder of DataChain and creator of DVC, discusses building semantic layers to make AI agents smarter when working with unstructured data (video, images, telemetry) on object storage like S3. |
|   2 | (e.g., "What data was used for training?") and receiving accurate answers without manually navigating millions of files.                                                                            |
|   3 | :                                                                                                                                                                                                   |
|   4 | :** Single large files or massive datasets cannot fit into LLM context windows, requiring an intermediary metadata layer.                                                                           |
|   5 | :** Extracting information requires significant resources (GPUs, multiple machines), and agents often waste budget on inefficient operations or failed sync checks.                                 |
|   6 | :** Agents struggle to verify if cached knowledge is still accurate or relevant, leading to hallucinations or incorrect aggregations if they blindly trust previous results.                        |
|   7 | % of complex storage scenarios, such as failing to check cache synchronization or wasting resources re-processing data that is already available.                                                   |
|   8 | (tables, files) increases accuracy by less than 1% while significantly increasing processing time, according to recent benchmarks.                                                                  |
|   9 | ; it must be continuously updated by agents as new insights are generated, rather than being a static, manually curated database that becomes outdated.                                             |
|  10 | : a query that would take 30–45 minutes of compute from scratch was answered in 3 minutes by retrieving and verifying previous results.                                                             |
|  11 | : agents must verify retrieved knowledge against current reality (e.g., checking for duplicates or data changes) to ensure accuracy, as cached data may not match the specific query requirements.  |
|  12 | (e.g., Markdown) including descriptions, dependencies, and schemas, which are crucial for preventing agent hallucinations and enabling efficient code generation.                                   |
|  13 | , low-latency queries (e.g., 100ms joins in Postgres); it is designed for analytical, prolonged use cases involving large-scale data processing and lineage.                                        |
|  14 | (e.g., suggesting video splitting or model selection) but struggle with domain-specific, team-level knowledge that is not easily generalizable across different organizations.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0o93aKBvuYQ/hqdefault.jpg)]("https://www.youtube.com/watch?v=0o93aKBvuYQ")

[Watch on YouTube](https://www.youtube.com/watch?v=0o93aKBvuYQ)
