---
layout: default
title: "No New Authority: Publishing and Finding MCP Agents... - Igor Racic & Ingmar Van Glabbeek, Infoblox"
nav_order: 59
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Ingmar from Infoblox presents a solution to the unsolved problem of discovering and trusting Model Context Protocol (MCP) servers, arguing that current methods like hardcoded URLs or central regist..."
resource: "https://www.youtube.com/watch?v=8iv1NuwOHSc"
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

Ingmar from Infoblox presents a solution to the unsolved problem of discovering and trusting Model Context Protocol (MCP) servers, arguing that current methods like hardcoded URLs or central registries introduce significant supply chain risks and lack lifecycle management.
He introduces DNS-8, an IETF draft sponsored by Infoblox, Deutsche Telekom, and Amazon, which leverages existing DNS infrastructure to provide a decentralized, verifiable discovery mechanism without introducing new roots of trust.
The system utilizes SVCB records to define endpoints and capabilities, TLSA records for key pinning via DANE, and DNSSEC to ensure the authenticity of the publisher, allowing clients to verify server identity and integrity through standard resolver validation.
A live demonstration illustrates how this approach enables secure agent discovery, policy enforcement, and tool invocation, effectively replacing the need for trusted third-party directories with a self-contained, domain-owner-controlled trust model.
While acknowledging current limitations such as uneven DNSSEC deployment and the lack of standardized IANA numbers for certain keys, the speaker emphasizes that DNS-8 offers a scalable, low-latency alternative that integrates seamlessly with existing toolchains and supports strict policy enforcement at both the client and resolver levels.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , relying on hardcoded URLs (lacking lifecycle management) or registries (creating supply chain risks and central authority dependencies).                            |
|   2 | , token scope creep, and registry rent, where central indices can be poisoned and dictate terms.                                                                      |
|   3 | ,000 agents and 5,900 MCP servers exist, most use non-standard methods like `mcp.domain` prefixes rather than DNS records like TXT or SRV.                            |
|   4 | (Revision 2) sponsored by Infoblox, Deutsche Telekom, and Amazon, utilizing existing DNS infrastructure to provide a trust and naming system for MCP.                 |
|   5 | , TLSA records for key pinning (DANE), and DNSSEC for integrity verification, requiring no new roots of trust.                                                        |
|   6 | : SVCB for "where and how," TLSA for "which key," and DNSSEC for publisher identity, with ALPN used to identify the MCP protocol.                                     |
|   7 | , and IANA numbers are pending, currently using private sets that some providers reject.                                                                              |
|   8 | (direct SVCB lookup), domain-based discovery (via `_index_agents`), and unknown agents (using directories as optional hints that must be re-verified via DNS).        |
|   9 | (active, unverified, inactive) but does not vouch for trust, leaving verification to the client’s DNS checks.                                                         |
|  10 | : caller filters, publisher-defined policy documents (allowing/denying methods), and resolver-level policies (RPZ) can block non-compliant lookups before connection. |
|  11 | , TXT, and index records locally, verifying DNSSEC validation, and enforcing strict mode policies that allow specific tools while denying others.                     |
|  12 | –231 milliseconds for MCP first answers, highlighting the efficiency of DNS-based discovery.                                                                          |
|  13 | , lack of IANA numbers, and unresolved search capabilities, though the project is now a Linux Foundation initiative with an available SDK.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/8iv1NuwOHSc/hqdefault.jpg)](https://www.youtube.com/watch?v=8iv1NuwOHSc)

[Watch on YouTube](https://www.youtube.com/watch?v=8iv1NuwOHSc)
