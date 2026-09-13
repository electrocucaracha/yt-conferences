---
layout: default
title:
  "Golem To Murderbot: Challenges With Agentic Security Delegation Via MCP -
  Michael Schwartz, Gluu"
nav_order: 31
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Mike Schwarz, founder of Glue, explores the challenges
  of agentic security delegation using metaphors from the golem legend and Martha
  Wells’ Murderbot series to illustrate issues of intent, control, and risk in AI
  agents. He...
resource: https://www.youtube.com/watch?v=ixQorHltcfw
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

In this talk, Mike Schwarz, founder of Glue, explores the challenges of agentic security delegation using metaphors from the golem legend and Martha Wells’ Murderbot series to illustrate issues of intent, control, and risk in AI agents.
He argues that while human and software authentication are largely solved problems, delegation and authorization—especially in complex, automated environments—remain difficult, with current solutions like OAuth and UMA falling short.
Schwarz emphasizes the need for multi-layered, embedded security rather than relying solely on gateways, and advocates for centralized policy management using analyzable policy engines like Cedar.
He introduces a governance framework with layers for risk management, identity (for accountability), visibility, and event response, stressing that effective governance requires transparency, accountability, and communication in terms understandable to organizational leadership.
The talk concludes with a call to rethink governance processes and to adopt new tools and frameworks for managing risk and security in increasingly automated IT landscapes.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk is titled "Golem to Murderbot: Challenges with Agentic Security Delegation via MCP" by Mike Schwarz, founder of Glue.                                                    |
|   2 | The golem story raises questions about trusting AI agents to perform intended actions and the need for a "kill switch."                                                           |
|   3 | The golem is unstable, soulless, and not desirable; the story is used as a metaphor for agentic security.                                                                         |
|   4 | Martha Wells' "Murderbot" series provides metaphors for agent governance, including the governor module (controls/punishes agents) and hub system (monitors/logs agent activity). |
|   5 | Insurance in "Murderbot" is a metaphor for monetizing risk, influencing IT decisions.                                                                                             |
|   6 | Modern IT environments (e.g., Amazon microservices) are too complex for manual review; automation is needed for security.                                                         |
|   7 | Zero trust security requires multi-layer defense, not just at the MCP gateway; security/policy should be embedded in all components, especially close to data.                    |
|   8 | Human authentication is considered a solved problem due to passkeys and digital wallets.                                                                                          |
|   9 | Federated authentication (social login) and secure software authentication (asymmetric) are also considered solved, though shared secrets remain problematic.                     |
|  10 | Agent registration/discovery needs improvement; authentication itself is solved.                                                                                                  |
|  11 | Digital identity relies on cryptographically signed proofs: attestations (self-asserted) and assertions (event-based).                                                            |
|  12 | Delegation via OAuth is not a solved problem; existing patterns (e.g., UMA) are complex and lack adoption.                                                                        |
|  13 | Authenticity degrades with each network hop; skepticism is advised regarding delegation solutions.                                                                                |
|  14 | Authorization should focus on actions on resources within context, not just on identity.                                                                                          |
|  15 | Access alone is insufficient; obligations and restrictions must be considered.                                                                                                    |
|  16 | Role-based access control is inadequate for environments with more software than humans.                                                                                          |
|  17 | Centralized policy management and authorization engines are emerging; three types: rego/cel (flexible), graphs (efficient with complete data), cedar (analyzab                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ixQorHltcfw)
