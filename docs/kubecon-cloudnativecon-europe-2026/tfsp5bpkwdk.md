---
layout: default
title: The State of Backstage in 2026 - Ben Lambert & Patrik Oldsberg, Spotify
nav_order: 368
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk at CubeCon EU, Ben and Patrick, maintainers of Backstage
  at Spotify, provided an update on the project's progress since the last conference.
  They highlighted significant growth, with over 4,000 adopters, 255 open source plugins...
resource: https://www.youtube.com/watch?v=tFsp5bpKwdk
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

In this talk at CubeCon EU, Ben and Patrick, maintainers of Backstage at Spotify, provided an update on the project's progress since the last conference.
They highlighted significant growth, with over 4,000 adopters, 255 open source plugins, and nearly 33,000 GitHub stars, and discussed improvements such as a new process for handling pull request reviews and the addition of two new core maintainers.
The team showcased advancements in the frontend system, including better plugin isolation, improved navigation, built-in permissions, and a move toward a new design system, with the new frontend now the default for new apps and a planned phase-out of the old system by year-end.
Updates to the CLI and authentication processes were detailed, including support for the CIMD spec, modularization of the CLI, and new catalog actions, making automation and integration with AI tools more seamless.
The presenters emphasized Backstage’s evolving role as a central hub for developer experience, especially as AI adoption increases, and introduced ongoing work to make the software catalog model more extensible and machine-readable, supporting better integration with plugins and AI agents.
They concluded with a roadmap focused on catalog model extensions, AI context integration, improvements to the release process, continued evolution of the Backstage UI, and the deprecation of the old frontend system.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Over 4,000 Backstage adopters, 255+ open source plugins, and nearly 33,000 GitHub stars                                                             |
|   2 | Community plugins moved to a dedicated repository with 190+ plugin packages and 85 maintainers                                                      |
|   3 | Two new core maintainers: Andre and Aramis, contributing across multiple project areas                                                              |
|   4 | New pull request review process: global queue, personal boards, automated state tracking, and priority scoring                                      |
|   5 | Expanded reviewer group with incentives for participation and clearer PR status for contributors                                                    |
|   6 | Frontend system updates: improved plugin isolation, documentation, testing utilities, and navigation                                                |
|   7 | Old frontend system now forwards compatible with the new system; support for permissions and feature flags added                                    |
|   8 | Migration to Backstage UI design system underway, replacing Material UI                                                                             |
|   9 | New frontend system at 1.0 release candidate; now default for new apps; agent skills for migration launched                                         |
|  10 | Old frontend system support to phase out by end of year, with new features shipping only in the new system                                          |
|  11 | Authentication improvements: support for CIMD, offline access scopes, and refresh tokens for CLI and MCP                                            |
|  12 | CLI can now log in to multiple Backstage instances and supports modularization into standalone modules                                              |
|  13 | Actions registry enables plugins to expose reusable actions, now callable via CLI and MCP tools                                                     |
|  14 | New catalog actions: query catalog entities, add/remove location, validate entities, and "who am I"                                                 |
|  15 | CLI modularization allows separate modules for different user personas and standalone command execution                                             |
|  16 | Backstage's role in AI: increased usage of UI and automation tools, catalog model context critical for AI                                           |
|  17 | Catalog model extension API in development: plugins can claim ownership of annotations, extend specs, and create new kinds with structured metadata |
|  18 | Model extensions to be available in upcoming releases, aiming for machine-readable formats for LLMs                                                 |
|  19 | Introduction of AI context kind for storing skills and context in the catalog                                                                       |
|  20 | Planned changes to release process: slowe                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tFsp5bpKwdk)
