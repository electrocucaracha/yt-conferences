---
type: Video Note
title: "Keynote: Navigating Primitives for Agent Collaboration - Nick Aldridge, Co-founder & CEO, Mousecat"
description: "Nick Aldridge, a former AWS principal engineer and current startup founder, reflects on the evolution of agent interactions since the first MCP summit. He describes how early language models enabled basic chat and Q&A, leading to more compl..."
resource: https://www.youtube.com/watch?v=1HhfFkFQrn8
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Nick Aldridge, a former AWS principal engineer and current startup founder, reflects on the evolution of agent interactions since the first MCP summit.
He describes how early language models enabled basic chat and Q&A, leading to more complex workflow automation and the widespread development of tools for agents, which created redundancy and motivated the creation of MCP—a protocol for sharing tools and standardizing agent interactions.
Aldridge compares approaches like CLI-based tool use, which is context-efficient and composable but poses security and integration challenges, with MCP, which offers better security, birectional communication, and easier integration but can suffer from context bloat and lacks composability.
He introduces "skills" as a way to provide agents with dynamic, progressively disclosed instructions, noting their compatibility with MCP but current lack of shareability.
Aldridge suggests that MCP could be improved by adopting progressive disclosure, composability, and skill integration, and encourages community contributions to the protocol.
He concludes by recommending MCP for enterprises due to its security, while advising developers to use whatever approach is most convenient.
# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nick Aldridge, former AWS principal engineer and core maintainer, now working on AI-enabled fraud at a startup.                   |
|   2 | Discusses evolution from early GPT chat models to Q&A and RAG applications.                                                       |
|   3 | Companies began automating workflows using LLMs, with tools like Langchain and Langraph.                                          |
|   4 | Tool and function calling became possible as models improved, leading to widespread tool development for agents.                  |
|   5 | Problem emerged: everyone was building the same tools (e.g., Google, Salesforce, Confluence integrations).                        |
|   6 | MCP was created to enable tool sharing and define a protocol for agent interactions.                                              |
|   7 | Code generation models have advanced, allowing models to generate and execute code efficiently.                                   |
|   8 | Using CLIs is context-efficient and composable, allowing code outputs to be piped together.                                       |
|   9 | CLIs provide a unified interface for humans and machines, leveraging existing APIs and tools.                                     |
|  10 | Downsides of CLIs: security risks (remote code execution), integration overhead, dependency bloat.                                |
|  11 | MCP offers bidirectionality, strong semantics (elicitation), easy integration, standardized authorization, and improved security. |
|  12 | Downsides of MCP: requires building/maintaining servers, risk of context bloat, not easily composable.                            |
|  13 | Skills have emerged as a way to provide agents with instructions and context for complex operations.                              |
|  14 | Skills enable progressive disclosure, revealing information only when needed.                                                     |
|  15 | Skills are not currently sharable or integrated with MCP servers.                                                                 |
|  16 | Opportunities to improve MCP: add progressive disclosure, support composability (piping tools), and integrate skills.             |
|  17 | Encourages community contributions to MCP protocol improvements.                                                                  |
|  18 | Enterprises should prefer MCP for security and curation; developers should use whatever is easiest.                               |
|  19 | Invitation to discuss AI-enabled fraud after the talk.                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1HhfFkFQrn8)