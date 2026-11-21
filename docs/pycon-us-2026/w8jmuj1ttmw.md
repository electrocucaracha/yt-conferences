---
layout: default
title: "Switching from Sphinx to Markdown - Kattni"
nav_order: 63
parent: PyCon US 2026
type: Video Note
description: "Katney, a core developer on the Beeware project, presented a detailed case study on migrating the project’s documentation infrastructure from Sphinx and reStructuredText to MakeDocs and Markdown."
resource: "https://www.youtube.com/watch?v=W8jmuJ1Ttmw"
youtube_stats:
  view_count: 429
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

Katney, a core developer on the Beeware project, presented a detailed case study on migrating the project’s documentation infrastructure from Sphinx and reStructuredText to MakeDocs and Markdown.
She highlighted that while reStructuredText has a long history in the Python ecosystem, Markdown offers superior human readability, broader ecosystem adoption, and better compatibility with modern AI tools.
The migration process, which took over nine months, involved rigorous preparation, including selecting MakeDocs for its static site capabilities and translation support, and developing custom tools to handle complex features like type alias documentation and community-driven translations.
Katney emphasized that the shift was not merely technical but also social, requiring a phased approach to manage risk and engage the community, such as converting READMEs through "good first issues." The result was a unified, faster, and more maintainable documentation system that significantly improved the developer and user experience, proving that despite the substantial effort required, the transition to Markdown is a worthwhile investment for modern Python projects.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Katney, chair of the PyOhio conference and core developer of the Briefcase project, presented on migrating documentation from Sphinx and reStructuredText to MakeDocs and Markdown. |
|   2 | ReStructuredText has been the standard for Python documentation for 23 years, while Sphinx has been used for 18 years, but both are criticized for poor human readability and complex link syntax. |
|   3 | Markdown is designed to be human-readable and writable, with widespread adoption across tech ecosystems, messaging platforms, and AI tools due to its simplicity and ease of conversion to HTML. |
|   4 | The Briefcase project migration involved converting multiple tools, including Toga, Briefcase, and Rubicon Objective-C, along with the project website and standalone documents. |
|   5 | MakeDocs was selected as the new documentation generator because it is a static site generator built around Markdown, offering faster live previews and better tracking of source code changes than Sphinx. |
|   6 | The migration required establishing feature parity with Sphinx, including documenting type aliases, which was a key requirement for project approval. |
|   7 | A custom translation solution was developed using the Translate Toolkit to convert PO files to Markdown, integrating with Weblate for community-driven translations. |
|   8 | Several MakeDocs plugins were utilized, including Attribute List, AutoRef, Macros, Literate Nav, MakeDocstrings, and PyMdown Extensions, to replicate Sphinx features and enhance Markdown formatting. |
|   9 | Pandoc was used for initial reStructuredText to Markdown conversion, supplemented by custom regular expression scripts to handle docstrings and malformed links that Pandoc could not process. |
|  10 | A shared utilities repository, Briefcase Docs Tools, was created to centralize dependencies, theme customizations, build tooling, and shared content like contribution guides. |
|  11 | The migration process took over nine months, with the Toga documentation taking two and a half months due to its complexity, while Briefcase took only three days after the initial infrastructure was built. |
|  12 | Manual verification was performed by comparing the new and old documentation sites page by page to catch issues and edge cases, which is recommended for complex migrations. |
|  13 | The project also involved a social change, requiring a solid proposal to convince the core team and engaging the community to convert README files via labeled good first issues. |
|  14 | The migration resulted in faster incremental builds, native type documentation, improved API documentation layout, and easier content maintenance. |
|  15 | MakeDocs is currently in a transition period, with version 1.x no longer maintained and version 2.0 not backwards compatible, while alternatives like ProperDocs and Zens exist. |
|  16 | The speaker recommends the migration for projects with the resources to undertake it, noting that it can be split among multiple developers to reduce total time. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/W8jmuJ1Ttmw/hqdefault.jpg)](https://www.youtube.com/watch?v=W8jmuJ1Ttmw)

[Watch on YouTube](https://www.youtube.com/watch?v=W8jmuJ1Ttmw)
