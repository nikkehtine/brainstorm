#!/usr/bin/env -S just --justfile

set windows-shell := ["pwsh", "-NoLogo", "-NoProfileLoadTime", "-Command"]

default:
    @just --list

# Development

[group("dev")]
client:
    cd client && pnpm dev

[group("dev")]
server:
    uv run flask --app main run

# Linting and formatting

[group("fmt")]
lint-server:
    uv run ruff check . && uv run ruff format .

[group("fmt")]
lint-client:
    cd client && pnpm lint

[group("fmt")]
lint: lint-server lint-client

[group("fmt")]
format-server:
    uv run ruff format .

[group("fmt")]
format-client:
    cd client && pnpm format

[group("fmt")]
format: format-server format-client

# Miscellaneous

[group("housekeeping")]
clean:
    rm -rf dist
    rm -rf client/dist
    rm -rf .venv
    rm -rf __pycache__

[group("housekeeping")]
versions:
    @echo "Python: $(uv run python --version)"
    @echo "Node:   $(node --version)"
    @echo "pnpm:   $(pnpm --version)"
    @echo "uv:     $(uv --version)"

[group("housekeeping")]
install:
    uv sync
    cd client && pnpm i
