---
layout: default
title: "Building Scalable AI Tool Servers with Model Context Protocol (MCP) and Heroku (Sponsor: Heroku)"
nav_order: 73
parent: PyCon US 2025
type: Video Note
description: This presentation by Ken Alger and Hillary Sanders from Heroku explores the Model Context Protocol (MCP) as a standardized framework for enabling Large Language Models (LLMs) to interact with exter...
resource: "https://www.youtube.com/watch?v=01I4ywanRDc"
youtube_stats:
  view_count: 954
  like_count: 10
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

This presentation by Ken Alger and Hillary Sanders from Heroku explores the Model Context Protocol (MCP) as a standardized framework for enabling Large Language Models (LLMs) to interact with external tools, addressing the previous lack of interoperability in AI agent development.
The speakers explain that MCP uses JSON-RPC 2.0 to define consistent request and response structures, allowing LLMs to reliably call tools and interpret results without custom integration code for each specific API.
They highlight Python as an ideal language for building MCP-compliant tool servers due to its rich ecosystem, readability, and frameworks like FastAPI and the official MCP Python package, which simplify the creation of modular and maintainable server logic.
A live demonstration showcases the deployment of a Python-based MCP code execution server on Heroku, illustrating how the platform’s Platform-as-a-Service features simplify infrastructure management, horizontal scaling, and logging.
The demo covers various MCP transport modes, including stdio, Server-Sent Events (SSE), and stateless streamable HTTP, while emphasizing security best practices such as isolating arbitrary code execution in one-off dynos to prevent prompt injection attacks and malware risks.
Additionally, the session introduces Heroku’s new AI plugin, which automates tool registration and execution, allowing developers to connect LLMs to secure, scalable tool servers with minimal manual orchestration.
The talk concludes with a Q&A session clarifying that LLMs generate text requests rather than executing tools directly, and that the application layer is responsible for securely handling tool invocations and permissions.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Model Context Protocol (MCP) standardizes communication between LLMs and external tools to replace chaotic, custom integrations.                                   |
|   2 | MCP acts as a universal translator, defining a standardized format for AI applications to request actions and receive responses from tools.                            |
|   3 | Key benefits of MCP include consistency in request-response structures, flexibility in tool implementation, and ease of integrating new compliant tools.               |
|   4 | MCP uses JSON-RPC 2.0 as its wire format, with requests containing tool names and parameters, and responses including content and error status.                        |
|   5 | The connection lifecycle involves initiation, request-response cycles, and termination, supporting both stateless and stateful transport types like HTTP and SSE.      |
|   6 | Python is recommended for building MCP tool servers due to its rich ecosystem, readability, and frameworks like FastAPI and the MCP Python package.                    |
|   7 | Implementing MCP endpoints in Python involves defining routes, parsing JSON requests, using Pydantic for validation, and routing to specific tool logic.               |
|   8 | Tool-specific logic should be abstracted from MCP request handling to keep servers modular and easy to extend with new tools.                                          |
|   9 | Scalability is critical for MCP tool servers to prevent slow responses, timeouts, and crashes as traffic increases.                                                    |
|  10 | Horizontal scaling, or scaling out, involves adding more application instances and using a load balancer to distribute traffic evenly.                                 |
|  11 | Heroku simplifies deployment and scaling of Python MCP servers by handling infrastructure, containerization via buildpacks, and offering dashboard-based scaling.      |
|  12 | A demo showcased deploying a Python code execution MCP server to Heroku using an app.json file and a Procfile for configuration.                                       |
|  13 | The demo utilized the MCP Python package to define tools and attach them to an MCP server, supporting both stdio and SSE transport modes.                              |
|  14 | Local testing demonstrated listing tools and executing code via stdio and SSE clients, verifying standardized input schemas generated from docstrings.                 |
|  15 | Deploying the server to Heroku allowed interaction via a public URL, enabling remote tool calls and demonstrating horizontal scaling capabilities.                     |
|  16 | Security concerns were highlighted regarding running arbitrary code on shared multi-tenant servers, recommending isolation for untrusted inputs.                       |
|  17 | Heroku’s AI plugin allows registering MCP tools and executing them in isolated one-off dynos, preventing resource contention and security risks.                       |
|  18 | The V1 agents endpoint automates the tool-calling loop, injecting tool schemas and handling execution without manual client-side orchestration.                        |
|  19 | LLMs do not execute tools directly; they generate text requests that application code or platforms like Heroku interpret and execute securely.                         |
|  20 | Authentication and permissions should be managed at the application layer, keeping credentials away from the LLM to prevent prompt injection attacks.                  |
|  21 | When multiple MCP servers are available, the LLM determines which tools to call based on the provided schemas and context.                                             |
|  22 | Heroku supports integrating MCP servers with external clients like Visual Studio Code and provides built-in tools for tasks like reading PDFs and accessing databases. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/01I4ywanRDc/hqdefault.jpg)](https://www.youtube.com/watch?v=01I4ywanRDc)

[Watch on YouTube](https://www.youtube.com/watch?v=01I4ywanRDc)
