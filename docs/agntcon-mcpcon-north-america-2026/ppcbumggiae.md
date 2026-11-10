---
layout: default
title: "MCP Rug Pulls in the Wild: Live Attacks and How To Stop Them - Advait Patel & Charit Upadhyay"
nav_order: 146
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'The speaker highlights critical security vulnerabilities in Model Context Protocol (MCP) implementations, specifically focusing on "rug pull" attacks where legitimate tools are compromised during s...'
resource: "https://www.youtube.com/watch?v=PPcbuMGGiAE"
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

The speaker highlights critical security vulnerabilities in Model Context Protocol (MCP) implementations, specifically focusing on "rug pull" attacks where legitimate tools are compromised during subsequent patches or upgrades to exfiltrate sensitive data.
By analyzing real-world incidents, such as an npm package that secretly forwarded email contents to attackers, the presentation demonstrates how MCPs can be manipulated to bypass user consent and access restricted information like credentials and cluster details.
The speaker argues that traditional security measures, including Software Bill of Materials (SBOM), Web Application Firewalls (WAF), and prompt injection filters, are insufficient to detect these subtle behavioral changes and unauthorized tool misuse.
To mitigate these risks, the presentation advocates for a robust security framework that treats tool definitions as code, requiring cryptographic signing of every tool identity and definition change to ensure integrity and traceability.
Furthermore, it emphasizes the necessity of strict runtime behavior monitoring and policy-based guardrails that restrict MCPs to specific network routes and actions, ensuring that any deviation from approved scopes triggers immediate alerts and prevents unauthorized data exploration.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , but security engineers must ensure they remain allies rather than threats by analyzing internal versions, patches, and security models.                 |
|   2 | , prompt injections, jailbreaks, tool misuse, and over-permissive scopes that can break systems.                                                          |
|   3 | "MCP rug pull" occurs when a trusted package is initially approved, but subsequent patches or upgrades introduce malicious behavior without user consent. |
|   4 | , such as reading email content and exfiltrating credentials to unauthorized addresses while hiding the action from the user.                             |
|   5 | , including conversation history, tool definitions, and session identifiers, to attackers.                                                                |
|   6 | , such as two-line HTTP GET requests without authentication, can allow attackers to access internal MCP patches and cluster information.                  |
|   7 | , prompt injection filters, and WAFs are insufficient against MCP-specific rug pulls and JSON-based manipulations.                                        |
|   8 | ; every tool and upgrade must be signed by a publisher, and clients should pin signatures rather than relying on tool names.                              |
|   9 | /egress routes, ensuring the agent cannot cross organizational boundaries without explicit user intent.                                                   |
|  10 | , access unauthorized Confluence pages, or interact with other MCPs.                                                                                      |
|  11 | , with approvals based on cryptographic signatures and client IDs rather than simple identity-based access.                                               |
|  12 | , as MCPs may possess more system knowledge than internal staff.                                                                                          |
|  13 | , triggering alerts via Slack or Outlook when boundaries are breached.                                                                                    |
|  14 | , patch intents, and author details to build trust, while corporate networks must perform due diligence on upgrades.                                      |
|  15 | , security parameters, and SBOMs, as name-based identification is insufficient.                                                                           |
|  16 | /stage testing to evaluate new MCP upgrades before production deployment.                                                                                 |
|  17 | , GCP, or OCI, which handle issuance, rotation, and renewal of security certificates.                                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/PPcbuMGGiAE/hqdefault.jpg)](https://www.youtube.com/watch?v=PPcbuMGGiAE)

[Watch on YouTube](https://www.youtube.com/watch?v=PPcbuMGGiAE)
