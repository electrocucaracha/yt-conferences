---
type: Video Note
title: "[Session] Building a MCP Server for Agentic Commerce with Brenden Lane and Nitin Sharma from PayPal"
description: "In this presentation, Brendan and Nitten from PayPal introduce the MCP server developed for Agentic Commerce, explaining how it enables agents to handle the entire online shopping process—from product discovery and price comparison to check..."
resource: https://www.youtube.com/watch?v=ZKagb-ZkNnI
tags: ["mcp-dev-summit-na-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Brendan and Nitten from PayPal introduce the MCP server developed for Agentic Commerce, explaining how it enables agents to handle the entire online shopping process—from product discovery and price comparison to checkout and order confirmation—through conversational interfaces.
They demonstrate how an agent, such as Claude, can search for products, retrieve detailed catalog information, initiate purchases, and manage payment and shipping, all while maintaining user consent and security protocols like multi-factor authentication.
The talk then delves into the design principles behind MCP tools, emphasizing modularity, single-purpose functions, explicit context handling, robust security measures, and comprehensive lifecycle management, including auditing, deprecation, and backward compatibility.
They highlight the importance of secure data handling, agent and tool discoverability, and integration with protocols like A2A for cross-agent coordination.
The session concludes with a discussion of emerging directions such as unified tool registries, event-driven controls, privacy-preserving invocations, and simulation protocols, inviting attendees to explore PayPal’s MCP toolkits and engage further with the team.
# Main Points

|   # | Main point                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of MCP server for Agentic Commerce at PayPal                                                                                                                                                                    |
|   2 | Traditional online shopping involves manual searching, comparing, and purchasing by users; merchants focus on SEO, ads, and sales                                                                                            |
|   3 | MCP servers enable agents to perform shopping tasks (finding items, comparing prices, purchasing, tracking shipping) via conversation                                                                                        |
|   4 | Demo shows using Claude assistant to shop for hoodies, access product catalogs, view details, and complete checkout                                                                                                          |
|   5 | MCP tools allow access to product catalogs across multiple stores, aggregate information, and automate checkout with stored payment/shipping info                                                                            |
|   6 | Multifactor authentication is supported for secure purchases                                                                                                                                                                 |
|   7 | Agents can handle logical tasks like waiting for sales, finding cheapest options, and tracking shipping                                                                                                                      |
|   8 | MCP toolkit includes tools for catalog access, identity, purchase, payments, and business reporting                                                                                                                          |
|   9 | Tools are designed for composability, security, and agent control                                                                                                                                                            |
|  10 | MCP toolkit design principles:                                                                                                                                                                                               |
|  11 | Tool ownership and scope: central registry, access control, unique identity, schema contracts, domain grouping, policy guardrails, auditing, and traceability                                                                |
|  12 | Tool function and behavior: modularity, single purpose, concise input/output, safe evaluation, explicit context dependency, structured error handling, latency transparency, runtime behavior contracts, composable planning |
|  13 | Tool evolution and lifecycle: usage monitoring, CI validation, maturity tagging, deprecation flow, audits for stale tools, change history, lifecycle dates, backward compatibility                                           |
|  14 | Security considerations: avoid oversharing, prevent PII leakage, use encryption, prevent replay attacks, ensure agent identity, enforce tool scope                                                                           |
|  15 | Improved MCP context includes TLS/MTLS, HMAC/JWT signatures, nonces, schema validation, field-level encryption                                                                                                               |
|  16 | MCP integrates with A2A (agent-to-agent) protocols for cross-agent discovery and coordination                                                                                                                                |
|  17 | Emerging directions: unified tool registries, event-driven controls, privacy-preserving invocations, sta                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZKagb-ZkNnI)