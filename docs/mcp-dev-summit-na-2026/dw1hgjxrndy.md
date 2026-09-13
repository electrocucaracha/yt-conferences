---
type: Video Note
title: "MCP at 18 Months: Protocols, Patterns, and What We Didn't See Coming - Shaun Smith, Hugging Face"
description: "Sean Smith from Hugging Face discusses the evolution and impact of the MCP server and related agent technologies. He reflects on the initial limitations of MCP, such as the lack of agentic CLIs, transport solutions, and long-running model c..."
resource: https://www.youtube.com/watch?v=DW1hGJXrNdY
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Sean Smith from Hugging Face discusses the evolution and impact of the MCP server and related agent technologies.
He reflects on the initial limitations of MCP, such as the lack of agentic CLIs, transport solutions, and long-running model capabilities, and explains how advancements like reinforcement learning have enabled models to perform complex, multi-step tasks.
Smith highlights the growing sophistication of tool integration, dynamic tool calling, and code execution within agent frameworks, emphasizing the importance of protocols like the Agent Client Protocol and Open Responses API for bundling inference engines and tools.
He notes that MCP has achieved strong product-market fit, especially for consumer and enterprise use cases, due to its ease of integration, authentication, and support for regulatory needs.
Ultimately, Smith concludes that MCP has matured into essential infrastructure, facilitating seamless transportability and composability in modern AI systems.
# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | Sean Smith from Hugging Face manages MCP server, is an NCP maintainer, and maintains the open-source fast agent.        |
|   2 | Attended a "funeral" for MCP, suggesting its evolution or end.                                                          |
|   3 | The debate around MCP is more interesting than MCP itself.                                                              |
|   4 | At MCP launch, key features were missing: agentic CLIs, cloud code, remote transport, agent/skills agreement, and APIs. |
|   5 | Early models couldn't conduct long-running tasks; now, models handle chains of 80-100 tool calls.                       |
|   6 | Model improvements driven by reinforcement learning in post-training, enabling goal-driven, long-sequence tasks.        |
|   7 | Meta's Open library supports reinforcement experiments.                                                                 |
|   8 | SWE bench benchmark: minimal harnesses with small codebases can achieve 76-80% on software engineering tasks.           |
|   9 | Smarter models enable dynamic tool routes, improved harnesses, and better skill utilization.                            |
|  10 | Dynamic tool calling allows access to thousands of ML models at Hugging Face with minimal token cost.                   |
|  11 | NCP enables models to write and call their own tool descriptions, supports authentication, and multimodal support.      |
|  12 | Open-weight stack: models can connect with minimal tokens and small language models.                                    |
|  13 | Models can now execute code, produce tools/utilities, and use shell for dense execution.                                |
|  14 | Modern models can write and execute code natively, often with embedded interpreters.                                    |
|  15 | Blurring boundaries between code generation and execution environments; choice of model and environment is key.         |
|  16 | MCP enables remote execution, local resource access, and fine-tuning for known API surfaces.                            |
|  17 | NCP allows bypassing extra model post-processing, saving output tokens.                                                 |
|  18 | Prefect library enables models to generate UI components instead of just JSON.                                          |
|  19 | Runtime and inference environments are blending; context window management is increasingly important.                   |
|  20 | Agent Client Protocol (by Zetra) and Open Responses API are emerging standards for agent-tool integration.              |
|  21 | Open Responses API distinguishes between internal and external tools, supports free-form gra Ratings (1-5): 4           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=DW1hGJXrNdY)