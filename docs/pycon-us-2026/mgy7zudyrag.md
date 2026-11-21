---
layout: default
title: "Post Incident Runtime SBOM Generation from Python Memory - Hala Ali"
nav_order: 79
parent: PyCon US 2026
type: Video Note
description: "Hala Ali, a PhD student at Virginia Commonwealth University, presented a novel memory forensic tool called MemSBOM designed to generate runtime Software Bill of Materials (SBOMs) from Python proces..."
resource: "https://www.youtube.com/watch?v=mgY7zuDYrag"
youtube_stats:
  view_count: 299
  like_count: 7
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Hala Ali, a PhD student at Virginia Commonwealth University, presented a novel memory forensic tool called MemSBOM designed to generate runtime Software Bill of Materials (SBOMs) from Python process memory.
The talk addresses the critical security gap where static SBOM tools and file system data fail to reflect the actual packages loaded and executed in a compromised production environment, particularly due to Python’s dynamic nature and runtime imports.
By leveraging Volatility 3 to parse internal Python structures such as the garbage collector, thread stacks, and bytecode, MemSBOM accurately recovers the exact versions of third-party modules in use, even when version metadata is missing or inconsistent with installed files.
Evaluation against 51 real-world applications demonstrated that MemSBOM outperforms eight existing static tools by identifying runtime discrepancies and reducing false positives in vulnerability detection, such as distinguishing between applications that merely import a vulnerable package versus those that actively execute the vulnerable code paths.
The tool, which supports Python versions up to 3.14 and is slated for open-source release, provides incident responders with a precise view of the runtime state to enable targeted remediation of supply chain attacks.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Hala Ali, a PhD student at Virginia Commonwealth University, presented on generating post-incident runtime Software Bill of Materials (SBOM) from Python memory. |
|   2 | The core problem is determining which packages were actually loaded and running in a compromised Python process, as file system data and static tools like pip freeze may not reflect the true runtime state. |
|   3 | Python’s dynamic nature allows for runtime imports and module manipulation, making static SBOM tools insufficient for accurate incident response. |
|   4 | In 2025, over 2,000 malware reports were processed by PyPI, including malicious versions of popular packages like Mistral AI and Elementary Data that trigger payloads upon import. |
|   5 | Runtime SBOMs differ from build or deployed SBOMs by capturing the exact components and versions active in memory, which is critical for identifying actual vulnerabilities. |
|   6 | Existing SBOM tools often rely on configuration files or metadata, leading to version estimation errors and missed runtime-only modules. |
|   7 | The research introduces MemSBOM, a novel memory forensic tool built on Volatility 3 to parse Python processes directly from memory dumps. |
|   8 | MemSBOM identifies Python runtime entry points, accesses interpreter data structures, and recovers modules from threads, garbage collectors, and heap arenas. |
|   9 | The tool handles multi-process applications by parsing memory from all related processes, such as Apache Airflow’s 26+ concurrent processes. |
|  10 | Version information is often missing in memory, so MemSBOM extracts cached metadata using regular expressions and normalizes names to query PyPI for accurate version mapping. |
|  11 | To determine dependency relationships, the tool parses function bytecode from memory to identify transitive calls between modules. |
|  12 | Evaluation against 51 real-world Python applications showed that existing tools missed 4-6% of runtime modules and had limited support for modern configuration files like PEP 621. |
|  13 | In five tested applications, the installed version on the file system differed from the version actually running in memory, highlighting the unreliability of static analysis. |
|  14 | A case study involving Tornado 6.4.2 demonstrated that MemSBOM can reduce false positives by identifying which specific applications actually call vulnerable functions. |
|  15 | The tool supports Python versions up to 3.14 and 3.15, accounting for changes in garbage collector data structures across versions. |
|  16 | MemSBOM was accepted for the Black Hat Arsenal and is planned to be open-sourced within two months of the presentation. |
|  17 | The researchers acknowledge the adversarial nature of memory forensics, noting that attackers can manipulate memory structures, which necessitates multi-layered scanning techniques. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mgY7zuDYrag/hqdefault.jpg)](https://www.youtube.com/watch?v=mgY7zuDYrag)

[Watch on YouTube](https://www.youtube.com/watch?v=mgY7zuDYrag)
