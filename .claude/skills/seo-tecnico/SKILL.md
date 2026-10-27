---
name: seo-tecnico
description: Auditoría y corrección de SEO técnico del sitio estático de BC Arquitectura (bcarqstudio.com, GitHub Pages). Usar cuando se pida revisar indexación, títulos, meta descriptions, canonical, Open Graph, datos estructurados JSON-LD, sitemap.xml, robots.txt, velocidad de carga, peso de imágenes, Core Web Vitals o enlaces rotos, o antes de publicar una página nueva.
---

# Auditoría SEO técnica — BC Arquitectura

Sitio HTML estático sin build, servido por GitHub Pages con dominio `bcarqstudio.com` (archivo `CNAME`).
No hay servidor: no existen redirecciones 301 ni cabeceras HTTP configurables. Todo se resuelve en HTML.

## 1. Ejecutar el chequeo automático

```bash
python3 .claude/skills/qa-predespliegue/scripts/qa_check.py
```

Filtra por categoría `seo`, `links` y `perf`. `--json` produce salida para procesar.

## 2. Checklist manual por página

| Elemento | Criterio | Cómo verificar |
|---|---|---|
| `<title>` | 30–65 caracteres, keyword principal + "Guatemala" + marca al final | qa_check |
| meta description | 70–160 caracteres, beneficio + llamada a la acción | qa_check |
| `<h1>` | Exactamente 1, contiene la intención de búsqueda | qa_check |
| Jerarquía | h2 → h3 sin saltos; los títulos decorativos no deben ser h2 | revisar `headings` |
| canonical | Absoluto `https://bcarqstudio.com/<ruta>` y **coincide con la URL enlazada internamente** | grep `canonical` |
| Open Graph | `og:title`, `og:description`, `og:image` (1200×630, < 300 KB), `og:url`, `og:locale=es_GT` | qa_check |
| JSON-LD | Ver plantillas abajo; validar que el JSON parsea | qa_check + Rich Results Test |
| Imágenes | WebP/AVIF, ≤ 400 KB, `width`/`height`, `alt` descriptivo, `loading="lazy"` excepto la primera | qa_check |
| Enlaces internos | Sin 404, sin rutas en la raíz que solo existen en `/img/` | qa_check |
| robots.txt / sitemap.xml | Existen; el sitemap lista todas las URLs indexables con `<lastmod>` | qa_check |

## 3. Reglas específicas del proyecto

- **URLs**: GitHub Pages sirve `pagina.html` y `pagina` (sin extensión). Elegir **una** forma y usarla en canonical, sitemap y enlaces internos. Para URLs nuevas preferir carpetas: `servicios/prefactibilidad/index.html` → `/servicios/prefactibilidad/`.
- **Cambiar una URL existente**: dejar el archivo viejo como página puente con `<meta http-equiv="refresh" content="0; url=/nueva/">`, `<link rel="canonical" href="https://bcarqstudio.com/nueva/">` y `<meta name="robots" content="noindex">`. Nunca borrar la URL vieja sin puente.
- **Imágenes**: las originales PNG de 6–9 MB no se publican. Exportar a WebP (máx. 1920 px de ancho, calidad ~80) y una variante de 960 px para `srcset` con el script de la sección 5.
- **Fuentes**: cargar Google Fonts una sola vez por página; no repetir `@import` dentro de `<svg>`.
- `meta keywords` no aporta; no añadirla en páginas nuevas.

## 4. Plantillas JSON-LD

Usar solo datos verificados por el cliente. Si un dato (teléfono, dirección, horario) no está confirmado, **omitir la propiedad**, no inventarla.

Home (`ProfessionalService` + `Organization`):
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://bcarqstudio.com/#organizacion",
  "name": "BC Arquitectura",
  "url": "https://bcarqstudio.com/",
  "logo": "https://bcarqstudio.com/img/bc-logo-studio.svg",
  "image": "https://bcarqstudio.com/img/og-home.jpg",
  "email": "info@bcarqstudio.com",
  "areaServed": {"@type": "Country", "name": "Guatemala"},
  "address": {"@type": "PostalAddress", "addressLocality": "Ciudad de Guatemala", "addressCountry": "GT"},
  "founder": {"@type": "Person", "name": "Bryan Castro", "jobTitle": "Arquitecto"},
  "sameAs": []
}
```
Página de servicio: `Service` con `provider: {"@id": "https://bcarqstudio.com/#organizacion"}` y `areaServed`.
Página de proyecto: `CreativeWork` (o `Place` si está construido) + `BreadcrumbList`.
FAQ visible en la página → `FAQPage` (solo si las preguntas están visibles).

## 5. Optimización de imágenes (no cambia el diseño)

```bash
python3 .claude/skills/seo-tecnico/scripts/optimizar_imagenes.py img/archivo.png [...]
```
Genera `archivo.webp` (1920 px) y `archivo-960.webp` junto al original. Luego sustituir en HTML:
```html
<img src="img/archivo.webp" srcset="img/archivo-960.webp 960w, img/archivo.webp 1920w"
     sizes="(max-width: 900px) 100vw, 60vw" width="1920" height="1047" alt="…" loading="lazy" decoding="async">
```

## 6. Entregable

Tabla priorizada: `Prioridad (P0–P3) · Página · Problema · Evidencia (comando/salida) · Solución · Impacto esperado`.
P0 = rompe indexación o conversión; P1 = afecta ranking/velocidad de forma medible; P2 = mejora; P3 = higiene.
