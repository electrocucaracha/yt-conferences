---
layout: default
title:
  The Life (or Death) of a Kubernetes API Request, 2025 Edition - Abu Kashem
  & Stefan Schimanski
nav_order: 337
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=Hc0jj-654lA
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

Here is a summary of the video transcript in 3-5 sentences: The API server handles incoming requests by executing a chain of handler functions, each responsible for specific aspects of request processing.
The request is first validated and authorized, then converted to an internal object using a converter registered in the scheme, which maps to different versions of the job resource (e.g., v1, internal).
After validation and authorization, the request is stored in the etcd key-value store, encrypted, and then retrieved by the API server for response.
The API server returns a successful response to the client, and if necessary, retries the request based on the retry-after header.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Hc0jj-654lA)
