---
layout: default
title: "Agentic Workflows Are Distributed Systems: The... - Praneeth Kamalaksha Patil, CoreWeave"
nav_order: 139
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Pranay Patil, an AI infrastructure engineer at CoreWeave, argues that agentic workflows are fundamentally distributed systems that inherit complex reliability challenges when crossing cloud boundar..."
resource: "https://www.youtube.com/watch?v=0m7SvSIeZYs"
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

Pranay Patil, an AI infrastructure engineer at CoreWeave, argues that agentic workflows are fundamentally distributed systems that inherit complex reliability challenges when crossing cloud boundaries.
He illustrates this with a case study where an AI agent deleted a storage volume due to architectural flaws, emphasizing that such incidents stem from system design errors rather than model intelligence.
Patil proposes four key patterns to improve agent reliability: durable execution to manage long-running workflows, idempotency to prevent duplicate actions, strategies to mitigate cold start latency, and compensation mechanisms like the saga pattern to handle failures.
He further highlights that latency is often dominated by network fabric and authentication overhead rather than model inference, noting that cross-cloud operations can significantly increase these costs.
Ultimately, he concludes that agent reliability is an architectural property, requiring engineers to treat workflows with the same rigor as traditional distributed systems to avoid costly failures and ensure efficient performance.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | ; crossing cloud boundaries inherits complex distributed system problems.                                                                                               |
|   2 | , causing a 30-hour crisis and data loss.                                                                                                                               |
|   3 | : policy in prompts, excessive credential blast radius, bypassed guardrails via legacy APIs, colocateed backups, and lack of human-in-the-loop pauses.                  |
|   4 | , not model failures; swapping models without fixing architecture leaves a "time bomb."                                                                                 |
|   5 | % of enterprises use multi-cloud, and 73% are hybrid; token consumption is expected to jump 1000x by 2027.                                                              |
|   6 | % of AI projects are expected to be canceled in 2027 due to architectural errors and cost overruns.                                                                     |
|   7 | %, forcing workload migration for cost efficiency.                                                                                                                      |
|   8 | , retries, rate limiting, and authentication.                                                                                                                           |
|   9 | : Durable Execution.** Workflows must survive crashes and region outages. State must be externalized from the Python process.                                           |
|  10 | , maintaining event history/checkpoints, and placing workers based on SLOs rather than convenience.                                                                     |
|  11 | : Idempotency.** Prevents duplicate actions (e.g., double bookings) when agents retry failed calls.                                                                     |
|  12 | (workflow + step + attempt) rather than model-generated to ensure uniqueness across providers.                                                                          |
|  13 | , not inside a single provider’s model.                                                                                                                                 |
|  14 | ; tools without annotations are treated as non-idempotent and potentially destructive.                                                                                  |
|  15 | : Cold Start Problem.** Latency varies drastically: warm endpoints (<1s) vs. cold containers with object storage weights (40–90s).                                      |
|  16 | % cheaper and 85% faster than misses; cache does not travel across clouds, so routing must account for cache locality.                                                  |
|  17 | , hedging the tail (sending requests to multiple workers for latency-critical tasks), and prioritizing cache hits over geographic proximity.                            |
|  18 | : Compensation.** Rollback is not built into providers; the Saga pattern (1987) is required for multi-step workflows.                                                   |
|  19 | (undoable), pivot (point of no return, e.g., shipped goods), or retryable.                                                                                              |
|  20 | ; even top models lose track of the big picture during planning.                                                                                                        |
|  21 | , "fabric" (non-model overhead) accounts for 70% of total latency.                                                                                                      |
|  22 | , fabric is 70% of latency; across the Pacific, it rises to 89%.                                                                                                        |
|  23 | ~1 second, while distance adds only milliseconds.                                                                                                                       |
|  24 | ; improper routing to high-performance endpoints risks unpredictable response times.                                                                                    |
|  25 | :** Label tools clearly, move workflow state to a durable execution layer, place workers based on SLOs, and define latency budgets prioritizing caching and warm nodes. |
|  26 | , not a model property.                                                                                                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/0m7SvSIeZYs/hqdefault.jpg)](https://www.youtube.com/watch?v=0m7SvSIeZYs)

[Watch on YouTube](https://www.youtube.com/watch?v=0m7SvSIeZYs)
