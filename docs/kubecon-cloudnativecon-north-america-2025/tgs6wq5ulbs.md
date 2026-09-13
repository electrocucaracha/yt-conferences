---
type: Video Note
title: "Return of the Mesh: Gateway API's Epic Quest for Unity - Henrik Rexed, Dynatrace"
description: "The speaker, Henrik Cruxed, introduces a comparative analysis of service meshes in the cloud-native ecosystem, focusing on the Gateway API and its impact on service mesh functionality. He reviews several service meshes—Kuma, Linkerd, Istio..."
resource: https://www.youtube.com/watch?v=tgs6Wq5UlBs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, Henrik Cruxed, introduces a comparative analysis of service meshes in the cloud-native ecosystem, focusing on the Gateway API and its impact on service mesh functionality.
He reviews several service meshes—Kuma, Linkerd, Istio, and Ambient (with and without KGateway)—highlighting their architectures, configuration simplicity, observability features, and support for key capabilities like ingress/egress, mTLS, traffic splitting, circuit breaking, and rate limiting.
While the Gateway API brings promise by separating platform and routing concerns and supporting both north-south and east-west traffic, it currently lacks full support for advanced service mesh policies, requiring users to rely on mesh-specific CRDs or extensions.
Benchmark results show Ambient mesh offers the lowest latency but lacks some features unless combined with KGateway, while Kuma is noted for its simplicity but higher resource usage.
The speaker concludes that combining Ambient with KGateway provides a strong balance of simplicity, features, and performance, though he encourages users to choose based on their needs and to provide feedback for further improvement.
# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction to service meshes and Gateway API in the context of cloud native environments                                                                            |
|   2 | Presenter: Henrik Cruxed, cloud advocate, CNCF ambassador, performance engineer, content creator (Perf Bites, Is It Observable?)                                      |
|   3 | Overview of service mesh solutions: Kuma, Linkerd, Istio, Ambient, KGateway                                                                                           |
|   4 | Gateway API separates platform security (Gateway) from routing (Routes)                                                                                               |
|   5 | Gateway API supports north-south (ingress) and east-west (service-to-service) traffic                                                                                 |
|   6 | Gamma initiative focuses on service mesh interoperability with Gateway API                                                                                            |
|   7 | Gateway API now includes inference support for machine learning workloads                                                                                             |
|   8 | CRDs available: HTTPRoute, GRPCRoute, TLSRoute, TCPRoute, UDPRoute                                                                                                    |
|   9 | HTTPRoute features: traffic split, request mirroring, timeouts, retries; lacks circuit breaker support                                                                |
|  10 | GRPCRoute has fewer features; complex routing limited                                                                                                                 |
|  11 | ExtensionRef and TargetRef mechanisms for attaching policies; TargetRef not widely implemented yet                                                                    |
|  12 | Most service meshes support Gateway API and Gamma initiative; AI inference support mainly in Istio family                                                             |
|  13 | Service mesh architecture: control plane and data plane (proxy-based, sidecar or sidecarless models)                                                                  |
|  14 | Sidecar model: local proxy per app, low latency, higher resource usage                                                                                                |
|  15 | Sidecarless model: node-level proxy, efficient for L4, requires additional proxy for L7                                                                               |
|  16 | Feature expectations: ingress/egress, mTLS, traffic split, circuit breaker, rate limiting, timeouts, retries, observability                                           |
|  17 | Kuma: simple configuration, straightforward CRDs, easy mesh joining via annotation                                                                                    |
|  18 | Linkerd: uses service profile CRDs for advanced features, requires extension references, mesh joining via annotation                                                  |
|  19 | Istio/Ambient: many CRDs, requires destination rules and envoy filters for advanced features, mesh joining via annotation (sidecar for Istio, no restart for Ambient) |
|  20 | KGateway adds missing features (circuit breaker, rate limiting) to Ambient                                                                                            |
|  21 | Observability: all solutions support OpenTelemetry; Kuma and Istio/Ambient have smoother integration                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tgs6Wq5UlBs)