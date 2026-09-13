---
type: Video Note
title: "Project Lightning Talk: Forensics With Falco - Gerald Combs, Maintainer"
description: "Gerald Combmes, creator of Wireshark and a Falco maintainer, introduces Falco as a cloud-native, real-time threat detection engine typically used in Kubernetes clusters to monitor system calls and log messages against predefined rules, trig..."
resource: https://www.youtube.com/watch?v=oiuh1eHGFMY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Gerald Combmes, creator of Wireshark and a Falco maintainer, introduces Falco as a cloud-native, real-time threat detection engine typically used in Kubernetes clusters to monitor system calls and log messages against predefined rules, triggering alerts when necessary.
He highlights a recent Falco feature that allows triggered activity to be saved to capture files for further investigative analysis using Stratark, a sibling application to Wireshark that applies similar workflows to system calls and log messages.
Gerald explains how to enable and configure this capture feature in Falco, including specifying which rules to capture, where to save files, and when to stop capturing, while noting the potential performance impact and the need for careful experimentation.
He invites feedback on this new feature, offers further resources and demos at CubeCon, and expresses gratitude to the community for their support.
# Main Points

|   # | Main point                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------- |
|   1 | Gerald Combmes is the creator and lead developer of Wireshark and a Falco maintainer.                                  |
|   2 | Falco is a cloud-native real-time threat detection engine, typically deployed in Kubernetes clusters.                  |
|   3 | Falco monitors system calls and log messages, matching them against rules to trigger alerts.                           |
|   4 | Falco is approaching its 10-year anniversary and is widely used.                                                       |
|   5 | A recent feature in Falco allows triggered activity to be saved to a capture file.                                     |
|   6 | The capture file enables further investigative analysis using Stratark.                                                |
|   7 | Stratark is a sibling application to Wireshark, sharing its user interface and dissection engine.                      |
|   8 | Stratark allows Wireshark-like workflows to be applied to system calls and log messages.                               |
|   9 | The goal is to replicate networking analysis workflows for system calls using Falco and Stratark.                      |
|  10 | Last year at KubeCon North America, Gerald demoed using Stratark with Falco, focusing on Stratark.                     |
|  11 | The demo showed using these tools to analyze data transmitted across a pipe during an SSH key exploit attempt.         |
|  12 | To enable capture in Falco, changes must be made to the configuration file, specifically enabling the capture section. |
|  13 | By default, capture is disabled to keep Falco lightweight.                                                             |
|  14 | Capture can be enabled for all rules or a specific set of rules.                                                       |
|  15 | The file path for saving captures can be specified; default is "slimfalco".                                            |
|  16 | Users must specify when Falco should stop saving information, currently by time duration in milliseconds.              |
|  17 | Future versions will allow stopping by number of events or file size.                                                  |
|  18 | When enabled, triggered rules generate timestamped capture files.                                                      |
|  19 | For the demo, additional configuration was needed to capture read and write system calls, which increases overhead.    |
|  20 | Monitoring can affect system performance (observer effect); no passive hardware taps exist for system calls.           |
|  21 | Users are encouraged to experiment and provide feedback on this new feature.                                           |
|  22 | More information and live demos are available at the Falco booth at KubeCon and at the URLs provi                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oiuh1eHGFMY)