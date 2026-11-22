---
layout: default
title: "Tutorials - Meagen Voss, Scott Cranfill: How To Build More Accessible Websites with Wagtail"
nav_order: 20
parent: PyCon US 2024
type: Video Note
description: "This workshop, led by Wagtail community manager Megan Voss and core team member Scott Cranfill, guides participants through building an accessible blog using the Wagtail CMS."
resource: "https://www.youtube.com/watch?v=JbeuuHR8qU8"
youtube_stats:
  view_count: 627
  like_count: 5
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

This workshop, led by Wagtail community manager Megan Voss and core team member Scott Cranfill, guides participants through building an accessible blog using the Wagtail CMS.
The session begins with an overview of web accessibility standards, highlighting that 95.9% of top sites fail WCAG 2.0 checks, and emphasizes the legal and moral imperatives for inclusive design.
Participants set up a local development environment, create a basic blog structure using Django models and templates, and implement custom image models to properly handle alt text and decorative images.
The tutorial then focuses on leveraging Wagtail’s built-in accessibility checker and custom validation logic to prevent common errors, such as incorrect heading hierarchies and missing alt text, directly within the content editor interface.
Finally, the presenters demonstrate various automated testing tools, including Axe DevTools, Accessibility Insights, and WAVE, while stressing the critical importance of manual testing with screen readers and keyboard navigation to ensure a fully accessible user experience.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Web accessibility is critical as 95.9% of top sites fail WCAG 2.0 standards, leading to legal risks and exclusion of users with disabilities.            |
|   2 | Common accessibility issues include low contrast, missing alt text, missing form labels, empty links, and lack of keyboard navigation support.           |
|   3 | The W3C Web Content Accessibility Guidelines (WCAG) 2.2 are the primary standard to follow, with WCAG 3.0 currently in development.                      |
|   4 | Accessibility is a shared responsibility for developers, content editors, and infrastructure teams, requiring collaboration to ensure compliance.        |
|   5 | Wagtail is a content management system built on Django that provides an intuitive interface for editors and built-in accessibility tools.                |
|   6 | Setting up a Wagtail project involves creating a virtual environment, installing dependencies, and using a starter template to save time.                |
|   7 | Custom models should be defined early in the project to avoid complex database migration issues when adding fields like alt text later.                  |
|   8 | Wagtail’s default image model uses the title as alt text, which is often unhelpful; a custom image model with a dedicated alt text field is recommended. |
|   9 | The Wagtail Accessibility Checker, powered by the axe engine, helps editors identify issues like empty headings and missing landmarks.                   |
|  10 | Developers can enable full error reporting for admin users via Wagtail hooks to address code-level accessibility problems.                               |
|  11 | Semantic HTML elements like header and main should be used instead of divs to provide proper landmarks for screen readers.                               |
|  12 | Incorrect heading hierarchy, such as skipping levels, breaks document structure for assistive technologies and should be avoided.                        |
|  13 | Custom validation in Wagtail stream fields can prevent editors from saving pages with incorrect heading levels by overriding the clean method.           |
|  14 | Alt text should describe the image’s purpose for screen reader users, while decorative images should have an empty alt attribute.                        |
|  15 | A custom image block can include alt text and decorative checkboxes to provide context-specific alternatives for images in stream fields.                |
|  16 | Validation logic can prevent conflicting inputs, such as marking an image as decorative while also providing alt text.                                   |
|  17 | Help text in Wagtail fields can guide editors on writing effective alt text and maintaining proper heading structures.                                   |
|  18 | Help panels can provide page-level guidance for specific content types, such as image galleries, to ensure consistent accessibility practices.           |
|  19 | Automated testing tools like axe DevTools, Accessibility Insights, IBM Equal Access, and WAVE offer different perspectives on accessibility issues.      |
|  20 | Manual testing with keyboard navigation, screen readers, and speech recognition is essential to catch issues that automated tools miss.                  |
|  21 | Accessibility audits should track findings by severity and effort to prioritize fixes, using tools like spreadsheets or GitHub projects.                 |
|  22 | Continuous evaluation and integration of accessibility checks into CI/CD pipelines help maintain standards over time.                                    |
|  23 | Resources like the Wagtail Bakery Demo, extended tutorials, and the A11Y Project provide further guidance for implementing accessible sites.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/JbeuuHR8qU8/hqdefault.jpg)](https://www.youtube.com/watch?v=JbeuuHR8qU8)

[Watch on YouTube](https://www.youtube.com/watch?v=JbeuuHR8qU8)
