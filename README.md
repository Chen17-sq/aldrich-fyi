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

The fifth review revision keeps the approved masthead and editorial layout, and gives each tool a distinct, clickable cover: an abstract newspaper for Kickstarter China Tracker, a waveform and editing lines for clearscript, and a connected memory graph for OpenPersona. These are decorative illustrations of their purpose, not product screenshots or real data. Each has a brief, one-time entrance gesture and a restrained hover/focus response. Desktop firm labels stay in view while reading their entries; a thin line tracks progress through the article. The closing email link has its own prominent row.

The larger chapter titles, distinct investment/execution hierarchy, embedded fonts and Chinese spacing from revision four are retained. Company dates, roles, descriptions and groupings come from the original website, not the generated art-direction mockup. Portfolio lift, icon inversion and one-time content entrances remain, with reduced-motion support.

Design reference: [mono-color-skill](https://github.com/yanliudesign/mono-color-skill). The folded-paper illustration was generated for this site from the approved visual concept.

## Files

- `index.html` — content and semantic structure.
- `assets/fonts.css` and `assets/fonts/` — local variable fonts, source records and licenses.
- `assets/site.css` — typography, layout, responsive behavior and motion.
- `assets/content.css` — lower-page backgrounds, portfolio interactions and section entrances.
- `assets/site.js` — translations, navigation state and small interactions.
- `assets/folded-paper.png` — transparent decorative illustration.

The website has no build step. Open `index.html` in a browser, or serve this directory with any static HTTP server. Bodoni Moda and Inter are served locally; the review copy embeds both fonts and their licenses for offline use. Chinese uses explicit Simplified and Traditional system-font fallbacks.

For a single-file review copy with the artwork, CSS and JavaScript embedded:

```sh
python3 scripts/build-preview.py
```

Open `review/Aldrich-FYI-preview.html` in a browser, or send the accompanying `review/Aldrich-FYI-preview.zip`. Generated review files are ignored by Git. Their content comes directly from the website source.

## Validation

Source checks confirm the original 56 translation entries, 24 portfolio entries, three tools and all external links are preserved. Four-language switching works with unavailable browser storage. JavaScript syntax, anchor targets and asset references pass. Motion checks cover one-time entry, changed reduced-motion preferences, cleanup and unavailable observers. Browser visual review is still pending because local HTTP binding and browser automation are unavailable in this session.

Font checks from revision four verify the original source Git blob hashes, WOFF2 round trips and coverage of all 57 Latin characters used in the English/French translations; those font assets are unchanged. Revision five checks cover named project links, decorative SVG references, embedded resources and ZIP integrity. Reading-progress logic is checked at the article start, midpoint and page end, with changed content/viewport geometry, overscroll, reduced motion and a single shared animation-frame scheduler. These are source and logic checks, not browser screenshot measurements.

## Hosting

Cloudflare Pages serves this static repository. Production follows `main`; the design branch has not been published. See `DEPLOY.md` for the existing hosting configuration.
