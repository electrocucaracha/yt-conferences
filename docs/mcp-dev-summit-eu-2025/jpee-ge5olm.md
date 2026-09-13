---
layout: default
title: "[Session] Let's dream big for MCP Auth with Tobin South - WorkOS"
nav_order: 19
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  The speaker, drawing on their background in AI security and experience
  at WorkOS, discusses the challenges and opportunities in designing robust authorization
  (OAuth) and identity management systems for AI-driven MCP (Machine Control Platfo...
resource: https://www.youtube.com/watch?v=jPee-GE5oLM
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker, drawing on their background in AI security and experience at WorkOS, discusses the challenges and opportunities in designing robust authorization (OAuth) and identity management systems for AI-driven MCP (Machine Control Platform) servers.
They emphasize the need to plan for increasing levels of AI autonomy, from simple chatbots to complex, asynchronous agents and sub-agents, highlighting pain points such as dynamic access, least privilege enforcement, and the limitations of current OAuth implementations.
The talk explores both practical solutions—like step-up authentication, client-initiated backchannel auth, and enterprise integrations (SSO, SAML, SCIM)—and more speculative ideas, such as natural language policy enforcement and programmatic delegation of permissions.
Throughout, the speaker stresses the importance of building flexible, secure systems that can adapt to evolving AI use cases, ensuring that as AI agents become more autonomous, access controls remain effective and manageable.
The ultimate goal is to enable safe automation while maintaining robust security and clear identity management, as detailed further in a newly released white paper.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Five previous OR talks at the conference; this talk aims to be more provocative and forward-thinking.                                          |
|   2 | Emphasis on dreaming big for orth and careful design for integration into current specs.                                                       |
|   3 | Speaker has a background in AI security (MIT PhD) and works at Work OS, a security and orth vendor for AI labs.                                |
|   4 | Example: Darren built an MCP server using their product but encountered orth limitations when pushing MCP capabilities.                        |
|   5 | Talk is based on a new 30-page white paper from the OpenID Foundation and Stanford HAI on identity management for AI.                          |
|   6 | Goal: Enable safe, effective automation and increasing AI autonomy.                                                                            |
|   7 | Overview of current orth flow: AI requests access to MCP, authorization server mediates, human approves, AI receives token.                    |
|   8 | Authentication identifies who is accessing; authorization defines what MCP can do.                                                             |
|   9 | Role-based access controls can change MCP behavior and tool availability based on user identity or role.                                       |
|  10 | Security risks and opportunities arise from dynamic, role-based tool access and behavior.                                                      |
|  11 | Challenges include dynamic client registration, developer experience, and moving identity/orth state in UIs.                                   |
|  12 | Higher autonomy: background agents may need dynamic access at runtime, leading to permission request interruptions.                            |
|  13 | Developers often bypass permissions in development, but robust access controls are needed for consumer and financial use cases.                |
|  14 | Proposed solutions: step-up orth, client-initiated backchannel orth, elicitation requests, and possibly natural language policy enforcement.   |
|  15 | Enterprises require integrations with existing security stacks (SSO, SAML, SCIM), robust audit logging, and agent provisioning/deprovisioning. |
|  16 | Emerging standards and proposals: agent identity schemas, cross-app access, token exchange, and attenuated credentials (biscuits, macaroons).  |
|  17 | Increasing autonomy introduces challenges with sub-agents, delegation, and cross-trust boundary access and identity.                           |
|  18 | Payment protocols and web identity offer partial solution                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jPee-GE5oLM)
