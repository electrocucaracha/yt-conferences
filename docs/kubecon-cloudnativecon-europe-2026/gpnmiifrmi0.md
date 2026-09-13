---
type: Video Note
title: "K8s-sigs NFD × SYLVA: Declarative Image-to-Node Compatibi... Eduardo Arango Gutierrez & Chaoyi Huang"
description: "The presentation discusses a collaborative project between the Kubernetes community, the Node Feature Discovery (NFD) maintainers, and the Silva Foundation to address the challenge of deploying containers across highly heterogeneous hardwar..."
resource: https://www.youtube.com/watch?v=GPnMIIfrmi0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation discusses a collaborative project between the Kubernetes community, the Node Feature Discovery (NFD) maintainers, and the Silva Foundation to address the challenge of deploying containers across highly heterogeneous hardware environments, such as those found in telecom and academic high-performance computing (HPC) clusters.
The problem arises because containers, while designed to be portable, often encounter compatibility and performance issues due to differences in system-on-chips (SoCs), CPUs, and other hardware components.
The solution involves integrating NFD with Silva’s validation framework to capture detailed node information and embed it as artifacts within container images using the ORAS registry standard.
This enables precise scheduling of containers to compatible nodes by matching image metadata with node features, reducing deployment failures and improving reliability, especially in environments with strict service level agreements.
The approach supports multi-architecture images and allows for fine-grained control over deployments, benefiting both telecom operators and academic institutions with diverse hardware.
The project is open for contributions, and further details are available in a Kubernetes blog post.
# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on solving heterogeneous hardware compatibility issues in Kubernetes environments, especially for telecom and academic use cases.                                |
|   2 | NFD (Node Feature Discovery) integration with the Silva Foundation addresses real-world problems of deploying containers across diverse SOCs and hardware.                        |
|   3 | Telecom operators require high service availability (five nines), strict SLAs, and low latency, making hardware compatibility critical.                                           |
|   4 | Network outages can have significant economic impacts; minor issues can propagate due to interconnected devices (the "butterfly effect").                                         |
|   5 | Traditionally, vendors ensured compatibility by testing applications on specific hardware and OS stacks; now, operators expect compatibility on third-party Kubernetes platforms. |
|   6 | Compatibility validation before deployment is essential due to short rollout windows and the need for zero downtime.                                                              |
|   7 | SA (Silva Automation) is a Linux Foundation project releasing Kubernetes stacks tailored for telecom and edge use cases, with a validation program for telecom applications.      |
|   8 | Image compatibility validation is integrated into the SA validation center, using automation scripts and Kubernetes jobs.                                                         |
|   9 | NFD enhancements allow capturing detailed node information and embedding it as artifacts with container images using the ORAS standard.                                           |
|  10 | The solution involves building images with NFD-generated artifacts, storing them in ORAS registries, and using an NFD CLI and admission controllers for scheduling.               |
|  11 | Node Feature Groups (NFGs) aggregate infrastructure into catalogs for fine-grained scheduling and compatibility matching.                                                         |
|  12 | The NFD scheduler uses node and image metadata to ensure containers are only deployed on compatible nodes.                                                                        |
|  13 | The approach supports multi-vendor, multi-architecture clusters and is beneficial for both telecom and academic environments.                                                     |
|  14 | The NFD matching system allows for flexible rule definitions, including ranges and matchers for fine-grained control.                                                             |
|  15 | The system supports multi-archi                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GPnMIIfrmi0)