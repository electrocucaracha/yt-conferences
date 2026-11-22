---
layout: default
title: "Keynote - The Marshall Project"
nav_order: 103
parent: PyCon US 2025
type: Video Note
description: "This keynote explores the intersection of data journalism, Python programming, and criminal justice reform through the work of the Marshall Project, a Pulitzer Prize-winning nonprofit newsroom."
resource: "https://www.youtube.com/watch?v=qog-dGVhSBI"
youtube_stats:
  view_count: 718
  like_count: 6
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

This keynote explores the intersection of data journalism, Python programming, and criminal justice reform through the work of the Marshall Project, a Pulitzer Prize-winning nonprofit newsroom.
Speakers Jeff Ping and Tom Mayer, moderated by Dr.
Jackie Kel, discuss how they utilize Python libraries such as Django, Pandas, and Camelot to uncover systemic injustices within the US criminal justice system.
They detail specific investigations, including building a real-time execution tracker and analyzing misconduct data from New York State prisons to reveal that only one in ten accused officers was fired for physical abuse.
The presentation highlights the technical challenges of data journalism, such as cleaning messy government records, managing the lifecycle of news applications, and the difficulty of scaling data collection across thousands of fragmented local jurisdictions.
Finally, the speakers invite the Python community to contribute to journalism by developing tools, fixing bugs in data libraries, and engaging with organizations like the Marshall Project to support high-quality, accessible reporting on critical social issues.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Marshall Project is a Pulitzer Prize-winning nonprofit newsroom dedicated to covering the US criminal justice system through in-depth investigations and data journalism.               |
|   2 | Jeff Ping and Tom Mayer are data reporters and senior editors who use Python, Django, and Pandas to uncover stories about prison conditions, executions, and police accountability.         |
|   3 | Tom Mayer learned Python through a workshop at the NIKAR conference in 2011, which demonstrated that coding was accessible for journalists without formal computer science training.        |
|   4 | The Marshall Project aims to create a sense of national urgency about the criminal justice system by telling complex, contextual stories rather than simplistic crime reports.              |
|   5 | The organization covers the entire justice system, including policing, jails, courts, prisons, and reentry, to identify systemic injustices and unintended consequences.                    |
|   6 | Tom Mayer built an execution tracker using a Django admin interface to manage data from a network of partner news organizations, automating updates via Slack and Twitter.                  |
|   7 | The execution tracker utilized JSON files stored in S3 and a frontend built with D3 and WebGL to visualize real-time execution schedules and case statuses.                                 |
|   8 | A major investigation into New York State prison misconduct involved analyzing approximately 5,600 cases of employee misconduct, including physical and sexual abuse.                       |
|   9 | Analysis of the prison misconduct data revealed that only about one in ten cases of serious physical abuse resulted in the accused officer being fired.                                     |
|  10 | The team used the Python library Camelot to extract data from heavily redacted PDFs and Jupyter notebooks for initial exploration and error identification.                                 |
|  11 | Data cleaning required extensive "shoe leather" reporting, including hundreds of emails and phone calls to resolve missing unique identifiers and misspelled names.                         |
|  12 | The data processing pipeline was refactored from Jupyter notebooks into reproducible scripts managed by a Makefile to ensure reliability and ease of sharing with non-technical colleagues. |
|  13 | The team emphasized the importance of maintaining the humanity of the subjects in data visualizations, using illustrations to remind viewers that each data point represents a person.      |
|  14 | Scaling data journalism to a national level is difficult because the US criminal justice system is highly distributed, with thousands of overlapping local and state systems.               |
|  15 | Inconsistent data reporting from local jurisdictions to federal agencies, such as the FBI, makes it challenging to create a single, consistent national dataset.                            |
|  16 | The team shifted focus from maintaining long-term news apps to conducting data-driven investigations that provide context and evidence for specific stories.                                |
|  17 | When sunsetting the execution tracker after five years, the team analyzed the accumulated data to publish a final story on the delays and lack of finality in capital punishment cases.     |
|  18 | Previously collected data on prison misconduct was revisited to write new stories when related news events occurred, demonstrating the long-term value of processed datasets.               |
|  19 | Current work at the Marshall Project includes investigating the impact of federal grant cuts on local justice systems and analyzing deaths in custody.                                      |
|  20 | The team is also examining how the criminal justice system is used to address social issues like homelessness and poverty, rather than traditional public safety concerns.                  |
|  21 | Python developers can support data journalism by contributing to open-source tools, fixing bugs, and improving documentation for libraries used by newsrooms.                               |
|  22 | Individuals interested in data journalism can join the News Nerdery Slack group or attend the NIKAR conference to connect with practitioners and share ideas.                               |
|  23 | The Marshall Project relies on foundation funding and donations, as it does not charge for subscriptions, to support its investigative work and digital infrastructure.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qog-dGVhSBI/hqdefault.jpg)](https://www.youtube.com/watch?v=qog-dGVhSBI)

[Watch on YouTube](https://www.youtube.com/watch?v=qog-dGVhSBI)
