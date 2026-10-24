"""Style a Kiso site, enable Markdown downloads, and publish an LLM guide."""

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

MARKER = "\n/* Conference Knowledge stylesheet */\n"


class MarkdownDownloadParser(HTMLParser):
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
            self.links.add(self.get_starttag_text())


def write_llms(destination: Path) -> None:
    parser = MarkdownDownloadParser()
    parser.feed((destination / "index.html").read_text(encoding="utf-8"))
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
        f"- [Collection index]({urljoin(parser.llms_url, 'index.md')}): Browse all conferences and topics.",
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
            f"- [{title}]({urljoin(parser.llms_url, index.as_posix())}): "
            "Overview and links to individual talk notes."
        )
    lines.extend(
        [
            "",
            "## Optional",
            "",
            f"- [Change log]({urljoin(parser.llms_url, 'log.md')}): Collection update history.",
            "",
        ]
    )
    (destination / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def style_site(destination: Path) -> None:
    stylesheet = destination / "assets" / "css" / "application.css"
    original = stylesheet.read_text(encoding="utf-8").partition(MARKER)[0]
    custom = Path(__file__).with_name("site.css").read_text(encoding="utf-8")
    stylesheet.write_text(original + MARKER + custom, encoding="utf-8")

    for page in destination.rglob("*.html"):
        original = page.read_text(encoding="utf-8")
        parser = MarkdownDownloadParser()
        parser.feed(original)
        updated = original
        for link in parser.links:
            updated = updated.replace(link, f"{link[:-1]} download>")
        if updated != original:
            page.write_text(updated, encoding="utf-8")

    write_llms(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    style_site(parser.parse_args().destination)
