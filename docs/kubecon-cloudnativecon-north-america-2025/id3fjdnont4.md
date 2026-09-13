---
type: Video Note
title: "An Introduction to Capture The Flag"
description: "Fabian from Control Plane introduces a Kubernetes-themed Capture the Flag (CTF) event at KubeCon, designed to teach participants about common security pitfalls by letting them break into intentionally vulnerable Kubernetes clusters. The eve..."
resource: https://www.youtube.com/watch?v=Id3FJDnont4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Fabian from Control Plane introduces a Kubernetes-themed Capture the Flag (CTF) event at KubeCon, designed to teach participants about common security pitfalls by letting them break into intentionally vulnerable Kubernetes clusters.
The event, organized by a 50-person security consultancy, provides three different scenarios—each with three flags to find—created by their security engineers, Andrea and Gabriella.
Participants connect to the clusters using SSH credentials provided via the CNCF Slack channel, and only need SSH and a web browser to play.
The walkthrough demonstrates how to explore the cluster, identify misconfigurations, and creatively use available tools like kubectl and Grafana plugins to uncover flags, with points awarded for each flag found and a live scoreboard tracking progress.
The event is flexible, allowing participants to join at any time during the day, and support is available both in person and online, with hints accessible at a points cost.
# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Fabian from Control Plane introduces the Capture the Flag (CTF) event at KubeCon.                                                                           |
|   2 | Control Plane is a security consultancy with about 50 people across UK, Europe, North America, and APAC.                                                    |
|   3 | The CTF events are designed to teach about common security pitfalls in Kubernetes and cloud environments.                                                   |
|   4 | Vulnerable Kubernetes clusters are intentionally designed for participants to break into and learn attacker techniques.                                     |
|   5 | Three scenarios will be available in the main event, each with three flags to find (total of nine flags).                                                   |
|   6 | Credentials for the event are provided via the CNCF Slack, specifically in the KubeCon NACTF channel.                                                       |
|   7 | Participants need only SSH and a web browser; all other tools are provided.                                                                                 |
|   8 | Each scenario is created by Control Plane security engineers Andrea and Gabriella.                                                                          |
|   9 | Instructions, schedule, and setup details are available on a dedicated web page (QR code provided).                                                         |
|  10 | Participants receive a tar.gz archive with SSH key, config, and known hosts file for access.                                                                |
|  11 | Each participant gets their own Kubernetes cluster and jump host (Debian-based, with kubectl access).                                                       |
|  12 | Participants can install additional tools as needed within resource limits.                                                                                 |
|  13 | The event is not strictly time-based; participants can join anytime during the day but competing for first place is easier if starting at 11 a.m.           |
|  14 | Flags follow the pattern "flag{ctf...}" and can be found in various locations (pod name, log file, annotation, etc.).                                       |
|  15 | CTFD is used as the scoreboard; flags are submitted there for points.                                                                                       |
|  16 | Scenarios involve exploring Kubernetes resources, decoding secrets, fixing misconfigurations, and creatively using available tools (e.g., Grafana plugins). |
|  17 | Points are awarded based on scenario difficulty; leaderboard is overall, not per scenario.                                                                  |
|  18 | Hints can be requested via CTFD at the cost of points.                                                                                                      |
|  19 | Wi-Fi issues are being addressed; SSH uses minimal data.                                                                                                    |
|  20 | Participants can play remotely after receiving credentials via Slack; on-site support is available.                                                         |
|  21 | Scenarios vary                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Id3FJDnont4)