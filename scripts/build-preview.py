"""Create a browser-openable review copy without publishing the website."""

from base64 import b64encode
from pathlib import Path

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
css = (root / 'assets/site.css').read_text()
js = (root / 'assets/site.js').read_text()
image = b64encode((root / 'assets/folded-paper.png').read_bytes()).decode('ascii')

assert '</style' not in css.lower()
assert '</script' not in js.lower()
html = html.replace('<link rel="stylesheet" href="assets/site.css">', f'<style>\n{css}\n</style>')
html = html.replace('src="assets/folded-paper.png"', f'src="data:image/png;base64,{image}"')
html = html.replace('<script src="assets/site.js" defer></script>', f'<script>\n{js}\n</script>')
html = html.replace('<meta name="author"', '<meta name="robots" content="noindex,nofollow">\n<meta name="author"', 1)

output = root / 'review/Aldrich-FYI-preview.html'
output.parent.mkdir(exist_ok=True)
output.write_text(html)
print(f'Created {output} ({output.stat().st_size:,} bytes)')
