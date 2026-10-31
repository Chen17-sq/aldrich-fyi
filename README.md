# Aldrich FYI

The personal website of **Aldrich Chen / 陈思蕲** — Tech Investor at Hillhouse Investment.

Production: https://aldrich.fyi

## Design preview

The `design/mono-color-20261031` branch implements the approved blue-and-terracotta folded-paper direction. **This is a review version; do not push to the production branch or deploy until Aldrich explicitly confirms it.**

- Bodoni Moda display type and Inter text on a neutral-white canvas.
- Cobalt `#2148B8`, terracotta `#C65F38`, paper `#FAFAF7`.
- A single illustrated cover, a section index, and open portfolio and tool layouts.
- All 24 portfolio entries, three tools, contact links, and four original languages retained.
- Brief entrance transitions and restrained paper movement; reduced-motion preferences respected.

The second review revision restores portfolio-card lift and icon inversion, tool-link feedback and the editor-note entrance. Content enters once while scrolling without depending on JavaScript for visibility. Lower-page backgrounds vary between pale-blue grid paper, warm paper and a cobalt footer, with a decorative Beijing–Shenzhen route and restrained halftone accents.

Design reference: [mono-color-skill](https://github.com/yanliudesign/mono-color-skill). The folded-paper illustration was generated for this site from the approved visual concept.

## Files

- `index.html` — content and semantic structure.
- `assets/site.css` — typography, layout, responsive behavior and motion.
- `assets/content.css` — lower-page backgrounds, portfolio interactions and section entrances.
- `assets/site.js` — translations, navigation state and small interactions.
- `assets/folded-paper.png` — transparent decorative illustration.

The website has no build step. Open `index.html` in a browser, or serve this directory with any static HTTP server. Web fonts load from Google Fonts, with system fallbacks if unavailable.

For a single-file review copy with the artwork, CSS and JavaScript embedded:

```sh
python3 scripts/build-preview.py
```

Open `review/Aldrich-FYI-preview.html` in a browser, or send the accompanying `review/Aldrich-FYI-preview.zip`. Generated review files are ignored by Git. Their content comes directly from the website source.

## Validation

Source checks confirm the original 56 translation entries, 24 portfolio entries, three tools and all external links are preserved. Four-language switching works with unavailable browser storage. JavaScript syntax, anchor targets and asset references pass. Motion checks cover one-time entry, changed reduced-motion preferences, cleanup and unavailable observers. Browser visual review is still pending because local HTTP binding and browser automation are unavailable in this session.

## Hosting

Cloudflare Pages serves this static repository. Production follows `main`; the design branch has not been published. See `DEPLOY.md` for the existing hosting configuration.
