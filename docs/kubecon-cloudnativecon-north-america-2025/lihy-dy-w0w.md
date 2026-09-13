---
type: Video Note
title: "Navigating the AI/ML Networking Maze in Kubernetes: Lessons From the Trenches - Antonio Ojea, Google"
description: "In this talk, Antonio from Google’s SIG Network shares his experiences navigating complex networking challenges in Kubernetes, particularly as they relate to large-scale AI/ML workloads. He recounts how issues such as DNS delays and headles..."
resource: https://www.youtube.com/watch?v=liHY_dy-W0w
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Antonio from Google’s SIG Network shares his experiences navigating complex networking challenges in Kubernetes, particularly as they relate to large-scale AI/ML workloads.
He recounts how issues such as DNS delays and headless service scalability impacted performance for jobs requiring thousands of nodes, leading to improvements like measuring DNS propagation delays and adding server-side filtering for headless services.
Antonio explains the limitations of traditional device and network plugin models, especially when coordinating specialized hardware like GPUs and network interfaces, and introduces the Device Resource Assignment (DRA) API as a solution that enables more precise and efficient resource pairing.
He describes how the DRA and related projects, such as the open-source Det at Google, improve both performance consistency and user experience by making workloads more portable and easier to configure.
The talk concludes with a discussion of ongoing efforts to further optimize inter-node communication and expose hardware topology information, aiming to deliver seamless, efficient infrastructure for evolving AI/ML workloads in Kubernetes.
# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is Antonio, works at Google in SIG Network, focused on improving Kubernetes networking.                                                                                                 |
|   2 | Collaboration with others in SIG Network and networking community, including Multus and projects like Cilium and Calico.                                                                        |
|   3 | Real-world issue reported by Vanessa from Limor Lab: MPI jobs in Kubernetes were slow due to networking problems.                                                                               |
|   4 | MPI jobs require coordinated, lock-step communication between processes, relying on DNS and headless services for pod discovery.                                                                |
|   5 | Discovered DNS scalability issue: CoreDNS struggled to generate DNS records quickly for large jobs (e.g., 5,000 nodes), causing delays and financial cost.                                      |
|   6 | Identified Golang DNS resolver bug: exceeded TCP DNS record limits, causing failures in resolving pod names.                                                                                    |
|   7 | Solution: Added a new SLI to measure DNS propagation delay; optimized CoreDNS and used local DNS cache.                                                                                         |
|   8 | Another issue: clusters with tens of thousands of headless services caused excessive API server load, as kubelet and kube-proxy watched all services unnecessarily.                             |
|   9 | Solution: Implemented server-side field selector filtering in the API server to reduce resource consumption.                                                                                    |
|  10 | Persistent performance issues due to hardware topology: AI/ML workloads use GPUs/TPUs and specialized NICs, but lack of standardization led to inefficient resource pairing.                    |
|  11 | Introduced DRA (Device Resource Assignment) API in Kubernetes 1.34, allowing devices to express qualities and enabling scheduling of compound resources (e.g., specific GPU with specific NIC). |
|  12 | Developed Kubernetes Network Driver (KND) using DRA and NRI to provide efficient network functionality.                                                                                         |
|  13 | Example: Det project at Google uses DRA with Nvidia GPU driver for complex topology scheduling; open source and GA.                                                                             |
|  14 | DRA model provides consistent, zero-variance performance and better user experience compared to device plugin/CNI chaining.                                                                     |
|  15 | DRA enables portable workloads with simple configuration, improving efficiency and reducing infrastructure lock-in.                                                                             |
|  16 | Lessons learned: DNS and headless services                                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=liHY_dy-W0w)