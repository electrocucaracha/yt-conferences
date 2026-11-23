---
layout: default
title: "Well-Isolated Access Control in a Massive Multi Tenant OpenStack Environment"
nav_order: 95
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "LINE Corporation presented a solution for implementing well-isolated access control in a massive multi-tenant OpenStack environment following its merger with Yahoo Japan."
resource: "https://www.youtube.com/watch?v=Bd8y2bnlV84"
youtube_stats:
  view_count: 67
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

LINE Corporation presented a solution for implementing well-isolated access control in a massive multi-tenant OpenStack environment following its merger with Yahoo Japan.
To address the security risks of excessive permissions and the operational challenges of managing roles across hundreds of clusters, the company designed a new private cloud named "Flower" that utilizes a single OpenStack cluster integrated with a centralized authority platform, Asense.
The core of their strategy involves role isolation, specifically introducing "semi-admin" roles for service providers that grant necessary cross-project API access without the dangerous, unrestricted privileges of the standard admin role.
They further demonstrated the flexibility of the Keystone policy framework by using service tokens to allow end users to create snapshots while preventing them from uploading custom images, and they optimized API performance by strategically ordering policy rules to reduce response times.
Finally, the team detailed the integration of Asense with Keystone using federation APIs to synchronize identity and role data, enabling a unified, secure, and centrally managed access control system for their large-scale infrastructure.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | LINE Corporation merged with Yahoo Japan Corporation to create a new private cloud named Flower using a massive single OpenStack cluster.                       |
|   2 | Legacy systems like Veruda used a single OpenStack cluster with shared roles, leading to excessive permissions and dangerous admin misoperations.               |
|   3 | Yahoo Japan's legacy system used isolated role management across over 200 clusters, causing policy inconsistency and management difficulties.                   |
|   4 | The new design aims for a single OpenStack cluster with centralized authority management integrated with an external identity platform.                         |
|   5 | Role-based access control (RBAC) in OpenStack uses Keystone for token issuance and policy files to validate user, project, and role permissions.                |
|   6 | Standard OpenStack roles are insufficient for service providers because the admin role is too powerful and the member role is too weak.                         |
|   7 | A new semi-admin role was created for service providers to allow cross-project resource access and specific API usage without full admin privileges.            |
|   8 | The semi-admin role is defined in policy files to restrict access to only the central APIs required for specific provider services.                             |
|   9 | Implementing cross-project access for semi-admin roles required specific policy configurations in Neutron and other services to bypass project ID constraints.  |
|  10 | Complex requirements, such as allowing users to create snapshots but not upload custom images, were resolved using the Echo service token mechanism.            |
|  11 | Nova sends an Echo service token to Glance during snapshot creation, allowing Glance to validate the service user ID instead of the end user.                   |
|  12 | Policy evaluation order significantly impacts API performance; placing broader access rules earlier in the policy file improved network request response times. |
|  13 | The system integrates with Asense, an open-source identity platform, to serve as the single source of truth for access control information.                     |
|  14 | Identity mapping is achieved by configuring Asense as an identity provider in Keystone using the SAML federation protocol.                                      |
|  15 | A synchronization component maps roles from Asense to Keystone to maintain a consistent cloud authority system.                                                 |
|  16 | The authentication flow converts Asense tokens into unscoped Keystone tokens, which are then scoped to projects for API access.                                 |
|  17 | Cloud users no longer need to manage passwords directly within OpenStack, relying instead on the centralized Asense authentication.                             |
|  18 | The implementation successfully secured the OpenStack environment while leveraging the flexibility of the policy framework for complex real-world requirements. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Bd8y2bnlV84/hqdefault.jpg)](https://www.youtube.com/watch?v=Bd8y2bnlV84)

[Watch on YouTube](https://www.youtube.com/watch?v=Bd8y2bnlV84)
