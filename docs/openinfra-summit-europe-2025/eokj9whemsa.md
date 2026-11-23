---
layout: default
title: "Scaling Kubernetes to 2,000 Pods with 10,000 Interfaces per worker node  Achieving Stability in High"
nav_order: 78
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Matias and Andre from Deutsche Telecom presented their work on scaling Kubernetes to emulate large-scale non-terrestrial networks, such as satellite constellations, where nodes are mobile and stand..."
resource: "https://www.youtube.com/watch?v=eokj9WhEMsA"
youtube_stats:
  view_count: 88
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Matias and Andre from Deutsche Telecom presented their work on scaling Kubernetes to emulate large-scale non-terrestrial networks, such as satellite constellations, where nodes are mobile and standard routing algorithms require rigorous testing.
To address the complexity of these networks, they developed a platform using containers and Linux traffic control to simulate link characteristics, avoiding the overhead of virtual machines while ensuring that network conditions are controlled externally to prevent validation bias.
The team faced significant technical challenges, including IPv6 instability in standard tools like Canonical’s MAAS and Ironic, which led them to build a custom, fully automated netboot installation process using standard HTTP, DNS, and image builders.
They also resolved numerous hardware and kernel limitations, such as MAC address table overflows, socket buffer sizes, and BIOS bugs, ultimately achieving a stable setup capable of running approximately 2,000 ports with five interfaces per worker node.
Looking ahead, the team plans to integrate NASA satellite data for higher-fidelity simulations, test existing protocols like OSPF and IS-IS, and potentially share their configuration knowledge through open-source documentation or containerized solutions.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Matias and Andre from Deutsche Telekom presented their work on scaling Kubernetes to emulate non-REST networks with moving nodes, such as satellite constellations.                            |
|   2 | The motivation for the project was to test routing algorithms in dynamic networks where nodes change positions, which standard analytical methods cannot handle.                               |
|   3 | The emulation platform must block or allow communication between interfaces based on node positions, such as satellite visibility over the horizon.                                            |
|   4 | To avoid validation problems, the platform controls network conditions externally rather than letting the emulated software decide its own link conditions.                                    |
|   5 | The system must scale to support thousands of ground stations and satellites, including constellations with up to 8,000 satellites like SpaceX.                                                |
|   6 | Containers were chosen over virtual machines due to lower overhead, while traffic control and network filter tables were used to emulate the link layer.                                       |
|   7 | Key requirements included determining container density, identifying bottlenecks that affect emulation fidelity, ensuring long-term stability, and supporting unrestricted network topologies. |
|   8 | The lab setup uses Dell servers with 25-gigabit and 100-gigabit connections, utilizing bonding protocols and exclusively IPv6.                                                                 |
|   9 | Canonical's MAAS and Ironic failed to provide stable IPv6 support, leading the team to develop a custom handcrafted installation process.                                                      |
|  10 | The custom installation uses standard tools like DHCP, TFTP, and an image builder to create a bootable disk image with specific scripts.                                                       |
|  11 | A BIOS bug in Dell hardware caused boot failures with standard IPv6 configurations, which was resolved after weeks of debugging and vendor support.                                            |
|  12 | Kernel parameters such as file descriptor limits, socket buffer sizes, and packet processing cycles had to be significantly increased to handle thousands of interfaces.                       |
|  13 | Network interface cards experienced MAC address table overflows, requiring workarounds to disable hardware offloading and handle traffic in software.                                          |
|  14 | Centralized IP address managers overwhelmed the system, so the team switched to using IPv6 with global addresses to manage the high volume of interfaces.                                      |
|  15 | The final stable setup supports approximately 2,000 ports per worker node, with each port having five interfaces, including one primary and four multi-homed interfaces.                       |
|  16 | The entire setup is fully automated via CI/CD pipelines, allowing for complete reinstallation from scratch to ensure consistency.                                                              |
|  17 | Current testing involves basic ICMP traffic to verify topology stability, with future plans to test OSPF and IS-IS protocols in dynamic topologies.                                            |
|  18 | Preliminary tests revealed issues with return path hot counts and TTL expirations, indicating potential problems in routing behavior under changing topologies.                                |
|  19 | The team is developing a simulator that loads satellite positioning data from NASA to automatically generate network topologies and link conditions.                                           |
|  20 | Future work includes improving the fidelity of topology emulations to reduce command lag and its impact on the software running in containers.                                                 |
|  21 | The solution is open source, with plans to publish a paper and potentially distribute the boot server solution as a containerized package.                                                     |
|  22 | The team is open to collaboration and research partnerships, noting that their scaling level exceeds that of other known simulators or emulators.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eokj9WhEMsA/hqdefault.jpg)](https://www.youtube.com/watch?v=eokj9WhEMsA)

[Watch on YouTube](https://www.youtube.com/watch?v=eokj9WhEMsA)
