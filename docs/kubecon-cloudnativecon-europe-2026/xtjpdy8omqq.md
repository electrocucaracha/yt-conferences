---
type: Video Note
title: "An Immersive and Visual Journey Into Kubernetes Networking - Benoit Entzmann, Feesh"
description: "The speaker, Benoman, a DevSecOps consultant with extensive networking experience, introduces a 3D game designed to visually explain Kubernetes networking concepts, from basic to advanced scenarios. Using an underwater world analogy, he dem..."
resource: https://www.youtube.com/watch?v=Xtjpdy8OmQQ
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, Benoman, a DevSecOps consultant with extensive networking experience, introduces a 3D game designed to visually explain Kubernetes networking concepts, from basic to advanced scenarios.
Using an underwater world analogy, he demonstrates how packets (represented as fish) travel between pods (rooms) and nodes (buildings), illustrating the roles of network layers, eBPF programs, and network policies.
He covers scenarios involving direct pod-to-pod communication, DNS resolution via CoreDNS, service load balancing, and inter-node communication using VXLAN tunnels.
The presentation then explores more advanced topics, including exposing services to the external world through ingress gateways, implementing service mesh with sidecars for observability and routing, and the newer ambient mesh approach using Z tunnel and waypoint components for improved performance and layer 7 processing.
Throughout, Benoman emphasizes the importance of understanding packet flow and the impact of various Kubernetes networking components, concluding with a brief mention of potential future topics like multicluster communication.
# Main Points

|   # | Main point                                                                                       |
| --: | ------------------------------------------------------------------------------------------------ |
|   1 | Presenter is Benoman, a DevSecOps consultant with 20 years in networking and telecommunications. |
|   2 | Developed a 3D game to explain Kubernetes networking concepts.                                   |
|   3 | Demonstration uses four levels: two with Cilium, two with Istio.                                 |
|   4 | Visual analogy: buildings = nodes, rooms = pods, fish = packets, backpack colors = OSI layers.   |
|   5 | Layer 2 (MAC address) not used by Cilium; Layer 3 (IP address/room number) used for routing.     |
|   6 | Layer 4 (transport, e.g., TCP) and Layer 7 (payload) are also represented.                       |
|   7 | Mini camera shows packet path; right panel shows current location.                               |
|   8 | First scenario: packet travels from front-end pod to back-end pod using Cilium.                  |
|   9 | eBPF program processes packets at the host interface, bypassing netfilter/IP tables.             |
|  10 | eBPF checks destination and routes packet directly to destination pod.                           |
|  11 | Port matching at destination is required; mismatched ports result in dropped packets.            |
|  12 | Second scenario: packet resolves a service name via CoreDNS (service has stable IP).             |
|  13 | Service acts as a load balancer, forwarding traffic to pods behind it.                           |
|  14 | Egress network policy checks if packet is allowed to reach CoreDNS.                              |
|  15 | Service translation/load balancing gives pod number behind the service.                          |
|  16 | VXLAN tunnel (overlay network) used for cross-node communication; encapsulates packets.          |
|  17 | Incoming network policy checks source before allowing packet to back-end pod.                    |
|  18 | Third scenario: exposing front-end to the world using service mesh (Istio).                      |
|  19 | External DNS resolves front-end name; packet sent to external IP of load balancer service.       |
|  20 | Ingress gateway pod receives packet; eBPF routes to ingress gateway.                             |
|  21 | Service mesh uses sidecar (Envoy proxy) for observability, tracing, advanced routing.            |
|  22 | IP tables redirect traffic to sidecar before reaching application.                               |
|  23 | Loopback interface used for intra-pod communication between sidecar and app.                     |
|  24 | Fourth scenario: service mesh ambient mode (no sidecar).                                         |
|  25 | Uses edgebone protocol and MTLS for encrypted communication.                                     |
|  26 | Cysto CNI and Z tunnel co                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Xtjpdy8OmQQ)