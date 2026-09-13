---
type: Video Note
title: "Project Lightning Talk: Istio: Set Sailing With Istio Without Sidecars - Lin Sun"
description: "The speaker introduces Istio Ambient, a service mesh architecture that operates without sidecars, and demonstrates its setup and functionality within a Kubernetes cluster. By applying specific labels to a namespace, all pods are enrolled in..."
resource: https://www.youtube.com/watch?v=SwB7W8g9r6I
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces Istio Ambient, a service mesh architecture that operates without sidecars, and demonstrates its setup and functionality within a Kubernetes cluster.
By applying specific labels to a namespace, all pods are enrolled into Ambient mode without needing to restart application pods, enabling features like mutual TLS, layer 7 metrics, observability, and traffic control.
The demo showcases traffic shifting between two versions of a "rag" service, where HTTP route policies are used to direct traffic and enforce policies without sidecars.
The speaker highlights the simplicity and efficiency of Ambient mode, emphasizing its lighter architecture and ease of deployment, and concludes by summarizing the benefits observed in the demonstration.
# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on Istio Ambient, a service mesh running without sidecars.                                                    |
|   2 | Demo is conducted on a Kubernetes cluster in the default namespace.                                                                |
|   3 | Demo application and rag pods (version one and two) are deployed without sidecars (one container per pod).                         |
|   4 | Enrolling pods into Ambient requires adding the label istio.io/dataplane-mode=ambient to the namespace.                            |
|   5 | No need to restart application pods when enrolling into Ambient.                                                                   |
|   6 | Layer 7 policy enforcement is demonstrated using HTTP routes for traffic shifting between rag v1 and v2.                           |
|   7 | A waypoint is deployed and the namespace is labeled to use the waypoint for HTTP routes.                                           |
|   8 | Two HTTP routes are set up: one from Istio ingress gateway to the demo app, and one for controlling traffic between rag v1 and v2. |
|   9 | Initially, all traffic is routed to rag version one.                                                                               |
|  10 | Demo application is accessed via port forwarding (ingress forwarded to 8888).                                                      |
|  11 | Rag version one service only handles PDF files; TXT files are not supported.                                                       |
|  12 | Traffic shifting is demonstrated by updating the HTTP route policy to send all traffic to rag version two.                         |
|  13 | After updating, rag version two successfully handles TXT file uploads.                                                             |
|  14 | Istio Ambient is described as a lighter architecture that removes the need for sidecars.                                           |
|  15 | Ambient provides mutual TLS, layer 7 metrics, observability, traffic control, and authorization policy via waypoint.               |
|  16 | Visualization in the demo shows traffic routing and file handling differences between rag v1 and v2.                               |
|  17 | Demo concludes with a summary of Ambient’s benefits and features.                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SwB7W8g9r6I)