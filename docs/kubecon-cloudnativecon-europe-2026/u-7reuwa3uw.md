---
layout: default
title:
  "Cloud Native Theater | Cloud Native University: Kubernetes and the Answer
  is… 42! - Jan Stomphorst"
nav_order: 48
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Yan Stoneport, a solutions architect at a Dutch
  cloud-native company, shares a comprehensive checklist of considerations for running
  applications on Kubernetes. He emphasizes the importance of determining whether
  an ap...
resource: https://www.youtube.com/watch?v=U_7Reuwa3Uw
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Yan Stoneport, a solutions architect at a Dutch cloud-native company, shares a comprehensive checklist of considerations for running applications on Kubernetes.
He emphasizes the importance of determining whether an application is stateful or stateless, ensuring security through practices like running containers as non-root users, minimizing image size, and scanning images for vulnerabilities.
Stoneport also highlights best practices such as configuring proper resource requests and limits, using init containers when necessary, managing secrets and configuration, setting up health probes, and defining network policies.
He discusses operational aspects like revision history, rolling updates, logging, metrics, scaling, and the use of certificates for DNS.
The talk concludes by stressing that production readiness requires attention to many details and encourages attendees to adopt a mindset focused on thorough preparation, offering to share his full checklist upon request.

# Main Points

|   # | Main point                                                                                  |
| --: | ------------------------------------------------------------------------------------------- |
|   1 | Determine if your application is stateful or stateless                                      |
|   2 | Generate an SBOM (Software Bill of Materials) for your application                          |
|   3 | Consider security, e.g., use Trivy for image scanning                                       |
|   4 | Ensure your application runs as PID 1 and handles SIGTERM properly                          |
|   5 | Do not use supervisor in containers                                                         |
|   6 | Run your application as a non-root user                                                     |
|   7 | Use minimal base images (e.g., Alpine, Distroless)                                          |
|   8 | Use Kubernetes debug for troubleshooting                                                    |
|   9 | Remove unnecessary layers in your image; balance layer count for build speed                |
|  10 | Use multi-stage builds to avoid including build tools in production images                  |
|  11 | Scan images before and during production                                                    |
|  12 | Properly define entrypoint and command in your Dockerfile                                   |
|  13 | Avoid using the "latest" tag for images                                                     |
|  14 | Drop all unnecessary Linux capabilities in your deployment                                  |
|  15 | Set image pull policy appropriately                                                         |
|  16 | Make root filesystem read-only if possible                                                  |
|  17 | Mount volumes as read-only when feasible                                                    |
|  18 | Configure liveness and readiness probes                                                     |
|  19 | Set resource requests and limits, especially for memory                                     |
|  20 | Limit ephemeral storage in your deployment                                                  |
|  21 | Use init containers if needed for setup tasks                                               |
|  22 | Limit API access and service account tokens to only what is necessary                       |
|  23 | Disable service links if not needed; prefer DNS discovery                                   |
|  24 | Define priority class name for workload prioritization                                      |
|  25 | Configure security context and FSGroup for file permissions                                 |
|  26 | Set up pod topology spread constraints for zone distribution                                |
|  27 | Use anti-affinity and affinity as needed                                                    |
|  28 | Configure pod tolerations appropriately                                                     |
|  29 | Ensure unique labels within a namespace                                                     |
|  30 | Set process deadline seconds to a reasonable value                                          |
|  31 | Store variables in ConfigMaps or Secrets (note: Kubernetes Secrets are only base64 encoded) |
|  32 | Use annotations for tracking and integrations (e.g., Argo, Flux)                            |
|  33 | Set revision history limit to a reasonable number                                           |
|  34 | Configure rolling update settings for deployments                                           |
|  35 | Sign your container images                                                                  |
|  36 | Export logs, metrics, and traces; export Kubernetes events                                  |
|  37 | Define HPA (Horizontal Pod Autoscaler) an                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=U_7Reuwa3Uw)
