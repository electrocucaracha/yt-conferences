---
layout: default
title: "Enterprise-Ready Python for High-Performance Data Teams (Sponsor: Snowflake)"
nav_order: 69
parent: PyCon US 2025
type: Video Note
description: "At PyCon, Savannah and Doris from Snowflake presented a comprehensive overview of how the platform integrates with the Python data ecosystem to support enterprise-scale workflows."
resource: "https://www.youtube.com/watch?v=o2JUXACkv4k"
youtube_stats:
  view_count: 1031
  like_count: 13
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

At PyCon, Savannah and Doris from Snowflake presented a comprehensive overview of how the platform integrates with the Python data ecosystem to support enterprise-scale workflows.
They introduced "pandas on Snowflake," a solution built on the open-source Modin project that allows developers to use familiar pandas APIs while pushing compute down to Snowflake’s engine, thereby eliminating memory limitations and achieving up to 30x faster performance on large datasets.
The session detailed the use of Snowflake Notebooks as an all-in-one environment for blending SQL and Python, enabling seamless data exploration and model development without infrastructure management.
Additionally, they highlighted the Snowflake container runtime, which provides managed access to GPUs and pre-installed machine learning packages, facilitating distributed training for frameworks like PyTorch and XGBoost with significant speed improvements over standard open-source setups.
Finally, the speakers demonstrated how to deploy interactive dashboards using Streamlit within Snowflake and automate model retraining, offering a secure, governed, and end-to-end solution for building, scaling, and sharing data-driven applications.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Slides and code examples are available on a GitHub repository accessible via QR codes displayed during the presentation.                                                          |
|   2 | Savannah is a Python core developer maintaining the JIT compiler and argparse module, currently working at Snowflake on notebooks and Python developer experience.                |
|   3 | Doris has a background in astrophysics and data science tools, co-founded Ponder (acquired by Snowflake), and works on Modin and pandas on Snowflake.                             |
|   4 | Snowflake is a full data ecosystem supporting build, run, and share of data applications, including native Python support and a content network for third-party data and apps.    |
|   5 | The platform offers Snowflake Notebooks for interactive exploration, Snowpark for Python-based data processing, and Streamlit in Snowflake for deploying interactive data apps.   |
|   6 | Snowflake embraces open standards, allowing users to connect via external IDEs like Visual Studio Code or Jupyter and use familiar APIs like pandas and Spark.                    |
|   7 | Pandas on Snowflake provides a unified interface to access Snowflake data using the pandas API, enabling lazy evaluation to avoid loading large datasets into memory.             |
|   8 | Traditional pandas is limited by in-memory constraints and single-threading, often causing out-of-memory errors or slow performance on enterprise-scale data.                     |
|   9 | Modin is an open-source distributed pandas implementation that acts as a drop-in replacement, improving performance through parallel execution.                                   |
|  10 | Pandas on Snowflake is built on Modin, transpiling pandas operations to SQL for execution on the Snowflake engine, achieving up to 30x faster performance on 10GB datasets.       |
|  11 | Benchmarks show pandas on Snowflake can process terabytes of data in under a minute, significantly outperforming traditional pandas on large workloads.                           |
|  12 | Support for the DataFrame Interchange Protocol enables interoperability with libraries like Plotly, Scikit-learn, and NumPy within the Snowflake environment.                     |
|  13 | Snowflake Notebooks allow seamless blending of SQL and Python cells, enabling variable sharing and eliminating the need to switch between tools.                                  |
|  14 | Streamlit in Snowflake facilitates the creation of interactive dashboards and reports, allowing real-time model updates and secure sharing with stakeholders.                     |
|  15 | Common enterprise ML challenges include balancing cost and performance, scalability, reproducibility, and managing GPU infrastructure.                                            |
|  16 | Snowflake ML provides a three-layer architecture: ML development (Notebooks), ML APIs for accelerated training, and a container runtime for scalable execution.                   |
|  17 | The container runtime is built on Snowpark Container Services and Ray, offering pre-installed ML packages like PyTorch and TensorFlow, with automatic scaling.                    |
|  18 | Users can select GPU or CPU resources in Snowflake Notebooks without manual cluster provisioning or driver configuration.                                                         |
|  19 | The data connector API uses Ray to load data in parallel, reducing data loading time from nearly 9.5 minutes to 50 seconds for 81GB datasets.                                     |
|  20 | Distributed trainers for PyTorch, XGBoost, and LightGBM are supported, with XGBoost workloads running 3 to 7 times faster than open-source equivalents.                           |
|  21 | Notebooks can be scheduled for automated execution, ensuring models are retrained on the latest data without manual intervention.                                                 |
|  22 | Snowflake provides governance and security features, allowing admins to control access to notebooks, models, and data assets.                                                     |
|  23 | The platform supports open formats like Iceberg and integrates with the broader Python ecosystem to reduce tool sprawl and infrastructure management.                             |
|  24 | Snowflake differentiates from competitors like Databricks by keeping data and compute in a governed environment, avoiding IO costs associated with moving data between platforms. |
|  25 | Users can install additional packages via pip within the container runtime, extending the pre-installed set of 50+ Python data packages.                                          |
|  26 | The Snowpark ecosystem compiles Python code to SQL for execution on the Snowflake engine, ensuring security and scalability while maintaining familiar syntax.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/o2JUXACkv4k/hqdefault.jpg)](https://www.youtube.com/watch?v=o2JUXACkv4k)

[Watch on YouTube](https://www.youtube.com/watch?v=o2JUXACkv4k)
