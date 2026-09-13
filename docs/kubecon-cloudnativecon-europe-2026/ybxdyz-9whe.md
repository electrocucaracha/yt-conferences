---
type: Video Note
title: "Kube-Oddities - The Quirks That Keep Kubernetes Interesting - Marcus Noble & Márk Sági-Kazár"
description: "In this talk, Marcus Noble and Mark Shagi Kazar, both experienced Kubernetes practitioners and CNCF ambassadors, share a range of oddities and quirks they've encountered in Kubernetes over their careers. They discuss the confusing implement..."
resource: https://www.youtube.com/watch?v=ybxDYZ-9wHE
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Marcus Noble and Mark Shagi Kazar, both experienced Kubernetes practitioners and CNCF ambassadors, share a range of oddities and quirks they've encountered in Kubernetes over their careers.
They discuss the confusing implementation of sidecar containers, best practices for referencing container images using SHAs, and inconsistencies in volume referencing between secrets and config maps.
The speakers highlight networking nuances, such as the inability to assign DNS directly to pods and the use of headless services as a workaround, as well as the misleading default value for DNS policies.
Security topics include the risks of unrevokable service account tokens and the dangers of overly broad RBAC permissions, especially with the "escalate" verb.
They also explain the limitations of admission policies, operational differences between kubectl and crictl, and the use of static manifests and kubelet standalone mode for running pods outside the API server.
Throughout, they invite the audience to share their own Kubernetes oddities and provide resources for further learning.
# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Marcus Noble and Mark Shagi Kazar introduce themselves as CNCF ambassadors with extensive Kubernetes experience.                                           |
|   2 | The talk focuses on "cube oddities"—unusual or confusing aspects of Kubernetes.                                                                            |
|   3 | Sidecar containers are now officially supported in Kubernetes 1.29 via init containers with restartPolicy: Always.                                         |
|   4 | The sidecar container implementation uses a special init container, not a distinct sidecar type.                                                           |
|   5 | Best practice for container images is to reference images by SHA, not tags, to ensure immutability.                                                        |
|   6 | If both a tag and SHA are specified, Kubernetes uses only the SHA; keep them in sync for clarity.                                                          |
|   7 | Referencing secrets as volumes uses "secret.secretName", while config maps use "configMap.name"—an inconsistency that often causes confusion.              |
|   8 | Pod hostnames and subdomains can be set, but pods cannot be addressed directly via DNS.                                                                    |
|   9 | Headless services allow direct pod addressing by attaching the pod name to the DNS domain.                                                                 |
|  10 | The default DNS policy for pods is "ClusterFirst", not "Default".                                                                                          |
|  11 | Kubernetes allows creation of service account tokens that cannot be revoked or rotated except by expiration or deleting the service account.               |
|  12 | RBAC is additive; users can only create roles with permissions they already have, unless they have the "escalate" verb, which allows privilege escalation. |
|  13 | Admission policies and webhooks cannot restrict themselves; they cannot control creation, deletion, or editing of other admission policies or webhooks.    |
|  14 | "crictl" (CRI tool) can be used to interact with the container runtime interface, which differs from "kubectl".                                            |
|  15 | Pod sandboxes in CRI are similar but not identical to Kubernetes pods.                                                                                     |
|  16 | Kubelet can run pods without an API server using static manifests; such pods can be hidden by placing them in a non-existent namespace.                    |
|  17 | Static manifests are used for control plane components and kubelet standalone mode; these pods lack features requiring the API server.                     |
|  18 | Kubelet has its own API, accessible via "kubeletctl".                                                                                                      |
|  19 | Additional resou                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ybxDYZ-9wHE)