---
layout: default
title: "How Open Standards Solve the Missing Identity Layer for AI... - Aaron Parecki & Danny Zollner, Okta"
nav_order: 133
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: Danny Zolner and Aaron Parecki from Okta discuss how open identity standards are essential for solving governance challenges posed by the rapid deployment of AI agents in enterprises.
resource: "https://www.youtube.com/watch?v=IfAxktGni_I"
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

Danny Zolner and Aaron Parecki from Okta discuss how open identity standards are essential for solving governance challenges posed by the rapid deployment of AI agents in enterprises.
They highlight that current gaps in identity management lead to shadow IT and compliance risks, necessitating standardized solutions that no single company can provide alone.
The presentation focuses on three key standards: Cross-App Access, an OAuth extension that allows agents to securely access user data across different applications; the Workload Authorization Grant, a new draft enabling autonomous agents to act on their own behalf without static API keys; and the extension of SCIM protocols to manage the full lifecycle and governance of non-human identities.
These standards aim to replace insecure practices like shared credentials with secure, token-based access models that are already being implemented by major platforms like Claude, Cursor, and various SaaS providers.
The speakers urge industry participants to actively engage in IETF working groups to help refine these specifications, emphasizing that consensus-driven development requires broad input to effectively address the scaling and security needs of the emerging AI agent ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , with 91% of organizations currently using them.                                                                                                                                                                            |
|   2 | , a ratio Gartner predicts will rise to 150,000 agents per Fortune 500 company by 2028.                                                                                                                                      |
|   3 | : 52% of employees use AI tools without IT approval, 80% use shadow IT, and 84% of organizations doubt they could pass a compliance audit on agent behavior.                                                                 |
|   4 | ; proprietary solutions lead to fragmented, hard-to-manage API integrations.                                                                                                                                                 |
|   5 | (e.g., Claude, Cursor) to access data from enterprise apps (e.g., Atlassian, Slack) via a back-channel token exchange through a shared Identity Provider, eliminating the need for static API keys or manual user approvals. |
|   6 | , including Cloudflare, Okta, and various SaaS platforms.                                                                                                                                                                    |
|   7 | (WAG)** addresses autonomous agents acting on their own behalf without a specific user context.                                                                                                                              |
|   8 | , which are then exchanged for access tokens by resource servers, removing the need for shared or static credentials.                                                                                                        |
|   9 | , with prototypes planned for Okta and Anthropic, and feedback is sought as it prepares for IETF adoption.                                                                                                                   |
|  10 | (System for Cross-domain Identity Management)** is proposed to manage agent lifecycle and governance, similar to how it manages human users and groups.                                                                      |
|  11 | "at rest" or proactively enumerate them; SCIM provides a consistent attribute model for this.                                                                                                                                |
|  12 | % of organizations lack documented policies for creating or removing AI identities, highlighting the need for centralized inventory and provisioning workflows.                                                              |
|  13 | , and the standard is in the earliest stages of development compared to the other two.                                                                                                                                       |
|  14 | ; contributors are encouraged to join mailing lists to shape these standards, particularly during the SCIM rechartering process.                                                                                             |
|  15 | (via OAuth/Cross-App Access and WAG) before addressing lifecycle management (via SCIM).                                                                                                                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/IfAxktGni_I/hqdefault.jpg)]("https://www.youtube.com/watch?v=IfAxktGni_I")

[Watch on YouTube](https://www.youtube.com/watch?v=IfAxktGni_I)
