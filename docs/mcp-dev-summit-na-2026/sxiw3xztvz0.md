---
layout: default
title:
  "URL Elicitation Deep Dive: Third-party OAuth Solved (and More!) - Nate Barbettini,
  Arcade.dev"
nav_order: 103
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Nate, a founding engineer at Arcade, introduces the concept
  of URL elicitation, a new feature in the MCP protocol designed to securely handle
  sensitive user interactions, such as payments or OAuth authorization, without exposi...
resource: https://www.youtube.com/watch?v=sXIw3xZTVZ0
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

In this talk, Nate, a founding engineer at Arcade, introduces the concept of URL elicitation, a new feature in the MCP protocol designed to securely handle sensitive user interactions, such as payments or OAuth authorization, without exposing confidential data to either the client or the underlying model.
He explains that URL elicitation allows an MCP server to send a secure URL directly to the client, prompting the user to complete sensitive actions—like entering a credit card number or authorizing access—in a trusted browser environment, rather than through chat or the client interface.
This approach maintains strict trust boundaries, ensuring that sensitive information never passes through the model or client, and is particularly useful for integrating with external APIs that require OAuth or similar flows.
Nate also addresses security considerations, such as phishing risks and the need for trusted registries, and notes that while adoption across clients is still uneven, the feature is gaining support and provides a robust foundation for secure, user-mediated interactions in the MCP ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nate, founding engineer at Arcade, presented on the MCP feature "URL elicitation"                                                                                                             |
|   2 | Arcade builds an MCP runtime focused on governance, security, and permissions                                                                                                                 |
|   3 | URL elicitation provides MCP servers a secure way to cross trust boundaries                                                                                                                   |
|   4 | Sensitive interactions (e.g., payments) should not be handled via chat messages or exposed to models/clients                                                                                  |
|   5 | Ideal flow: server sends a secure URL to the client, client asks user for consent, user completes sensitive action (e.g., payment) in a trusted browser environment                           |
|   6 | Sensitive data (e.g., credit card numbers) never enters the chat, model, or client; only the trusted third-party (e.g., Stripe, PayPal) receives it                                           |
|   7 | Server receives confirmation of action (e.g., payment) without accessing sensitive data                                                                                                       |
|   8 | URL elicitation is now part of the MCP spec; user consent is required before opening URLs                                                                                                     |
|   9 | Keeps sensitive data out of both the model and the client, not just the model                                                                                                                 |
|  10 | Other approaches (e.g., entering data in the client UI) are less secure as they expose data to the client                                                                                     |
|  11 | Demo: client receives a URL from the server, user chooses to open it, server is notified upon completion                                                                                      |
|  12 | URL elicitation also applies to third-party OAuth scenarios, maintaining strict trust boundaries                                                                                              |
|  13 | MCP spec forbids token reuse between client-server and external APIs to prevent security vulnerabilities                                                                                      |
|  14 | MCP server is not a proxy; it maintains its own OAuth scopes and tokens                                                                                                                       |
|  15 | Correct pattern: server triggers URL elicitation for external authorization, user completes flow in browser, server receives necessary token, sensitive data never exposed to model or client |
|  16 | Mechanism is generic: useful for payments, OAuth, API keys, passwords, and other sensitive data entry                                                                                         |
|  17 | Supported in MCP since November release; Visual Studio Code, Cursor, and Cloud Code clients support it                                                                                        |
|  18 | Adoption across clients is slow; more SDK and conformance suite support needed                                                                                                                |
|  19 | Security considerations: URLs should not expose sensitive parameters; provenance and trust of MCP set                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=sXIw3xZTVZ0)
