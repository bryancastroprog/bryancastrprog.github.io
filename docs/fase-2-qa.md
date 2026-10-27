# Fase 2 — Correcciones técnicas sin cambio visual · Informe de QA

Rama: `fase-2-correcciones-tecnicas` · Base: `fase-1-diagnostico-seo` · Fecha: 27-oct-2026

## Qué se corrigió (puntos del diagnóstico)

| # | Corrección | Páginas |
|---|---|---|
| 2 | Menú móvil funcional (antes no abría) y accesible: `<button aria-expanded aria-controls>`, operable con teclado | 4 fichas de proyecto; botón accesible en las 6 |
| 3 | 15 PNG de 1.7–9 MB convertidos a WebP (1920 px; 2560 px en planos) + variante de 960 px con `srcset`, `width`/`height`, `loading="lazy"` y `fetchpriority="high"` en el hero | Fichas + Diseño estratégico |
| 8 | 10 imágenes 404 de la home apuntan ahora directamente a `img/`; eliminados `onerror` y el script de respaldo de la foto de Bryan | index |
| 11 | JSON-LD: `ProfessionalService` (home), `Service` + `BreadcrumbList` (diseño estratégico), `CreativeWork` + `BreadcrumbList` (proyectos) | 6 |
| 12 | Canonical absoluto coherente con los enlaces internos (`.html`) y Open Graph/Twitter completos con imagen 1200×630 | 6 |
| 13 | `robots.txt`, `sitemap.xml`, `404.html` (estilo del sitio, `noindex`) y `favicon.svg` (logo BC) | sitio |
| 21 | `alt` de La Autoría que decían "Miami / Wynwood Miami" → "Huehuetenango, Guatemala" | la-autoria |
| 22 | Hero de SweetPop en móvil: título, ubicación y "Construido" ya no se cortan | sweetpop |
| 23 | Botón de menú alineado a la derecha en móvil (estaba descentrado) | index, diseno-estrategico |
| 25 | Copyright unificado en 2026 | 5 |
| 27 | Email clicable (`mailto:`) | index |
| 30 | Title (80 → 58 caracteres) y meta description (185 → 152) ajustados; eliminada `meta keywords` | diseno-estrategico |

También: `_config.yml` excluye los PNG originales del sitio publicado (se conservan en el repositorio como fuente, no se borró nada).

## Qué NO se tocó (y por qué)

- Texto "Proyecto confidencial / Uso interno", tarjetas con Unsplash, cifras sin respaldo, Barnes & Noble, nombre comercial, title/H1 de la home → **Fase 3**, requiere tus respuestas.
- Contraste y tamaños de fuente < 12 px → **Fase 6**, cambian el aspecto y requieren tu autorización.
- Fuentes de Google cargadas por `@import` dentro del SVG del logo: quitarlas cambiaría la tipografía del logo en las fichas de proyecto. Se deja como está.
- JSON-LD sin `sameAs` (redes sociales): los enlaces actuales son genéricos; se añadirá cuando confirmes los perfiles reales.

## Resultados medidos

`qa_check.py`: **41 → 5 bloqueantes**, **116 → 35 advertencias**. Los 5 bloqueantes restantes son el texto "uso interno / confidencial" (Fase 3).

Peso transferido medido en Chromium (escritorio / móvil):

| Página | Antes | Después |
|---|---|---|
| aesthetica-medica | 22.9 MB | 0.4 / 0.1 MB |
| libreria-cayala | 22.0 MB | 0.6 / 0.1 MB |
| sweetpop | 37.0 MB | 0.4 / 0.2 MB |
| la-autoria | 3.5 MB | 0.2 / 0.1 MB |
| diseno-estrategico (imágenes locales) | 32.1 MB | 0.3 MB |
| index | 1.7 MB + 10 errores 404 | 0.5 / 1.0 MB, 0 errores |

Navegador (390 px y 1440 px): 0 recursos 404, 0 errores JavaScript, 0 imágenes rotas (sin contar Unsplash, bloqueado en el entorno de pruebas), menú abre y cierra en las 6 páginas con teclado y clic.

## Verificación de "sin cambio visual"

Capturas de página completa de `main` frente a esta rama, comparadas píxel a píxel (umbral 40/255):

| Página | Escritorio | Móvil | Explicación |
|---|---|---|---|
| index | 0.00 % | 0.00 % | Solo se mueve el botón de menú en móvil (#23) |
| diseno-estrategico | 0.01 % | 0.01 % | Botón de menú (#23) y recompresión |
| aesthetica-medica | 0.15 % | 0.09 % | Recompresión WebP |
| la-autoria | 0.01 % | 0.01 % | Recompresión WebP |
| libreria-cayala | 0.06 % | 0.03 % | Recompresión WebP |
| sweetpop | 0.30 % | 0.98 % | Recompresión + corrección del hero móvil (#22) |

Legibilidad de planos anotados revisada al 100 % de zoom: sin pérdida apreciable.

## Pendiente tras fusionar (requiere tu acción)

1. Fusionar el PR en `main` (lo publica GitHub Pages).
2. Search Console: verificar `bcarqstudio.com`, enviar `https://bcarqstudio.com/sitemap.xml`.
3. Probar una URL en https://search.google.com/test/rich-results.
4. Compartir un enlace por WhatsApp para confirmar la vista previa con imagen.

Veredicto: **LISTO PARA PR** (los bloqueantes restantes dependen de la Fase 3).
