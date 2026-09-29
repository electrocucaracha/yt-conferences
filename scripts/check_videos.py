#!/usr/bin/env python3
"""
Detect YouTube videos that are no longer available and unlink them from notes.

For every note whose frontmatter 'resource' is a YouTube video, the oEmbed
endpoint is queried several times. When every attempt answers 404, the video
is considered removed: the 'resource' line is moved into an HTML comment and
the '# Video' section is replaced with a notice. Network errors or other statuses never
trigger a removal.

Run as: python3 scripts/check_videos.py [--attempts N] [--delay SECONDS]
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"
UNAVAILABLE_NOTICE = "This video is no longer available on YouTube."
RESOURCE_PATTERN = re.compile(
    r"^resource: (\S*youtube\.com/watch\?v=[A-Za-z0-9_-]{11}\S*)\s*\n", re.MULTILINE
)
VIDEO_SECTION_PATTERN = re.compile(r"^# Video\n.*\Z", re.MULTILINE | re.DOTALL)


def is_removed(url: str, attempts: int, delay: float) -> bool:
    """Return True only when every oEmbed attempt reports the video as missing."""
    endpoint = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(
        url, safe=""
    )
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(endpoint, timeout=30):
                return False
        except urllib.error.HTTPError as error:
            # 401/403 mean embedding is disabled, but the video still exists.
            if error.code != 404:
                return False
        except (urllib.error.URLError, TimeoutError):
            return False
        if attempt < attempts:
            time.sleep(delay * attempt)
    return True


def unlink_video(path: Path, text: str, url: str) -> None:
    """Comment out the resource URL and replace the Video section with a notice."""
    text = RESOURCE_PATTERN.sub("", text, count=1)
    # Link checkers skip HTML comments but not YAML comments in the frontmatter.
    text = VIDEO_SECTION_PATTERN.sub(
        f"# Video\n\n{UNAVAILABLE_NOTICE}\n\n<!-- resource: {url} -->\n", text
    )
    path.write_text(text, encoding="utf-8")


def main() -> int:
    """Scan notes and unlink YouTube videos that are no longer available."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--delay", type=float, default=30.0)
    args = parser.parse_args()

    for note in sorted(args.root.rglob("*.md")):
        text = note.read_text(encoding="utf-8")
        resource = RESOURCE_PATTERN.search(text)
        if resource and is_removed(resource.group(1), args.attempts, args.delay):
            print(f"Unavailable: {resource.group(1)} ({note})", file=sys.stderr)
            unlink_video(note, text, resource.group(1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
