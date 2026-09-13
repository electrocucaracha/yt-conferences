---
type: Video Note
title: "A Bug’s-Eye View: Kubernetes SIG Security Explains It... Ian C, Tabitha S, Rory M, Iain S & Mahé T"
description: "The video features a Kubernetes SIG Security maintainer track talk, led by Ian Coldwater and other SIG Security members, focusing on recent updates and processes within the group. The SIG Security Docs subproject, co-chaired by Rory McHune..."
resource: https://www.youtube.com/watch?v=ujnqeWQZ17w
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a Kubernetes SIG Security maintainer track talk, led by Ian Coldwater and other SIG Security members, focusing on recent updates and processes within the group.
The SIG Security Docs subproject, co-chaired by Rory McHune, highlighted their work updating the OWASP Kubernetes Top 10, a key security resource, through community input and collaborative drafting.
Ian discussed the third-party audit subproject, which reviews Kubernetes components with external vendors to identify and address security issues, noting ongoing efforts to resolve findings from past audits and the recent audit by Shielder that focused on non-core components.
Tabitha Sable explained the role of the Security Response Committee in confidentially triaging, fixing, and disclosing vulnerabilities, emphasizing the importance of clear communication and accurate CVE scoring.
Mah from SIG Security Tooling described improvements to the official CVE feed and tooling to streamline vulnerability disclosure and metadata management.
The talk concluded with an invitation for new contributors of all backgrounds to join SIG Security’s inclusive community and participate in ongoing efforts to enhance Kubernetes security.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ian Coldwater (they/them) is co-chair of Kubernetes SIG Security.                                                                            |
|   2 | The talk covers updates and processes of SIG Security, including collaboration with the Security Response Committee.                         |
|   3 | SIG Security is a horizontal SIG working across Kubernetes to improve security, with much work done in subprojects.                          |
|   4 | SIG Security Docs works to improve Kubernetes security documentation and creates independent security docs.                                  |
|   5 | Major recent project: Updating the OWASP Kubernetes Top 10, which had become outdated.                                                       |
|   6 | The team gained access to the OWASP Kubernetes Top 10 repo, brainstormed new items, surveyed the community, and released an updated list.    |
|   7 | Third Party Audit subproject manages external security audits of Kubernetes.                                                                 |
|   8 | Previous audits: Trail of Bits (2019) and NCC Group (2022); some findings remain open.                                                       |
|   9 | Recent audit (2023) by Shielder focused on non-core Kubernetes components; findings are being addressed.                                     |
|  10 | Security Response Committee (SRC) handles confidential security issues, incident response, and vulnerability disclosure.                     |
|  11 | Vulnerabilities are defined as violations of reasonable security expectations or explicit promises.                                          |
|  12 | Vulnerabilities are reported via HackerOne or security@kubernetes.io, triaged privately, fixed, and then disclosed publicly.                 |
|  13 | Disclosures include GitHub issues, mailing lists, Slack, forums, and the CVE database.                                                       |
|  14 | CVSS scoring is used for vulnerability severity, requiring careful context-based judgment.                                                   |
|  15 | SIG Security Tooling maintains code and tools to support security, including the official CVE feed and Snyk dependency scanning.             |
|  16 | Recent improvements: Structured CVE data using OSV schema, new CLI tool for disclosures, and plans for a "won't fix" label for certain CVEs. |
|  17 | Shoutouts to new contributors and ongoing work to improve CVE feed accuracy.                                                                 |
|  18 | SIG Security encourages new contributors of all backgrounds; meetings are open and inclusive.                                                |
|  19 | Contact via mailing list, Slack (#sig-security), or at conference booth.                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ujnqeWQZ17w)