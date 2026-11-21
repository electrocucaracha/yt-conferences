---
layout: default
title: "When KPIs Go Weird: Anomaly Detection with Python - Juliana Ferreira Alves"
nav_order: 113
parent: PyCon US 2026
type: Video Note
description: "The speaker, a business intelligence engineer and former chemical engineer, introduces a talk on anomaly detection, emphasizing that it extends beyond simple KPIs to analyzing diverse data types us..."
resource: "https://www.youtube.com/watch?v=7Zj9Ma2l0lM"
youtube_stats:
  view_count: 762
  like_count: 3
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

The speaker, a business intelligence engineer and former chemical engineer, introduces a talk on anomaly detection, emphasizing that it extends beyond simple KPIs to analyzing diverse data types using tools like Spark.
The presentation defines anomaly detection as identifying outliers in large datasets where manual monitoring is impractical, highlighting real-world applications such as financial fraud prevention, medical image analysis, and identifying bot traffic on websites.
The core of the talk focuses on unsupervised learning algorithms, specifically Isolation Forest, Support Vector Machines, and Local Outlier Factor, explaining how they identify data points that deviate from normal patterns without requiring labeled targets.
The speaker demonstrates the implementation of these models using Python libraries like scikit-learn and PyOD, noting that while the coding is straightforward, the process is heavily dependent on tuning parameters like contamination rates and understanding the specific computational trade-offs of each algorithm.
Finally, the talk addresses the practical challenges of deploying these models, including class imbalance, the scarcity of labeled data, and the critical need for business context to ensure that detected anomalies are meaningful and actionable, while also cautioning about the responsible use of AI agents in selecting and interpreting these complex algorithms.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker is a business intelligence engineer with a background in chemical engineering and computer science, currently working in analytics. |
|   2 | The talk focuses on anomaly detection, defining it as identifying data points that deviate significantly from normal patterns or distributions. |
|   3 | Anomaly detection is essential for monitoring large datasets, such as banking transactions, where manual analysis by humans is impossible. |
|   4 | Key application areas include financial fraud prevention, medical image analysis for disease detection, and identifying bot traffic or unusual user behavior on websites. |
|   5 | In real-world scenarios, stakeholders often present general problems rather than specific anomaly detection requests, requiring analysts to classify the issue and select appropriate techniques. |
|   6 | Machine learning algorithms for anomaly detection are divided into supervised learning, which uses labeled data with known targets, and unsupervised learning, which identifies differences without prior labels. |
|   7 | Unsupervised learning is more common in practice because real-world data is often messy and lacks pre-labeled anomaly classifications. |
|   8 | Different algorithms, such as those in the PyOD library, use various methods like distance-based or density-based approaches to classify outliers. |
|   9 | Isolation Forest works by building multiple decision trees to isolate data points; anomalies are easier to isolate and thus identified as outliers through a voting mechanism. |
|  10 | Support Vector Machines (SVM) can transform data dimensions using polynomial functions to separate outliers that cannot be divided by a simple linear boundary. |
|  11 | Local Outlier Factor (LOF) identifies anomalies based on density, flagging points that are far from their neighbors or do not fit within a local cluster. |
|  12 | Implementation can be done using libraries like scikit-learn, which offers basic algorithms, or PyOD for more complex models. |
|  13 | The contamination parameter is critical in anomaly detection, representing the expected percentage of outliers, but is difficult to define accurately in real-world scenarios. |
|  14 | Fine-tuning models is the most time-consuming aspect, often requiring data transformations like PCA to visualize and adjust detection precision. |
|  15 | Class imbalance is a significant challenge, as anomalies are rare compared to normal data, making it hard to determine the correct contamination level. |
|  16 | Detecting anomalies is not sufficient; the results must be validated against business logic to ensure the identified outliers are meaningful and actionable. |
|  17 | Algorithms should be used responsibly, and the rise of AI agents may assist in selecting and explaining the appropriate algorithms for specific problems. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7Zj9Ma2l0lM/hqdefault.jpg)](https://www.youtube.com/watch?v=7Zj9Ma2l0lM)

[Watch on YouTube](https://www.youtube.com/watch?v=7Zj9Ma2l0lM)
