---
layout: default
title:
  "Cloud Native Theater | EnvoyCon: From ingress-nginx to Envoy Gateway at Zapier:
  The... Kalen Wessel"
nav_order: 58
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Kayn Wessle, a senior site reliability engineer at Zapier, discusses
  the company's migration from Ingress NGINX to Envoy Gateway, prompted by NGINX's
  end-of-life announcement, accumulated technical debt, and the desire for a more
  unified an...
resource: https://www.youtube.com/watch?v=kIj2U13VZJY
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

Kayn Wessle, a senior site reliability engineer at Zapier, discusses the company's migration from Ingress NGINX to Envoy Gateway, prompted by NGINX's end-of-life announcement, accumulated technical debt, and the desire for a more unified and robust ingress solution.
The team chose Envoy Gateway for its strong Kubernetes API alignment, extensibility, active community, and comprehensive features without enterprise licensing barriers.
The migration process involved thorough auditing, baseline establishment, incremental rollouts using weighted DNS, and careful monitoring to ensure stability, with several unexpected challenges such as buffer limits, reconciliation loops, latency changes, and differing default behaviors between NGINX and Envoy.
Solutions included adjusting buffer sizes, refining connection settings, and explicitly configuring policies to match previous behaviors.
Post-migration, Zapier achieved a unified edge view, improved operational consistency, and enhanced developer experience, migrating 500 production ingresses in under six months with minimal incidents.

# Main Points

|   # | Main point                                                                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Zapier migrated from Ingress NGINX to Envoy Gateway due to NGINX end-of-life, frozen Ingress API, and growing Gateway API adoption.                                                                                                         |
|   2 | Years of tech debt led to inconsistent environments, annotation drift, and occasional outages.                                                                                                                                              |
|   3 | Migration was seen as an opportunity to rebuild the ingress layer around Kubernetes API Gateway.                                                                                                                                            |
|   4 | Benefits of Gateway API: clear separation of responsibilities, strongly typed CRDs, early CI linting, richer traffic primitives (traffic splitting, header-based canary matching), and reduced reliance on controller-specific annotations. |
|   5 | Envoy Gateway chosen for strong Kubernetes API alignment, extensibility, active community, consistent releases, and no enterprise license lock-in.                                                                                          |
|   6 | Pre-migration steps: inventory of ingress resources, rollout of Kyverno policy to flag new ingresses, establish latency baselines, full ingress audit, mapping annotations to Envoy equivalents, and creation of tracking sheets.           |
|   7 | High-traffic services migrated first for faster detection of issues and to inform design decisions.                                                                                                                                         |
|   8 | Migration was incremental, observable, and reversible; used weighted DNS for gradual traffic shifts.                                                                                                                                        |
|   9 | Compared Envoy metrics to NGINX baselines at each migration step; DNS weights adjusted as needed.                                                                                                                                           |
|  10 | Unexpected issues included:                                                                                                                                                                                                                 |
|  11 | 503 errors due to Envoy buffer limits on large webhook payloads; fixed by increasing buffer limit in client traffic policy.                                                                                                                 |
|  12 | Excessive reconciliation events caused by Vault operator updating TLS secrets; fixed by dropping unused CA secret distribution.                                                                                                             |
|  13 | Elevated HTTP latency due to Envoy’s connection pooling; fixed by forcing one request per connection in backend traffic policy.                                                                                                             |
|  14 | Path normalization differences (Envoy unescapes encoded slashes); fixed by setting escape/action to keep unchanged.                                                                                                                         |
|  15 | Header handling differences (Envoy Gateway rejects headers with underscores); fixed by updating client traffic policy to drop such headers.                                                                                                 |
|  16 | Retry behavior differences; added explicit retry block to ma                                                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kIj2U13VZJY)
