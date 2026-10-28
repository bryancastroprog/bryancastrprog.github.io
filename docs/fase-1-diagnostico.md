# Fase 1 — Diagnóstico de bcarqstudio.com

Fecha: 27 de octubre de 2026 · Rama: `fase-1-diagnostico-seo` · Commit base de `main`: `931ca25`
Alcance: las 6 páginas publicadas. No se modificó ninguna página del sitio.

---

## 0. Resumen ejecutivo

El sitio tiene una identidad visual sólida y un posicionamiento diferenciado ("desarrolladores que diseñan"). Pero hoy **no está construido para captar clientes desde Google** y tiene fallos técnicos que cuestan credibilidad y conversiones:

1. **"Prefactibilidad" aparece 0 veces en todo el sitio.** Es uno de los tres servicios que quieres posicionar y no existe ninguna página ni párrafo que lo mencione. Google no puede posicionar lo que no está escrito.
2. **Las páginas de proyecto pesan entre 22 y 37 MB** (deberían pesar < 3 MB). En 4G en Guatemala tardan decenas de segundos en cargar. Es el principal freno para el SEO móvil y para la conversión.
3. **El menú móvil no funciona en 4 de las 6 páginas** (las fichas de proyecto): el botón existe pero no tiene código. En móvil, el visitante no puede navegar.
4. **Riesgo de credibilidad en el contenido**: textos "Proyecto confidencial · Uso interno" visibles al público, imágenes de stock (Unsplash) presentadas como "Trabajo reciente", cifras sin respaldo ("15+ años", "+30 %") que contradicen "Fundación 2025", y el uso de la marca Barnes & Noble como "primera sede en Centroamérica". Un inversionista o cliente corporativo que lo detecte descarta al estudio.
5. **Sin medición**: no hay Google Analytics, Search Console verificado (no consta en el código) ni seguimiento de formularios. No se sabe cuántos leads genera el sitio.

**Lo más rentable primero:** (a) corregir los fallos que bloquean conversión e indexación (1–2 días de trabajo, sin tocar el diseño), (b) crear la página de **Prefactibilidad** como producto de entrada con precio fijo, y (c) activar Google Business Profile y la medición. Detalle en §6.

---

## 1. Análisis del repositorio

| Aspecto | Hallazgo |
|---|---|
| Framework | Ninguno. HTML estático, CSS y JS en línea por página (~40 KB de CSS duplicado por archivo). |
| Dependencias | Google Fonts (3 familias), Formspree (formularios), Google Calendar (agenda), WhatsApp, Unsplash (13 imágenes externas en `diseno-estrategico.html`). |
| Despliegue | GitHub Pages desde `main`, dominio `bcarqstudio.com` por `CNAME`. Cada push a `main` = producción. Sin staging, sin CI. |
| Historial | 50 commits, la mayoría vía "Add files via upload" y ediciones web de GitHub. Sin ramas ni PRs. |
| Tamaño | **124 MB** de imágenes; 18 PNG de 1.7–9 MB. 9 archivos no se usan en ninguna página (≈ 36 MB), incluidos 3 duplicados exactos (`Kiosko de dulces *.png` = `sweetpop-*.png`). |
| Archivos SEO | No existen `robots.txt`, `sitemap.xml`, `404.html` ni favicon. |
| Jekyll | GitHub Pages procesa el repo con Jekyll: sin exclusión, cualquier `.md` (como este informe) se publicaría. Se añadió `_config.yml` que excluye `CLAUDE.md`, `docs/` y `.claude/`. |

---

## 2. Problemas priorizados

Prioridad: **P0** bloquea conversión/indexación o daña credibilidad · **P1** impacto medible en ranking o velocidad · **P2** mejora relevante · **P3** higiene.
"¿Cambia el diseño?" indica si la corrección requiere tu autorización visual.

### P0 — Críticos

| # | Página | Problema | Evidencia | Solución | ¿Cambia el diseño? |
|---|---|---|---|---|---|
| 1 | Todas | **No existe contenido de prefactibilidad** ni de análisis de terreno | `grep -i prefactibilidad *.html` → 0 resultados en las 6 páginas | Crear `/servicios/prefactibilidad-inmobiliaria/` (ver §4) y mencionarla en home | No (página nueva con la plantilla actual) |
| 2 | 4 fichas de proyecto | **Menú móvil no abre** | `#navToggle` existe pero no hay ningún `addEventListener` en `aesthetica-medica`, `la-autoria`, `libreria-cayala`, `sweetpop` | Añadir el mismo JS de la home y convertir el `<div>` en `<button aria-expanded>` | No |
| 3 | Fichas de proyecto + Diseño estratégico | **Peso de 22–37 MB por página** | Medición con Chromium: Aesthetica 22.9 MB, Librería 22.0 MB, SweetPop 37.0 MB, Diseño estratégico 32 MB en imágenes locales. Prueba: `sweetpop-perspectiva.png` 8.9 MB → 244 KB en WebP 1920 px (−97 %) sin pérdida visible | Convertir a WebP + `srcset`, añadir `width`/`height` y `loading="lazy"` | No |
| 4 | `la-autoria.html`, `sweetpop.html`, `libreria-cayala.html` | **Texto "Proyecto confidencial · Uso interno" / "Uso interno" visible al público** en el pie | Pie de página de cada ficha | Retirar la leyenda o, si el proyecto realmente es confidencial, despublicar la página. **Necesito tu confirmación** | No |
| 5 | `diseno-estrategico.html` | **Imágenes de stock presentadas como proyectos propios** en "Trabajo reciente": "Oficinas corporativas — Rediseño de planta completa para empresa de tecnología", "Boutique hotel lobby", "Consultorio especializado", "Local comercial", "Interiorismo residencial" | 6 tarjetas usan `images.unsplash.com` con descripción de proyecto | Si no son proyectos reales: moverlas a la sección de servicios como ambientación, sin texto de autoría, o retirarlas. **Necesito tu confirmación por tarjeta** | Sí (contenido de la grilla) |
| 6 | `diseno-estrategico.html` | **Cifras sin respaldo** que contradicen otros datos: "15+ años de experiencia en arquitectura comercial" (la home dice "Fundación 2025"), "+30 % incremento de valor en remodelaciones", "entre 15 y 40 %" de aumento de renta/venta | Bloque de métricas y sección "Fundamento" | Sustituir por datos verificables o atribuidos (p. ej. años de experiencia profesional de Bryan si es correcto) o retirar. **Necesito los datos reales** | No |
| 7 | `libreria-cayala.html` | **Uso de marca de tercero**: "Barnes & Noble Guatemala — Primera sede en Centroamérica", con estado "Propuesta" | H1, ficha técnica y descripción | Confirmar si existe encargo y autorización de la marca. Si es un ejercicio conceptual, rotularlo como "Concepto de librería" sin la marca, o indicar explícitamente "propuesta no encargada". Riesgo legal y de credibilidad alto | No |
| 8 | `index.html` | **10 imágenes con error 404** en cada visita (galería ONA y foto de Bryan) | Las rutas apuntan a la raíz (`ona-lobby.jpg`), donde los archivos fueron borrados (commits del 25-abr). Se ven gracias a un `onerror` que reintenta en `img/` → doble petición y 10 errores en consola | Apuntar directamente a `img/…` y eliminar el `onerror` y el script de respaldo | No |
| 9 | Todo el sitio | **Sin medición de conversiones** | No hay GA4, Tag Manager ni meta de verificación de Search Console | Instalar GA4 (o Plausible) con eventos: envío de formulario, clic en WhatsApp, clic en agenda. Verificar Search Console y enviar sitemap | No |

### P1 — Alto impacto

| # | Página | Problema | Evidencia | Solución | ¿Cambia el diseño? |
|---|---|---|---|---|---|
| 10 | `index.html` | **Title y H1 sin palabras clave**: "BC Arquitectura — Del terreno al retorno" / H1 "Del terreno al retorno." | No contiene "arquitectos", "Guatemala", "desarrollo inmobiliario" ni "prefactibilidad" | Title: "Arquitectura y desarrollo inmobiliario en Guatemala \| BC Arquitectura". H1: mantener el eslogan visualmente y añadir una línea con la keyword (p. ej. en el eyebrow convertido a texto semántico). Propuesta exacta para tu aprobación | Mínimo (texto) |
| 11 | Todas | **Sin datos estructurados** (JSON-LD) | 0 bloques `application/ld+json` | `ProfessionalService` en home; `Service` en servicios; `CreativeWork` + `BreadcrumbList` en proyectos | No |
| 12 | 5 de 6 | **Sin canonical ni Open Graph**; ninguna página tiene `og:image` | Solo `diseno-estrategico.html` tiene canonical, y apunta a `/diseno-estrategico` mientras los enlaces internos usan `.html` | Canonical absoluto coherente con los enlaces; OG completo con imagen 1200×630 por página (al compartir por WhatsApp hoy no aparece imagen) | No |
| 13 | Sitio | **Falta `robots.txt`, `sitemap.xml`, `404.html`, favicon** | `qa_check.py` | Crearlos | No (404 con la plantilla actual) |
| 14 | `index.html` | **La home no enlaza a ningún proyecto ni muestra portafolio** | Los 4 proyectos con ficha solo son accesibles desde `diseno-estrategico.html` | Añadir enlace "Proyectos" al menú y un bloque de proyectos destacados | Sí (nuevo bloque, mismo estilo) |
| 15 | `index.html` | **CTA principal orientado a inversionistas, no a clientes**: "Conocer ONA →" | El objetivo es captar clientes de arquitectura y prefactibilidad; el inversionista es una audiencia minoritaria | Hero con 2 rutas: "Diagnóstico de terreno" (primario) y "Ver proyectos"; ONA como sección | Mínimo (texto/destino del botón) |
| 16 | `index.html` | **Formulario sin calificación del lead** | Campos: nombre, email, tipo, mensaje. Sin teléfono, ubicación del terreno/proyecto, m², etapa ni plazo | Añadir teléfono/WhatsApp, zona, m² aproximados, etapa. Permite priorizar y responder con propuesta | Mínimo |
| 17 | `index.html` y fichas | **WhatsApp solo existe en `diseno-estrategico.html`** | `grep -c wa.me` → 0 en home y fichas | Botón WhatsApp en todas las páginas (canal dominante en Guatemala) | Sí (elemento nuevo; propuesta discreta en el estilo actual) |
| 18 | `index.html`, `diseno-estrategico.html` | **"Eficiencia estructural 91.9 %" mal etiquetado** | 17,267 m² vendibles ÷ 18,792 m² construidos = 91.9 %. Es **eficiencia de planta (área vendible/construida)**, no eficiencia estructural | Cambiar la etiqueta. Un inversionista técnico lo detecta | No |
| 19 | Todas | **Contraste insuficiente** (WCAG AA) | axe-core en móvil: 7–15 elementos con contraste insuficiente por página (textos al 40–50 % de opacidad sobre negro) | Subir opacidad de esos textos al mínimo que cumple 4.5:1. Te mostraré antes/después | Sí (ajuste leve de tono) |
| 20 | Todas | **Textos de 8.5–11 px** (etiquetas, eyebrows, labels de formulario) | Medición en navegador: hasta 50 elementos < 12 px por página | Subir a 12 px mínimo | Sí (ajuste leve) |

### P2 — Mejoras relevantes

| # | Página | Problema | Evidencia | Solución |
|---|---|---|---|---|
| 21 | `la-autoria.html` | `alt` de imágenes dicen "Miami" y "Wynwood Miami" en un proyecto de Huehuetenango | Restos del proyecto BRASAS (commit `e7d1625`) | Corregir `alt` |
| 22 | `sweetpop.html` | En móvil el hero se recorta: "Construido" y la línea de ubicación quedan fuera de pantalla | Captura 390 px + `browser_audit.js` (`hero-stats`, `hero-meta` desbordan) | Permitir salto de línea en los datos del hero en móvil |
| 23 | `index.html` | En móvil el botón hamburguesa aparece centrado, no a la derecha | Captura 390 px: el `margin-left:auto` está en `.nav-cta`, que se oculta en móvil | `margin-left:auto` en `.nav-toggle` en móvil |
| 24 | Todas | **Nombre comercial inconsistente**: "BC Arquitectura", "BC Arq Studio", "BC Studio", "Build & Create Studio" | Titles, pies y logos | Definir un nombre oficial (impacta SEO local y Google Business Profile). **Decisión tuya** |
| 25 | Fichas | Años de copyright distintos (2024, 2025, 2026) | Pies de página | Unificar en 2026 |
| 26 | `index.html` | Redes sociales apuntan a `linkedin.com` e `instagram.com` genéricos; "Aviso legal / Privacidad / Términos" no son enlaces | Footer | Perfiles reales; crear página de privacidad (el formulario recoge datos personales) |
| 27 | `index.html` | Email y web en texto plano, sin `mailto:` | Sección contacto y footer | Enlaces clicables |
| 28 | `index.html` | Numeración duplicada "05 — Agenda" y "05 — Contacto" | Eyebrows | Renumerar |
| 29 | `libreria-cayala.html` | La URL dice "cayala" y el proyecto está en Avia, Zona 10 | Commits `e89481c`, `660f4e8` | Nueva URL `/proyectos/libreria-avia/` con puente desde la actual |
| 30 | `diseno-estrategico.html` | Title de 80 caracteres y description de 185; `meta keywords` (sin efecto) | `qa_check.py` | Ajustar longitudes |
| 31 | `index.html` | Badge "Más solicitado" en Co-desarrollo | Afirmación de demanda difícil de sostener con fundación en 2025 | Confirmar o retirar |
| 32 | Estados de proyecto | SweetPop "Construido 2023–2024" y La Autoría "Construido 2025" se muestran solo con renders | Imágenes `.png` generadas | Si están construidos, añadir fotos reales (multiplica la credibilidad); si no, corregir el estado |

### P3 — Higiene técnica

- 9 archivos sin uso (≈ 36 MB) y 3 duplicados exactos: moverlos fuera del sitio publicado (no borrar sin tu visto bueno).
- Google Fonts se carga 3 veces por página (link + 2 `@import` dentro de SVG del logo).
- Animaciones sin `prefers-reduced-motion`; secciones `.reveal` invisibles si el JS falla.
- CSS duplicado en 6 archivos: a medio plazo, extraer a `assets/css/` (sin cambio visual) para que los cambios se hagan una sola vez.

---

## 3. Verificación pendiente de tu parte (bloquea parte de la implementación)

No puedo corregir esto sin datos tuyos, porque la regla es no inventar:

1. **Barnes & Noble**: ¿hubo encargo y autorización de la marca? ¿O es un concepto propio?
2. **Tarjetas con Unsplash** en "Trabajo reciente" (oficinas, hotel, clínica, local comercial, interiorismo): ¿corresponden a proyectos reales?
3. **"15+ años de experiencia"**: ¿es la experiencia profesional de Bryan? ¿Cuántos años exactos? ¿De dónde salen "+30 %" y "15–40 %"?
4. **La Autoría y SweetPop "Construido"**: ¿están construidos? ¿Hay fotos reales?
5. **"Confidencial / Uso interno"**: ¿algún proyecto no debe ser público?
6. **Nombre comercial oficial** y datos NAP: nombre, teléfono público, dirección u "área de servicio", horario.
7. **Credenciales**: número de colegiado (Colegio de Arquitectos de Guatemala), formación, LinkedIn real, Instagram real.
8. **ONA**: ¿se mantiene "Anteproyecto aprobado" e "Inicio de construcción 2026"? Hoy es octubre de 2026.
9. **Prefactibilidad**: qué incluye, plazo de entrega y si quieres publicar precio o "desde Q…".

---

## 4. Arquitectura de páginas propuesta

Organizada por audiencia, con una keyword principal por URL. Las URLs actuales se mantienen como puentes (no se pierde nada de lo indexado).

```
/                                        Home — "Arquitectura y desarrollo inmobiliario en Guatemala"
│                                        3 rutas: Tengo un negocio · Tengo un terreno · Quiero invertir
├── /servicios/
│   ├── prefactibilidad-inmobiliaria/    ★ NUEVA — producto de entrada (diagnóstico de terreno)
│   ├── desarrollo-inmobiliario/         NUEVA — diseño para desarrolladores + co-desarrollo (modelos 01 y 02)
│   ├── diseno-arquitectonico/           NUEVA — residencial/vertical, anteproyecto, ejecutivo, licencias
│   └── diseno-comercial/                ← actual diseno-estrategico.html (oficinas, clínicas, retail, restaurantes)
├── /proyectos/                          NUEVA — portafolio filtrable por tipología y estado
│   ├── ona/                             NUEVA — ficha completa (hoy solo existe como sección en la home)
│   ├── aesthetica-medica/               ← aesthetica-medica.html
│   ├── la-autoria/                      ← la-autoria.html
│   ├── libreria-avia/                   ← libreria-cayala.html (nombre sujeto a tu respuesta §3.1)
│   └── sweetpop/                        ← sweetpop.html
├── /inversionistas/                     NUEVA — tesis, ONA, lista de interés, aviso legal (modelo 03)
├── /estudio/                            NUEVA — Bryan Castro, credenciales, método de 3 filtros
├── /recursos/                           NUEVA — guías que atraen a propietarios de terreno
│   ├── como-saber-cuanto-puedo-construir-en-mi-terreno/
│   ├── que-es-un-estudio-de-prefactibilidad/
│   └── licencia-de-construccion-municipalidad-guatemala/
├── /contacto/                           NUEVA — formulario calificado + agenda + WhatsApp
├── /privacidad/                         NUEVA — obligatoria por el formulario
└── /404.html
```

**Por qué esta estructura:**
- **Prefactibilidad como puerta de entrada**: el propietario de terreno busca "cuánto puedo construir en mi terreno" mucho antes de buscar un arquitecto. Quien resuelve esa pregunta se queda con el proyecto completo (diseño → desarrollo → co-inversión). Es la ruta de mayor valor por cliente del estudio.
- **Separar audiencias** evita que un cliente que busca diseñar su clínica aterrice en un mensaje de co-inversión, y viceversa.
- **Una URL por proyecto y por servicio** multiplica las páginas que Google puede posicionar (hoy: 6; propuesta: ~20 en la primera ola).
- **Recursos** generan tráfico orgánico de largo plazo sobre normativa local (POT, licencias), donde la competencia en Guatemala es baja.

---

## 5. Plan de implementación (requiere tu aprobación)

Cada fase se entrega en su propia rama con PR, informe de QA (`qa-predespliegue`) y capturas antes/después. Nada se publica sin tu visto bueno.

### Fase 2 — Correcciones técnicas sin cambio visual (1–2 días)
Puntos #2, #3, #8, #11, #12, #13, #21, #22, #23, #25, #27, #30 y P3 de fuentes.
Resultado esperado: páginas de proyecto de 22–37 MB a < 3 MB; 0 errores 404; menú móvil operativo; sitio indexable con sitemap, canonical, OG y JSON-LD.

### Fase 3 — Contenido y credibilidad (depende de tus respuestas §3)
Puntos #4, #5, #6, #7, #18, #24, #26, #28, #31, #32 y textos de title/H1 (#10).

### Fase 4 — Conversión y medición
Puntos #9, #15, #16, #17, #14. GA4 + Search Console + eventos de conversión. Página `/contacto/` y `/privacidad/`.

### Fase 5 — Nuevas páginas (arquitectura §4)
Orden por rentabilidad: Prefactibilidad → Proyectos (índice + ONA) → Desarrollo inmobiliario → Inversionistas → Estudio → Diseño arquitectónico → Recursos (1–2 al mes).

### Fase 6 — Accesibilidad visual (requiere autorización de diseño)
Puntos #19 y #20, con muestra antes/después.

---

## 6. Oportunidades de negocio que no estás aprovechando

1. **Productizar la prefactibilidad**: "Diagnóstico de terreno" a precio fijo, con entregable estándar (cabida, normativa aplicable, programa de áreas, pro forma preliminar). Convierte una consulta gratuita en ingreso, filtra curiosos y abre la puerta al proyecto completo. Se puede automatizar la captura: formulario con ubicación, m² y uso, pago anticipado y agenda.
2. **Google Business Profile**: hoy no consta en el sitio. Es el canal con más búsquedas locales ("arquitectos cerca de mí", "arquitectos zona 10") y es gratuito.
3. **Lista de inversionistas con proceso**: el botón "Unirme a la lista" lleva al formulario genérico. Un formulario propio (perfil de inversionista, ticket aproximado) más una secuencia de correos crea un activo comercializable para ONA y los proyectos siguientes. Requiere aviso legal (no es oferta pública de valores; validar con abogado).
4. **Contenido que vende**: cada guía de normativa local capta propietarios de terreno con meses de antelación. Se puede producir con un proceso repetible usando la skill `redaccion-arquitectura`.
5. **Fotos reales de obra construida**: si La Autoría y SweetPop están construidos, una sesión fotográfica profesional vale más que cualquier render para cerrar clientes comerciales.

---

## 7. Entregables de esta fase

| Archivo | Contenido |
|---|---|
| `CLAUDE.md` | Instrucciones permanentes del proyecto |
| `.claude/skills/seo-tecnico/` | Auditoría SEO técnica + `scripts/optimizar_imagenes.py` |
| `.claude/skills/seo-local-contenido/` | Keywords, arquitectura de URLs, SEO local |
| `.claude/skills/redaccion-arquitectura/` | Guía de redacción y veracidad |
| `.claude/skills/ux-accesibilidad/` | Auditoría UX + `scripts/browser_audit.js` (Playwright + axe) |
| `.claude/skills/qa-predespliegue/` | Checklist de despliegue + `scripts/qa_check.py` |
| `_config.yml` | Evita que Jekyll publique los archivos internos |
| `docs/fase-1-diagnostico.md` | Este informe |

Línea base de QA actual (`qa_check.py`): **41 bloqueantes · 116 advertencias · 18 informativos** en 6 páginas. Cada fase siguiente debe reducir esta cifra.
