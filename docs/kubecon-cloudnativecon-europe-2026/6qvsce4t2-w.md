---
layout: default
title:
  Exploring NRI for Automated CA Trust Injection - Tsuzuki Tsuchiya & Kento Kubo,
  LY Corporation
nav_order: 110
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Suzuit and Kent Kubo discuss the challenges of
  injecting private CA certificates into containers within their private cloud infrastructure,
  which operates over 1,000 Kubernetes clusters. They review existing approaches...
resource: https://www.youtube.com/watch?v=6qvsce4t2_w
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

In this presentation, Suzuit and Kent Kubo discuss the challenges of injecting private CA certificates into containers within their private cloud infrastructure, which operates over 1,000 Kubernetes clusters.
They review existing approaches—such as modifying Dockerfiles, using init containers, and mounting static files—and highlight their limitations, particularly regarding OS and language-specific trust store differences.
To address these issues, they developed an automated solution using the Node Resource Interface (NRI), which enables OS- and language-aware CA certificate injection during container startup with minimal user intervention, requiring only a pod annotation.
Their implementation leverages NRI plugins, OCI hooks, and an entry point modifier to detect environments and inject certificates appropriately, currently supporting Node.js and Python, with plans to add Java and other languages.
While their approach simplifies certificate management and improves automation, it requires node-level privileges and does not yet support read-only filesystems or complete CA replacement, but future work aims to address these limitations and integrate with Kubernetes standards like cluster trust bundles.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on automating CA trust injection in containers using NRI (Node Resource Interface)                                                |
|   2 | Private cloud runs on multiple on-premises data centers using OpenStack and Ascend for IAM                                                     |
|   3 | Over 1,000 Kubernetes clusters managed, with internal PKI and private CA for certificate management                                            |
|   4 | Private CA certificates trusted internally, not externally; installing them in all containers is challenging                                   |
|   5 | Existing approaches for CA injection:                                                                                                          |
|   6 | Dockerfile multi-stage builds: requires maintaining images, CI pipelines, Dockerfiles                                                          |
|   7 | Init containers: complex pod templates, mutating webhooks, slower startup                                                                      |
|   8 | Mounting static files: uses configmaps, secrets, hostPath, or cluster trust bundle (not enabled by default)                                    |
|   9 | Issues with existing approaches:                                                                                                               |
|  10 | Trust store locations differ across Linux distributions                                                                                        |
|  11 | CA bundle update commands differ                                                                                                               |
|  12 | Some languages (e.g., Java, Python, Node.js) require special handling                                                                          |
|  13 | Need for OS- and language-aware automatic CA trust injection                                                                                   |
|  14 | NRI is a plugin API for high-level container runtimes, intercepts container lifecycle events, mutates configs, works with containerd and CRI-O |
|  15 | Implemented NRI plugin for automatic CA trust injection:                                                                                       |
|  16 | Detects OS and runtime in container                                                                                                            |
|  17 | Appends CA certificates to correct files                                                                                                       |
|  18 | Modifies environment variables for NodeJS/Python if needed                                                                                     |
|  19 | Enabled via single pod annotation                                                                                                              |
|  20 | Demo: NRI plugin enables client to trust server certificate with minimal changes                                                               |
|  21 | Implementation steps:                                                                                                                          |
|  22 | NRI program subscribes to create container events, adds OCI hook and entrypoint modifier                                                       |
|  23 | OCI hook detects environment, injects CA certificates                                                                                          |
|  24 | Entrypoint modifier sets environment variables, then runs original entrypoint                                                                  |
|  25 | Advantages: no need to manage Dockerfiles, simple pod templates, short startup delay, OS/language-aware injection                              |
|  26 | Limitation: requires node-level privileges; plan to add sandboxing                                                                             |
|  27 | Issues/future work: environment variables not set for kubectl exec, not available for read-                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6qvsce4t2_w)
