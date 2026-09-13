---
type: Video Note
title: "Lightning Talk: Avoiding CPU Throttling: How Go 1.25's Container-Aware Runtime Fix... Adarsh K Kumar"
description: "Adash, a principal engineer at Rapido, discusses a throttling issue in Go-based applications running in containers, particularly when the GOMAXPROCS setting is not properly configured. He explains how containers use Linux constructs like na..."
resource: https://www.youtube.com/watch?v=BrjeW5ARaZY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Adash, a principal engineer at Rapido, discusses a throttling issue in Go-based applications running in containers, particularly when the GOMAXPROCS setting is not properly configured.
He explains how containers use Linux constructs like namespaces and cgroups to isolate processes and control resources, and highlights that Go, until version 1.25, was not container-aware, leading to problems when the runtime set GOMAXPROCS based on the host's available CPUs rather than the container's limits.
This mismatch could cause applications to be throttled due to exceeding CPU limits enforced by cgroups, resulting in increased response times.
Go 1.25 addresses this by setting GOMAXPROCS according to the container's CPU bandwidth, but users should be cautious with fractional CPU limits, as rounding up can still cause throttling.
For those unable to upgrade to Go 1.25, Adash recommends using Uber's automaxprocs library to achieve similar behavior.
# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speaker: Adash, Principal Engineer at Rapido                                                                                                                 |
|   2 | Topic: Throttling issue in Go-based applications when GOMAXPROCS is not set                                                                                  |
|   3 | Announcement: KCD event in Kochi, India on April 18th                                                                                                        |
|   4 | Containers isolate processes using Linux constructs: namespaces, cgroups, chroot                                                                             |
|   5 | Docker and Kubernetes are built on Go; many cloud-native apps use Go                                                                                         |
|   6 | Go (before version 1.25) was not container-aware                                                                                                             |
|   7 | Go's basic concurrency unit: goroutine (lightweight, 2KB stack, multiplexed onto OS threads)                                                                 |
|   8 | Go runtime handles memory management and scheduling, compiled into binary                                                                                    |
|   9 | CPU resource requests help schedule pods; CPU limits control max resources used                                                                              |
|  10 | Cgroups restrict CPU time; exceeding memory triggers OOM kill, exceeding CPU causes throttling                                                               |
|  11 | Default cgroup accounting window: 100ms (CF period)                                                                                                          |
|  12 | Example: API takes 200ms to execute, container has 400 millicore limit, gets 40ms CPU per 100ms period, actual execution takes up to 500ms due to throttling |
|  13 | Go routines are multiplexed onto OS threads; number of scheduler threads is set by GOMAXPROCS                                                                |
|  14 | Before Go 1.25, GOMAXPROCS was set to the number of logical CPUs on the node (e.g., 24 vCPUs on host, container limited to 2, GOMAXPROCS set to 24)          |
|  15 | Result: Application gets throttled due to mismatch between visible CPUs and container limits                                                                 |
|  16 | Go 1.25 fix: GOMAXPROCS is set based on cgroup CPU bandwidth limit                                                                                           |
|  17 | If CPU limits are fractional, Go 1.25 rounds up, which can still cause throttling                                                                            |
|  18 | Kubernetes now supports in-place pod resize; Go 1.25 periodically updates GOMAXPROCS based on cgroup bandwidth                                               |
|  19 | All automatic GOMAXPROCS adjustments are disabled if GOMAXPROCS is manually set                                                                              |
|  20 | Alternative for older Go versions: Use Uber's automaxprocs library for similar effect                                                                        |
|  21 | End of talk                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BrjeW5ARaZY)