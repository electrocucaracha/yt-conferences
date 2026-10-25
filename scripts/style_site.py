"""Style a Kiso site, embed videos, and publish downloads and an LLM guide."""

import argparse
import json
import re
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

MARKER = "\n/* Conference Knowledge stylesheet */\n"
VIDEO_THUMBNAIL = re.compile(
    r'<a href="https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})">'
    r'<img src="https://img\.youtube\.com/vi/\1/hqdefault\.jpg"'
    r' alt="Video thumbnail"></a>'
)
PAGE_NAVIGATION = re.compile(
    r'\n<nav class="kiso-page-navigation".*?</nav>\n', re.DOTALL
)


class CollectionLinksParser(HTMLParser):
    """Read unique local page links in collection content order."""

    def __init__(self) -> None:
        super().__init__()
        self.links: dict[str, str] = {}
        self.in_article = False
        self.href = ""
        self.title: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "article":
            self.in_article = "kiso-content" in (attributes.get("class") or "").split()
        if tag == "a" and self.in_article:
            href = attributes.get("href") or ""
            if (
                href.endswith(".html")
                and Path(href).name == href
                and href != "index.html"
            ):
                self.href = href
                self.title = []

    def handle_data(self, data: str) -> None:
        if self.href:
            self.title.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self.href:
            self.links.setdefault(self.href, "".join(self.title).strip())
            self.href = ""
        if tag == "article":
            self.in_article = False


def collection_navigation(destination: Path) -> dict[Path, str]:
    """Build previous/next navigation following each collection index."""
    navigation: dict[Path, str] = {}
    for index in destination.glob("*/index.html"):
        parser = CollectionLinksParser()
        parser.feed(index.read_text(encoding="utf-8"))
        links = list(parser.links.items())
        for position, (filename, _) in enumerate(links):
            items = []
            if position > 0:
                href, title = links[position - 1]
                items.append(
                    f'<a rel="prev" href="{escape(href, quote=True)}">'
                    f"<span>Previous</span>{escape(title)}</a>"
                )
            items.append('<a href="index.html">Back to collection</a>')
            if position + 1 < len(links):
                href, title = links[position + 1]
                items.append(
                    f'<a rel="next" href="{escape(href, quote=True)}">'
                    f"<span>Next</span>{escape(title)}</a>"
                )
            navigation[index.parent / filename] = (
                '\n<nav class="kiso-page-navigation" aria-label="Talk navigation">'
                + "".join(items)
                + "</nav>\n"
            )
    return navigation


def embed_videos(html: str) -> str:
    """Replace generated YouTube thumbnails with privacy-enhanced players."""
    return VIDEO_THUMBNAIL.sub(
        r'<iframe class="kiso-video"'
        r' src="https://www.youtube-nocookie.com/embed/\1"'
        r' title="YouTube video player" loading="lazy"'
        r' allow="encrypted-media; fullscreen; picture-in-picture"'
        r' referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>'
        r"</iframe>",
        html,
    )


class MarkdownDownloadParser(HTMLParser):
    """Find Markdown links and the site's LLM guide URL."""

    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()
        self.llms_url = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "link" and attributes.get("rel") == "describedby":
            self.llms_url = attributes.get("href") or ""
        if (
            tag == "a"
            and "download" not in attributes
            and "font-mono" in (attributes.get("class") or "").split()
            and (attributes.get("href") or "").endswith(".md")
        ):
            start_tag = self.get_starttag_text()
            assert start_tag is not None
            self.links.add(start_tag)


def write_llms(destination: Path) -> None:
    """Generate the LLM guide from the site's collection indexes."""
    html_parser = MarkdownDownloadParser()
    html_parser.feed((destination / "index.html").read_text(encoding="utf-8"))
    documents = json.loads(
        (destination / "search-index.json").read_text(encoding="utf-8")
    )["documents"]
    collections = sorted({Path(document["url"]).parent for document in documents})
    lines = [
        "# YouTube Conference Knowledge",
        "",
        "> AI-generated notes from technology conferences and courses, covering",
        "> Kubernetes, cloud-native computing, AI, developer productivity, and leadership.",
        "",
        "Start with a collection index, then follow its links to individual talk notes.",
        "Prefer the Markdown versions: replace .html with .md, or append index.md",
        "to a directory URL. HTML pages also advertise Markdown with rel=alternate",
        "and this guide with rel=describedby.",
        "",
        "Notes are generated from video transcripts and may contain errors.",
        "Use each note's original recording link to verify claims and attribution.",
        "",
        "## Start Here",
        "",
        (
            f"- [Collection index]({urljoin(html_parser.llms_url, 'index.md')}): "
            "Browse all conferences and topics."
        ),
        "",
        "## Collections",
        "",
    ]
    for collection in collections:
        index = collection / "index.md"
        if collection == Path(".") or not (destination / index).is_file():
            continue
        title = next(
            line[2:]
            for line in (destination / index).read_text(encoding="utf-8").splitlines()
            if line.startswith("# ")
        )
        title = title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
        lines.append(
            f"- [{title}]({urljoin(html_parser.llms_url, index.as_posix())}): "
            "Overview and links to individual talk notes."
        )
    lines.extend(
        [
            "",
            "## Optional",
            "",
            (
                f"- [Change log]({urljoin(html_parser.llms_url, 'log.md')}): "
                "Collection update history."
            ),
            "",
        ]
    )
    (destination / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def style_site(destination: Path) -> None:
    """Apply site styles, video players, and Markdown download links."""
    stylesheet = destination / "assets" / "css" / "application.css"
    original = stylesheet.read_text(encoding="utf-8").partition(MARKER)[0]
    custom = Path(__file__).with_name("site.css").read_text(encoding="utf-8")
    stylesheet.write_text(original + MARKER + custom, encoding="utf-8")

    navigation = collection_navigation(destination)
    for page in destination.rglob("*.html"):
        original = page.read_text(encoding="utf-8")
        html_parser = MarkdownDownloadParser()
        html_parser.feed(original)
        updated = embed_videos(original)
        updated = PAGE_NAVIGATION.sub("", updated)
        if page in navigation:
            updated = updated.replace("</article>", navigation[page] + "</article>", 1)
        for link in html_parser.links:
            updated = updated.replace(link, f"{link[:-1]} download>")
        if updated != original:
            page.write_text(updated, encoding="utf-8")

    write_llms(destination)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument("destination", type=Path)
    style_site(arg_parser.parse_args().destination)
