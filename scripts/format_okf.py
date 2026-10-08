#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.1",
# ]
# ///
"""
Normalize OKF concept document formatting for consistency and readability.

This formatter improves:
  - Summary sections: Splits long paragraphs into semantic sentences (one per line)
    for easier diffs, version control tracking, and readability
  - Video sections: Adds a clickable YouTube thumbnail derived from the resource URL
  - Consistent file encoding and trailing whitespace handling

Run as: make fmt (as part of the broader format pipeline)

Modifies files in-place. Safe to run repeatedly.
"""

from __future__ import annotations

import re
from pathlib import Path

import click

ROOT = Path(__file__).resolve().parents[1] / "docs"
VIDEO_ID_PATTERN = re.compile(r"[?&]v=([A-Za-z0-9_-]{11})")
THUMBNAIL_PATTERN = re.compile(r"^\[!\[Video thumbnail\]\(.*\n\n", re.MULTILINE)


def add_video_thumbnail(text: str, frontmatter: str) -> str:
    """
    Return the document with a clickable YouTube thumbnail under '# Video'.

    The thumbnail URL is derived from the video id in the frontmatter 'resource'
    field. Documents without a YouTube resource or without a Video section are
    returned unchanged. Any previously generated thumbnail is replaced, which
    keeps the function idempotent.

    Args:
        text: Full Markdown document content.
        frontmatter: The frontmatter block of the document.

    Returns:
        str: The document content, with the thumbnail inserted when applicable.

    Examples:
        >>> doc = '# Video\\n\\n[Watch on YouTube](https://youtu.be/x)\\n'
        >>> out = add_video_thumbnail(doc, 'resource: https://y.com/watch?v=abcdefghijk\\n')
        >>> 'img.youtube.com/vi/abcdefghijk/hqdefault.jpg' in out
        True
        >>> add_video_thumbnail(out, 'resource: https://y.com/watch?v=abcdefghijk\\n') == out
        True
        >>> add_video_thumbnail(doc, 'type: test\\n') == doc
        True
    """
    resource = re.search(r"^resource: (\S+)\s*$", frontmatter, re.MULTILINE)
    if not resource:
        return text
    video_id = VIDEO_ID_PATTERN.search(resource.group(1))
    if not video_id:
        return text
    thumbnail = (
        f"[![Video thumbnail]"
        f"(https://img.youtube.com/vi/{video_id.group(1)}/hqdefault.jpg)]"
        f"({resource.group(1)})"
    )
    text = THUMBNAIL_PATTERN.sub("", text)
    return re.sub(
        r"^# Video\n\n", f"# Video\n\n{thumbnail}\n\n", text, flags=re.MULTILINE
    )


def format_concept(path: Path) -> None:
    """
    Format the summary section of one OKF concept document in place.

    Processes a single Markdown document to normalize its Summary section:
    - Splits long paragraphs into separate lines at sentence boundaries
      (periods, question marks, exclamation marks)
    - Preserves frontmatter and all other sections unchanged
    - Handles multi-line input by joining and then re-splitting
    - Returns early without changes if document lacks frontmatter or Summary

    The function is idempotent: running it multiple times produces the same result.

    Args:
        path: Path to a Markdown document (.md file)

    Raises:
        No exceptions; silently returns if file cannot be processed.

    Side Effects:
        Modifies the file at `path` in-place with UTF-8 encoding.

    Examples:
        >>> import tempfile
        >>> from pathlib import Path
        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     # Create a document with a multi-sentence summary
        ...     doc_path = Path(tmpdir) / "test.md"
        ...     content = '''---
        ... type: test
        ... ---
        ... # Summary
        ...
        ... This is a long summary. It has multiple sentences. They should be split.
        ...
        ... # Main Points
        ...
        ... | # | Main point |
        ... | --- | --- |
        ... '''
        ...     doc_path.write_text(content)
        ...     format_concept(doc_path)
        ...     result = doc_path.read_text()
        ...     # Verify sentences are now on separate lines
        ...     "This is a long summary.\n" in result
        True

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     # Document without frontmatter should be skipped
        ...     doc_path = Path(tmpdir) / "no_frontmatter.md"
        ...     content = "# Summary\n\nThis is a summary. With sentences.\n"
        ...     doc_path.write_text(content)
        ...     original = doc_path.read_text()
        ...     format_concept(doc_path)
        ...     result = doc_path.read_text()
        ...     # Content unchanged
        ...     original == result
        True

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     # Document without Summary section should be skipped
        ...     doc_path = Path(tmpdir) / "no_summary.md"
        ...     content = '''---
        ... type: test
        ... ---
        ... # Details
        ...
        ... Some content here. With sentences.
        ... '''
        ...     doc_path.write_text(content)
        ...     original = doc_path.read_text()
        ...     format_concept(doc_path)
        ...     result = doc_path.read_text()
        ...     # Content unchanged
        ...     original == result
        True
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return
    end = text.find("\n---", 4)
    if end == -1:
        return
    text = add_video_thumbnail(text, text[4:end])
    end = text.find("\n---", 4)
    body = text[end + 4 :].strip()
    existing_summary = re.search(
        r"^# Summary\s*\n\n(.*?)(?=\n# Main Points)", body, re.MULTILINE | re.DOTALL
    )
    if not existing_summary:
        path.write_text(text, encoding="utf-8")
        return
    summary_lines = [
        sentence.strip()
        for sentence in re.split(
            r"(?<=[.!?])\s+", " ".join(existing_summary.group(1).split())
        )
        if sentence.strip()
    ]
    replacement = "# Summary\n\n" + "\n".join(summary_lines) + "\n\n"
    formatted = (
        text[: end + 4]
        + "\n\n"
        + body[: existing_summary.start()]
        + replacement
        + body[existing_summary.end() :].lstrip()
    ).rstrip() + "\n"
    path.write_text(formatted, encoding="utf-8")


@click.command()
@click.option(
    "--root", type=click.Path(path_type=Path), default=ROOT, show_default=True
)
def main(root: Path = ROOT) -> None:
    """Format all concept documents in the documentation bundle."""
    for concept in sorted(root.rglob("*.md")):
        if concept.name not in {"index.md", "log.md"}:
            format_concept(concept)


if __name__ == "__main__":
    main()
