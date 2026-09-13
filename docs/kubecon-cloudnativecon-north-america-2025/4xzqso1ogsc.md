---
type: Video Note
title: "Project Lightning Talk: OpenFGA: Google Zanzibar Style Authorization Made Developer-Fri... Tyler Nix"
description: "Tyler Nicks, a product manager at Octa, introduces Open FGA, a centralized, developer-friendly authorization system based on relationship-based access control, blending elements of role-based and attribute-based models and inspired by Googl..."
resource: https://www.youtube.com/watch?v=4xZqSO1OGSc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Tyler Nicks, a product manager at Octa, introduces Open FGA, a centralized, developer-friendly authorization system based on relationship-based access control, blending elements of role-based and attribute-based models and inspired by Google’s Zanzibar paper.
Open FGA, now an incubating project within the CNCF, is open-source and maintained by Octa and Grafana, with contributions from companies like Canonical, Docker, Headspace, and GoDaddy.
The system requires an authorization model and tuples (user-relation-object data) to evaluate policies, supporting various databases such as SQLite, Postgres, and MySQL, and offers multiple SDKs.
Open FGA simplifies the creation and iteration of complex, nested permission hierarchies, allowing for cascading and inherited permissions across resources like organizations, folders, and documents.
Tyler invites interested developers to connect at the project pavilion and attend further talks on Open FGA.
# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tyler Nicks is a product manager at Octa overseeing the Open FGA project.                                                    |
|   2 | Open FGA is a centralized authorization system designed for developers.                                                      |
|   3 | It uses relationship-based access control, combining role-based and attribute-based access control.                          |
|   4 | Inspired by Google’s Zanzibar authorization system.                                                                          |
|   5 | Open FGA is an open-source project based on Zanzibar’s concepts.                                                             |
|   6 | Recently graduated from a sandbox project to an incubating project in the CNCF.                                              |
|   7 | Octa donated Open FGA to the CNCF in September 2022.                                                                         |
|   8 | Open FGA joins 36 other incubating projects, including Open Policy Agent and Keycloak, in the security and compliance space. |
|   9 | Maintained by Octa and Grafana, with contributions from companies like Canonical, Docker, Headspace, and GoDaddy.            |
|  10 | Special thanks to Grafana, Docker, Aicap, Zuplo, and Reed AI for participating in CNCF due diligence interviews.             |
|  11 | Two main components are needed for Open FGA to evaluate authorization:                                                       |
|  12 | Authorization model: defines object types (resources) and roles (e.g., admin, member).                                       |
|  13 | Tuples: data entries representing user, relation, and object (e.g., Marie is a member of Acme organization).                 |
|  14 | Tuples are written to Open FGA and stored in a centralized data store (supports in-memory, SQLite, Postgres, MySQL).         |
|  15 | SDKs available for Go and other popular languages.                                                                           |
|  16 | Permissions are checked using the Check API (e.g., does Marie have edit rights in Acme organization).                        |
|  17 | Open FGA allows easy iteration and extension of authorization policies.                                                      |
|  18 | Supports nested hierarchies (e.g., organizations, folders, documents) and recursive relationships.                           |
|  19 | Enables cascading/inherited permissions across object types (e.g., admins inherit editor and viewer rights).                 |
|  20 | Invitation to visit the Open FGA team at the project pavilion on Wednesday and attend a talk by Jose and Alice on Thursday.  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4xZqSO1OGSc)