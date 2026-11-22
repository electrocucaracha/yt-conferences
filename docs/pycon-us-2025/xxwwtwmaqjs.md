---
layout: default
title: "Safeguard your precious API endpoints built on FastAPI using OAuth 2.0 - Semona Igama"
nav_order: 88
parent: PyCon US 2025
type: Video Note
description: "Simone Gama, a developer advocate at Okta, presented a session on safeguarding API endpoints built with FastAPI using OAuth 2.0 and OpenID Connect."
resource: "https://www.youtube.com/watch?v=XxWWTwmaQJs"
youtube_stats:
  view_count: 942
  like_count: 19
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Simone Gama, a developer advocate at Okta, presented a session on safeguarding API endpoints built with FastAPI using OAuth 2.0 and OpenID Connect.
She emphasized that security is often treated as an afterthought despite the rising threat of identity-based data breaches, urging developers to adopt a "secure first" mindset.
The talk covered the history of OAuth, the distinction between access and ID tokens, and the recommended Authorization Code Flow with PKCE for modern web and mobile applications.
Gama demonstrated how to implement these standards in FastAPI by leveraging built-in security features like the HTTP Bearer scheme and dependency injection, while using the `authlib` library to validate tokens either locally or via remote introspection.
She concluded by advising developers to rely on established Identity Providers rather than building custom authentication solutions, ensuring robust token management and compliance with current security best practices.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker introduces a talk on safeguarding API endpoints built with FastAPI using OAuth 2.0 and OpenID Connect.                                                                                 |
|   2 | Security is often treated as an afterthought in software development, despite over 80% of data breaches stemming from identity attacks.                                                            |
|   3 | OAuth was introduced in 2006-2007 to solve delegated access issues, replacing the insecure practice of sharing usernames and passwords.                                                            |
|   4 | OpenID Connect extends OAuth to provide user identity verification, addressing the limitation of OAuth which only grants access tokens without identifying the user.                               |
|   5 | Different OAuth flows are recommended for different application types, with the Authorization Code Flow with PKCE being the current best practice for web, SPA, and mobile apps.                   |
|   6 | Key roles in the OAuth flow include the resource owner, client, authorization server, and resource server.                                                                                         |
|   7 | Access tokens are now in JWT format, allowing applications to validate them locally without relying solely on the authorization server.                                                            |
|   8 | FastAPI provides built-in security features such as the HTTP Bearer scheme, OpenAPI documentation integration, and dependency injection for reusable security functions.                           |
|   9 | The speaker demonstrates a FastAPI backend using the `authlib` library to validate access tokens from an identity provider like Okta.                                                              |
|  10 | Token validation can be performed locally by checking keys and claims or remotely via the introspection endpoint, with remote validation being more expensive but ensuring real-time status.       |
|  11 | Best practices include using industry-standard protocols, preferring token-based security over static API keys for better control and revocation capabilities, and utilizing an Identity Provider. |
|  12 | The Model Context Protocol (MCP) draft incorporates OAuth 2.1 best practices and uses the Authorization Code Flow with PKCE for secure token acquisition.                                          |
|  13 | Developers are encouraged to use established identity providers rather than building custom authentication solutions to ensure resilience and security.                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XxWWTwmaQJs/hqdefault.jpg)](https://www.youtube.com/watch?v=XxWWTwmaQJs)

[Watch on YouTube](https://www.youtube.com/watch?v=XxWWTwmaQJs)
