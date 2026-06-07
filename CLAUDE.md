# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Read this first

See **[AGENTS.md](AGENTS.md)** for project structure, build/preview commands, coding style, testing, and PR conventions. It is the primary guide; the notes below add what matters most for an agent.

## Critical: branches

This repo splits two roles across branches:

- **`main`** — the **Quarto source**. Edit here (`.qmd` / `.ipynb`, `_quarto.yml`, `custom.scss`, `benchmark.csv`, images, workflows).
- **`gh-pages`** — **generated build output** (rendered HTML, `site_libs/`, `search.json`), produced by `quarto publish` in CI. **Never hand-edit.** Every push to `main` overwrites this branch, so anything committed here (including this file) is wiped on the next publish.

If you find yourself on `gh-pages`, switch to `main` before making any change.

## Publishing is automated — don't publish manually

Pushing to `main` triggers `.github/workflows/publish.yml`, which executes `performance.ipynb`, renders the site, and deploys to `gh-pages`. Do not run `quarto publish` yourself.

## The one live data path

`benchmark.csv` → `performance.ipynb` → plots in `images/`. `.github/workflows/update_image.yml` re-executes the notebook and commits regenerated `images/` to `main` whenever `performance.ipynb` or `benchmark.csv` changes; the publish workflow re-executes it again at deploy time, so the live performance page always reflects current `benchmark.csv`.
