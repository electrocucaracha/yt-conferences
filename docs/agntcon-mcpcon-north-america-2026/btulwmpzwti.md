---
layout: default
title: "How Contexts Fail (and How to Fix Them) - Drew Breunig, cmpnd.ai"
nav_order: 7
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker, author of the upcoming *Context Engineering Handbook*, argues that while long-context windows have expanded, they simultaneously introduce critical failure modes such as context poison..."
resource: "https://www.youtube.com/watch?v=btuLWMpzwtI"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

The speaker, author of the upcoming _Context Engineering Handbook_, argues that while long-context windows have expanded, they simultaneously introduce critical failure modes such as context poisoning, distraction, confusion, and clash.
He demonstrates that models often prioritize recent or irrelevant context over base knowledge, citing examples like Gemini 2.5 failing Pokémon benchmarks due to outdated information and research showing models mimicking bad examples in long contexts.
To address these issues, he outlines a toolbox of six deterministic fixes—including context augmentation, tool loadout, quarantine, pruning, offloading, and summarization—that can be implemented with simple code, such as using small decision models to filter tools or prune history.
The discussion also highlights new challenges arising from agentic models trained to be persistent, which can lead to "hyperfocus" and stagnation, requiring strategic context deletion or "forgetting" to maintain productivity.
Ultimately, the speaker emphasizes that effective AI engineering requires balancing probabilistic model capabilities with deterministic harness controls, advising practitioners to actively manage context hygiene, use handoff documents, and avoid relying solely on default model behaviors to prevent "slop" and ensure high-quality outputs.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                        |
|   2 | • AI capabilities have been underestimated, particularly regarding what AI can accomplish                                                           |
|   3 | • Context windows expanded from 8K to 1 million tokens by late 2024, creating new failure modes                                                     |
|   4 | • Four key context failure modes: context poisoning, context distraction, context confusion, and context collision                                  |
|   5 | • Long contexts enable more errors alongside more information                                                                                       |
|   6 | • Context engineering involves providing correct context to get correct answers                                                                     |
|   7 | • Six primary context management tools: context augmentation, tool loading, context quarantine, context pruning, context offloading, and compaction |
|   8 | • Models trained for agentic behavior exhibit overfitting to training tools and struggle with unfamiliar environments                               |
|   9 | • Agents trained for persistence become hyperfocused on subtasks, requiring strategic context resets                                                |
|  10 | • Context resets every 1.5-3 hours and limiting context to 200-300K tokens improves agent performance                                               |
|  11 | • Memory and forgetting must be managed strategically in long-running systems                                                                       |
|  12 | • Solutions implemented today create tomorrow's problems                                                                                            |
|  13 | • Output = context × model weights; understanding training data helps debug failures                                                                |
|  14 | • Quality of context formatting affects model behavior through implicit cueing                                                                      |
|  15 | • Skill development through distillation and multi-stage task decomposition improves agent reliability                                              |
|  16 | • Tools like Kata, Agents View, and Superpowers help track and optimize agent sessions                                                              |
|  17 | • DSPy framework enables readable AI workflow construction with ~12 lines of code for agents                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/btuLWMpzwtI/hqdefault.jpg)]("https://www.youtube.com/watch?v=btuLWMpzwtI")

[Watch on YouTube](https://www.youtube.com/watch?v=btuLWMpzwtI)
