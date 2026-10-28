# Capa de movimiento para prefactibilidad-inmobiliaria.html.
# Se ejecuta dentro de build_a.py (exec) después de construir PREF; usa WA, WA_TXT y PREF de ese contexto.
import re

MOTION_CSS = """
/* ============================================================
   MOVIMIENTO — PREFACTIBILIDAD
   Luz ámbar difusa, escaneo del plano, análisis en curso,
   entradas al hacer scroll y cifras que cuentan.
   ============================================================ */
:root { --amber: 222, 164, 82; --amber-deep: 196, 116, 44; }
.amb { position: absolute; inset: -15%; z-index: 1; pointer-events: none; mix-blend-mode: screen; opacity: 0.8; }
.amb i { position: absolute; display: block; width: 62vmax; height: 62vmax; border-radius: 50%; will-change: transform; }
.amb i:nth-child(1) { left: -12%; top: -8%; background: radial-gradient(circle, rgba(var(--amber), 0.42) 0%, rgba(var(--amber), 0) 62%); animation: drift-a 24s ease-in-out infinite alternate; }
.amb i:nth-child(2) { right: -18%; top: 18%; background: radial-gradient(circle, rgba(var(--amber-deep), 0.38) 0%, rgba(var(--amber-deep), 0) 60%); animation: drift-b 30s ease-in-out infinite alternate; }
.amb i:nth-child(3) { left: 30%; bottom: -30%; width: 48vmax; height: 48vmax; background: radial-gradient(circle, rgba(216, 199, 163, 0.30) 0%, rgba(216, 199, 163, 0) 62%); animation: drift-c 20s ease-in-out infinite alternate; }
@keyframes drift-a { from { transform: translate3d(0, 0, 0) scale(1); } to { transform: translate3d(14vw, 10vh, 0) scale(1.18); } }
@keyframes drift-b { from { transform: translate3d(0, 0, 0) scale(1.1); } to { transform: translate3d(-16vw, -8vh, 0) scale(0.92); } }
@keyframes drift-c { from { transform: translate3d(0, 0, 0) scale(0.95); } to { transform: translate3d(-10vw, -14vh, 0) scale(1.15); } }

.scan { position: absolute; inset: 0; z-index: 1; pointer-events: none; overflow: hidden; }
.scan::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 1px; background: linear-gradient(90deg, transparent 0%, rgba(var(--amber), 0.9) 30%, rgba(255, 236, 200, 1) 50%, rgba(var(--amber), 0.9) 70%, transparent 100%); box-shadow: 0 0 18px 2px rgba(var(--amber), 0.55); animation: scan 7s cubic-bezier(0.65, 0, 0.35, 1) infinite; }
.scan::after { content: ''; position: absolute; left: 0; right: 0; top: -120px; height: 120px; background: linear-gradient(0deg, rgba(var(--amber), 0.12), transparent); animation: scan 7s cubic-bezier(0.65, 0, 0.35, 1) infinite; }
@keyframes scan { 0% { transform: translateY(12vh); opacity: 0; } 12% { opacity: 1; } 85% { opacity: 1; } 100% { transform: translateY(78vh); opacity: 0; } }

.analysis { position: relative; z-index: 2; align-self: end; background: rgba(14, 13, 11, 0.62); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(var(--amber), 0.35); border-radius: var(--radius); padding: 24px 26px; max-width: 380px; margin-left: auto; }
.analysis-head { display: flex; justify-content: space-between; gap: 12px; align-items: center; color: var(--gold); margin-bottom: 14px; }
.analysis-head .live { display: inline-flex; align-items: center; gap: 8px; }
.analysis-head .live::before { content: ''; width: 7px; height: 7px; border-radius: 50%; background: rgb(var(--amber)); animation: pulse 2s infinite; }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(var(--amber), 0.6); } 70% { box-shadow: 0 0 0 10px rgba(var(--amber), 0); } 100% { box-shadow: 0 0 0 0 rgba(var(--amber), 0); } }
.analysis ol { list-style: none; display: flex; flex-direction: column; }
.analysis li { display: grid; grid-template-columns: 22px minmax(0, 1fr) auto; gap: 12px; align-items: center; padding: 11px 0; border-top: 1px solid var(--line-dark); font-size: 15px; animation: step-in 0.6s ease both; animation-delay: calc(0.9s + var(--i) * 0.55s); }
.analysis li .ok { width: 22px; height: 22px; border-radius: 50%; border: 1px solid rgba(var(--amber), 0.6); display: grid; place-items: center; color: var(--ink); font-size: 12px; font-weight: 700; background: rgb(var(--amber)); animation: tick 0.5s ease both; animation-delay: calc(1.2s + var(--i) * 0.55s); }
.analysis li .st { color: var(--on-dark-muted); }
.analysis-foot { margin-top: 14px; padding-top: 14px; border-top: 1px solid rgba(var(--amber), 0.35); color: var(--on-dark); font-size: 15px; animation: step-in 0.6s ease both; animation-delay: 3.4s; }
.analysis-foot b { color: var(--gold); }
@keyframes step-in { from { opacity: 0.25; transform: translateX(-6px); } to { opacity: 1; transform: none; } }
@keyframes tick { from { background: transparent; color: transparent; transform: scale(0.6); } to { background: rgb(var(--amber)); color: var(--ink); transform: scale(1); } }

/* Entradas al hacer scroll: solo con JS activo, para que sin JS todo se vea */
.js .rv { opacity: 0; transform: translateY(28px); transition: opacity 0.9s var(--ease), transform 0.9s var(--ease); transition-delay: calc(var(--d, 0) * 90ms); }
.js .rv.in { opacity: 1; transform: none; }

/* Entregables: realce ámbar al pasar el cursor */
.routes-6 .route { position: relative; }
.routes-6 .route::before { content: ''; position: absolute; left: 0; top: -1px; height: 2px; width: 0; background: rgb(var(--amber)); transition: width 0.6s var(--ease); }
.routes-6 .route:hover::before { width: 100%; }
.routes-6 .route:hover .route-who { color: rgb(var(--amber)); }

/* Cómo funciona: línea de progreso que se llena paso a paso */
.steps.flow { position: relative; }
.steps.flow::before { content: ''; position: absolute; left: 0; top: -1px; height: 2px; width: 100%; background: var(--bronze); transform: scaleX(0); transform-origin: left; transition: transform 2.4s var(--ease); }
.steps.flow.in::before { transform: scaleX(1); }
.js .steps.flow .step-n { color: rgba(111, 92, 60, 0.28); transition: color 0.5s; }
.js .steps.flow.in .step-n { color: var(--bronze); transition-delay: calc(var(--d) * 550ms); }

/* Brillo ámbar que sigue el cursor en secciones oscuras */
.glow { position: relative; overflow: hidden; }
.glow::after { content: ''; position: absolute; width: 640px; height: 640px; left: var(--mx, -999px); top: var(--my, -999px); transform: translate(-50%, -50%); border-radius: 50%; background: radial-gradient(circle, rgba(var(--amber), 0.13) 0%, rgba(var(--amber), 0) 65%); pointer-events: none; transition: opacity 0.4s; opacity: 0; }
.glow.hovering::after { opacity: 1; }
.glow > .wrap { position: relative; z-index: 1; }

@media (max-width: 1100px) { .analysis { margin-left: 0; max-width: none; } }
@media (max-width: 640px) {
  .amb { opacity: 0.38; }
  .amb i { width: 90vmin; height: 90vmin; }
  .amb i:nth-child(1) { left: -40%; top: -20%; }
  .amb i:nth-child(2) { right: -50%; top: 40%; }
  .amb i:nth-child(3) { display: none; }
  #inicio.hero::after { background: linear-gradient(180deg, rgba(14,13,11,0.62) 0%, rgba(14,13,11,0.72) 45%, rgba(14,13,11,0.9) 100%); }
}
/* Cuadrícula de 6 entregables: cada fila empieza alineada y sin borde final */
@media (min-width: 1101px) {
  .routes-6 .route:nth-child(3n+1) { padding-left: 0; }
  .routes-6 .route:nth-child(3n) { border-right: 0; }
}
@media (prefers-reduced-motion: reduce) {
  .amb i, .scan::before, .scan::after, .analysis li, .analysis li .ok, .analysis-foot, .analysis-head .live::before { animation: none !important; }
  .scan { display: none; }
  .js .rv { opacity: 1; transform: none; transition: none; }
  .steps.flow::before { transform: scaleX(1); transition: none; }
  .js .steps.flow .step-n { color: var(--bronze); }
  .glow::after { display: none; }
}
"""

MOTION_JS = """
// ============================================================
// MOVIMIENTO — entradas, progreso, cifras y brillo de cursor
// ============================================================
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
document.documentElement.classList.add('js');
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    if (e.target.dataset.count !== undefined) countUp(e.target);
    io.unobserve(e.target);
  });
}, { threshold: 0.18, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.rv, .steps.flow, [data-count]').forEach((el) => io.observe(el));

function countUp(el) {
  if (reduce) return;
  const end = parseFloat(el.dataset.count), dec = parseInt(el.dataset.dec || '0', 10), suf = el.dataset.suf || '';
  const fmt = (v) => v.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
  const t0 = performance.now(), dur = 1600;
  const tick = (t) => {
    const p = Math.min(1, (t - t0) / dur), k = 1 - Math.pow(1 - p, 3);
    el.textContent = fmt(end * k);
    if (p < 1) requestAnimationFrame(tick); else el.textContent = fmt(end);
  };
  requestAnimationFrame(tick);
}

if (!reduce && window.matchMedia('(hover: hover)').matches) {
  document.querySelectorAll('.glow').forEach((sec) => {
    sec.addEventListener('pointermove', (e) => {
      const r = sec.getBoundingClientRect();
      sec.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      sec.style.setProperty('--my', (e.clientY - r.top) + 'px');
      sec.classList.add('hovering');
    });
    sec.addEventListener('pointerleave', () => sec.classList.remove('hovering'));
  });
}
"""

ANALYSIS = """
      <aside class="analysis" aria-label="Qué analizamos en tu terreno">
        <div class="analysis-head mono"><span class="live">Análisis de terreno</span><span>4 filtros</span></div>
        <ol>
          <li style="--i:0"><span class="ok" aria-hidden="true">✓</span><span>Normativa aplicable</span><span class="st mono">POT</span></li>
          <li style="--i:1"><span class="ok" aria-hidden="true">✓</span><span>Cabida</span><span class="st mono">m²</span></li>
          <li style="--i:2"><span class="ok" aria-hidden="true">✓</span><span>Programa de áreas</span><span class="st mono">Eficiencia</span></li>
          <li style="--i:3"><span class="ok" aria-hidden="true">✓</span><span>Números preliminares</span><span class="st mono">Pro forma</span></li>
        </ol>
        <p class="analysis-foot">Resultado: <b>avanzar, ajustar o no avanzar.</b></p>
      </aside>"""


def prep(a, b, n=1):
    global PREF
    assert PREF.count(a) == n, (a[:70], PREF.count(a))
    PREF = PREF.replace(a, b)


PREF = PREF.replace('</style>', MOTION_CSS + '</style>', 1)

# Capas del hero: luz ámbar + escaneo
prep('<div class="hero-media">', '<div class="amb" aria-hidden="true"><i></i><i></i><i></i></div>\n  <div class="scan" aria-hidden="true"></div>\n  <div class="hero-media">')

# Panel de análisis en la columna derecha del hero
wa_link = f'<a href="{WA}{WA_TXT}" target="_blank" rel="noopener" class="link">Escribir por WhatsApp</a>\n        </div>\n      </div>\n'
prep(wa_link, wa_link + ANALYSIS + '\n')

# Entradas al hacer scroll (contenido de cada sección)
for sec in ['por-que', 'entregables', 'condiciones', 'como-funciona', 'ejemplo', 'preguntas', 'solicitar']:
    PREF = re.sub(rf'(id="{sec}">\s*<div class="wrap)', r'\1 rv', PREF, count=1)

# Tarjetas de entregables en cascada
_n = [0]
def _card(m):
    _n[0] += 1
    return f'<article class="route rv" style="--d:{(_n[0] - 1) % 3}">'
PREF = re.sub(r'<article class="route">(?=<span class="mono route-who">0)', _card, PREF)

# Línea de progreso en "Cómo funciona"
m = re.search(r'id="como-funciona">.*?<ol class="steps">', PREF, re.S)
PREF = PREF[:m.end() - len('<ol class="steps">')] + '<ol class="steps flow">' + PREF[m.end():]
seg_start = PREF.index('<ol class="steps flow">')
seg_end = PREF.index('</ol>', seg_start)
seg = PREF[seg_start:seg_end]
for k, n in enumerate(['01', '02', '03', '04']):
    seg = seg.replace(f'<div class="step-n">{n}</div>', f'<div class="step-n" style="--d:{k}">{n}</div>', 1)
PREF = PREF[:seg_start] + seg + PREF[seg_end:]

# Brillo de cursor en secciones oscuras
for cls, sec in [('on-dark', 'entregables'), ('on-dark-2', 'ejemplo'), ('on-dark', 'solicitar')]:
    prep(f'class="section {cls}" id="{sec}"', f'class="section {cls} glow" id="{sec}"')

# Cifras de ONA que cuentan
prep('<dd>18,792</dd>', '<dd data-count="18792">18,792</dd>')
prep('<dd>17,267</dd>', '<dd data-count="17267">17,267</dd>')
prep('<div><dt>Eficiencia de planta</dt><dd>91.9%</dd></div>', '<div><dt>Eficiencia de planta</dt><dd data-count="91.9" data-dec="1" data-suf="%">91.9%</dd></div>')

PREF = PREF.replace('\n</script>\n\n</body>', MOTION_JS + '\n</script>\n\n</body>', 1)
assert 'countUp' in PREF
