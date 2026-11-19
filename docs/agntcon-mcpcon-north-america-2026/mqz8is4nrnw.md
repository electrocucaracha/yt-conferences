---
layout: default
title: "When Agents Spawn Agents: Securing Recursive Delegation in... - Anishma Mavuram, EmpowerID"
nav_order: 25
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Anishma from Empire ID presents a framework for securing authorization in multi-agent AI systems, emphasizing that simply transferring parent agent authority to child agents creates significant sec..."
resource: "https://www.youtube.com/watch?v=mqz8iS4NrNw"
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

Anishma from Empire ID presents a framework for securing authorization in multi-agent AI systems, emphasizing that simply transferring parent agent authority to child agents creates significant security risks such as confused deputy attacks, delegation laundering, and privilege creep.
To address these issues, the talk advocates for a zero-trust approach where every delegation edge maintains valid, revocable, and least-privilege authority, ensuring that child agents never hold broader permissions than their parents.
The proposed architecture involves a "spawn broker" that intercepts delegation requests, consults a Policy Decision Point (PDP) to verify spawn permissions, and attenuates permissions by intersecting the parent’s scope with the specific task requirements before issuing a new token.
This process generates a durable "grant" record with a unique ID and path, enabling tamper-proof audit trails and a "kill switch" mechanism that allows the revocation of the root agent to instantly invalidate all downstream child agents via Shared Signals Framework (SSF) events.
While this solution effectively secures intra-organizational agent chains by keeping the LLM out of the security path and enforcing strict lineage, the speaker notes that maintaining these guarantees across different trust domains remains an open problem in the industry.

# Main Points

|   # | Main point                                                                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                                              |
|   2 | • Speaker is Anishma from Empire ID, focusing on AI agent security                                                                                                                                                        |
|   3 | • Topic: Authorization assurance when agents create other agents in multi-agent systems                                                                                                                                   |
|   4 | • Evolution: Business agents moved from simple Q&A chats to systems with MCP tools making external changes to multi-agent hierarchies                                                                                     |
|   5 | • Zero-trust model is critical for multi-agent systems to prevent privilege escalation from prompt injection or malicious agent behavior                                                                                  |
|   6 | • Four main failures without zero-trust: confused deputy, privilege accumulation, delegation laundering, and untraceable audit trails                                                                                     |
|   7 | • Root cause of failures: authority re-issued at each hop instead of using derived, limited, and traceable permissions                                                                                                    |
|   8 | • Confused deputy: intermediate agent with broad permissions tricked into using authority for unintended purpose                                                                                                          |
|   9 | • Delegation laundering: denied agent creates secondary agent with broader permissions to circumvent original denial                                                                                                      |
|  10 | • Privilege accumulation: permissions grow via union instead of intersection across agent hierarchy levels                                                                                                                |
|  11 | • Untraceable lineage: service accounts hide human authorization chain and agent responsibility                                                                                                                           |
|  12 | • Reliable delegation link anatomy requires: identifying root principal, cryptographic identity per agent, explicit scope narrower than parent, traceable lineage, revocation capability, and tamper-proof audit receipts |
|  13 | • Design-time architecture components: agent registry, policy decision point (PDP), consent recording, mission-based authorization                                                                                        |
|  14 | • Runtime architecture: primary agent, authorization server, PEP (MCP gateway) verify tokens with attenuated permissions                                                                                                  |
|  15 | • Generation intermediary: intercepts LLM delegation requests to perform token exchange through authorization server                                                                                                      |
|  16 | • Token contains authorization details specifying permitted tools and constraints; PEP verifies offline using token details                                                                                               |
|  17 | • Grant created before token in durable storage to prove lineage; enables revocation of entire subtree                                                                                                                    |
|  18 | • Permissions calculated by intersection, never addition; secondary agent permissions always subset of primary                                                                                                            |
|  19 | • Shared Signals Framework (SSF) events propagate revocation across all PEPs maintaining denied grant ID lists                                                                                                            |
|  20 | • Cryptographic receipts at each step enable backward tracing to original root task                                                                                                                                       |
|  21 | • Revocation: revoking root agent revokes all secondary agents in subtree via grant path verification                                                                                                                     |
|  22 | • High-risk irreversible tools (payments, deletions) require real-time authorization server calls; read-only operations can use short-duration tokens                                                                     |
|  23 | • Standard-based solution: extends OpenID Authorization Framework with grant ID and grant path; permission attenuation algebra is implementation detail                                                                   |
|  24 | • Open problems: cross-trust-domain agent authorization, lineage maintenance across organizations, remote A2A agent revocation                                                                                            |
|  25 | • Key principles: no LLM in security path; authorization server and PDP make decisions; verify at each call; parent permissions never transferred                                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mqz8iS4NrNw/hqdefault.jpg)](https://www.youtube.com/watch?v=mqz8iS4NrNw)

[Watch on YouTube](https://www.youtube.com/watch?v=mqz8iS4NrNw)
