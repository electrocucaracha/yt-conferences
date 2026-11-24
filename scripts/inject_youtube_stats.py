"""Add YouTube statistics and template styles to a Kiso site build."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "\n/* YouTube knowledge template stylesheet */\n"
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.DOTALL)
STATS_BLOCK = re.compile(
    r"^youtube_stats:[ \t]*\r?\n((?:[ \t]+[^\r\n]*\r?\n?)*)", re.MULTILINE
)
ARTICLE = re.compile(
    r'(<article\b[^>]*\bclass="[^"]*\bkiso-content\b[^"]*"[^>]*>)',
    re.IGNORECASE,
)
METRICS = (
    ("view_count", "Views"),
    ("like_count", "Likes"),
    ("channel_subscriber_count", "Subscribers"),
)


def youtube_stats(markdown: str) -> dict[str, int]:
    """Read known non-negative integer metrics from a note's YAML front matter."""
    frontmatter = FRONTMATTER.match(markdown)
    if frontmatter is None:
        return {}
    block = STATS_BLOCK.search(frontmatter[1])
    if block is None:
        return {}
    values = {
        key: int(value)
        for key, value in re.findall(
            r"^[ \t]+(view_count|like_count|channel_subscriber_count):"
            r"[ \t]*(\d+)[ \t]*$",
            block[1],
            re.MULTILINE,
        )
    }
    return values


def stats_markup(stats: dict[str, int]) -> str:
    """Render available metrics as an accessible definition list."""
    items = "".join(
        f"<div><dt>{label}</dt><dd>{stats[key]:,}</dd></div>"
        for key, label in METRICS
        if key in stats
    )
    return (
        '<dl class="kiso-youtube-stats" aria-label="YouTube statistics">'
        f"{items}</dl>"
    )


def style_site(source: Path, destination: Path) -> None:
    """Add stats from Markdown notes and append the stylesheet to a Kiso build."""
    stylesheet = destination / "assets/css/application.css"
    original = stylesheet.read_text(encoding="utf-8").partition(MARKER)[0]
    custom = (ROOT / "scripts/site.css").read_text(encoding="utf-8")
    stylesheet.write_text(original + MARKER + custom, encoding="utf-8")

    for markdown in source.rglob("*.md"):
        stats = youtube_stats(markdown.read_text(encoding="utf-8"))
        if not stats:
            continue
        page = destination / markdown.relative_to(source).with_suffix(".html")
        html = page.read_text(encoding="utf-8")
        if 'class="kiso-youtube-stats"' in html:
            continue
        markup = stats_markup(stats)
        updated, count = ARTICLE.subn(r"\g<1>" + markup, html, count=1)
        if count != 1:
            raise ValueError(f"Cannot find Kiso content article in {page}")
        page.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="Kiso build output directory")
    style_site(ROOT / "docs", parser.parse_args().destination)
