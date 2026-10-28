---
name: qa-predespliegue
description: Control de calidad y verificación previa al despliegue de bcarqstudio.com. Usar antes de cada commit que vaya a fusionarse en main, antes de abrir un pull request, o cuando se pida "verificar", "revisar antes de publicar" o "QA" del sitio. Ejecuta chequeos automáticos (enlaces, imágenes, SEO, fugas de texto, menú móvil) y una revisión visual en navegador.
---

# QA previo al despliegue — Build & Create Studio

GitHub Pages publica automáticamente **todo lo que llega a `main`**. Por eso:
- Nunca hacer push directo a `main`. Trabajar en rama y abrir PR para que el cliente apruebe.
- Ningún cambio se considera listo sin pasar este checklist.

## 1. Chequeo estático (obligatorio)

```bash
python3 .claude/skills/qa-predespliegue/scripts/qa_check.py
```
- Código de salida 1 = hay **BLOQUEANTES**. No se fusiona.
- Comparar contra la línea base anterior: el número de advertencias no debe subir. Guardar la salida en la descripción del PR.

Detecta: recursos locales inexistentes, anclas rotas, imágenes > 1.5 MB, páginas con > 5 MB de imágenes, `<title>`/description fuera de rango, h1 ≠ 1, canonical/OG/JSON-LD faltantes o inválidos, `alt` ausente, menú móvil sin JS, textos visibles tipo "uso interno"/"confidencial"/marcadores pendientes, robots/sitemap/404.

## 2. Chequeo en navegador (obligatorio si cambió HTML/CSS/JS)

```bash
python3 -m http.server 8765 >/dev/null 2>&1 &
node .claude/skills/ux-accesibilidad/scripts/browser_audit.js http://127.0.0.1:8765 <páginas cambiadas>
```
Revisar capturas de `.qa-shots/` en móvil y escritorio y compararlas con `main` (mismo comando sobre un worktree de `main`) para confirmar que **no hubo cambios visuales no autorizados**.

## 3. Checklist de contenido

- [ ] Ningún dato nuevo (cifra, cliente, proyecto, año, estado) sin fuente del cliente. Buscar `[DATO PENDIENTE` → debe ser 0 antes de publicar.
- [ ] El estado de cada proyecto (Construido / Propuesta / Anteproyecto) es el confirmado.
- [ ] Ubicación y `alt` de imágenes coinciden con el proyecto (no restos de otro proyecto).
- [ ] Nombre comercial, email y teléfono idénticos en todas las páginas y en JSON-LD.
- [ ] No se eliminó contenido existente sin justificarlo en el PR.

## 4. Checklist técnico

- [ ] `CNAME` intacto (`bcarqstudio.com`). Si se borra, el dominio deja de funcionar.
- [ ] `sitemap.xml` actualizado con URLs nuevas y `<lastmod>`.
- [ ] Toda URL renombrada tiene página puente (ver skill `seo-tecnico` §3).
- [ ] Formularios: `FORMSPREE_ID` correcto; enviar una prueba desde la vista local solo con autorización (genera un correo real a info@bcarqstudio.com).
- [ ] JSON-LD validado en https://search.google.com/test/rich-results tras publicar.
- [ ] Imágenes nuevas pasadas por `optimizar_imagenes.py`.

## 5. Después de fusionar (lo hace el cliente o con su autorización)

1. Esperar el build de GitHub Pages (pestaña Actions / Settings → Pages).
2. Abrir https://bcarqstudio.com en móvil, forzar recarga.
3. Search Console: inspeccionar las URLs cambiadas y reenviar `sitemap.xml`.

## 6. Informe de QA

```
Rama: <rama> · Commit: <sha>
qa_check: X bloqueantes · Y advertencias (base: Y0)
Navegador: páginas revisadas, capturas comparadas, diferencias visuales: ninguna / lista
Pendientes del cliente: …
Veredicto: LISTO PARA PR / NO LISTO (motivos)
```
