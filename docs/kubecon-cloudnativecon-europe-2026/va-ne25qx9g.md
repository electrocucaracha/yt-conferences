---
layout: default
title:
  "Tutorial: Attack Defense: Leverage eBPF To Reveal Attack Flows... Constanze
  R, Markus G & Teodor P"
nav_order: 378
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The transcript details a CBPF attack-defense gamified workshop focused
  on Kubernetes security, where participants engage in both offensive and defensive
  roles using production-ready eBPF tools. The facilitators introduce key contributors
  an...
resource: https://www.youtube.com/watch?v=VA-ne25QX9g
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

The transcript details a CBPF attack-defense gamified workshop focused on Kubernetes security, where participants engage in both offensive and defensive roles using production-ready eBPF tools.
The facilitators introduce key contributors and tools such as Tetragon, Cubecape, Inspector Gadget, and Pixie, guiding attendees through hands-on labs without requiring local setup.
The workshop progresses through a series of "rooms," each simulating different stages of an attack chain, including initial access, environment discovery, credential access, lateral movement, and exploitation of vulnerabilities.
Participants learn to detect and respond to various adversarial techniques using anomaly detection, signature rules, and protocol tracing, with emphasis on real-world tactics and the importance of monitoring for unexpected behaviors.
The session concludes by encouraging attendees to continue exploring the labs, consult provided materials, and engage with tool maintainers for further learning.

# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Welcome to the CBPF attack defense gamified workshop                                                                      |
|   2 | Workshop involves attacking and defending systems using a provided manual                                                 |
|   3 | Presenters: Marcus Gillinger (monster), author of EVPF Turpp, Adopnik (defense), Constanze (CNCF ambassador)              |
|   4 | Options to play in pairs, solo, or read along; fully hosted environment, no local setup required                          |
|   5 | GitHub account needed to sign up; community-driven, no purchase necessary                                                 |
|   6 | Patience requested due to conference Wi-Fi limitations                                                                    |
|   7 | Participants join, press start, and wait for the boot process                                                             |
|   8 | Tools used: Tetragon (Mah), Cubecape (Matias), Inspector Gadget (Quasim), Pixie (Dom Delano)                              |
|   9 | Node agent (Cubecape) installed first; follow instructions exactly during explanations                                    |
|  10 | Labs allow sharing ports and terminals for co-play and debugging                                                          |
|  11 | Dev machine has tools like helm and k9s; cplane is a squeezed Kubernetes environment                                      |
|  12 | Application profile CRD applied for later use in noise detection                                                          |
|  13 | Pixie installed for eBPF-native monitoring; data remains node-local unless queried                                        |
|  14 | Run tool used for adversary emulation, based on MITRE ATT&CK framework                                                    |
|  15 | Run UI provides a graph of attack techniques and flow tracking                                                            |
|  16 | Workshop structured as a dungeon with multiple rooms/modules, each with attack and defense parts                          |
|  17 | Initial access demonstrated via compromised pod and tracing policy in Tetragon                                            |
|  18 | Detection of attacks using tracing policies and Pixie queries                                                             |
|  19 | Discovery phase includes environment variable checks and service account token access                                     |
|  20 | Node agent detects anomalies like unexpected service account token use, process drift, and suspicious network connections |
|  21 | Attackers install tools like kubectl and nmap for further exploration                                                     |
|  22 | Detection of nmap scans and reverse DNS queries using Cubecape and Pixie                                                  |
|  23 | Exploitation of vulnerable services (e.g., Redis) and demonstration of lateral movement                                   |
|  24 | Observability tools with high permissions can be abused for cluster takeover                                              |
|  25 | Custom eBPF gadget detects attacks exploiting node/proxy get                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=VA-ne25QX9g)
