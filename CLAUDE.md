# CLAUDE.md — bcarqstudio.com (Build & Create Studio)

Sitio web de Build & Create Studio, estudio de arquitectura, prefactibilidad y desarrollo inmobiliario en Ciudad de Guatemala.
Objetivo del sitio: **captar consultas calificadas** de empresas (diseño de espacios), propietarios de terreno/desarrolladores (prefactibilidad, diseño, co-desarrollo) e inversionistas (proyectos propios como ONA).

## Stack y despliegue

- HTML estático puro. Sin framework, sin build, sin `package.json`. Cada página es un `.html` autocontenido con su `<style>` y `<script>` en línea.
- Hosting: **GitHub Pages** desde la rama `main` del repo `bryancastroprog/bryancastrprog.github.io`. Dominio propio vía `CNAME` → `bcarqstudio.com`.
- **Todo push a `main` se publica en producción en minutos.** No hay entorno de staging.
- Servicios externos: Google Fonts (Fraunces, Inter, Space Grotesk), Formspree (`FORMSPREE_ID = 'xbdbdlay'`, envía a info@bcarqstudio.com), Google Calendar (agenda), WhatsApp (`wa.me/50254131753`), imágenes de Unsplash en `diseno-estrategico.html`.
- Imágenes en `img/`. Los originales PNG (6–9 MB) se conservan como fuente pero **no se publican** (`_config.yml` los excluye): las páginas usan `<nombre>.webp` + `<nombre>-960.webp` con `srcset`, y `<nombre>-og.jpg` para Open Graph. Toda imagen nueva pasa por `optimizar_imagenes.py`.
- Archivos SEO: `robots.txt`, `sitemap.xml` (actualizar al crear o renombrar páginas), `404.html`, `favicon.svg`.

## Páginas actuales

| Archivo | Rol |
|---|---|
| `index.html` | Home: tesis, ONA, estudio, modelos de trabajo, agenda, contacto |
| `diseno-estrategico.html` | Servicios de diseño para negocios + grilla de proyectos + formulario |
| `aesthetica-medica.html`, `la-autoria.html`, `libreria-cayala.html`, `sweetpop.html` | Fichas de proyecto (misma plantilla) |

## Generador de páginas (dirección visual A)

`index.html`, `prefactibilidad-inmobiliaria.html` y `edificio-w.html` se generan con `python3 .claude/build/build_a.py` (CSS compartido, cabecera, pie y formularios). **Editar el generador, no el HTML de salida**, y volver a ejecutarlo. La capa de movimiento de prefactibilidad está en `.claude/build/motion_pref.py`. Las demás páginas (`diseno-estrategico.html`, `la-autoria.html`) todavía son HTML manual con el diseño anterior.

## Reglas obligatorias

1. **No modificar el diseño visual** (colores, tipografías, layout, animaciones, estilo) sin autorización explícita. Correcciones técnicas invisibles (SEO, peso de imágenes, accesibilidad sin impacto visual, JS roto) sí están permitidas dentro de una tarea aprobada.
2. **No inventar** proyectos, clientes, cifras, porcentajes, años de experiencia, resultados ni testimonios. Si falta un dato: `[DATO PENDIENTE: …]` y preguntar.
3. **No eliminar contenido existente** sin justificarlo por escrito (PR o informe).
4. **No publicar en producción**: nunca push a `main`. Trabajar en rama (`fase-N-…`) y abrir PR solo cuando el cliente lo pida.
5. **No cambiar URLs existentes** sin página puente (meta refresh + canonical + noindex).
6. Mantener intacto el archivo `CNAME`.
7. No ejecutar envíos reales del formulario Formspree sin autorización (llegan a la bandeja del cliente).

## Convenciones

- Idioma: español de Guatemala, tuteo. "Ciudad de Guatemala", "m²", miles con coma (18,792).
- Respetar el estilo de código existente: CSS en línea por página con variables en `:root`, comentarios de sección en mayúsculas (`/* ===== SECCION ===== */`), JS vanilla al final del `<body>`.
- Rutas de imagen siempre `img/archivo.ext` (relativas). Nombres en minúsculas, con guiones, sin espacios.
- Cada `<img>`: `alt` descriptivo, `width`/`height`, `loading="lazy"` salvo la imagen principal.
- Cada página: 1 `<h1>`, `<title>` ≤ 65 caracteres, meta description 140–160, canonical absoluto, Open Graph con imagen, JSON-LD.

## Skills del proyecto (`.claude/skills/`)

| Skill | Cuándo |
|---|---|
| `seo-tecnico` | Indexación, metadatos, JSON-LD, sitemap, imágenes, velocidad |
| `seo-local-contenido` | Keywords, arquitectura de URLs, enlazado interno, Google Business Profile |
| `redaccion-arquitectura` | Escribir o reescribir cualquier texto del sitio |
| `ux-accesibilidad` | Responsive, menú, contraste, formularios, conversión |
| `qa-predespliegue` | Antes de todo commit destinado a PR |

## Comandos

```bash
# Servir localmente
python3 -m http.server 8765
# QA estático (exit 1 = bloqueantes)
python3 .claude/skills/qa-predespliegue/scripts/qa_check.py
# Auditoría en navegador (móvil + escritorio, capturas en .qa-shots/)
node .claude/skills/ux-accesibilidad/scripts/browser_audit.js http://127.0.0.1:8765
# Optimizar imágenes a WebP (no borra originales)
python3 .claude/skills/seo-tecnico/scripts/optimizar_imagenes.py img/archivo.png
```

## Documentación

- `docs/fase-1-diagnostico.md`: diagnóstico inicial, problemas priorizados, arquitectura propuesta y plan de implementación.
