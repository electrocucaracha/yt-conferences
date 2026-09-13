---
type: Video Note
title: "Enhancing Software Composition Analysis Resilience Against Contai... Agathe Blaise & Jacopo Bufalino"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=G24upbAXVd8
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: The presentation discusses container image obuscation, which refers to the intentional or unintentional modification of a container image to evade vulnerability scanning tools.
Researchers analyzed various tools for container vulnerability analysis and found that many are vulnerable to individual instances of obuscation, but become more vulnerable when multiple techniques are combined.
The researchers also conducted an analysis of real-world containers and found that over 10% of them contain obuscation techniques, including OS package information, dependency offuscation, URL autheis, alias and link offiscation, and pack ofcation.
To mitigate these issues, the researchers developed an open-source tool called ORCA, which can reconstruct a container image's content from its layers and metadata.
The goal is to find a balance between transparency and image size reduction.
# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Container image obuscation refers to intentionally or unintentionally modifying or generating content in a container image.               |
|   2 | Obuscation techniques include:                                                                                                            |
|   3 | OS offuscation                                                                                                                            |
|   4 | OS package information offuscation                                                                                                        |
|   5 | Dependency offuscation                                                                                                                    |
|   6 | Package offuscation                                                                                                                       |
|   7 | URL autheis                                                                                                                               |
|   8 | Alias and link offiscation                                                                                                                |
|   9 | Pack ofcation (compressing the content of the image)                                                                                      |
|  10 | State-of-the-art tools are vulnerable to obuscation techniques.                                                                           |
|  11 | A study analyzed 600 containers and found that:                                                                                           |
|  12 | Over 10% of containers had OS offuscation                                                                                                 |
|  13 | Many containers downloaded software from the internet                                                                                     |
|  14 | Some containers removed dependencies or packages                                                                                          |
|  15 | The study also developed an open-source tool called ORCA to mitigate obuscation.                                                          |
|  16 | ORCA generates a sbomb (software bill of materials) that can be used by other tools to scan containers.                                   |
|  17 | The study found that multi-stage builds and compression can make it difficult for tools to detect obuscation.                             |
|  18 | Guidelines for preventing obuscation are needed, but this requires a community effort.                                                    |
|  19 | A middle ground could be adding metadata to the image during build, providing transparency while reducing image size and vulnerabilities. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=G24upbAXVd8)