---
layout: default
title: "Talks - Krishi Sharma: Trust Fall: Three Hidden Gems in MLFlow"
nav_order: 175
parent: PyCon US 2024
type: Video Note
description: 'The presentation, titled "Trust Fall," emphasizes the critical importance of building trust in machine learning applications through rigorous documentation, reproducibility, and transparency, using...'
resource: "https://www.youtube.com/watch?v=cAgrIilgP4A"
youtube_stats:
  view_count: 339
  like_count: 7
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

The presentation, titled "Trust Fall," emphasizes the critical importance of building trust in machine learning applications through rigorous documentation, reproducibility, and transparency, using the defunct biotech startup Theranos as a cautionary tale against unsupported claims.
The speaker introduces MLflow, an open-source Python package, as a solution to automate metric tracking and organize experiment data via artifact storage and a SQLite database, thereby reducing the manual burden of documenting AI workflows.
Through a case study of a nine-month radar data project, the speaker highlights three "hidden gems" of MLflow: the `autolog` feature for automatic framework-specific tracking, Git commit hash logging to ensure code-metric alignment for reproducibility, and the model registry for organizing and versioning models for client presentation.
The talk also shares practical lessons learned, such as the necessity of backing up the MLflow database to prevent data loss and implementing pre-commit hooks to ensure frequent code commits before running experiments.
Finally, the speaker addresses audience questions regarding local deployment, feature engineering tracking, and the storage mechanisms of the model registry, reinforcing that while MLflow is powerful, understanding the underlying principles of trust and data management is equally vital for successful AI integration.

# Main Points

|   # | Main point                                                                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation emphasizes building trust in machine learning applications through documentation, reproducibility, and transparency, using the defunct biotech startup Theranos as a cautionary tale about the dangers of unverified metrics. |
|   2 | MLflow is an open-source Python package that automates metric tracking and provides organization tools, including artifact storage and a SQLite database, to manage machine learning experiments without manual design.                        |
|   3 | The artifact storage system organizes data by experiments and runs, assigning unique hash values to each trial, while the database schema is automatically generated to store nuances of each run.                                             |
|   4 | MLflow includes a user-friendly interface for visualizing metrics, parameters, and tags, which helps teams communicate findings to both technical and non-technical stakeholders.                                                              |
|   5 | Integration into a Python project requires only two lines of code to set the tracking URI and experiment name, after which MLflow automatically organizes experiment runs and database entries.                                                |
|   6 | The tool supports a command-line interface for quick database management and a low-level API for advanced features, while also supporting major frameworks like PyTorch, TensorFlow, and LLM-based frameworks.                                 |
|   7 | A key feature called MLflow Auto-log automatically detects the machine learning framework and tracks all specific parameters and metrics, reducing technical debt and ensuring consistent logging from the start.                              |
|   8 | Logging the Git commit hash alongside MLflow runs creates a one-to-one mapping between code versions and metric results, enabling reproducibility and allowing developers to check out specific commits to verify results.                     |
|   9 | The MLflow Model Registry organizes models into searchable versions linked to specific run IDs, facilitating the presentation of a clear narrative of model development and evolution to clients.                                              |
|  10 | A critical lesson from a real project was the accidental deletion of the MLflow database, highlighting the necessity of backing up metric data just as rigorously as input training data.                                                      |
|  11 | Frequent Git commits are essential for effective reproducibility; the team implemented a pre-commit hook to ensure developers committed changes before executing MLflow runs, creating accurate code snapshots.                                |
|  12 | While MLflow is powerful, it lacks some advanced visualizations for system metrics like CPU and GPU utilization compared to competitors like Weights and Biases.                                                                               |
|  13 | MLflow can track custom feature engineering parameters and metrics by adding specific log lines, allowing for detailed monitoring of unique variables outside of standard framework logging.                                                   |
|  14 | The tool can be run entirely locally for experimentation, though users must be cautious about data loss since local databases lack cloud-based versioning or object lock features.                                                             |
|  15 | Storing sensitive data, such as patient images, in the MLflow database requires careful consideration for backup strategies, potentially necessitating private cloud storage rather than Git repositories.                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/cAgrIilgP4A/hqdefault.jpg)](https://www.youtube.com/watch?v=cAgrIilgP4A)

[Watch on YouTube](https://www.youtube.com/watch?v=cAgrIilgP4A)
