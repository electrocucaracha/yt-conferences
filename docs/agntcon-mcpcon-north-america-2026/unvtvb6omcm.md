---
layout: default
title: "5 Ways to Build a Durable Browser Agent in 2026 - Andrew Baker, Temporal"
nav_order: 82
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Andrew Baker, a developer at Temporal, presents a talk on building resilient browser agents by treating websites as downstream services rather than direct user interfaces."
resource: "https://www.youtube.com/watch?v=UnVtvB6OMcM"
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

Andrew Baker, a developer at Temporal, presents a talk on building resilient browser agents by treating sites as downstream services rather than direct user interfaces.
He argues that exposing agents directly to users is inefficient due to slowness and error-proneness, and legally risky given the economic incentives of sites to block automated traffic.
Instead, he advocates for using browser agents to convert web data into API-like services that other agents can consume reliably.
Baker demonstrates this approach through several projects, including "No Stopping SF," which scrapes undocumented city data to identify unenforceable parking signs, and "Even Better Seat," which uses Kernel’s cloud browser infrastructure to monitor airline seat maps cost-effectively.
He highlights the importance of orchestration platforms like Temporal for handling failures and retries in these workflows, ensuring that complex tasks remain durable despite infrastructure or third-party service disruptions.
Finally, he shares his experience scaling the "IMAXing" ticket monitoring service, which successfully tracked millions of seats for Christopher Nolan’s films by leveraging Temporal to manage high-volume, fault-tolerant data extraction and user notifications.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | : Andrew Baker, formerly DevRel at Twilio and creator of O'Reilly’s first Docker course, currently works at Temporal.                                                                                                                                                    |
|   2 | : An open-source orchestration platform that makes applications resilient to failure by defining workflows and activities, ensuring reliability against infrastructure or downstream service failures.                                                                   |
|   3 | : A ticket ordering system demo showed that a naive implementation failed significantly under load, while the Temporal-based version successfully handled retries and service outages without data loss.                                                                 |
|   4 | : Early browser agents (e.g., Claude for Chrome) operated as co-browsing sidebars but were slow, error-prone, and difficult to supervise, leading to user frustration.                                                                                                   |
|   5 | : It is better to build browser agents as backend services that turn sites into APIs for AI agents to consume, rather than exposing them directly to end users.                                                                                                          |
|   6 | & Legal Tensions**: Companies like DoorDash and Amazon resist agent-driven orders because they lose ad revenue; legal disputes (e.g., Perplexity vs. Amazon) highlight the gray area of scraping and terms of service violations.                                        |
|   7 | : Undocumented APIs**: Agents can exploit undocumented XHR endpoints. Example: "No Stopping SF.io" used a city API to reveal that 62% of San Francisco’s "no parking" signs were unenforceable.                                                                          |
|   8 | : Cloud Browsers**: For sites with strong bot protection (e.g., United Airlines), cloud browser services like Browserbase are required to execute requests in a realistic environment.                                                                                   |
|   9 | :                                                                                                                                                                                                                                                                        |
|  10 | : A command-line interface allowing agents to interact with sites via Browserbase’s cloud infrastructure.                                                                                                                                                                |
|  11 | : A framework that separates LLM-powered data extraction from deterministic Playwright automation to reduce costs and improve reliability.                                                                                                                               |
|  12 | : Cost-Optimized Execution**: Kernel offers "Kernel Browser’s cURL," allowing standard HTTP requests to be executed within a cloud browser environment. It charges per second (vs. per minute for competitors), reducing costs for high-frequency, low-complexity tasks. |
|  13 | : A product that monitors airline seat maps to automatically upgrade seats. It used Kernel’s per-second billing and curl-like requests to efficiently check availability without full browser navigation.                                                                |
|  14 | : Scaling with Temporal**: The "IMAXing" project monitored 2.6 million seats across 8,000 showings for Christopher Nolan’s _The Odyssey_.                                                                                                                                |
|  15 | : Temporal automatically handled retries for API failures (theater data, email, Telegram notifications) without requiring manual intervention or paging the developer.                                                                                                   |
|  16 | : Browser agents should be treated as unreliable downstream services. Using orchestration platforms like Temporal ensures that agents can handle failures, retries, and scaling challenges effectively in production environments.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UnVtvB6OMcM/hqdefault.jpg)](https://www.youtube.com/watch?v=UnVtvB6OMcM)

[Watch on YouTube](https://www.youtube.com/watch?v=UnVtvB6OMcM)
