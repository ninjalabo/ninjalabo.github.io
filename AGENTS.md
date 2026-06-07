# Repository Guidelines

## Project Structure & Module Organization

This repository is a Quarto website for NinjaLABO. Root `.qmd` files such as `index.qmd`, `getstarted.qmd`, `pricing.qmd`, and `blog.qmd` define top-level pages. `_quarto.yml` controls navigation, metadata, theme selection, and publishing. Blog posts live in `blogs/`; tutorials live in `tutorials/`; TinyMLaaS documentation and notebooks live in `docs/tinymlaas/`. Shared assets are in `images/`, while post-specific assets usually sit under `blogs/images/` or `docs/tinymlaas/images/`. `performance.ipynb` and `benchmark.csv` drive the performance comparison content.

## Build, Test, and Development Commands

- `quarto preview`: run the site locally with live reload.
- `quarto render`: render the full static site and catch Quarto, Markdown, and notebook integration issues.
- `python -m pip install jupyter pandas matplotlib plotly kaleido`: install the Python packages used by the publishing workflows.
- `jupyter nbconvert --execute performance.ipynb --to notebook --output performance.ipynb`: refresh the performance notebook before publishing changes that touch `benchmark.csv` or generated charts.

GitHub Actions publishes from `main` to `gh-pages` and regenerates performance images when `performance.ipynb` or `benchmark.csv` changes.

## Coding Style & Naming Conventions

Use Quarto Markdown for pages and keep YAML front matter valid and minimal. Prefer lowercase, hyphenated filenames for new `.qmd` pages, for example `edge-ai-guide.qmd`. Keep asset paths relative and store new images near the content that uses them. Use 2-space indentation in YAML blocks and nested Markdown lists. Keep CSS edits focused in `styles.css` or `custom.scss`.

## Testing Guidelines

There is no dedicated unit test suite. Treat `quarto render` as the primary validation step. For notebook or benchmark changes, execute `performance.ipynb` and inspect generated figures. For content changes, verify links, images, dates, categories, and rendered headings in the local preview.

## Commit & Pull Request Guidelines

Recent history uses short, imperative commit messages such as `add PyTorch setup blog`, `fix publish date`, and `reformat image eb1 to fix rendering pipeline`. Follow that style and keep each commit focused. Pull requests should include a concise description, linked issue when applicable, affected pages or posts, and screenshots for visual layout changes. Note any notebook execution or generated image updates in the PR description.

## Security & Configuration Tips

Do not commit secrets, API keys, private customer data, or unpublished credentials. Keep analytics, domain, and publishing configuration changes in `_quarto.yml`, `CNAME`, or GitHub Actions workflows, and call them out explicitly in the PR.
