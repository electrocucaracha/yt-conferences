---
layout: default
title: "Evolution, not Revolution: How MCP is Reshaping OAuth - Aaron Parecki, Okta"
nav_order: 64
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Aaron Parecki, an editor for OAuth 2.1 and a key figure in the MCP OAuth working group, presents a talk on how the Model Context Protocol (MCP) is driving the evolution of OAuth standards to addres..."
resource: "https://www.youtube.com/watch?v=eSPm7I2bm1M"
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

Aaron Parecki, an editor for OAuth 2.1 and a key figure in the MCP OAuth working group, presents a talk on how the Model Context Protocol (MCP) is driving the evolution of OAuth standards to address modern challenges.
He explains that while OAuth was originally designed to replace insecure password sharing with scoped access tokens, the rise of AI agents and MCP servers has exposed limitations in traditional client identification, dynamic discovery, and enterprise user experience.
To solve the issue of unauthenticated dynamic client registration, Parecki advocates for Client ID Metadata Documents, which allow applications to host their own identity information, enabling scalable and secure integration with unknown OAuth servers.
Additionally, he highlights the importance of dynamic discovery specifications that allow MCP clients to automatically locate necessary OAuth endpoints from a single server URL, removing the need for hardcoded configurations.
Finally, he addresses "click-through fatigue" in enterprise environments by introducing the Identity Assertion Job Authorization Grant (ID JAG), a mechanism that allows AI agents to securely access multiple enterprise applications behind the scenes using tokens issued by the Identity Provider, thereby eliminating repetitive user consent prompts while maintaining administrative visibility and control.

# Main Points

|   # | Main point                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Aaron Parecki from Okta is involved in OAuth 2.1, Client ID Metadata Documents, and the MCP OAuth working group.                                                                                                          |
|   2 | : Created to replace the insecure practice of sharing passwords with third-party apps (e.g., Yelp accessing email contacts) by allowing granular data access without exposing credentials.                                  |
|   3 | : OAuth uses access tokens (analogous to hotel key cards) to grant specific permissions, ensuring users can revoke access and limit scope, unlike shared passwords.                                                         |
|   4 | : A key design goal is the authorization server prompt, which ensures users explicitly agree to share specific data with an application.                                                                                    |
|   5 | : Model Context Protocol (MCP) enables agents to connect to unknown servers dynamically, breaking the traditional model where developers pre-register apps with specific providers.                                         |
|   6 | : Dynamic Client Registration (DCR) fails at scale because it creates unauthenticated, uncorrelated registrations for every app instance, leading to database bloat and security risks.                                     |
|   7 | : A new IETF draft solution where clients host their own metadata (name, logo, redirect URIs) at a URL, providing a stable identity for OAuth servers without manual registration.                                          |
|   8 | : Traditional OAuth requires hardcoded endpoints. MCP requires a discovery mechanism to find OAuth server metadata from a single MCP server URL, a spec recently published to support this.                                 |
|   9 | : In enterprise environments, users face repetitive consent screens when connecting AI agents to multiple apps, creating poor UX and security blind spots for admins.                                                       |
|  10 | (ID JAG)**: A solution using token exchange (RFC 7523) where an Identity Provider issues a signed JWT (ID JAG) to an agent, allowing it to access other enterprise apps behind the scenes without further user interaction. |
|  11 | : ID JAG allows the Identity Provider to remain in the loop for auditing and policy enforcement, while eliminating the need for users to repeatedly click through consent screens.                                          |
|  12 | : Client ID Metadata Documents and Discovery specs are adopted drafts; ID JAG is deployed in enterprise MCP implementations like Claude.                                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eSPm7I2bm1M/hqdefault.jpg)]("https://www.youtube.com/watch?v=eSPm7I2bm1M")

[Watch on YouTube](https://www.youtube.com/watch?v=eSPm7I2bm1M)
