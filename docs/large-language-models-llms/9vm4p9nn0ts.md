---
type: Video Note
title: "Stanford CS229 I Machine Learning I Building Large Language Models (LLMs)"
description: "The lecture provides an overview of how large language models (LLMs) like ChatGPT, Claude, and Gemini are built and trained. It begins by outlining the key components involved: architecture, training loss and algorithms, data, evaluation, a..."
resource: https://www.youtube.com/watch?v=9vM4p9NN0Ts
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The lecture provides an overview of how large language models (LLMs) like ChatGPT, Claude, and Gemini are built and trained.
It begins by outlining the key components involved: architecture, training loss and algorithms, data, evaluation, and systems, emphasizing that while academia often focuses on architecture, in practice, data, evaluation, and systems are most critical.
The speaker explains the pre-training process, where models learn to predict the next word in a sequence using vast internet data, and discusses the importance of tokenization for handling diverse languages and typos.
Evaluation methods such as perplexity and benchmark tasks are described, along with challenges like inconsistencies and data contamination.
The lecture details the complexities of data collection and filtering, scaling laws that guide model and data size decisions, and the significant computational resources required.
Post-training, including supervised fine-tuning and reinforcement learning from human feedback (RLHF), is covered as essential for aligning models to user instructions and ethical guidelines.
The speaker also touches on system-level optimizations, such as low-precision computation and operator fusion, to efficiently utilize hardware.
Throughout, the importance of practical considerations—especially data quality, evaluation methods, and system efficiency—is highlighted as central to building effective LLMs.
# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Large Language Models (LLMs) are neural networks used for chatbots like ChatGPT, Claude, and Gemini.                                 |
|   2 | Key components in LLM training: architecture, training loss/algorithm, data, evaluation, and systems.                                |
|   3 | Most LLMs use Transformer architectures.                                                                                             |
|   4 | Academia focuses on architecture and algorithms, but data, evaluation, and systems are more critical in practice.                    |
|   5 | Pre-training involves modeling the probability distribution over sequences of tokens (language modeling).                            |
|   6 | LLMs are generative models; they can generate new sentences by sampling from learned distributions.                                  |
|   7 | Auto-regressive language models predict the next word given previous context using the chain rule of probability.                    |
|   8 | Tokenization is crucial; tokens are often subwords, not just words or characters, to balance sequence length and vocabulary size.    |
|   9 | Byte Pair Encoding (BPE) is a common tokenization method, merging frequent character pairs.                                          |
|  10 | Tokenizers keep smaller tokens for handling typos and rare words.                                                                    |
|  11 | Evaluation during pre-training uses perplexity (exponentiated average per-token loss), but perplexity depends on tokenizer and data. |
|  12 | Academic benchmarks aggregate multiple NLP tasks; examples include HELM and Hugging Face Open LLM Leaderboard.                       |
|  13 | Evaluation challenges: inconsistent methods, train-test contamination, and open-ended generation.                                    |
|  14 | Data collection involves crawling the web, extracting text, filtering undesirable content, deduplication, and domain balancing.      |
|  15 | High-quality data (e.g., Wikipedia) is used for final training stages.                                                               |
|  16 | Scaling laws: more data and larger models consistently improve performance; overfitting is not observed at scale.                    |
|  17 | Optimal training: about 20 tokens per parameter (Chinchilla scaling law); inference cost considerations may shift this ratio.        |
|  18 | Training LLMs is expensive (e.g., Llama 3: ~$75M, 16,000 GPUs, 70 days).                                                             |
|  19 | Post-training (alignment) makes LLMs follow instructions and avoid toxic outputs.                                                    |
|  20 | Supervised fine-tuning (SFT) uses human-annotated question                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9vM4p9NN0Ts)