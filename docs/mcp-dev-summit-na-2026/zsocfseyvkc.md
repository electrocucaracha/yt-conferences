---
layout: default
title: "Evolution, Not Revolution: How MCP Is Reshaping OAuth - Aaron Parecki, Okta"
nav_order: 86
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Aaron Parecki, an expert at Okta and the IETF, discusses how the Model Context Protocol (MCP) is driving the evolution of OAuth standards to accommodate decentralized AI agents."
resource: "https://www.youtube.com/watch?v=zsoCFSeYvkc"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Aaron Parecki, an expert at Okta and the IETF, discusses how the Model Context Protocol (MCP) is driving the evolution of OAuth standards to accommodate decentralized AI agents.
He explains that traditional OAuth relies on pre-registered clients, which is impractical for MCP where generic clients connect to arbitrary servers; to solve this, the community is adopting client ID metadata documents, allowing clients to publish their identity at a URL rather than requiring manual registration.
Additionally, dynamic discovery is being enhanced through Protected Resource Metadata, enabling a single MCP server URL to bootstrap the entire authentication flow by pointing to the necessary authorization endpoints.
Parecki also addresses enterprise challenges such as "click-through fatigue" and the lack of administrative visibility into AI tool access, proposing the Identity Assertion Authorization Grant (cross-app access) to streamline single sign-on and provide better control.
He concludes by emphasizing that these changes represent an incremental evolution of OAuth, filling specific gaps created by the rapid adoption of MCP while maintaining backward compatibility.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Aaron Parecki from Okta discusses how MCP is shaping the future of OAuth standards.                                                                                               |
|   2 | OAuth was originally created to allow apps to access data without sharing user passwords, solving the security risks of password sharing.                                         |
|   3 | The OAuth flow uses an authorization server to issue limited access tokens, analogous to a hotel key that grants access to specific resources rather than the entire building.    |
|   4 | Traditional OAuth relies on pre-registration where developers manually register their client applications with the authorization server.                                          |
|   5 | MCP breaks this model because users connect generic clients to arbitrary servers, making pre-registration impossible at scale.                                                    |
|   6 | Dynamic Client Registration was initially used to solve client identification but causes operational issues like unbounded database growth and lack of authority for client data. |
|   7 | The new approach uses Client ID Metadata Documents, where clients publish their metadata at a URL and use that URL as the client ID.                                              |
|   8 | Dynamic discovery is required so users can start with a single MCP server URL and have the client automatically find the necessary OAuth endpoints.                               |
|   9 | Protected Resource Metadata is an RFC that allows an MCP server to point to its authorization server metadata, enabling this single-URL bootstrapping.                            |
|  10 | Enterprise environments face click-through fatigue as users must manually approve connections to multiple MCP servers one by one.                                                 |
|  11 | This manual process creates a visibility gap where enterprise admins cannot see the tokens issued to AI tools, leading to shadow AI risks.                                        |
|  12 | The Identity Assertion Authorization Grant, also known as Cross-App Access, is an in-progress draft designed to solve these enterprise visibility and UX issues.                  |
|  13 | Cross-App Access allows an AI tool to obtain a cross-domain token from the enterprise IDP to access other apps without repeated user prompts.                                     |
|  14 | The overall strategy is to evolve OAuth incrementally to fill gaps created by the decentralized nature of MCP clients and servers.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/zsoCFSeYvkc/hqdefault.jpg)](https://www.youtube.com/watch?v=zsoCFSeYvkc)

[Watch on YouTube](https://www.youtube.com/watch?v=zsoCFSeYvkc)
