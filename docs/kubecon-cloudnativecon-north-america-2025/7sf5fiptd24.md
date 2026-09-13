---
type: Video Note
title: "Performance Tuning Java Apps for Kubernetes: From Startup Time To Conta... Ryan Jarvinen & Daniel Oh"
description: "In this presentation, Daniel from Red Hat IBM and Ryan Jarvin discuss performance tuning for Java applications on Kubernetes, addressing common challenges such as slow startup times, high memory usage, and scaling issues compared to lighter..."
resource: https://www.youtube.com/watch?v=7sF5fiPtd24
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Daniel from Red Hat IBM and Ryan Jarvin discuss performance tuning for Java applications on Kubernetes, addressing common challenges such as slow startup times, high memory usage, and scaling issues compared to lighter languages like Go or Python.
They introduce several open-source tools and frameworks—including JIB, GraalVM, CDS, CRaC, and Quarkus—that help optimize Java applications for containerized environments by reducing startup time, memory footprint, and container size.
Through a live demo, they show how Quarkus integrates these technologies to enable fast, efficient Java applications that can scale rapidly on Kubernetes, highlighting features like native compilation and streamlined container image creation.
The speakers emphasize the importance of choosing the right Java framework and tuning JVM and Kubernetes configurations, such as garbage collection and startup probes, to achieve optimal performance.
They conclude that Java remains a viable and competitive choice for cloud-native workloads when leveraging modern tools and best practices.
# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on Java performance tuning on Kubernetes with practical tips.                                                              |
|   2 | Java has historically had slow startup times and high resource usage, especially with monolithic applications.                                  |
|   3 | Shift from monolithic to microservices (e.g., Spring Boot, Micronaut) has exposed Java’s startup and resource challenges in cloud environments. |
|   4 | Java applications in containers can have slow startup, leading to Kubernetes killing pods due to readiness probe failures.                      |
|   5 | Java containers are often larger and consume more resources compared to lighter languages like JavaScript, Go, or Python.                       |
|   6 | Despite challenges, Java remains widely used with over 12 million developers.                                                                   |
|   7 | Kubernetes expects fast startup times; traditional JVM apps may not meet these, causing scaling and reliability issues.                         |
|   8 | Newer JVMs and frameworks can improve startup time, reduce memory footprint, and create leaner containers.                                      |
|   9 | Tools and projects discussed:                                                                                                                   |
|  10 | JIB: Builds small, lean Java containers without Dockerfile.                                                                                     |
|  11 | GraalVM: Compiles Java to native executables, eliminating JVM dependency and improving startup/memory.                                          |
|  12 | CDS (Class Data Sharing): Preloads class metadata for faster JVM startup.                                                                       |
|  13 | CRaC (Coordinated Restore at Checkpoint): Snapshots JVM state for near-instant startup, useful for serverless.                                  |
|  14 | Quarkus: Kubernetes-native Java framework, optimized for fast startup and low memory, integrates with GraalVM and other tools.                  |
|  15 | Quarkus offers out-of-the-box features, build-time optimizations, and supports many extensions for cloud-native workloads.                      |
|  16 | Demo showed Quarkus app with fast startup and low memory usage, both on JVM and as a native executable.                                         |
|  17 | Native executables start up ~10x faster and use significantly less memory than JVM.                                                             |
|  18 | Quarkus simplifies containerization and deployment to Kubernetes, supporting rapid scaling.                                                     |
|  19 | Recommendations:                                                                                                                                |
|  20 | Reduce base image size (e.g., with JIB).                                                                                                        |
|  21 | Tune JVM (garbage collector, class data sharing).                                                                                               |
|  22 | Use Kubernetes startup probes for sl                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7sF5fiPtd24)