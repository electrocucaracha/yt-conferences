---
layout: default
title: "When pip install isn't enough: real threats and practical defenses... - Diego Caceres Solis"
nav_order: 15
parent: PyCon US 2026
type: Video Note
description: "Diego Cáceres, a systems engineer from Chile, presents a cybersecurity talk titled \"When pip install isn't enough,\" focusing on real threats and practical defenses within the Python and PyPI ecosys..."
resource: "https://www.youtube.com/watch?v=IyLccXQ8xBk"
youtube_stats:
  view_count: 162
  like_count: 1
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

Diego Cáceres, a systems engineer from Chile, presents a cybersecurity talk titled "When pip install isn't enough," focusing on real threats and practical defenses within the Python and PyPI ecosystems.
He argues that simply installing packages via `pip` creates significant structural risks due to implicit trust, where developers often overlook the extensive attack surface created by unknown dependencies and the potential for malicious code hidden within seemingly legitimate libraries.
The presentation details specific threats such as typosquatting, where attackers exploit common spelling errors to distribute malware, and dependency confusion, which involves hijacking package resolution to inject malicious code from public repositories into private environments.
Cáceres highlights real-world incidents, including the Glassworm campaign and compromised PyPI packages, emphasizing that adversaries use obfuscation, reverse shells, and social engineering to bypass security controls and exfiltrate data.
To mitigate these risks, he recommends a multi-layered defense strategy that includes verifying package reputation and origin, using static and dynamic analysis tools like `pip-audit`, `Safety`, and `OSV-Scanner` to detect vulnerabilities, and implementing secure dependency management practices such as hash verification, Software Bill of Materials (SBOM) generation, and rigorous CI/CD pipeline security.
Ultimately, the speaker stresses the importance of fostering a security culture where developers proactively analyze code integrity, monitor for unusual behavior, and maintain incident response capabilities, noting that while tools and legislation like Chile’s National Cybersecurity Agency provide frameworks, human vigilance and secure coding practices from day one are essential to staying ahead of evolving cyber threats.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The presentation addresses cybersecurity threats in the Python ecosystem, specifically focusing on risks associated with PyPI and pip install commands. |
|   2 | Implicit trust in package installation creates structural risks, as developers often install packages without verifying their source or integrity. |
|   3 | The attack surface extends beyond the primary package to include numerous transitive dependencies that may be unknown or unvetted. |
|   4 | Typosquatting is a threat where malicious packages mimic legitimate names through spelling errors to trick developers into installing malware. |
|   5 | Dependency confusion occurs when public repositories are exploited to override private package names, leading to the installation of malicious code. |
|   6 | Real-world supply chain compromises include the Glassworm campaign, Ultra-ytics compromise, and package spoofing for data exfiltration. |
|   7 | Adversaries use obfuscation and encryption to hide malicious code within Python packages, which can execute scripts during installation. |
|   8 | Malicious packages can open unauthorized ports, establish command-and-control connections, or create backdoors and reverse shells. |
|   9 | Social engineering targets developers through deceptive emails or messages, exploiting human error to compromise systems. |
|  10 | Chile's National Cybersecurity Agency (ANSI) and its CSIRT publish alerts and indicators of compromise, such as fraudulent URLs mimicking legitimate sites. |
|  11 | Tools like revshells.com provide free resources for generating reverse shells, highlighting the ease with which attackers can exploit vulnerabilities. |
|  12 | Detection strategies include static and dynamic analysis, as well as combined approaches to identify malicious dependencies before execution. |
|  13 | Security tools such as pip audit, Safety, and OSV-Scanner help identify vulnerabilities and Common Vulnerabilities and Exposures (CVEs) in projects. |
|  14 | CVEs identify specific vulnerabilities, such as command injection flaws in the webbrowser module, which can allow arbitrary code execution. |
|  15 | Developers should verify package reputation, origin, and creator trustworthiness before implementation to avoid malicious or low-quality libraries. |
|  16 | Recommendations include verifying file hashes for integrity, using private or trusted repositories, and reducing dependency risk through control. |
|  17 | Secure dependency management involves fixing specific versions and generating Software Bills of Materials (SBOMs) to track all project dependencies. |
|  18 | Organizations should maintain a dedicated security role for risk assessment, incident response, and continuous integration security controls. |
|  19 | A strong security culture requires developers to integrate security practices from the initial coding phase rather than treating it as an afterthought. |
|  20 | Best practices include monitoring for unusual behavior like RAM spikes or suspicious connections, and rotating credentials upon suspicion of compromise. |
|  21 | Additional tools like Bandit, Syft, Grype, Retire.js, and Snyk assist in scanning for vulnerabilities across various software components. |
|  22 | The Python Software Foundation recently completed a successful audit of PyPI, reinforcing the importance of ongoing security assessments in the ecosystem. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/IyLccXQ8xBk/hqdefault.jpg)](https://www.youtube.com/watch?v=IyLccXQ8xBk)

[Watch on YouTube](https://www.youtube.com/watch?v=IyLccXQ8xBk)
