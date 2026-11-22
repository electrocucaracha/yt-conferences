---
layout: default
title: "Sponsor Presentations - Avoid the top 5 web data pitfalls when developing AI models (Bright Data)"
nav_order: 37
parent: PyCon US 2024
type: Video Note
description: "Jakub Glodek from Bright Data presents a webinar on the top five pitfalls in AI model development, emphasizing that high-quality data collection is the foundation for successful AI."
resource: "https://www.youtube.com/watch?v=3NH_bLdSOCo"
youtube_stats:
  view_count: 296
  like_count: 2
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Jakub Glodek from Bright Data presents a webinar on the top five pitfalls in AI model development, emphasizing that high-quality data collection is the foundation for successful AI.
He identifies data bias as a primary issue, noting that biased training data leads to skewed outputs, and stresses the need for diverse data sources to prevent models from overfitting or underfitting.
To address insufficient data variety, he recommends using robust proxy networks and web unlocking technologies to scrape diverse, global data effectively.
Glodek also highlights the critical importance of data validation, suggesting specific checks like uniqueness and persistence to ensure data integrity before it enters the AI pipeline.
Finally, he discusses data drift, explaining that while models may become less effective over time due to changing real-world conditions, proper labeling and source tracking allow teams to diagnose and correct these issues.
The session concludes with a discussion on the legal legitimacy of scraping publicly accessible data, citing recent court victories that support the practice, and offers practical tools for managing data pipelines and quality assurance.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Data bias occurs when training data does not match reality in quantity or quality, often originating from biased data collection sources.                         |
|   2 | Bias can be identified by searching for terms like "nurse" or "programmer" to see if search results reflect historical rather than current demographic realities. |
|   3 | Key areas where bias breaks the pipeline include data collection, data labeling, model training, and deployment testing.                                          |
|   4 | Insufficient data variety leads to poor model performance in real-world conditions because homogeneous training data fails to capture diverse scenarios.          |
|   5 | To address lack of variety, organizations must gather data from different sources, groups, and regions using diverse proxy networks.                              |
|   6 | A robust proxy network requires a large IP pool, such as over 72 million IPs, to allow for precise regional targeting and diverse user experiences.               |
|   7 | Crawling capabilities must include browser fingerprinting, retry logic, and proxy management to bypass anti-bot technologies effectively.                         |
|   8 | Centralizing web unlocking technology reduces costs and improves efficiency compared to maintaining separate in-house teams for each scraping task.               |
|   9 | Overfitting happens when a model is too complex and fails to generalize, while underfitting occurs when a model is too simple to capture underlying patterns.     |
|  10 | Both overfitting and underfitting are best addressed by increasing the volume and diversity of the training data rather than just adjusting model complexity.     |
|  11 | Data-as-a-Service models allow data architects to purchase pre-scraped datasets without managing the underlying scraping infrastructure.                          |
|  12 | Dataset marketplaces offer pre-built, filterable data from major sites, reducing the need for custom scraper development for common sources.                      |
|  13 | Poor data quality, including errors and inconsistencies, causes AI models to inherit flaws, making high-quality data essential for reliability.                   |
|  14 | Implementing validation checks such as uniqueness, persistence, and record thresholds helps detect data issues before they enter the AI model.                    |
|  15 | Validation flags should be monitored continuously because sites change frequently, which can silently break data pipelines and introduce bad data.                |
|  16 | Data drift occurs when real-world data changes over time, causing the model to become less effective if it is not monitored and adapted.                          |
|  17 | Monitoring data drift involves comparing current data trends against training data to identify acceptable seasonal changes versus problematic manipulations.      |
|  18 | Legal precedents in the US have established that scraping publicly accessible data without login requirements is generally permissible.                           |
|  19 | GDPR compliance often involves removing personally identifiable information during the validation step before data is stored or processed.                        |
|  20 | Bypassing anti-bot measures is legally distinct from accessing non-public data, as public accessibility defines the scope of permissible scraping.                |
|  21 | Data stability refers to maintaining consistent schema structures and data types across scraping runs to ensure reliable model inputs.                            |
|  22 | Validation rules should be reviewed and adjusted regularly as sites evolve, with some checks serving as yellow flags for investigation rather than hard failures. |
|  23 | Bright Data does not directly monitor post-deployment data drift but ensures proper labeling and source tracking to help clients diagnose and fix drift issues.   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3NH_bLdSOCo/hqdefault.jpg)](https://www.youtube.com/watch?v=3NH_bLdSOCo)

[Watch on YouTube](https://www.youtube.com/watch?v=3NH_bLdSOCo)
