---
layout: default
title: "Inclusive Data for 1.3 Billion: Designing Accessible Visualizations"
nav_order: 14
parent: PyCon US 2025
type: Video Note
description: "In this session, Frank Elabsky and Pavitraishwaramorti discuss the critical importance of designing accessible data visualizations for the 1.3 billion people worldwide living with disabilities."
resource: "https://www.youtube.com/watch?v=WZMo6QG1j98"
youtube_stats:
  view_count: 1069
  like_count: 11
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

In this session, Frank Elabsky and Pavitraishwaramorti discuss the critical importance of designing accessible data visualizations for the 1.3 billion people worldwide living with disabilities.
They emphasize that accessibility is not only a moral and legal requirement under laws like the ADA but also benefits everyone through the "curbcut effect," where features designed for specific needs improve the experience for all users.
The speakers introduce Chartability, a framework derived from Web Content Accessibility Guidelines (WCAG) that provides 50 systematic tests to evaluate the accessibility of charts and interactive data experiences.
Through live demonstrations using the Bokeh library, they highlight common barriers such as insufficient color contrast and the lack of semantic HTML elements, which prevent screen readers from properly interpreting interactive components like buttons and charts.
To address these issues, they recommend practical strategies including ensuring high color contrast, adding clear text descriptions and titles, increasing line widths for better visibility, and providing raw data in alternative formats.
The talk concludes with a discussion on emerging technologies like sonification and machine learning for chart description, noting that while promising, these tools require further development to ensure accuracy and ethical reliability for blind users.

# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | 1.3 billion people globally live with a disability, with over a quarter of the US population self-reporting a disability affecting daily life.                                   |
|   2 | CDC data indicates 4.1% of US residents have color vision deficiency, 4.8% are blind or low vision, and 12.8% have cognitive or neurological disabilities.                       |
|   3 | Accessibility is a legal requirement under the Americans with Disabilities Act and the European Accessibility Act, which are increasing regulatory expectations.                 |
|   4 | The curb cut effect demonstrates that accessibility features designed for people with disabilities, such as curb cuts and screen contrast, benefit everyone.                     |
|   5 | Data visualization is critical for equitable participation in politics, health decisions, and data analysis careers for people with disabilities.                                |
|   6 | The Python ecosystem offers a broad spectrum of visualization tools, but accessibility work requires low-level understanding of building blocks like HTML rather than just PNGs. |
|   7 | Chartability is a framework created to systematically evaluate charts and interactive data experiences for accessibility, containing 50 specific tests.                          |
|   8 | Accessibility principles include perceivable, operable, understandable, and robust, with additional principles of compromising, assistive, and flexible.                         |
|   9 | Bokeh was selected as the initial library for accessibility audits because it targets web browsers and renders in HTML-friendly formats.                                         |
|  10 | Color contrast is a critical accessibility factor, and the WCAG Color Contrast Checker browser extension can be used to audit foreground and background colors.                  |
|  11 | High contrast palettes are difficult to create because they require changing both hue and luminance to meet accessibility standards.                                             |
|  12 | Screen readers navigate web pages using the keyboard API, and elements must have proper semantics to be perceivable and operable.                                                |
|  13 | Audits of Bokeh revealed that many charts lack alt text, and interactive buttons often use div elements that screen readers cannot identify as interactive.                      |
|  14 | A total of 150 accessibility tests were performed on the Bokeh ecosystem, with findings and next steps published in a public audit report.                                       |
|  15 | Complete graphs require titles, legends, and axis labels before accessibility improvements can be effectively applied.                                                           |
|  16 | Relying solely on color to convey information is inaccessible; adding texture and increasing line width improves perceivability for all users.                                   |
|  17 | Interactive features like pan and zoom should be disabled if they do not provide additional information, reducing cognitive load and potential errors.                           |
|  18 | Text descriptions are essential for accessibility, as textless charts are inaccessible to screen reader users and less effective for general audiences.                          |
|  19 | Effective text descriptions follow a layered approach, starting with high-level context and axes, moving to main statistics, and ending with detailed data points.               |
|  20 | Sharing raw data in formats like tables or CSV files provides additional ways for users to interact with and verify visualization data.                                          |
|  21 | The accessibility audit and improvements for Bokeh were funded by the Chan Zuckerberg Initiative’s Essential Open Source Software Program.                                       |
|  22 | Language register and clarity are part of the understandable principle, impacting how effectively data is communicated to diverse audiences.                                     |
|  23 | Research on accessibility for dyscalculia exists but is not yet integrated into formal standards, which typically take 10 to 20 years to update.                                 |
|  24 | Sonification of charts is a potential accessibility feature, with existing examples in libraries like Eerie, Highcharts, and Apple’s Audio Graphs.                               |
|  25 | Machine learning models for describing charts show promise but face ethical risks due to hallucinations and the inability of blind users to verify generated descriptions.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WZMo6QG1j98/hqdefault.jpg)](https://www.youtube.com/watch?v=WZMo6QG1j98)

[Watch on YouTube](https://www.youtube.com/watch?v=WZMo6QG1j98)
