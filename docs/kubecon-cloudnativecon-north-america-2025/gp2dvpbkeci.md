---
type: Video Note
title: "Project Lightning Talk: Copacetic: Directly Patch Container Image Vulnerabilities - Jeremy Rickard"
description: "Jeremy from Microsoft introduces Copaetic, a CNCF sandbox project designed to patch container images and address vulnerabilities, particularly CVEs, without requiring a full rebuild. Copa is a Go-based CLI tool that leverages BuildKit, the..."
resource: https://www.youtube.com/watch?v=gp2DVPBkECI
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jeremy from Microsoft introduces Copaetic, a CNCF sandbox project designed to patch container images and address vulnerabilities, particularly CVEs, without requiring a full rebuild.
Copa is a Go-based CLI tool that leverages BuildKit, the default builder for Docker, to analyze vulnerability scan reports—by default using Trivy—and generate patch layers that update only the affected components in a container image.
The tool supports multiple platforms, all OCI media types, and can now patch not just OS-level vulnerabilities but also issues in application dependencies like Python and Node.js.
Recent enhancements include multi-platform support, bulk image patching, and integration with various workflows such as GitHub Actions and Docker extensions.
Jeremy encourages interested users to join the community, explore the GitHub repository, and participate in weekly meetings.
# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Copaetic is a CNCF sandbox project aimed at directly patching container images to address vulnerabilities.                |
|   2 | It is a CLI tool written in Go, based on BuildKit (the default builder for Docker).                                       |
|   3 | Copa uses container vulnerability scan reports, by default from Trivy, to identify OS vulnerabilities in images.          |
|   4 | The scan component is pluggable and can be replaced with other tools.                                                     |
|   5 | Copa analyzes the scan report, determines what needs updating, and generates a patch layer (diff) to append to the image. |
|   6 | It enables patching of images, including those without package managers, by adding updated layers.                        |
|   7 | Common use cases include patching vulnerabilities in libraries like OpenSSL.                                              |
|   8 | Patched images can be pushed to container registries and used like the original images.                                   |
|   9 | Recent features include:                                                                                                  |
|  10 | Multi-platform support (no longer requires patching on the target architecture).                                          |
|  11 | Support for all OCI media types, not just Docker images.                                                                  |
|  12 | Compatibility with Podman.                                                                                                |
|  13 | Ability to patch application dependencies (e.g., Python, Node.js), not just OS vulnerabilities.                           |
|  14 | Introduction of an MCP server for AI-related initiatives.                                                                 |
|  15 | Upcoming features:                                                                                                        |
|  16 | Bulk image patching (batch processing).                                                                                   |
|  17 | BuildKit frontend integration for broader tool compatibility.                                                             |
|  18 | Copa can be used via GitHub Action, Docker extension, and supports custom scanner plugins.                                |
|  19 | Weekly community meetings are held Wednesdays at 6:30 p.m. Eastern time.                                                  |
|  20 | The Copa GitHub repository is available for more information.                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gp2DVPBkECI)