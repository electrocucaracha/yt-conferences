---
type: Video Note
title: "Scalable DNS With CoreDNS Plugins: A Deep Dive - Yong Tang, Ivanti & John Belamaric, Google"
description: "The Cord DNS project is a general-purpose DNS server that offers flexibility and ease of integration with other backends. It's primarily an authoritative DNS server but can also handle recursive requests. The project is written in Go, a mem..."
resource: https://www.youtube.com/watch?v=W3f5Ks0j2Q8
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The Cord DNS project is a general-purpose DNS server that offers flexibility and ease of integration with other backends.
It's primarily an authoritative DNS server but can also handle recursive requests.
The project is written in Go, a memory-safe language, and has gained popularity due to its simplicity and scalability.
A recent addition is the "multisocket" feature, which allows for better scaling by utilizing multiple sockets on each CPU core, resulting in linear QPS growth up to 5 CPUs.
This feature can help address the scaling limitations of Cord DNS, particularly when dealing with large numbers of services or external domains.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=W3f5Ks0j2Q8)