---
layout: default
title: Enterprise Challenges with MCP Adoption - Christian Posta, Solo.io
nav_order: 102
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Christian Posta, Global Field CTO at Solo.io, discusses the adoption
  of the Model Context Protocol (MCP) in enterprises, highlighting challenges faced
  when moving from pilot projects to production, particularly around security, tenancy,
  obs...
resource: https://www.youtube.com/watch?v=ipKgoKSkBnc
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Christian Posta, Global Field CTO at Solo.io, discusses the adoption of the Model Context Protocol (MCP) in enterprises, highlighting challenges faced when moving from pilot projects to production, particularly around security, tenancy, observability, and compliance.
He notes that while MCP enables AI models to interact with external data and services through a unified protocol, the original spec was not designed with enterprise needs in mind, leading to concerns about credential management and policy enforcement.
Posta demonstrates how Solo.io’s open source agent registry and agent gateway can help enterprises securely onboard and manage remote MCP servers, integrate with internal identity providers for authentication, and apply fine-grained access policies.
He critiques the MCP authentication spec for its reliance on public internet OAuth flows and dynamic client registration, which are not suitable for most enterprise environments, and instead advocates for leveraging existing enterprise identity systems.
Finally, he addresses the complexities of securely connecting to external SaaS MCP servers, outlining current limitations and interim solutions involving token vaults and policy-managed gateways, and invites further discussion and feedback from the community.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on MCP (Model Context Protocol) adoption in organizations and associated challenges.                                                                       |
|   2 | MCP enables AI models to access external data and functionality via a unified protocol, reducing the need for custom code.                                                      |
|   3 | Enterprises began adopting MCP around summer 2025, encountering issues with security, tenancy, observability, logging, and compliance.                                          |
|   4 | The MCP community acknowledges enterprise challenges and is seeking input, but plans to address enterprise needs as extensions rather than core spec features.                  |
|   5 | Enterprises are concerned about managing credentials (API keys, tokens) and compliance when MCP servers call external APIs or SaaS endpoints.                                   |
|   6 | Recommendation: MCP servers that call remote endpoints should be remote, not local, and exposed via HTTP transport.                                                             |
|   7 | Enterprises need consistent authentication, authorization, telemetry, access logs, and policy enforcement for MCP, similar to established API management practices.             |
|   8 | Gateways and registries are used to manage and expose MCP servers securely within enterprises.                                                                                  |
|   9 | Solo.io donated their open-source agent registry to CNCF, supporting MCP server management and deployment.                                                                      |
|  10 | Demo showcased adding a remote MCP server to a registry, exposing it via an agent gateway, and deploying it to Kubernetes.                                                      |
|  11 | MCP authentication (MCP auth) spec initially lacked enterprise focus, relying on OAuth flows (authorization code, dynamic client registration) unsuitable for most enterprises. |
|  12 | Enterprises prefer tying access to internal identity providers (e.g., Okta, Azure) and single sign-on, not public OAuth flows.                                                  |
|  13 | MCP auth spec does not address tool-level access control within MCP servers.                                                                                                    |
|  14 | Gateways can enforce policies, filter tool access, and integrate with enterprise SSO for user authentication and authorization.                                                 |
|  15 | Challenges exist when connecting to external SaaS MCP servers, as federated SSO does not solve authorization for scoped access tokens.                                          |
|  16 | Industry initiatives (e.g., JAT/JAG token exchange) for                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ipKgoKSkBnc)
