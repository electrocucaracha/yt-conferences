---
type: Video Note
title: "Stanford CS25: V5 I On the Biology of a Large Language Model, Josh Batson of Anthropic"
description: 'Joshua Batson from Anthropic presents an overview of his team''s work on mechanistic interpretability of large language models, focusing on understanding their internal "biology." He explains that, rather than simply pattern-matching or usin...'
resource: https://www.youtube.com/watch?v=vRQs7qfIDaU
tags: ["large-language-models-llms", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Joshua Batson from Anthropic presents an overview of his team's work on mechanistic interpretability of large language models, focusing on understanding their internal "biology." He explains that, rather than simply pattern-matching or using shallow heuristics, these models develop abstract, compositional representations and perform complex, parallel computations.
Batson describes their approach of using sparse dictionary learning to identify interpretable features—linear combinations of neurons—that correspond to meaningful concepts, such as the Golden Gate Bridge or medical diagnoses, and demonstrates how interventions on these features can causally influence model outputs.
He provides examples showing that models generalize concepts across languages, perform arithmetic through parallel motifs, and exhibit planning behaviors, such as generating rhymes.
The talk also addresses challenges like hallucinations and the limitations of current interpretability methods, emphasizing the need for deeper understanding as models become more capable and their behaviors more subtle.
# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Joshua Batson from Anthropic leads the circuits effort on the mechanistic interpretability team.                                   |
|   2 | The talk is based on the paper "On the Biology of a Large Language Model."                                                         |
|   3 | Interpretability is compared to biology: studying complex systems produced by a process (evolution/training).                      |
|   4 | Large language models (LLMs) can outperform specialized NLP models, even in low-resource languages, via in-context learning.       |
|   5 | LLMs exhibit both impressive capabilities and strange, inconsistent behaviors.                                                     |
|   6 | Interpretability seeks to understand what models have learned and how behaviors arise.                                             |
|   7 | Common misconceptions: models only pattern match, use shallow heuristics, and work one word at a time.                             |
|   8 | Findings: models learn abstract representations, perform complex parallel computations, and plan multiple tokens ahead.            |
|   9 | Neural network basics: words are embedded as vectors, processed through layers, and output is generated one word at a time.        |
|  10 | Transformer architectures use residual connections, attention, and MLP blocks.                                                     |
|  11 | Analogy: LLMs are "grown" via training, not "built."                                                                               |
|  12 | Individual neurons in LLMs are rarely interpretable; dictionary learning (sparse autoencoders) yields more interpretable features. |
|  13 | Discovered features can represent abstract concepts (e.g., Golden Gate Bridge, bugs in code).                                      |
|  14 | Interventions (activating/suppressing features) can causally change model outputs.                                                 |
|  15 | Cross-layer transcoders are used to model computation across layers, improving interpretability.                                   |
|  16 | Features can be grouped and traced through causal graphs to explain model decisions.                                               |
|  17 | Multilingual analysis shows models develop shared abstract representations across languages in middle layers.                      |
|  18 | Parallel processing motifs: models perform computations (e.g., addition) in parallel, not serially.                                |
|  19 | Hallucinations and refusals are mediated by competing features and suppression mechanisms.                                         |
|  20 | Planning: models can plan ahead (e.g., rhyming in poetry) by activating features before output.                                    |
|  21 | Limitations: attent                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vRQs7qfIDaU)