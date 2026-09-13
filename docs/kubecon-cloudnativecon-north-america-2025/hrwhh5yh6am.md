---
layout: default
title:
  Package Management for Your Clust... Jordan Keister, Rashmi Gottipati, Joe
  Lanford & Attila Mészáros
nav_order: 194
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The Operator Life Cycle Manager (OLM) is a project under the Cloud Native
  Computing Foundation (CNCF) aimed at providing automated life cycle management for
  operators on a cluster. OLM v1 has addressed several pain points, including isolate...
resource: https://www.youtube.com/watch?v=HrwHh5Yh6AM
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

The Operator lifecycle Manager (OLM) is a project under the Cloud Native Computing Foundation (CNCF) aimed at providing automated lifecycle management for operators on a cluster.
OLM v1 has addressed several pain points, including isolated deterministic installs and upgrades, automatic bundle scope permissions, and complete cleanup during uninstallation.
The new revision-based lifecycle management introduces a cluster extension revision API, allowing for predictable rollbacks and rollouts.
OLM also supports registry v1 bundles with web hooks, single-namespace and own-namespace install modes, and has improved compatibility with existing operators and catalogs.
However, limitations include eventual consistency in caches and the need for optimistic locking to ensure resource version comparability.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Operator lifecycle Manager (OLM) is a project aimed at providing automated lifecycle management for operators on a cluster.                                               |
|   2 | OLM has over 380 operators in its catalog and has seen 41,000 downloads on GitHub since its 1.0 release last December.                                                    |
|   3 | Pain points identified by customers include:                                                                                                                              |
|   4 | Upgrades: changes occur in one namespace but not another.                                                                                                                 |
|   5 | Automatic back-up aggregation: what's applied isn't always what you get.                                                                                                  |
|   6 | Explicit bundle scope permissions: every time.                                                                                                                            |
|   7 | Uninstallation: things left behind, unclear what to remove.                                                                                                               |
|   8 | Lack of version pinning: only for initial install.                                                                                                                        |
|   9 | Opaque non-Cubernetes resources: install plan, etc.                                                                                                                       |
|  10 | OLM v1 has improved compatibility with existing operators and catalogs, including support for registry v1 bundles with web hooks and single-namespace installs.           |
|  11 | The cluster extension revision API allows tracking installs, upgrades, and manifest changes, making rollbacks and rollouts predictable and deterministic.                 |
|  12 | Web hook support has been added to OMv1, allowing operators to include validating, mutating, and conversion web hooks in their bundles.                                   |
|  13 | OLM v1 no longer tries to manage certificates itself, relying on third-party certificate management instead.                                                              |
|  14 | Single-namespace installs are now supported, but only for registry v1 bundles.                                                                                            |
|  15 | The revision-based lifecycle management has improved the experience by providing a new unit of lifecycle and making rollbacks and rollouts predictable and deterministic. |
|  16 | Limitations of OLM v1 include:                                                                                                                                            |
|  17 | Uninstalling cluster extensions deletes everything, including dependent resources.                                                                                        |
|  18 | No operator conditions API in OMv1.                                                                                                                                       |
|  19 | Eventual consistency with caches and informers.                                                                                                                           |
|  20 | Java Operator SDK has improved resource version handling to address eventual consistency issues.                                                                          |
|  21 | Kubernetes will have comparable resource versions in the next version, making it easier to use optimistic locking.                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HrwHh5Yh6AM)
