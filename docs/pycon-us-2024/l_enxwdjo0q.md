---
layout: default
title: "Sponsor Presentations - Build an Intelligent Python App, No Infra Hassles! (Sponsor: Microsoft)"
nav_order: 47
parent: PyCon US 2024
type: Video Note
description: "In this session, Devanshi Joshi and Anthony demonstrate how to build and deploy an intelligent Python RAG application using Azure services, starting with a local setup powered by LangChain, Chainli..."
resource: "https://www.youtube.com/watch?v=L_enXWDjO0Q"
youtube_stats:
  view_count: 437
  like_count: 6
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

In this session, Devanshi Joshi and Anthony demonstrate how to build and deploy an intelligent Python RAG application using Azure services, starting with a local setup powered by LangChain, Chainlit, and the Qdrant vector database.
They illustrate the process of ingesting PDF documents into a vector store to enable context-aware chatbot responses and explain how to transition the application to the cloud using Azure Container Apps, which provides serverless compute for both the web UI and file indexing jobs.
A key security focus is the use of managed identities to eliminate the need for static API keys, ensuring fine-grained access control to Azure OpenAI.
The presentation also addresses the risks of prompt injection and performance bottlenecks associated with running LLM-generated code locally, introducing Azure Container Apps Dynamic Sessions as a secure, isolated, and scalable sandbox for executing Python code in the cloud.
By integrating Dynamic Sessions with the application, the team shows how to safely process uploaded data files and execute complex queries while maintaining high performance and robust security postures for production environments.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The session demonstrates building a Python RAG application with a chat interface powered by LLMs using LangChain and Chainlit.                         |
|   2 | The application uses Azure OpenAI as the LLM and Qdrant as the vector database to store document embeddings.                                           |
|   3 | A Python script parses PDFs, chunks them, calculates embeddings, and stores them in the vector database for retrieval.                                 |
|   4 | Local execution utilizes Docker for the vector database and Chainlit for the chat interface, with authentication handled via Default Azure Credential. |
|   5 | The architecture employs a ReAct agent that uses a retriever tool to query the vector database for relevant information.                               |
|   6 | Deployment to Azure Container Apps involves running the chat UI as a continuous app and the file indexer as a job.                                     |
|   7 | Azure Container Apps offers serverless compute with features like scale-to-zero, pay-per-use billing, and native vector database add-ons.              |
|   8 | Managed Identity is used for secure authentication to Azure OpenAI, eliminating the need for static API keys in environment variables.                 |
|   9 | The application can be deployed without manual containerization using the `az containerapp up` command, which automates environment and app creation.  |
|  10 | A Python REPL tool is added to the agent to enable data analysis capabilities, such as processing CSV files with pandas.                               |
|  11 | The agent selects tools based on their descriptions, allowing it to decide between searching documents or executing code.                              |
|  12 | Security risks such as prompt injection are demonstrated, where malicious prompts can attempt to expose environment variables.                         |
|  13 | Azure Container Apps Dynamic Sessions provide secure, isolated sandboxes for executing LLM-generated code in the cloud.                                |
|  14 | Dynamic Sessions use Hyper-V isolation and maintain a pool of interpreters to ensure fast execution and scalability.                                   |
|  15 | Integrations for Dynamic Sessions are available for LangChain, LlamaIndex, and Semantic Kernel, allowing seamless replacement of local REPL tools.     |
|  16 | Files uploaded to the chat interface can be stored within a Dynamic Session for secure processing by the code interpreter.                             |
|  17 | The solution addresses production concerns including security, performance, and lifecycle management of code execution environments.                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/L_enXWDjO0Q/hqdefault.jpg)](https://www.youtube.com/watch?v=L_enXWDjO0Q)

[Watch on YouTube](https://www.youtube.com/watch?v=L_enXWDjO0Q)
