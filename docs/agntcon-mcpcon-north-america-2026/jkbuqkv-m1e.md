---
layout: default
title: "AGENTS.md is the New CONTRIBUTING.md: A Field Report from One Year of... - Unnati Mishra, Nutanix"
nav_order: 18
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "This presentation by Unnati Mishra explores the critical role of the `agents.md` file in guiding AI agents for open-source contributions, highlighting that while it serves as a new standard akin to..."
resource: "https://www.youtube.com/watch?v=jKbuqKv-M1E"
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

This presentation by Unnati Mishra explores the critical role of the `agents.md` file in guiding AI agents for open-source contributions, highlighting that while it serves as a new standard akin to `contributing.md`, its effectiveness depends heavily on precise, imperative instructions rather than vague context.
Citing contradictory research findings, the speaker explains that bloated files containing redundant information or unnecessary tool names cause "inflation," leading to higher token usage and lower task success rates, whereas compressed files with exact, copy-pasteable build and test commands significantly improve efficiency.
The talk emphasizes that `agents.md` must contain specific sections for build commands, targeted test suites, and "never touch" boundaries to prevent agents from making confident but incorrect guesses, with the nearest file in the directory hierarchy taking precedence to handle monorepo complexities.
To optimize existing files, the speaker recommends using a "line ablation test" to remove redundant lines and establishing `agents.md` as a single source of truth, pointing other tool-specific files to it to avoid duplication.
Finally, the presentation advises treating `agents.md` with the same rigor as code by validating commands in clean containers, assigning owners for review, and tracking metrics like PR acceptance rates and human edit frequency to ensure the file remains accurate and effective over time.

# Main Points

|   # | Main point                                                                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | : AI agents often fail in open source contributions because they lack the context humans naturally acquire (e.g., asking questions on Slack), leading to uninformed edits and manual corrections.                                    |
|   2 | : This file serves as a new "contributing.md" specifically for AI agents, providing necessary context to prevent confident guessing and errors.                                                                                      |
|   3 | : Two studies showed conflicting results: one found LLM-generated context files lowered task success rates, while another found agents.md reduced median runtime by 28.6% and token usage by 16.6%.                                  |
|   4 | : Unlike `contributing.md`, which should be welcoming and explanatory for humans, `agents.md` must be short, imperative, and exact to prevent agents from guessing.                                                                  |
|   5 | : The "nearest file wins" rule applies, similar to `OWNERS` files. Root files contain general rules, while nested folder-specific files contain specific build and test commands.                                                    |
|   6 | : An effective `agents.md` must include exact copy-pasteable build commands, specific test commands for particular PRs (avoiding full suites for minor changes), and a "never touch" list for generated or vendor files.             |
|   7 | : Agents treat every keyword as an order. Vague instructions, project overviews, or unnecessary tool names cause agents to burn more tokens and take extra steps. Compressed, exact commands improve efficiency.                     |
|   8 | : Remove information already present in the repository or known by the agent. Use the "line ablation test" to delete lines that do not change output, thereby saving tokens.                                                         |
|   9 | : Maintain one primary `agents.md` file. Other tool-specific files (e.g., Cursor, Copilot) should point to this source rather than duplicating content to avoid conflicts.                                                           |
|  10 | : Agent context consists of `agents.md` (repository rules), Skills (job-specific playbooks), and MCP (live tool access to systems like issue trackers).                                                                              |
|  11 | : Track acceptance rate (PRs opened vs. merged), time to first green CI run, number of human edits, and for non-coding tasks, suggestion usage rates and re-prompting frequency.                                                     |
|  12 | : Treat `agents.md` edits with caution as they are instructions for autonomous agents. Review for dangerous commands (e.g., downloading and executing files) and ensure nested files in vendor folders are not accidentally created. |
|  13 | : Treat `agents.md` like code. Run its commands in clean containers during CI to detect drift. Assign an owner in the `OWNERS` file to review changes and prevent stale instructions.                                                |
|  14 | : Start by copying build/test commands from CI, adding a "never added by hand" section, and tracking performance metrics from day one.                                                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/jKbuqKv-M1E/hqdefault.jpg)]("https://www.youtube.com/watch?v=jKbuqKv-M1E")

[Watch on YouTube](https://www.youtube.com/watch?v=jKbuqKv-M1E)
