---
layout: default
title:
  "Get WITty: Evolving Kubernetes Scheduling With the WebAssembly... Dejan Pejchev
  & Jonathan Giannuzzi"
nav_order: 109
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speakers, Dan Pchev and Jonathan, discuss their journey of applying
  the component model to the Kubernetes scheduler using WebAssembly (WASM). They initially
  encountered challenges with defining their own width and generating bindings fo...
resource: https://www.youtube.com/watch?v=hjbZOBghxYU
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

The speakers, Dan Pchev and Jonathan, discuss their journey of applying the component model to the Kubernetes scheduler using WebAssembly (WASM).
They initially encountered challenges with defining their own width and generating bindings for various programming languages.
However, they discovered Xism, an alternative that supports multiple hosts and guest languages, including Go and Rust.
The team implemented a Go host using Xism with JSON serialization, achieving better performance compared to manual implementation.
They also explored other alternatives, such as XTP binden and Gravity, but found them less suitable due to limitations in protogeneration and support for complex types.
The speakers conclude that the component model is an amazing idea, but its tooling lacks certain aspects, prompting a call to action for contributors to join working groups and contribute to improving the tooling and runtime support.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hjbZOBghxYU)
