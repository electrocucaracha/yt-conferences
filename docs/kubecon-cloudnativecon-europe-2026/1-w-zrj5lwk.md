---
layout: default
title:
  "Project Lightning Talk: OpenFGA For Agents: Safe Delegation In 5 Minutes -
  Andres Aguiar, Maintainer"
nav_order: 282
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Andreas, an OpenFGA maintainer, presents on behalf of Sedant, introducing
  OpenFGA as an authorization service for developers inspired by Google Zanzibar,
  which enables relationship-based access control and is designed for scalability.
  The p...
resource: https://www.youtube.com/watch?v=1_w_ZRJ5lWk
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

Andreas, an OpenFGA maintainer, presents on behalf of Sedant, introducing OpenFGA as an authorization service for developers inspired by Google Zanzibar, which enables relationship-based access control and is designed for scalability.
The project has recently been accepted into incubation and now supports the OpenID Zen 1.0 specification, with notable improvements in performance, as demonstrated by Docker’s latency metrics.
Andreas explains how OpenFGA allows fine-grained, per-task, and per-resource permissions, using authorization models to define entities and relationships, which can be applied to various domains such as project management systems.
He demonstrates two agent use cases: an interactive mode where users approve permissions as needed, and an autonomous mode where permissions are inferred and granted automatically, both ensuring agents only perform authorized actions.
The presentation concludes with an invitation to further discussions and a mention of upcoming integrations with other technologies.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Andreas is presenting on behalf of Sedant, an Open FGA maintainer.                                                                                                        |
|   2 | Open FGA is an authorization service for developers, inspired by Google Zanzibar.                                                                                         |
|   3 | Zanzibar powers Google Docs, Google Cloud, and YouTube, and is designed for large scale and high data volume.                                                             |
|   4 | Open FGA extends Zanzibar concepts with developer tooling for application use.                                                                                            |
|   5 | There is an adopters MD page listing companies using Open FGA.                                                                                                            |
|   6 | Open FGA was recently accepted into incubation.                                                                                                                           |
|   7 | Support for OpenZan 1.0 (an OpenID specification for authorization checks) was launched.                                                                                  |
|   8 | Performance improvements have been made, with reduced latency shown by Docker’s migration.                                                                                |
|   9 | Presented a use case for agents needing credentials with restricted, ephemeral, per-task permissions.                                                                     |
|  10 | In Open FGA, an authorization model defines relevant entities and permissions.                                                                                            |
|  11 | Example: Modeling tools and parameters, assigning fine-grained permissions per task and resource.                                                                         |
|  12 | Permissions can be set at any level of a hierarchy (e.g., project, ticket).                                                                                               |
|  13 | Intent-based authorization: An LLM interprets a prompt to infer required permissions for an agent.                                                                        |
|  14 | Two modes: interactive (user approves permissions) and autonomous (permissions granted automatically).                                                                    |
|  15 | Demo 1 (interactive): Agent requests permissions to summarize a project and post to Slack; prompt injection tries to send an email, but permission is denied by the user. |
|  16 | Demo 2 (autonomous): Agent infers permissions, detects prompt injection, cancels the task due to insufficient permissions.                                                |
|  17 | Two scenarios demonstrated: interactive and autonomous agent permission handling.                                                                                         |
|  18 | Mention of upcoming presentations and Open FGA integration with Envoy.                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1_w_ZRJ5lWk)
