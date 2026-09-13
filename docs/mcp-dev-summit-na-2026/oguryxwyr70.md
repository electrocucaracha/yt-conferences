---
type: Video Note
title: "Stateless: The Future of MCP Transports - Shaun Smith, Hugging Face & Kurtis Van Gent, Google"
description: "In this session, Sean from Hugging Face and Curtis from Google Cloud, both MCP maintainers, discuss ongoing and future improvements to MCP transports, focusing on making the protocol stateless for better scalability, reliability, and simpli..."
resource: https://www.youtube.com/watch?v=OguRYXwyR70
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Sean from Hugging Face and Curtis from Google Cloud, both MCP maintainers, discuss ongoing and future improvements to MCP transports, focusing on making the protocol stateless for better scalability, reliability, and simplicity.
They highlight current challenges such as excessive protocol "chattiness," difficulties with session management, and inefficiencies in routing due to JSON RPC payloads.
Key proposals include removing session initialization to ensure each request is independent (as outlined in SCP 1442), restructuring multi-round trip requests to avoid state dependencies across servers (SCP 2322), and standardizing HTTP headers for more efficient routing (SCP 2243).
The speakers also address future optimizations like leveraging HTTP features and enabling pluggable transports for broader interoperability.
Throughout, they emphasize the importance of minimizing disruption for existing users and ensuring consistent feature support across all transport types, aiming for a more robust and scalable MCP ecosystem.
# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sean (Hugging Face) and Curtis (Google Cloud) are MCP core maintainers and lead the transport working group.                                                           |
|   2 | MCP is used at scale at Google Cloud for managed database services and at Hugging Face for inference models.                                                           |
|   3 | MCP must be highly reliable and scalable due to high usage (over 20 million tool calls/month, 2,500+ servers at Hugging Face).                                         |
|   4 | Current MCP protocol is chatty, with over 100 protocol messages per tool call, causing inefficiency.                                                                   |
|   5 | Dynamic tool lists and tool change notifications are difficult with current transports.                                                                                |
|   6 | MCP protocol is currently stateful, requiring session management, protocol version tracking, and client/server capabilities, making scaling difficult.                 |
|   7 | Stateless protocol (SCP 1442) is proposed: every request is independent, improving scalability, reliability, and simplicity.                                           |
|   8 | Statelessness removes initialization; protocol negotiation happens per request.                                                                                        |
|   9 | Multi-round trip requests (SCP 2322) will be handled as independent requests, reducing server state synchronization issues and improving elicitation support.          |
|  10 | Session handling is unclear in current protocol; proposal to move sessions to the data layer as an extension, but session-free protocols are preferred for simplicity. |
|  11 | HTTP standardization (SCP 2243) introduces headers to move routing information from the payload to the envelope, improving routing efficiency and reducing overhead.   |
|  12 | Future improvements include leveraging HTTP features (e.g., ETags), optimizing refresh intervals, and supporting pluggable transports (e.g., websockets, gRPC).        |
|  13 | Goal is to keep MCP core simple for interoperability and allow for non-standard or custom transports.                                                                  |
|  14 | SDK tiering introduced; most SDKs will implement new features by June spec release.                                                                                    |
|  15 | Emphasis on consistency across transports so features work the same way regardless of transport.                                                                       |
|  16 | Community contributions and feedback have been crucial to protocol improvements.                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OguRYXwyR70)