#!/usr/bin/env python3
"""Chequeo estático de calidad para el sitio estático de BC Arquitectura.

Uso (desde la raíz del repo):
    python3 .claude/skills/qa-predespliegue/scripts/qa_check.py [--json] [archivo.html ...]

Sin argumentos revisa todos los *.html del repo (excepto node_modules y .git).
Sale con código 1 si encuentra BLOQUEANTES; 0 si solo hay advertencias.
Solo usa la librería estándar.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.getcwd()
DOMAIN = "bcarqstudio.com"
IMG_WARN_KB = 400        # imágenes > 400 KB = advertencia
IMG_BLOCK_KB = 1500      # imágenes > 1.5 MB = bloqueante
PAGE_IMG_BLOCK_MB = 5    # peso total de imágenes locales por página
TITLE_RANGE = (30, 65)
DESC_RANGE = (70, 160)
LEAK_PATTERNS = [r"uso interno", r"confidencial", r"lorem ipsum"]          # sin distinguir mayúsculas
PLACEHOLDERS = [r"\bTU_FORM_ID\b", r"\bGOOGLE_CALENDAR_LINK\b", r"\bTODO\b", r"\bXXX\b", r"\bFIXME\b"]  # exactos


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta, self.links, self.imgs, self.anchors = {}, [], [], []
        self.h1, self.headings, self.ids = 0, [], set()
        self.title, self._in_title, self._skip, self._hstack = "", False, 0, []
        self.lang, self.text, self.jsonld, self._in_jsonld = None, [], [], False
        self.inline_style_urls, self.buttons_div = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title" and not self._skip:
            self._in_title = True
        if tag in ("style", "svg"):
            self._skip += 1
        if tag == "script":
            if a.get("type") == "application/ld+json":
                self._in_jsonld = True
            self._skip += 1
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        if tag == "link":
            self.links.append(a)
        if tag == "img":
            self.imgs.append(a)
        if tag == "a":
            self.anchors.append(a)
        if re.fullmatch(r"h[1-6]", tag) and not self._skip:
            if tag == "h1":
                self.h1 += 1
            self._hstack.append([tag, ""])
        if "style" in a and "url(" in a["style"]:
            self.inline_style_urls += re.findall(r"url\(['\"]?([^'\")]+)", a["style"])
        if tag == "div" and "toggle" in (a.get("class") or ""):
            self.buttons_div += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in ("style", "svg", "script"):
            self._skip = max(0, self._skip - 1)
            self._in_jsonld = False
        if self._hstack and tag == self._hstack[-1][0]:
            t, txt = self._hstack.pop()
            self.headings.append((t, " ".join(txt.split())))

    def handle_data(self, data):
        if self._in_jsonld:
            self.jsonld.append(data)
        if self._in_title:
            self.title += data
        if self._skip:
            return
        for h in self._hstack:
            h[1] += data
        if data.strip():
            self.text.append(data.strip())


def is_local(url):
    if not url or url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return False
    p = urlparse(url)
    return not p.scheme and not p.netloc or p.netloc.endswith(DOMAIN)


def local_path(url, base_file):
    p = urlparse(url)
    path = unquote(p.path)
    if not path:
        return None
    if path.startswith("/"):
        full = os.path.join(ROOT, path.lstrip("/"))
    else:
        full = os.path.join(os.path.dirname(base_file), path)
    if os.path.isdir(full):
        full = os.path.join(full, "index.html")
    if not os.path.exists(full) and not os.path.splitext(full)[1]:
        if os.path.exists(full + ".html"):
            full += ".html"
    return os.path.normpath(full)


def check(file):
    raw = open(file, encoding="utf-8").read()
    p = Page()
    p.feed(raw)
    rel = os.path.relpath(file, ROOT)
    issues = []

    def add(level, cat, msg):
        issues.append({"file": rel, "level": level, "cat": cat, "msg": msg})

    # --- SEO on-page
    t = " ".join(p.title.split())
    if not t:
        add("BLOQUEANTE", "seo", "Falta <title>")
    elif not TITLE_RANGE[0] <= len(t) <= TITLE_RANGE[1]:
        add("ADVERTENCIA", "seo", f"<title> de {len(t)} caracteres (ideal {TITLE_RANGE[0]}–{TITLE_RANGE[1]}): «{t}»")
    d = p.meta.get("description", "")
    if not d:
        add("BLOQUEANTE", "seo", "Falta meta description")
    elif not DESC_RANGE[0] <= len(d) <= DESC_RANGE[1]:
        add("ADVERTENCIA", "seo", f"meta description de {len(d)} caracteres (ideal {DESC_RANGE[0]}–{DESC_RANGE[1]})")
    if p.h1 != 1:
        add("BLOQUEANTE" if p.h1 == 0 else "ADVERTENCIA", "seo", f"{p.h1} etiquetas <h1> (debe haber exactamente 1)")
    canon = [l for l in p.links if (l.get("rel") or "").lower() == "canonical"]
    if not canon:
        add("ADVERTENCIA", "seo", "Falta <link rel=canonical>")
    else:
        href = canon[0].get("href", "")
        if not href.startswith(f"https://{DOMAIN}"):
            add("ADVERTENCIA", "seo", f"canonical no absoluto con https://{DOMAIN}: {href}")
    for og in ("og:title", "og:description", "og:image", "og:url"):
        if og not in p.meta:
            add("ADVERTENCIA", "seo", f"Falta {og}")
    if not p.jsonld:
        add("ADVERTENCIA", "seo", "Sin datos estructurados JSON-LD")
    else:
        for block in p.jsonld:
            try:
                json.loads(block)
            except ValueError as e:
                add("BLOQUEANTE", "seo", f"JSON-LD inválido: {e}")
    if "keywords" in p.meta:
        add("INFO", "seo", "meta keywords no tiene efecto en Google; se puede eliminar")
    if p.lang != "es":
        add("ADVERTENCIA", "a11y", f'<html lang="{p.lang}"> (esperado "es")')
    if not any("icon" in (l.get("rel") or "") for l in p.links):
        add("ADVERTENCIA", "seo", "Falta favicon (<link rel=icon>)")

    # --- Enlaces y recursos locales
    refs = [("img", i.get("src")) for i in p.imgs]
    refs += [("a", a.get("href")) for a in p.anchors]
    refs += [("link", l.get("href")) for l in p.links if (l.get("rel") or "") not in ("preconnect", "dns-prefetch", "canonical")]
    refs += [("css", u) for u in re.findall(r"url\(['\"]?([^'\")]+)", raw) if not u.startswith(("data:", "%23", "#"))]
    refs += [("css", u) for u in p.inline_style_urls]
    seen = set()
    page_img_bytes = 0
    for kind, url in refs:
        if not url or (kind, url) in seen:
            continue
        seen.add((kind, url))
        if url.startswith("#") and len(url) > 1 and url[1:] not in p.ids:
            add("BLOQUEANTE", "links", f"Ancla rota {url}")
        if not is_local(url):
            if "unsplash.com" in url:
                add("ADVERTENCIA", "contenido", f"Imagen de stock (Unsplash) en uso: {url[:70]}… — verificar que no se presente como proyecto propio")
            continue
        lp = local_path(url, file)
        if lp is None:
            continue
        if not os.path.exists(lp):
            add("BLOQUEANTE", "links", f"Recurso local inexistente ({kind}): {url}")
            continue
        frag = urlparse(url).fragment
        if frag and lp.endswith(".html"):
            target_ids = set(re.findall(r'id="([^"]+)"', open(lp, encoding="utf-8").read()))
            if frag not in target_ids:
                add("BLOQUEANTE", "links", f"Ancla inexistente en destino: {url}")
        if re.search(r"\.(png|jpe?g|webp|avif|gif)$", lp, re.I):
            kb = os.path.getsize(lp) / 1024
            page_img_bytes += kb
            if kb > IMG_BLOCK_KB:
                add("BLOQUEANTE", "perf", f"Imagen de {kb/1024:.1f} MB: {url}")
            elif kb > IMG_WARN_KB:
                add("ADVERTENCIA", "perf", f"Imagen de {kb:.0f} KB: {url}")
        if " " in url:
            add("ADVERTENCIA", "links", f"URL con espacios: {url}")
    if page_img_bytes / 1024 > PAGE_IMG_BLOCK_MB:
        add("BLOQUEANTE", "perf", f"Imágenes locales suman {page_img_bytes/1024:.1f} MB (máx. {PAGE_IMG_BLOCK_MB} MB)")

    # --- Imágenes: alt, dimensiones, lazy
    for i, img in enumerate(p.imgs):
        src = (img.get("src") or "")[:60]
        if img.get("alt") is None:
            add("BLOQUEANTE", "a11y", f"<img> sin alt: {src}")
        if not (img.get("width") and img.get("height")):
            add("ADVERTENCIA", "perf", f"<img> sin width/height (riesgo de CLS): {src}")
        if i > 0 and img.get("loading") != "lazy":
            add("INFO", "perf", f"<img> bajo el pliegue sin loading=lazy: {src}")

    # --- Enlaces externos y vacíos
    for a in p.anchors:
        href = a.get("href") or ""
        if a.get("target") == "_blank" and "noopener" not in (a.get("rel") or ""):
            add("ADVERTENCIA", "seguridad", f'target=_blank sin rel="noopener": {href[:60]}')
        if href.rstrip("/") in ("https://linkedin.com", "https://instagram.com", "https://facebook.com", "https://www.linkedin.com", "https://www.instagram.com"):
            add("ADVERTENCIA", "conversion", f"Enlace social genérico sin perfil: {href}")

    # --- Accesibilidad / UX
    if p.buttons_div:
        add("ADVERTENCIA", "a11y", "Botón de menú implementado como <div> (usar <button> con aria-expanded)")
    if re.search(r'id="navToggle"', raw) and not re.search(r"getElementById\(['\"]navToggle['\"]\)", raw):
        add("BLOQUEANTE", "ux", "Menú móvil (navToggle) sin JavaScript: no abre en móvil")
    small = sorted(set(float(x) for x in re.findall(r"font-size:\s*([0-9.]+)px", raw) if float(x) < 12))
    if small:
        add("ADVERTENCIA", "a11y", f"Tamaños de fuente < 12px en CSS: {small}")

    # --- Fugas de contenido
    body_text = " ".join(p.text)
    for pat in LEAK_PATTERNS:
        if re.search(pat, body_text, re.I):
            add("BLOQUEANTE", "contenido", f"Texto visible sospechoso: «{pat}»")
    for pat in PLACEHOLDERS:
        if re.search(pat, body_text):
            add("BLOQUEANTE", "contenido", f"Marcador pendiente visible: «{pat}»")
    years = sorted(set(re.findall(r"©\s*(20\d\d)", body_text)))
    if years:
        add("INFO", "contenido", f"Año de copyright: {years}")
    return issues


def site_checks(files):
    issues = []
    def add(level, cat, msg):
        issues.append({"file": "(sitio)", "level": level, "cat": cat, "msg": msg})
    for f in ("robots.txt", "sitemap.xml", "404.html", "CNAME"):
        if not os.path.exists(os.path.join(ROOT, f)):
            add("BLOQUEANTE" if f in ("CNAME",) else "ADVERTENCIA", "seo", f"Falta {f}")
    sm = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(sm):
        locs = re.findall(r"<loc>([^<]+)</loc>", open(sm, encoding="utf-8").read())
        for f in files:
            relp = os.path.relpath(f, ROOT).replace(os.sep, "/")
            if relp == "404.html" or "noindex" in open(f, encoding="utf-8").read():
                continue
            slug = relp[:-len("index.html")] if relp.endswith("index.html") else relp
            if not any(l.rstrip("/").endswith(slug.rstrip("/").replace(".html", "")) or l.endswith(slug) for l in locs):
                add("ADVERTENCIA", "seo", f"{relp} no aparece en sitemap.xml")
    total = 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "node_modules", ".claude")]
        total += sum(os.path.getsize(os.path.join(dp, x)) for x in fn)
    if total > 300 * 1024 * 1024:
        add("BLOQUEANTE", "perf", f"Repositorio publicado de {total/1048576:.0f} MB (GitHub Pages recomienda < 1 GB; objetivo < 100 MB)")
    elif total > 60 * 1024 * 1024:
        add("ADVERTENCIA", "perf", f"Repositorio publicado de {total/1048576:.0f} MB — optimizar imágenes")
    return issues


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    excluded = {".git", "node_modules", ".claude", "docs"}
    files = [os.path.abspath(a) for a in args] or sorted(
        os.path.join(dp, f) for dp, dn, fn in os.walk(ROOT)
        if not excluded & set(os.path.relpath(dp, ROOT).split(os.sep))
        for f in fn if f.endswith(".html"))
    issues = []
    for f in files:
        issues += check(f)
    issues += site_checks(files)
    if as_json:
        print(json.dumps(issues, ensure_ascii=False, indent=1))
    else:
        order = {"BLOQUEANTE": 0, "ADVERTENCIA": 1, "INFO": 2}
        for i in sorted(issues, key=lambda x: (order[x["level"]], x["file"], x["cat"])):
            print(f'[{i["level"]}] {i["file"]} · {i["cat"]} · {i["msg"]}')
        counts = {k: sum(1 for i in issues if i["level"] == k) for k in order}
        print(f"\nResumen: {counts['BLOQUEANTE']} bloqueantes · {counts['ADVERTENCIA']} advertencias · {counts['INFO']} info · {len(files)} páginas")
    sys.exit(1 if any(i["level"] == "BLOQUEANTE" for i in issues) else 0)


if __name__ == "__main__":
    main()
