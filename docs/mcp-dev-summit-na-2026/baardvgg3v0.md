---
layout: default
title:
  "MCPwned: Hacking MCP Servers With One Skeleton Key Vulnerability - Jonathan
  Leitschuh, Independent"
nav_order: 64
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Jonathan Lechu, a software engineer and security researcher, presents
  his findings on vulnerabilities in locally running servers, particularly focusing
  on Model Context Protocol (MCP) servers. He explains how browsers' same origin policy
  an...
resource: https://www.youtube.com/watch?v=baardVGG3v0
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

Jonathan Lechu, a software engineer and security researcher, presents his findings on vulnerabilities in locally running servers, particularly focusing on Model Context Protocol (MCP) servers.
He explains how browsers' same origin policy and longstanding behaviors allow malicious websites to communicate with local servers through simple requests or DNS rebinding attacks, a technique that can bypass security restrictions and has been exploited in numerous high-profile incidents over the past two decades.
Lechu demonstrates that many MCP servers, including those from major vendors like Google, Docker, and AWS, were vulnerable to these attacks due to improper validation of the origin header, despite clear warnings in the MCP specification.
He shares examples where these vulnerabilities allowed remote code execution or unauthorized access to sensitive data, and notes that while some vendors have patched their SDKs or issued bounties, many servers remain at risk because protections are not enabled by default.
Lechu concludes by urging developers to properly configure their servers and not rely on browsers for protection, as these attack vectors remain largely unmitigated in most environments.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jonathan Lechu is a software engineer and security researcher, currently staff security engineer at Braise.                                              |
|   2 | Research focus: vulnerabilities in locally running servers, especially on developer machines.                                                            |
|   3 | Locally running servers often have broad data access and can be attacked via browsers.                                                                   |
|   4 | Same Origin Policy (SOP) prevents cross-origin requests but has exceptions and legacy behaviors.                                                         |
|   5 | Browsers allow certain "simple requests" (GET, POST, etc.) to localhost and private network servers.                                                     |
|   6 | Developers often unaware that browsers can access localhost/private servers, leading to vulnerabilities.                                                 |
|   7 | Historical attacks include:                                                                                                                              |
|   8 | 2008: Drive-by pharming (reconfiguring home router DNS via browser).                                                                                     |
|   9 | 2015: DNS rebinding Wi-Fi attacks.                                                                                                                       |
|  10 | 2016: JetBrains IDE and Trend Micro password manager local server vulnerabilities.                                                                       |
|  11 | 2018: Port scanning via browser timing attacks.                                                                                                          |
|  12 | 2019: Zoom webcam hijack via local server; Dell remote support assistant RCE.                                                                            |
|  13 | 2020: eBay port scanning.                                                                                                                                |
|  14 | 2024: Bypassing browser protections using 0.0.0.0.                                                                                                       |
|  15 | Recent: Yandex/Meta deanonymizing users via local servers in Android apps.                                                                               |
|  16 | DNS rebinding attacks bypass SOP, allowing malicious sites to interact with local/private servers.                                                       |
|  17 | Tools like Singularity of Origin automate DNS rebinding attacks.                                                                                         |
|  18 | MCP (Model Context Protocol) servers are vulnerable if origin header validation is not enforced.                                                         |
|  19 | TypeScript MCP SDK previously had DNS rebinding protection disabled by default; few servers set protection flags.                                        |
|  20 | Demonstrated attacks on MCP protocol server, Google OSS Fuzz, Google Cloud Run, Google Toolbox, Apollo GraphQL, Docker MCP gateway, AWS Labs MCP server. |
|  21 | Vulnerabilities allowed arbitrary code execution, file uploads, database access, and AWS CLI calls.                                                      |
|  22 | Some vendors have patched; others have not (e.g., Google Toolbox remains vulnerable as of talk date).                                                    |
|  23 | Anthropic added API maturity tiers; only Tier 1 guaranteed protected.                                                                                    |
|  24 | Total bounties: $2,100 and a t-shirt.                                                                                                                    |
|  25 | Testing tip                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=baardVGG3v0)
