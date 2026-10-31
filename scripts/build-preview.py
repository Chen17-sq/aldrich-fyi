"""Create a browser-openable review copy without publishing the website."""

from base64 import b64encode
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
js = (root / 'assets/site.js').read_text()
image = b64encode((root / 'assets/folded-paper.png').read_bytes()).decode('ascii')

assert '</script' not in js.lower()
for stylesheet in ['fonts.css', 'site.css', 'content.css']:
    css = (root / 'assets' / stylesheet).read_text()
    assert '</style' not in css.lower()
    if stylesheet == 'fonts.css':
        for font in ['BodoniModa', 'Inter']:
            encoded = b64encode((root / 'assets/fonts' / f'{font}.woff2').read_bytes()).decode('ascii')
            css = css.replace(f'fonts/{font}.woff2', f'data:font/woff2;base64,{encoded}')
            license_text = (root / 'assets/fonts' / f'{font}-OFL.txt').read_text()
            assert '*/' not in license_text
            css += f'\n/* {font} license\n{license_text}\n*/\n'
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
        'Aldrich FYI — 第五版预览\n\n'
        '解压后，用 Chrome 或 Safari 打开 Aldrich-FYI-preview.html。\n'
        '图片、样式和脚本都已包含在 HTML 中，无需安装。\n'
        'Bodoni Moda 和 Inter 字体已包含在 HTML 内，离线也可使用；中文使用对应系统字体。\n\n'
        '本版为三个工具绘制独立封面：日报、转录、记忆网络；封面可直接打开项目。\n'
        '加入一次性的封面动效、阅读进度细线、桌面投资机构标签跟随和更醒目的邮件入口。\n'
        '保留原始24个项目、3个工具、年份、项目归属和四语内容；保留卡片和滚动动效。\n'
        '如系统开启「减少动态效果」，位移动效会关闭。\n\n'
        '源码、四语切换与动效逻辑检查已通过；本轮尚未完成浏览器视觉验收。\n'
        '此文件仅供确认设计，aldrich.fyi 线上未更新。\n')
with ZipFile(archive) as package:
    assert package.testzip() is None
print(f'Created {archive} ({archive.stat().st_size:,} bytes)')
