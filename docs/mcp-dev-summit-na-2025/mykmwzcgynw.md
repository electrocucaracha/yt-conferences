---
type: Video Note
title: "[Session] Intro to OAuth for MCP Servers with Aaron Parecki, Okta"
description: "Aaron Pari from Octa discusses the complexities and evolution of OAuth, particularly its application within MCP (Modular Component Platform) servers and clients. He explains that OAuth, originally designed to allow applications to access us..."
resource: https://www.youtube.com/watch?v=mYKMwZcGynw
tags: ["mcp-dev-summit-na-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Aaron Pari from Octa discusses the complexities and evolution of OAuth, particularly its application within MCP (Modular Component Platform) servers and clients.
He explains that OAuth, originally designed to allow applications to access user data without sharing passwords, has grown into a collection of specifications, with OAuth 2.1 aiming to simplify and standardize best practices.
Using the analogy of hotel key cards, he illustrates how OAuth access tokens grant specific resource access without exposing user credentials.
Pari emphasizes the importance of separating OAuth server responsibilities from MCP server functions, enabling clients to authenticate and obtain tokens independently before interacting with resource servers.
He also highlights recent advancements like protected resource metadata and dynamic client registration, which streamline client configuration and support interoperability without prior relationships.
Finally, he addresses enterprise scenarios, proposing a model where identity providers (IDPs) mediate application connections for improved security and user experience, shifting token negotiations to the back channel and enhancing visibility for enterprises.
# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Aaron Pari from Octa introduces the session and polls the audience on MCP server, MCP client, and OAuth server development.                                      |
|   2 | The talk focuses on OAuth and its relationship to MCP.                                                                                                           |
|   3 | OAuth specifications are complex and not intended as tutorials; OAuth consists of multiple specs.                                                                |
|   4 | OAuth 2 core spec was published in 2012; many changes and additions have occurred since then.                                                                    |
|   5 | OAuth 2.1 aims to consolidate 13 years of specs and set a new baseline.                                                                                          |
|   6 | MCP remote spec references OAuth 2.1 as best current practice.                                                                                                   |
|   7 | OAuth was created to solve the problem of users giving passwords to third-party apps.                                                                            |
|   8 | OAuth enables applications to access user data without sharing passwords, addressing trust issues.                                                               |
|   9 | Analogy: OAuth access token is like a hotel key card—grants access to resources, not identity.                                                                   |
|  10 | OAuth authorization server issues tokens; resource servers (e.g., MCP servers) validate them.                                                                    |
|  11 | OAuth flow: user is redirected to OAuth server to log in, then redirected back to the client with an authorization code, which is exchanged for an access token. |
|  12 | MCP server only sees the access token at the end of the flow and must validate it per the OAuth server's documentation.                                          |
|  13 | OpenID Connect extends OAuth to provide user identity information (ID token).                                                                                    |
|  14 | MCP aims to allow client configuration with only the server URL, enabled by protected resource metadata.                                                         |
|  15 | Protected resource metadata allows an MCP server to point to a file describing the server, including the OAuth server location.                                  |
|  16 | Dynamic client registration allows clients to register with servers without prior relationships, receiving a client ID and possibly a secret.                    |
|  17 | In enterprise environments, single sign-on is common; OAuth flows are used to connect multiple applications.                                                     |
|  18 | Current user experience for connecting multiple apps is poor and lacks enterprise visibility.                                                                    |
|  19 | Proposal: shift control to the IDP, allowing back-channel token exchanges for better security and user experience.                                               |
|  20 | Blog post available for more                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mYKMwZcGynw)