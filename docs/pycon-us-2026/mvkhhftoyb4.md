---
layout: default
title: "Inside an AI Agent SDK: Building One from Scratch in Python (Sponsor: SerpApi)"
nav_order: 102
parent: PyCon US 2026
type: Video Note
description: "In this presentation, Adarsh, a Python developer advocate at SerpApi, guides the audience through building an AI agent SDK from scratch in Python to demystify the internal mechanics of AI agents."
resource: "https://www.youtube.com/watch?v=mVkhhFtOyB4"
youtube_stats:
  view_count: 576
  like_count: 2
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

In this presentation, Adarsh, a Python developer advocate at SerpApi, guides the audience through building an AI agent SDK from scratch in Python to demystify the internal mechanics of AI agents.
The talk begins by establishing that while Large Language Models (LLMs) serve as the "brain" of an agent, they are limited by their training data and lack real-time access, necessitating the integration of tools, memory, and decision-making loops to create capable autonomous agents.
The core of the session involves the step-by-step development of a unified Python SDK named "baby agent," which abstracts provider-specific complexities to support OpenAI, Anthropic, and local Ollama models seamlessly.
Key components implemented include a robust agent loop with short-term memory management, a decorator-based system for defining and executing custom tools, and support for the Model Context Protocol (MCP) to standardize external integrations like GitHub and search APIs.
The presentation concludes by introducing "skills" as reusable markdown-based instructions for specialized workflows and drawing architectural parallels between traditional backend development and AI agent design, emphasizing that effective agents require a balanced combination of reasoning, context, and external capabilities.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The presentation covers building an AI agent SDK from scratch in Python, focusing on core components like LLMs, tools, MCP, and skills. |
|   2 | LLMs serve as the brain of AI agents but lack real-time information access, necessitating external tools for current data. |
|   3 | Selecting an LLM involves balancing intelligence benchmarks against cost, with options including hosted models and local open-source models like Gamma 4. |
|   4 | Reasoning effort levels can be adjusted to control token consumption and response time, with higher levels suited for complex tasks. |
|   5 | Context windows represent the model's working memory, allowing for larger codebases or conversations but increasing costs and latency. |
|   6 | System prompts define the agent's personality and behavioral rules, guiding the model to stay within specific domains like PyCon. |
|   7 | Short-term memory is implemented by maintaining a conversation history list that is appended with each user and assistant message. |
|   8 | The "baby agent" SDK uses an abstract base class to support multiple providers like OpenAI and Anthropic through a unified interface. |
|   9 | Provider-specific implementations handle the conversion of internal message formats to API-specific structures for sending requests. |
|  10 | Tools are external capabilities defined as Python functions that the agent can call to perform actions like web searches or API calls. |
|  11 | Tool calling requires the developer to execute the function and append the result back to the conversation history for the model to process. |
|  12 | The SDK includes a tool decorator that automatically converts Python function type annotations into JSON schemas for LLM consumption. |
|  13 | An agent loop manages the interaction cycle, sending requests to the LLM and handling tool calls until a final response is generated. |
|  14 | A safety mechanism called max tool rounds prevents infinite loops if the model repeatedly requests tools without responding. |
|  15 | Model Context Protocol (MCP) acts as a standardized interface for AI integrations, allowing agents to discover and call external server tools automatically. |
|  16 | MCP reduces developer burden by abstracting tool discovery and execution, similar to a USB-C standard for AI capabilities. |
|  17 | Providers like OpenAI and Anthropic natively support MCP, while local models like Ollama require custom workarounds to map MCP tools to native formats. |
|  18 | Skills are plain markdown files containing reusable instructions or workflows that specialize agent behavior without requiring code changes. |
|  19 | Skills provide context to the model for specific tasks, such as using SerpApi for web searches or following best practices for coding. |
|  20 | The agent architecture parallels backend development, with LLMs handling logic, tools acting as APIs, and memory serving as databases. |
|  21 | The final SDK supports a stack of capabilities including agent loops, short-term memory, custom tools, MCP integration, and skill loading. |
|  22 | Unimplemented features in the demo include retries, structured output, and file uploads, which are noted for future development. |
|  23 | The source code for the baby agent SDK is available on GitHub for reference and further exploration. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mVkhhFtOyB4/hqdefault.jpg)](https://www.youtube.com/watch?v=mVkhhFtOyB4)

[Watch on YouTube](https://www.youtube.com/watch?v=mVkhhFtOyB4)
