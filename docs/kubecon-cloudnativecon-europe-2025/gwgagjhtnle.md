---
layout: default
title:
  "How We Solved TLS at Scale: Self-Service, Multi-Tenant Cert-manager - Erik
  Godding Boye & Tim Ramlot"
nav_order: 125
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The presentation discusses how Eric set up Search Manager, a CNCF graduated
  project, to create certificates for a multi-tenant environment in a Kubernetes cluster.
  Initially, Eric used Spiffy and Spir, but faced challenges running it on Ope...
resource: https://www.youtube.com/watch?v=gWgagjHtnlE
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The presentation discusses how Eric set up Search Manager, a CNCF graduated project, to create certificates for a multi-tenant environment in a Kubernetes cluster.
Initially, Eric used Spiffy and Spir, but faced challenges running it on OpenShift clusters.
He then turned to Search Manager, which he customized to meet his needs.
To ensure security and control, Eric implemented policies using the "approve-a-policy" plugin, allowing tenants to self-provision certificates while preventing unauthorized requests.
Additionally, he used a custom monitoring solution to track certificate expirations and implement a rolling update mechanism using Reloader to minimize downtime during changes.

# Main Points

|   # | Main point                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------- |
|   1 | Eric set up Search Manager for a client using Manager, creating a multi-tenant environment with self-service certificates. |
|   2 | The setup uses private PI (Private Key Infrastructure) with a shared common root CA.                                       |
|   3 | A cluster issuer was created to control access to the Search Manager issuer.                                               |
|   4 | An application operator was used to provide a simplified way for users to schedule workloads.                              |
|   5 | Trust Manager is another project that allows configuring a set of sources containing trusted certificates.                 |
|   6 | Approval Policy is a plug-in for Search Manager that configures policies for certificate requests.                         |
|   7 | Policies can be configured to approve or deny certificate requests based on conditions such as URI prefixes.               |
|   8 | Monitoring and alerting are crucial for automation failures and policy non-adherence.                                      |
|   9 | Reloader is used to watch config maps and secrets, triggering rolling updates when changes occur.                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gWgagjHtnlE)
