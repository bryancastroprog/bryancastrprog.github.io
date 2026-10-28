#!/usr/bin/env node
// Auditoría en navegador real (Chromium vía Playwright) para BC Arquitectura.
//
// Uso (desde la raíz del repo, con el sitio servido localmente):
//   python3 -m http.server 8765 &
//   node .claude/skills/ux-accesibilidad/scripts/browser_audit.js [http://127.0.0.1:8765] [pagina.html ...]
//
// Mide por página y viewport (390px móvil, 1440px escritorio): recursos locales 404, errores de consola,
// peso transferido, desborde horizontal, elementos recortados, textos < 12px, objetivos táctiles < 24px,
// imágenes que no cargan y, si axe-core está instalado (npm i axe-core), violaciones WCAG 2 A/AA.
// Guarda capturas en ./.qa-shots/ (ignorado por git).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const args = process.argv.slice(2);
const base = (args.find(a => a.startsWith('http')) || 'http://127.0.0.1:8765').replace(/\/$/, '');
let pages = args.filter(a => !a.startsWith('http'));
if (!pages.length) {
  const walk = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => {
    if (['.git', 'node_modules', '.claude', 'docs', '.qa-shots'].includes(e.name)) return [];
    const p = path.join(d, e.name);
    return e.isDirectory() ? walk(p) : e.name.endsWith('.html') ? [path.relative('.', p)] : [];
  });
  pages = walk('.');
}
let axeSrc = null;
try { axeSrc = fs.readFileSync(require.resolve('axe-core/axe.min.js', { paths: [process.cwd(), __dirname] }), 'utf8'); } catch (e) {}

const shots = path.join(process.cwd(), '.qa-shots');
fs.mkdirSync(shots, { recursive: true });

(async () => {
  const browser = await chromium.launch();
  const report = [];
  for (const vp of [{ n: 'movil', w: 390, h: 844 }, { n: 'escritorio', w: 1440, h: 900 }]) {
    for (const p of pages) {
      const ctx = await browser.newContext({ viewport: { width: vp.w, height: vp.h } });
      const page = await ctx.newPage();
      const r = { pagina: p, viewport: vp.n, local404: [], consola: [], bytesLocales: 0, externosFallidos: new Set() };
      page.on('console', m => { if (m.type() === 'error') r.consola.push(m.text().slice(0, 140)); });
      page.on('pageerror', e => r.consola.push('JS: ' + e.message.slice(0, 140)));
      page.on('requestfailed', q => { if (!q.url().startsWith(base)) r.externosFallidos.add(new URL(q.url()).host); });
      page.on('response', async res => {
        if (!res.url().startsWith(base)) return;
        if (res.status() >= 400) r.local404.push(res.url().slice(base.length + 1) + ' → ' + res.status());
        else { try { r.bytesLocales += (await res.body()).length; } catch (e) {} }
      });
      await page.goto(`${base}/${p}`, { waitUntil: 'load', timeout: 90000 }).catch(e => r.consola.push('GOTO ' + e.message.slice(0, 80)));
      await page.evaluate(async () => {
        for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(z => setTimeout(z, 80)); }
        window.scrollTo(0, 0);
      });
      await page.waitForTimeout(1200);
      Object.assign(r, await page.evaluate(() => {
        const vw = window.innerWidth;
        const recortados = [...document.querySelectorAll('h1,h2,h3,p,a,button,li,span,div')]
          .filter(e => { const b = e.getBoundingClientRect(); return b.width && b.right > vw + 2 && getComputedStyle(e).position !== 'fixed' && e.closest('svg') === null; })
          .slice(0, 6).map(e => `${e.tagName.toLowerCase()}.${String(e.className).split(' ')[0]} «${(e.textContent || '').trim().slice(0, 30)}»`);
        const pequenos = {};
        document.querySelectorAll('body *').forEach(e => {
          if (![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
          const f = parseFloat(getComputedStyle(e).fontSize);
          if (f < 12) pequenos[f + 'px'] = (pequenos[f + 'px'] || 0) + 1;
        });
        const tactiles = [...document.querySelectorAll('a,button,[role=button]')]
          .filter(e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.height > 0 && (b.height < 24 || b.width < 24); }).length;
        const imgsRotas = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => (i.getAttribute('src') || '').slice(0, 60));
        return { desbordeX: document.documentElement.scrollWidth - vw, recortados, textosMenores12: pequenos, tactilesMenores24: tactiles, imgsRotas };
      }));
      if (axeSrc && vp.n === 'movil') {
        await page.addScriptTag({ content: axeSrc });
        r.wcag = await page.evaluate(async () => (await axe.run(document, { runOnly: ['wcag2a', 'wcag2aa'] }))
          .violations.map(v => `${v.impact} · ${v.id} · ${v.nodes.length} nodos`));
      }
      await page.screenshot({ path: path.join(shots, `${vp.n}-${p.replace(/[\/]/g, '_').replace('.html', '')}.png`) });
      r.MB = +(r.bytesLocales / 1048576).toFixed(1); delete r.bytesLocales;
      r.externosFallidos = [...r.externosFallidos];
      report.push(r);
      await ctx.close();
    }
  }
  await browser.close();
  console.log(JSON.stringify(report, null, 1));
  if (!axeSrc) console.error('Nota: axe-core no instalado; se omitió el chequeo WCAG automático (npm i --no-save axe-core).');
})();
