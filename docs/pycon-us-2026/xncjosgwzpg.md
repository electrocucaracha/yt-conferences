---
layout: default
title: "Distributing AI with Python in the Browser: Edge Inference and Flexibility... - Fabio Pliger"
nav_order: 59
parent: PyCon US 2026
type: Video Note
description: "Fabio, the creator of PyScript and a long-time community member, presents a talk on building AI agents within the browser, shifting focus from simple inference to agentic workflows."
resource: "https://www.youtube.com/watch?v=xncJoSGWZpg"
youtube_stats:
  view_count: 206
  like_count: 1
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

Fabio, the creator of PyScript and a long-time community member, presents a talk on building AI agents within the browser, shifting focus from simple inference to agentic workflows.
He defines an agent as a combination of a model (the brain), tools, context (memory), and a loop that connects them, emphasizing that the LLM does not execute tools itself but instructs the agent to do so.
The presentation features live demos using PyScript and Pyodide to run Python code in the browser, showcasing three scenarios: running models locally via Anaconda Desktop, processing CSV files with local Python tools, and utilizing Chrome’s local folder mounting feature to save data directly to the user’s machine without downloads.
Additionally, he demonstrates Anaconda Agent Studio, a tool for creating and distributing agents, by loading a pre-configured "Snoop the Dev" agent into the browser and running it offline with a local model.
Fabio concludes by discussing the trade-offs of browser-based agents, such as resource constraints and latency, while highlighting the browser’s potential as a powerful medium for distributing secure, installation-free AI applications.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker shifted the talk focus from browser inference to agents due to rapid AI changes and the importance of agentic tools. |
|   2 | An agent is defined as a system comprising four parts: a model (brain), tools (capabilities), context (memory), and a loop connecting them. |
|   3 | In a browser context, the model can run locally via WebLLM/WebGPU, on a local machine via Ollama, or remotely via APIs like Anthropic. |
|   4 | Tools in the browser can include MCP servers, Python code via PyScript/Pyodide, or skills, while context is managed as an array of data. |
|   5 | The agent loop involves the LLM processing prompts and context, requesting tool calls, receiving results, and iterating until a final answer is generated. |
|   6 | The LLM does not execute tools directly but instructs the agent to call them, adding the results back to the context for further processing. |
|   7 | A live demo showcased an agent running in the browser using PyScript and Pyodide to execute Python tools and interact with local files. |
|   8 | The demo utilized three model options: in-browser (Qwen 2.5), local (via Anaconda Desktop), and remote APIs, with the local option highlighted for distribution. |
|   9 | Chrome’s feature to mount local folders into the browser allows agents to read and write directly to the user’s local machine without downloads. |
|  10 | This folder mounting capability acts as a security guardrail, requiring explicit user permission before accessing local files. |
|  11 | Anaconda Agent Studio was used to create and distribute agents, storing agent configurations in local folders with YAML files and context documents. |
|  12 | The browser can load these local agent files to run fully offline, demonstrating the viability of shipping agents without internet connectivity. |
|  13 | Small local models are becoming capable enough for simple tasks, making browser-based agents a viable option for specific use cases. |
|  14 | Trade-offs for browser agents include resource constraints per tab, initial model download latency, and potential limitations on low-end devices or phones. |
|  15 | Combining browser agents with Tauri or similar frameworks offers a path to shipping native applications with agentic capabilities. |
|  16 | The core takeaway is that an agent is fundamentally a loop, and the browser is an effective medium for distributing such loops to users. |
|  17 | The UI for the demo was built using PyScript and Panels, generating dynamic content via DOM and CSS manipulation. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xncJoSGWZpg/hqdefault.jpg)](https://www.youtube.com/watch?v=xncJoSGWZpg)

[Watch on YouTube](https://www.youtube.com/watch?v=xncJoSGWZpg)
