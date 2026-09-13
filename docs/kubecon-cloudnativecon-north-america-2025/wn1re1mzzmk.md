---
type: Video Note
title: "Kubernetes at the Edge – Come See It in Action! - Xavier Avrillier & Antonia von den Driesch"
description: "Antonia and Savvi from Giantswarm introduce Kubernetes at the edge, explaining that edge computing brings data processing closer to where information is generated, such as in factories with IoT devices, to address challenges like latency, b..."
resource: https://www.youtube.com/watch?v=Wn1rE1MzZmk
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Antonia and Savvi from Giantswarm introduce Kubernetes at the edge, explaining that edge computing brings data processing closer to where information is generated, such as in factories with IoT devices, to address challenges like latency, bandwidth, autonomy, and privacy.
They focus on the open-source project KubeEdge, which extends Kubernetes to edge and IoT environments by handling unreliable networks and managing devices through a device twin model.
The architecture involves a cloud core component in the Kubernetes cluster and an edge core on each edge node, enabling edge devices to appear as standard Kubernetes nodes and continue operating workloads even when offline, thanks to local caching.
They demonstrate a practical setup using a Raspberry Pi, webcam, and Python app to count raised hands, showing how device data is collected, mapped, and visualized through KubeEdge’s custom resources and mappers.
The session concludes with a Q&A covering KubeEdge’s applicability beyond IoT, its resource overhead, installation process, digital twin representation, and how edge nodes maintain operation during network disconnections.
# Main Points

|   # | Main point                                                                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Antonia and Savvi from Giantswarm present on Kubernetes at the edge, focusing on edge computing and the KubeEdge project.                                                                                                                            |
|   2 | Edge computing processes data close to where it’s produced, reducing latency, bandwidth usage, and supporting autonomy and privacy.                                                                                                                  |
|   3 | Edge computing is used in IoT, retail, smart cities, telco, healthcare, automotive, and more.                                                                                                                                                        |
|   4 | Running workloads at the edge differs from the cloud: many small, resource-constrained, sometimes offline nodes.                                                                                                                                     |
|   5 | Kubernetes is useful at the edge due to its declarative, portable, and automated nature.                                                                                                                                                             |
|   6 | Vanilla Kubernetes assumes stable networking, which is not always available at the edge.                                                                                                                                                             |
|   7 | KubeEdge extends Kubernetes to edge and IoT devices, handling unreliable networks and device management via device twins.                                                                                                                            |
|   8 | KubeEdge started in 2018 by Huawei, joined CNCF in 2019, and graduated in October 2024.                                                                                                                                                              |
|   9 | Success stories include China’s electronic toll collection system (100,000 edge nodes, 300 million data points/day) and cloud-native edge satellites for disaster mitigation (reduced response time from days to hours, 90% less data transmission). |
|  10 | KubeEdge architecture: Cloud Core (in Kubernetes cluster) connects to Edge Core (on each edge node); Edge Core communicates with devices via MQTT and local apps via HTTP.                                                                           |
|  11 | Cloud Core components: Cloud Hub (messaging broker), Edge Controller (workload/status sync), Device Controller (device CR reconciliation).                                                                                                           |
|  12 | Edge Core components: Edge Hub (cloud link), Meta Manager (local cache), Device Twin (device state), Edged (manages pods), Beehive (messaging layer), Event Bus (MQTT), Service Bus (HTTP).                                                          |
|  13 | Devices are integrated via mappers (protocol translators) and represented as Kubernetes custom resources (device models and instances).                                                                                                              |
|  14 | Demo: Raspberry Pi with webcam and Python app detects raised hands, data flows via MQTT mapper to KubeEdge, visualized in Grafana.                                                                                                                   |
|  15 | KubeEdge overhead on edge devices is about 70-100MB RAM.                                                                                                                                                                                             |
|  16 | Edge Core is installed on edge devices using a token                                                                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Wn1rE1MzZmk)