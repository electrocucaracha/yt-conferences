---
layout: default
title: What’s New in Containerd 2.2 - Derek McGowan, Docker & Phil Estes, AWS
nav_order: 340
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Phil Estus and Derek McGawan present updates on the containerd project,
  highlighting its recent 2.2 release and ongoing community growth, including new
  reviewers and committers from diverse companies. They note the project's 10-year
  anniver...
resource: https://www.youtube.com/watch?v=iV_qCOCi0yE
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

Phil Estus and Derek McGawan present updates on the containerd project, highlighting its recent 2.2 release and ongoing community growth, including new reviewers and committers from diverse companies.
They note the project's 10-year anniversary and emphasize the importance of extensibility and community contributions, such as Netflix's work on user namespaces.
Derek details architectural components—high-level runtime, core, and low-level runtime—and introduces new features like the transfer service, parallel unpack, sandbox controller, mount manager, and enhanced support for Aerofs snapshotter.
A new shim leveraging these features now enables containerd to run fully on macOS using libkrun, with a demonstration showing fast Linux container startup on a Darwin host.
The session concludes with a discussion on the shim's potential use cases and its compatibility with other runtimes, reinforcing containerd's commitment to innovation and broad ecosystem support.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Maintainer track session focused on containerd 2.2 release updates                                                                                                                          |
|   2 | New project reviewers: Jyn, Chris, Gal; Austin became a committer; Kana promoted to committer                                                                                               |
|   3 | Reviewers and committers come from diverse companies and vendors                                                                                                                            |
|   4 | containerd 1.6 LTS has reached end of life after 38 releases; 1.7 is now LTS until next September                                                                                           |
|   5 | containerd 2.0 went end of life; 2.1 and 2.2 are active; some releases may be extended by sponsor committers                                                                                |
|   6 | containerd project is celebrating its 10-year anniversary; first commit in November 2015                                                                                                    |
|   7 | Netflix contributed significantly to user namespaces capability; migrated Titus platform to containerd with user namespaces and NRI plugins                                                 |
|   8 | containerd’s extensibility (shims, snapshotters, NRI plugins) has enabled innovation and experimentation                                                                                    |
|   9 | containerd architecture: high-level runtime (API, CRI, transfer service), core (snapshots, containers, images, metadata store, garbage collector), low-level runtime (shim, runC, OCI spec) |
|  10 | Transfer service (added in 1.7) centralizes registry operations, enables shared configuration, and supports unpack progress                                                                 |
|  11 | 2.2 introduces parallel unpack for overlayFS and Aerofs snapshotters, improving image pull speed                                                                                            |
|  12 | Transfer service is pluggable for custom transfer implementations                                                                                                                           |
|  13 | Sandbox controller (default since 2.0) abstracts pod/multicontainer environments, supports VM use cases, and exposes a sandbox API to shims                                                 |
|  14 | 2.2 implements CRI pod metrics, allowing kubelet to get metrics directly from containerd                                                                                                    |
|  15 | Mount manager (new in 2.2) provides API/backend for mounts, device activation, temporary mounting, and chaining mounts; integrated with garbage collector                                   |
|  16 | Aerofs snapshotter integrated with mount manager in 2.2; adds quota and block file support                                                                                                  |
|  17 | New non-core shim project uses mount manager, Aerofs, and libkrun to run Linux containers on macOS and Linux; fast VM startup (~370ms)                                                      |
|  18 | Project works with Docker and is being explored for broader use beyond macOS                                                                                                                |
|  19 | Features developed for one runtime                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=iV_qCOCi0yE)
