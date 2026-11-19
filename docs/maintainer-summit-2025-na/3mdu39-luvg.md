---
layout: default
title: "Tending the Kubernetes Dependency Tree: Bonsai or Bonfire? - Jordan Liggitt & Davanum Srinivas"
nav_order: 3
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: 'Jordan Liot and Dims discuss the critical importance of managing software dependencies in Kubernetes, emphasizing that uncontrolled growth can turn a manageable project into a "dependency bonfire."...'
resource: "https://www.youtube.com/watch?v=3mDu39-LUVg"
tags:
  - maintainer-summit-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T17:23:58+00:00
---

# Summary

Jordan Liot and Dims discuss the critical importance of managing software dependencies in Kubernetes, emphasizing that uncontrolled growth can turn a manageable project into a "dependency bonfire." They highlight the use of tools like `depstat` and the practice of vendoring code to gain visibility into the actual impact of dependency changes, allowing teams to identify hidden risks such as unmaintained libraries or excessive transitive dependencies.
The speakers detail strategies for reducing complexity, including isolating test-only and tooling dependencies into separate modules and collaborating with upstream projects to extract unnecessary binary components, which helped reduce Kubernetes' dependency count from over 400 to under 250.
To prevent future regressions, they implement a "ratcheting" mechanism using a dependency verifier that blocks new unwanted links and tracks progress toward removing existing ones.
Finally, they describe proactive CI jobs that test against the latest upstream versions and Go master branches to catch breaking changes early, ensuring that security updates and version bumps remain manageable and do not disrupt the release cycle.

# Main Points

|   # | Main point                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Systems depend on external components, meaning any issue in dependencies becomes a direct problem for the project.                                                                        |
|   2 | Projects often start with minimal dependencies but can quickly accumulate a large, unmanaged dependency tree, described as a "dependency bonfire."                                        |
|   3 | Kubernetes currently has over 250 dependencies and over a million lines of vendor code, which is a significant improvement from previous years.                                           |
|   4 | The tool depstat is used to visualize the dependency graph and identify the specific impact of pull requests on the dependency tree.                                                      |
|   5 | Storing the vendor tree in the repository allows for precise code review of dependencies and visibility into what is actually linked into binaries.                                       |
|   6 | Vendoring reveals hidden issues, such as pulling in unmaintained libraries or excessive code through simple helper functions.                                                             |
|   7 | Key areas for code review include checking for init functions that execute automatically and identifying compatibility breaks in API surfaces.                                            |
|   8 | Adding tests for the specific surface area of dependencies helps detect breaking changes in behavior before they impact the project.                                                      |
|   9 | Library packages, binaries, and test-only dependencies all pass their dependencies downstream to consumers of the module.                                                                 |
|  10 | Isolating binary-specific dependencies from library code, as done with cAdvisor, prevents unnecessary dependency complexity for library users.                                            |
|  11 | Test-only dependencies still impact project health and may need isolation in separate Go modules to prevent unwanted transitive links.                                                    |
|  12 | The Go tool directive does not isolate tool dependencies from the main module, so separate submodules are required for tooling.                                                           |
|  13 | Upstream projects can be modified to improve dependency management, such as extracting specific libraries or removing unused code.                                                        |
|  14 | The Gen Proto dependency issue required a two-to-three-year effort to unwind, involving upstream collaboration and gradual isolation.                                                     |
|  15 | A ratcheting strategy is used to prevent new unwanted dependencies and track the removal of existing ones over time.                                                                      |
|  16 | Kubernetes uses a dependency verifier with a JSON file to define unwanted dependencies and track their status in the graph and vendor tree.                                               |
|  17 | Presubmit checks enforce the dependency rules, alerting developers when they attempt to add new links to unwanted dependencies.                                                           |
|  18 | CI jobs that test against the latest master branches of dependencies help identify breaking changes early, before they become difficult to fix.                                           |
|  19 | Testing against the master branch of the Go language allows for early detection of compatibility issues with new Go versions.                                                             |
|  20 | Regular monitoring of dependency counts, code lines, and distance from latest releases helps maintain visibility and prevent steady growth.                                               |
|  21 | Vulnerability scanning tools like go vet check are used to determine if a project is actually impacted by a security issue, rather than just having a dependency on a vulnerable version. |
|  22 | Release branches are only updated for security vulnerabilities that directly impact the code being used, avoiding unnecessary updates.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3mDu39-LUVg/hqdefault.jpg)](https://www.youtube.com/watch?v=3mDu39-LUVg)

[Watch on YouTube](https://www.youtube.com/watch?v=3mDu39-LUVg)
