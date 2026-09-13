---
layout: default
title: "[Session] Effortless User Onboarding with MCP with Pedro Rodrigues - SingleStore"
nav_order: 24
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Pedro, a software engineer at Single Store (formerly MemSQL), discusses
  how the company uses its MCP server to improve user onboarding for both new and
  existing users. He explains that traditional onboarding methods—such as documentation,
  w...
resource: https://www.youtube.com/watch?v=OjglGeBvDBs
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Pedro, a software engineer at Single Store (formerly MemSQL), discusses how the company uses its MCP server to improve user onboarding for both new and existing users.
He explains that traditional onboarding methods—such as documentation, webinars, and tutorials—are scalable but can overwhelm users as documentation grows and may not address specific issues promptly.
Additionally, proprietary products like Single Store face challenges with large language models (LLMs) lacking sufficient context, making onboarding harder compared to open-source alternatives.
To address these issues, Single Store developed the MCP server, which provides resources like Markdown guides and prompt templates to help users and LLMs interact more effectively with the platform.
Pedro demonstrates how integrating these resources streamlines setting up applications with tools like Drizzle and Single Store, and shares lessons learned, including the importance of defining concrete user flows, adapting documentation for LLMs, and hosting the MCP server remotely for better analytics and control.
Future plans include making documentation more LLM-friendly, expanding resource coverage, and enhancing direct database access and management through the MCP server.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Pedro from Single Store (formerly MemSQL) presented on onboarding users using their MCP server.                                                                          |
|   2 | Pedro is a full-time software engineer, MCP contributor, event organizer in Portugal, and has contributed to the Python SDK.                                             |
|   3 | Single Store is a data platform supporting transactional, analytical, search, and AI workloads, available on-prem, cloud, and hybrid environments.                       |
|   4 | Onboarding methods include documentation, webinars, tutorials, social media, and product-led growth (PLG) for their cloud platform (Ilas).                               |
|   5 | Documentation is public and scalable but can become overwhelming and slow to update as the product grows.                                                                |
|   6 | Users may get lost in extensive documentation or face delays in customer support if documentation is unclear or incomplete.                                              |
|   7 | LLMs (Large Language Models) often lack information about proprietary products like Single Store, leading to hallucinations or inaccurate answers.                       |
|   8 | Open-source technologies (e.g., Postgres, MySQL) are easier for users to onboard due to abundant public resources.                                                       |
|   9 | Single Store’s technical nature makes it challenging for users to write and optimize queries without deep documentation knowledge.                                       |
|  10 | Users often switch between UI and documentation, which can be confusing.                                                                                                 |
|  11 | The MCP server was developed to allow users to interact with Single Store services, communicate with databases, and get contextual help.                                 |
|  12 | MCP server features passwordless login and supports authentication via Single Store accounts or OAuth providers.                                                         |
|  13 | Tools and resources in MCP are grouped; resources include static documents, database records, and prompt templates for LLMs.                                             |
|  14 | Demo showed integrating Drizzle (TypeScript ORM) with Single Store using MCP resources for guided onboarding.                                                            |
|  15 | MCP resources (e.g., Markdown files) provide LLMs with context-specific guidance for Single Store integrations.                                                          |
|  16 | Lessons learned: define concrete use cases for onboarding, adapt documentation for LLMs (convert HTML to Markdown), and run MCP server remotely for better analytics and |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=OjglGeBvDBs)
