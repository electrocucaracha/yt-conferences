---
layout: default
title: End-to-End Security With gRPC in Kubernetes - Shiva & Abhishek Agrawal, Google
nav_order: 69
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this CubeCon Atlanta session, Abhishek and Shiva from Google’s GPC
  team discuss the security journey for microservices using gRPC in Kubernetes environments.
  They begin by explaining the importance of TLS for authentication, encryption...
resource: https://www.youtube.com/watch?v=fhjiLyntYBg
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this CubeCon Atlanta session, Abhishek and Shiva from Google’s GPC team discuss the security journey for microservices using gRPC in Kubernetes environments.
They begin by explaining the importance of TLS for authentication, encryption, and integrity, and highlight the operational challenges of managing certificates and mutual TLS (mTLS) at scale, recommending tools like cert-manager for automation.
The presenters then address the need for user-level authentication using JWTs and advocate for using interceptors to centralize token validation.
They introduce service meshes like Istio, which offload security and authorization logic from application code to infrastructure via sidecar proxies, simplifying management but adding network latency.
To address performance concerns, they present proxyless gRPC, which integrates directly with the service mesh control plane using XDS APIs, eliminating the sidecar and reducing latency while shifting some security responsibilities back to the application.
The talk concludes with best practices for securing gRPC in Kubernetes, emphasizing layered security, automation, and centralized policy management.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Abshik and Shiva, software developers at Google, present on the security journey in Kubernetes, focusing on TLS, service mesh, and proxyless gRPC.               |
|   2 | Microservices and gRPC are now industry standards for building distributed systems.                                                                              |
|   3 | gRPC is preferred for its high performance, HTTP2 support, lightweight serialization (Protobuf), and bidirectional streaming.                                    |
|   4 | Kubernetes introduces security risks due to its dynamic, flat network; static firewall rules are ineffective.                                                    |
|   5 | End-to-end security is essential; TLS provides authentication, encryption, and integrity.                                                                        |
|   6 | Standard TLS only authenticates the server; mutual TLS (mTLS) is needed for zero trust, authenticating both client and server.                                   |
|   7 | mTLS is operationally challenging in Kubernetes due to certificate generation, secure distribution, and rotation.                                                |
|   8 | cert-manager automates certificate issuance, renewal, and management in Kubernetes.                                                                              |
|   9 | cert-manager workflow: define issuer (CA), create certificate resource, cert-manager issues and stores certificate as a Kubernetes secret, mount secret in pods. |
|  10 | cert-manager handles certificate renewal and updates secrets automatically.                                                                                      |
|  11 | mTLS provides service identity but not user identity; user authentication is handled via JWTs (JSON Web Tokens).                                                 |
|  12 | JWTs are obtained from identity providers and attached to gRPC metadata; servers verify tokens and extract claims.                                               |
|  13 | Use interceptors in gRPC to validate JWTs and populate user context.                                                                                             |
|  14 | Service mesh (e.g., Istio) moves security from application to infrastructure layer using sidecar proxies (Envoy).                                                |
|  15 | Service mesh enables mTLS, certificate management, and authorization policies with minimal code changes.                                                         |
|  16 | Sidecar proxies add network latency; for high-scale or real-time services, this can be a concern.                                                                |
|  17 | Proxyless gRPC eliminates sidecar proxies, integrating XDS APIs directly into gRPC libraries for improved performance.                                           |
|  18 | Proxyless gRPC shifts mTLS and JWT validation back to the application layer.                                                                                     |
|  19 | XDS APIs provide dynamic configur                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fhjiLyntYBg)
