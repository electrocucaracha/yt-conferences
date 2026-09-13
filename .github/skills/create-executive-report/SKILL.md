---
name: create-executive-report
description: "Generates an executive summary of a conference by analyzing talk notes using the QMD knowledge engine and writing a README.md file in the conference folder. Use when asked to generate an executive report, executive summary, or README for a conference."
argument-hint: "<conference-folder-path>"
user-invocable: true
---

# Create Executive Report

Generates an executive summary of a conference by querying and retrieving talk notes via the QMD MCP server tools in the specified conference directory, then synthesizing a comprehensive `README.md` report in the same directory.

## When to Use

- When requested to summarize or create an executive report for a conference folder.
- When generating high-level executive summaries across all presentations in a conference.
- Triggered by `/create-executive-report` or phrases like "generate executive report for `folder`", "summarize conference `folder`", or "create readme for conference".

## Input Argument

- `<conference-folder-path>`: Relative or absolute path to the conference directory (e.g., `docs/aie-code-2025-ai-leadership`).

## Step-by-Step Procedure

### 1. Locate and Validate Conference Folder

1. Verify that the specified folder exists in the workspace.
2. Read `index.md` (or retrieve via `mcp_qmd_get`) to understand the conference title, scope, and initial talk listing.

### 2. Gather Talk Content via QMD MCP Tools

Use the QMD MCP server tools to search, batch retrieve, and navigate between knowledge documents in the conference:

1. **Batch Document Retrieval (`mcp_qmd_multi_get`)**:
   - Batch retrieve all talk Markdown files in the conference folder using glob patterns (e.g., `<conference-folder-path>/*.md`).
2. **Targeted Knowledge Querying (`mcp_qmd_query`)**:
   - Run lexical (`lex`) and vector (`vec`) queries over the conference index to discover recurring themes, key takeaways, architectural patterns, and strategic insights across talks.
3. **Single Document Deep-Dive (`mcp_qmd_get`)**:
   - Fetch specific documents or line ranges when deeper context or verification on a talk is needed.
4. Extract key details from each talk:
   - Talk title and speaker.
   - Summary and main points.
   - Strategic insights, architectural patterns, or industry trends.

### 3. Synthesize Executive Summary

Synthesize the aggregated knowledge into the following structured sections:

- **Executive Overview**: High-level summary of the conference theme and goals.
- **Key Themes & Trends**: Core recurring themes, technological shifts, and industry directions discussed across talks.
- **Key Takeaways & Strategic Insights**: Actionable takeaways and strategic implications for developers, leaders, and teams.
- **Sessions & Talks Summary**: A structured table listing key presentations, speakers, document links (e.g. `[path/to/talk.md](path/to/talk.md)`), and their core thesis.

### 4. Generate README.md

Create or update `README.md` in the target conference folder with the synthesized content.

The generated `README.md` MUST include YAML frontmatter with OKF v0.2 and GitHub Pages (Jekyll / Just the Docs) metadata at the top:

```yaml
---
layout: default
title: "Executive Report: <Conference Title>"
parent: "<Conference Title>"
nav_order: 1
type: "Executive Report"
okf_version: "0.2"
description: "Executive report and summary of the <Conference Title> conference."
tags:
  - <conference-folder-name>
  - executive-report
status: stable
---
```

Adhere to the repository's Markdown guidelines (Semantic Line Breaks):

- Place each sentence on its own physical line.
- Separate sections, headings, lists, and tables with empty lines.
- Keep table rows on a single line.

### 5. Confirm Output

1. Verify `README.md` was created in the conference folder.
2. Return a summary of the report to the user along with a link to the generated `README.md`.
