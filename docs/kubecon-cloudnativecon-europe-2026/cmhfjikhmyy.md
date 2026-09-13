---
layout: default
title:
  Helm 4 Is Here. So, Now What? - Andrew Block, Red Hat; Scott Rigby, Replicated;
  Robert Sirchia, SUSE
nav_order: 139
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation introduces Helm 4, the latest major release of the Kubernetes
  package manager, highlighting its first update in six years and marking Helm’s ten-year
  anniversary. Key features in Helm 4 include a new WASM-based plugin engin...
resource: https://www.youtube.com/watch?v=cmHFJikhmyY
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

The presentation introduces Helm 4, the latest major release of the Kubernetes package manager, highlighting its first update in six years and marking Helm’s ten-year anniversary.
Key features in Helm 4 include a new WASM-based plugin engine (which coexists with the existing system), server-side apply, improved status handling, and enhanced chart caching, while maintaining backward compatibility with existing charts (charts v2 remain unchanged).
The team has laid the groundwork for charts v3, enabling future enhancements such as resource sequencing, alternative template engines, improved value passing to subcharts, and better ignore file handling, all without breaking existing charts.
The Helm Improvement Proposal (HIP) process, modeled after Python’s PEPs, ensures transparency and community involvement in major changes.
Additional improvements focus on strengthening OCI support, registry mirroring, streamlining the release process, and enhancing contributor experience.
The presenters encourage community participation through reviewing and proposing HIPs, joining developer meetings, and engaging on Slack to help shape Helm’s future.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Helm 4 has been released, marking the first major release in six years and the project's 10-year anniversary.                                                            |
|   2 | Helm is a package manager for Kubernetes, using Helm charts, values/configs, and an SDK CLI.                                                                             |
|   3 | Helm 4 introduces a WASM-based plugin engine, which does not replace the current engine; existing plugins still work.                                                    |
|   4 | Server-side apply and Kstatus implementation are included in Helm 4.                                                                                                     |
|   5 | Chart cache improvements and organizational dependency tracking have been added.                                                                                         |
|   6 | Charts v2 format remains unchanged; Helm 4 does not break existing charts.                                                                                               |
|   7 | Helm 4 is not a rewrite and is not written in Rust.                                                                                                                      |
|   8 | Scaffolding for Charts v3 is included, allowing future API version upgrades without breaking backwards compatibility.                                                    |
|   9 | Helm Improvement Proposals (HIPs) are used for major changes, modeled after Python’s PEPs, ensuring transparency and community involvement.                              |
|  10 | Charts v3 will allow features not possible in v2, such as sequencing resources, new rendering engines, and improved value passing to subcharts.                          |
|  11 | Chart authors will be able to define plugins as dependencies in charts v3.                                                                                               |
|  12 | New plugin types include render, getter, transform, and signer plugins.                                                                                                  |
|  13 | Additional signing mechanisms (e.g., cosign, SSH keys) will be supported beyond PGP.                                                                                     |
|  14 | Experimental support for charts v3 is available; users can track progress via a Helm tracking issue.                                                                     |
|  15 | OCI support is being strengthened, including better credential management, policy.json support, and registry mirroring for enterprise environments.                      |
|  16 | Collaboration with CNCF projects like ORAS and container tools is ongoing to improve OCI capabilities.                                                                   |
|  17 | Efforts are underway to streamline the Helm release process and improve contributor experience.                                                                          |
|  18 | Community involvement is encouraged via reviewing/commenting on HIPs, joining Kubernetes Slack channels (Helm Users, Helm Dev), and attending weekly developer meetings. |
|  19 | Information on developer meetings and tracking Helm v3 charts implementation is available on the Helm website.                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cmHFJikhmyY)
