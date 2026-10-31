"""Create a browser-openable review copy without publishing the website."""

from base64 import b64encode
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
js = (root / 'assets/site.js').read_text()
image = b64encode((root / 'assets/folded-paper.png').read_bytes()).decode('ascii')

assert '</script' not in js.lower()
for stylesheet in ['site.css', 'content.css']:
    css = (root / 'assets' / stylesheet).read_text()
    assert '</style' not in css.lower()
    html = html.replace(f'<link rel="stylesheet" href="assets/{stylesheet}">', f'<style>\n{css}\n</style>')
html = html.replace('src="assets/folded-paper.png"', f'src="data:image/png;base64,{image}"')
html = html.replace('<script src="assets/site.js" defer></script>', f'<script>\n{js}\n</script>')
html = html.replace('<meta name="author"', '<meta name="robots" content="noindex,nofollow">\n<meta name="author"', 1)

output = root / 'review/Aldrich-FYI-preview.html'
output.parent.mkdir(exist_ok=True)
output.write_text(html)
print(f'Created {output} ({output.stat().st_size:,} bytes)')

archive = output.with_suffix('.zip')
with ZipFile(archive, 'w', ZIP_DEFLATED) as package:
    package.write(output, output.name)
    package.writestr('READ-ME.txt',
        'Aldrich FYI — 第二版预览\n\n'
        '解压后，用 Chrome 或 Safari 打开 Aldrich-FYI-preview.html。\n'
        '图片、样式和脚本都已包含在 HTML 中，无需安装。\n'
        '联网时会加载设计字体；离线时使用系统字体。\n\n'
        '本版恢复投资卡片上浮、图标变色和工具链接反馈；加入正文滚动入场、'
        '双城路线装饰、分区背景和蓝色页脚。\n'
        '如系统开启「减少动态效果」，位移动效会关闭。\n\n'
        '此文件仅供确认设计，aldrich.fyi 线上未更新。\n')
with ZipFile(archive) as package:
    assert package.testzip() is None
print(f'Created {archive} ({archive.stat().st_size:,} bytes)')
