---
layout: default
title: "Tips and Tricks for JSON Web Tokens (JWTs) - Emin Martinian"
nav_order: 87
parent: PyCon US 2025
type: Video Note
description: "Emmen Martinian presents a comprehensive overview of JSON Web Tokens (JWTs), highlighting their utility as a secure, stateless alternative to traditional cookies and sessions for authentication and..."
resource: "https://www.youtube.com/watch?v=CX15E_djxvI"
youtube_stats:
  view_count: 1173
  like_count: 31
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

Emmen Martinian presents a comprehensive overview of JSON Web Tokens (JWTs), highlighting their utility as a secure, stateless alternative to traditional cookies and sessions for authentication and authorization.
The talk explains how JWTs enable the separation of authentication from validation, allowing highly secure authentication servers to manage secret keys while application servers use public keys to verify tokens, thereby simplifying deployment and scaling.
Martinian demonstrates practical Python implementations using Flask decorators to validate tokens, check specific claims, and handle proxy use cases where one user acts on behalf of another.
He also addresses critical security caveats, emphasizing the necessity of whitelisting cryptographic algorithms and key identifiers to prevent attacks such as algorithm confusion or key substitution.
Finally, the presentation details the access and refresh token flow, explaining how short-lived access tokens combined with revocable refresh tokens provide a robust mechanism for managing token expiration and revocation in stateless architectures.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | JSON Web Tokens (JWTs) are compact, standardized, and secure alternatives to cookies and sessions for authentication and authorization in stateless systems.                                        |
|   2 | Separating authentication from validation allows application servers to use public keys only, simplifying security management and enabling scalable, serverless deployments.                        |
|   3 | A JWT consists of a base64 encoded header, payload containing claims, and a cryptographic signature that validates the payload integrity.                                                           |
|   4 | Standardized payload fields include 'sub' for the subject, 'iat' for issued at, 'exp' for expiration, and 'nbf' for not before, which help manage token lifecycle.                                  |
|   5 | Python developers can use decorators with libraries like PyJWT to validate tokens, check specific claims, and enforce permissions on Flask routes.                                                  |
|   6 | The proxy use case allows one user to act on behalf of another by including a 'proxy' field in the claims, distinguishing the real user from the effective user.                                    |
|   7 | Security best practices require whitelisting accepted algorithms and key IDs in the header to prevent attacks where attackers manipulate the header to use symmetric keys or malicious public keys. |
|   8 | JWTs are not sessions and cannot be easily revoked; therefore, they should not be used to simulate long-lived session states on stateless servers.                                                  |
|   9 | The access and refresh token flow solves revocation issues by using short-lived access tokens for service requests and long-lived refresh tokens to obtain new access tokens.                       |
|  10 | If a device is compromised, revoking the refresh token at the authentication server prevents further access token generation, limiting the attacker's window of opportunity.                        |
|  11 | Middleware can be used to verify JWT signatures before requests reach the application code, providing a centralized security layer that protects static routes and simplifies security audits.      |
|  12 | Refresh tokens should be stored securely and only sent to the authentication server, never to application servers, to prevent unauthorized access token generation.                                 |
|  13 | Best practices recommend keeping access tokens very short-lived (e.g., 30 seconds) and refresh tokens reasonably long-lived (e.g., days or weeks) with a logout mechanism to cancel them.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CX15E_djxvI/hqdefault.jpg)](https://www.youtube.com/watch?v=CX15E_djxvI)

[Watch on YouTube](https://www.youtube.com/watch?v=CX15E_djxvI)
