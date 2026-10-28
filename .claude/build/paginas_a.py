# Páginas adicionales en la dirección A: Diseño para negocios y La Autoría.
# Se ejecuta dentro de build_a.py (exec) y reutiliza head, nav, footer, img, BASE_JS, FORM_JS, CSS, ORG, SITE, BRAND, WA, CAL.

# ================================================================== DISEÑO PARA NEGOCIOS
D_URL = SITE + 'diseno-estrategico.html'
D_TITLE = 'Diseño de oficinas y clínicas Guatemala | Build &amp; Create Studio'
D_DESC = 'Diseño de oficinas, clínicas, comercios, restaurantes y hoteles en Guatemala. Diseño estratégico que mejora la operación y eleva el valor del inmueble.'
SERVICES = [
    ('Oficinas corporativas', 'Espacios que reflejan la cultura de tu empresa y elevan la productividad del equipo.'),
    ('Clínicas médicas y odontológicas', 'Diseño funcional que cumple normativas sanitarias y transmite confianza al paciente.'),
    ('Diseño comercial y retail', 'Locales diseñados para convertir visitas en ventas con circulación y exhibición estratégica.'),
    ('Restaurantes y gastronomía', 'Ambientes que refuerzan el concepto gastronómico y generan experiencias memorables.'),
    ('Hoteles y hospitalidad', 'Proyectos con identidad clara y eficiencia operativa.'),
    ('Diseño interior', 'Paleta de materiales, iluminación, mobiliario y acabados alineados con tu identidad.'),
    ('Remodelaciones', 'Transformamos espacios existentes con una intervención precisa y eficiente.'),
    ('Mobiliario estratégico', 'Mobiliario diseñado a la medida de tu operación: exhibición, atención y almacenaje.'),
    ('Planificación y documentación', 'Planos, memorias, permisos y expediente técnico completo para construcción.'),
]
d_ld = [
    {"@context": "https://schema.org", "@type": "Service", "name": "Diseño estratégico para negocios",
     "description": D_DESC, "url": D_URL, "provider": ORG,
     "areaServed": [{"@type": "Country", "name": "Guatemala"}, {"@type": "Country", "name": "Honduras"}],
     "serviceType": [n for n, _ in SERVICES]},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Diseño para negocios", "item": D_URL}]}]

PAGE_A_CSS = """
/* ---------- DISEÑO PARA NEGOCIOS / FICHA DE PROYECTO ---------- */
.svc-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--line-dark); }
.svc { padding: 32px 28px 36px 0; border-bottom: 1px solid var(--line-dark); display: flex; flex-direction: column; gap: 10px; }
.svc:nth-child(3n+2), .svc:nth-child(3n) { padding-left: 28px; border-left: 1px solid var(--line-dark); }
.svc .n { color: var(--gold); }
.svc h3 { font-size: 22px; font-weight: 700; font-stretch: 112%; line-height: 1.15; }
.svc p { color: var(--on-dark-muted); font-size: 15px; line-height: 1.6; }
.pillars { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px; margin-top: 64px; border-top: 1px solid var(--line-light); padding-top: 28px; }
.pillars h3 { font-size: 19px; font-weight: 700; font-stretch: 112%; margin-bottom: 8px; }
.pillars p { color: var(--on-light-muted); font-size: 15px; line-height: 1.6; }
.quote-band { text-align: left; }
.quote-band p { font-weight: 300; font-stretch: 75%; font-size: clamp(30px, 4.2vw, 60px); line-height: 1.05; letter-spacing: -0.02em; max-width: 22ch; text-wrap: balance; }
.quote-band p em { font-style: normal; font-weight: 800; font-stretch: 125%; color: var(--gold); }
.quote-band .by { display: flex; align-items: center; gap: 14px; margin-top: 32px; }
.quote-band .by img { width: 56px; height: 56px; object-fit: cover; border-radius: var(--radius); }
.quote-band .by span { color: var(--gold); }
.concepts { list-style: none; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 48px; border-top: 1px solid var(--line-dark); }
.concepts li { display: grid; grid-template-columns: 48px minmax(0, 1fr); gap: 12px; padding: 24px 0; border-bottom: 1px solid var(--line-dark); color: var(--on-dark-muted); font-size: 16px; line-height: 1.6; }
.concepts li b { color: var(--on-dark); font-weight: 600; }
.concepts .n { color: var(--gold); font-size: 30px; font-weight: 200; font-stretch: 62%; line-height: 1; }
.program { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
.program div { border: 1px solid var(--line-light); border-radius: var(--radius); padding: 24px; display: flex; flex-direction: column; gap: 8px; }
.program .m { font-size: 40px; font-weight: 300; font-stretch: 75%; line-height: 1; color: var(--bronze); }
.program h3 { font-size: 18px; font-weight: 700; font-stretch: 112%; }
.program p { color: var(--on-light-muted); font-size: 14px; line-height: 1.55; }
@media (max-width: 1100px) {
  .svc-grid { grid-template-columns: 1fr 1fr; }
  .svc:nth-child(3n+2), .svc:nth-child(3n) { padding-left: 0; border-left: 0; }
  .svc:nth-child(even) { padding-left: 24px; border-left: 1px solid var(--line-dark); }
  .pillars, .program { grid-template-columns: 1fr 1fr; }
  .concepts { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .svc-grid, .pillars, .program { grid-template-columns: 1fr; }
  .svc:nth-child(even) { padding-left: 0; border-left: 0; }
}
"""

# Proyecto construido que respalda cada servicio (enlace bajo la descripción)
SVC_WORK = {'Remodelaciones': '<a href="once-once.html" class="link" style="display:inline-block;margin-top:14px;font-size:13px">Ver remodelación Once Once →</a>'}

svc_html = '\n'.join(
    f'      <article class="svc"><span class="mono n">{i + 1:02d}</span><h3>{n}</h3><p>{t}</p>{SVC_WORK.get(n, "")}</article>'
    for i, (n, t) in enumerate(SERVICES))

D_FORM = '''<form class="form" id="contactForm" novalidate>
        <input type="hidden" name="_subject" value="Consulta Diseño para negocios — Build &amp; Create Studio">
        <div id="formBody">
          <span class="mono" style="color:var(--gold)">Formulario de contacto</span>
          <h3 class="form-title">Cuéntanos tu proyecto</h3>
          <div class="row">
            <div class="field"><label for="name">Nombre</label><input type="text" id="name" name="name" required placeholder="Tu nombre" autocomplete="name"></div>
            <div class="field"><label for="company">Empresa</label><input type="text" id="company" name="empresa" placeholder="Tu empresa" autocomplete="organization"></div>
          </div>
          <div class="row">
            <div class="field"><label for="email">Correo</label><input type="email" id="email" name="email" required placeholder="tu@empresa.com" autocomplete="email"></div>
            <div class="field"><label for="phone">Teléfono o WhatsApp</label><input type="tel" id="phone" name="telefono" placeholder="+502 0000 0000" autocomplete="tel"></div>
          </div>
          <div class="field">
            <label for="type">Tipo de proyecto</label>
            <select id="type" name="project_type" required>
              <option value="">Selecciona una opción</option>
''' + '\n'.join(f'              <option value="{n.lower()}">{n}</option>' for n, _ in SERVICES) + '''
              <option value="otro">Otro / Consulta general</option>
            </select>
          </div>
          <div class="row">
            <div class="field"><label for="location">Ubicación</label><input type="text" id="location" name="ubicacion" placeholder="Zona o municipio"></div>
            <div class="field"><label for="area">m² aproximados</label><input type="text" id="area" name="metros_cuadrados" placeholder="Del espacio" inputmode="numeric"></div>
          </div>
          <div class="field"><label for="message">Mensaje</label><textarea id="message" name="message" required placeholder="Tipo de espacio, m² aproximados y qué buscas lograr"></textarea></div>
          <button type="submit" class="btn btn-light form-submit" id="formSubmitBtn">Enviar mensaje →</button>
          <p class="form-error" id="formError" role="alert">Revisa los campos obligatorios o escríbenos a info@bcarqstudio.com</p>
        </div>
        <div class="form-success" id="formSuccess" role="status">
          <h3>Mensaje recibido</h3>
          <p>Te respondemos en menos de 24 horas hábiles. Revisa también tu carpeta de spam.</p>
        </div>
      </form>'''

DPAGE = head(D_TITLE, D_DESC, D_URL, 'img/restaurante-interior-og.jpg', d_ld) + nav('Diseño para negocios', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio" style="min-height:max(600px,min(88svh,820px))">
  <div class="hero-media">{img('edificio-w-acceso', 'Acceso comercial en planta baja del Edificio W, San Pedro Sula', 1920, 1080, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Diseño para negocios · Guatemala y Honduras</p>
        <h1 class="hero-slogan page-slogan">Diseño estratégico <span>para negocios que quieren crecer.</span></h1>
        <p class="hero-sub">Oficinas, clínicas, comercios, espacios gastronómicos y hoteles pensados para mejorar la operación, elevar la percepción de marca y aumentar el valor del inmueble.</p>
        <div class="hero-actions">
          <a href="#contacto-d" class="btn btn-light">Agendar una consulta →</a>
          <a href="{WA}?text=Hola%2C%20me%20interesa%20conocer%20sus%20servicios%20de%20dise%C3%B1o%20estrat%C3%A9gico." target="_blank" rel="noopener" class="link">Escribir por WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SERVICIOS
     ============================================================ -->
<section class="section on-dark" id="servicios-d">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Servicios</span>
        <h2 class="sec-title">Lo que diseñamos <span>para ti.</span></h2>
      </div>
      <p class="sec-lead">Cada proyecto comienza con el diagnóstico del negocio, no con el plano. Entendemos cómo opera tu empresa antes de decidir cómo se ve el espacio.</p>
    </div>
    <div class="svc-grid">
{svc_html}
    </div>
  </div>
</section>

<!-- ============================================================
     FUNDAMENTO
     ============================================================ -->
<section class="section on-light" id="fundamento">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Fundamento</span>
        <h2 class="sec-title">El diseño no es <span>solo estética.</span></h2>
      </div>
      <div class="sec-lead" style="display:flex;flex-direction:column;gap:16px">
        <p>Un espacio mal diseñado genera fricción invisible: clientes incómodos que no regresan, empleados que pierden tiempo en circulaciones deficientes, operaciones que se complican porque nadie pensó en el flujo real del negocio.</p>
        <p>El diseño estratégico parte de entender cómo funciona tu negocio antes de decidir cómo se ve. El resultado es un activo que trabaja para ti.</p>
      </div>
    </div>
    <div class="pillars">
      <div><h3>Productividad</h3><p>Espacios diseñados para el flujo real de trabajo reducen tiempos muertos y mejoran la coordinación.</p></div>
      <div><h3>Experiencia del cliente</h3><p>Un espacio que comunica bien genera confianza y aumenta la permanencia.</p></div>
      <div><h3>Valor del inmueble</h3><p>Una buena intervención puede aumentar el valor de renta o venta del inmueble.</p></div>
      <div><h3>Percepción de marca</h3><p>El espacio físico es el primer contacto tangible con tu marca. La coherencia convierte visitas en clientes recurrentes.</p></div>
    </div>
  </div>
</section>

<!-- ============================================================
     PROYECTOS RELACIONADOS
     ============================================================ -->
<section class="section on-light-2" id="trabajo">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Proyectos</span>
        <h2 class="sec-title">Trabajo <span>relacionado.</span></h2>
      </div>
      <p class="sec-lead">Mobiliario comercial, oficinas, gastronomía y comercio a nivel de calle. Cada ficha indica el estado real del proyecto.</p>
    </div>
    <div class="work">
      <a href="kishi-books.html" class="work-card half">
        <div class="work-img">{img('kishi-books-escalera', 'Kiosco de madera curvada de Kishi Books, Peri Roosevelt', 1920, 1442, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Kishi Books</span><span class="status built">Construido · 3 sedes</span></div>
        <p class="work-info">Mobiliario comercial · 3 kioscos de librería · Diseño y ejecución · 2024–2026</p>
      </a>
      <a href="navante.html" class="work-card half">
        <div class="work-img">{img('navante-lampara', 'Lámpara colgante lineal curva sobre las estaciones de trabajo de Navante', 1920, 1407, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Navante</span><span class="status built">Construido</span></div>
        <p class="work-info">Oficina · 96 m² · Diseño interior, ejecución y mobiliario · 2026</p>
      </a>
      <a href="petshop-gt.html" class="work-card full">
        <div class="work-img">{img('petshop-gt-recepcion', 'Render de la recepción de Petshop GT, Vista Hermosa, Zona 15', 1920, 1080, sizes='100vw')}</div>
        <div class="work-meta"><span class="work-name">Petshop GT</span><span class="status">Diseño aprobado</span></div>
        <p class="work-info">Tienda de mascotas · 70 m² · Vista Hermosa, Zona 15</p>
      </a>
      <a href="la-autoria.html" class="work-card half">
        <div class="work-img">{img('restaurante-interior', 'Salón del restaurante La Autoría, Huehuetenango', 1344, 768, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">La Autoría</span><span class="status">Diseño completado</span></div>
        <p class="work-info">Restaurante · 240 m² · 74 comensales · Huehuetenango</p>
      </a>
      <a href="edificio-w.html" class="work-card half">
        <div class="work-img">{img('edificio-w-acceso', 'Acceso comercial del Edificio W, San Pedro Sula', 1920, 1080, sizes='(max-width: 640px) 100vw, 50vw')}</div>
        <div class="work-meta"><span class="work-name">Edificio W</span><span class="status">Anteproyecto · En aprobación</span></div>
        <p class="work-info">Uso mixto · 2 locales comerciales a la calle · San Pedro Sula, Honduras</p>
      </a>
    </div>
  </div>
</section>

<!-- ============================================================
     CITA
     ============================================================ -->
<section class="section on-dark-2 quote-band">
  <div class="wrap">
    <p>Un espacio bien diseñado no solo se ve bien. <em>Trabaja</em> para el negocio cada día que abre sus puertas.</p>
    <div class="by"><img src="img/bryan-castro-avatar.webp" width="320" height="320" alt="Bryan Castro" loading="lazy" decoding="async"><div><strong>Bryan Castro</strong><br><span class="mono">Fundador · {BRAND}</span></div></div>
  </div>
</section>

<!-- ============================================================
     PROCESO
     ============================================================ -->
<section class="section on-light" id="proceso-d">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Proceso</span>
        <h2 class="sec-title">Cómo <span>trabajamos.</span></h2>
      </div>
    </div>
    <ol class="steps">
      <li class="step"><div class="step-n">01</div><h3 class="step-name">Reunión inicial</h3><p class="step-text">Escuchamos el negocio y los objetivos operativos y comerciales del espacio. Sin compromiso.</p></li>
      <li class="step"><div class="step-n">02</div><h3 class="step-name">Diagnóstico</h3><p class="step-text">Analizamos el espacio, restricciones técnicas, normativas y presupuesto. Te entregamos un diagnóstico honesto.</p></li>
      <li class="step"><div class="step-n">03</div><h3 class="step-name">Concepto y documentación</h3><p class="step-text">Distribución, materialidad, identidad visual y estimación de costo. Después, planos, renders, especificaciones y expediente para licitación y permisos.</p></li>
      <li class="step"><div class="step-n">04</div><h3 class="step-name">Ejecución</h3><p class="step-text">Supervisión de obra y control de que lo construido corresponda a lo diseñado.</p></li>
    </ol>
  </div>
</section>

<!-- ============================================================
     CONTACTO
     ============================================================ -->
<section class="section on-dark" id="contacto-d">
  <div class="wrap contact">
    <div>
      <span class="mono sec-label">Contacto</span>
      <h2 class="sec-title">Hablemos de <span>tu proyecto.</span></h2>
      <p class="sec-lead" style="margin-top:28px">Una primera reunión para evaluar el espacio, el negocio y los objetivos. Sin compromiso y sin presentaciones de venta. Respondemos en menos de 24 horas hábiles.</p>
      <div class="host">
        <img src="img/bryan-castro-avatar.webp" width="320" height="320" alt="Bryan Castro, arquitecto y fundador de {BRAND}" loading="lazy" decoding="async">
        <div><strong>Bryan Castro</strong><span class="mono">Arquitecto · Fundador</span></div>
      </div>
      <dl class="channels" style="margin-top:32px">
        <div><dt class="mono">Email</dt><dd><a href="mailto:info@bcarqstudio.com">info@bcarqstudio.com</a></dd></div>
        <div><dt class="mono">WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">+502 5413 1753</a></dd></div>
      </dl>
    </div>
    {D_FORM}
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', FORM_JS)
DPAGE = DPAGE.replace('</style>', PAGE_A_CSS + '\n.page-slogan { font-size: clamp(34px, 6vw, 96px); }\n@media (max-width: 640px) { .page-slogan { font-size: clamp(28px, 8.6vw, 40px); } }\n</style>', 1)
open('diseno-estrategico.html', 'w', encoding='utf-8').write(DPAGE)

# ================================================================== LA AUTORÍA
L_URL = SITE + 'la-autoria.html'
L_TITLE = 'La Autoría, restaurante en Huehuetenango | Build &amp; Create Studio'
L_DESC = 'La Autoría: diseño de restaurante de cocina guatemalteca contemporánea en Huehuetenango. 240 m², 74 comensales y cocina de fuego abierta al salón.'
l_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "La Autoría", "description": L_DESC, "url": L_URL,
     "image": SITE + "img/restaurante-interior-og.jpg", "creator": ORG, "dateCreated": "2025", "inLanguage": "es",
     "creativeWorkStatus": "Diseño completado", "contentLocation": {"@type": "Place", "name": "Huehuetenango, Guatemala"}},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "#proyectos"},
        {"@type": "ListItem", "position": 3, "name": "La Autoría", "item": L_URL}]}]

LPAGE = head(L_TITLE, L_DESC, L_URL, 'img/restaurante-interior-og.jpg', l_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('restaurante-interior', 'Salón principal del restaurante La Autoría, Huehuetenango', 1344, 768, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Restaurante · Cocina guatemalteca contemporánea · Huehuetenango</p>
        <h1 class="hero-slogan">La <span>Autoría.</span></h1>
        <p class="hero-sub">Un restaurante que convierte la cocina guatemalteca y el fuego en el protagonista del espacio.</p>
        <div class="hero-actions">
          <a href="diseno-estrategico.html#contacto-d" class="btn btn-light">Diseñemos tu restaurante →</a>
          <a href="#concepto" class="link">Ver el concepto</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>Diseño completado</dd></div>
          <div><dt>Año</dt><dd>2025</dd></div>
          <div><dt>Diseño</dt><dd>{BRAND}</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     CIFRAS Y PROYECTO
     ============================================================ -->
<section class="section on-dark-2" id="proyecto">
  <div class="wrap">
    <dl class="figures" style="margin-top:0;grid-template-columns:repeat(3,minmax(0,1fr))">
      <div><dt class="mono">Área total</dt><dd>240<small> m²</small></dd></div>
      <div><dt class="mono">Comensales</dt><dd>74</dd></div>
      <div><dt class="mono">Año</dt><dd>2025</dd></div>
    </dl>
    <div class="thesis" style="margin-top:96px">
      <h2 class="thesis-quote">El fuego como <b>arquitectura.</b></h2>
      <div class="thesis-text">
        <p>La Autoría nació del encargo de diseñar un concepto gastronómico de alto impacto en Huehuetenango. El cliente quería un espacio que expresara la identidad culinaria guatemalteca con autenticidad y sofisticación: un lugar donde la cocina abierta y el fuego real fueran tan parte de la experiencia como la comida misma.</p>
        <p>La solución fue estructurar el programa alrededor de la cocina de fuego como elemento central y visible. El salón se organiza en torno a ella: los comensales miran a los chefs trabajar sobre brasas reales, bajo techos de ladrillo en arco y frente a una barra de degustación que conecta la cocina con el salón.</p>
        <p><strong>La paleta de materiales (terracota, ladrillo visto, madera oscura y latón) responde a la identidad del altiplano guatemalteco.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     GALERIA
     ============================================================ -->
<section class="section on-dark" id="galeria">
  <div class="wrap">
    <div class="gal">
      <figure class="w7"><div class="frame">{img('cocina', 'Cocina abierta de fuego del restaurante La Autoría, Huehuetenango', 1344, 768, sizes='(max-width: 640px) 100vw, 60vw')}</div><figcaption><strong>Cocina abierta</strong><span class="mono">Parrilla de leña y horno de ladrillo</span></figcaption></figure>
      <figure class="w5"><div class="frame">{img('restaurante-interior', 'Salón de comensales de La Autoría, Huehuetenango', 1344, 768, sizes='(max-width: 640px) 100vw, 40vw')}</div><figcaption><strong>Salón principal</strong><span class="mono">74 comensales</span></figcaption></figure>
    </div>
    <p class="gal-note">Renders del diseño entregado.</p>
  </div>
</section>

<!-- ============================================================
     CONCEPTO
     ============================================================ -->
<section class="section on-dark-2" id="concepto">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Concepto de diseño</span>
        <h2 class="sec-title">La brasa como <span>razón de ser.</span></h2>
      </div>
    </div>
    <ol class="concepts">
      <li><span class="n">01</span><span><b>Cocina abierta como protagonista.</b> El área de preparación ocupa el centro visual del restaurante: los comensales ven, escuchan y sienten la cocina en tiempo real.</span></li>
      <li><span class="n">02</span><span><b>Paleta de materiales de fuego.</b> Terracota, ladrillo visto en arco, madera oscura y latón: cada material habla del calor, la textura y la identidad latinoamericana.</span></li>
      <li><span class="n">03</span><span><b>Vegetación integrada.</b> Plantas colgantes y elementos vivos que contrastan con la dureza del ladrillo y la terracota.</span></li>
      <li><span class="n">04</span><span><b>Iluminación estratificada.</b> Luminarias de ratán, luz cálida sobre las mesas y retroiluminación de la barra: tres niveles que transforman el ambiente del almuerzo a la cena.</span></li>
    </ol>
  </div>
</section>

<!-- ============================================================
     PROGRAMA Y FICHA
     ============================================================ -->
<section class="section on-light" id="programa">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Programa arquitectónico</span>
        <h2 class="sec-title">240 m² <span>bien repartidos.</span></h2>
      </div>
    </div>
    <div class="program">
      <div><span class="m">145 m²</span><h3>Salón principal</h3><p>74 comensales en mesas de 2, 4 y 6 personas. Barra alta con vista directa a la cocina.</p></div>
      <div><span class="m">58 m²</span><h3>Cocina abierta</h3><p>Parrilla de leña, horno de ladrillo, estación fría y barra de degustación con asientos frente al chef.</p></div>
      <div><span class="m">37 m²</span><h3>Bar y recepción</h3><p>Área de espera con coctelería, barra en latón y madera, y recepción de reservaciones.</p></div>
      <div><span class="m">Incluido</span><h3>Servicios y bodega</h3><p>Bodega, área de lavado, cuarto frío y zona de personal independiente del área pública.</p></div>
    </div>
    <dl class="spec" style="margin-top:64px;border-color:var(--line-light)">
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Proyecto</dt><dd>La Autoría</dd></div>
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Tipología</dt><dd>Restaurante · Cocina abierta</dd></div>
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Ubicación</dt><dd>Huehuetenango, Guatemala</dd></div>
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Área construida</dt><dd>240 m²</dd></div>
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Chef · Cliente</dt><dd>Javier Buezo</dd></div>
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Rol de {BRAND}</dt><dd>Diseño arquitectónico e interiorismo</dd></div>
      <div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">Estado</dt><dd>Diseño completado</dd></div>
    </dl>
  </div>
</section>

<!-- ============================================================
     CIERRE
     ============================================================ -->
<section class="section on-dark-2 quote-band">
  <div class="wrap">
    <p>La autoría del chef sobre su cocina y la nuestra sobre el espacio. <em>Diseñamos</em> para que ambas se vean.</p>
    <div class="by"><img src="img/bryan-castro-avatar.webp" width="320" height="320" alt="Bryan Castro" loading="lazy" decoding="async"><div><strong>Bryan Castro</strong><br><span class="mono">Director de diseño · {BRAND}</span></div></div>
    <div class="cta-row">
      <a href="diseno-estrategico.html#contacto-d" class="btn btn-light">Diseñemos tu restaurante →</a>
      <a href="index.html#proyectos" class="link">Ver todos los proyectos</a>
    </div>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
LPAGE = LPAGE.replace('</style>', W_CSS + PAGE_A_CSS + '</style>', 1)
open('la-autoria.html', 'w', encoding='utf-8').write(LPAGE)

# ================================================================== FOTOS VERTICALES (fichas de obra construida)
TALL_CSS = """
/* ===== GALERIA VERTICAL (fotografías de obra) ===== */
.gal .w3 { grid-column: span 3; }
.gal .w6 { grid-column: span 6; }
.gal .tall img { aspect-ratio: 3 / 4; }
.sede + .sede { margin-top: 120px; }
.sede-meta { display: flex; flex-wrap: wrap; gap: 8px 28px; margin: 0 0 28px; padding: 16px 0; border-top: 1px solid var(--line-dark); border-bottom: 1px solid var(--line-dark); }
.sede-meta div { display: flex; gap: 10px; align-items: baseline; }
.sede-meta dt { font-family: var(--mono); font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--on-dark-muted); }
.sede-meta dd { margin: 0; color: var(--on-dark); font-size: 15px; }
@media (max-width: 1100px) { .gal .w3 { grid-column: span 6; } }
@media (max-width: 640px) { .gal .w3, .gal .w6 { grid-column: span 6; } .sede + .sede { margin-top: 80px; } }
"""

def vfig(stem, alt, title, sub, cls='w4 tall', sizes='(max-width: 1100px) 50vw, 33vw'):
    return f'<figure class="{cls}"><div class="frame">{img(stem, alt, 1200, 2131, sizes=sizes)}</div><figcaption><strong>{title}</strong><span class="mono">{sub}</span></figcaption></figure>'

def sede_meta(*pairs):
    return '<dl class="sede-meta">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in pairs) + '</dl>'

def ficha(rows):
    return ''.join(f'<div style="border-color:var(--line-light)"><dt style="color:var(--on-light-muted)">{a}</dt><dd>{b}</dd></div>' for a, b in rows)

def crumbs(name, url):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Proyectos", "item": SITE + "#proyectos"},
        {"@type": "ListItem", "position": 3, "name": name, "item": url}]}

# ================================================================== KISHI BOOKS (3 sedes construidas)
K_URL = SITE + 'kishi-books.html'
K_TITLE = 'Kishi Books, 3 kioscos de librería | Build &amp; Create Studio'
K_DESC = 'Kishi Books: tres kioscos de librería en madera curvada en Peri Roosevelt, Naranjo Mall y Plaza Girasoles, Chiquimula. Diseño y ejecución, 2024–2026.'
KISHI_SEDES = [
    ("Kishi Books · Peri Roosevelt", "Peri Roosevelt, Ciudad de Guatemala", "2024", "img/kishi-books-escalera-og.jpg"),
    ("Kishi Books · Naranjo Mall", "Naranjo Mall", "2025", SITE + "img/kishi-books-naranjo-vista-general.webp"),
    ("Kishi Books · Plaza Girasoles", "Plaza Girasoles, Chiquimula", "2026", "img/kishi-books-chiquimula-vista-frontal-og.jpg"),
]
k_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Kishi Books · Kioscos de librería", "description": K_DESC,
     "url": K_URL, "image": SITE + "img/kishi-books-escalera-og.jpg", "creator": ORG, "inLanguage": "es", "creativeWorkStatus": "Construido",
     "hasPart": [{"@type": "CreativeWork", "name": n, "dateCreated": y, "creativeWorkStatus": "Construido", "creator": ORG,
                  "image": im if im.startswith('http') else SITE + im, "contentLocation": {"@type": "Place", "name": p}} for n, p, y, im in KISHI_SEDES]},
    crumbs("Kishi Books", K_URL)]

def kfig(stem, alt, title, sub, cls, sizes='(max-width: 640px) 100vw, 50vw'):
    return f'<figure class="{cls}"><div class="frame">{img(stem, alt, 1920, 1442, sizes=sizes)}</div><figcaption><strong>{title}</strong><span class="mono">{sub}</span></figcaption></figure>'

KPAGE = head(K_TITLE, K_DESC, K_URL, 'img/kishi-books-escalera-og.jpg', k_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('kishi-books-escalera', 'Kiosco de madera curvada de Kishi Books junto a la escalera del atrio, Peri Roosevelt', 1920, 1442, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Mobiliario comercial · Librería · 3 sedes construidas</p>
        <h1 class="hero-slogan">Kishi <span>Books.</span></h1>
        <p class="hero-sub">Tres kioscos de madera curvada para la misma marca: Peri Roosevelt, Naranjo Mall y Plaza Girasoles en Chiquimula. Un mismo lenguaje adaptado a cada planta, con diseño y ejecución de cada pieza.</p>
        <div class="hero-actions">
          <a href="diseno-estrategico.html?tipo=mobiliario%20estrat%C3%A9gico#contacto-d" class="btn btn-light">Diseñemos tu mobiliario →</a>
          <a href="#sedes" class="link">Ver las 3 sedes</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>3 sedes construidas</dd></div>
          <div><dt>Periodo</dt><dd>2024 – 2026</dd></div>
          <div><dt>Alcance</dt><dd>Diseño y ejecución</dd></div>
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
    <dl class="figures" style="margin-top:0;grid-template-columns:repeat(3,minmax(0,1fr))">
      <div><dt class="mono">Sedes construidas</dt><dd>3</dd></div>
      <div><dt class="mono">Kiosco más largo</dt><dd>9<small> m</small></dd></div>
      <div><dt class="mono">Alcance</dt><dd style="font-size:clamp(24px,2.6vw,38px)">Diseño y ejecución</dd></div>
    </dl>
    <div class="thesis" style="margin-top:96px">
      <h2 class="thesis-quote">Un sistema que <b>viaja de sede en sede.</b></h2>
      <div class="thesis-text">
        <p>Kishi Books trabajó con nosotros su kiosco de Peri Roosevelt en 2024 y volvió para Naranjo Mall en 2025 y Plaza Girasoles en 2026. Cada sede parte del mismo lenguaje: madera curvada de estilo natural, una línea de luz continua y exhibición por ambos lados.</p>
        <p>Lo que cambia es la planta. En Peri Roosevelt el mueble sigue la escalera del atrio; en Naranjo Mall se concentra en islas escalonadas de 2 × 4 m; en Plaza Girasoles se abre en un pasillo curvo que invita a entrar.</p>
        <p><strong>Diseño y ejecución de {BRAND} en las tres sedes: del concepto a la pieza instalada.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     SEDES (fotografías de obra construida)
     ============================================================ -->
<section class="section on-dark" id="sedes">
  <div class="wrap">
    <article class="sede" id="peri-roosevelt">
      <div class="sec-head">
        <div>
          <span class="mono sec-label">Sede 01 · 2024</span>
          <h2 class="sec-title">Peri Roosevelt, <span>sigue la escalera.</span></h2>
        </div>
        <p class="sec-lead">Un kiosco de 9 metros resuelto como una sola pieza: estructura, exhibición, asiento e iluminación en el mismo mueble.</p>
      </div>
      {sede_meta(('Ubicación', 'Peri Roosevelt, Ciudad de Guatemala'), ('Medidas', '1.40 × 9 m'), ('Año', '2024'))}
      <div class="gal">
        {kfig('kishi-books-vista-general', 'Vista general del kiosco Kishi Books en el atrio de Peri Roosevelt', 'Vista general', 'Kiosco junto a la escalera', 'w12', '100vw')}
        {kfig('kishi-books-escalera-interior', 'Recorrido interior del kiosco con asiento de lectura y estantería verde', 'Recorrido interior', 'Asiento de lectura y estantería', 'w7')}
        {kfig('kishi-books-pasillo', 'Pasillo central entre los dos muebles curvos de Kishi Books', 'Pasillo central', 'Exhibición por ambos lados', 'w5')}
        {kfig('kishi-books-baranda', 'Kiosco Kishi Books con iluminación lineal junto a la baranda del atrio', 'Línea de luz', 'Perfil iluminado', 'w5')}
        {kfig('kishi-books-conjunto', 'Kiosco Kishi Books con la escalera y los asientos de lectura', 'Conjunto', 'Escalera, asientos y exhibición', 'w7')}
        <figure class="w6 tall"><div class="frame">{img('kishi-books-lectura', 'Lector sentado en los peldaños de madera del kiosco Kishi Books, Peri Roosevelt', 1200, 1598, sizes='(max-width: 640px) 50vw, 50vw')}</div><figcaption><strong>En uso</strong><span class="mono">Los peldaños como asiento de lectura</span></figcaption></figure>
        <figure class="w6 tall"><div class="frame">{img('kishi-books-exhibicion-lineal', 'Visitantes revisando libros en la exhibición lineal iluminada de Kishi Books', 1200, 1598, sizes='(max-width: 640px) 50vw, 50vw')}</div><figcaption><strong>Inauguración</strong><span class="mono">Exhibición lineal iluminada</span></figcaption></figure>
      </div>
    </article>

    <article class="sede" id="naranjo-mall">
      <div class="sec-head">
        <div>
          <span class="mono sec-label">Sede 02 · 2025</span>
          <h2 class="sec-title">Naranjo Mall, <span>islas escalonadas.</span></h2>
        </div>
        <p class="sec-lead">Un kiosco compacto de 2 × 4 m en el centro del pasillo: niveles de exhibición iluminados que se leen desde cualquier ángulo.</p>
      </div>
      {sede_meta(('Ubicación', 'Naranjo Mall'), ('Medidas', '2 × 4 m'), ('Año', '2025'))}
      <div class="gal">
        {vfig('kishi-books-naranjo-vista-general', 'Kiosco Kishi Books en el pasillo central de Naranjo Mall', 'Vista general', 'Kiosco en el pasillo')}
        {vfig('kishi-books-naranjo-mesa-exhibicion', 'Isla de exhibición escalonada con iluminación lineal, Kishi Books Naranjo Mall', 'Isla central', 'Niveles iluminados')}
        {vfig('kishi-books-naranjo-isla', 'Mueble de exhibición curvo de Kishi Books en Naranjo Mall', 'Exhibición perimetral', 'Esquinas curvas')}
      </div>
    </article>

    <article class="sede" id="plaza-girasoles">
      <div class="sec-head">
        <div>
          <span class="mono sec-label">Sede 03 · 2026</span>
          <h2 class="sec-title">Plaza Girasoles, <span>un pasillo curvo.</span></h2>
        </div>
        <p class="sec-lead">Dos brazos de madera curvada forman un recorrido interior: el cliente entra al kiosco en lugar de mirarlo desde fuera.</p>
      </div>
      {sede_meta(('Ubicación', 'Plaza Girasoles, Chiquimula'), ('Año', '2026'))}
      <div class="gal">
        {vfig('kishi-books-chiquimula-pasillo', 'Pasillo curvo entre los muebles de madera de Kishi Books, Plaza Girasoles, Chiquimula', 'Pasillo curvo', 'Recorrido interior')}
        {vfig('kishi-books-chiquimula-recorrido', 'Recorrido del kiosco Kishi Books con luz lineal en la base, Chiquimula', 'Recorrido', 'Luz lineal en la base')}
        {vfig('kishi-books-chiquimula-esquina', 'Esquina del kiosco Kishi Books con el logotipo de la marca, Chiquimula', 'Remate con marca', 'Identidad en el mueble')}
        {vfig('kishi-books-chiquimula-vista-frontal', 'Vista frontal del kiosco Kishi Books en Plaza Girasoles, Chiquimula', 'Vista frontal', 'Exhibición escalonada')}
        {vfig('kishi-books-chiquimula-isla', 'Isla de exhibición de Kishi Books con la mascota de la marca, Chiquimula', 'Isla de acceso', 'Señal visible a distancia')}
        {vfig('kishi-books-chiquimula-remate', 'Remate curvo del kiosco Kishi Books con exhibición en niveles, Chiquimula', 'Remate curvo', 'Exhibición en niveles')}
      </div>
    </article>
    <p class="gal-note">Fotografías de los kioscos construidos e instalados.</p>
  </div>
</section>

<!-- ============================================================
     TESTIMONIO
     ============================================================ -->
{testimonio(link=False)}

<!-- ============================================================
     CONCEPTO
     ============================================================ -->
<section class="section on-dark" id="concepto">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Decisiones de diseño</span>
        <h2 class="sec-title">Un lenguaje, <span>tres plantas.</span></h2>
      </div>
    </div>
    <ol class="concepts">
      <li><span class="n">01</span><span><b>Se adapta al lugar.</b> Escalera, pasillo central o recorrido interior: el mueble responde a la planta de cada centro comercial.</span></li>
      <li><span class="n">02</span><span><b>Exhibe por ambos lados.</b> Estanterías hacia el pasillo y hacia el interior del kiosco, sin espaldas muertas.</span></li>
      <li><span class="n">03</span><span><b>Luz como dibujo.</b> Una línea de luz continua sigue el perfil curvo y convierte el mueble en una señal visible a distancia.</span></li>
      <li><span class="n">04</span><span><b>Marca reconocible.</b> La madera curvada de estilo natural se repite en las tres sedes y se vuelve parte de la identidad de la marca.</span></li>
    </ol>
  </div>
</section>

<!-- ============================================================
     FICHA
     ============================================================ -->
<section class="section on-light" id="ficha">
  <div class="wrap">
    <span class="mono sec-label">Ficha técnica</span>
    <dl class="spec" style="border-color:var(--line-light)">
      {ficha([('Cliente', 'Kishi Books'), ('Tipología', 'Kioscos de librería · Mobiliario comercial'),
              ('Sede 01', 'Peri Roosevelt, Ciudad de Guatemala · 1.40 × 9 m · 2024'),
              ('Sede 02', 'Naranjo Mall · 2 × 4 m · 2025'),
              ('Sede 03', 'Plaza Girasoles, Chiquimula · 2026'),
              ('Material', 'Madera curvada, estilo natural'), (f'Alcance de {BRAND}', 'Diseño y ejecución'), ('Estado', 'Construido · 3 sedes')])}
    </dl>
    <div class="cta-row">
      <a href="diseno-estrategico.html?tipo=mobiliario%20estrat%C3%A9gico#contacto-d" class="btn btn-dark">Diseñemos tu mobiliario →</a>
      <a href="index.html#proyectos" class="link">Ver todos los proyectos</a>
    </div>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
KPAGE = KPAGE.replace('</style>', W_CSS + PAGE_A_CSS + TALL_CSS + TESTI_CSS + '</style>', 1)
open('kishi-books.html', 'w', encoding='utf-8').write(KPAGE)

# ================================================================== NAVANTE (oficina construida)
N_URL = SITE + 'navante.html'
N_TITLE = 'Navante, diseño de oficina de 96 m² | Build &amp; Create Studio'
N_DESC = 'Navante: oficina de 96 m² para una empresa de logística marítima y aérea. Diseño interior, ejecución y mobiliario de Build & Create Studio, construida en 2026.'
n_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Navante · Oficina", "description": N_DESC,
     "url": N_URL, "image": SITE + "img/navante-lampara-og.jpg", "creator": ORG, "inLanguage": "es",
     "creativeWorkStatus": "Construido", "dateCreated": "2026"},
    crumbs("Navante", N_URL)]

NPAGE = head(N_TITLE, N_DESC, N_URL, 'img/navante-lampara-og.jpg', n_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('navante-lampara', 'Lámpara colgante lineal curva sobre las estaciones de trabajo de Navante', 1920, 1407, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Oficina corporativa · Logística marítima y aérea</p>
        <h1 class="hero-slogan">Navante <span>Oficina.</span></h1>
        <p class="hero-sub">Oficina de 96 m² para una empresa de logística marítima y aérea: estaciones de trabajo abiertas, salas privadas en vidrio y luz que dibuja el espacio. Diseño interior, ejecución y mobiliario.</p>
        <div class="hero-actions">
          <a href="diseno-estrategico.html?tipo=dise%C3%B1o%20interior#contacto-d" class="btn btn-light">Diseñemos tu oficina →</a>
          <a href="#galeria" class="link">Ver fotografías</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>Construido · 2026</dd></div>
          <div><dt>Área</dt><dd>96 m²</dd></div>
          <div><dt>Alcance</dt><dd>Diseño interior, ejecución y mobiliario</dd></div>
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
    <dl class="figures" style="margin-top:0;grid-template-columns:repeat(3,minmax(0,1fr))">
      <div><dt class="mono">Área</dt><dd>96<small> m²</small></dd></div>
      <div><dt class="mono">Año</dt><dd>2026</dd></div>
      <div><dt class="mono">Alcance</dt><dd style="font-size:clamp(24px,2.6vw,38px)">Llave en mano</dd></div>
    </dl>
    <div class="thesis" style="margin-top:96px">
      <h2 class="thesis-quote">Una oficina que <b>se mueve como su negocio.</b></h2>
      <div class="thesis-text">
        <p>Navante es una empresa de logística marítima y aérea. Su oficina reúne en 96 m² un área de trabajo abierta, salas privadas para llamadas y reuniones, y una cocineta para el equipo.</p>
        <p>Las luminarias lineales curvas recorren el techo y ordenan las zonas de trabajo. El color marca cada función: turquesa en el almacenamiento, naranja en la cocineta, amarillo en el acceso. Las salas privadas se cierran con vidrio y perfil negro para no perder luz ni amplitud.</p>
        <p><strong>Diseño interior, ejecución y mobiliario de {BRAND}: un solo responsable de principio a fin.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     GALERIA (fotografías de obra construida)
     ============================================================ -->
<section class="section on-dark" id="galeria">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Fotografías del proyecto construido</span>
        <h2 class="sec-title">Luz, color <span>y vidrio.</span></h2>
      </div>
      <p class="sec-lead">96 m² con área abierta, salas privadas y cocineta, resueltos con un mismo sistema de luz y mobiliario.</p>
    </div>
    <div class="gal">
      {vfig('navante-acceso', 'Acceso a la oficina de Navante con puerta de vidrio y muro amarillo', 'Acceso', 'Vidrio y perfil negro', 'w3 tall', '(max-width: 1100px) 50vw, 25vw')}
      {vfig('navante-estaciones', 'Estaciones de trabajo de Navante bajo luminarias lineales curvas', 'Estaciones de trabajo', 'Luz lineal curva', 'w3 tall', '(max-width: 1100px) 50vw, 25vw')}
      {vfig('navante-cocineta', 'Cocineta de Navante con salpicadero naranja y gabinetes blancos', 'Cocineta', 'Color por función', 'w3 tall', '(max-width: 1100px) 50vw, 25vw')}
      {vfig('navante-area-abierta', 'Área abierta de la oficina de Navante con salas privadas en vidrio', 'Área abierta', 'Salas privadas en vidrio', 'w3 tall', '(max-width: 1100px) 50vw, 25vw')}
    </div>
    <p class="gal-note">Fotografías de la oficina construida.</p>
  </div>
</section>

<!-- ============================================================
     CONCEPTO
     ============================================================ -->
<section class="section on-dark-2" id="concepto">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Decisiones de diseño</span>
        <h2 class="sec-title">Cuatro decisiones, <span>96 m².</span></h2>
      </div>
    </div>
    <ol class="concepts">
      <li><span class="n">01</span><span><b>Luz que ordena.</b> Luminarias lineales curvas suspendidas sobre cada grupo de trabajo, en lugar de una retícula uniforme.</span></li>
      <li><span class="n">02</span><span><b>Color por función.</b> Turquesa, naranja y amarillo identifican almacenamiento, cocineta y acceso sin necesidad de señalética.</span></li>
      <li><span class="n">03</span><span><b>Privacidad sin perder luz.</b> Salas cerradas con vidrio y perfil negro: espacios privados que no cortan la luz ni la amplitud.</span></li>
      <li><span class="n">04</span><span><b>Mobiliario integrado.</b> Estaciones, gabinetes y cocineta definidos junto con el diseño interior, como un solo proyecto.</span></li>
    </ol>
  </div>
</section>

<!-- ============================================================
     FICHA
     ============================================================ -->
<section class="section on-light" id="ficha">
  <div class="wrap">
    <span class="mono sec-label">Ficha técnica</span>
    <dl class="spec" style="border-color:var(--line-light)">
      {ficha([('Cliente', 'Navante'), ('Giro', 'Logística marítima y aérea'), ('Tipología', 'Oficina corporativa'), ('Área', '96 m²'),
              (f'Alcance de {BRAND}', 'Diseño interior, ejecución y mobiliario'), ('Año', '2026'), ('Estado', 'Construido')])}
    </dl>
    <div class="cta-row">
      <a href="diseno-estrategico.html?tipo=dise%C3%B1o%20interior#contacto-d" class="btn btn-dark">Diseñemos tu oficina →</a>
      <a href="index.html#proyectos" class="link">Ver todos los proyectos</a>
    </div>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
NPAGE = NPAGE.replace('</style>', W_CSS + PAGE_A_CSS + TALL_CSS + '</style>', 1)
open('navante.html', 'w', encoding='utf-8').write(NPAGE)

# ================================================================== PETSHOP GT (diseño aprobado)
P_URL = SITE + 'petshop-gt.html'
P_TITLE = 'Petshop GT, diseño de tienda de mascotas | Build &amp; Create Studio'
P_DESC = 'Petshop GT: diseño de tienda de mascotas de 70 m² en Vista Hermosa, Zona 15, Ciudad de Guatemala. Tienda, recepción, estancias y grooming. Diseño aprobado.'
p_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Petshop GT · Tienda de mascotas", "description": P_DESC,
     "url": P_URL, "image": SITE + "img/petshop-gt-recepcion-og.jpg", "creator": ORG, "inLanguage": "es",
     "creativeWorkStatus": "Diseño aprobado", "contentLocation": {"@type": "Place", "name": "Vista Hermosa, Zona 15, Ciudad de Guatemala"}},
    crumbs("Petshop GT", P_URL)]

def pfig(stem, alt, title, sub, cls, sizes='(max-width: 640px) 100vw, 50vw'):
    return f'<figure class="{cls}"><div class="frame">{img(stem, alt, 1920, 1080, sizes=sizes)}</div><figcaption><strong>{title}</strong><span class="mono">{sub}</span></figcaption></figure>'

PPAGE = head(P_TITLE, P_DESC, P_URL, 'img/petshop-gt-recepcion-og.jpg', p_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('petshop-gt-recepcion', 'Render de la recepción de Petshop GT con mostrador curvo y estancias en vidrio', 1920, 1080, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Comercio · Tienda de mascotas · Vista Hermosa, Zona 15</p>
        <h1 class="hero-slogan">Petshop <span>GT.</span></h1>
        <p class="hero-sub">Tienda de mascotas de 70 m² pensada como un espacio de bienestar: recepción, tienda, estancias en vidrio y grooming bajo un mismo lenguaje de madera, verde y luz.</p>
        <div class="hero-actions">
          <a href="diseno-estrategico.html?tipo=dise%C3%B1o%20interior#contacto-d" class="btn btn-light">Diseñemos tu local →</a>
          <a href="#galeria" class="link">Ver el diseño</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>Diseño aprobado</dd></div>
          <div><dt>Área</dt><dd>70 m²</dd></div>
          <div><dt>Alcance</dt><dd>Diseño</dd></div>
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
    <dl class="figures" style="margin-top:0;grid-template-columns:repeat(3,minmax(0,1fr))">
      <div><dt class="mono">Área</dt><dd>70<small> m²</small></dd></div>
      <div><dt class="mono">Zonas</dt><dd>4</dd></div>
      <div><dt class="mono">Estado</dt><dd style="font-size:clamp(24px,2.6vw,38px)">Diseño aprobado</dd></div>
    </dl>
    <div class="thesis" style="margin-top:96px">
      <h2 class="thesis-quote">Una tienda que se siente <b>como un spa.</b></h2>
      <div class="thesis-text">
        <p>El concepto parte del bienestar animal: madera natural, verde profundo, blanco y plantas como base de todo el local. La mascota y su dueño entran a un espacio tranquilo, no a una bodega de productos.</p>
        <p>En 70 m² conviven cuatro zonas: recepción con mostrador curvo, estancias en vidrio a la vista, tienda con exhibición a ambos lados y un área de grooming con baño elevado.</p>
        <p><strong>Diseño de {BRAND}, aprobado por el cliente.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     GALERIA (renders del diseño aprobado)
     ============================================================ -->
<section class="section on-dark" id="galeria">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Diseño aprobado</span>
        <h2 class="sec-title">Madera, verde <span>y bienestar.</span></h2>
      </div>
      <p class="sec-lead">Un mismo lenguaje recorre las cuatro zonas: madera natural, verde, luz lineal y vegetación.</p>
    </div>
    <div class="gal">
      {pfig('petshop-gt-estancias', 'Render del recorrido de Petshop GT con estancias en vidrio para mascotas', 'Recorrido', 'Estancias en vidrio a la vista', 'w12', '100vw')}
      {pfig('petshop-gt-tienda', 'Render de la tienda de Petshop GT con estanterías de producto a ambos lados', 'Tienda', 'Exhibición a ambos lados', 'w7')}
      {pfig('petshop-gt-grooming', 'Render del área de grooming de Petshop GT con baño elevado', 'Grooming', 'Baño elevado y repisas', 'w5')}
      {pfig('petshop-gt-concepto', 'Moodboard de Petshop GT con madera, verde, blanco y terrazo', 'Concepto', 'Paleta y materiales', 'w12', '100vw')}
    </div>
    <p class="gal-note">Renders del diseño aprobado.</p>
  </div>
</section>

<!-- ============================================================
     CONCEPTO
     ============================================================ -->
<section class="section on-dark-2" id="concepto">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Decisiones de diseño</span>
        <h2 class="sec-title">Cuatro zonas, <span>70 m².</span></h2>
      </div>
    </div>
    <ol class="concepts">
      <li><span class="n">01</span><span><b>Recepción curva.</b> Un mostrador blanco de líneas suaves recibe y ordena el recorrido hacia el resto del local.</span></li>
      <li><span class="n">02</span><span><b>Estancias a la vista.</b> Módulos en vidrio con estructura de madera: las mascotas quedan visibles y el local se siente abierto.</span></li>
      <li><span class="n">03</span><span><b>Tienda en pasillo.</b> Estanterías a ambos lados aprovechan cada metro lineal para producto.</span></li>
      <li><span class="n">04</span><span><b>Grooming integrado.</b> Baño elevado con escalones para la mascota, azulejo blanco y almacenamiento en verde.</span></li>
    </ol>
  </div>
</section>

<!-- ============================================================
     FICHA
     ============================================================ -->
<section class="section on-light" id="ficha">
  <div class="wrap">
    <span class="mono sec-label">Ficha técnica</span>
    <dl class="spec" style="border-color:var(--line-light)">
      {ficha([('Cliente', 'Petshop GT'), ('Tipología', 'Tienda de mascotas'), ('Ubicación', 'Vista Hermosa, Zona 15, Ciudad de Guatemala'), ('Área', '70 m²'),
              (f'Alcance de {BRAND}', 'Diseño'), ('Estado', 'Diseño aprobado')])}
    </dl>
    <div class="cta-row">
      <a href="diseno-estrategico.html?tipo=dise%C3%B1o%20interior#contacto-d" class="btn btn-dark">Diseñemos tu local →</a>
      <a href="index.html#proyectos" class="link">Ver todos los proyectos</a>
    </div>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
PPAGE = PPAGE.replace('</style>', W_CSS + PAGE_A_CSS + TALL_CSS + '</style>', 1)
open('petshop-gt.html', 'w', encoding='utf-8').write(PPAGE)

# ================================================================== CASA MILPAS ALTAS (diseño completado)
M_URL = SITE + 'casa-milpas-altas.html'
M_TITLE = 'Casa Milpas Altas, Sacatepéquez | Build &amp; Create Studio'
M_DESC = 'Casa Milpas Altas: vivienda de 120 m² en San Miguel Milpas Altas, Sacatepéquez. Concepto ecosistema cuántico. Diseño arquitectónico e interiorismo, 2024.'
m_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Casa Milpas Altas · Ecosistema cuántico", "description": M_DESC,
     "url": M_URL, "image": SITE + "img/casa-milpas-altas-fachada-og.jpg", "creator": ORG, "inLanguage": "es",
     "creativeWorkStatus": "Diseño completado", "dateCreated": "2024",
     "contentLocation": {"@type": "Place", "name": "San Miguel Milpas Altas, Sacatepéquez, Guatemala"}},
    crumbs("Casa Milpas Altas", M_URL)]

MPAGE = head(M_TITLE, M_DESC, M_URL, 'img/casa-milpas-altas-fachada-og.jpg', m_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('casa-milpas-altas-fachada', 'Render de Casa Milpas Altas con muros curvos, cúpula geodésica y terrazas de piedra en el bosque', 1920, 1080, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Vivienda · San Miguel Milpas Altas, Sacatepéquez</p>
        <h1 class="hero-slogan">Casa <span>Milpas Altas.</span></h1>
        <p class="hero-sub">Una casa de 120 m² en una ladera boscosa, pensada como un ecosistema: el lugar donde sus dueños viven y cultivan lo que llevarán a su restaurante.</p>
        <div class="hero-actions">
          <a href="index.html#contacto" class="btn btn-light">Diseñemos tu casa →</a>
          <a href="#galeria" class="link">Ver el diseño</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>Diseño completado · 2024</dd></div>
          <div><dt>Área</dt><dd>120 m²</dd></div>
          <div><dt>Alcance</dt><dd>Diseño arquitectónico e interiorismo</dd></div>
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
    <dl class="figures" style="margin-top:0;grid-template-columns:repeat(3,minmax(0,1fr))">
      <div><dt class="mono">Área</dt><dd>120<small> m²</small></dd></div>
      <div><dt class="mono">Año</dt><dd>2024</dd></div>
      <div><dt class="mono">Concepto</dt><dd style="font-size:clamp(24px,2.6vw,38px)">Ecosistema cuántico</dd></div>
    </dl>
    <div class="thesis" style="margin-top:96px">
      <h2 class="thesis-quote">Todo lo que se crea aquí <b>se expande.</b></h2>
      <div class="thesis-text">
        <p>Los propietarios eligieron este terreno en San Miguel Milpas Altas para sembrar los cultivos que llevarán a su restaurante. La casa nace de esa decisión: no es solo un lugar para vivir, es parte del ciclo que va de la tierra a la mesa.</p>
        <p>De ahí el concepto <strong>ecosistema cuántico</strong>: un espacio donde lo que se siembra, se cocina y se vive se expande hacia todo lo demás. La casa se asienta en la ladera con terrazas de piedra, muros curvos de textura natural y una cúpula geodésica que lleva la luz al centro de la vida diaria.</p>
        <p><strong>Diseño arquitectónico e interiorismo de {BRAND}.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     GALERIA (renders del diseño completado)
     ============================================================ -->
<section class="section on-dark" id="galeria">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Diseño completado</span>
        <h2 class="sec-title">Piedra, bosque <span>y luz cenital.</span></h2>
      </div>
      <p class="sec-lead">La casa sigue la pendiente del terreno y se abre al bosque; adentro, la cúpula ordena la sala, el comedor y la cocina.</p>
    </div>
    <div class="gal">
      {pfig('casa-milpas-altas-terrazas', 'Render de las terrazas de piedra y los muros curvos de Casa Milpas Altas en la ladera', 'Terrazas en la ladera', 'Muros de piedra y jardín', 'w12', '100vw')}
      {pfig('casa-milpas-altas-sala-cupula', 'Render de la sala y comedor de Casa Milpas Altas bajo la cúpula geodésica', 'Bajo la cúpula', 'Sala y comedor', 'w7')}
      {pfig('casa-milpas-altas-comedor', 'Render del comedor y la cocina de Casa Milpas Altas abiertos al bosque', 'Comedor y cocina', 'Ventanales al bosque', 'w5')}
    </div>
    <p class="gal-note">Renders del diseño completado.</p>
  </div>
</section>

<!-- ============================================================
     CONCEPTO
     ============================================================ -->
<section class="section on-dark-2" id="concepto">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Decisiones de diseño</span>
        <h2 class="sec-title">Cuatro decisiones, <span>120 m².</span></h2>
      </div>
    </div>
    <ol class="concepts">
      <li><span class="n">01</span><span><b>La casa sigue la pendiente.</b> Terrazas y muros de piedra escalonan la ladera y dejan espacio para jardines y cultivos.</span></li>
      <li><span class="n">02</span><span><b>Luz desde el centro.</b> Una cúpula geodésica con tragaluz corona la sala y el comedor, el corazón de la casa.</span></li>
      <li><span class="n">03</span><span><b>Formas orgánicas.</b> Muros curvos de textura natural y cubiertas que se doblan como el terreno.</span></li>
      <li><span class="n">04</span><span><b>Abierta al bosque.</b> Ventanales de piso a techo conectan el interior con el paisaje y los cultivos.</span></li>
    </ol>
  </div>
</section>

<!-- ============================================================
     FICHA
     ============================================================ -->
<section class="section on-light" id="ficha">
  <div class="wrap">
    <span class="mono sec-label">Ficha técnica</span>
    <dl class="spec" style="border-color:var(--line-light)">
      {ficha([('Proyecto', 'Casa Milpas Altas'), ('Tipología', 'Vivienda unifamiliar'), ('Ubicación', 'San Miguel Milpas Altas, Sacatepéquez, Guatemala'), ('Área', '120 m²'),
              ('Concepto', 'Ecosistema cuántico'), (f'Alcance de {BRAND}', 'Diseño arquitectónico e interiorismo'), ('Año', '2024'), ('Estado', 'Diseño completado')])}
    </dl>
    <div class="cta-row">
      <a href="index.html#contacto" class="btn btn-dark">Diseñemos tu casa →</a>
      <a href="index.html#proyectos" class="link">Ver todos los proyectos</a>
    </div>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
MPAGE = MPAGE.replace('</style>', W_CSS + PAGE_A_CSS + TALL_CSS + '</style>', 1)
open('casa-milpas-altas.html', 'w', encoding='utf-8').write(MPAGE)

# ================================================================== ONCE ONCE (remodelación construida)
O_URL = SITE + 'once-once.html'
O_TITLE = 'Once Once, remodelación de restaurante | Build &amp; Create Studio'
O_DESC = 'Once Once: remodelación interior de la barra de un restaurante en Guatemala. Diseño, ejecución y mobiliario de Build & Create Studio, construida en 2024.'
o_ld = [
    {"@context": "https://schema.org", "@type": "CreativeWork", "name": "Once Once · Remodelación de barra", "description": O_DESC,
     "url": O_URL, "image": SITE + "img/once-once-barra-logo-og.jpg", "creator": ORG, "inLanguage": "es",
     "creativeWorkStatus": "Construido", "dateCreated": "2024"},
    crumbs("Once Once", O_URL)]

OPAGE = head(O_TITLE, O_DESC, O_URL, 'img/once-once-barra-logo-og.jpg', o_ld) + nav('Proyectos', 'index.html') + f"""
<main>
<!-- ============================================================
     HERO
     ============================================================ -->
<section class="hero" id="inicio">
  <div class="hero-media">{img('once-once-barra-logo', 'Barra de concreto iluminada del restaurante Once Once con el logotipo 11:11', 1200, 2131, lazy=False, cls='on')}</div>
  <div class="hero-body">
    <div class="wrap hero-grid">
      <div>
        <p class="hero-kicker">Remodelación interior · Restaurante</p>
        <h1 class="hero-slogan">Once <span>Once.</span></h1>
        <p class="hero-sub">Remodelación de la barra de un restaurante: una pieza de concreto con luz indirecta que se vuelve el centro del lugar, bajo un techo de madera y caña con lámparas tejidas.</p>
        <div class="hero-actions">
          <a href="index.html?tipo=remodelaci%C3%B3n#contacto" class="btn btn-light">Cotiza tu remodelación →</a>
          <a href="#galeria" class="link">Ver fotografías</a>
        </div>
      </div>
      <div>
        <dl class="spec">
          <div><dt>Estado</dt><dd>Construido · 2024</dd></div>
          <div><dt>Tipo</dt><dd>Remodelación interior</dd></div>
          <div><dt>Alcance</dt><dd>Diseño, ejecución y mobiliario</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     CONCEPTO
     ============================================================ -->
<section class="section on-dark-2" id="proyecto">
  <div class="wrap">
    <div class="thesis" style="margin-top:0">
      <h2 class="thesis-quote">Una barra que <b>se vuelve el lugar.</b></h2>
      <div class="thesis-text">
        <p>La remodelación concentra la intervención donde más pesa: la barra. Un volumen de concreto con luz indirecta en todo su frente ordena el espacio y lleva la marca 11:11 a la vista de cada mesa.</p>
        <p>Alrededor, el techo de madera y caña, las lámparas tejidas y los bancos de madera mantienen el carácter cálido del restaurante.</p>
        <p><strong>Diseño, ejecución y mobiliario de {BRAND}.</strong></p>
      </div>
    </div>
  </div>
</section>

<!-- ============================================================
     GALERIA (fotografías de obra construida)
     ============================================================ -->
<section class="section on-dark" id="galeria">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <span class="mono sec-label">Fotografías del proyecto construido</span>
        <h2 class="sec-title">Concreto, luz <span>y madera.</span></h2>
      </div>
      <p class="sec-lead">Una sola pieza de concreto con luz indirecta, mobiliario de madera y lámparas tejidas.</p>
    </div>
    <div class="gal">
      {vfig('once-once-barra-logo', 'Barra de Once Once con el logotipo 11:11 y bancos de madera', 'Frente de barra', 'Marca 11:11 en el volumen')}
      {vfig('once-once-terraza', 'Vista de la barra de Once Once desde la terraza con techo de madera y caña', 'Vista general', 'Techo de madera y caña')}
      {vfig('once-once-barra-lateral', 'Lateral de la barra de concreto de Once Once con luz indirecta y lámpara tejida', 'Lateral', 'Luz indirecta y lámparas tejidas')}
    </div>
    <p class="gal-note">Fotografías del proyecto construido.</p>
  </div>
</section>

<!-- ============================================================
     FICHA
     ============================================================ -->
<section class="section on-light" id="ficha">
  <div class="wrap">
    <span class="mono sec-label">Ficha técnica</span>
    <dl class="spec" style="border-color:var(--line-light)">
      {ficha([('Proyecto', 'Once Once'), ('Tipología', 'Restaurante · Barra'), ('Tipo de intervención', 'Remodelación interior'),
              (f'Alcance de {BRAND}', 'Diseño, ejecución y mobiliario'), ('Año', '2024'), ('Estado', 'Construido')])}
    </dl>
    <div class="cta-row">
      <a href="index.html?tipo=remodelaci%C3%B3n#contacto" class="btn btn-dark">Cotiza tu remodelación →</a>
      <a href="index.html#proyectos" class="link">Ver todos los proyectos</a>
    </div>
  </div>
</section>
</main>
""" + footer('index.html') + BASE_JS.replace('%EXTRA%', '')
OPAGE = OPAGE.replace('</style>', W_CSS + PAGE_A_CSS + TALL_CSS + '</style>', 1)
open('once-once.html', 'w', encoding='utf-8').write(OPAGE)
