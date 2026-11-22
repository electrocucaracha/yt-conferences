---
layout: default
title: "Going From Notebooks to Scalable Systems - Catherine Nelson"
nav_order: 24
parent: PyCon US 2025
type: Video Note
description: Dr.
resource: "https://www.youtube.com/watch?v=o4hyA4hotxw"
youtube_stats:
  view_count: 2161
  like_count: 57
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Dr.
Katherine Nelson presents a talk on transitioning Python code from Jupyter notebooks to scalable, production-ready systems, emphasizing that this process requires a fundamental mindset shift from flexible exploration to robust, reproducible engineering.
While acknowledging the utility of notebooks for data exploration and visualization, she highlights their limitations regarding version control, automation, and code reuse, advocating for standalone scripts when deploying models or ensuring code reliability.
Using a penguin classification model as a case study, she demonstrates a refactoring workflow that involves identifying distinct tasks, converting notebook cells into modular functions with defined inputs and outputs, and writing unit tests to verify functionality.
The presentation also covers tools like `nbconvert` and `jupytext` for initial code extraction, while stressing that manual refactoring into a structured pipeline with a main execution function is essential for scalability.
Nelson concludes by recommending best practices such as consistent formatting, documentation, and CI/CD integration, and addresses audience questions on using frameworks like Kedro, managing global variables, and fostering better communication between data scientists and software engineers to adopt these engineering standards.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Dr. Katherine Nelson presented a talk on transitioning Python code from Jupyter notebooks to scalable production systems.                                                      |
|   2 | The speaker highlighted that while notebooks are excellent for exploration, visualization, and interactive data analysis, they lack structure for production use.              |
|   3 | Key limitations of notebooks include difficulty with version control, potential for out-of-order cell execution, and challenges in reusing code across different projects.     |
|   4 | A mindset shift is required when moving to standalone scripts, focusing on maintainability, robustness, reproducibility, and automation rather than flexibility.               |
|   5 | Indicators for moving to scripts include preparing code for production, needing to run code automatically, or when the notebook becomes too complex to manage.                 |
|   6 | Tools such as nbconvert and jupytext can automate the conversion of notebook code into Python scripts, though manual refactoring is usually necessary.                         |
|   7 | The refactoring process involves identifying distinct tasks within the notebook and organizing them into modular functions with clear inputs and outputs.                      |
|   8 | Writing unit tests is essential to verify that refactored functions behave as expected and to prevent errors during the transition from notebook to script.                    |
|   9 | The speaker demonstrated this process using a machine learning example that classifies penguin species based on physical features.                                             |
|  10 | Best practices for scalable code include consistent formatting, thorough documentation, separating configuration into dedicated files, and using CI/CD tools for automation.   |
|  11 | Key skills for this transition include breaking code into sensible modular functions, ensuring efficiency, and using tests to safely refactor code.                            |
|  12 | The speaker recommended using notebooks for initial exploration and then importing reusable functions into notebooks from standalone Python files for further experimentation. |
|  13 | Effective communication between software engineers and data scientists is crucial for adopting software engineering best practices in data science workflows.                  |
|  14 | Global variables and configuration settings found in notebooks should be separated into dedicated configuration files to improve code clarity and maintainability.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/o4hyA4hotxw/hqdefault.jpg)](https://www.youtube.com/watch?v=o4hyA4hotxw)

[Watch on YouTube](https://www.youtube.com/watch?v=o4hyA4hotxw)
