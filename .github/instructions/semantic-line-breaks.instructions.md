---
description: "Use Semantic Line Breaks for every Markdown document in this repository."
applyTo: "**/*.md"
---

# Markdown Writing Rules

Follow the [Semantic Line Breaks specification](https://sembr.org).

## Prose

- Put each sentence on its own line.
- Break after an independent clause when punctuation makes the boundary clear.
- Prefer a maximum line length of 80 characters.
- Allow longer lines for URLs, Markdown links, frontmatter, and other markup.
- Preserve the rendered meaning of the document.
- Do not insert hard-break syntax such as trailing spaces or `<br>` elements.
- Keep a hyphenated word on one line.
- Put a blank line before headings, lists, tables, and fenced code blocks.
- Preserve intentional blank lines that separate logical sections.

## Structured Markdown

- Keep each table row on one physical line.
- Keep each list item on one physical line unless it contains a nested block.
- Keep frontmatter keys and values on their own lines.
- Keep fenced code blocks unchanged unless the code itself is being edited.
- Do not apply prose wrapping inside URLs, inline code, or HTML attributes.

## Video Notes

For video-note concepts, use this order after the YAML frontmatter:

1. `# Summary`
2. A concise summary with semantic line breaks.
3. `# Main Points`
4. A Markdown table with one main point per row.
5. `# Video`
6. The YouTube link.
