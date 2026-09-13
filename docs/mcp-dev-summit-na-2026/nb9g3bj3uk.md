---
layout: default
title:
  "Mix-Up Attacks in MCP: Multi-Issuer Confusion and Mitigations - Emily Lauber,
  Microsoft"
nav_order: 66
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Emily Lober, a senior product manager at Microsoft, discusses the challenges
  of mixup attacks in the MCP (Managed Client Protocol) ecosystem, emphasizing their
  subtlety and prevalence due to MCP’s architecture, which often involves multiple...
resource: https://www.youtube.com/watch?v=-nb9g3Bj3uk
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Emily Lober, a senior product manager at Microsoft, discusses the challenges of mixup attacks in the MCP (Managed Client Protocol) ecosystem, emphasizing their subtlety and prevalence due to MCP’s architecture, which often involves multiple clients and authorization servers.
Using an analogy involving her pets, she explains how a malicious authorization server can impersonate a client and gain unauthorized access by exploiting shared redirect URIs and the complexity of authorization flows.
She outlines two main mitigations: using unique redirect URIs per authorization server—which is difficult to implement at scale in MCP—and validating the issuer parameter in authorization responses, a practice now recommended in a new draft specification (SE 2468).
Lober urges developers to adopt issuer validation, update SDKs, and carefully manage trust relationships to protect against these attacks, concluding with a call to action for the MCP community to implement these security measures.
During the Q&A, she acknowledges that while resource and audience validation can help, they may not fully prevent mixup attacks, reinforcing the need for issuer parameter validation.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Emily Lober is a senior product manager in identity at Microsoft and facilitator for the mixup attack prevention working group and MCP specification.   |
|   2 | Mixup attacks are subtle, hard to detect, and more prevalent in the MCP architecture due to its structure.                                              |
|   3 | MCP ecosystem involves many clients, servers, and authorization servers, creating ideal conditions for mixup attacks.                                   |
|   4 | Mixup attack requirements: client interacts with multiple authorization servers and uses a single redirect URI for all.                                 |
|   5 | Example scenario: smart home agent (client), pet MCP server (resource), two authorization servers (guinea pigs and cat).                                |
|   6 | Attack flow: malicious authorization server impersonates the client, redirects authorization requests, and gains unauthorized access tokens.            |
|   7 | Attack can go unnoticed as all parties complete their expected tasks.                                                                                   |
|   8 | Attack can occur if a malicious authorization server is trusted or if the MCP server is compromised and adds a malicious authorization server.          |
|   9 | Mixup attacks have been known since at least 2016 (OAuth 2.1).                                                                                          |
|  10 | MCP is more vulnerable due to scale, increased phishing attempts, and non-deterministic client-server relationships.                                    |
|  11 | First mitigation: unique redirect URIs per authorization server, but this is difficult to implement at scale in MCP.                                    |
|  12 | Client registration methods (pre-registration, dynamic client registration, SIMD client ID metadata) have limitations for unique redirect URIs.         |
|  13 | Second mitigation: validate the issuer parameter in authorization responses.                                                                            |
|  14 | Issuer parameter is defined in authorization server metadata and should be validated by the client.                                                     |
|  15 | Issuer is required in metadata but not always sent in authorization responses; new draft SE 2468 recommends including it in MCP.                        |
|  16 | MCP clients should check and validate issuer; authorization servers should send issuer parameter.                                                       |
|  17 | Call to action: MCP resources should carefully choose trusted authorization servers; clients and SDKs should support issuer validation; authorization s |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-nb9g3Bj3uk)
