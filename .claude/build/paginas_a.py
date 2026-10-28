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

svc_html = '\n'.join(
    f'      <article class="svc"><span class="mono n">{i + 1:02d}</span><h3>{n}</h3><p>{t}</p></article>'
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
      <p class="sec-lead">Gastronomía y comercio a nivel de calle. Cada ficha indica el estado real del proyecto.</p>
    </div>
    <div class="work">
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
