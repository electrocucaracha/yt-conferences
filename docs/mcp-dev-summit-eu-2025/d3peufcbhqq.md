---
type: Video Note
title: "[Session] One Test a Day Keeps the Issues Away with Oleksandr Kotov - Grafana Labs"
description: "Alexander introduces the importance of testing MCP servers, emphasizing that testing provides confidence, mitigates risks, and improves user satisfaction by ensuring software reliability and security. He explains the distinction between fun..."
resource: https://www.youtube.com/watch?v=D3pEufcBHQQ
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Alexander introduces the importance of testing MCP servers, emphasizing that testing provides confidence, mitigates risks, and improves user satisfaction by ensuring software reliability and security.
He explains the distinction between functional and non-functional testing, focusing on performance testing as a key aspect for MCP servers, which can suffer from issues like broken tools, privilege escalation, data leaks, scalability problems, and low performance.
Alexander demonstrates how to use the open-source tool K6 for performance testing, including writing basic and extended tests, utilizing custom extensions for MCP protocols, and visualizing results with Grafana dashboards.
He discusses setting thresholds for automated CI testing, simulating various load patterns such as constant, ramping, spike, and soak tests to identify bottlenecks and potential failures.
Finally, he highlights the ability to use K6 for both performance and functional testing, encourages integrating these tests into CI pipelines, and stresses the importance of acting on test results to derive real value.
# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction to testing MCP servers, including general testing concepts and performance testing                             |
|   2 | Testing provides developer confidence, ensures software reliability, security, and boosts user satisfaction                 |
|   3 | Testing mitigates risks such as user trust, security, and revenue loss                                                      |
|   4 | Two main testing types: functional (e.g., unit, integration, system, smoke tests) and non-functional (e.g., performance)    |
|   5 | Common MCP server issues: broken tools, privilege escalation, data leaks, scalability problems, low performance             |
|   6 | Users expect quick responses from MCP servers; slow responses can lead to user abandonment                                  |
|   7 | MCP servers can be tested by simulating synthetic load with synthetic MCP clients before production                         |
|   8 | K6 (Ksix) is an open-source performance testing tool that generates synthetic load and metrics                              |
|   9 | Basic K6 test uses JavaScript to define virtual users and test parameters                                                   |
|  10 | K6 summary includes metrics like request duration, request count, and network bandwidth                                     |
|  11 | K6 can be extended with custom extensions, such as one for MCP protocol testing                                             |
|  12 | MCP extension for K6 allows defining MCP clients over different transports (e.g., HTTP, stdio)                              |
|  13 | Performance metrics specific to MCP (e.g., MCP request duration, MCP request count) can be visualized in Grafana dashboards |
|  14 | Tests can be automated in CI pipelines with thresholds for specific metrics (e.g., 99th percentile request duration)        |
|  15 | K6 supports various load patterns: constant, ramping, spike, and soak testing                                               |
|  16 | Spike testing simulates sudden load increases; soak testing helps detect memory leaks and long-term issues                  |
|  17 | K6 allows filtering and analyzing metrics for each scenario separately                                                      |
|  18 | Functional testing can also be done with K6 using assertions in test scripts                                                |
|  19 | Tests can be configured to run continuously in CI; acting on test results is crucial for improvement                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=D3pEufcBHQQ)