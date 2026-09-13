---
type: Video Note
title: "[Session] Next Generation Agent Architectures with MCP with Darren Shepherd from Acorn Labs"
description: "The speaker, a co-founder at Acorn Labs with a background in automation and orchestration, discusses the challenges of building AI agents and how the MCP (Message Control Protocol) architecture simplifies the process. He explains that while..."
resource: https://www.youtube.com/watch?v=z4vgc3lFMYM
tags: ["mcp-dev-summit-na-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a co-founder at Acorn Labs with a background in automation and orchestration, discusses the challenges of building AI agents and how the MCP (Message Control Protocol) architecture simplifies the process.
He explains that while agent architectures are conceptually straightforward, in practice they often become overly complex, especially when implemented in Python or TypeScript.
MCP helps by standardizing the connection between large language models (LLMs) and tools, making it easier to build modular, declarative agents where most functionalities can be treated as tool calls.
Through live demos, he shows how simple agents and workflows can be constructed using MCP, including dynamic instructions and browser automation, and introduces his experimental project "nanobot" as an example.
He concludes that with MCP, building agents is becoming much easier for traditional software engineers, and predicts that 2025 will be a significant year for agent development, though improvements like structured outputs and better distributed tracing would further help the ecosystem.
# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is co-founder at Acorn Labs, previously co-founded Rancher and created K3S.                                     |
|   2 | Focuses on automation and orchestration, prefers autonomous agents over interactive AI.                                 |
|   3 | Finds building agents conceptually simple but practically difficult, especially due to Python code complexity.          |
|   4 | Anthropic and OpenAI provide good agent architecture guides; main missing elements are guardrails and LLM instructions. |
|   5 | MCP (Message Control Protocol) standardizes the connection between LLMs and tools, acting as a middleman.               |
|   6 | Retrieval and memory in agent architectures can be handled as tool calls via MCP.                                       |
|   7 | Sampling can also be managed through MCP, simplifying agent architecture.                                               |
|   8 | MCP enables modular agent components, making it easier to build agents by connecting code blocks.                       |
|   9 | Agentic patterns are essentially code and can be implemented as tools.                                                  |
|  10 | Demonstrated a simple MCP server and tool (echo tool) to show basic sampling and tool calling.                          |
|  11 | Most clients do not support sampling, so speaker created "nanobot" to experiment with these ideas.                      |
|  12 | Nanobot allows running agents as tools, supporting sampling and tool calls.                                             |
|  13 | Reimplemented OpenAI's research bot example using MCP and TypeScript, defining planner, search, and response agents.    |
|  14 | Agents are defined declaratively with instructions, tools, and models.                                                  |
|  15 | Demonstrated browser automation using MCP and Playwright as a tool.                                                     |
|  16 | Dynamic instructions and prompt templating can be handled with MCP server prompts.                                      |
|  17 | MCP servers can be combined with minimal code to create agents for various tasks.                                       |
|  18 | Coding agents like OpenAI Codex can be replicated with simple MCP-based scripts.                                        |
|  19 | MCP makes building agents easier for traditional software engineers.                                                    |
|  20 | Suggests improvements for MCP: JSON schema output for create message and built-in distributed tracing.                  |
|  21 | Nanobot tool is available at nanobot.ai for experimentation.                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=z4vgc3lFMYM)