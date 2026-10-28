"""Genera index.html y prefactibilidad-inmobiliaria.html en la dirección visual A (Obra primero)."""
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # raíz del repo

BRAND = 'Build &amp; Create Studio'
BRAND_TXT = 'Build & Create Studio'
SITE = 'https://bcarqstudio.com/'
WA = 'https://wa.me/50254131753'
WA_TXT = '?text=Hola%2C%20me%20interesa%20un%20diagn%C3%B3stico%20de%20terreno.'
CAL = 'https://calendar.app.google/bmpsEQCsqqF3ZQgA9'

def img(stem, alt, w, h, sizes='100vw', lazy=True, cls='', webp=True, extra=''):
    if webp:
        src = f'img/{stem}.webp'
        srcset = f' srcset="img/{stem}-960.webp 960w, img/{stem}.webp {w}w" sizes="{sizes}"'
    else:
        src, srcset = f'img/{stem}.jpg', ''
    load = 'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return f'<img src="{src}"{srcset} width="{w}" height="{h}" alt="{alt}"{c} {load}{extra}>'

CSS = r'''
/* ============================================================
   DIRECCION A — OBRA PRIMERO
   Imagen a sangre, tipografía ancha (Archivo) y datos en mono.
   ============================================================ */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --ink: #0e0d0b;
  --ink-2: #181613;
  --paper: #f3f1ec;
  --paper-2: #e8e4da;
  --on-dark: #f3f1ec;
  --on-dark-muted: #bdb7ab;
  --on-light: #141311;
  --on-light-muted: #4f4a41;
  --gold: #d8c7a3;
  --bronze: #6f5c3c;
  --line-dark: rgba(243, 241, 236, 0.16);
  --line-light: rgba(20, 19, 17, 0.14);
  --font: 'Archivo', 'Arial Narrow', Arial, sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --ease: cubic-bezier(0.65, 0, 0.35, 1);
  --wrap: 1320px;
  --radius: 10px;
  --radius-sm: 6px;
  color-scheme: dark;
}
html { scroll-behavior: smooth; -webkit-font-smoothing: antialiased; }
body { font-family: var(--font); font-weight: 400; background: var(--ink); color: var(--on-dark); line-height: 1.55; overflow-x: hidden; }
img { display: block; max-width: 100%; height: auto; }
a { color: inherit; text-decoration: none; }
button { font: inherit; color: inherit; background: none; border: 0; cursor: pointer; }
:focus-visible { outline: 2px solid var(--gold); outline-offset: 3px; }
.wrap { max-width: var(--wrap); margin: 0 auto; padding-left: max(24px, env(safe-area-inset-left, 0px)); padding-right: max(24px, env(safe-area-inset-right, 0px)); }
.mono { font-family: var(--mono); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
.wide { font-stretch: 125%; }

/* ============================================================
   CABECERA
   ============================================================ */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  transition: background 0.4s ease, border-color 0.4s ease;
  border-bottom: 1px solid transparent;
  background: linear-gradient(180deg, rgba(14, 13, 11, 0.55), rgba(14, 13, 11, 0));
}
.nav.scrolled, .nav.solid { background: rgba(14, 13, 11, 0.94); border-bottom-color: var(--line-dark); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); }
.nav-inner { display: flex; align-items: center; gap: 40px; height: 76px; }
.brand { display: flex; align-items: center; gap: 14px; color: var(--on-dark); }
.brand svg { height: 24px; width: auto; }
.brand span { font-size: 12px; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; font-stretch: 110%; white-space: nowrap; }
.nav-menu { display: flex; gap: 28px; list-style: none; margin-left: auto; }
.nav-menu a { font-size: 13px; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; color: var(--on-dark-muted); transition: color 0.3s; }
.nav-menu a:hover, .nav-menu a[aria-current="page"] { color: var(--on-dark); }
.nav-cta { font-size: 13px; font-weight: 600; letter-spacing: 0.04em; padding: 12px 18px; background: var(--on-dark); color: var(--ink); white-space: nowrap; transition: background 0.3s; }
.nav-cta:hover { background: var(--gold); }
.nav-toggle { display: none; width: 44px; height: 44px; margin-left: auto; position: relative; }
.nav-toggle span { position: absolute; left: 11px; right: 11px; height: 1.5px; background: var(--on-dark); transition: transform 0.3s, opacity 0.3s; }
.nav-toggle span:nth-child(1) { top: 16px; } .nav-toggle span:nth-child(2) { top: 22px; } .nav-toggle span:nth-child(3) { top: 28px; }
.nav-toggle[aria-expanded="true"] span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
.nav-toggle[aria-expanded="true"] span:nth-child(2) { opacity: 0; }
.nav-toggle[aria-expanded="true"] span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }

/* ============================================================
   HERO
   ============================================================ */
.hero { position: relative; min-height: max(640px, min(100svh, 920px)); display: flex; align-items: flex-end; overflow: hidden; background: var(--ink-2); color: var(--on-dark); }
.hero-media { position: absolute; inset: 0; }
.hero-media img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transform: scale(1.05); transition: opacity 1s ease, transform 7s ease; }
.hero-media img.on { opacity: 1; transform: scale(1); }
.hero::after { content: ''; position: absolute; inset: 0; pointer-events: none; background: linear-gradient(90deg, rgba(14,13,11,0.72) 0%, rgba(14,13,11,0.38) 45%, rgba(14,13,11,0) 70%), linear-gradient(180deg, rgba(14,13,11,0.5) 0%, rgba(14,13,11,0) 24%, rgba(14,13,11,0.15) 50%, rgba(14,13,11,0.9) 100%); }
.hero-body { position: relative; z-index: 2; width: 100%; padding-top: 140px; padding-bottom: 48px; }
.hero-grid { display: grid; grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr); gap: 48px; align-items: end; }
.hero-kicker { font-family: var(--mono); font-size: 13px; font-weight: 500; text-shadow: 0 1px 12px rgba(0,0,0,0.5); letter-spacing: 0.12em; text-transform: uppercase; color: var(--gold); margin-bottom: 22px; }
.hero-slogan { font-weight: 800; font-stretch: 125%; font-size: clamp(52px, 8.8vw, 138px); line-height: 0.86; letter-spacing: -0.02em; text-transform: uppercase; text-wrap: balance; }
.hero-slogan span { display: block; font-weight: 300; font-stretch: 62%; color: var(--gold); }
.hero-sub { font-size: 18px; line-height: 1.55; color: rgba(243, 241, 236, 0.9); max-width: 48ch; margin-top: 26px; }
.hero-actions { display: flex; gap: 14px 28px; align-items: center; flex-wrap: wrap; margin-top: 32px; }
.btn { display: inline-flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 600; letter-spacing: 0.03em; padding: 17px 24px; transition: background 0.3s, color 0.3s, transform 0.3s; }
.btn-light { background: var(--on-dark); color: var(--ink); }
.btn-light:hover { background: var(--gold); transform: translateY(-2px); }
.btn-dark { background: var(--ink); color: var(--on-dark); }
.btn-dark:hover { background: var(--bronze); transform: translateY(-2px); }
.link { font-size: 14px; font-weight: 500; padding: 6px 0; border-bottom: 1px solid currentColor; transition: color 0.3s; }
.on-dark .link:hover, .hero .link:hover { color: var(--gold); }
.on-light .link:hover { color: var(--bronze); }
.hero-index { text-shadow: 0 1px 10px rgba(0,0,0,0.45); list-style: none; border-top: 1px solid rgba(243, 241, 236, 0.35); }
.hero-index button { width: 100%; display: grid; grid-template-columns: 34px minmax(0, 1fr) auto; gap: 12px; align-items: baseline; text-align: left; padding: 14px 0; border-bottom: 1px solid rgba(243, 241, 236, 0.35); color: rgba(243, 241, 236, 0.75); transition: color 0.3s, padding 0.3s; }
.hero-index .n, .hero-index .st { font-family: var(--mono); font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; }
.hero-index .name { font-size: 15px; font-weight: 500; }
.hero-index button[aria-pressed="true"], .hero-index button:hover, .hero-index button:focus-visible { color: var(--on-dark); padding-left: 8px; }
.hero-index button[aria-pressed="true"] .name { font-weight: 700; font-stretch: 125%; }
.hero-open { display: inline-block; margin-top: 16px; font-size: 13px; font-weight: 600; color: var(--gold); }
.hero-open:hover { color: var(--on-dark); }

/* ============================================================
   SECCIONES
   ============================================================ */
.section { padding: 128px 0; }
.on-dark { background: var(--ink); color: var(--on-dark); }
.on-dark-2 { background: var(--ink-2); color: var(--on-dark); }
.on-light { background: var(--paper); color: var(--on-light); }
.on-light-2 { background: var(--paper-2); color: var(--on-light); }
.sec-head { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 32px 64px; align-items: end; margin-bottom: 64px; }
.sec-label { display: block; margin-bottom: 18px; }
.on-dark .sec-label, .on-dark-2 .sec-label { color: var(--gold); }
.on-light .sec-label, .on-light-2 .sec-label { color: var(--bronze); }
.sec-title { font-weight: 800; font-stretch: 125%; font-size: clamp(40px, 6vw, 88px); line-height: 0.9; letter-spacing: -0.02em; text-transform: uppercase; text-wrap: balance; }
.sec-title span { display: block; font-weight: 300; font-stretch: 62%; }
.on-dark .sec-title span, .on-dark-2 .sec-title span { color: var(--gold); }
.on-light .sec-title span, .on-light-2 .sec-title span { color: var(--bronze); }
.sec-lead { font-size: 18px; line-height: 1.6; max-width: 52ch; }
.on-dark .sec-lead, .on-dark-2 .sec-lead { color: var(--on-dark-muted); }
.on-light .sec-lead, .on-light-2 .sec-lead { color: var(--on-light-muted); }

/* ---------- PROYECTOS ---------- */
.work { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 40px 24px; }
.work-card { grid-column: span 4; display: flex; flex-direction: column; gap: 16px; }
.work-card.big { grid-column: span 8; }
.work-card.half { grid-column: span 6; }
.work-img { overflow: hidden; aspect-ratio: 4 / 3; background: var(--paper-2); border-radius: var(--radius); }
.work-card.big .work-img { aspect-ratio: 16 / 10.6; }
.work-card.half .work-img { aspect-ratio: 16 / 10; }
.work-card.full { grid-column: span 12; }
.work-card.full .work-img { aspect-ratio: 21 / 8; }
.work-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s var(--ease); }
.work-card:hover .work-img img { transform: scale(1.04); }
.work-meta { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap; }
.work-name { font-size: 24px; font-weight: 700; font-stretch: 112%; letter-spacing: -0.01em; }
.work-card.big .work-name { font-size: 32px; }
.work-info { color: var(--on-light-muted); }
.status { font-family: var(--mono); font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; padding: 5px 9px; border-radius: 3px; border: 1px solid var(--line-light); color: var(--on-light); white-space: nowrap; }
.status.built { background: var(--on-light); color: var(--paper); border-color: var(--on-light); }

/* ---------- SERVICIOS ---------- */
.routes { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--line-dark); }
.route { display: flex; flex-direction: column; gap: 18px; padding: 40px 32px 44px 0; border-right: 1px solid var(--line-dark); transition: background 0.4s; }
.route + .route { padding-left: 32px; }
.route:last-child { border-right: 0; }
.route.lead-route { border-top: 2px solid var(--gold); margin-top: -1px; }
.route-who { color: var(--gold); }
.route-title { font-size: clamp(26px, 2.4vw, 34px); font-weight: 700; font-stretch: 112%; line-height: 1.08; letter-spacing: -0.01em; text-wrap: balance; }
.route-text { color: var(--on-dark-muted); font-size: 16px; line-height: 1.6; }
.route ul { list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 14px; color: var(--on-dark); }
.route li::before { content: '—'; color: var(--gold); margin-right: 10px; }
.route .link { margin-top: auto; align-self: flex-start; }
.specialties { margin-top: 72px; }
.spec-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.spec-card { display: flex; flex-direction: column; gap: 12px; padding: 28px; border: 1px solid var(--line-dark); border-radius: var(--radius); transition: border-color 0.3s, background 0.3s; }
.spec-card:hover, .spec-card:focus-visible { border-color: var(--gold); background: var(--ink-2); }
.spec-card h3 { font-size: 22px; font-weight: 700; font-stretch: 112%; }
.spec-card p { color: var(--on-dark-muted); font-size: 15px; line-height: 1.6; }
.spec-card .link { margin-top: auto; align-self: flex-start; font-size: 13px; }

/* ---------- PROCESO ---------- */
.steps { list-style: none; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0; border-top: 1px solid var(--line-light); counter-reset: s; }
.step { padding: 36px 28px 36px 0; border-right: 1px solid var(--line-light); }
.step + .step { padding-left: 28px; }
.step:last-child { border-right: 0; }
.step-n { font-size: 64px; font-weight: 200; font-stretch: 62%; line-height: 1; color: var(--bronze); margin-bottom: 22px; }
.step-name { font-size: 22px; font-weight: 700; font-stretch: 112%; line-height: 1.15; margin-bottom: 12px; }
.step-text { font-size: 15px; color: var(--on-light-muted); line-height: 1.6; margin-bottom: 18px; }
.step-deliv { font-size: 14px; line-height: 1.5; }
.step-deliv b { display: block; font-family: var(--mono); font-size: 12px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: var(--bronze); margin-bottom: 4px; }
.cta-row { display: flex; gap: 16px 32px; align-items: center; flex-wrap: wrap; margin-top: 56px; }

/* ---------- DIFERENCIAL / ONA ---------- */
.thesis { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 64px; align-items: start; }
.thesis-quote { font-weight: 300; font-stretch: 75%; font-size: clamp(36px, 4.6vw, 68px); line-height: 1.02; letter-spacing: -0.02em; text-wrap: balance; }
.thesis-quote b { font-weight: 800; font-stretch: 125%; color: var(--gold); }
.thesis-text { color: var(--on-dark-muted); font-size: 17px; line-height: 1.65; display: flex; flex-direction: column; gap: 16px; }
.thesis-text strong { color: var(--on-dark); font-weight: 500; }
.figures { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); margin: 96px 0 0; border-top: 1px solid var(--line-dark); }
.figures div { padding: 26px 20px 0 0; }
.figures dt { color: var(--on-dark-muted); margin-bottom: 12px; }
.figures dd { font-size: clamp(34px, 4vw, 60px); font-weight: 300; font-stretch: 75%; line-height: 1; font-variant-numeric: tabular-nums; }
.figures dd small { font-size: 0.5em; color: var(--gold); }
.ona { margin-top: 96px; display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 24px 48px; }
.ona-gallery { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 8px; grid-auto-rows: 150px; }
.ona-gallery figure { overflow: hidden; background: var(--ink); border-radius: var(--radius-sm); }
.ona-gallery figure.g1, .ona-gallery figure.g5, .ona-gallery figure.g6 { border-radius: var(--radius); }
.ona-gallery img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s var(--ease); }
.ona-gallery figure:hover img { transform: scale(1.04); }
.g1 { grid-column: span 6; grid-row: span 2; } .g2, .g3, .g4 { grid-column: span 2; } .g5, .g6 { grid-column: span 3; grid-row: span 2; }
.ona-name { font-size: clamp(64px, 9vw, 128px); font-weight: 800; font-stretch: 125%; line-height: 0.85; letter-spacing: -0.03em; }
.ona-tag { color: var(--gold); margin: 14px 0 26px; }
.ona-text { color: var(--on-dark-muted); font-size: 16px; line-height: 1.65; margin-bottom: 28px; }
.spec { border-top: 1px solid var(--line-dark); margin-bottom: 28px; }
.spec div { display: flex; justify-content: space-between; gap: 16px; padding: 12px 0; border-bottom: 1px solid var(--line-dark); font-size: 14px; }
.spec dt { color: var(--on-dark-muted); }
.spec dd { text-align: right; }
.disclaimer { font-size: 13px; color: var(--on-dark-muted); line-height: 1.55; margin-top: 18px; max-width: 52ch; }
.models { margin-top: 96px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.model { border: 1px solid var(--line-dark); padding: 28px; display: flex; flex-direction: column; gap: 12px; }
.model h3 { font-size: 20px; font-weight: 700; font-stretch: 112%; }
.model .who { color: var(--gold); }
.model p { font-size: 15px; color: var(--on-dark-muted); line-height: 1.6; }
.model .link { margin-top: auto; align-self: flex-start; font-size: 13px; }

/* ---------- ESTUDIO ---------- */
.studio { display: grid; grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); gap: 72px; align-items: start; }
.studio-photo img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: center top; border-radius: var(--radius); }
.studio-photo figcaption { display: flex; justify-content: space-between; gap: 12px; padding-top: 14px; }
.studio-photo figcaption strong { font-size: 18px; font-weight: 700; font-stretch: 112%; }
.studio-photo figcaption span { color: var(--bronze); }
.studio-quote { font-weight: 300; font-stretch: 75%; font-size: clamp(28px, 3.2vw, 44px); line-height: 1.12; letter-spacing: -0.01em; margin-bottom: 36px; text-wrap: balance; }
.studio-bio { font-size: 17px; color: var(--on-light-muted); line-height: 1.7; display: flex; flex-direction: column; gap: 16px; max-width: 62ch; }
.studio-meta { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 36px; padding-top: 28px; border-top: 1px solid var(--line-light); }
.studio-meta dt { color: var(--bronze); margin-bottom: 8px; }
.studio-meta dd { font-size: 15px; line-height: 1.6; }

/* ---------- CONTACTO ---------- */
.contact { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 72px; align-items: start; }
.agenda { border: 1px solid var(--line-dark); padding: 32px; margin: 40px 0 32px; }
.agenda h3 { font-size: 24px; font-weight: 700; font-stretch: 112%; margin: 10px 0 12px; }
.host { display: flex; align-items: center; gap: 16px; margin: 20px 0 4px; }
.host img { width: 64px; height: 64px; object-fit: cover; border-radius: var(--radius); flex-shrink: 0; }
.host strong { display: block; font-size: 17px; font-weight: 700; font-stretch: 112%; }
.host span { color: var(--gold); }
.host-photo { margin: 36px 0 0; max-width: 360px; }
.host-photo img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: center 30%; border-radius: var(--radius); }
.host-photo figcaption { display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; padding-top: 12px; }
.host-photo figcaption strong { font-weight: 700; font-stretch: 112%; }
.host-photo figcaption span { color: var(--gold); }
.agenda p { color: var(--on-dark-muted); font-size: 15px; line-height: 1.6; margin-bottom: 8px; }
.agenda ul { list-style: none; margin: 18px 0 24px; display: flex; flex-direction: column; gap: 8px; font-size: 15px; }
.agenda li::before { content: '—'; color: var(--gold); margin-right: 10px; }
.channels { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.channels dt { color: var(--gold); margin-bottom: 6px; }
.channels dd { font-size: 16px; }
.channels a:hover { color: var(--gold); }
.form { background: var(--ink-2); border: 1px solid var(--line-dark); padding: 40px; }
.form-title { font-size: 26px; font-weight: 700; font-stretch: 112%; margin: 10px 0 28px; }
.field { display: flex; flex-direction: column; gap: 8px; margin-bottom: 22px; }
.field label { font-family: var(--mono); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--on-dark-muted); }
.field input, .field select, .field textarea { width: 100%; font: inherit; font-size: 16px; color: var(--on-dark); background: transparent; border: 0; border-bottom: 1px solid rgba(243, 241, 236, 0.32); padding: 10px 0; border-radius: 0; }
.field select { appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%23d8c7a3' d='M6 8L0 0h12z'/%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right center; padding-right: 24px; }
.field select option { background: var(--ink); color: var(--on-dark); }
.field input::placeholder, .field textarea::placeholder { color: rgba(243, 241, 236, 0.5); }
.field input:focus, .field select:focus, .field textarea:focus { outline: none; border-bottom-color: var(--gold); }
.field textarea { min-height: 96px; resize: vertical; }
.row { display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; }
.form-submit { width: 100%; justify-content: center; margin-top: 8px; }
.form-error { display: none; margin-top: 14px; font-size: 14px; color: #f0a58f; }
.form-success { display: none; padding: 24px 0; }
.form-success h3 { font-size: 26px; font-weight: 700; font-stretch: 112%; margin-bottom: 10px; }
.form-success p { color: var(--on-dark-muted); }

/* ---------- PIE ---------- */
.footer { background: var(--ink); color: var(--on-dark); border-top: 1px solid var(--line-dark); padding: 72px 0 40px; }
.footer-grid { display: grid; grid-template-columns: minmax(0, 1.6fr) repeat(3, minmax(0, 1fr)); gap: 40px; margin-bottom: 56px; }
.footer-brand svg { height: 40px; width: auto; color: var(--on-dark); margin-bottom: 18px; }
.footer-brand p { color: var(--on-dark-muted); font-size: 15px; max-width: 34ch; }
.footer-brand .slogan { font-weight: 800; font-stretch: 125%; text-transform: uppercase; font-size: 15px; color: var(--on-dark); margin-bottom: 6px; }
.footer h4 { color: var(--gold); margin-bottom: 16px; font-weight: 500; }
.footer ul { list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 15px; color: var(--on-dark-muted); }
.footer ul a:hover { color: var(--on-dark); }
.footer-bottom { display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; padding-top: 24px; border-top: 1px solid var(--line-dark); color: var(--on-dark-muted); font-size: 13px; }

/* ---------- WHATSAPP FLOTANTE ---------- */
.wa-float { position: fixed; z-index: 90; right: max(20px, env(safe-area-inset-right, 0px)); bottom: max(20px, env(safe-area-inset-bottom, 0px)); width: 54px; height: 54px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: var(--on-dark); color: var(--ink); box-shadow: 0 8px 28px rgba(0, 0, 0, 0.35); transition: background 0.3s, transform 0.3s; }
.wa-float:hover { background: var(--gold); transform: translateY(-2px); }
.wa-float svg { width: 26px; height: 26px; }

/* ---------- PENDIENTES (solo vista previa: bloquean publicación) ---------- */
.pending { display: inline-block; border: 1px dashed currentColor; padding: 3px 9px; font-family: var(--mono); font-size: 12px; letter-spacing: 0.02em; line-height: 1.5; }
.on-dark .pending, .on-dark-2 .pending { color: var(--gold); }
.on-light .pending, .on-light-2 .pending { color: var(--bronze); }

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 1560px) and (min-width: 1280px) {
  .brand span { display: none; }
  .nav-inner { gap: 28px; }
  .nav-menu { gap: 22px; }
}
@media (max-width: 1279px) {
  .nav-menu, .nav-inner > .nav-cta { display: none; }
  .nav-toggle { display: block; }
  .nav-menu.open { display: flex; position: fixed; inset: 76px 0 0; flex-direction: column; gap: 0; margin: 0; padding: 16px max(24px, env(safe-area-inset-left, 0px)) 40px; background: var(--ink); overflow-y: auto; }
  .nav-menu.open a { display: block; font-size: 22px; font-weight: 700; font-stretch: 112%; letter-spacing: 0; text-transform: none; color: var(--on-dark); padding: 18px 0; border-bottom: 1px solid var(--line-dark); }
  .nav-menu.open .menu-cta a { margin-top: 24px; border: 0; background: var(--on-dark); color: var(--ink); text-align: center; font-size: 16px; padding: 18px; }
}
@media (max-width: 1100px) {
  .hero-grid, .thesis, .ona, .studio, .contact, .sec-head { grid-template-columns: 1fr; }
  .routes, .models, .spec-grid { grid-template-columns: 1fr; }
  .route, .route + .route { padding: 36px 0; border-right: 0; border-bottom: 1px solid var(--line-dark); }
  .steps { grid-template-columns: 1fr 1fr; }
  .step, .step + .step { padding: 32px 24px 32px 0; border-right: 0; border-bottom: 1px solid var(--line-light); }
  .step:nth-child(even) { padding-left: 24px; border-left: 1px solid var(--line-light); }
  .work-card, .work-card.big, .work-card.half { grid-column: span 6; }
  .work-card.big, .work-card.full { grid-column: span 12; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
}
@media (min-width: 1280px) { .menu-cta { display: none; } }
@media (max-width: 640px) {
  .wrap { padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }
  .section { padding: 88px 0; }
  .brand span { display: none; }
  .hero-body { padding-top: 120px; padding-bottom: 40px; }
  /* En móvil la sección Proyectos sigue al hero: el índice sobra y choca con WhatsApp */
  #heroIndex, #heroOpen { display: none; }
  .hero::after { background: linear-gradient(180deg, rgba(14,13,11,0.55) 0%, rgba(14,13,11,0.6) 30%, rgba(14,13,11,0.62) 60%, rgba(14,13,11,0.92) 100%); }
  .hero-sub { font-size: 16px; }
  .hero-actions .btn { width: 100%; justify-content: center; }
  .work { grid-template-columns: 1fr; gap: 36px; }
  .work-card, .work-card.big, .work-card.half, .work-card.full { grid-column: auto; }
  .work-card.big .work-img, .work-card.half .work-img, .work-card.full .work-img { aspect-ratio: 4 / 3; }
  .steps { grid-template-columns: 1fr; }
  .step:nth-child(even) { padding-left: 0; border-left: 0; }
  .figures { grid-template-columns: 1fr 1fr; gap: 0 16px; }
  .figures div { padding-bottom: 20px; }
  .ona-gallery { grid-auto-rows: 110px; }
  .row, .channels, .studio-meta { grid-template-columns: 1fr; }
  .form, .agenda { padding: 26px 20px; }
  .footer-grid { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; }
  .hero-media img { transform: none; }
}
'''

LOGO_MARK = '''<svg viewBox="0 0 800 270" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="15" stroke-linejoin="round"><path d="M 17,25 L 320,25 Q 378,25 378,80 Q 378,135 320,135 L 17,135 L 320,135 Q 378,135 378,190 Q 378,245 320,245 L 17,245"/><path d="M 784,25 L 475,25 Q 417,25 417,80 L 417,190 Q 417,245 475,245 L 784,245"/></g><circle cx="78" cy="80" r="15" fill="currentColor"/><circle cx="78" cy="190" r="15" fill="currentColor"/></svg>'''

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.08 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35zM12.04 21.5h-.01a9.4 9.4 0 0 1-4.8-1.31l-.34-.2-3.57.93.95-3.48-.22-.36a9.4 9.4 0 0 1-1.44-5.02c0-5.2 4.23-9.43 9.44-9.43 2.52 0 4.89.98 6.67 2.77a9.37 9.37 0 0 1 2.76 6.67c0 5.2-4.24 9.43-9.44 9.43zm8.03-17.46A11.27 11.27 0 0 0 12.04.7C5.78.7.68 5.8.68 12.06c0 2 .52 3.96 1.52 5.68L.58 23.7l6.1-1.6a11.33 11.33 0 0 0 5.36 1.37h.01c6.26 0 11.36-5.1 11.36-11.36 0-3.04-1.18-5.89-3.33-8.04z"/></svg>'

def head(title, desc, url, og, jsonld):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e0d0b">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_GT">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{json.dumps(jsonld, ensure_ascii=False, indent=2)}
</script>

<!-- ============ FUENTES (Archivo ancho variable + JetBrains Mono para datos) ============ -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,200..800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
'''

def nav(current, home_prefix):
    p = home_prefix
    items = [('Servicios', f'{p}#servicios'), ('Prefactibilidad', 'prefactibilidad-inmobiliaria.html'),
             ('Diseño para negocios', 'diseno-estrategico.html'), ('Proyectos', f'{p}#proyectos'),
             ('ONA', f'{p}#ona'), ('Estudio', f'{p}#estudio'), ('Contacto', f'{p}#contacto')]
    lis = '\n'.join(f'      <li><a href="{h}"{" aria-current=\"page\"" if n == current else ""}>{n}</a></li>' for n, h in items)
    solid = ' solid' if current == 'Prefactibilidad' else ''
    return f'''<!-- ============================================================
     CABECERA
     ============================================================ -->
<header class="nav{solid}" id="nav">
  <div class="wrap nav-inner">
    <a href="{p or 'index.html'}" class="brand" aria-label="{BRAND} — Inicio">{LOGO_MARK}<span>{BRAND}</span></a>
    <ul class="nav-menu" id="navMenu">
{lis}
      <li class="menu-cta"><a href="prefactibilidad-inmobiliaria.html#solicitar">Solicitar diagnóstico de terreno</a></li>
    </ul>
    <a href="prefactibilidad-inmobiliaria.html#solicitar" class="nav-cta">Diagnóstico de terreno</a>
    <button type="button" class="nav-toggle" id="navToggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="navMenu"><span></span><span></span><span></span></button>
  </div>
</header>
'''

def footer(p):
    return f'''
<!-- ============================================================
     PIE
     ============================================================ -->
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        {LOGO_MARK}
        <p class="slogan">Del terreno al retorno.</p>
        <p>{BRAND}. Arquitectura, prefactibilidad y desarrollo inmobiliario. Ciudad de Guatemala.</p>
      </div>
      <div>
        <h4 class="mono">Servicios</h4>
        <ul>
          <li><a href="prefactibilidad-inmobiliaria.html">Prefactibilidad</a></li>
          <li><a href="diseno-estrategico.html">Diseño para negocios</a></li>
          <li><a href="{p}#modelos">Co-desarrollo e inversión</a></li>
        </ul>
      </div>
      <div>
        <h4 class="mono">Proyectos</h4>
        <ul>
          <li><a href="{p}#ona">ONA</a></li>
          <li><a href="kishi-books.html">Kishi Books</a></li>
          <li><a href="navante.html">Navante</a></li>
          <li><a href="petshop-gt.html">Petshop GT</a></li>
          <li><a href="casa-milpas-altas.html">Casa Milpas Altas</a></li>
          <li><a href="edificio-w.html">Edificio W</a></li>
          <li><a href="la-autoria.html">La Autoría</a></li>
        </ul>
      </div>
      <div>
        <h4 class="mono">Contacto</h4>
        <ul>
          <li><a href="mailto:info@bcarqstudio.com">info@bcarqstudio.com</a></li>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp +502 5413 1753</a></li>
          <li><a href="{CAL}" target="_blank" rel="noopener">Agendar llamada</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 {BRAND} · Ciudad de Guatemala</span>
      <span>bcarqstudio.com</span>
    </div>
  </div>
</footer>

<!-- WHATSAPP FLOTANTE -->
<a href="{WA}{WA_TXT}" class="wa-float" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{WA_ICON}</a>
'''

FORM_JS = '''
// ============================================================
// FORMULARIO — Formspree AJAX
// ============================================================
const FORMSPREE_ID = 'xbdbdlay';
const form = document.getElementById('contactForm');
if (form) {
  const tipoParam = new URLSearchParams(location.search).get('tipo');
  const tipoSel = document.getElementById('type');
  if (tipoParam && tipoSel) {
    const opt = tipoSel.querySelector(`option[value="${CSS.escape(tipoParam)}"]`);
    if (opt) opt.selected = true;
  }
  const btn = document.getElementById('formSubmitBtn');
  const err = document.getElementById('formError');
  const label = btn.textContent;
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { err.style.display = 'block'; form.reportValidity(); return; }
    btn.textContent = 'Enviando…';
    btn.disabled = true;
    err.style.display = 'none';
    try {
      const res = await fetch(`https://formspree.io/f/${FORMSPREE_ID}`, {
        method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' }
      });
      if (!res.ok) throw new Error('server');
      document.getElementById('formBody').style.display = 'none';
      document.getElementById('formSuccess').style.display = 'block';
    } catch {
      btn.textContent = label;
      btn.disabled = false;
      err.style.display = 'block';
    }
  });
}
'''

BASE_JS = '''
<script>
// ============================================================
// CABECERA — fondo sólido al hacer scroll + menú móvil
// ============================================================
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const setMenu = (open) => {
  navMenu.classList.toggle('open', open);
  navToggle.setAttribute('aria-expanded', String(open));
  navToggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  nav.classList.toggle('solid', open || nav.dataset.solid === '1');
  document.body.style.overflow = open ? 'hidden' : '';
};
nav.dataset.solid = nav.classList.contains('solid') ? '1' : '';
navToggle.addEventListener('click', () => setMenu(!navMenu.classList.contains('open')));
navMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
%EXTRA%
</script>

</body>
</html>
'''

def contact_fields(prefact=False):
    if prefact:
        tipo = '<input type="hidden" name="project_type" value="diagnostico-terreno">'
        select_tipo = ''
        subject = 'Solicitud de diagnóstico de terreno — Build &amp; Create Studio'
        stage_opts = '''<option value="evaluando-terreno">Evaluando comprar el terreno</option>
              <option value="tengo-terreno">Ya tengo el terreno</option>
              <option value="desarrollador">Soy desarrollador y evalúo una oportunidad</option>'''
        use = '''<div class="field">
            <label for="use">Uso que imaginas</label>
            <select id="use" name="uso">
              <option value="">Selecciona una opción</option>
              <option value="residencial">Residencial (casas o apartamentos)</option>
              <option value="comercial">Comercial u oficinas</option>
              <option value="mixto">Uso mixto</option>
              <option value="no-se">Aún no lo sé</option>
            </select>
          </div>'''
        loc_label, area_label, req = 'Ubicación del terreno', 'm² del terreno', ' required'
        submit = 'Solicitar diagnóstico →'
        title = 'Datos del terreno'
        eyebrow = 'Diagnóstico de terreno'
        msg_ph = 'Lo que sepas del terreno y lo que te gustaría lograr'
    else:
        tipo = ''
        select_tipo = '''<div class="field">
            <label for="type">Tipo de proyecto</label>
            <select id="type" name="project_type" required>
              <option value="">Selecciona una opción</option>
              <option value="diagnostico-terreno">Diagnóstico de terreno / prefactibilidad</option>
              <option value="diseño-estratégico">Diseño estratégico para desarrolladores</option>
              <option value="diseño-comercial">Diseño de oficinas, clínicas o comercios</option>
              <option value="diseño-interior">Diseño interior</option>
              <option value="remodelación">Remodelación</option>
              <option value="mobiliario-estratégico">Mobiliario estratégico</option>
              <option value="co-desarrollo">Co-desarrollo integral (tengo un terreno)</option>
              <option value="inversión">Inversión en proyectos propios</option>
              <option value="otro">Otro / Conversación inicial</option>
            </select>
          </div>'''
        subject = 'Nuevo mensaje — Build &amp; Create Studio'
        stage_opts = '''<option value="evaluando-terreno">Evaluando comprar un terreno</option>
              <option value="tengo-terreno">Tengo el terreno, sin diseño</option>
              <option value="tengo-anteproyecto">Tengo anteproyecto o planos</option>
              <option value="espacio-existente">Tengo un espacio para diseñar o remodelar</option>
              <option value="inversion">Busco invertir</option>'''
        use = ''
        loc_label, area_label, req = 'Ubicación', 'm² aproximados', ''
        submit = 'Enviar mensaje →'
        title = 'Cuéntanos qué traes al estudio'
        eyebrow = 'Formulario de contacto'
        msg_ph = 'Cuéntanos brevemente qué buscas'
    stage_req = ' required' if prefact else ''
    return f'''<form class="form" id="contactForm" novalidate>
        <input type="hidden" name="_subject" value="{subject}">
        {tipo}
        <div id="formBody">
          <span class="mono" style="color:var(--gold)">{eyebrow}</span>
          <h3 class="form-title">{title}</h3>
          <div class="field">
            <label for="name">Nombre completo</label>
            <input type="text" id="name" name="name" required placeholder="Tu nombre" autocomplete="name">
          </div>
          <div class="row">
            <div class="field">
              <label for="email">Correo electrónico</label>
              <input type="email" id="email" name="email" required placeholder="tu@empresa.com" autocomplete="email">
            </div>
            <div class="field">
              <label for="phone">Teléfono o WhatsApp</label>
              <input type="tel" id="phone" name="telefono" placeholder="+502 0000 0000" autocomplete="tel">
            </div>
          </div>
          {select_tipo}
          <div class="row">
            <div class="field">
              <label for="location">{loc_label}</label>
              <input type="text" id="location" name="ubicacion" placeholder="Zona o municipio"{req}>
            </div>
            <div class="field">
              <label for="area">{area_label}</label>
              <input type="text" id="area" name="metros_cuadrados" placeholder="Aproximado" inputmode="numeric">
            </div>
          </div>
          {use}
          <div class="field">
            <label for="stage">Etapa</label>
            <select id="stage" name="etapa"{stage_req}>
              <option value="">Selecciona una opción</option>
              {stage_opts}
            </select>
          </div>
          <div class="field">
            <label for="message">Mensaje</label>
            <textarea id="message" name="message" placeholder="{msg_ph}"{'' if prefact else ' required'}></textarea>
          </div>
          <button type="submit" class="btn btn-light form-submit" id="formSubmitBtn">{submit}</button>
          <p class="form-error" id="formError" role="alert">Revisa los campos obligatorios o escríbenos a info@bcarqstudio.com</p>
        </div>
        <div class="form-success" id="formSuccess" role="status">
          <h3>Mensaje recibido</h3>
          <p>Te respondemos en menos de 24 horas hábiles. Revisa también tu carpeta de spam.</p>
        </div>
      </form>'''

ORG = {"@id": SITE + "#organizacion"}

# ================================================================== HOME
HOME_TITLE = 'Estudio de arquitectura en Guatemala | Build &amp; Create Studio'
HOME_DESC = 'Arquitectura en Ciudad de Guatemala: diagnóstico de terreno, prefactibilidad, diseño arquitectónico y desarrollo inmobiliario. Del terreno al retorno.'
home_ld = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "#organizacion",
    "name": BRAND_TXT, "alternateName": "BC Studio", "description": HOME_DESC, "url": SITE,
    "logo": SITE + "favicon.svg", "image": SITE + "img/ona-fachada-atardecer-og.jpg",
    "email": "info@bcarqstudio.com", "telephone": "+502 5413 1753",
    "address": {"@type": "PostalAddress", "addressLocality": "Ciudad de Guatemala", "addressCountry": "GT"},
    "areaServed": [{"@type": "Country", "name": "Guatemala"}, {"@type": "Country", "name": "Honduras"}], "foundingDate": "2025",
    "founder": {"@type": "Person", "name": "Bryan Castro", "jobTitle": "Arquitecto y desarrollador inmobiliario", "image": SITE + "img/bryan-castro-frontal.webp"},
    "knowsAbout": ["Arquitectura", "Prefactibilidad inmobiliaria", "Desarrollo inmobiliario", "Diseño interior", "Remodelaciones", "Mobiliario a la medida", "Estructuración de inversión inmobiliaria"]}

# ================================================================== TESTIMONIO (Kishi Books)
# Texto aprobado por la clienta (Ady Hernández, fundadora de Kishi Books).
TESTI_QUOTE = 'Gracias al diseño bien implementado, hemos logrado transmitir con mayor fuerza <em>la esencia de la marca</em>, abriéndonos puertas en más centros comerciales del país. Vamos por nuestra cuarta tienda con BC Studio.'
TESTI_NAME = 'Ady Hernández'
TESTI_ROLE = 'Fundadora · Kishi Books'
TESTI_CSS = """
/* ===== TESTIMONIO ===== */
.testi { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 64px; align-items: center; }
.testi-img { margin: 0; overflow: hidden; border-radius: var(--radius); }
.testi-img img { width: 100%; height: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.testi blockquote { margin: 0; }
.testi blockquote p { margin: 18px 0 0; font-weight: 300; font-stretch: 75%; font-size: clamp(28px, 3.4vw, 50px); line-height: 1.08; letter-spacing: -0.02em; text-wrap: balance; }
.testi blockquote p em { font-style: normal; font-weight: 800; font-stretch: 125%; color: var(--gold); }
.testi .by { display: flex; align-items: center; gap: 14px; margin-top: 32px; }
.testi .by img { width: 56px; height: 56px; object-fit: cover; border-radius: var(--radius); }
.testi .by .mono { color: var(--gold); }
@media (max-width: 900px) { .testi { grid-template-columns: 1fr; gap: 36px; } }
"""
def testimonio(link=True):
    more = '\n        <div class="cta-row"><a href="kishi-books.html" class="link">Ver el proyecto Kishi Books</a></div>' if link else ''
    return f"""<section class="section on-dark-2" id="testimonio">
  <div class="wrap testi">
    <figure class="testi-img">{img('kishi-books-inauguracion', 'Ady Hernández, fundadora de Kishi Books, con Bryan Castro en la inauguración del kiosco de Peri Roosevelt', 1920, 1442, sizes='(max-width: 900px) 100vw, 40vw')}</figure>
    <div>
      <span class="mono sec-label">Testimonio · Cliente desde 2024</span>
      <blockquote>
        <p>«{TESTI_QUOTE}»</p>
        <footer class="by"><img src="img/kishi-books-clienta-avatar.webp" width="320" height="320" alt="Ady Hernández, fundadora de Kishi Books" loading="lazy" decoding="async"><div><strong>{TESTI_NAME}</strong><br><span class="mono">{TESTI_ROLE}</span></div></footer>
      </blockquote>{more}
    </div>
  </div>
</section>"""

HERO_PROJECTS = [
    ('edificio-w-aerea', 'webp', 1920, 1080, 'Edificio W, uso mixto en esquina, San Pedro Sula, Honduras', 'Edificio W · San Pedro Sula', 'En aprobación', 'edificio-w.html'),
    ('kishi-books-escalera', 'webp', 1920, 1442, 'Kiosco de madera curvada de Kishi Books, Peri Roosevelt, Ciudad de Guatemala', 'Kishi Books · 3 sedes', 'Construido', 'kishi-books.html'),
    ('navante-lampara', 'webp', 1920, 1407, 'Lámpara colgante lineal curva sobre las estaciones de trabajo de Navante', 'Navante · Oficina', 'Construido', 'navante.html'),
    ('ona-fachada-atardecer', 'jpg', 1365, 768, 'Torre residencial ONA al atardecer, Zona 15, Ciudad de Guatemala', 'ONA · Zona 15', 'En desarrollo', '#ona'),
    ('restaurante-interior', 'webp', 1344, 768, 'Salón del restaurante La Autoría con cocina de fuego, Huehuetenango', 'La Autoría · Salón', 'Diseño completado', 'la-autoria.html'),
]
hero_imgs = '\n    '.join(
    img(s, a, w, h, lazy=(i > 0), cls='on' if i == 0 else '', webp=(ext == 'webp'))
    for i, (s, ext, w, h, a, *_r) in enumerate(HERO_PROJECTS))
hero_btns = '\n          '.join(
    f'<li><button type="button" aria-pressed="{"true" if i == 0 else "false"}" data-i="{i}" data-href="{href}"><span class="n">{i+1:02d}</span><span class="name">{name}</span><span class="st">{st}</span></button></li>'
    for i, (s, ext, w, h, a, name, st, href) in enumerate(HERO_PROJECTS))

HOME = head(HOME_TITLE, HOME_DESC, SITE, 'img/ona-fachada-atardecer-og.jpg', home_ld) + nav('', '') + f'''
<main>
<!-- ============================================================
     01 · HERO — EL TRABAJO A PANTALLA COMPLETA
     ============================================================ -->
<section class="hero" id="inicio" aria-label="Proyectos destacados">
  <div class="hero-media" id="heroMedia">
    {hero_imgs}
  </div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <h1 class="hero-kicker">Arquitectura, diseño comercial y prefactibilidad en Guatemala y Honduras</h1>
        <p class="hero-slogan">Del terreno <span>al retorno.</span></p>
        <p class="hero-sub">Te decimos qué puedes construir en tu terreno y si los números cierran. Después lo diseñamos y lo desarrollamos contigo.</p>
        <div class="hero-actions">
          <a href="prefactibilidad-inmobiliaria.html" class="btn btn-light">Solicitar diagnóstico de terreno →</a>
          <a href="#proyectos" class="link">Ver proyectos</a>
        </div>
      </div>
      <div>
        <ol class="hero-index" id="heroIndex" aria-label="Elegir proyecto">
          {hero_btns}
        </ol>
        <a href="edificio-w.html" class="hero-open" id="heroOpen">Ver proyecto →</a>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     02 · PROYECTOS
     ============================================================ -->
<section class="section on-light" id="proyectos">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Proyectos · 07</span>
        <h2 class="sec-title">Trabajo <span>reciente.</span></h2>
      </div>
      <p class="sec-lead">Mobiliario comercial, oficinas, comercio, uso mixto, vivienda, residencial vertical y gastronomía, en Guatemala y Honduras. Cada ficha indica el estado real del proyecto.</p>
    </div>
    <div class="work">
      <a href="edificio-w.html" class="work-card full">
        <div class="work-img">{img('edificio-w-aerea', 'Vista aérea del Edificio W en esquina, San Pedro Sula, Honduras', 1920, 1080, sizes='100vw')}</div>
        <div class="work-meta"><span class="work-name">Edificio W</span><span class="status">Anteproyecto · En aprobación</span></div>
        <p class="work-info">Uso mixto · 8 apartamentos + 2 locales · 591.86 m² · San Pedro Sula, Honduras</p>
      </a>
      <a href="kishi-books.html" class="work-card half">
        <div class="work-img">{img('kishi-books-escalera', 'Kiosco de madera curvada de Kishi Books, Peri Roosevelt', 1920, 1442, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Kishi Books</span><span class="status built">Construido · 3 sedes</span></div>
        <p class="work-info">Mobiliario comercial · Peri Roosevelt, Naranjo Mall y Plaza Girasoles, Chiquimula · Diseño y ejecución · 2024–2026</p>
      </a>
      <a href="navante.html" class="work-card half">
        <div class="work-img">{img('navante-lampara', 'Lámpara colgante lineal curva sobre las estaciones de trabajo de Navante', 1920, 1407, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Navante</span><span class="status built">Construido</span></div>
        <p class="work-info">Oficina · 96 m² · Diseño interior, ejecución y mobiliario · 2026</p>
      </a>
      <a href="petshop-gt.html" class="work-card half">
        <div class="work-img">{img('petshop-gt-recepcion', 'Render de la recepción de Petshop GT, Vista Hermosa, Zona 15', 1920, 1080, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Petshop GT</span><span class="status">Diseño aprobado</span></div>
        <p class="work-info">Tienda de mascotas · 70 m² · Vista Hermosa, Zona 15</p>
      </a>
      <a href="#ona" class="work-card half">
        <div class="work-img">{img('ona-fachada-atardecer', 'Torre residencial ONA al atardecer, Zona 15, Ciudad de Guatemala', 1365, 768, webp=False)}</div>
        <div class="work-meta"><span class="work-name">ONA</span><span class="status">En fase de desarrollo</span></div>
        <p class="work-info">Residencial vertical · 18,792 m² · Zona 15, Vista Hermosa I</p>
      </a>
      <a href="la-autoria.html" class="work-card half">
        <div class="work-img">{img('restaurante-interior', 'Salón del restaurante La Autoría, Huehuetenango', 1344, 768, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">La Autoría</span><span class="status">Diseño completado</span></div>
        <p class="work-info">Restaurante · 240 m² · Huehuetenango</p>
      </a>
      <a href="casa-milpas-altas.html" class="work-card half">
        <div class="work-img">{img('casa-milpas-altas-fachada', 'Render de Casa Milpas Altas en la ladera, San Miguel Milpas Altas, Sacatepéquez', 1920, 1080, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Casa Milpas Altas</span><span class="status">Diseño completado</span></div>
        <p class="work-info">Vivienda · 120 m² · San Miguel Milpas Altas, Sacatepéquez</p>
      </a>
    </div>
  </div>
</section>

<!-- ============================================================
     TESTIMONIO
     ============================================================ -->
{testimonio()}

<!-- ============================================================
     03 · SERVICIOS — TRES PUNTOS DE PARTIDA
     ============================================================ -->
<section class="section on-dark" id="servicios">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Servicios</span>
        <h2 class="sec-title">¿Qué necesitas <span>resolver?</span></h2>
      </div>
      <p class="sec-lead">Elige tu punto de partida. Cada ruta empieza con un diagnóstico honesto y termina en un proyecto que se puede construir y vender.</p>
    </div>
    <div class="routes">
      <article class="route lead-route">
        <span class="mono route-who">Tengo un terreno</span>
        <h3 class="route-title">Prefactibilidad y diagnóstico de terreno</h3>
        <p class="route-text">Antes de invertir en diseño, sabes qué permite la normativa, cuánto puedes construir y si los números cierran.</p>
        <ul><li>Normativa y cabida</li><li>Programa de áreas</li><li>Números preliminares y recomendación</li></ul>
        <a href="prefactibilidad-inmobiliaria.html" class="link">Ver diagnóstico de terreno →</a>
      </article>
      <article class="route">
        <span class="mono route-who">Tengo un negocio</span>
        <h3 class="route-title">Diseño de oficinas, clínicas y comercios</h3>
        <p class="route-text">El espacio donde operas es tu primer argumento de ventas. Diseñamos desde cómo funciona tu negocio.</p>
        <ul><li>Oficinas y clínicas</li><li>Retail y restaurantes</li><li>Diseño interior, remodelaciones y mobiliario</li></ul>
        <a href="diseno-estrategico.html" class="link">Ver diseño para negocios →</a>
      </article>
      <article class="route">
        <span class="mono route-who">Quiero desarrollar o invertir</span>
        <h3 class="route-title">Diseño inmobiliario, co-desarrollo e inversión</h3>
        <p class="route-text">Arquitectura con lectura financiera para desarrolladores, socios con terreno e inversionistas.</p>
        <ul><li>Anteproyecto con pro forma</li><li>Alianzas de co-desarrollo</li><li>Lista de interés de proyectos propios</li></ul>
        <a href="#modelos" class="link">Ver modelos de trabajo →</a>
      </article>
    </div>

    <div class="specialties">
      <span class="mono sec-label">También diseñamos</span>
      <div class="spec-grid">
        <a href="?tipo=diseño-interior#contacto" class="spec-card">
          <h3>Diseño interior</h3>
          <p>Paleta de materiales, iluminación, mobiliario y acabados alineados con tu identidad.</p>
          <span class="link">Cotizar diseño interior →</span>
        </a>
        <a href="?tipo=remodelación#contacto" class="spec-card">
          <h3>Remodelaciones</h3>
          <p>Transformamos espacios existentes con una intervención precisa y eficiente.</p>
          <span class="link">Cotizar remodelación →</span>
        </a>
        <a href="?tipo=mobiliario-estratégico#contacto" class="spec-card">
          <h3>Mobiliario estratégico</h3>
          <p>Mobiliario diseñado a la medida de tu operación: exhibición, atención y almacenaje pensados para cómo funciona tu espacio.</p>
          <span class="link">Cotizar mobiliario →</span>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     04 · PROCESO — DEL TERRENO A LA OBRA
     ============================================================ -->
<section class="section on-light-2" id="proceso">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Cómo trabajamos</span>
        <h2 class="sec-title">Del terreno <span>a la obra.</span></h2>
      </div>
      <p class="sec-lead">Cuatro etapas, cada una con un entregable concreto. Puedes contratar solo la primera o el proceso completo. Si los números no cierran en la etapa 01, te lo decimos antes de que gastes en diseño.</p>
    </div>
    <ol class="steps">
      <li class="step"><div class="step-n">01</div><h3 class="step-name">Diagnóstico de terreno</h3><p class="step-text">Normativa aplicable, cabida, programa de áreas y números preliminares.</p><p class="step-deliv"><b>Recibes</b>Informe de prefactibilidad y recomendación.</p></li>
      <li class="step"><div class="step-n">02</div><h3 class="step-name">Anteproyecto con pro forma</h3><p class="step-text">Distribución, volumetría y eficiencia de planta, validadas contra los números.</p><p class="step-deliv"><b>Recibes</b>Plantas, renders y pro forma del proyecto.</p></li>
      <li class="step"><div class="step-n">03</div><h3 class="step-name">Proyecto ejecutivo</h3><p class="step-text">Planos, memorias, especificaciones y expediente técnico para licitación y permisos.</p><p class="step-deliv"><b>Recibes</b>Juego de planos y expediente completo.</p></li>
      <li class="step"><div class="step-n">04</div><h3 class="step-name">Acompañamiento en obra</h3><p class="step-text">Supervisión para que lo construido corresponda a lo diseñado.</p><p class="step-deliv"><b>Recibes</b>Visitas y control de diseño en obra.</p></li>
    </ol>
    <div class="cta-row">
      <a href="prefactibilidad-inmobiliaria.html" class="btn btn-dark">Empezar por el diagnóstico →</a>
      <a href="#contacto" class="link">Agendar llamada de 30 minutos</a>
    </div>
  </div>
</section>

<!-- ============================================================
     05 · DIFERENCIAL — TESIS, CIFRAS, ONA Y MODELOS
     ============================================================ -->
<section class="section on-dark-2" id="vision">
  <div class="wrap">
    <span class="mono sec-label">Por qué Build &amp; Create</span>
    <div class="thesis">
      <h2 class="thesis-quote">No somos arquitectos que construyen. Somos <b>desarrolladores</b> que <b>diseñan.</b></h2>
      <div class="thesis-text">
        <p>Esa diferencia define todo lo que hacemos.</p>
        <p>Cada metro cuadrado que dibujamos pasa por tres filtros: viabilidad técnica, viabilidad comercial y viabilidad financiera. Si los tres no cierran, el proyecto no sale.</p>
        <p><strong>Trabajamos con terrenos seleccionados, desarrolladores alineados e inversionistas que entienden que la arquitectura correcta es la variable que más valor crea en un activo.</strong></p>
      </div>
    </div>

    <dl class="figures" style="grid-template-columns:repeat(3,minmax(0,1fr))">
      <div><dt class="mono">m² en desarrollo · ONA</dt><dd>18,792</dd></div>
      <div><dt class="mono">Eficiencia de planta · ONA</dt><dd>91.9<small>%</small></dd></div>
      <div><dt class="mono">Líneas de negocio</dt><dd>3</dd></div>
    </dl>

    <div class="ona" id="ona">
      <div class="ona-gallery">
        <figure class="g1">{img('ona-rooftop-pergolas', 'Rooftop de ONA con pérgolas iluminadas al atardecer', 1365, 768, webp=False)}</figure>
        <figure class="g2">{img('ona-fachada-organica', 'Fachada orgánica de ONA en vista contrapicada', 1365, 768, webp=False)}</figure>
        <figure class="g3">{img('ona-lobby', 'Lobby principal de ONA', 1365, 768, webp=False)}</figure>
        <figure class="g4">{img('ona-rooftop-yoga', 'Deck de yoga en el rooftop de ONA', 1365, 768, webp=False)}</figure>
        <figure class="g5">{img('ona-planta-tipo', 'Planta arquitectónica tipo de ONA', 1266, 832, webp=False)}</figure>
        <figure class="g6">{img('ona-planta-jardin', 'Planta de ONA con jardín integrado', 1076, 976, webp=False)}</figure>
      </div>
      <div>
        <span class="mono sec-label">Proyecto propio · En desarrollo · Inicio 2026</span>
        <h2 class="ona-name">ONA</h2>
        <p class="mono ona-tag">Movimiento. Vida. Balance.</p>
        <p class="ona-text">Nuestro primer proyecto como arquitectos-desarrolladores: residencial vertical en Zona 15 de Ciudad de Guatemala. Originación estratégica del terreno, diseño optimizado para rentabilidad y ejecución bajo control propio.</p>
        <dl class="spec">
          <div><dt>Ubicación</dt><dd>Zona 15, Vista Hermosa I</dd></div>
          <div><dt>Tipología</dt><dd>Residencial vertical</dd></div>
          <div><dt>m² construidos</dt><dd>18,792</dd></div>
          <div><dt>m² vendibles</dt><dd>17,267</dd></div>
          <div><dt>Eficiencia de planta (vendible/construido)</dt><dd>91.9%</dd></div>
          <div><dt>Fase actual</dt><dd>En fase de desarrollo</dd></div>
          <div><dt>Estructura de inversión</dt><dd>En estructuración final</dd></div>
        </dl>
        <a href="#contacto" class="btn btn-light">Unirme a la lista de inversionistas →</a>
        <p class="disclaimer">Cuando el vehículo de inversión esté estructurado y los números validados externamente, los inversionistas de la lista serán los primeros en conocer la oportunidad. La información es referencial y no constituye una oferta pública de valores ni asesoría financiera.</p>
      </div>
    </div>

    <div class="models" id="modelos">
      <article class="model">
        <span class="mono who">Para desarrolladores con equipo propio</span>
        <h3>Diseño estratégico</h3>
        <p>Tú desarrollas, nosotros diseñamos. Diagnóstico de terreno, anteproyecto con pro forma, proyecto ejecutivo y acompañamiento en obra.</p>
        <a href="#contacto" class="link">Proponer proyecto →</a>
      </article>
      <article class="model">
        <span class="mono who">Para dueños de terreno que buscan socio</span>
        <h3>Co-desarrollo integral</h3>
        <p>Aportamos diseño, gestión del proyecto y entre 10 y 30 por ciento del capital, según tamaño y etapa. Participamos en la utilidad proporcionalmente.</p>
        <a href="#contacto" class="link">Explorar alianza →</a>
      </article>
      <article class="model">
        <span class="mono who">Para inversionistas calificados</span>
        <h3>Inversión en proyectos propios</h3>
        <p>Estructuramos vehículos de inversión para proyectos que originamos, diseñamos y ejecutamos. ONA será el primero cuando la estructura esté lista.</p>
        <a href="#contacto" class="link">Unirme a la lista →</a>
      </article>
    </div>
  </div>
</section>

<!-- ============================================================
     06 · ESTUDIO
     ============================================================ -->
<section class="section on-light" id="estudio">
  <div class="wrap">
    <div class="studio">
      <figure class="studio-photo">
        {img('bryan-castro-retrato', 'Bryan Castro, arquitecto y fundador de Build &amp; Create Studio', 1200, 1800, sizes='(max-width: 1100px) 100vw, 40vw')}
        <figcaption><strong>Bryan Castro</strong><span class="mono">Fundador</span></figcaption>
      </figure>
      <div>
        <span class="mono sec-label">El estudio</span>
        <p class="studio-quote">“Diseño desde la perspectiva de quien va a poner capital en el proyecto. Esa es la única arquitectura que sé hacer.”</p>
        <div class="studio-bio">
          <p>Bryan Castro es arquitecto y desarrollador inmobiliario. Fundó {BRAND} con una convicción simple: la arquitectura sin lectura financiera es decoración cara, y el desarrollo inmobiliario sin diseño estratégico es capital subutilizado.</p>
          <p>El estudio opera bajo esa premisa. Cada proyecto se origina, diseña y desarrolla con un criterio único: maximizar el valor del activo desde el primer trazo.</p>
          <p>Ese criterio ya está construido: tres kioscos para Kishi Books, la oficina de Navante y proyectos en desarrollo en Guatemala y Honduras, como ONA y Edificio W.</p>
        </div>
        <dl class="studio-meta">
          <div><dt class="mono">Disciplinas</dt><dd>Arquitectura · Desarrollo inmobiliario · Estructuración de inversión</dd></div>
          <div><dt class="mono">Base de operaciones</dt><dd>Ciudad de Guatemala · Latinoamérica</dd></div>
        </dl>
        <div class="cta-row" style="margin-top:36px">
          <a href="https://linkedin.com/in/bryan-castro" target="_blank" rel="noopener" class="link">Conectar en LinkedIn →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     07 · CONTACTO — AGENDA, FORMULARIO Y WHATSAPP
     ============================================================ -->
<section class="section on-dark" id="contacto">
  <div class="wrap contact">
    <div>
      <span class="mono sec-label">Contacto</span>
      <h2 class="sec-title">Hablemos de <span>tu proyecto.</span></h2>
      <div class="agenda" id="agenda">
        <span class="mono" style="color:var(--gold)">Consulta inicial · 30 min · Videollamada · Sin costo</span>
        <div class="host">
          <img src="img/bryan-castro-avatar.webp" width="320" height="320" alt="Bryan Castro, arquitecto y fundador de Build &amp; Create Studio" loading="lazy" decoding="async">
          <div><strong>Bryan Castro</strong><span class="mono">Arquitecto · Fundador</span></div>
        </div>
        <h3>Agenda una llamada con Bryan Castro</h3>
        <p>Sin presentaciones de venta. Evaluamos juntos si tu terreno, proyecto o capital encajan con lo que hacemos.</p>
        <ul>
          <li>Diagnóstico rápido de viabilidad</li>
          <li>Revisión del potencial de tu terreno</li>
          <li>Alineación sobre modelos de trabajo</li>
          <li>Respuesta honesta: si no encaja, te lo decimos</li>
        </ul>
        <a href="{CAL}" target="_blank" rel="noopener" class="btn btn-light" id="btnAgenda">Elegir horario →</a>
      </div>
      <dl class="channels">
        <div><dt class="mono">Email</dt><dd><a href="mailto:info@bcarqstudio.com">info@bcarqstudio.com</a></dd></div>
        <div><dt class="mono">WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">+502 5413 1753</a></dd></div>
        <div><dt class="mono">Base</dt><dd>Ciudad de Guatemala</dd></div>
        <div><dt class="mono">Respuesta</dt><dd>Menos de 24 horas hábiles</dd></div>
      </dl>
    </div>
    {contact_fields()}
  </div>
</section>
</main>
''' + footer('') + BASE_JS.replace('%EXTRA%', '''
// ============================================================
// HERO — el índice de proyectos cambia la imagen
// ============================================================
const heroImgs = document.querySelectorAll('#heroMedia img');
const heroBtns = document.querySelectorAll('#heroIndex button');
const heroOpen = document.getElementById('heroOpen');
const showProject = (i) => {
  heroImgs.forEach((im, k) => {
    if (k === i) im.loading = 'eager';
    im.classList.toggle('on', k === i);
  });
  heroBtns.forEach((b, k) => b.setAttribute('aria-pressed', String(k === i)));
  heroOpen.href = heroBtns[i].dataset.href;
};
heroBtns.forEach((b, i) => {
  b.addEventListener('click', () => showProject(i));
  b.addEventListener('mouseenter', () => showProject(i));
  b.addEventListener('focus', () => showProject(i));
});
// Precarga discreta del resto de imágenes del hero cuando la página termina de cargar
window.addEventListener('load', () => heroImgs.forEach(im => { im.loading = 'eager'; }));
''' + FORM_JS)
HOME = HOME.replace('</style>\n</head>', TESTI_CSS + '</style>\n</head>', 1)
open('index.html', 'w', encoding='utf-8').write(HOME)

# ================================================================== PREFACTIBILIDAD
PEND = lambda t: f'<span class="pending">[DATO PENDIENTE: {t}]</span>'
P_URL = SITE + 'prefactibilidad-inmobiliaria.html'
P_TITLE = 'Prefactibilidad inmobiliaria Guatemala | Build &amp; Create Studio'
P_DESC = 'Diagnóstico de terreno en Guatemala: normativa, cabida, programa de áreas y números preliminares antes de invertir en diseño. Avanzar, ajustar o no avanzar.'
p_ld = [
    {"@context": "https://schema.org", "@type": "Service", "name": "Diagnóstico de terreno y prefactibilidad inmobiliaria",
     "serviceType": "Prefactibilidad inmobiliaria", "description": P_DESC, "url": P_URL, "provider": ORG,
     "areaServed": {"@type": "Country", "name": "Guatemala"}},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Prefactibilidad inmobiliaria", "item": P_URL}]}]

PREF = head(P_TITLE, P_DESC, P_URL, 'img/ona-fachada-atardecer-og.jpg', p_ld) + nav('Prefactibilidad', 'index.html') + f'''
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio" style="min-height:max(600px,min(88svh,820px))">
  <div class="hero-media">{img('ona-planta-tipo', 'Planta arquitectónica tipo del proyecto ONA', 1266, 832, lazy=False, cls='on', webp=False)}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Prefactibilidad inmobiliaria · Guatemala</p>
        <h1 class="hero-slogan page-slogan">Diagnóstico <span>de terreno.</span></h1>
        <p class="hero-sub">Antes de pagar un diseño completo, sabes qué permite la normativa en tu terreno, cuánto puedes construir y si el proyecto cierra financieramente.</p>
        <div class="hero-actions">
          <a href="#solicitar" class="btn btn-light">Solicitar diagnóstico →</a>
          <a href="{WA}{WA_TXT}" target="_blank" rel="noopener" class="link">Escribir por WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     POR QUE
     ============================================================ -->
<section class="section on-light" id="por-que">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Por qué</span>
        <h2 class="sec-title">El error más caro <span>ocurre antes del primer plano.</span></h2>
      </div>
      <div class="sec-lead" style="display:flex;flex-direction:column;gap:16px">
        <p>Comprar o desarrollar un terreno sin conocer su potencial real es la forma más rápida de inmovilizar capital.</p>
        <p>Cada metro cuadrado que dibujamos pasa por tres filtros: viabilidad técnica, comercial y financiera. El diagnóstico aplica esos tres filtros a tu terreno antes de que inviertas en diseño, trámites o compra.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     ENTREGABLES
     ============================================================ -->
<section class="section on-dark" id="entregables">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Entregables</span>
        <h2 class="sec-title">Qué <span>recibes.</span></h2>
      </div>
      <p class="sec-lead">Un informe con lo que necesitas para decidir, y una reunión para revisarlo juntos.</p>
    </div>
    <div class="routes routes-6">
      <article class="route"><span class="mono route-who">01</span><h3 class="route-title">Normativa aplicable</h3><p class="route-text">Usos permitidos, alturas, retiros e índices de edificabilidad que aplican al terreno según el plan de ordenamiento municipal.</p></article>
      <article class="route"><span class="mono route-who">02</span><h3 class="route-title">Cabida</h3><p class="route-text">Área construible, número de niveles y cantidad aproximada de unidades o metros comerciales posibles.</p></article>
      <article class="route"><span class="mono route-who">03</span><h3 class="route-title">Programa de áreas</h3><p class="route-text">Distribución preliminar y eficiencia de planta: cuánto del área construida se puede vender o rentar.</p></article>
      <article class="route"><span class="mono route-who">04</span><h3 class="route-title">Números preliminares</h3><p class="route-text">Estimación de costos y pro forma de alto nivel para saber si el proyecto cierra.</p></article>
      <article class="route"><span class="mono route-who">05</span><h3 class="route-title">Riesgos y restricciones</h3><p class="route-text">Lo que puede encarecer o frenar el proyecto: accesos, topografía, servidumbres y trámites.</p></article>
      <article class="route"><span class="mono route-who">06</span><h3 class="route-title">Recomendación</h3><p class="route-text">Avanzar, ajustar o no avanzar. Con argumentos.</p></article>
    </div>
  </div>
</section>

<!-- ============================================================
     CONDICIONES Y PARA QUIEN ES
     ============================================================ -->
<section class="section on-light-2" id="condiciones">
  <div class="wrap studio" style="grid-template-columns:minmax(0,1fr) minmax(0,1fr)">
    <div>
      <span class="mono sec-label">Condiciones</span>
      <dl class="spec" style="border-color:var(--line-light)">
        <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Plazo de entrega</dt><dd>Según la complejidad del terreno</dd></div>
        <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Inversión</dt><dd>Cotización según terreno</dd></div>
        <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Formato</dt><dd>Informe + reunión de resultados</dd></div>
        <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Si continúas con el diseño</dt><dd>Se descuenta del anteproyecto</dd></div>
        <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Primera llamada</dt><dd>30 min · Sin costo</dd></div>
      </dl>
    </div>
    <div>
      <span class="mono sec-label">Para quién es</span>
      <h3 class="step-name">Es para ti si…</h3>
      <ul class="fit">
        <li>Tienes un terreno y no sabes qué conviene construir en él.</li>
        <li>Vas a comprar un terreno y quieres validarlo antes de firmar.</li>
        <li>Eres desarrollador y quieres una segunda lectura con criterio de diseño y de negocio.</li>
        <li>Tienes un inmueble y evalúas si conviene venderlo o desarrollarlo.</li>
      </ul>
      <h3 class="step-name" style="margin-top:36px">No es para ti si…</h3>
      <ul class="fit no">
        <li>Ya tienes anteproyecto aprobado y solo necesitas planos ejecutivos: en ese caso, <a href="index.html#modelos" class="link">diseño estratégico</a>.</li>
        <li>Buscas únicamente un render o una imagen comercial.</li>
      </ul>
    </div>
  </div>
</section>

<!-- ============================================================
     COMO FUNCIONA
     ============================================================ -->
<section class="section on-light" id="como-funciona">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Cómo funciona</span>
        <h2 class="sec-title">Cuatro pasos, <span>sin rodeos.</span></h2>
      </div>
    </div>
    <ol class="steps">
      <li class="step"><div class="step-n">01</div><h3 class="step-name">Llamada de 30 minutos</h3><p class="step-text">Evaluamos si el diagnóstico tiene sentido para tu caso. Sin costo. Si no encaja, te lo decimos.</p></li>
      <li class="step"><div class="step-n">02</div><h3 class="step-name">Nos envías la información</h3><p class="step-text">Ubicación, medidas o plano del terreno, escritura si la tienes y fotografías del sitio.</p></li>
      <li class="step"><div class="step-n">03</div><h3 class="step-name">Análisis</h3><p class="step-text">Revisamos normativa, cabida, programa de áreas y números preliminares.</p></li>
      <li class="step"><div class="step-n">04</div><h3 class="step-name">Entrega y decisión</h3><p class="step-text">Te presentamos el informe y la recomendación. Tú decides el siguiente paso.</p></li>
    </ol>
    <div class="cta-row">
      <a href="#solicitar" class="btn btn-dark">Solicitar diagnóstico →</a>
      <a href="{CAL}" target="_blank" rel="noopener" class="link">Agendar llamada de 30 minutos</a>
    </div>
  </div>
</section>

<!-- ============================================================
     EL METODO APLICADO: ONA
     ============================================================ -->
<section class="section on-dark-2" id="ejemplo">
  <div class="wrap">
    <div class="ona" style="margin-top:0">
      <div class="ona-gallery">
        <figure class="g1">{img('ona-fachada-atardecer', 'Torre residencial ONA al atardecer, Zona 15', 1365, 768, webp=False)}</figure>
        <figure class="g5">{img('ona-planta-amplia', 'Planta arquitectónica amplia de ONA', 1024, 1039, webp=False)}</figure>
        <figure class="g6">{img('ona-planta-jardin', 'Planta de ONA con jardín integrado', 1076, 976, webp=False)}</figure>
      </div>
      <div>
        <span class="mono sec-label">El método aplicado</span>
        <h2 class="ona-name">ONA</h2>
        <p class="ona-text" style="margin-top:20px">Nuestro proyecto propio en Zona 15 se originó con el mismo criterio que aplicamos en cada diagnóstico: diseño optimizado para que la mayor parte del área construida sea vendible.</p>
        <dl class="spec">
          <div><dt>m² construidos</dt><dd>18,792</dd></div>
          <div><dt>m² vendibles</dt><dd>17,267</dd></div>
          <div><dt>Eficiencia de planta</dt><dd>91.9%</dd></div>
          <div><dt>Fase</dt><dd>En fase de desarrollo</dd></div>
        </dl>
        <a href="index.html#ona" class="link">Ver el proyecto ONA →</a>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     PREGUNTAS FRECUENTES
     ============================================================ -->
<section class="section on-light" id="preguntas">
  <div class="wrap" style="max-width:960px">
    <span class="mono sec-label">Preguntas frecuentes</span>
    <div class="faq">
      <details><summary>¿Necesito tener el terreno comprado?</summary><p>No. El diagnóstico también sirve para evaluar un terreno antes de comprarlo, cuando la decisión todavía tiene marcha atrás.</p></details>
      <details><summary>¿Qué información necesito para empezar?</summary><p>La ubicación exacta, las medidas o un plano del terreno y fotografías del sitio. Si tienes escritura o plano de registro, mejor.</p></details>
      <details><summary>¿Qué pasa si el resultado es negativo?</summary><p>Te lo decimos. Es mejor saberlo ahora que después de pagar diseño, trámites o el terreno.</p></details>
      <details><summary>¿Trabajan fuera de Ciudad de Guatemala?</summary><p>Sí. Atendemos proyectos en Guatemala y en otros países, como Edificio W en San Pedro Sula, Honduras. El análisis parte de la información del terreno y de la normativa local.</p></details>
      <details><summary>¿El diagnóstico se descuenta si contrato el diseño?</summary><p>Sí. Si contratas el anteproyecto con nosotros, lo que pagaste por el diagnóstico se descuenta del diseño.</p></details>
    </div>
  </div>
</section>

<!-- ============================================================
     SOLICITAR
     ============================================================ -->
<section class="section on-dark" id="solicitar">
  <div class="wrap contact">
    <div>
      <span class="mono sec-label">Solicitar</span>
      <h2 class="sec-title">Cuéntanos de <span>tu terreno.</span></h2>
      <p class="sec-lead" style="margin-top:28px">Con estos datos preparamos la primera llamada. Respondemos en menos de 24 horas hábiles.</p>
      <figure class="host-photo">
        {img('bryan-castro-reloj', 'Bryan Castro, arquitecto, revisando la hora', 1200, 1800, sizes='(max-width: 1100px) 100vw, 30vw')}
        <figcaption><strong>Bryan Castro</strong><span class="mono">Atiende cada solicitud personalmente</span></figcaption>
      </figure>
      <dl class="channels" style="margin-top:40px">
        <div><dt class="mono">Email</dt><dd><a href="mailto:info@bcarqstudio.com">info@bcarqstudio.com</a></dd></div>
        <div><dt class="mono">WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">+502 5413 1753</a></dd></div>
      </dl>
    </div>
    {contact_fields(prefact=True)}
  </div>
</section>
</main>
''' + footer('index.html') + BASE_JS.replace('%EXTRA%', FORM_JS)

PREF_CSS = '''
/* ---------- PREFACTIBILIDAD: listas y preguntas ---------- */
.fit { list-style: none; border-top: 1px solid var(--line-light); }
.fit li { padding: 14px 0 14px 28px; border-bottom: 1px solid var(--line-light); position: relative; font-size: 16px; line-height: 1.55; color: var(--on-light-muted); }
.fit li::before { content: '✓'; position: absolute; left: 2px; color: var(--bronze); }
.fit.no li::before { content: '—'; }
.faq { border-top: 1px solid var(--line-light); margin-top: 8px; }
.faq details { border-bottom: 1px solid var(--line-light); }
.faq summary { list-style: none; cursor: pointer; padding: 26px 44px 26px 0; position: relative; font-size: clamp(19px, 2vw, 24px); font-weight: 700; font-stretch: 112%; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: '+'; position: absolute; right: 4px; top: 20px; font-size: 30px; font-weight: 300; color: var(--bronze); }
.faq details[open] summary::after { content: '−'; }
.faq p { padding: 0 0 26px; font-size: 17px; line-height: 1.65; color: var(--on-light-muted); max-width: 64ch; }
.on-dark .route-text .pending, .on-dark .sec-lead .pending { margin-top: 8px; }
.page-slogan { font-size: clamp(34px, 7vw, 112px); }
.routes-6 .route:nth-child(n+4) { border-top: 1px solid var(--line-dark); }
@media (max-width: 640px) { .page-slogan { font-size: clamp(30px, 9.4vw, 44px); } .hero-slogan { overflow-wrap: anywhere; } }
'''
PREF = PREF.replace('</style>', PREF_CSS + '</style>', 1)
exec(open(os.path.join('.claude', 'build', 'motion_pref.py'), encoding='utf-8').read())
open('prefactibilidad-inmobiliaria.html', 'w', encoding='utf-8').write(PREF)

# ================================================================== EDIFICIO W
W_URL = SITE + 'edificio-w.html'
W_TITLE = 'Edificio W, uso mixto en San Pedro Sula | Build &amp; Create Studio'
W_DESC = 'Edificio W: uso mixto en esquina en San Pedro Sula, Honduras. Dos locales, ocho apartamentos y rooftop social en 591.86 m², con 89.6 % de área rentable.'
w_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Edificio W", "description": W_DESC, "url": W_URL,
     "image": SITE + "img/edificio-w-aerea-og.jpg", "creator": ORG, "dateCreated": "2026", "inLanguage": "es",
     "creativeWorkStatus": "Anteproyecto en aprobación",
     "contentLocation": {"@type": "Place", "name": "San Pedro Sula, Cortés, Honduras"}},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "#proyectos"},
        {"@type": "ListItem", "position": 3, "name": "Edificio W", "item": W_URL}]}]

W_CSS = """
/* ---------- FICHA DE PROYECTO ---------- */
.p-figures { grid-template-columns: repeat(5, minmax(0, 1fr)); margin-top: 0; }
.gal { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 12px; }
.gal figure { margin: 0; display: flex; flex-direction: column; gap: 10px; }
.gal .frame { overflow: hidden; border-radius: var(--radius); background: var(--ink-2); }
.gal img { width: 100%; height: 100%; object-fit: cover; aspect-ratio: 16 / 10; transition: transform 1.2s var(--ease); }
.gal figure:hover img { transform: scale(1.03); }
.gal figcaption { display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; color: var(--on-dark-muted); font-size: 14px; }
.gal figcaption strong { color: var(--on-dark); font-weight: 600; }
.gal .w7 { grid-column: span 7; } .gal .w5 { grid-column: span 5; } .gal .w4 { grid-column: span 4; } .gal .w12 { grid-column: span 12; }
.gal .w12 img { aspect-ratio: 21 / 9; }
.gal-note { margin-top: 18px; font-size: 13px; color: var(--on-dark-muted); }
.plans { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; }
.plan { margin: 0; background: #fff; border: 1px solid var(--line-light); border-radius: var(--radius); padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.plan img { width: 100%; height: auto; border-radius: var(--radius-sm); }
.plan figcaption { color: var(--on-light-muted); }
.types-row { margin-top: 72px; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
.types { list-style: none; border-top: 1px solid var(--line-light); }
.types li { display: grid; grid-template-columns: 44px minmax(0, 1fr) auto; gap: 16px; align-items: center; padding: 16px 0; border-bottom: 1px solid var(--line-light); }
.types .t { width: 44px; height: 44px; display: grid; place-items: center; border: 1px solid var(--bronze); color: var(--bronze); font-weight: 700; border-radius: 3px; }
.types b { display: block; font-size: 17px; font-weight: 700; font-stretch: 112%; }
.types small { color: var(--on-light-muted); }
.types .m { font-size: clamp(26px, 3vw, 38px); font-weight: 300; font-stretch: 75%; font-variant-numeric: tabular-nums; }
.types .m sub { font-size: 14px; vertical-align: baseline; color: var(--on-light-muted); }
.trio { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; border-top: 1px solid var(--line-dark); padding-top: 24px; }
.trio dt { color: var(--gold); margin-bottom: 8px; }
.trio dd { font-size: 17px; }
.eff { display: grid; grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); gap: 48px; align-items: center; }
.eff-n { font-size: clamp(72px, 11vw, 160px); font-weight: 300; font-stretch: 75%; line-height: 0.9; color: var(--bronze); }
.eff-n small { font-size: 0.35em; }
.bar { display: flex; height: 56px; border-radius: var(--radius-sm); overflow: hidden; font-size: 13px; font-weight: 600; }
.bar span { display: flex; align-items: center; padding: 0 16px; }
.bar .a { flex: 89.6; background: var(--on-light); color: var(--paper); }
.bar .b { flex: 10.4; background: var(--paper-2); color: var(--on-light); justify-content: center; padding: 0 4px; }
.bar-legend { display: flex; gap: 24px; flex-wrap: wrap; margin-top: 14px; color: var(--on-light-muted); font-size: 15px; }
.bar-legend b { color: var(--on-light); }
@media (max-width: 1100px) {
  .p-figures { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .gal .w7, .gal .w5, .gal .w4 { grid-column: span 6; }
  .plans, .eff, .trio, .types-row { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .p-figures { grid-template-columns: 1fr 1fr; }
  .gal .w7, .gal .w5, .gal .w4, .gal .w12 { grid-column: span 12; }
  .gal .w12 img { aspect-ratio: 16 / 10; }
}
"""

def gfig(stem, alt, title, sub, cls, w=1920, h=1080, sizes='(max-width: 640px) 100vw, 50vw'):
    return f'<figure class="{cls}"><div class="frame">{img(stem, alt, w, h, sizes=sizes)}</div><figcaption><strong>{title}</strong><span class="mono">{sub}</span></figcaption></figure>'

WPAGE = head(W_TITLE, W_DESC, W_URL, 'img/edificio-w-aerea-og.jpg', w_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('edificio-w-aerea', 'Vista aérea del Edificio W en esquina al atardecer, San Pedro Sula, Honduras', 1920, 1080, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Uso mixto · San Pedro Sula · Cortés · Honduras</p>
        <h1 class="hero-slogan">Edificio <span>W.</span></h1>
        <p class="hero-sub">Edificio de uso mixto en esquina: comercio en planta baja, ocho apartamentos y una terraza social con vista a la montaña.</p>
        <div class="hero-actions">
          <a href="#contacto-w" class="btn btn-light">Conversemos de este proyecto →</a>
          <a href="#planos" class="link">Ver plantas</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>Anteproyecto · En aprobación</dd></div>
          <div><dt>Año</dt><dd>2026</dd></div>
          <div><dt>Diseño</dt><dd>{BRAND}</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     CIFRAS Y CONCEPTO
     ============================================================ -->
<section class="section on-dark-2" id="proyecto">
  <div class="wrap">
    <dl class="figures p-figures">
      <div><dt class="mono">Niveles</dt><dd>3<small> + rooftop</small></dd></div>
      <div><dt class="mono">Apartamentos</dt><dd>8</dd></div>
      <div><dt class="mono">Locales comerciales</dt><dd>2</dd></div>
      <div><dt class="mono">m² construidos</dt><dd>591.86</dd></div>
      <div><dt class="mono">Área rentable</dt><dd>89.6<small>%</small></dd></div>
    </dl>
    <div class="thesis" style="margin-top:96px">
      <h2 class="thesis-quote">Una esquina que trabaja en <b>tres tiempos.</b></h2>
      <div class="thesis-text">
        <p>Comercio que activa la calle, vivienda eficiente en los niveles medios y una azotea social que remata el conjunto.</p>
        <p>Un volumen contemporáneo de concreto, celosía de madera y piedra, resuelto sobre un lote de esquina con dos frentes a vía pública: acceso comercial independiente, entrada de residentes diferenciada y mejor asoleamiento y ventilación en todos los niveles.</p>
        <p><strong>Ubicado sobre el corredor del Boulevard Los Próceres, en una zona mixta residencial y comercial de San Pedro Sula.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     GALERIA
     ============================================================ -->
<section class="section on-dark" id="galeria">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Renders del anteproyecto</span>
        <h2 class="sec-title">Materia noble, <span>líneas limpias.</span></h2>
      </div>
      <p class="sec-lead">Concreto visto, paneles de celosía en madera, muros de piedra y un jardín vertical que respira sobre la fachada.</p>
    </div>
    <div class="gal">
      {gfig('edificio-w-volumetria', 'Fachada del Edificio W con celosía de madera, piedra y jardín vertical', 'Volumetría', 'Celosía, piedra y jardín vertical', 'w12', 1920, 1072, '100vw')}
      {gfig('edificio-w-fachada', 'Fachada principal del Edificio W en esquina a nivel de calle', 'Fachada principal', 'Esquina a nivel de calle', 'w5')}
      {gfig('edificio-w-acceso', 'Acceso comercial en planta baja del Edificio W', 'Acceso comercial', 'Planta baja a la calle', 'w7')}
      {gfig('edificio-w-apartamentos', 'Apartamentos del Edificio W con terrazas, ventanales y balcones', 'Apartamentos', 'Terrazas, ventanales y balcones', 'w7')}
      {gfig('edificio-w-balcon', 'Balcón del Edificio W junto al jardín vertical con vista a la montaña', 'Vida en balcón', 'Jardín vertical y montaña', 'w5', 1920, 1072)}
    </div>
    <p class="gal-note">Imágenes de referencia del diseño propuesto en fase de anteproyecto.</p>
  </div>
</section>

<!-- ============================================================
     PLANTAS Y TIPOLOGIAS
     ============================================================ -->
<section class="section on-light" id="planos">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Programa arquitectónico</span>
        <h2 class="sec-title">Cuatro unidades <span>por nivel.</span></h2>
      </div>
      <p class="sec-lead">Planta baja con dos locales a la calle, lobby residencial independiente y parqueo comercial. En los niveles 2 y 3, cuatro apartamentos alrededor de un núcleo de circulación central.</p>
    </div>
    <div class="plans">
      <figure class="plan">{img('edificio-w-planta-baja', 'Planta nivel calle del Edificio W con locales comerciales y lobby', 1082, 780, sizes='(max-width: 1100px) 100vw, 50vw')}<figcaption class="mono">Planta nivel calle · Locales y lobby</figcaption></figure>
      <figure class="plan">{img('edificio-w-planta-tipo', 'Planta arquitectónica tipo del Edificio W con cuatro apartamentos', 1090, 783, sizes='(max-width: 1100px) 100vw, 50vw')}<figcaption class="mono">Planta arquitectónica · Nivel tipo</figcaption></figure>
    </div>
    <div class="studio types-row">
      <figure class="plan" style="margin:0">{img('edificio-w-tipologias', 'Distribución por unidad del nivel tipo del Edificio W', 1176, 739, sizes='(max-width: 1100px) 100vw, 50vw')}<figcaption class="mono">Distribución por unidad · Nivel tipo</figcaption></figure>
      <div>
        <h3 class="step-name" style="font-size:26px">De estudio a dos habitaciones</h3>
        <p class="step-text">Las cuatro tipologías se repiten en dos niveles residenciales: ocho apartamentos en total.</p>
        <ul class="types">
          <li><span class="t">A</span><span><b>Apartamento A</b><small>2 habitaciones</small></span><span class="m">57.49 <sub>m²</sub></span></li>
          <li><span class="t">B</span><span><b>Apartamento B</b><small>1 habitación · estudio</small></span><span class="m">25.00 <sub>m²</sub></span></li>
          <li><span class="t">C</span><span><b>Apartamento C</b><small>2 habitaciones</small></span><span class="m">67.31 <sub>m²</sub></span></li>
          <li><span class="t">D</span><span><b>Apartamento D</b><small>1 habitación · estudio</small></span><span class="m">26.78 <sub>m²</sub></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     EFICIENCIA
     ============================================================ -->
<section class="section on-light-2" id="eficiencia">
  <div class="wrap eff">
    <div>
      <span class="mono sec-label">Eficiencia del diseño</span>
      <p class="eff-n">89.6<small>%</small></p>
      <p class="sec-lead" style="margin-top:16px">Diseñado para rentar, no para circular. Casi 9 de cada 10 m² construidos generan ingreso.</p>
    </div>
    <div>
      <div class="bar" role="img" aria-label="89.6 por ciento área rentable, 10.4 por ciento área común"><span class="a">Rentable · 89.6%</span><span class="b">10.4%</span></div>
      <div class="bar-legend"><span><b>507.51 m²</b> área rentable</span><span><b>58.77 m²</b> área común</span></div>
      <p class="step-text" style="margin-top:24px">El rooftop social (25.58 m²) suma como amenidad, sin restar al área rentable.</p>
    </div>
  </div>
</section>

<!-- ============================================================
     MATERIALIDAD, ROOFTOP Y FICHA
     ============================================================ -->
<section class="section on-dark-2" id="ficha">
  <div class="wrap">
    <div class="ona" style="margin-top:0">
      <div>
        <span class="mono sec-label">Materialidad</span>
        <dl class="trio">
          <div><dt class="mono">Estructura</dt><dd>Concreto armado aparente</dd></div>
          <div><dt class="mono">Envolvente</dt><dd>Celosía de madera · piedra natural</dd></div>
          <div><dt class="mono">Verde</dt><dd>Jardín vertical integrado</dd></div>
        </dl>
        <span class="mono sec-label" style="margin-top:56px">Rooftop social</span>
        <dl class="trio">
          <div><dt class="mono">Estar</dt><dd>Lounge + comedor exterior</dd></div>
          <div><dt class="mono">Cocina</dt><dd>Parrilla · área social</dd></div>
          <div><dt class="mono">Paisaje</dt><dd>Vista abierta a la montaña</dd></div>
        </dl>
      </div>
      <div>
        <span class="mono sec-label">Ficha técnica</span>
        <dl class="spec">
          <div><dt>Proyecto</dt><dd>Edificio W</dd></div>
          <div><dt>Ubicación</dt><dd>San Pedro Sula, Cortés, Honduras</dd></div>
          <div><dt>Uso</dt><dd>Mixto · comercial + residencial</dd></div>
          <div><dt>Niveles</dt><dd>3 + rooftop</dd></div>
          <div><dt>Área de lote</dt><dd>228.76 m² (fracción principal)</dd></div>
          <div><dt>Área construida</dt><dd>591.86 m²</dd></div>
          <div><dt>Apartamentos</dt><dd>8 unidades (A–D) · 25–67 m²</dd></div>
          <div><dt>Locales comerciales</dt><dd>2 · 45 y 53 m²</dd></div>
          <div><dt>Parqueos comerciales</dt><dd>2</dd></div>
          <div><dt>Estado</dt><dd>Anteproyecto · En aprobación</dd></div>
          <div><dt>Año</dt><dd>2026</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     CONTACTO
     ============================================================ -->
<section class="section on-dark" id="contacto-w">
  <div class="wrap contact">
    <div>
      <span class="mono sec-label">Edificio W</span>
      <h2 class="sec-title">Disponible para <span>desarrollo e inversión.</span></h2>
      <p class="sec-lead" style="margin-top:28px">El anteproyecto está disponible para desarrollo, inversión y comercialización. Agenda una llamada y revisamos el proyecto contigo.</p>
      <p class="disclaimer">La información es referencial y no constituye una oferta pública de valores ni asesoría financiera.</p>
      <div class="host">
          <img src="img/bryan-castro-avatar.webp" width="320" height="320" alt="Bryan Castro, arquitecto y fundador de Build &amp; Create Studio" loading="lazy" style="margin-top:28px" decoding="async">
          <div><strong>Bryan Castro</strong><span class="mono">Arquitecto · Fundador</span></div>
        </div>
      <div class="cta-row">
        <a href="index.html?tipo=inversión#contacto" class="btn btn-light">Solicitar información →</a>
        <a href="{CAL}" target="_blank" rel="noopener" class="link">Agendar llamada de 30 minutos</a>
      </div>
    </div>
    <dl class="channels" style="align-self:end">
      <div><dt class="mono">Email</dt><dd><a href="mailto:info@bcarqstudio.com">info@bcarqstudio.com</a></dd></div>
      <div><dt class="mono">WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">+502 5413 1753</a></dd></div>
    </dl>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
WPAGE = WPAGE.replace('</style>', W_CSS + '</style>', 1)
open('edificio-w.html', 'w', encoding='utf-8').write(WPAGE)
exec(open(os.path.join('.claude', 'build', 'paginas_a.py'), encoding='utf-8').read())
print('ok', len(HOME), len(PREF), len(WPAGE), len(DPAGE), len(LPAGE), len(KPAGE), len(NPAGE), len(PPAGE), len(MPAGE))
