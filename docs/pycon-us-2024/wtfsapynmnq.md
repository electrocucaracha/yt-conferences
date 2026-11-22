---
layout: default
title: "Talks - Juliana Ferreira Alves: Improve Your ML Projects: Embrace Reproducibility and Production..."
nav_order: 152
parent: PyCon US 2024
type: Video Note
description: "Juliana Fera Alves presents a talk on improving machine learning projects by embracing reproducibility and production readiness using Kedro, a Python framework for scalable data science pipelines."
resource: "https://www.youtube.com/watch?v=wtFsapyNmNQ"
youtube_stats:
  view_count: 217
  like_count: 1
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

Juliana Fera Alves presents a talk on improving machine learning projects by embracing reproducibility and production readiness using Kedro, a Python framework for scalable data science pipelines.
Developed by Quantum Black, Kedro bridges the communication gap between data scientists and engineers by enforcing software engineering best practices, such as providing a standardized project template and a data catalog that simplifies data management and configuration.
The framework organizes workflows into pipelines and nodes, which are essentially wrapped functions with defined inputs and outputs, facilitating clear dependency management and easier debugging.
Additionally, Kedro offers built-in experiment tracking to automatically log parameters and metrics, along with visualization tools like Kedro Vis to monitor model performance over time.
The presentation concludes by highlighting Kedro’s extensibility for connecting to various data sources and orchestrators, emphasizing its role in ensuring code readability, reproducibility, and seamless collaboration across diverse technical teams.

# Main Points

|   # | Main point                                                                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kedro is a Python framework designed to create scalable data science pipelines using software engineering best practices for production-ready code.                                                         |
|   2 | It facilitates communication between data scientists, machine learning engineers, and data engineers by providing a common structure for project development.                                               |
|   3 | Created by Quantum Black from McKinsey, Kedro helps teams integrate processes and understand how data science code translates into production environments.                                                 |
|   4 | The framework should be viewed as a pipeline framework rather than a complete MLOps solution or data infrastructure replacement, though it offers connectors for orchestration and data sources.            |
|   5 | Key features include a standardized project template, a data catalog, the concept of nodes and pipelines, experiment tracking, and extensibility for integration with other tools.                          |
|   6 | The project template provides a directory structure with folders for configuration, data, documentation, notebooks, and source code to facilitate project organization and sharing.                         |
|   7 | The configuration folder contains the data catalog and model settings, supporting different environments such as base, local, dev, and production to manage version control and local overrides.            |
|   8 | The data folder is structured to separate raw, intermediate, features, models, and reporting data, making it easier to track data lineage and access specific datasets.                                     |
|   9 | Notebooks are recommended for initial experimentation and prototyping, after which the logic can be translated into Kedro pipelines for better maintainability and reproducibility.                         |
|  10 | The data catalog allows users to specify data sources and destinations, with Kedro managing the data retrieval and storage, supporting local files, Hadoop, S3, GCP, and HDFS.                              |
|  11 | A pipeline is an object that organizes the dependencies of code nodes, defining the sequence of actions to manipulate data and ensuring proper execution order.                                             |
|  12 | Nodes are wrappers for functions within a pipeline that specify inputs, outputs, and names, allowing for easier debugging and tracking of specific processing steps.                                        |
|  13 | Experiment tracking automatically logs parameters, metrics, and model artifacts during pipeline runs, storing results in JSON or YAML files for analysis.                                                   |
|  14 | The Kedro Vis tool provides a visualization interface to compare pipeline runs, monitor metric changes over time, and inspect pipeline structures and data flows.                                           |
|  15 | Extensibility features allow Kedro to connect with commercial machine learning platforms and open-source orchestrators, with an active community continuously developing new connectors.                    |
|  16 | The framework enhances reproducibility by ensuring projects can be easily shared and run on different machines, with support for generating Docker files and managing requirements.                         |
|  17 | Scalability is improved by making it easier to compare different algorithms and parameters as projects grow, preventing the complexity issues often associated with notebook-based development.             |
|  18 | The core goal of using Kedro is to improve code readability and ensure that the work reflects care and clarity, aligning with the principle that clean code looks like it was written by someone who cares. |
|  19 | Inference pipelines can be set up using Kedro by creating specific pipelines for testing or prediction, which can then be deployed in cloud environments for continuous inference.                          |
|  20 | Resources for learning Kedro include its official documentation, which offers examples and a get-started kit, as well as videos available on YouTube.                                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/wtFsapyNmNQ/hqdefault.jpg)](https://www.youtube.com/watch?v=wtFsapyNmNQ)

[Watch on YouTube](https://www.youtube.com/watch?v=wtFsapyNmNQ)
