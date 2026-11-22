---
layout: default
title: "Build modern Python apps on Azure (Sponsor: Microsoft)"
nav_order: 74
parent: PyCon US 2025
type: Video Note
description: "At PyCon US 2025, Microsoft’s Python Cloud Advocacy team presented a session on building modern Python applications on Azure, demonstrating the full developer lifecycle using a RAG-based chatbot fo..."
resource: "https://www.youtube.com/watch?v=k6Vm2hakkV4"
youtube_stats:
  view_count: 1344
  like_count: 27
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

At PyCon US 2025, Microsoft’s Python Cloud Advocacy team presented a session on building modern Python applications on Azure, demonstrating the full developer lifecycle using a RAG-based chatbot for Pittsburgh restaurants.
The presentation highlighted the use of Visual Studio Code Dev Containers to create isolated, reproducible development environments with integrated PostgreSQL and vector search capabilities, alongside the newly launched PostgreSQL extension for Visual Studio Code, which offers schema visualization and AI-assisted SQL querying.
The team showcased local development workflows using the AI Toolkit extension to compare LLMs via GitHub Models, and detailed the implementation of a FastAPI backend utilizing the OpenAI Agents SDK for robust tool calling and hybrid search strategies.
They further demonstrated debugging techniques using the Python extension’s ability to step into third-party packages, as well as the use of GitHub Copilot’s agent mode for automated code generation and testing.
Finally, the session covered deploying the application to Azure Container Apps using the Azure Developer CLI and Bicep infrastructure-as-code, followed by load testing with Locust to verify auto-scaling performance and system reliability in the cloud.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The session demonstrates building a modern Python application for querying Pittsburgh restaurant data using Azure and Visual Studio Code.              |
|   2 | The application architecture consists of a React frontend, a FastAPI Python backend, PostgreSQL with pgvector, and the OpenAI Agents SDK.              |
|   3 | Dev Containers are used to create isolated, reproducible development environments with Docker Compose for Python and PostgreSQL.                       |
|   4 | A new prerelease PostgreSQL extension for Visual Studio Code allows users to visualize schemas, execute SQL, and export data to CSV or JSON.           |
|   5 | The extension features an AI chat capability that generates and executes SQL queries, including vector searches, using LLMs like Claude.               |
|   6 | GitHub Models provides free credits for local LLM experimentation without requiring Azure permissions or complex setup.                                |
|   7 | The AI Toolkit extension in Visual Studio Code enables model comparison, parameter tuning, and local model testing via Ollama.                         |
|   8 | The RAG flow involves query rewriting by an LLM, hybrid search combining full-text and vector results, and final answer generation.                    |
|   9 | The OpenAI Agents SDK is used for tool calling, allowing the LLM to generate search queries and structured filters like price or rating.               |
|  10 | Python debugging in Visual Studio Code supports stepping into third-party packages, such as the OpenAI Agents SDK, for detailed code inspection.       |
|  11 | Pytest is used for unit testing, with features for snapshot updates and debugging individual failing tests directly in the IDE.                        |
|  12 | GitHub Copilot Agent Mode is demonstrated to autonomously write new API routes and corresponding tests based on user instructions.                     |
|  13 | Custom instructions for Copilot can be defined in user settings or repository files to enforce specific coding conventions and best practices.         |
|  14 | Deployment to Azure is handled via the Azure Developer CLI using the `azd up` command, which packages, provisions, and deploys resources.              |
|  15 | Infrastructure as Code is defined using Bicep, with the Azure extension for Copilot assisting in writing and visualizing resource configurations.      |
|  16 | Azure AI Foundry extension allows for one-click deployment of models to the cloud, transitioning from local GitHub Models to Azure services.           |
|  17 | The application is deployed to Azure Container Apps, which provides managed Kubernetes scalability without requiring direct Kubernetes administration. |
|  18 | Load testing is performed using the Python-based Locust tool to simulate realistic user behavior and verify application scaling.                       |
|  19 | Azure Container Apps scaling rules are configured to automatically increase replicas based on concurrent HTTP requests during load tests.              |
|  20 | Azure Application Insights is used to monitor server requests, failures, and performance metrics during the load testing phase.                        |
|  21 | The OpenAI Agents SDK was chosen over lower-level APIs to simplify tool validation and enable future support for MCP tool servers.                     |
|  22 | The session concludes with resources for further learning, including links to the demo code, PyCon US 2025 details, and the Microsoft booth.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/k6Vm2hakkV4/hqdefault.jpg)](https://www.youtube.com/watch?v=k6Vm2hakkV4)

[Watch on YouTube](https://www.youtube.com/watch?v=k6Vm2hakkV4)
