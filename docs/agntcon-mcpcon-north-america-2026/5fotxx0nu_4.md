---
layout: default
title: "Trustworthy Context Is Untrusted By Default - Shub Argha, Arcade.dev"
nav_order: 77
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Shub, an FTE at arcade.dev, presents a critical analysis of the security risks associated with AI agents processing untrusted context, arguing that current evaluation systems fail to account for th..."
resource: "https://www.youtube.com/watch?v=5FotXX0NU_4"
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

Shub, an FTE at arcade.dev, presents a critical analysis of the security risks associated with AI agents processing untrusted context, arguing that current evaluation systems fail to account for the "trust" layer between agents and their inputs.
Through research involving tens of thousands of agent runs over three months, he demonstrates that while loud, explicit attacks are largely mitigated by modern model training, silent attacks—such as fake authority claims or subtle manipulations—successfully compromise 89% of agents.
The core issue is that agents treat all incoming context, whether from internal teams, external partners, or downloaded files, with the same high level of authority, leading to potential data leaks or destructive actions like deleting production databases.
To address this, Shub proposes a five-part architectural framework: implementing a server-generated preamble that explicitly labels context as hypothesis rather than fact, automatically classifying risk levels, recording detailed provenance (who, what, when, where, why), anchoring changes to specific versions or commits, and rigorously verifying all inputs against known truths.
This approach reduces the success rate of malicious silent attacks from 89% to 33%, highlighting the necessity for highly vetted context stores in regulated industries and establishing the principle that trust should always decay with distance from the original source.

# Main Points

|   # | Main point                                                                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** AI agents treat all provided context (PDFs, code, notes, MCP tools) as the highest authority, leading to risks like production database deletion or data leakage.                                                 |
|   2 | :** Major AI labs (Copilot, Claude, Cursor) have introduced shared context layers, increasing the surface area for untrusted information to enter agent workflows.                                                    |
|   3 | :** Context has a short half-life; documents or code become outdated quickly, causing agents to act on stale or incorrect information.                                                                                |
|   4 | :**                                                                                                                                                                                                                   |
|   5 | "Loud" attacks (e.g., direct prompts to exfiltrate data) are largely ineffective, with success rates under 7% due to model training.                                                                                  |
|   6 | "Silent" attacks (e.g., fake authority, claiming code is "tested" or "deprecated") are highly effective, succeeding in 89% of cases across 80 different agents.                                                       |
|   7 | :** Current evaluation systems test outcomes from a clean slate rather than testing what the agent _believes_. They often fail to detect forged claims or malicious instructions embedded in trusted-looking context. |
|   8 | (5 Components):**                                                                                                                                                                                                     |
|   9 | :** Server-generated wrapper for every read operation that explicitly states context is a hypothesis, not fact, and instructs the agent to trust code over human writers.                                             |
|  10 | :** Automatically assign risk classes (e.g., specific vs. structural code) at the time of writing to ensure higher security defaults.                                                                                 |
|  11 | :** Record "who, what, when, where, why" for all context, including server-generated timestamps, URIs, and commit hashes (SHA) to enable verification against a true source.                                          |
|  12 | :** Pin context to specific versions or commit histories (similar to Git) to track changes and prevent reliance on outdated documents.                                                                                |
|  13 | :** Always verify context against existing knowledge or codebases before execution; never blindly trust external documents or internet-sourced data.                                                                  |
|  14 | :** Implementing these five layers reduces the success rate of malicious silent attacks from 89% to 33%.                                                                                                              |
|  15 | :** Highly regulated industries (finance, pharma) must build vetted context stores with these trust layers, distinct from standard blob stores, to allow safe agent interaction.                                      |
|  16 | :** Determining when an agent is lying, understanding side effects of forged frames, and analyzing how wording/length affects attack success remain active research areas.                                            |
|  17 | :** Trust should always decay with distance; users must verify context before passing it to agents, especially when sharing across teams or organizations.                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5FotXX0NU_4/hqdefault.jpg)]("https://www.youtube.com/watch?v=5FotXX0NU_4")

[Watch on YouTube](https://www.youtube.com/watch?v=5FotXX0NU_4)
