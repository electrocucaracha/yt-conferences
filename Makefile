.PHONY: fmt check qmd-setup qmd-update qmd-embed qmd-check qmd-mcp clean

fmt:
	uvx ruff format .
	uvx black .
	uvx isort .
	uv run --script scripts/format_okf.py
	npx --yes prettier "docs/**/*.md" --write

check:
	uv run --script scripts/check_okf.py

qmd-setup: format
	bash scripts/configure_qmd.sh

qmd-update:
	QMD_FORCE_CPU=1 qmd update

qmd-embed:
	QMD_FORCE_CPU=1 qmd embed -c yt-conferences

qmd-check:
	QMD_FORCE_CPU=1 qmd status
	QMD_FORCE_CPU=1 qmd ls yt-conferences

qmd-mcp:
	QMD_FORCE_CPU=1 qmd mcp

clean:
	rm -rf docs