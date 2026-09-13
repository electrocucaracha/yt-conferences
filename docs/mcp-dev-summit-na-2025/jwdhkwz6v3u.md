---
layout: default
title: "[Session] Building Protected MCP Servers with MCP - Den Delimarsky from Microsoft"
nav_order: 13
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  The speaker, a Microsoft engineer, introduces a new draft authorization
  specification for the Model Context Protocol (MCP), developed collaboratively with
  the MCP community and partners like Okta and AWS. This specification separates the
  re...
resource: https://www.youtube.com/watch?v=jwDHkWZ6V3U
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker, a Microsoft engineer, introduces a new draft authorization specification for the Model Context Protocol (MCP), developed collaboratively with the MCP community and partners like Okta and AWS.
This specification separates the resource server from the authorization server, allowing developers to use off-the-shelf authorization solutions and reducing the complexity of implementing OAuth 2.1.
The new C# MCP SDK makes it simple for developers to add secure authorization to their MCP servers with minimal configuration, supporting various identity providers and focusing on ease of use and extensibility.
The demo shows how both server and client code can be quickly set up to handle authorization flows, token validation, and integration with tools like Visual Studio Code, emphasizing developer ergonomics and plug-and-play functionality.
The speaker concludes by highlighting that the SDK is designed to be accessible even for those without deep security expertise and invites further questions about the project.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter works at Microsoft, known for MS Dawson Basic.                                                                                                        |
|   2 | Focus of talk: simplifying authorization in MCP using the C SDK and a new authorization specification.                                                          |
|   3 | New authorization spec for Model Context Protocol (MCP) is in draft, developed with significant community contributions (partners include Okta, AWS, Entra ID). |
|   4 | Spec introduces separation between resource server and authorization server, reducing complexity for MCP server developers.                                     |
|   5 | Enables use of off-the-shelf authorization servers from any identity provider (Okta, AWS, Entra ID, etc.) while following OAuth 2.1 standards.                  |
|   6 | Developer burden is minimized to one extra request for authorization.                                                                                           |
|   7 | MCP server returns a 401 with a pointer to a protected resource metadata document if client is unauthorized.                                                    |
|   8 | Client retrieves and parses the metadata document (JSON or JWT) to identify the authorization server and initiate the flow.                                     |
|   9 | Tokens are returned to the client after authorization, enabling access to the MCP server.                                                                       |
|  10 | Goal: make integration simple and intuitive, requiring minimal security expertise from developers.                                                              |
|  11 | Solution is designed to be idiomatic for C# developers and compatible with .NET ecosystem (including Azure).                                                    |
|  12 | SDK is extensible for future authorization approaches.                                                                                                          |
|  13 | Work-in-progress pull request for MCP C# SDK adds support for the new authorization spec.                                                                       |
|  14 | Server setup uses builder pattern in ASP.NET Core; works with any OAuth provider.                                                                               |
|  15 | Server configuration includes authentication, token validation, and hosting protected resource metadata.                                                        |
|  16 | Client implementation uses a generic OAuth provider interface (IMCPCredentialProvider) for flexible authorization logic.                                        |
|  17 | Demo shows local server and client exchanging tokens and validating authorization.                                                                              |
|  18 | Visual Studio Code now supports the new authorization spec; can connect to MCP servers and reuse existing credentials (e.g., Entra ID, GitHub).                 |
|  19 | No need for dynamic client registration if client is already registered with the identity prov                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jwDHkWZ6V3U)
