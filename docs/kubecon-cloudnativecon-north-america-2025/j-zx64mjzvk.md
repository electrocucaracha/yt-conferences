---
type: Video Note
title: "Fix First, Investigate Later: When an eBPF Rollout Brought Down Our... Zain Malik & Grzegorz Głąb"
description: "The team investigated a network outage caused by an EBPF rollout, which affected 50% of their nodes and resulted in significant performance degradation. They discovered that the issue was due to the packet parser plugin in the retina toolin..."
resource: https://www.youtube.com/watch?v=J-Zx64mJzVk
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The team investigated a network outage caused by an EBPF rollout, which affected 50% of their nodes and resulted in significant performance degradation.
They discovered that the issue was due to the packet parser plugin in the retina tooling, which was causing high CPU usage and context switching on multi-core machines.
To resolve the issue, they implemented ring buffers in the kernel, which significantly improved performance.
The team also found that the problem was not unique to their environment, as other BPF toolings were still using perf rings, but Celium had moved to ring buffers.
They concluded that observability is essential for identifying performance issues and that choosing between perf rings and ring buffers depends on workload requirements.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=J-Zx64mJzVk)