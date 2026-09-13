---
layout: default
title:
  "Modern PostgreSQL Authorization With Keycloak: Cloud Native... Yoshiyuki Tabata
  & Gabriele Bartolini"
nav_order: 172
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The presentation introduces a new collaboration between two CNCF projects—Keycloak,
  an open-source identity and access management solution, and CloudNativePG, a Kubernetes
  operator for PostgreSQL—to improve authentication and authorization...
resource: https://www.youtube.com/watch?v=TYgPemq06fg
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The presentation introduces a new collaboration between two CNCF projects—Keycloak, an open-source identity and access management solution, and CloudNativePG, a Kubernetes operator for PostgreSQL—to improve authentication and authorization for PostgreSQL databases in cloud-native environments.
With the release of PostgreSQL 18, native OAuth support allows the database to delegate both authentication and authorization directly to Keycloak, enabling users to authenticate with OAuth tokens instead of passwords and centralizing access control.
The speakers demonstrate how this integration works using a custom PostgreSQL OAuth validator for Keycloak, showing how roles and permissions can be managed declaratively in Kubernetes and enforced centrally via Keycloak policies.
The demo illustrates the OAuth 2.0 device authorization flow, where users obtain access tokens from Keycloak to connect to PostgreSQL, and access is granted or denied based on Keycloak’s authorization policies.
This approach externalizes identity and authorization, simplifies governance, and enhances security and scalability for database access in cloud-native architectures.

# Main Points

|   # | Main point                                                                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CNCF enables collaboration and synergy between projects.                                                                                                                                                                                    |
|   2 | Presentation introduces a new collaboration between two CNCF projects to improve authentication and authorization for PostgreSQL databases in cloud native environments.                                                                    |
|   3 | Speakers: Yoshuki Tabata (specialist in API and identity security, Keycloak contributor) and Gabriel Bolini (VP and chief architect for Kubernetes, PostgreSQL contributor).                                                                |
|   4 | Agenda: Introduction to CloudNativePG, overview of Keycloak, demonstration of their integration.                                                                                                                                            |
|   5 | Keycloak: CNCF incubating project, open-source identity and access management solution, supports industry standards (OAuth 2.0, OpenID Connect), integrates with social and enterprise identity providers, centralizes authorization logic. |
|   6 | CloudNativePG: Open-source Kubernetes operator for PostgreSQL, manages full database lifecycle, provides high availability, disaster recovery, and is declarative and Kubernetes-native.                                                    |
|   7 | PostgreSQL 18 introduces native OAuth support, allowing direct delegation of authentication and authorization to Keycloak.                                                                                                                  |
|   8 | Traditional PostgreSQL authentication methods (password, LDAP) create management silos and require manual user synchronization.                                                                                                             |
|   9 | New OAuthBearer SASL mechanism in PostgreSQL 18 enables external token validation and identity-to-role mapping via pluggable validator modules.                                                                                             |
|  10 | No in-box validator modules yet; community is developing them, including for Keycloak.                                                                                                                                                      |
|  11 | Validator modules can be loaded into PostgreSQL containers via extension image volumes or custom images.                                                                                                                                    |
|  12 | New experimental project: PostgreSQL OAuth validator for Keycloak, available on GitHub, works inside and outside Kubernetes.                                                                                                                |
|  13 | Centralized authorization with Keycloak allows policy-driven, scalable, and consistent access control for PostgreSQL.                                                                                                                       |
|  14 | Demo: PSQL client obtains access token from Keycloak using OAuth 2.0 device authorization flow, connects to PostgreSQL, and authorization decisions are enforced by Keycloak.                                                               |
|  15 | Role mapping and authorization are managed centra                                                                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=TYgPemq06fg)
