---
layout: default
title: "Stanford CME295 Transformers & LLMs | Autumn 2025 | Lecture 7 - Agentic LLMs"
nav_order: 7
parent: "Stanford CME295: Transformers and Large Language Models I Autumn 2025"
type: Video Note
description: "Lecture 7 of CME 295 focuses on enabling Large Language Models (LLMs) to interact with external systems by covering Retrieval-Augmented Generation (RAG), tool calling, and agentic workflows."
resource: "https://www.youtube.com/watch?v=h-7S6HNq0Vg"
tags:
  - stanford-cme295-transformers-and-large-language-models-i-autumn-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T20:43:47+00:00
---

# Summary

Lecture 7 of CME 295 focuses on enabling Large Language Models (LLMs) to interact with external systems by covering Retrieval-Augmented Generation (RAG), tool calling, and agentic workflows.
The lecture begins by addressing the limitations of static LLM knowledge, explaining how RAG overcomes knowledge cutoffs and context length constraints by retrieving relevant documents from a knowledge base using embedding-based similarity search and cross-encoder reranking.
It details the technical components of RAG, including chunking strategies, hyperparameter tuning, and evaluation metrics such as NDCG and MRR, while also discussing hybrid retrieval methods that combine semantic search with keyword-based approaches like BM25.
The second part of the lecture introduces tool calling, where LLMs are trained via supervised fine-tuning or prompt engineering to select and execute external functions, such as API calls, to perform actions or retrieve real-time data.
Finally, the lecture explores agentic systems, defined as autonomous loops of observation, planning, and action that allow LLMs to decompose complex tasks into sub-steps, while also addressing critical safety concerns, standardization protocols like MCP, and the challenges of error propagation in multi-step reasoning.

# Main Points

|   # | Main point                                                                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lecture 7 of CME 295 focuses on practical techniques for LLMs to interact with external systems, specifically Retrieval-Augmented Generation (RAG), tool calling, and agents.                                        |
|   2 | The lecture recaps reasoning models and the GRPO algorithm, noting that GRPO does not train a value function and uses group-relative advantages to improve reasoning tasks like math and coding.                     |
|   3 | A length bias phenomenon was identified in GRPO where output length increases even as performance plateaus, with mitigation strategies including DAPo and removing normalization terms.                              |
|   4 | Vanilla LLMs have knowledge cutoff dates, limiting their ability to answer questions about recent events, and retraining to update knowledge is impractical due to regression risks and maintenance overhead.        |
|   5 | Injecting all new information into the prompt is inefficient due to limited context windows, performance degradation from irrelevant information (needle-in-a-haystack problem), and high per-token costs.           |
|   6 | RAG addresses these limitations by retrieving relevant documents from a knowledge base to augment the prompt, consisting of three steps: retrieve, augment, and generate.                                            |
|   7 | Building a RAG knowledge base involves chunking documents into segments of hundreds of tokens, computing embeddings for each chunk, and tuning hyperparameters like embedding size, chunk size, and overlap.         |
|   8 | Retrieval typically uses a two-stage approach: candidate retrieval using semantic similarity search (e.g., cosine similarity) to filter candidates, followed by optional ranking to refine the top results.          |
|   9 | Candidate retrieval leverages encoder-only models like Sentence-BERT to compute embeddings, while ranking may use cross-encoder setups that process the query and chunk together for more accurate relevance scores. |
|  10 | Hybrid retrieval methods combine embedding-based semantic search with heuristic keyword matching (e.g., BM25) to ensure both semantic relevance and exact keyword presence.                                          |
|  11 | Techniques like HyDE generate a fake document from the query to improve embedding similarity, and prompt caching reduces costs by reusing activations for repeated prompt prefixes.                                  |
|  12 | Evaluation metrics for RAG include NDCG, MRR, Precision at K, and Recall at K, with benchmarks like MTEB used to assess retriever performance.                                                                       |
|  13 | Tool calling allows LLMs to access external resources and perform actions by dynamically invoking predefined functions, overcoming knowledge gaps and enabling real-time data access.                                |
|  14 | Tool calling workflows involve the LLM selecting the appropriate function and arguments, executing the function externally, and using the structured output to generate a natural language response.                 |
|  15 | Training for tool calling can be achieved through supervised fine-tuning (SFT) with specific input-output pairs or by using reasoning models to generate detailed explanations for tool usage without extensive SFT. |
|  16 | Tool selection is necessary when managing many tools to avoid context window saturation and confusion, often implemented via a router or selector that filters relevant tools before execution.                      |
|  17 | The Model Context Protocol (MCP) standardizes how tools are exposed to LLMs, defining servers, tools, prompts, and resources to facilitate interoperability between different systems.                               |
|  18 | Agents are systems that autonomously pursue goals through iterative loops of observation, planning, and action, differing from simple tool calls by their ability to reason and adapt over multiple steps.           |
|  19 | The ReAct framework decomposes complex tasks into atomic steps of thinking, observing, and acting, allowing agents to refine their approach based on intermediate results.                                           |
|  20 | Multi-agent systems require communication protocols like Google's Agent-to-Agent protocol to standardize how agents expose skills and coordinate actions.                                                            |
|  21 | Safety concerns in agentic systems include data exfiltration and unauthorized actions, necessitating training-time harmlessness measures and inference-time safeguards like safety classifiers.                      |
|  22 | Building effective agents requires starting with simple cases, using capable models to establish baselines, and leveraging reasoning chains for debugging and optimization.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/h-7S6HNq0Vg/hqdefault.jpg)](https://www.youtube.com/watch?v=h-7S6HNq0Vg)

[Watch on YouTube](https://www.youtube.com/watch?v=h-7S6HNq0Vg)
