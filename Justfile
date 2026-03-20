#!/usr/bin/env -S just --justfile

set windows-shell := ["pwsh", "-NoLogo", "-NoProfileLoadTime", "-Command"]

default:
    @just --list

# Development

[group("dev")]
client:
    cd frontend && pnpm dev

[group("dev")]
server:
    uv run flask --app main run

# Linting and formatting

[group("fmt")]
lint-server:
    uv run ruff check . && uv run ruff format .

[group("fmt")]
lint-client:
    cd frontend && pnpm lint

[group("fmt")]
lint: lint-server lint-client

[group("fmt")]
format-server:
    uv run ruff format .

[group("fmt")]
format-client:
    cd frontend && pnpm format

[group("fmt")]
format: format-server format-client

# Miscellaneous

[group("housekeeping")]
clean:
    rm -rf dist
    rm -rf frontend/dist
    rm -rf .venv
    rm -rf __pycache__

[group("housekeeping")]
versions:
    @echo "Python: $(uv run python --version)"
    @echo "Node:   $(node --version)"
    @echo "pnpm:   $(pnpm --version)"
    @echo "uv:     $(uv --version)"
