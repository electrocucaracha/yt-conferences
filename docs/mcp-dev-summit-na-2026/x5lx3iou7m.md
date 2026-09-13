---
type: Video Note
title: "Context Middleware for MCP: From Enterprise Needs To Protocol Extension - Peder Holdgaard Pedersen"
description: "Peter, an MCP maintainer and developer at Saxo Bank, discusses the evolution of context middleware in AI systems, reflecting on the earlier popularity of retrieval-augmented generation (RAG) and its limitations, particularly in ensuring acc..."
resource: https://www.youtube.com/watch?v=-X5lx3IOu7M
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Peter, an MCP maintainer and developer at Saxo Bank, discusses the evolution of context middleware in AI systems, reflecting on the earlier popularity of retrieval-augmented generation (RAG) and its limitations, particularly in ensuring accuracy and compatibility across different systems.
He shares his experience proposing an "augmentations" capability for MCP to better handle context injection and middleware needs, which was initially rejected but has since become more relevant as AI agents and multi-agent systems have grown more complex.
Peter highlights the importance of standardized middleware—such as validation, mutation, and observability interceptors—to provide guardrails, manage sensitive data, and enable flexible, composable pipelines for enterprise and agentic use cases.
He describes a new proposal for protocol-level middleware that allows for easy integration and configuration of these interceptors, aiming to address the current fragmented ecosystem and improve security, compliance, and developer experience.
Peter encourages community engagement with the proposal, emphasizing that standardizing middleware will benefit platform teams, AI engineers, and enterprises by making advanced context management more accessible and robust.
# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Peter is an MCP maintainer and developer at Saxo Bank, previously worked in game development.                                        |
|   2 | Used images of Saxo Bank offices in the presentation.                                                                                |
|   3 | Discussed the history and limitations of RAG (Retrieval Augmented Generation) systems.                                               |
|   4 | RAG involved chunking data, vector embedding, similarity search, reranking, and context injection.                                   |
|   5 | RAG was popular before advanced models and tool use; sometimes led to counterproductive results.                                     |
|   6 | Proposed "augmentations" in MCP to support RAG-like context injection, but the proposal was rejected.                                |
|   7 | Community preferred resource templates over augmentations.                                                                           |
|   8 | Porting RAG systems between chat/agent systems is difficult due to incompatibility.                                                  |
|   9 | Shared a story about a chatbot in financial services that sometimes hallucinated answers and citations.                              |
|  10 | Hallucination detection was implemented by checking if cited links existed; rerunning the model often fixed hallucinations.          |
|  11 | Middleware could have helped integrate hallucination detection into MCP.                                                             |
|  12 | Modern agents are more complex, use tools, and pass context in/out without direct user messages.                                     |
|  13 | Mentioned Gas Town as an example of complex multi-agent systems.                                                                     |
|  14 | Emphasized the need for guardrails and middleware in advanced agent systems.                                                         |
|  15 | Many gateways and SDKs implement middleware-like features, but naming and standards vary.                                            |
|  16 | Proposed a new middleware extension for MCP, introducing three protocol-level interceptors: validation, mutation, and observability. |
|  17 | Validation interceptors check context and return pass/fail; can be used for hallucination detection or data contract checks.         |
|  18 | Mutation interceptors transform payloads (e.g., inject RAG context, handle PII, progressive disclosure).                             |
|  19 | Observability interceptors run in parallel for monitoring or sidecar tasks (e.g., sentiment analysis).                               |
|  20 | Middleware extension allows interceptors to be discovered, ordered, and composed in pipelines.                                       |
|  21 | Use cases include PII redaction, auditing, API key validation, content guardrails, and inje Ratings (1-5): 4                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-X5lx3IOu7M)