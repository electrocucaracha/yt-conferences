---
layout: default
title: "What Happens When You Integrate MCP and A2A at the Infrastructure Layer - Mohamed Maktal, Vultr"
nav_order: 152
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Mohamed Mokhtal, a solution engineer at Vultr, presents a technical analysis of critical failure modes that occur when integrating Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocols wi..."
resource: "https://www.youtube.com/watch?v=PpTfGwnIhBE"
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

Mohamed Mokhtal, a solution engineer at Vultr, presents a technical analysis of critical failure modes that occur when integrating Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocols with sandboxed infrastructure.
He identifies three primary issues: agents failing to detect sandbox crashes due to reliance on default timers, the accumulation of "zombie" background processes like Chrome units when MCP servers restart, and the risk of duplicate financial transactions caused by timeout-based retries during payment processing.
To address these problems, Mokhtal advocates for replacing passive timeout mechanisms with active, real-time status checks against the host provider’s API and implementing kernel-level cgroups to ensure complete process isolation and cleanup.
He demonstrates that these solutions, which leverage existing cloud infrastructure best practices rather than new protocols, significantly reduce resource waste and operational errors in large-scale agent deployments.
Finally, he provides specific diagnostic tests for each failure mode, emphasizing that robust agent systems must actively verify the state of their underlying hardware and external services rather than guessing based on elapsed time.

# Main Points

|   # | Main point                                                                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | :** Agents often operate "blind" when sandboxes fail because they rely on default timers rather than real-time infrastructure status, leading to inefficiencies and errors.                                                    |
|   2 | :** Frontier labs and RL companies run approximately 3 million sandboxes daily; losing 1 in 200 instances results in ~15,000 daily failures, causing significant cost and progress delays.                                     |
|   3 | :** The standard flow (Model → Agent Harness → MCP/Tools) lacks direct checks with the underlying hardware, creating a disconnect between the agent’s perception and the sandbox’s actual state.                               |
|   4 | :** Firecracker micro-VMs are commonly used for isolation due to their lightweight nature and fast boot times, which are critical for high-volume deployments.                                                                 |
|   5 | (Silent Death):** The sandbox dies mid-tool-call, but the agent only detects this after a default timeout (approx. 45–55 seconds), resulting in a "blind window" where the agent continues processing invalid requests.        |
|   6 | :* Implement keep-alive requests or status checks directly to the host provider’s API to verify sandbox liveness in real-time.                                                                                                 |
|   7 | (Zombie Processes):** When an MCP server (e.g., Playwright) stops, underlying Chrome units may not terminate, leading to "zombie tasks" that accumulate memory (e.g., 36 processes consuming ~1GB) and persist across retries. |
|   8 | :* Group all related processes into a single cgroup at the kernel level to ensure complete termination and add system checks to verify no residual units remain.                                                               |
|   9 | (Double Execution):** If a request (e.g., payment) is still processing when the agent’s timeout triggers, the agent retries the action, causing duplicate charges or actions (e.g., double billing).                           |
|  10 | :* Replace generic timeouts with purposeful, tailored checks that query the specific service (e.g., shop ledger) via read-only requests to confirm whether the process is still active before retrying.                        |
|  11 | :** The overarching solution for all failure modes is to stop guessing via default timers and instead "ask the part that knows" (the host supervisor or specific service) for real-time status.                                |
|  12 | :** These solutions do not require new protocols or SDKs; they utilize existing cloud infrastructure best practices and standard tools.                                                                                        |
|  13 | :** Agent-to-Agent (A2A) protocols exhibit identical failure modes and benefit from the same robustness improvements regarding hardware awareness and process management.                                                      |
|  14 | :**                                                                                                                                                                                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/PpTfGwnIhBE/hqdefault.jpg)]("https://www.youtube.com/watch?v=PpTfGwnIhBE")

[Watch on YouTube](https://www.youtube.com/watch?v=PpTfGwnIhBE)
