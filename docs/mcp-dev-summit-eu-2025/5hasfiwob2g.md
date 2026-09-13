---
type: Video Note
title: "[Session] What are Profiles? A Proposed Foundational Feature of MCP Servers"
description: "The speaker introduces their background in standards development and explains the challenges of enforcing specific policies within the broadly applicable MCP (Model Context Protocol) framework, especially given its use across diverse enterp..."
resource: https://www.youtube.com/watch?v=5HasfiWOB2g
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces their background in standards development and explains the challenges of enforcing specific policies within the broadly applicable MCP (Model Context Protocol) framework, especially given its use across diverse enterprise and consumer scenarios.
They propose the use of "profiles" as a solution, allowing organizations to mandate or extend certain behaviors without imposing requirements on the entire MCP community.
Profiles are defined by unique URLs and can specify requirements such as authentication methods or token durations, and are discoverable via a well-known document on the server.
The negotiation of profiles between clients and servers occurs during the initialization phase, enabling both parties to agree on which profiles to use or to terminate the connection if agreement isn't reached.
This approach supports both standard and custom profiles, allows SaaS providers to serve multiple tenants with different requirements, and can be used to differentiate service tiers in consumer applications, thus promoting flexible policy enforcement and broader MCP adoption.
# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is a standards expert, previously authored a widely adopted blog at Google.                                                                                                      |
|   2 | MCP (Model Context Protocol) is broadly applicable across enterprise and consumer use cases.                                                                                             |
|   3 | Challenge: Enforcing specific policies for different use cases without burdening the entire MCP community.                                                                               |
|   4 | MCP optionally supports OAuth for authentication/authorization, but enterprises may want to enforce specific OAuth options (e.g., JWT-based client assertions, client credentials flow). |
|   5 | Enterprises may use both internal MCP servers and third-party SaaS services, each with different policy needs.                                                                           |
|   6 | Profiles allow mandating specific behaviors or properties and can extend MCP with features not in the core standard (e.g., token duration limits).                                       |
|   7 | Profiles enable enterprises and service providers to enforce policies without impacting the whole community.                                                                             |
|   8 | Profiles are defined by a specification URL, uniquely identifying each profile.                                                                                                          |
|   9 | Servers declare supported profiles via a well-known document (MCP supported profiles), including minimum MCP version requirements.                                                       |
|  10 | Clients request desired profiles in the MCP initialize request; servers respond with supported profiles in the initialize result.                                                        |
|  11 | If client and server agree on profiles, the session proceeds; otherwise, connection is dropped.                                                                                          |
|  12 | Standard profiles are defined in the MCP repository and are optional; custom profiles are defined elsewhere.                                                                             |
|  13 | SaaS services can support tenant-specific custom profiles using well-known URLs or subdomains per tenant.                                                                                |
|  14 | Profile-unaware clients omit the requested profiles field; servers respond without profiles, defaulting to standard behavior.                                                            |
|  15 | Profiles support both profile-aware and profile-unaware clients simultaneously.                                                                                                          |
|  16 | Consumer use case: Video service with standard and premium tiers; profiles control access and client behavior based on user tier.                                                        |
|  17 | Feedback and comments on the SE (Specification Enhancement) are encouraged.                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5HasfiWOB2g)