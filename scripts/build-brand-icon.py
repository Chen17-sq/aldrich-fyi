"""Build the compact FYI browser mark from the site's licensed Inter outlines."""

from pathlib import Path
from xml.sax.saxutils import escape
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

root = Path(__file__).resolve().parents[1]
font = instantiateVariableFont(TTFont(root / 'assets/fonts/Inter.woff2'), {'wght': 650, 'opsz': 14})
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
layout = []
advance = 0
for letter in 'FYI':
    glyph = glyphs[cmap[ord(letter)]]
    layout.append((glyph, advance))
    advance += glyph.width - 30

bounds = BoundsPen(glyphs)
for glyph, x in layout:
    glyph.draw(TransformPen(bounds, (1, 0, 0, 1, x, 0)))
x0, y0, x1, y1 = bounds.bounds
scale = min(48 / (x1 - x0), 24 / (y1 - y0))
left = (64 - (x1 - x0) * scale) / 2 - x0 * scale
baseline = 35 + (y1 + y0) * scale / 2
pen = SVGPathPen(glyphs)
for glyph, x in layout:
    glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, left + x * scale, baseline)))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-labelledby="title">
<title id="title">Aldrich FYI</title>
<metadata>{escape((root / 'assets/fonts/Inter-OFL.txt').read_text())}</metadata>
<path fill="#2148B8" d="M0 0H48L64 16V64H0Z"/>
<path fill="#C65F38" d="M48 0V16H64Z"/>
<path fill="#FAFAF7" d="{pen.getCommands()}"/>
</svg>
'''
output = root / 'assets/favicon.svg'
output.write_text(svg)
print(f'Created {output} ({output.stat().st_size:,} bytes)')
