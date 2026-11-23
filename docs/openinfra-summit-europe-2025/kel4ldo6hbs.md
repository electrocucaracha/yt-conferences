---
layout: default
title: "OpenStack clients:  CLI and TUI for OpenStack written in Rust"
nav_order: 63
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Artim, a maintainer at CIS 111, presents a new OpenStack CLI and TUI tool written in Rust, designed to address the performance limitations and maintenance burdens of the existing Python-based client."
resource: "https://www.youtube.com/watch?v=KeL4lDo6Hbs"
youtube_stats:
  view_count: 120
  like_count: 3
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Artim, a maintainer at CIS 111, presents a new OpenStack CLI and TUI tool written in Rust, designed to address the performance limitations and maintenance burdens of the existing Python-based client.
By generating the code entirely from OpenAPI specifications, the project eliminates the need for manual updates when new API fields are added, allowing maintainers to focus on core features like authentication and caching rather than repetitive "monkey typing." The new CLI, abbreviated as `oc`, enforces consistent command syntax, supports flexible authentication methods including environment variables and config files, and offers advanced output customization with JSON support and status-based coloring.
Additionally, the project introduces a TUI interface inspired by K9s, which provides a visual, interactive experience for managing OpenStack resources, including context-based navigation and resource creation via pre-populated templates.
This approach aims to provide a faster, more reliable, and user-friendly alternative to the traditional OpenStack client while maintaining compatibility with existing cloud configurations.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The new OpenStack CLI (OC) and TUI (OS2) are written in Rust and generated from OpenAPI specifications to improve performance and maintainability.                                   |
|   2 | This approach eliminates the need for manual code updates when new API fields are added, allowing maintainers to focus on features like authentication and caching.                  |
|   3 | The project addresses the slowness and inconsistency of the Python-based client by using a compiled language for faster execution and easier containerization.                       |
|   4 | OC enforces consistent command syntax by prefixing commands with the service name (e.g., `oc identity user create`) to resolve naming collisions.                                    |
|   5 | Multi-word resources are separated by dashes, and explicit ID or name parameters are required to avoid ambiguous resolution errors.                                                  |
|   6 | Authentication supports multiple methods, including environment variables, config files, and authentication helpers for fetching secrets from external sources like HashiCorp Vault. |
|   7 | A strict separation is enforced between environment variables and config files to prevent the unpredictable merging behavior found in the Python client.                             |
|   8 | Cloud YAML files can be virtually merged from multiple locations into a single logical tree, allowing users to split configurations into manageable pieces.                          |
|   9 | Authentication caching is enabled by default and stored on the file system, enabling token rescoping to avoid repeated MFA or federation logins.                                     |
|  10 | Output formatting supports JSON, table views with customizable column widths, and status-based color coding for better visual clarity.                                               |
|  11 | The CLI includes a cURL mode that allows sending authenticated requests directly to the cloud for commands not yet fully implemented.                                                |
|  12 | OS2 is a terminal user interface inspired by K9s, providing a navigable dashboard for OpenStack resources with configurable shortcuts and views.                                     |
|  13 | The TUI supports context-based navigation, allowing users to move between related resources such as security groups and their rules.                                                 |
|  14 | Resource creation and editing in OS2 are handled through pre-populated templates in the user's default editor, leveraging OpenAPI schemas for validation.                            |
|  15 | Both tools support fuzzy search for cloud selection and resource navigation to enhance usability.                                                                                    |
|  16 | The project is maintained by a single developer who generates approximately 95% of the code automatically, with the remainder handling authentication and UX logic.                  |
|  17 | Future roadmap items include keyring integration for secure credential storage and the implementation of contexts similar to Kubernetes or Docker.                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/KeL4lDo6Hbs/hqdefault.jpg)](https://www.youtube.com/watch?v=KeL4lDo6Hbs)

[Watch on YouTube](https://www.youtube.com/watch?v=KeL4lDo6Hbs)
