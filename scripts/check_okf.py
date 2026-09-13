#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click>=8.1",
#     "python-frontmatter>=1.1",
# ]
# ///
"""
Validate the OKF v0.2 knowledge bundle for structural compliance.

This checker verifies:
  - Bundle has a root index.md with okf_version: "0.2" frontmatter
  - Every directory has an index.md (for progressive disclosure navigation)
  - Every concept document has valid YAML frontmatter
  - Every concept has a 'type' field in frontmatter
  - Every concept has required sections: # Summary, # Main Points, # Video
  - Main Points are structured as Markdown tables

Run as: make check

Exit code: 0 if all checks pass, 1 if any fail.
"""

import re
from pathlib import Path

import click
import frontmatter


ROOT = Path(__file__).resolve().parents[1] / "docs"


def validate_bundle(root: Path) -> list[str]:
    """
    Return structural validation errors for an OKF documentation bundle.

    Validates that the bundle conforms to OKF v0.2 structure:
    - Root contains index.md with okf_version: "0.2" frontmatter
    - Every subdirectory contains index.md for navigation
    - Every concept document (.md, excluding index.md and log.md) has:
      * Valid YAML frontmatter (delimited by ---)
      * Non-empty 'type' field in metadata
      * Required sections: # Summary, # Main Points, # Video
      * Main Points formatted as a Markdown table

    Args:
        root: Path to the OKF bundle root directory (containing docs/)

    Returns:
        list[str]: Empty list if valid; list of error messages otherwise.
                   Each error message is prefixed with the file path.

    Examples:
        >>> import tempfile
        >>> from pathlib import Path
        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     root = Path(tmpdir)
        ...     # Missing root index.md
        ...     errors = validate_bundle(root)
        ...     len(errors) > 0 and "missing bundle root index.md" in errors[0]
        True

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     root = Path(tmpdir)
        ...     # Create valid root index with OKF version
        ...     (root / "index.md").write_text('okf_version: "0.2"\n')
        ...     errors = validate_bundle(root)
        ...     # Now only checks for subdirectories, no root error
        ...     not any("missing bundle root index.md" in e for e in errors)
        True

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     root = Path(tmpdir)
        ...     (root / "index.md").write_text('okf_version: "0.2"\n')
        ...     subdir = root / "topics"
        ...     subdir.mkdir()
        ...     errors = validate_bundle(root)
        ...     # Missing index.md in subdirectory
        ...     any("missing directory index.md" in e for e in errors)
        True
    """
    errors: list[str] = []
    index_path = root / "index.md"
    if not index_path.is_file():
        errors.append(f"{root}: missing bundle root index.md")
    elif 'okf_version: "0.2"' not in index_path.read_text(encoding="utf-8"):
        errors.append(f"{index_path}: missing okf_version 0.2")

    directories = sorted(path for path in root.rglob("*") if path.is_dir() and "assets" not in path.parts)
    for directory in directories:
        if not (directory / "index.md").is_file():
            errors.append(f"{directory}: missing directory index.md")

    for path in sorted(root.rglob("*.md")):
        if path.name in {"index.md", "log.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path}: missing YAML frontmatter")
            continue
        end = text.find("\n---", 4)
        if end == -1:
            errors.append(f"{path}: unterminated YAML frontmatter")
            continue
        document = frontmatter.loads(text)
        if not document.metadata.get("type"):
            errors.append(f"{path}: missing non-empty type")
        body = document.content
        required_sections = ["# Summary", "# Main Points", "# Video"]
        missing_sections = [section for section in required_sections if section not in body]
        if missing_sections:
            errors.append(f"{path}: missing sections: {', '.join(missing_sections)}")
        if not re.search(r"^\|\s*#\s*\|\s*Main point\s*\|$", body, re.MULTILINE) or not re.search(r"^\|\s*:?-+:\s*\|\s*-+\s*\|$", body, re.MULTILINE):
            errors.append(f"{path}: Main Points must be a Markdown table")
    return errors


@click.command()
@click.option("--root", type=click.Path(path_type=Path), default=ROOT, show_default=True)
def main(root: Path) -> None:
    """Validate the bundle and exit with a failure status when invalid."""
    errors = validate_bundle(root)
    if errors:
        click.echo("OKF check failed:")
        click.echo("\n".join(errors))
        raise click.exceptions.Exit(1)

    concepts = sum(1 for path in root.rglob("*.md") if path.name not in {"index.md", "log.md"})
    click.echo(f"OKF v0.2 check passed: {concepts} concept documents")


if __name__ == "__main__":
    main()