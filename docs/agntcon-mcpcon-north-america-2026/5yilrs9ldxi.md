---
layout: default
title: "Why API Modernization is the Prerequisite to AI Governance - Amit Shah, Kong"
nav_order: 83
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker presents a talk arguing that API modernization is a prerequisite for effective AI governance, emphasizing that organizations must consider the entire AI data path—including APIs, events..."
resource: "https://www.youtube.com/watch?v=5YilRs9LDxI"
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

The speaker presents a talk arguing that API modernization is a prerequisite for effective AI governance, emphasizing that organizations must consider the entire AI data path—including APIs, events, and streaming data—rather than just model access.
Key takeaways include the necessity of building governance into system design from the start, as retrofitting it later is difficult, and the critical role of the gateway pattern in enforcing consistent controls.
The presentation highlights real-world risks, such as a Cursor agent deleting a production database in eight seconds due to excessive permissions, illustrating how fragmentation and lack of visibility lead to agent failures and security breaches.
To address these challenges, the speaker advocates for a unified "control tower" approach using gateways to manage identity, reliability, cost, and observability across GenAI and agentic workloads.
This strategy ensures that agents operate within defined boundaries, preventing unauthorized actions and mitigating the risks associated with shadow AI and context sprawl.

# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | , including APIs, events, real-time streaming data, and AI resources, rather than just access to AI models.                   |
|   2 | , as layering it on later is difficult and ineffective.                                                                       |
|   3 | % of AI initiatives fail to reach production, largely due to the lack of a governed path from pilot to production.            |
|   4 | % erosion of business margins.                                                                                                |
|   5 | % of security breaches are now categorized as shadow AI incidents, similar to previous shadow IT and cloud issues.            |
|   6 | , analogous to the design flaw in the movie _The Matrix_ where agent Smith only fixed glitches after they occurred.           |
|   7 | , an incident preventable by proper governance.                                                                               |
|   8 | , model selection, output validation, and cost management.                                                                    |
|   9 | , leading to rapid failure propagation.                                                                                       |
|  10 | , cost hemorrhaging from excessive context, and guarding against prompt injection and misuse.                                 |
|  11 | , agent sprawl (lack of visibility into spawned agents), and semantic sprawl (inconsistent understanding of data).            |
|  12 | % of organizations have no visibility into their AI data flows, and 63% have no AI governance at all.                         |
|  13 | , which is often unknown in distributed agent environments.                                                                   |
|  14 | , MCP servers, APIs, and multi-cloud environments, increasing the risk of hallucination and unauthorized access.              |
|  15 | , AI, and events, supported by four additional layers:                                                                        |
|  16 | : Verifying agent identity, acting on behalf of users, and enforcing permissions.                                             |
|  17 | : Ensuring connection uptime and failover between models.                                                                     |
|  18 | : Preventing the use of expensive models for menial tasks.                                                                    |
|  19 | : Tracking model access, usage, and agent activity.                                                                           |
|  20 | :                                                                                                                             |
|  21 | ’s ability to scan code for API keys.                                                                                         |
|  22 | , built on the Envoy platform, is designed for high throughput and low latency, differentiating it from legacy API solutions. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5YilRs9LDxI/hqdefault.jpg)]("https://www.youtube.com/watch?v=5YilRs9LDxI")

[Watch on YouTube](https://www.youtube.com/watch?v=5YilRs9LDxI)
