---
type: Video Note
title: 'The Evolution of Platform APIs in the Age of LLMs - Mauricio "Salaboy" Salatino & Viktor Farcic'
description: "The speaker discusses the challenges and considerations of integrating AI agents into internal developer platforms, particularly for operations tasks like creating cloud resources. They highlight that AI agents, much like new human hires, l..."
resource: https://www.youtube.com/watch?v=aOMcUwR4PN4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the challenges and considerations of integrating AI agents into internal developer platforms, particularly for operations tasks like creating cloud resources.
They highlight that AI agents, much like new human hires, lack context about company-specific practices, capabilities, and policies, leading to insufficient or incorrect results if not provided with detailed intent and relevant information.
To address this, the speaker proposes managing context through semantic search using embeddings and vector databases, enabling AI to retrieve relevant APIs, patterns, and policies from scattered company knowledge.
They demonstrate a system (MCP) that guides users through workflows, asks clarifying questions, and leverages company-specific data to generate appropriate solutions, emphasizing the importance of workflows, context management, and incremental learning.
The talk concludes by noting that AI is most valuable for creative, non-deterministic tasks, while deterministic, repeatable processes should remain automated by scripts or code, and that effective AI integration requires ongoing effort to curate and structure company knowledge.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focuses on AI agents in internal developer platforms and operations.                                                                         |
|   2 | Example given: asking an AI agent to create a database in AWS with minimal context.                                                                     |
|   3 | Main problems identified:                                                                                                                               |
|   4 | Insufficient intent: user provides vague requests, leading to assumptions by AI or humans.                                                              |
|   5 | AI lacks knowledge of company-specific capabilities, best practices, and policies.                                                                      |
|   6 | AI forgets previous interactions; lacks persistent learning.                                                                                            |
|   7 | Three key areas for successful AI agent systems:                                                                                                        |
|   8 | Effective context management.                                                                                                                           |
|   9 | Guided workflows for both users and agents.                                                                                                             |
|  10 | Mechanisms for AI learning about company-specific patterns and policies.                                                                                |
|  11 | Proposed solution:                                                                                                                                      |
|  12 | Expose platform capabilities via APIs (e.g., Kubernetes).                                                                                               |
|  13 | Convert API endpoints and company knowledge into embeddings stored in a vector database for semantic search.                                            |
|  14 | Use semantic search to match user intent with relevant resources, patterns, and policies.                                                               |
|  15 | Company patterns and policies are scattered across various sources (wiki, Slack, meetings) and should be embedded for searchability.                    |
|  16 | Policies act as a last line of defense but do not teach correct behavior.                                                                               |
|  17 | Demo presented: AI agent interacts with user, asks clarifying questions, retrieves relevant endpoints, policies, and patterns, and generates manifests. |
|  18 | AI agent uses company patterns to suggest preferred solutions (e.g., golden path).                                                                      |
|  19 | Emphasized importance of workflows and context in guiding AI responses.                                                                                 |
|  20 | AI is not suitable for deterministic, repeatable tasks—use scripts or code for those.                                                                   |
|  21 | AI excels in creative, non-deterministic tasks like generating manifests or specifications.                                                             |
|  22 | System prompt should contain behavioral instructions, not all company knowledge.                                                                        |
|  23 | Embedding process involves extracting relevant information and converting it to vectors; matching embedding dimensions is crucial.                      |
|  24 | Maintaining quality requires strong documentation and clear instructions; AI can process unstructured data but needs guidance.                          |
|  25 | AI s                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aOMcUwR4PN4)