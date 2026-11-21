---
layout: default
title: "Securing and Protecting Python Applications with Open Keycloak - Samuel Palacios"
nav_order: 2
parent: PyCon US 2026
type: Video Note
description: This presentation by Samuel Palacios explores the integration of OpenID Connect (referred to as Open Kicklock in the transcript) to address security and infrastructure gaps in Python applications.
resource: "https://www.youtube.com/watch?v=BYzqLBkqDaw"
youtube_stats:
  view_count: 371
  like_count: 2
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

This presentation by Samuel Palacios explores the integration of OpenID Connect (referred to as Open Kicklock in the transcript) to address security and infrastructure gaps in Python applications.
The speaker highlights that while Python is widely used, it lacks native application server features such as distributed transactions, clustering, and robust security management, which are standard in Java-based environments.
To solve this, the talk introduces OpenID Connect as a versatile, open-source identity and access manager that provides a single sign-on (SSO) solution, allowing users to access multiple applications through a unified entry point.
This approach simplifies security management by centralizing authentication and authorization, supporting standards like OAuth 2.0 and SAML, and enabling federation with existing systems such as Active Directory or Microsoft Entra ID.
The presentation concludes by detailing the implementation process, which involves creating clients, configuring adapters for various platforms, and leveraging the tool’s administrative console to manage user identities and audit logs effectively.

# Main Points

|   # | Main point                                                                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The talk focuses on cybersecurity and application infrastructure, specifically addressing gaps in Python applications that lack native infrastructure elements like Single Sign-On.                                            |
|   2 | Python is widely used for scripts and diverse applications but requires external tools for infrastructure components such as load balancing, reverse proxies, and security management.                                         |
|   3 | The speaker, Samuel Palacios from Guatemala, has 12 years of experience in cloud and data center infrastructure, supporting teams in securing projects and implementing infrastructure.                                        |
|   4 | The agenda covers application infrastructure concepts, an introduction to OpenID Connect, its features, advantages, disadvantages, and implementation methods.                                                                 |
|   5 | An application server acts as middleware connecting clients to backend systems like databases and queues, with Java being the primary language with formal application server support.                                         |
|   6 | Python web servers like Uvicorn and Gunicorn are lighter and more agile than Java application servers but lack native features for distributed transactions, messaging, clustering, and comprehensive administration consoles. |
|   7 | Java application servers are heavier and more expensive to maintain due to additional layers, while Python servers offer better agility for microservices and asynchronous tasks.                                              |
|   8 | Application security requires elements such as monitoring, observability, multi-factor authentication, authorization, roles, realms, certificates, and secret management.                                                      |
|   9 | Single Sign-On provides a unified entry point for multiple applications, reducing the complexity of managing individual logins across numerous systems.                                                                        |
|  10 | OpenID Connect is an open-source identity and access manager sponsored by the Cloud Native Computing Foundation and supported by Red Hat in an enterprise version.                                                             |
|  11 | OpenID Connect ensures authentication and authorization for all applications with minimal effort, supporting various identity sources including SQL databases, Microsoft Entra, and Active Directory.                          |
|  12 | Key features of OpenID Connect include single login points, clustering capabilities, and compatibility with standards like OpenID Connect, OAuth 2.0, and SAML.                                                                |
|  13 | The system supports federation with social networks like Gmail and Facebook, though protocol changes by these providers may require updates.                                                                                   |
|  14 | OpenID Connect offers a management console for audits and configuration, allowing custom login pages and execution of actions like audits during the login process.                                                            |
|  15 | Adapters facilitate the integration of OpenID Connect into various platforms and technologies, such as AWS and Azure, making deployment easier.                                                                                |
|  16 | Implementation involves setting up OpenID Connect as a container or in Kubernetes, creating clients with specific keys and redirect URLs for application integration.                                                          |
|  17 | Service accounts can be configured within OpenID Connect to manage users, create administrative accounts, or federate with existing directories like Active Directory.                                                         |
|  18 | Python applications can connect to OpenID Connect if they support the required protocols, utilizing available libraries to enable secure single sign-on functionality.                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BYzqLBkqDaw/hqdefault.jpg)](https://www.youtube.com/watch?v=BYzqLBkqDaw)

[Watch on YouTube](https://www.youtube.com/watch?v=BYzqLBkqDaw)
