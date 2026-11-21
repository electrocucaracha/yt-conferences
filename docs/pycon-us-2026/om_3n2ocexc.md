---
layout: default
title: "Create a Python Package From Zero to Hero - Mario Munoz"
nav_order: 52
parent: PyCon US 2026
type: Video Note
description: "Mario, a Python developer known for his blog \"Python by Night,\" presents a comprehensive guide on creating Python packages, emphasizing that the process extends far beyond technical configuration t..."
resource: "https://www.youtube.com/watch?v=oM_3N2ocExc"
youtube_stats:
  view_count: 730
  like_count: 13
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

Mario, a Python developer known for his blog "Python by Night," presents a comprehensive guide on creating Python packages, emphasizing that the process extends far beyond technical configuration to include strategic planning and community engagement.
He argues that before writing any code, developers should clearly define their problem, search for existing solutions to avoid redundancy, and use documentation-driven design to shape their API and scope.
The technical workflow involves configuring the `pyproject.toml` file, selecting a build system, and using tools like UV to generate distribution wheels.
Mario recommends testing the publishing process on TestPyPI to ensure security and functionality before releasing to the official PyPI index, while also highlighting the benefits of trusted publishing for enhanced security.
Finally, he stresses that maintaining a package is a social responsibility, requiring clear documentation, licensing, and active engagement with users to foster discovery and contribution, rather than simply uploading code and expecting it to succeed.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker, Mario, introduces his background in Python talks and his blog "Python by Night" before presenting a talk on creating Python packages from zero to hero. |
|   2 | Python packaging is described as an evergreen topic that can seem intimidating to newer developers, prompting a structured approach to the process. |
|   3 | The first step is to identify the problem and clearly define the intent of the code, noting that even niche libraries are valuable if their purpose is well-communicated. |
|   4 | The second step involves searching existing resources on PyPI and social media to ensure the problem hasn't already been solved, which helps avoid redundant work and user confusion. |
|   5 | If existing packages are close but incomplete, contributing to those projects may be more efficient than building a new one from scratch. |
|   6 | The third step is consolidating the idea by considering how the library will be used, what the API should look like, and defining the scope of the project. |
|   7 | The fourth step is preparation using documentation-driven design, where writing documentation and pseudo-code helps refine the API and naming conventions before writing actual code. |
|   8 | The fifth step is the work phase, where code is written based on the previously defined constraints to prevent scope creep. |
|   9 | The pyproject.toml file is highlighted as the central configuration file for packaging, containing the unique project name and build system details. |
|  10 | Build systems such as setuptools, hatchling, flit, and UV build are mentioned, with a note that the choice is often irrelevant for simple projects without extension modules. |
|  11 | The official Python packaging user guide is recommended as a primary resource for understanding the packaging process in detail. |
|  12 | Publishing begins with TestPyPI, a separate index for testing the distribution process before deploying to the official PyPI. |
|  13 | Creating an account on TestPyPI and generating an API token are necessary steps to publish the package securely. |
|  14 | The UV tool is used to build the package into a wheel and publish it using the uv publish command with the API token and specific URL. |
|  15 | The environment variable UV_PUBLISH_TOKEN can simplify the publishing process by storing the token securely. |
|  16 | Trusted publishing is an alternative security feature supported by PyPI that removes the need for manual tokens, available through services like GitHub Actions and GitLab CI/CD. |
|  17 | Updating packages frequently is encouraged, with tools like UV bump facilitating semantic versioning and automated distribution via CI/CD pipelines. |
|  18 | PyPI project pages are generated automatically from the README file and metadata defined in the pyproject.toml file. |
|  19 | Discovering a package is a social activity that requires engaging with users and communities rather than relying solely on the platform for visibility. |
|  20 | Maintaining a package involves providing proper documentation, a test suite, and a contribution guide to support users and future contributors. |
|  21 | The speaker recommends the official Python packaging guide and the Python Packaging Guide at pypa.io for comprehensive learning resources. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/oM_3N2ocExc/hqdefault.jpg)](https://www.youtube.com/watch?v=oM_3N2ocExc)

[Watch on YouTube](https://www.youtube.com/watch?v=oM_3N2ocExc)
