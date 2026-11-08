---
layout: default
title: "Multi-Agent SRE: What Happens When Your Agents Want Opposite Things - Aditi Mewada, Apple"
nav_order: 48
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Aditi, a software engineer at Apple, presents an independent analysis on managing multi-agent SRE systems in production environments, highlighting that 65% of production incidents are caused by AI ..."
resource: "https://www.youtube.com/watch?v=xDnheQC5GIg"
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

Aditi, a software engineer at Apple, presents an independent analysis on managing multi-agent SRE systems in production environments, highlighting that 65% of production incidents are caused by AI agents due to conflicts when multiple agents operate on shared resources.
She identifies key failure modes such as stale state, override wars, deadlocks, and cascading failures, using an example where a remediation agent and a cost agent simultaneously act on the same availability zone, resulting in an outage.
To address these issues, she proposes a "referee architecture" where agents only propose actions into a queue, and a deterministic, non-LLM referee system detects conflicts, ranks tasks based on organizational priorities (safety, availability, performance, cost), and leases execution rights to the highest-priority task.
The system enforces strict rules: if a proposal is stale, it must be replanned; if outranked, it is deferred; and if there is a priority tie, the decision is escalated to a human rather than an LLM.
Finally, she outlines a phased approach to autonomy, starting with observation and human-approved actions before moving to autonomous mode with canary deployments, emphasizing that all agent disagreements must remain visible, ranked, and reversible to ensure system stability.

# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Multi-agent SRE systems face conflicts when multiple AI agents operate on shared production resources simultaneously, leading to outages despite individual agent correctness. |
|   2 | :                                                                                                                                                                                |
|   3 | % of organizations have two or more agents running in production.                                                                                                                |
|   4 | % report a need for better error detection and tracing capabilities.                                                                                                             |
|   5 | % of production incidents are attributed to AI agents (Cloud Security Alliance survey).                                                                                          |
|   6 | :                                                                                                                                                                                |
|   7 | : Agents act on outdated information without understanding the broader system context.                                                                                           |
|   8 | : Agents repeatedly override each other’s actions (e.g., simultaneous scale-up and scale-down), resulting in no net change.                                                      |
|   9 | : Agents wait indefinitely for shared resources held by others.                                                                                                                  |
|  10 | : Actions by one agent inadvertently trigger incidents in dependent services.                                                                                                    |
|  11 | : A deterministic, non-LLM core system that manages agent proposals to prevent conflicts.                                                                                        |
|  12 | : Agents submit tasks containing identity, owner, verb (action), target, base version, priority, ETA, and evidence.                                                              |
|  13 | : The referee performs three tasks: Detect (identify conflicts), Rank (prioritize actions), and Lease (assign execution time).                                                   |
|  14 | : Tracks target versions, active leases, and time-to-live to maintain a global state view.                                                                                       |
|  15 | :                                                                                                                                                                                |
|  16 | : If the proposal’s base version does not match the current state, the plan is deemed stale and must be replanned.                                                               |
|  17 | : Identifies conflicting actions (e.g., draining a zone while terminating nodes) using predefined conflict pairs based on incident data.                                         |
|  18 | : Actions are sorted by organizational priority. If the top-ranked action is not the current proposal, the proposal is deferred.                                                 |
|  19 | : If priorities are equal, the decision is escalated to a human; LLMs are not used for final tie-breaking decisions.                                                             |
|  20 | : Execution is granted a time window (ETA multiplied by a factor for retries). If the action fails or times out, the lease is revoked.                                           |
|  21 | :                                                                                                                                                                                |
|  22 | : Deny actions that reduce availability below required thresholds (e.g., minimum two availability zones).                                                                        |
|  23 | : Hold low-priority tasks during active incidents to prioritize resolution.                                                                                                      |
|  24 | : Escalate to humans if the same conflicting proposals occur multiple times within a short window, indicating a systemic bug.                                                    |
|  25 | :                                                                                                                                                                                |
|  26 | (highest priority).                                                                                                                                                              |
|  27 | (lowest priority; high-cost actions may be blocked if other metrics are stable).                                                                                                 |
|  28 | :                                                                                                                                                                                |
|  29 | : Progress from observation to proposal, then to human-approved action, and finally to autonomous mode for small tasks.                                                          |
|  30 | : Always escalate to humans in cases of priority ties, repeated conflicts, or actions with a large blast radius/high traffic impact.                                             |
|  31 | : Use small traffic percentages (e.g., 20%) for autonomous changes to allow for easy rollback.                                                                                   |
|  32 | : Ensure all agent disagreements are visible, ranked, and reversible to maintain production stability.                                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xDnheQC5GIg/hqdefault.jpg)]("https://www.youtube.com/watch?v=xDnheQC5GIg")

[Watch on YouTube](https://www.youtube.com/watch?v=xDnheQC5GIg)
