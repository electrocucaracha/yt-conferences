---
type: Video Note
title: "Demystifying the Kubernetes Network Stack (From Pod to Pod) - Simone Rodigari, Microsoft"
description: "Simone Rodigari, a software engineer at Microsoft, presents an overview of Kubernetes networking with a focus on pod-to-pod communication and packet tracing within a cluster. He explains that while Kubernetes abstracts much of the networkin..."
resource: https://www.youtube.com/watch?v=fj5UQ0WBmAg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Simone Rodigari, a software engineer at Microsoft, presents an overview of Kubernetes networking with a focus on pod-to-pod communication and packet tracing within a cluster.
He explains that while Kubernetes abstracts much of the networking, understanding the packet path is crucial for effective troubleshooting.
The talk covers key concepts such as Linux network namespaces, virtual Ethernet (veth) connections between pods and nodes, and the data path for both intra-node and cross-node communication, including overlay and underlay networking approaches.
Rodigari details how Kubernetes services provide stable virtual IPs and load balancing through DNAT, and how DNS (via CoreDNS) maps service names to IPs, simplifying communication.
He demonstrates packet tracing and debugging techniques using Linux tools and highlights the importance of understanding these mechanisms for troubleshooting, concluding with a reminder that network policies can be used to secure pod communication.
# Main Points

|   # | Main point                                                                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Focus of session: Kubernetes networking, specifically pod-to-pod communication and packet tracing within a cluster                                                                                              |
|   2 | Importance of understanding packet paths for effective troubleshooting                                                                                                                                          |
|   3 | Six key concepts covered: pod, Linux network namespaces, veth (virtual Ethernet), pod-node connection and node data path, cross-node pod communication, Kubernetes services (DNAT, load balancing), DNS mapping |
|   4 | Kubernetes networking ground rules: unique pod IPs, no NAT between pods, flat layer 3 network                                                                                                                   |
|   5 | Kubernetes delegates networking setup to CNI plugins; kubelet and container runtime create network namespaces and configure veth, IP, and routes                                                                |
|   6 | Veth connects pod network namespace to host network namespace                                                                                                                                                   |
|   7 | Pod-to-pod communication on same node: packet travels via eth0 (pod), veth (host), routed by data path                                                                                                          |
|   8 | Cross-node pod communication: overlay (encapsulation, e.g., VXLAN, IP-IP) or underlay (native routing, e.g., BGP); depends on CNI                                                                               |
|   9 | Pod IPs are ephemeral; direct pod-to-pod communication is unreliable                                                                                                                                            |
|  10 | Kubernetes services provide stable cluster IPs and load balancing across pods                                                                                                                                   |
|  11 | Service data path implemented via kube-proxy (IP tables, NF tables, IPVS) or eBPF                                                                                                                               |
|  12 | DNAT rewrites destination IP to backend pod IP; source IP preserved                                                                                                                                             |
|  13 | Pods never communicate directly with service IP; DNAT maps service IP to pod IP                                                                                                                                 |
|  14 | DNS (CoreDNS) maps service names to cluster IPs; CoreDNS deployed as a service in Kubernetes                                                                                                                    |
|  15 | Packet tracing: packet sent to service IP, DNAT performed at host, routed to backend pod                                                                                                                        |
|  16 | Debugging tools: ip, iptables, eBPF tools, tcpdump, nslookup, dig, kubectl debug                                                                                                                                |
|  17 | Demo setup: kind cluster, kindnet CNI, kube-proxy in IP tables mode                                                                                                                                             |
|  18 | Verified pod-to-pod communication using pod IP, cluster IP, and service name; observed DNAT and load balancing via packet capture and IP tables                                                                 |
|  19 | Kubernetes allows unrestricted pod communication by default; network policies can restrict traffic                                                                                                              |
|  20 | Key takeaways: Kubernetes networking relies on Linux namespaces and veth, service                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fj5UQ0WBmAg)