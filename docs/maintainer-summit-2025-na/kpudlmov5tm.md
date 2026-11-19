---
layout: default
title: "Navigating the Multi-Version Kubernetes Universe: How Emulation Version Shapes Your... Siyuan Zhang"
nav_order: 5
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "Siwan from Google explains the introduction of two new flags, `emulatedVersion` and `minCompatVersion`, designed to navigate the complexity of multi-version Kubernetes upgrades."
resource: "https://www.youtube.com/watch?v=kPUdlmov5TM"
tags:
  - maintainer-summit-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T17:23:58+00:00
---

# Summary

Siwan from Google explains the introduction of two new flags, `emulatedVersion` and `minCompatVersion`, designed to navigate the complexity of multi-version Kubernetes upgrades.
The `emulatedVersion` flag allows a newer binary to emulate the API and feature capabilities of previous releases, enabling cluster administrators to upgrade binaries without immediately changing behavior, thereby facilitating safer, rollback-able steps and easier isolation of issues.
The `minCompatVersion` flag, introduced in Kubernetes 1.35, defines the minimum version a component must tolerate regarding storage and validation rules, effectively signaling that backward compatibility is no longer required.
This allows for faster feature adoption by enabling features to skip the alpha stage and go directly to beta if they are only delayed by compatibility concerns rather than maturity.
Together, these mechanisms provide granular control over the upgrade process, support skip-level upgrades, and allow for "emulated long-term support," while contributors must adhere to new guidelines for tracking feature gate changes and cleaning up code to ensure compatibility across emulated versions.

# Main Points

|   # | Main point                                                                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes introduces compatibility versions to address the risks and complexity of traditional monolithic upgrades, which often make rollbacks difficult and dangerous due to immediate changes in APIs and data persistence.               |
|   2 | The Emulated Version flag, introduced in Kubernetes 1.31 and 1.32, allows a component binary to emulate the capabilities, APIs, and features of prior releases ranging from N-1 to N-3.                                                      |
|   3 | The Min Compatibility Version flag, added in Kubernetes 1.35, controls the minimum version a component can tolerate regarding storage versions and validation rules, defining the minimum behavior the cluster must tolerate.                |
|   4 | Emulated Version defines what the server is capable of in terms of features and APIs, while Min Compatibility Version defines what the server understands about other components in the cluster.                                             |
|   5 | Upgrades can be broken into three safer steps: upgrading binaries without changing versions, bumping the Emulated Version to enable new features, and optionally bumping the Min Compatibility Version to acknowledge no rollback is needed. |
|   6 | This multi-step approach enables rollbackable upgrades, allows for better diagnostics and testing at each stage, and supports skip-level upgrades by upgrading binaries directly while managing version bumps separately.                    |
|   7 | The system supports emulated long-term support, allowing users to run newer binaries with older emulated versions to maintain compatibility with supported release cycles.                                                                   |
|   8 | Contributors must maintain an append-only list in feature gate specs to track changes and default values, ensuring the codebase can rebuild past behaviors for emulated versions.                                                            |
|   9 | Code cleanup for features graduating to GA or being deprecated is restricted until three versions have passed, requiring feature gates to remain toggleable to support N-3 emulation.                                                        |
|  10 | Non-feature-gated changes that impact users at N-3 versions should be gated behind lightweight feature gates to track changes, while bugfixes and performance optimizations do not require this.                                             |
|  11 | Min Compatibility Version allows features to skip the alpha stage and start as beta if they are delayed solely by backward compatibility concerns, accelerating feature adoption by one release.                                             |
|  12 | This fast-track mechanism applies to scenarios like new SELinux matching rules or simple API changes but is not a shortcut for complex features requiring rigorous testing.                                                                  |
|  13 | The implementation of these compatibility versions is a community effort that requires changes to development workflows to ensure safe upgrades and faster feature progression.                                                              |
|  14 | Min Compatibility Version primarily affects how storage versions are picked and may apply to nodes if they need to upgrade API fields, though it is not yet fully wired into all components.                                                 |
|  15 | Clients and sidecars generally work with one API version at a time, so they should adopt newer APIs after a full upgrade rather than during the emulated state.                                                                              |
|  16 | Bugfixes are typically not tied to specific emulated versions and apply across all supported emulated versions, ensuring that fixes for older releases are available in newer binaries.                                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kPUdlmov5TM/hqdefault.jpg)](https://www.youtube.com/watch?v=kPUdlmov5TM)

[Watch on YouTube](https://www.youtube.com/watch?v=kPUdlmov5TM)
