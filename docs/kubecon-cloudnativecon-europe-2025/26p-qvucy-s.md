---
layout: default
title: Identity-based Trust - Till Death Do We Part? - John Kjell & Kairo De Araujo
nav_order: 129
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker discusses identity-based trust and its implementation in
  various projects, including Ento, Tough, and Sig Store. They explain how signing
  artifacts with private keys and sharing public keys allows for verification of signatures...
resource: https://www.youtube.com/watch?v=26p_qvuCy-s
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

The speaker discusses identity-based trust and its implementation in various projects, including Ento, Tough, and Sig Store.
They explain how signing artifacts with private keys and sharing public keys allows for verification of signatures, but also highlights issues such as compromised private keys or leaked information.
To address these concerns, the speaker introduces OIDC (OpenID Connect) identity signature, which generates temporary private keys for signing artifacts.
The Sig Store project provides a secure way to store and manage these signatures, allowing for efficient verification and rotation of keys.
The speaker also discusses the importance of policies and attestations in ensuring software safety and security, highlighting the Witness policy's ability to detect issues like modified linting steps.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=26p_qvuCy-s)
