---
layout: default
title: "Less Waste, Less Work:  Using VM Lifetime for Resource Cleanup"
nav_order: 81
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Nisha and Kuruha from LINE Corporation presented a solution to the problem of unused virtual machines (VMs) in their large-scale OpenStack-based private cloud, where approximately 5% of instances w..."
resource: "https://www.youtube.com/watch?v=V0LWdO1c0hA"
youtube_stats:
  view_count: 83
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

Nisha and Kuruha from LINE Corporation presented a solution to the problem of unused virtual machines (VMs) in their large-scale OpenStack-based private cloud, where approximately 5% of instances were left idle, leading to increased costs, operational overhead, and security risks.
They introduced a "VM lifetime" feature that allows users to specify a grace period for resource usage, after which the VM is automatically shut down and deleted if no action is taken, thereby eliminating the need for manual cleanup.
The implementation utilizes a design where Nova compute acts as a trigger by periodically checking instance metadata, while an external event handler executes actions such as sending alerts, shutting down, or deleting instances based on defined metadata keys like `lifetime` and `lifetime_action`.
This approach ensures full traceability through Nova’s audit logs and includes resilience mechanisms to handle action failures, with metadata validation in the Nova API enforcing the lifetime requirement while allowing specific exceptions for critical services.
The feature has been successfully deployed in their development environment, reclaiming thousands of CPU cores and terabytes of storage, reducing the carbon footprint, and automating resource cleanup, although challenges remain regarding instances associated with load balancers and those stuck in error states.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | LINE Corporation merged with Yahoo Japan to create a large-scale OpenStack-based private cloud named Flower.                          |
|   2 | The team identified that nearly 5% of VMs, totaling 15,000 instances, were left unused due to human error and automation blind spots. |
|   3 | Unused resources caused significant financial loss, increased operational overhead, and created security vulnerabilities.             |
|   4 | Previous manual solutions, such as usage surveys and dashboard tags, proved inefficient and failed to reduce waste.                   |
|   5 | The proposed solution is a VM lifetime feature that automatically deletes resources after a user-specified grace period.              |
|   6 | The system targets test and development environments, using a multi-step process of alerts, shutdown, and final deletion.             |
|   7 | Design B was selected, placing the trigger inside Nova compute and the action runner outside to balance maintenance and logging.      |
|   8 | Nova compute runs a periodic task every hour to check instance metadata and update the lifetime action status.                        |
|   9 | Three metadata keys are defined: lifetime for the expiration date, lifetime_action for the current step, and execution timestamps.    |
|  10 | The event handler receives instance update notifications from Nova to execute actions like sending emails or deleting instances.      |
|  11 | Metadata validation in the Nova API enforces lifetime requirements, limiting values to one year and preventing deletion of the key.   |
|  12 | Exceptions are provided for specific platforms, system projects, or tagged instances that require different lifecycle management.     |
|  13 | The feature is operational in the Flower development environment, managing over 60% of instances across the infrastructure.           |
|  14 | The system has reclaimed 4,800 cores, 10,000 GB of RAM, and 72 TB of disk space over the past year.                                   |
|  15 | Approximately 1,000 instances were automatically deleted, while others were removed by users after receiving notifications.           |
|  16 | Deletion failures occurred for instances associated with load balancers due to existing cloud validation rules.                       |
|  17 | Some instances entered an error state, preventing the periodic task from processing their deletion.                                   |
|  18 | The team plans to coordinate with the load balancer team to resolve deletion conflicts and improve monitoring for error states.       |
|  19 | The VM lifetime feature reduces manual cleanup efforts for users and improves resource efficiency for operators.                      |
|  20 | Automated resource cleanup contributes to sustainability by lowering the carbon footprint of the infrastructure.                      |
|  21 | The implementation demonstrates that automation can effectively manage resource lifecycle without constant human intervention.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/V0LWdO1c0hA/hqdefault.jpg)](https://www.youtube.com/watch?v=V0LWdO1c0hA)

[Watch on YouTube](https://www.youtube.com/watch?v=V0LWdO1c0hA)
