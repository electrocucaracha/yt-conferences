---
layout: default
title: "Post-Training Is Back - Ariel Shulman, Nvidiav"
nav_order: 12
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Ariel argues that post-training is no longer exclusive to AI labs because new tools allow developers to generate realistic enterprise data for benchmarking and training agents."
resource: "https://www.youtube.com/watch?v=ff5o3F_SKO0"
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

Ariel argues that post-training is no longer exclusive to AI labs because new tools allow developers to generate realistic enterprise data for benchmarking and training agents.
The core challenge in making agents reliable is their tendency to guess answers when data is missing, unavailable, or inconsistent across siloed systems, rather than admitting they do not know.
Current workarounds, such as using larger models or complex prompts, are costly and fail to address the fundamental issue that enterprise data is high-volume, skewed, and messy in ways that LLMs cannot realistically simulate.
To solve this, the speaker introduces Era, a free company simulator that generates synthetic, high-volume data with built-in ground truths and intentional inconsistencies, enabling programmatic grading without human labeling.
By using Era to create disjoint training and testing datasets, developers can effectively fine-tune agents to recognize absent data and stop searching when answers are not present, thereby improving reliability and reducing inference costs.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , driven by the need for ground truth.                                                                                                             |
|   2 | : when the answer does not exist in records, when data is in unavailable systems, or when they misinterpret absent data (nulls) as valid answers.  |
|   3 | "I don't know," but agents are difficult to train to say this.                                                                                     |
|   4 | (which are more expensive and may still guess incorrectly) and improving prompts (which do not scale effectively).                                 |
|   5 | "Skills" are often misnamed; they function more like notes or instructions rather than abilities acquired through training and practice.           |
|   6 | , whereas training costs are paid once, making post-training a more efficient long-term strategy.                                                  |
|   7 | , siloed systems requiring cross-joins, time-based complexity, and skewed distributions (long-tail data).                                          |
|   8 | , consistent, and evenly distributed records, lacking the messiness, inconsistencies, and pagination complexities of real production environments. |
|   9 | ; labeling errors trains mistakes into the model, and using the same data for training and testing measures memory rather than skill.              |
|  10 | , training, and testing agents by generating realistic, high-volume synthetic data across cloud and SaaS systems.                                  |
|  11 | , forcing agents to learn how to page and aggregate results.                                                                                       |
|  12 | (e.g., employees) across all connected systems, unlike LLMs which may create conflicting versions.                                                 |
|  13 | , including missing fields, duplicates, and cross-system inconsistencies, to test agents where they typically fail in production.                  |
|  14 | , preventing overfitting and ensuring that evaluation measures learned behavior rather than memorization.                                          |
|  15 | , allowing for programmatic grading via code rather than relying on LLMs or human labelers.                                                        |
|  16 | "I don't know" responses by creating cases where the data is intentionally absent.                                                                 |
|  17 | ’s ability to withhold answers when data is missing and reduced context exhaustion.                                                                |
|  18 | (data creation, labeling, benchmarking) are now accessible and free for builders via Era.                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ff5o3F_SKO0/hqdefault.jpg)](https://www.youtube.com/watch?v=ff5o3F_SKO0)

[Watch on YouTube](https://www.youtube.com/watch?v=ff5o3F_SKO0)
