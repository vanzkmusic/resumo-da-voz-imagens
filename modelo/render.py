"""Renderiza os cards HTML de um dia em JPG 1080x1350 prontos para o Instagram.

Uso:  python3 modelo/render.py 2026-10-15
Lê:   <data>/cards/*.html  (ordem alfabética = ordem do carrossel)
Gera: <data>/*.jpg  e  <data>/_previa.png (folha de contato para conferência)
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image

repo = pathlib.Path(__file__).resolve().parent.parent
dia = repo / sys.argv[1]
cards = sorted((dia / "cards").glob("*.html"))
if not 2 <= len(cards) <= 10:
    sys.exit(f"Precisa de 2 a 10 cards em {dia/'cards'}, encontrei {len(cards)}")

fonts = repo / "modelo" / "fonts"
face = f"""<style>
@font-face{{font-family:'Archivo';src:url('{(fonts/'Archivo.ttf').as_uri()}') format('truetype');font-weight:100 900}}
@font-face{{font-family:'IBM Plex Sans';src:url('{(fonts/'IBMPlexSans.ttf').as_uri()}') format('truetype');font-weight:100 700}}
body{{margin:0}}
</style>"""

saidas = []
with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
    for c in cards:
        tmp = c.with_suffix(".render.html")
        tmp.write_text(c.read_text().replace("<head>", "<head>" + face, 1))
        page.goto(tmp.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        png = c.with_suffix(".png")
        page.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        out = dia / (c.stem + ".jpg")
        Image.open(png).convert("RGB").resize((1080, 1350), Image.LANCZOS).save(out, quality=95, subsampling=0, optimize=True)
        png.unlink(); tmp.unlink()
        saidas.append(out)
    b.close()

W, H = 540, 675
cols = 4
rows = (len(saidas) + cols - 1) // cols
folha = Image.new("RGB", (W * cols, H * rows), "white")
for i, f in enumerate(saidas):
    folha.paste(Image.open(f).resize((W, H)), ((i % cols) * W, (i // cols) * H))
folha.save(dia / "_previa.png")
for f in saidas:
    print(f.relative_to(repo), f.stat().st_size // 1024, "KB")
print("previa:", (dia / "_previa.png").relative_to(repo))
