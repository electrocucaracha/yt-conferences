---
type: Video Note
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 7 - Agentic LLMs"
description: "In this lecture, the instructors first recap previous discussions on reasoning models and reinforcement learning algorithms like GRPO, highlighting issues such as length bias and strategies to mitigate it. The main focus then shifts to enab..."
resource: https://www.youtube.com/watch?v=h-7S6HNq0Vg
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this lecture, the instructors first recap previous discussions on reasoning models and reinforcement learning algorithms like GRPO, highlighting issues such as length bias and strategies to mitigate it.
The main focus then shifts to enabling large language models (LLMs) to interact with external systems, starting with retrieval-augmented generation (RAG).
RAG addresses the limitations of LLMs’ static knowledge by retrieving and injecting relevant, up-to-date information from external knowledge bases into prompts, using techniques like chunking, embeddings, candidate retrieval, and reranking, with evaluation metrics such as NDCG and recall.
The lecture then introduces tool calling and function calling, where LLMs use structured APIs to perform tasks like fetching real-time data or executing actions, and discusses training approaches including supervised fine-tuning and prompt engineering.
To manage scalability and context limitations, tool selection methods and standardization protocols like MCP are presented.
Finally, the concept of agents is explored, describing systems that autonomously pursue goals through iterative reasoning and tool use, with examples like the React framework and agent-to-agent communication protocols.
The session concludes with a discussion on safety risks, mitigation strategies, and practical advice for building robust, agentic LLM systems.
# Main Points

|   # | Main point                                                                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Lecture focuses on practical techniques for enabling LLMs to interact with external systems.                                                                                                                 |
|   2 | Recap of previous lecture: reasoning models vs. vanilla LLMs, GRPO (Group Relative Policy Optimization) algorithm, length bias, and mitigation strategies (DAPO, GRPO Done Right).                           |
|   3 | LLMs have knowledge cutoffs and limited context windows, making it hard to access up-to-date information.                                                                                                    |
|   4 | Naively adding all new information to prompts is impractical due to context limits, cost, and performance degradation.                                                                                       |
|   5 | Retrieval Augmented Generation (RAG) addresses this by retrieving only relevant information to augment prompts.                                                                                              |
|   6 | RAG process: 1) Retrieve relevant documents from a knowledge base, 2) Augment the prompt with retrieved info, 3) Generate a response.                                                                        |
|   7 | Knowledge base is built from documents split into chunks, each chunk embedded for semantic search.                                                                                                           |
|   8 | Key hyperparameters: embedding size, chunk size, chunk overlap.                                                                                                                                              |
|   9 | Retrieval is typically a two-stage process: candidate retrieval (maximize recall using embeddings and approximate nearest neighbor search) and ranking/reranking (cross-encoder for fine-grained relevance). |
|  10 | Semantic similarity (e.g., cosine similarity) and keyword-based methods (e.g., BM25) can be combined for hybrid retrieval.                                                                                   |
|  11 | Chunking strategies and contextualization are important for coherence; prompt caching can reduce costs.                                                                                                      |
|  12 | Evaluation metrics: NDCG, MRR, precision@K, recall@K; benchmarks like Massive Text Embedding Benchmark.                                                                                                      |
|  13 | Tool calling/function calling allows LLMs to access external APIs for structured data and actions.                                                                                                           |
|  14 | Tool calls are defined by APIs with documented inputs/outputs; LLMs select and fill arguments, not implementations.                                                                                          |
|  15 | Training for tool use involves SFT pairs for tool prediction and response generation; few-shot and prompt engineering can supplement or replace SFT.                                                         |
|  16 | Tool selection/routing is needed when many tools exist; LLMs or RAG can be used to select relevant tools.                                                                                                    |
|  17 | Standardization efforts like MCP (Model Context Protoc                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=h-7S6HNq0Vg)