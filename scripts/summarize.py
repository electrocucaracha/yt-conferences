"""Validate playlist configuration and invoke the installed summarizer safely."""

import argparse
import shlex
import subprocess
import tomllib
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def commands(config, collection=None):
    """Build argument vectors only after all selected playlists pass validation."""
    playlists = config.get("playlists", {})
    if not isinstance(playlists, dict) or not playlists:
        raise ValueError("Add at least one [playlists.NAME] entry to knowledge.toml")
    if collection is not None and collection not in playlists:
        raise ValueError(f"Unknown collection: {collection}")
    for field in ("model", "api_base", "language"):
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise ValueError(f"{field} must be a non-empty string")
    workers = config.get("workers", 1)
    if isinstance(workers, bool) or not isinstance(workers, int) or workers < 1:
        raise ValueError("workers must be a positive integer")
    selected = playlists if collection is None else {collection: playlists[collection]}
    result = []
    for name, playlist in selected.items():
        url = playlist.get("url") if isinstance(playlist, dict) else None
        if not isinstance(url, str):
            raise ValueError(f"playlists.{name}.url must be a YouTube playlist URL")
        parsed = urlsplit(url)
        if (
            parsed.scheme != "https"
            or parsed.netloc not in {"youtube.com", "www.youtube.com", "m.youtube.com"}
            or parsed.path != "/playlist"
            or not parse_qs(parsed.query).get("list")
        ):
            raise ValueError(
                f"playlists.{name}.url must be an HTTPS YouTube playlist URL"
            )
        result.append(
            [
                "yt_summarizer",
                "--playlist-url",
                url,
                "--output-dir",
                str(ROOT / "docs"),
                "--model",
                config["model"],
                "--api-base",
                config["api_base"],
                "--language",
                config["language"],
                "--workers",
                str(workers),
            ]
        )
    return result


def main():
    """Run selected playlists sequentially, or print their commands for review."""
    parser = argparse.ArgumentParser(
        description="Summarize configured YouTube playlists."
    )
    parser.add_argument(
        "--collection", help="Run only this knowledge.toml playlist entry"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print commands without running them"
    )
    args = parser.parse_args()
    try:
        config = tomllib.loads((ROOT / "knowledge.toml").read_text(encoding="utf-8"))
        planned = commands(config, args.collection)
        for command in planned:
            if args.dry_run:
                print(shlex.join(command))
            else:
                subprocess.run(command, cwd=ROOT, check=True)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
