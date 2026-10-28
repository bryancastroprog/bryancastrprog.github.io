---
name: ux-accesibilidad
description: Auditoría de experiencia de usuario, accesibilidad (WCAG 2.1 AA), diseño responsive y conversión de bcarqstudio.com en navegador real. Usar cuando se revise cómo se ve o funciona el sitio en móvil o escritorio, el menú, formularios, contraste, tamaños de texto, CTAs, recorridos de usuario, o después de cualquier cambio de HTML/CSS.
---

# Auditoría UX, accesibilidad y responsive — Build & Create Studio

**Restricción**: el diseño visual (paleta, tipografías, composición, estilo editorial oscuro) no se modifica sin autorización explícita del cliente. Las correcciones de accesibilidad se proponen primero con el ajuste mínimo (p. ej. subir la opacidad de un texto de 0.45 a 0.65) y se presentan con captura antes/después.

## 1. Auditoría automática en navegador

```bash
python3 -m http.server 8765 >/dev/null 2>&1 &
npm i --no-save axe-core@4.10.2          # opcional, habilita el chequeo WCAG
node .claude/skills/ux-accesibilidad/scripts/browser_audit.js http://127.0.0.1:8765
```
Mide por página en 390 px y 1440 px: 404 locales, errores JS, MB transferidos, desborde horizontal, elementos recortados, textos < 12 px, objetivos táctiles < 24 px, imágenes rotas y violaciones axe. Capturas en `.qa-shots/` — **mirarlas siempre** (Read sobre el PNG), el JSON no detecta todo.

En este entorno los hosts externos (Unsplash, Google Fonts) pueden estar bloqueados; distinguir esos fallos de los errores reales del sitio.

## 2. Checklist manual

**Navegación**
- [ ] Menú móvil abre y cierra en **todas** las páginas (es `#navToggle`; las páginas de proyecto no tienen el JS).
- [ ] El botón de menú es `<button aria-expanded aria-controls>`, accesible con teclado y con nombre accesible.
- [ ] La home enlaza al portafolio de proyectos y a cada servicio.
- [ ] Desde cualquier página se llega a contacto en 1 clic.

**Legibilidad**
- [ ] Contraste texto/fondo ≥ 4.5:1 (≥ 3:1 en textos ≥ 24 px). Los grises con opacidad 0.4–0.5 sobre negro suelen fallar.
- [ ] Texto de cuerpo ≥ 16 px en móvil; etiquetas y eyebrows ≥ 12 px.
- [ ] Ningún titular o dato se corta en 390 px (revisar hero de páginas de proyecto).

**Formularios y conversión**
- [ ] Cada campo tiene `<label for>`; errores anunciados con `aria-live`.
- [ ] El formulario pide los datos que permiten calificar el lead (tipo de proyecto, ubicación/zona, m² aproximados, etapa, plazo).
- [ ] Hay confirmación visible tras enviar y un canal alternativo (correo/WhatsApp).
- [ ] Email como `mailto:`, teléfono como `tel:`, WhatsApp visible en todas las páginas.
- [ ] Enlaces legales (Privacidad, Aviso legal) son enlaces reales a páginas existentes.
- [ ] Redes sociales apuntan a perfiles reales, no a `linkedin.com` genérico.

**Movimiento y robustez**
- [ ] Animaciones respetan `@media (prefers-reduced-motion: reduce)`.
- [ ] El contenido con `.reveal` (opacity 0) es visible si el JS falla.
- [ ] `alt` presente; las imágenes decorativas con `alt=""`.

## 3. Recorridos a probar (móvil primero)

1. Empresa busca "diseño de clínicas Guatemala" → llega a servicio → ve proyecto clínica → envía formulario.
2. Propietario de terreno → home → prefactibilidad → agenda llamada.
3. Inversionista → home → ONA → se une a la lista.
Cronometrar clics y detectar bloqueos (menú que no abre, CTA que lleva a otra audiencia, formulario sin opción adecuada).

## 4. Entregable

Tabla `Prioridad · Página · Viewport · Problema · Evidencia (captura/medida) · Corrección propuesta · ¿Cambia el diseño visual? (sí/no)`. Lo marcado "sí" requiere aprobación antes de implementarse.
