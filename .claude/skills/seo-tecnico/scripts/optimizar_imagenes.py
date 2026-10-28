#!/usr/bin/env python3
"""Genera versiones WebP web-ready de imágenes del sitio sin tocar los originales.

Uso (desde la raíz del repo):
    python3 .claude/skills/seo-tecnico/scripts/optimizar_imagenes.py img/foto.png [img/otra.jpg ...]
    python3 .claude/skills/seo-tecnico/scripts/optimizar_imagenes.py --og img/foto.png   # además 1200x630 para Open Graph
    python3 .claude/skills/seo-tecnico/scripts/optimizar_imagenes.py --max=2560 --q=85 img/planta.png  # planos con texto

Por cada imagen crea, en la misma carpeta:
    <nombre>.webp      (máx. 1920 px de ancho o --max, calidad 80 o --q)
    <nombre>-960.webp  (960 px, para srcset en móvil)
    <nombre>-og.jpg    (solo con --og: 1200x630 recortado al centro)
Imprime width/height finales para colocarlos en el <img>. Requiere Pillow.
"""
import os
import sys

from PIL import Image, ImageOps

QUALITY = 80


def slug(path):
    base, _ = os.path.splitext(path)
    d, n = os.path.split(base)
    n = n.lower().replace(" ", "-").replace("_", "-")
    return os.path.join(d, n)


def main():
    og = "--og" in sys.argv
    opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
    max_w, quality = int(opts.get("max", 1920)), int(opts.get("q", QUALITY))
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not files:
        print(__doc__)
        sys.exit(1)
    for src in files:
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        out = slug(src)
        before = os.path.getsize(src) / 1024
        for width, suffix in ((max_w, ""), (960, "-960")):
            copy = im.copy()
            copy.thumbnail((width, width * 4))
            dest = f"{out}{suffix}.webp"
            copy.save(dest, "WEBP", quality=quality, method=6)
            print(f"{src} ({before:.0f} KB) → {dest} {copy.width}x{copy.height} {os.path.getsize(dest)/1024:.0f} KB")
        if og:
            dest = f"{out}-og.jpg"
            ImageOps.fit(im, (1200, 630), Image.LANCZOS).save(dest, "JPEG", quality=82, optimize=True, progressive=True)
            print(f"{src} → {dest} 1200x630 {os.path.getsize(dest)/1024:.0f} KB")


if __name__ == "__main__":
    main()
