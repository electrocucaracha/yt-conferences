---
type: Video Note
title: "Rust Vs. Go: Building a Container Network Stack From Scratch - Matt Heon & Shivang K Raghuvanshi"
description: "Matt Heon, principal engineer at Red Hat and core maintainer of Podman, explains that Podman is a single-node, rootless, and daemonless container engine with Docker-compatible interfaces, but not intended as a Kubernetes runtime. Initially..."
resource: https://www.youtube.com/watch?v=05wBWDa8W-g
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Matt Heon, principal engineer at Red Hat and core maintainer of Podman, explains that Podman is a single-node, rootless, and daemonless container engine with Docker-compatible interfaces, but not intended as a Kubernetes runtime.
Initially, Podman used CNI for networking due to its compatibility with Kubernetes, but this proved suboptimal as Podman only needed a small subset of CNI’s features and faced potential loss of support.
Consequently, the team developed Netavark, a Rust-based, monolithic networking tool tailored for Podman’s needs, along with the lightweight DNS server aardvark-dns.
The decision to use Rust over Go was driven by Rust’s static memory management, expressive type system, and improved error handling, despite the team’s greater familiarity with Go.
Shivang Keragwanshi, an LFX mentee, contributed by building Rust netlink conntrack support to resolve a UDP traffic bug, highlighting the value of mentorship and community contributions.
In retrospect, the team is satisfied with the move to Rust, noting improved developer satisfaction and manageable onboarding with the help of modern coding assistants, though code review and initial code quality remain challenges.
# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Matt Heon is a principal engineer at Red Hat and core maintainer of Podman.                                                                           |
|   2 | Podman is a single-node, rootless, daemonless container engine, not a Kubernetes runtime.                                                             |
|   3 | Podman provides Docker-compatible CLI and API, plus Podman-specific API features.                                                                     |
|   4 | Project started in 2017; CNCF sandbox since 2024.                                                                                                     |
|   5 | Podman initially used CNI for networking due to rapid development needs and Kubernetes compatibility.                                                 |
|   6 | CNI provided more features than needed; Podman used only about 5% of CNI’s capabilities.                                                              |
|   7 | Podman faced UI mismatches and bugs due to Docker CLI and Kubernetes networking differences.                                                          |
|   8 | In 2021, CNI maintainers considered dropping support for plugins Podman used.                                                                         |
|   9 | Podman team decided to build their own networking tool, Netavark, instead of forking CNI.                                                             |
|  10 | Netavark is a monolithic, Rust-based container network setup/teardown tool, released in 2022 with Podman 4.0.                                         |
|  11 | Netavark handles bridging, MacVLAN, IPVLAN, routing, firewall, and has a sister project, aardvark-dns, for container DNS.                             |
|  12 | Rust was chosen for Netavark due to static memory management, type system, and error handling; Go was seen as less suitable for persistent processes. |
|  13 | Most developers prefer Rust; LLMs have eased the learning curve.                                                                                      |
|  14 | Code review is harder in Rust than Go; onboarding new developers to Rust is challenging due to limited opportunities.                                 |
|  15 | Shivang Keragwanshi, an LFX mentee, contributed by fixing a UDP traffic bug involving Linux conntrack and Netavark.                                   |
|  16 | The fix required building a new Rust netlink conntrack library, now upstreamed.                                                                       |
|  17 | LFX mentorship and weekly syncs were key to successful onboarding and problem-solving.                                                                |
|  18 | Netavark’s codebase initially had suboptimal Rust due to team inexperience; ongoing refactoring is improving it.                                      |
|  19 | Slirp4netns is being replaced by pasta for rootless networking; migration will occur in Podman 6.                                                     |
|  20 | Rust’s package management was easier for Podman due to lessons learned from Go’s complex vendoring.                                                   |
|  21 | Podman team is satisfied with Rust; developer ava                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=05wBWDa8W-g)