---
type: Video Note
title: "Lima Project Updates: Expanding the Focus To Hardening AI - Akihiro Suda, NTT & Anshuman Sahoo"
description: "The video features maintainers of the Lima project discussing recent updates and the project's evolution. Originally designed to optimize Linux virtual machines for running containers on macOS, Lima now supports multiple host and guest oper..."
resource: https://www.youtube.com/watch?v=Cb5gGTFS5M0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features maintainers of the Lima project discussing recent updates and the project's evolution.
Originally designed to optimize Linux virtual machines for running containers on macOS, Lima now supports multiple host and guest operating systems, including Linux, Windows, FreeBSD, and plans for Windows guests in the future.
Recent releases have expanded Lima’s capabilities to include sandboxing AI agents, GPU acceleration, and enhanced security features such as sync mode, which allows users to review and approve changes before syncing files between guest and host, protecting against malicious AI actions.
The project has introduced a plugin infrastructure for extensibility, supports various container engines, and is widely adopted in the developer community, with integrations into third-party tools and use cases in CI environments.
Looking ahead, the team aims to further improve user experience, add more VM drivers, and extend support for AI workloads across more platforms.
# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dimma (Lima) is a project for running Linux virtual machines optimized for containers and AI agents.                                                                                            |
|   2 | Recent releases expanded support beyond containers to AI workloads.                                                                                                                             |
|   3 | Lima now supports MacOS, Linux, Windows, FreeBSD, NetBSD, and DragonFlyBSD as hosts; guests include Linux, MacOS, FreeBSD, and planned Windows.                                                 |
|   4 | Automatic host file system sharing and port forwarding are included, but can be disabled for security.                                                                                          |
|   5 | Default container engine is containerd; supports Docker, Podman, Kubernetes, and Apptainer.                                                                                                     |
|   6 | Originally for MacOS hosts, now supports multiple OSes.                                                                                                                                         |
|   7 | Installation on MacOS: brew install lima; start with limactl start.                                                                                                                             |
|   8 | Similar projects: WSL2 (Windows only), Multipass (now proprietary), Docker Machine (abandoned), Rancher Desktop, Finch, Lima GUI, Portman Desktop, Lima Explorer, 0MA, Lima DevTools, RF Swift. |
|   9 | Lima is used in GitHub Actions for testing on non-Ubuntu OSes and SElinux compatibility.                                                                                                        |
|  10 | Architecture: limactl CLI, host agent processes, VM drivers (QEMU, Apple HVF, Microsoft WSL2, KanKit), guest agent, network drivers, file system sharing (9P, reverse SSHFS, rsync).            |
|  11 | Supports GPU acceleration via KanKit for AI workloads on MacOS.                                                                                                                                 |
|  12 | Plugin infrastructure allows custom VM drivers, CLI plugins, and URL schema plugins.                                                                                                            |
|  13 | Lima promoted to CNCF incubating project; 20,000+ GitHub stars, 170+ contributors.                                                                                                              |
|  14 | Lima provides strong VM-based sandboxing for AI agents, addressing risks of AI hallucinations and malicious code.                                                                               |
|  15 | Two AI modes: AI inside Lima (run AI in VM), AI outside Lima (host AI uses sandboxed tools via MCP).                                                                                            |
|  16 | New sync mode in v2.1: user confirmation required before syncing guest changes to host, preventing unwanted modifications.                                                                      |
|  17 | Plans: add more VM drivers, Windows guest support, improved TUI, Lima Compose for multi-VM management, expand AI workload support to Linux/Windows hosts.                                       |
|  18 | Firecracker VM driver not yet implemented, but plugin API allows custom drivers.                                                                                                                |
|  19 | Community: website, GitHub, Slack, X, Mastodon, monthly meeting                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Cb5gGTFS5M0)