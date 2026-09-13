---
type: Video Note
title: "An Introduction to Capture The Flag"
description: "Fabian and John from Control Plane introduce an upcoming Capture the Flag (CTF) event at KubeCon, aimed at helping participants sharpen their security skills through hands-on challenges in a vulnerable Kubernetes cluster. They explain the e..."
resource: https://www.youtube.com/watch?v=FvvroBKV6dk
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Fabian and John from Control Plane introduce an upcoming Capture the Flag (CTF) event at KubeCon, aimed at helping participants sharpen their security skills through hands-on challenges in a vulnerable Kubernetes cluster.
They explain the event schedule, requirements (just a web browser and SSH), and coordination via the CNCF Slack channel, where participants will receive SSH bundles to access their own isolated environments.
The CTF consists of three scenarios, each with three hidden flags that can be found by exploring Kubernetes resources, exploiting misconfigurations, and creatively using available tools like Grafana and Victoria Metrics.
The session includes a walkthrough of a sample scenario, demonstrating techniques such as extracting secrets, fixing configuration errors, and leveraging plugins to access restricted data, with points tracked on a live scoreboard.
Participants are encouraged to be resourceful, ask questions, and use the provided GitHub page for guidance, with the organizers available for support throughout the event.
# Main Points

|   # | Main point                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------- |
|   1 | Fabian and John from Control Plane are running the Capture the Flag (CTF) session at CubeCon.                         |
|   2 | Two introduction sessions are offered: one now and another at 2:30 PM.                                                |
|   3 | Control Plane is a security consultancy headquartered in London, with team members globally.                          |
|   4 | CTF is designed to help practitioners and engineers sharpen security skills.                                          |
|   5 | The main CTF event is tomorrow at 11:00 AM; participants need Wi-Fi, a web browser, and SSH.                          |
|   6 | Updates about Wi-Fi and logistics will be posted in the CubeCon-NA-F25 channel on CNCF Slack.                         |
|   7 | Participants will receive SSH bundles (config, known_hosts, private key) to access personal Kubernetes instances.     |
|   8 | The CTF consists of three scenarios, each with a vulnerable Kubernetes cluster to attack and three flags to find.     |
|   9 | Scenarios were built by Andrea and Gabriella from Control Plane.                                                      |
|  10 | Flags can be hidden anywhere (file, pod name, log statement, config map, secret).                                     |
|  11 | All instructions and resources are available on a provided GitHub page (QR code shared).                              |
|  12 | The first scenario involves accessing a Grafana instance and Victoria Metrics in a Kubernetes cluster.                |
|  13 | Participants use kubectl to explore namespaces and RBAC permissions.                                                  |
|  14 | Access to secrets in the Grafana namespace reveals the admin password and the first flag.                             |
|  15 | Flags are submitted to CTFD.io, which tracks progress and points.                                                     |
|  16 | Victoria Metrics scenario involves fixing a typo in a config map to restore metric scraping and find the second flag. |
|  17 | Participants can install tools in their pod or use kubectl patch/edit to solve challenges.                            |
|  18 | Victoria Logs scenario requires integrating Grafana with Victoria Logs to access pod logs and find the third flag.    |
|  19 | Creative solutions are encouraged; multiple approaches are possible for each challenge.                               |
|  20 | Common security issues discussed include excessive RBAC permissions, lack of network controls, and outdated software. |
|  21 | Additional challenges may involve other Kubernetes or cloud-native tools.                                             |
|  22 | Organizers are available for questions                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FvvroBKV6dk)