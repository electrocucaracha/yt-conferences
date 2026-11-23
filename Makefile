# SPDX-license-identifier: Apache-2.0
##############################################################################
# Copyright (c) 2026
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

SUMMARIZER_SOURCE ?= git+https://github.com/electrocucaracha/yt-summarizer.git@561994d3fba4016a5b774e0b0660028d3cd66e80
COLLECTION ?=
PORT ?= 8099
QMD_COLLECTION ?= yt-conferences
.PHONY: install summarize summarize-dry-run fmt check validate build preview qmd-setup qmd-update qmd-embed qmd-check qmd-mcp clean cleanup lint update-versions template-check template-diff template-update
DOCKER_CMD ?= $(shell which docker 2> /dev/null || which podman 2> /dev/null || echo docker)
TOOLS := uv run --no-project --python 3.12 --with-requirements requirements-dev.txt

install:
	uv tool install --python 3.12 "$(SUMMARIZER_SOURCE)"
	uv tool install cruft==2.16.0

summarize:
	python3 scripts/summarize.py $(if $(COLLECTION),--collection "$(COLLECTION)")

summarize-dry-run:
	python3 scripts/summarize.py --dry-run $(if $(COLLECTION),--collection "$(COLLECTION)")

cleanup:
	rm -rf node_modules

lint:
	$(TOOLS) black --check --config pyproject.toml scripts
	$(TOOLS) isort --check-only --settings-path pyproject.toml scripts
	$(TOOLS) ruff check --config pyproject.toml scripts
	$(TOOLS) pylint --rcfile pyproject.toml scripts
	$(TOOLS) mypy --config-file pyproject.toml scripts
	$(TOOLS) bandit --recursive --severity-level medium --confidence-level medium scripts

fmt: cleanup
	command -v textlint > /dev/null && npm list --global --depth=0 textlint-rule-terminology > /dev/null 2>&1 || sudo npm install --global textlint textlint-rule-terminology
	textlint . --fix
	command -v shfmt > /dev/null || curl -s "https://i.jpillora.com/mvdan/sh!!?as=shfmt" | bash
	shfmt -l -w -s .
	command -v yamlfmt > /dev/null || curl -s "https://i.jpillora.com/google/yamlfmt!!" | bash
	yamlfmt -dstar **/*.{yaml,yml}
	command -v prettier > /dev/null || npm install prettier
	npx prettier . --write > /dev/null 2>&1
	uvx ruff format .
	uvx black .
	uvx isort .
	uv run --script scripts/format_okf.py

check:
	bash scripts/run_kiso.sh check

validate: check
	@destination=$$(mktemp -d) && \
		trap 'rm -rf "$$destination"' EXIT && \
		bash scripts/run_kiso.sh build --destination="$$destination"

build:
	bash scripts/run_kiso.sh build --destination=public
	python3 scripts/style_site.py public

preview: PORT ?= 8099
preview:
	bash scripts/run_kiso.sh build --destination=public --profile local
	python3 scripts/style_site.py public
	python3 -m http.server $(PORT) --directory public

qmd-setup: fmt
	QMD_COLLECTION="$(QMD_COLLECTION)" bash scripts/configure_qmd.sh

update-versions:
	bash ci/update_versions.sh

qmd-update:
	QMD_FORCE_CPU=1 qmd update

qmd-embed:
	QMD_FORCE_CPU=1 qmd embed -c yt-conferences

qmd-check:
	QMD_FORCE_CPU=1 qmd status
	QMD_FORCE_CPU=1 qmd ls yt-conferences

qmd-mcp:
	QMD_FORCE_CPU=1 qmd mcp

template-check:
	uv run --no-project --python 3.12 --with-requirements requirements-dev.txt cruft check

template-diff:
	uv run --no-project --python 3.12 --with-requirements requirements-dev.txt cruft diff

template-update:
	uv run --no-project --python 3.12 --with-requirements requirements-dev.txt cruft update --skip-apply-ask

