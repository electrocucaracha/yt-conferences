---
type: Video Note
title: "Lightning Talk: The $100K GPU Mystery: Why Your AI Training Dies at 99% - Michael Ifeanyi, Google"
description: "In this presentation, Mike Elifi, a technical solutions engineer at Google, explains why AI training jobs can crash at 99% completion despite GPU monitoring tools like Nvidia SMI showing available memory. The root cause is memory fragmentat..."
resource: https://www.youtube.com/watch?v=lp6LiupKtnU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Mike Elifi, a technical solutions engineer at Google, explains why AI training jobs can crash at 99% completion despite GPU monitoring tools like Nvidia SMI showing available memory.
The root cause is memory fragmentation: while Nvidia SMI reports total free memory, it does not account for whether that memory is contiguous, which is necessary for large tensor allocations in frameworks like PyTorch.
Using a parking lot analogy, Mike illustrates that fragmented memory blocks, though collectively sufficient in size, cannot be used for a single large allocation, leading to out-of-memory errors.
He recommends monitoring fragmentation using the torch.cuda memory stats API, reducing memory pressure through smaller batch sizes, gradient checkpointing, or mixed precision, and deploying observability tools or draining nodes with proper checkpointing to manage fragmentation.
The key takeaways are to recognize Nvidia SMI’s limitations, understand how fragmentation accumulates during training, and consistently monitor for fragmentation to prevent job failures.
# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | AI training jobs can crash at 99% even when GPU monitoring shows available memory.                                             |
|   2 | Nvidia System Management Interface (SMI) reports total free GPU memory, not contiguous free memory.                            |
|   3 | CUDA out of memory errors can occur when a large tensor allocation is rejected despite reported free memory.                   |
|   4 | Contiguous memory is required for large tensor allocations; fragmented memory cannot be used for such allocations.             |
|   5 | GPU memory fragmentation is similar to a parking lot with scattered empty spots that cannot fit a large vehicle.               |
|   6 | Fragmentation results in unusable free memory, causing job crashes.                                                            |
|   7 | PyTorch can detect peak fragmentation during training, even when Nvidia SMI shows available memory.                            |
|   8 | Fragmentation accumulates during training, reducing usable contiguous memory.                                                  |
|   9 | To prevent issues:                                                                                                             |
|  10 | Monitor the right metrics, such as fragmentation using torch.cuda memory stats API.                                            |
|  11 | Reduce memory pressure by using smaller batch sizes, enabling gradient checkpointing, or using mixed precision (FP16 or BF16). |
|  12 | Deploy a daemon set to extract fragmentation metrics and export to observability tools like Prometheus.                        |
|  13 | Drain nodes when necessary, and implement checkpointing to resume jobs after node restarts.                                    |
|  14 | Key takeaways:                                                                                                                 |
|  15 | Nvidia SMI does not show contiguous free memory, leading to a blind spot.                                                      |
|  16 | Fragmentation accumulates during training and can prevent allocations despite apparent free memory.                            |
|  17 | Always monitor for fragmentation to avoid unexpected job crashes.                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lp6LiupKtnU)