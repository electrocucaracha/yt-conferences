---
type: Video Note
title: "Introducing Helm 4 - Matt Farina & Robert Sirchia, SUSE"
description: "The presenters introduced Helm 4, assuring the audience that existing charts remain compatible and highlighting the project's commitment to backward compatibility. They recognized several maintainers and reflected on Helm's ten-year history..."
resource: https://www.youtube.com/watch?v=wkP1xCQMCaE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters introduced Helm 4, assuring the audience that existing charts remain compatible and highlighting the project's commitment to backward compatibility.
They recognized several maintainers and reflected on Helm's ten-year history, noting its evolution alongside Kubernetes and the major changes that led to each new version.
Helm 4 introduces several key improvements, including modernized logging with SLOG, reproducible chart builds, embeddable commands, colorized CLI output, and a new plugin engine supporting WebAssembly for cross-platform compatibility.
The groundwork has been laid for future chart API versions, and the team emphasized ongoing support for Helm 3 until mid-2026, with no feature backports.
They encouraged community involvement through contributions, feedback, and participation in meetings, and concluded by answering technical questions about plugin support and inviting further discussion at their booth.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Helm 4 was introduced; no existing charts were broken.                                                                                 |
|   2 | Maintainers Scott, George, Terry, and emeritus maintainer Martin were acknowledged.                                                    |
|   3 | Helm 4 was released live during the talk.                                                                                              |
|   4 | Presenters: Matt Fina (Helm maintainer, SUSA engineer, vegan) and Rob (open source maintainer, technical community marketing, hunter). |
|   5 | Helm's history: first commit in October 2015, announced at first KubeCon, 10-year anniversary.                                         |
|   6 | Helm evolved from merging with Deployment Manager (Helm 2), then Helm 3 after major Kubernetes changes.                                |
|   7 | Helm 4 initiated after 6 years to address accumulated changes and feature requests.                                                    |
|   8 | Adopted Go best practices for interfaces and module compatibility.                                                                     |
|   9 | Dropped support for older Kubernetes versions; now officially supports back to 1.16.                                                   |
|  10 | Improved logging with SLOG-based structured logging, especially for SDK users.                                                         |
|  11 | Helm has an SDK beyond the CLI.                                                                                                        |
|  12 | Chart API v2 limitations prompted groundwork for future Chart API v3.                                                                  |
|  13 | New features in Helm 4:                                                                                                                |
|  14 | Colored CLI output.                                                                                                                    |
|  15 | Commands embeddable in other applications.                                                                                             |
|  16 | Enhanced logging for SDK and CLI users.                                                                                                |
|  17 | Reproducible chart builds for consistent outputs.                                                                                      |
|  18 | WebAssembly (WASM) plugin support with backward compatibility; plugins now cross-platform (Windows, Linux, Mac, ARM, Intel).           |
|  19 | Post Renderers now plugin-based.                                                                                                       |
|  20 | Future plans:                                                                                                                          |
|  21 | Chart API v3 to be introduced during Helm 4 lifecycle as an experiment, with v2 still supported.                                       |
|  22 | GoReleaser and cosign signing to be added (planned for 4.1).                                                                           |
|  23 | Helm v3 support: bug fixes until July 8, 2026; security fixes until Nov 11, 2026; no feature backports.                                |
|  24 | Helm v5 is years away; feedback and suggestions are welcome.                                                                           |
|  25 | Community involvement encouraged via Slack, GitHub, community meetings, documentation, charts tooling, and unit tests.                 |
|  26 | Project pavilion presence for further questions and discussions.                                                                       |
|  27 | WASM plugins use WYP1, not the component model, due to Go limitations.                                                                 |
|  28 | Attendees invited to contribute and ask questions.                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wkP1xCQMCaE)