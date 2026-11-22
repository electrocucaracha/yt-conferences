---
layout: default
title: "Building AI Applications the Pydantic Way (Sponsor: Pydantic)"
nav_order: 64
parent: PyCon US 2025
type: Video Note
description: "Samuel, the creator of Pydantic, presents a talk on building reliable AI applications using the Pydantic ecosystem, specifically highlighting Pydantic AI, Pydantic Logfire, and Pydantic Evals."
resource: "https://www.youtube.com/watch?v=zJm5ou6tSxk"
youtube_stats:
  view_count: 12656
  like_count: 273
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

Samuel, the creator of Pydantic, presents a talk on building reliable AI applications using the Pydantic ecosystem, specifically highlighting Pydantic AI, Pydantic Logfire, and Pydantic Evals.
He emphasizes the critical importance of type safety in Python, arguing that it provides essential feedback for AI coding agents and ensures robust application development, a feature he claims distinguishes Pydantic AI from other agent frameworks.
The presentation demonstrates how Pydantic AI handles structured data extraction and agentic loops, where validation errors are fed back to the LLM to correct outputs, while also showcasing the integration of the Model Context Protocol (MCP) for secure, sandboxed Python execution and browser automation via Playwright.
Additionally, he introduces Pydantic Evals as a framework for systematically testing and improving stochastic AI behaviors, allowing developers to define datasets, use LLM-as-a-judge evaluators, and compare model performance.
Throughout the talk, the speaker underscores the company’s commitment to open standards, such as OpenTelemetry, and promises a stable version 1.0 release to ensure long-term reliability for developers building on these tools.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The speaker is Samuel, creator of Pydantic, which was first created in 2017 and is downloaded approximately 350 million times a month.                                   |
|   2 | Pydantic is widely used by GenAI libraries, including SDKs from OpenAI, Anthropic, and Google, as well as agent frameworks like LangChain and LlamaIndex.                |
|   3 | The company behind Pydantic has developed Pydantic Logfire, a developer-first observability platform, and Pydantic AI, an agent framework.                               |
|   4 | Type safety is emphasized as critical for AI-assisted coding, as type checking provides fast, side-effect-free feedback for AI agents.                                   |
|   5 | The talk defines an agent using a consensus model involving an environment, tools, a system prompt, and an LLM loop that updates state.                                  |
|   6 | A key challenge in agent design is determining when to stop the execution loop, as the standard pseudo-code definition contains an infinite loop bug.                    |
|   7 | Pydantic AI supports model agnosticism, allowing users to switch between different LLM providers with a single line of code.                                             |
|   8 | Structured outputs are achieved by defining a Pydantic model as the output type, which triggers validation and automatic retries if the model fails to meet constraints. |
|   9 | Pydantic Logfire provides observability into the agentic loop, showing how validation errors are fed back to the model to correct outputs.                               |
|  10 | Tools can be registered in Pydantic AI using decorators, with type-safe dependency injection ensuring that context variables are correctly typed and accessible.         |
|  11 | Long-term memory is implemented via tools that interact with a database, such as PostgreSQL, to record and retrieve user-specific information.                           |
|  12 | Short-term memory is managed by including message history in the context window, which is faster than tool-based retrieval for immediate conversational continuity.      |
|  13 | The Model Context Protocol (MCP) is introduced as a standard for connecting agents to external tools, resources, and prompts.                                            |
|  14 | Pydantic AI includes an MCP server for running sandboxed Python code using Pyodide and Deno to ensure isolation from the host system.                                    |
|  15 | This sandboxing approach prevents remote code execution risks associated with less isolated alternatives, such as those used by some competitors.                        |
|  16 | MCP servers can be used to control external applications, such as Playwright for browser automation, allowing agents to navigate sites and extract data.                 |
|  17 | Pydantic Evals is presented as a framework for evaluating stochastic AI applications, functioning similarly to benchmarks rather than simple unit tests.                 |
|  18 | Evaluation datasets can be generated using powerful models to create diverse test cases with expected outputs and specific evaluators.                                   |
|  19 | Evaluators include custom validators and LLM-as-a-judge metrics that assess output quality, such as tone, conciseness, and factual accuracy.                             |
|  20 | Pydantic Evals integrates with Logfire to visualize evaluation results, allowing users to identify failing cases and systematically improve agent behavior.              |
|  21 | The framework supports comparing different models by overriding the model instance in tests to assess performance and cost efficiency.                                   |
|  22 | Pydantic AI is committed to open standards, using OpenTelemetry for data emission to ensure compatibility with various observability platforms.                          |
|  23 | The team plans to release version 1.0 of Pydantic AI by the end of June, adhering to semantic versioning to ensure stability for users.                                  |
|  24 | Documentation quality is prioritized, with all code examples in the docs being unit-tested to ensure they are accurate and runnable.                                     |
|  25 | The framework supports self-hosted models and is working on allowing users to configure custom pricing data for local models in Logfire.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/zJm5ou6tSxk/hqdefault.jpg)](https://www.youtube.com/watch?v=zJm5ou6tSxk)

[Watch on YouTube](https://www.youtube.com/watch?v=zJm5ou6tSxk)
