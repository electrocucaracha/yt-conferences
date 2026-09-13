---
layout: default
title: The Boring Attack That Will Actually Get You - Craig Jellick, Obot AI
nav_order: 91
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Craig Jelik, VP of Engineering at Obot, emphasizes the
  growing threat of supply chain attacks on MCP servers, highlighting that simple
  tactics like name squatting and compromised dependencies can be more dangerous than
  novel e...
resource: https://www.youtube.com/watch?v=6Tn4YKRcR-E
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Craig Jelik, VP of Engineering at Obot, emphasizes the growing threat of supply chain attacks on MCP servers, highlighting that simple tactics like name squatting and compromised dependencies can be more dangerous than novel exploits.
He presents real-world case studies, including the Postmark MCP attack, the LiteLLM and Trivy compromise, and the Axios incident, illustrating how attackers exploit trust in open-source software and automated processes to exfiltrate sensitive data or gain remote access.
Jelik underscores the importance of careful dependency management, reviewing package provenance, using age-based cooldowns, disabling post-install hooks, and auditing GitHub Actions to mitigate risks.
He also advocates for organizational strategies such as secure build pipelines, containerization, repackaging open-source servers, and centralizing MCP server management through gateways to improve visibility, control, and incident response.
The talk concludes with practical recommendations and resources for developers to strengthen their security posture against evolving supply chain threats.

# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on practical supply chain attacks targeting MCP servers.                                               |
|   2 | Speaker: Craig Jelik, VP of Engineering at Obot, which builds an open-source MCP gateway.                               |
|   3 | Main takeaway: Be cautious and nervous when installing MCP servers locally.                                             |
|   4 | Commonly discussed attacks (tool poisoning, rug pulls, prompt injection) are less concerning than supply chain attacks. |
|   5 | Case Study 1: Postmark MCP                                                                                              |
|   6 | Legitimate GitHub repository name not registered on npm.                                                                |
|   7 | Attacker squatted the npm name, published a malicious version after 15 benign versions.                                 |
|   8 | Malicious version BCC’d all emails, exfiltrating data.                                                                  |
|   9 | Detected quickly by Koi security firm; impact limited.                                                                  |
|  10 | Case Study 2: LiteLLM Supply Chain Attack                                                                               |
|  11 | Malicious software scanned for and stole credentials.                                                                   |
|  12 | Discovered after a developer’s machine crashed due to a fork bomb.                                                      |
|  13 | Attack involved transitive dependency (Trivy) being compromised.                                                        |
|  14 | Attacker exploited GitHub Actions (pull_request_target) in Trivy, leading to chaos and credential theft.                |
|  15 | Malicious version of LiteLLM published, affecting downstream users.                                                     |
|  16 | Case Study 3: Axios Attack                                                                                              |
|  17 | Axios maintainer’s account compromised; two malicious versions published.                                               |
|  18 | Attack used a double-obfuscated, self-erasing dependency.                                                               |
|  19 | Malicious code was live for only 3.5 hours but Axios is downloaded 100M times weekly.                                   |
|  20 | Case Study 4: Claude code source leak                                                                                   |
|  21 | Caused by human error and manual process.                                                                               |
|  22 | Highlights risk of accidental exposure and potential for supply chain attacks.                                          |
|  23 | Recommendations for developers:                                                                                         |
|  24 | Reevaluate and pin MCP server installations.                                                                            |
|  25 | Carefully review package names and provenance.                                                                          |
|  26 | Use age-based cooldowns for dependencies (e.g., don’t install packages newer than 7 days).                              |
|  27 | Disable npm post-install hooks.                                                                                         |
|  28 | Audit GitHub Actions for risky patterns like pull_request_target.                                                       |
|  29 | Check for ongoing effects of attacks and read up on recent incidents.                                                   |
|  30 | Organizational recommendations:                                                                                         |
|  31 | Use secure build pipelines, pin depend Notes: Recommendations for developers:                                           |
|  32 | Reevaluate and pin MCP server installations.                                                                            |
|  33 | Carefully review package names and provenance.                                                                          |
|  34 | Use age-based cooldowns for dependencies (e.g., don’t install packages newer than 7 days).                              |
|  35 | Disable npm post-install hooks.                                                                                         |
|  36 | Audit GitHub Actions for risky patterns like pull_request_target.                                                       |
|  37 | Check for ongoing effects of attacks and read up on recent incidents.                                                   |
|  38 | Organizational recommendations:                                                                                         |
|  39 | Use secure build pipelines, pin depend Ratings (1-5): 4                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6Tn4YKRcR-E)
