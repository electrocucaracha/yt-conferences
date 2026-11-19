---
layout: default
title: "Tests Are What You Want, What You Really Really Want - Daniel Hiller & Ryan Hallisey"
nav_order: 9
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "This community session from the KubeVirt project focuses on improving testing practices, specifically addressing the challenges of flaky tests and the need for efficient, deterministic outcomes."
resource: "https://www.youtube.com/watch?v=TLkbHD70lb4"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

This community session from the KubeVirt project focuses on improving testing practices, specifically addressing the challenges of flaky tests and the need for efficient, deterministic outcomes.
The presenters discuss the limitations of simply re-running failed tests and introduce a machine learning-based approach to classify tests as flaky or stable, aiming to reduce wasted CI resources and improve developer experience.
The discussion covers various testing tools, including Ginkgo, Gomega, Prow, and the Go standard library, with participants sharing opinions on the idiomatic preferences for using native Go testing features over external assertion libraries.
Additionally, the session highlights the importance of scale and performance testing for Custom Resource Definitions (CRDs), demonstrating how KubeVirt measures API server load and memory usage over time to ensure responsible resource consumption.
Finally, the presenters explore simulation tools like Quark and kube-mare, which allow for large-scale testing of control planes and daemons without the cost of provisioning real hardware, enabling the simulation of tens of thousands of pods to identify bottlenecks and ensure system resilience.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session aims to facilitate a lively community discussion on testing strategies, sharing ideas, and addressing pain points rather than delivering a static presentation.                    |
|   2 | Core goals for tests include testing specific functionality, having finite runtime, being cost-efficient, developer-friendly, and producing deterministic outcomes.                            |
|   3 | A common pain point identified is the excessive use of the "retest" button to handle flaky tests, which wastes CI resources and creates uncertainty for developers.                            |
|   4 | The Kubert project uses Ginkgo, Gomega, and a self-hosted Prow instance for its CI/CD testing infrastructure.                                                                                  |
|   5 | Community feedback suggests a preference for the Go standard library over assertion libraries like Ginkgo or Testify, citing better alignment with Go idioms and clearer parallelism handling. |
|   6 | Testify is noted to have separate packages for assertions that continue on failure versus those that stop execution, which differs from standard Go testing behavior.                          |
|   7 | To address flaky tests, the team is exploring a machine learning approach based on a paper by Greg Kafaba that uses static and runtime analysis to predict test flakiness.                     |
|   8 | This approach aims to detect flaky tests before they merge into the codebase and to provide advice to test engineers on improving test complexity and structure.                               |
|   9 | The team developed a simple reporting tool that scans Prow data to create heat maps of test failures per day and per lane, helping identify the most problematic tests.                        |
|  10 | Infrastructure resilience is critical, as external factors like image repository outages can cause test failures regardless of code quality.                                                   |
|  11 | Scale and performance testing for Custom Resource Definitions (CRDs) is essential to prevent cluster outages and understand API server load.                                                   |
|  12 | Kubert measures the number of REST calls, such as patch requests, made by its control plane to the API server to track performance over time.                                                  |
|  13 | Data visualization tools plot these metrics against Kubernetes releases to identify changes in API load, such as an increase from 200 to 400 patch requests per 100 VMIs.                      |
|  14 | The goal is to publish performance metrics, including memory usage and API call counts, with every Kubert release to inform the community of expected resource consumption.                    |
|  15 | Simulation tools like Quark allow for large-scale testing by creating virtual nodes that make API calls without consuming real compute resources.                                              |
|  16 | Kubemark is used to simulate the runtime components, such as daemons managing virtual machine resources, which cannot be tested in Quark environments.                                         |
|  17 | These simulation techniques enable testing at scales of tens of thousands of objects to stress the API server and control plane effectively.                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TLkbHD70lb4/hqdefault.jpg)](https://www.youtube.com/watch?v=TLkbHD70lb4)

[Watch on YouTube](https://www.youtube.com/watch?v=TLkbHD70lb4)
