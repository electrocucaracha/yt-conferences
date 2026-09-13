---
type: Video Note
title: "Harbor Project - The Maintainers Session - Yan Wang, Broadcom & Vadim Bauer, 8gears"
description: "Vadim Bower and Yan, maintainers of Harbor, provided updates on the Harbor container registry project, highlighting recent developments and new features. They introduced the Harbor CLI, a command-line tool designed for CI/CD workflows and a..."
resource: https://www.youtube.com/watch?v=zVgMJPSNaLU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Vadim Bower and Yan, maintainers of Harbor, provided updates on the Harbor container registry project, highlighting recent developments and new features.
They introduced the Harbor CLI, a command-line tool designed for CI/CD workflows and automation, which now covers most use cases and has reached over 100,000 downloads, with significant contributions from LFX mentorship program participants.
The team also discussed progress on Harbor Satellite, aiming to offer a stateless, secretless, zero-trust registry for edge environments, with recent additions like Spiffy Inspire integration and proxy capabilities, and ongoing work to support air-gapped environments.
Yan detailed enhancements to Harbor’s proxy cache, including new parameters to manage upstream rate limits, improved artifact retention options, and performance improvements in garbage collection by optimizing tag management.
Additionally, Harbor is collaborating with Alibaba to support AI module artifacts, enabling users to manage large AI modules with OCI compatibility and standardizing workflows for AI workloads.
The session concluded with survey results showing Harbor’s growing adoption and appreciation within the community.
# Main Points

|   # | Main point                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------- |
|   1 | Vadim Bower and Yan are maintainers of Harbor.                                                                             |
|   2 | Harbor is a policy-driven container registry with image management and artifact signing.                                   |
|   3 | Harbor CLI is an alternative to the web UI, designed for CI/CD and command-line workflows.                                 |
|   4 | Harbor CLI supports Linux, Windows, and other platforms.                                                                   |
|   5 | CLI covers about 90-95% of use cases.                                                                                      |
|   6 | Harbor CLI was developed with contributions from LFX mentorship program mentees.                                           |
|   7 | CLI has reached over 100,000 downloads.                                                                                    |
|   8 | CLI is being "unsandboxed" and is now more officially released.                                                            |
|   9 | Harbor Satellite aims to provide a stateless, secretless, zero-trust registry for edge locations.                          |
|  10 | Satellite supports active replication of images to edge, not just proxying.                                                |
|  11 | Satellite now integrates with Spiffy Inspire for identity and can act as a proxy.                                          |
|  12 | Work is ongoing to support air-gapped environments for Satellite, aiming for unified tools and workflows.                  |
|  13 | Proxy cache enhancements: new parameter to limit upstream connections to avoid rate limits.                                |
|  14 | Proxy cache behavior updated to allow serving removed artifacts locally by default.                                        |
|  15 | Fixed issue with ptime updates for index references to improve tag retention.                                              |
|  16 | Outdated proxy adapters are now hidden from the UI; community help is welcome to maintain them.                            |
|  17 | Plans to support referral API for proxy cache to handle signatures and related artifacts.                                  |
|  18 | Future enhancement: allow limiting what can be proxy cached by repository or version.                                      |
|  19 | Performance improvements for Harbor garbage collection by managing tags only in the database, reducing storage operations. |
|  20 | Checkbox provided to enable new garbage collection behavior for existing artifacts.                                        |
|  21 | Collaboration with Alibaba on AI module support via the ModulePack project in CNCF sandbox.                                |
|  22 | Harbor now supports managing large AI module artifacts, following OCI compatibility.                                       |
|  23 | Users can build, push, and manage AI modules in Harbor, leveraging existing features like versioning and access control.   |
|  24 | CNCF survey shows Harbor is widely adopted in produc                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zVgMJPSNaLU)