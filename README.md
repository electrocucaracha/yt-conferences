# YouTube Conference Knowledge

<!-- markdown-link-check-disable-next-line -->

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Super-Linter](https://github.com/electrocucaracha/yt-conferences/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<!-- markdown-link-check-disable-next-line -->

![visitors](https://visitor-badge.laobi.icu/badge?page_id=electrocucaracha.yt-conferences)
[![Scc Code Badge](https://sloc.xyz/github/electrocucaracha/yt-conferences?category=code)](https://github.com/boyter/scc/)
[![Scc COCOMO Badge](https://sloc.xyz/github/electrocucaracha/yt-conferences?category=cocomo)](https://github.com/boyter/scc/)

## Overview

YouTube Conference Knowledge is a curated, searchable collection of notes from
technology conference videos.

It turns long-form talks into durable technical knowledge by capturing the
ideas, explanations, examples, and lessons that are most useful after the
video ends.
The collection brings together perspectives from conference speakers across
cloud-native computing, Kubernetes, artificial intelligence, developer
productivity, engineering leadership, and related areas.

The information is produced by
[`yt-summarizer`](https://github.com/electrocucaracha/yt-summarizer), an
application that fetches conference videos uploaded to YouTube, retrieves their
transcripts, and uses a large language model to generate summaries and extract key
points.
This project organizes that generated information into a durable knowledge base
that is easier to browse, search, and reuse.

The notes are organized as a structured, machine-readable knowledge base using
[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md).
The canonical collection lives in [`docs/`](docs/index.md), where content is
grouped into navigable conference and subject areas.
This structure supports both broad exploration by topic and focused reading of
an individual talk.

## What This Offers

- **Curated learning**: Explore concise notes from talks about Kubernetes,
  cloud-native platforms, artificial intelligence, developer productivity,
  leadership, and other areas of modern technology.
- **Efficient understanding**: Read a short summary and key takeaways before
  deciding whether a full talk is relevant to your work or interests.
- **Structured knowledge**: Use consistent notes that combine descriptive
  metadata, a summary, key takeaways, the original video, and its transcript.
- **Progressive discovery**: Move from the collection index to a subject or
  conference directory, then to an individual talk without losing context.
- **Semantic search**: Find related ideas by meaning and intent, not only by
  exact keyword matches.
- **Knowledge reuse**: Return to the collection as a reference for research,
  technical discussions, writing, planning, and continued learning.
- **Machine-readable content**: Build on a consistent format that makes the
  knowledge base suitable for indexing, automation, and future integrations.
