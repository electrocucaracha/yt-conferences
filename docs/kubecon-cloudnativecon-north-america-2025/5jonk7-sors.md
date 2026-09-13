---
type: Video Note
title: "Beyond the Cloud(s): Falco’s Ascent in Performance and... Leonardo Grasso & Leonardo Di Giovanna"
description: "In this presentation, Lonardo Graaso and Leonardo de Joanna, both maintainers of the Falco project, introduce themselves and provide an overview of Falco, an open-source, cloud-native security tool for runtime threat detection. They discuss..."
resource: https://www.youtube.com/watch?v=5JoNk7_Sors
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Lonardo Graaso and Leonardo de Joanna, both maintainers of the Falco project, introduce themselves and provide an overview of Falco, an open-source, cloud-native security tool for runtime threat detection.
They discuss Falco’s core functionality, which involves capturing events from the Linux kernel, evaluating them against customizable rules, and sending alerts when matches occur.
The latest release, Falco 0.42, introduces major features such as the capture recording feature, which allows users to record triggered events for troubleshooting and forensics, and can be analyzed using the new Stratoshark tool.
Another significant update is the drop entry initiative, which consolidates event reporting to exit events only, resulting in up to 20% lower system call latency and 30% lower CPU usage, while maintaining backward compatibility and simplifying the codebase.
The presenters also outline ongoing and future areas for performance and maintainability improvements, including event loop optimization, potential deprecation of legacy components, and encourage community feedback and participation through various channels.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Leonardo Graaso and Leonardo de Joanna, both Falco maintainers at CDI, Italian, contactable via GitHub or Slack (Falco channel). |
|   2 | Falco is an open-source, cloud-native security tool, donated to CNCF, standard for runtime threat detection, graduate project.               |
|   3 | Falco captures events from the Linux kernel and other data sources via plugins.                                                              |
|   4 | Events are evaluated against a set of rules; alerts are sent if rules match.                                                                 |
|   5 | Falco ships with default rules; users can create custom rules.                                                                               |
|   6 | LLMs (like ChatGPT and Claude) can help generate Falco rules.                                                                                |
|   7 | Example rule: detect when a laptop webcam is accessed.                                                                                       |
|   8 | Latest Falco version: 0.42 (released October).                                                                                               |
|   9 | New features in 0.42:                                                                                                                        |
|  10 | Capture recording: records events to scap files when a rule triggers, for troubleshooting and forensics; customizable per rule.              |
|  11 | Stratoshark: new tool (by Wireshark author) to visualize Falco scap files.                                                                   |
|  12 | Stricter validation on event schema from plugins.                                                                                            |
|  13 | Option to fine-tune Falco thread table cleanup.                                                                                              |
|  14 | Ability to add static fields to rules at configuration time.                                                                                 |
|  15 | Drop Entry Initiative:                                                                                                                       |
|  16 | Removed "enter" events, consolidated info into "exit" events for performance.                                                                |
|  17 | Enter events now only generated internally for specific vulnerable syscalls.                                                                 |
|  18 | SCAP backward compatibility maintained via a converter layer.                                                                                |
|  19 | Deprecated "direction" and "aender" fields; rules using them will show warnings.                                                             |
|  20 | Results: up to 20% lower syscall latency, up to 30% lower CPU usage, leaner codebase.                                                        |
|  21 | Performance improvement opportunities:                                                                                                       |
|  22 | Event loop optimization (kernel-side filtering, possible multi-threading).                                                                   |
|  23 | Replace process scan with eBPF iterators for faster state updates.                                                                           |
|  24 | Maintainability improvement opportunities:                                                                                                   |
|  25 | Possible deprecation of legacy BPF probe (low usage, limits feature parity).                                                                 |
|  26 | Possible deprecation or refactoring of gRPC output and Juvisisor lipcap engine (low usage, high maintenance).                                |
|  27 | Community feedback encouraged via Slack, CNCF dev list, communit                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5JoNk7_Sors)