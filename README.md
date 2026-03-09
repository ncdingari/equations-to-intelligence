# Equations to Intelligence

A Reveal.js-based presentation that connects math and physics concepts to practical AI engineering.

## Project layout

- `index.html` — Presentation runtime, styling, and canvas/WebGL animations.
- `slides.md` — Slide content (markdown + embedded HTML hooks).
- `images/` — Local image assets used by slides.
- `data/` — Supporting data and exported HTML widgets.
- `quickstart.md` — Fast local run instructions.
- `download_logos.py` — Utility script for downloading institution/company logos.
- `update_slides.py` — Utility script intended for targeted ancestry-block updates.

## Run locally

Serve the folder with any static file server (for example Python's built-in server), then open the local URL in your browser.

For a step-by-step, see `quickstart.md`.

## Authoring notes

- Keep slide content changes in `slides.md`.
- Keep animation/runtime changes in `index.html`.
- Prefer local assets from `images/` for reliability in offline or conference environments.

## Deployment

GitHub Pages deployment is configured in `.github/workflows/static.yml` and publishes on pushes to `main`.