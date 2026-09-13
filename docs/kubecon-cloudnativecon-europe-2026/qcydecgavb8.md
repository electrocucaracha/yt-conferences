---
type: Video Note
title: "Cloud Native at the Far(m) Edge: Running Kubernetes and AI... Mauro Morales & Jordan Karapanagiotis"
description: "The presentation discusses the application of cloud-native technologies, specifically Kubernetes and AI, at the farm edge to improve precision agriculture and reduce crop waste. The speakers describe how Ara Imaging’s Tree Scout device uses..."
resource: https://www.youtube.com/watch?v=qCyDeCGavB8
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation discusses the application of cloud-native technologies, specifically Kubernetes and AI, at the farm edge to improve precision agriculture and reduce crop waste.
The speakers describe how Ara Imaging’s Tree Scout device uses real-time computer vision and AI on ruggedized Nvidia Jetson hardware to map orchard blossoms, enabling targeted spraying and better fruit quality while minimizing chemical use.
They highlight the challenges of running edge systems, such as limited bandwidth, maintenance, and security, and explain how adopting the Kyros immutable Linux distribution and K3s Kubernetes has streamlined operations, enabled over-the-air updates, and improved fleet management without requiring field engineers.
The collaboration between Ara Imaging and the open-source Kyros project has led to mutual benefits, including feedback-driven improvements and easier deployment for new users.
Overall, the integration of these technologies has resulted in more sustainable farming practices, operational efficiencies, and a growing adoption of the Tree Scout system.
# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation topic: Cloud native at the farm edge, focusing on Kubernetes, AI, and immutable systems in agriculture.                                               |
|   2 | Precision farming aims to reduce post-harvest losses, which affect about 25% of global crop production.                                                            |
|   3 | In the Netherlands, average farms produce 10 million fruits per year, with 2.5 million wasted.                                                                     |
|   4 | Ara Imaging uses blossom thinning (precision thinning) to improve fruit quality and reduce waste.                                                                  |
|   5 | Process: Tractor with computer vision detects blossoms, creates blossom maps, and enables targeted spraying.                                                       |
|   6 | Tree Scout product: Embedded device with camera sensors, Nvidia Jetson, GPS, and a universal terminal for tractor integration.                                     |
|   7 | Real-time computer vision processes 15 frames per second at 1080p, requiring edge AI due to bandwidth and timing constraints.                                      |
|   8 | AI inference is performed on the edge device; only lightweight data is sent to the cloud.                                                                          |
|   9 | Edge computing challenges: maintenance, lack of technical staff, security, and diverse environments.                                                               |
|  10 | Chyros: An immutable, image-based Linux OS designed for edge, cloud, and on-prem, with features like trusted boot, no configuration drift, and simple maintenance. |
|  11 | Chyros integrates with Kubernetes for lifecycle management and supports canary upgrades.                                                                           |
|  12 | Arya Imaging transitioned from a single Python app to microservices on K3S Kubernetes, improving control, troubleshooting, and deployment.                         |
|  13 | Adoption of Chyros enabled over-the-air system upgrades, reducing the need for field engineers and standardizing operations.                                       |
|  14 | Homogeneous fleet management and defined OS images improved provisioning and troubleshooting.                                                                      |
|  15 | Tree Scout aims for a 20% reduction in crop waste; adoption is growing in Europe and the US.                                                                       |
|  16 | Collaboration between Arya Imaging and Chyros benefited both the company and the open-source project through feedback, testing, and improved governance.           |
|  17 | Demo showcased blossom mapping and targeted spraying, resulting in reduced waste and chemical use.                                                                 |
|  18 | References provided for Chyros documentati                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qCyDeCGavB8)