# Tech conferences

A curated knowledge base from YouTube playlists.

Maintained by Victor Morales.
The canonical knowledge collection lives in [docs/](docs/index.md).

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), Git, and
Python 3.12 or newer. Then run:

```bash
make install
```

The summarizer is installed from the Git revision pinned in the Makefile.
For local development against a sibling checkout, use
`make install SUMMARIZER_SOURCE=../yt-summarizer` instead.
Ensure uv's tool directory is on your `PATH` (`uv tool update-shell`).

The default model uses [Ollama](https://ollama.com/). Start Ollama and pull the
model before generating notes:

```bash
ollama pull llama3.2
```

For other LiteLLM providers, configure the model and endpoint in
[knowledge.toml](knowledge.toml) and export the provider's credentials locally.
Never put credentials in the manifest or generated notes. `.env` files and logs
are ignored because they may contain credentials or sensitive runtime data.

## Generate Notes

Add named public playlists to [knowledge.toml](knowledge.toml):

```toml
[playlists.conference]
url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

Keep the existing `[playlists]` table; append named entries below it.
Model, API base, summary language, and worker count are configured once in the
same manifest. Keep workers at 1 for a local Ollama server.

```bash
make summarize-dry-run
make summarize
make summarize COLLECTION=conference
```

The runner validates the configuration before starting, processes playlists
sequentially, and stops on the first failure. It always passes `--output-dir`
explicitly to select filesystem mode without requiring Notion credentials.
The summarizer creates title-based playlist directories, video notes,
executive summaries, and collection indexes under `docs/`. Manifest names
select playlists; they do not rename the generated directories.

Review the generated content and attribution before committing it. Notes can
contain model errors. Videos without accessible transcripts cannot be processed.
Repeat runs use the summarizer's existing-note handling; this template does not
implement a separate cache or force regeneration.

## Browse and Publish

Install [Kiso CLI v0.2.7](https://github.com/oak-invest/kiso/releases/tag/v0.2.7)
as `kiso` on your `PATH`, then run:

```bash
make check
make preview
```

The local preview is at <http://127.0.0.1:8099>. Override its port with `PORT=8100`.
`make build` writes the static portal to `public/`.

For GitHub Pages, push to
`electrocucaracha/yt-conferences` and choose
**GitHub Actions** as the Pages source in repository settings. The included
workflow publishes on pushes to `main` or manual
dispatch. Pages publishing may make your notes public; verify repository and
organization visibility settings first.

## Local Search

With [QMD](https://github.com/tobi/qmd) installed:

```bash
make qmd-setup
make qmd-update
make qmd-embed
make qmd-check
```

Run setup once per checkout. After notes change, run update and embed again.
Use `make qmd-mcp` to serve the local search index to an MCP client.
QMD defaults to CPU mode to avoid known Metal shutdown issues on macOS;
override with `QMD_FORCE_CPU=0` when appropriate.

## Python Quality Checks

```bash
make lint
make fmt
```

`make lint` checks Python scripts with Black, isort, Ruff, Pylint, mypy, and
Bandit using pinned development tool versions. `make fmt` applies compatible
Black and isort formatting. The Python CI workflow runs the same lint gates on
pushes and pull requests.

Bandit blocks medium-or-higher severity findings with medium-or-higher
confidence. Low-severity findings are informational; no individual rules are
disabled. `make check` remains the separate Kiso knowledge-bundle validation.

## Template Updates

This repository comes from
[yt-summarizer-template](https://github.com/electrocucaracha/yt-summarizer-template).
When generated through Cruft, run these commands from a clean working tree:

```bash
make template-check
make template-diff
make template-update
```

Review and commit the resulting changes. Cruft excludes `docs/` and
`knowledge.toml`, so your notes, indexes, playlists, and local model choices
remain repository-owned. New manifest settings must be adopted manually.
Projects rendered directly with Cookiecutter must first be linked with
`cruft link https://github.com/electrocucaracha/yt-summarizer-template`.