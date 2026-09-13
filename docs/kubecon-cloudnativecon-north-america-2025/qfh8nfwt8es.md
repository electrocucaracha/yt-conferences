---
layout: default
title:
  "Lightning Talk: Summarizing the Noise: LLM Observability With Open Data Hub,
  VLLM... Twinkll Sisodia"
nav_order: 152
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Twinkle Sodia, a senior software engineer at Red Hat, presents an open-source
  solution her team developed to address the challenges of monitoring AI workloads,
  which often involve navigating complex metric dashboards and require expertise i...
resource: https://www.youtube.com/watch?v=QFH8nfWt8Es
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Twinkle Sodia, a senior software engineer at Red Hat, presents an open-source solution her team developed to address the challenges of monitoring AI workloads, which often involve navigating complex metric dashboards and require expertise in promql.
Their system collects observability data from sources like Prometheus, Tempo, and Loki, and uses an AI-powered MCP server integrated with tools such as Llama Stack and Open Data Hub to generate actionable insights.
The platform correlates metrics, logs, and traces, enabling users—including those without operational expertise—to receive statistical analyses, trend reports, and recommended actions through a user-friendly Streamlit UI.
Additionally, it features a natural language interface that translates user queries into promql, allowing direct interaction with data sources for real-time troubleshooting and business context.
The solution aims to simplify AI infrastructure monitoring, making insights accessible to both engineers and business users, and is available for collaboration on GitHub.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Complex metric dashboards for AI workloads are time-consuming and challenging, especially for those unfamiliar with promql.                                             |
|   2 | The team built an open-source solution that gathers observability data from Prometheus, Tempo, and Loki, transforming it into AI-powered insights.                      |
|   3 | Developed an MCP server and integrated Llama Stack, Open Data Hub, and KServe for model deployment.                                                                     |
|   4 | Integrated Prometheus, Tempo, and Loki for observability data points.                                                                                                   |
|   5 | Used Correlator to correlate all collected data points.                                                                                                                 |
|   6 | The solution aims to provide instant AI-powered insights for non-ops users and correlate all data points for better understanding.                                      |
|   7 | Created an AI-powered observability system that analyzes and correlates data, providing statistical analysis and reports beyond basic averages.                         |
|   8 | Implemented a feature to chat with Prometheus and other data sources using natural language, which is converted to promql for querying.                                 |
|   9 | In a Kubernetes environment, Open Data Hub uses KServe and VLM to deploy the Llama 8 billion model.                                                                     |
|  10 | Data sources include Prometheus, Tempo, Loki, and Alert Manager.                                                                                                        |
|  11 | The application is deployed in a namespace with Streamlit UI, MCP server, controller, Llama Stack, and Correlator.                                                      |
|  12 | The MCP server gathers and correlates metrics, logs, and traces, builds a dynamic prompt, and sends it to a large language model for analysis.                          |
|  13 | The Streamlit UI allows users to select namespace, model, and time period, then generates a report with performance summary, trends, patterns, and recommended actions. |
|  14 | The chat feature enables users to ask questions in natural language (e.g., GPU usage, pod status), returning both answers and the promql used.                          |
|  15 | The system provides both engineering/debugging details and business context, benefiting technical and business users.                                                   |
|  16 | GitHub repository is available for those interested in contributing or exploring the project.                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QFH8nfWt8Es)
