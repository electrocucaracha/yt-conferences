# SPDX-license-identifier: Apache-2.0
##############################################################################
# Copyright (c) 2026
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

.PHONY: fmt check qmd-setup qmd-update qmd-embed qmd-check qmd-mcp clean
DOCKER_CMD ?= $(shell which docker 2> /dev/null || which podman 2> /dev/null || echo docker)

cleanup:
	rm -rf node_modules

fmt: cleanup
	command -v textlint > /dev/null && npm list --global --depth=0 textlint-rule-terminology > /dev/null 2>&1 || sudo npm install --global textlint textlint-rule-terminology
	textlint . --fix
	command -v shfmt > /dev/null || curl -s "https://i.jpillora.com/mvdan/sh!!?as=shfmt" | bash
	shfmt -l -w -s -i 4 .
	command -v yamlfmt > /dev/null || curl -s "https://i.jpillora.com/google/yamlfmt!!" | bash
	yamlfmt -dstar **/*.{yaml,yml}
	command -v prettier > /dev/null || npm install prettier
	npx prettier . --write
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

