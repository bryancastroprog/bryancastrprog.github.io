---
name: seo-local-contenido
description: Estrategia de SEO local para Guatemala y arquitectura de contenido de bcarqstudio.com. Usar cuando se planifiquen páginas nuevas, se elijan palabras clave, se defina la estructura de URLs o el enlazado interno, se trabaje Google Business Profile, NAP, datos de ubicación por zona, o se decida qué contenido crear para captar clientes de arquitectura, prefactibilidad, desarrollo inmobiliario o inversionistas.
---

# SEO local y arquitectura de contenido — BC Arquitectura

Objetivo de negocio: que el sitio genere **consultas calificadas** de tres audiencias:
1. **Empresas** que necesitan diseñar un espacio (oficinas, clínicas, retail, restaurantes).
2. **Propietarios de terreno y desarrolladores** que necesitan prefactibilidad, diseño o socio de co-desarrollo.
3. **Inversionistas** interesados en proyectos propios (ONA).

Cada página debe servir a **una** audiencia y a **una** intención de búsqueda principal.

## 1. Mapa de palabras clave (punto de partida — validar con Search Console/Keyword Planner)

| Cluster | Keyword principal | Secundarias | Página destino |
|---|---|---|---|
| Prefactibilidad | estudio de prefactibilidad inmobiliaria Guatemala | análisis de terreno, cabida de terreno, potencial constructivo, factibilidad de proyecto inmobiliario | `/servicios/prefactibilidad-inmobiliaria/` |
| Desarrollo | arquitectos para desarrollo inmobiliario Guatemala | diseño de edificios de apartamentos, anteproyecto, co-desarrollo | `/servicios/desarrollo-inmobiliario/` |
| Arquitectura | estudio de arquitectura Guatemala | arquitectos en Ciudad de Guatemala, diseño arquitectónico | `/` y `/servicios/diseno-arquitectonico/` |
| Comercial | diseño de oficinas Guatemala | diseño de clínicas, diseño de locales comerciales, diseño de restaurantes | `/servicios/diseno-comercial/` (+ subpáginas si hay volumen) |
| Normativa (contenido) | POT Guatemala zonas / licencia de construcción Municipalidad de Guatemala | índice de edificabilidad, requisitos de licencia | `/recursos/…` |
| Inversión | invertir en desarrollo inmobiliario Guatemala | preventa zona 15, proyectos residenciales | `/inversionistas/` |

Reglas: no asignar la misma keyword principal a dos URLs (canibalización). Incluir la zona (Zona 10, 14, 15, 16, Carretera a El Salvador) solo cuando el contenido sea realmente específico de esa zona.

## 2. Arquitectura de URLs objetivo

```
/                                   Home: propuesta de valor + 3 rutas por audiencia
/servicios/                         Índice de servicios
/servicios/prefactibilidad-inmobiliaria/
/servicios/desarrollo-inmobiliario/ (diseño para desarrolladores + co-desarrollo)
/servicios/diseno-arquitectonico/
/servicios/diseno-comercial/        (actual diseno-estrategico.html)
/proyectos/                         Portafolio filtrable por tipología
/proyectos/<slug>/                  Un proyecto por URL
/inversionistas/                    ONA + lista de interés + aviso legal
/estudio/                           Bryan Castro, credenciales verificables, método
/recursos/<slug>/                   Guías que responden preguntas reales de clientes
/contacto/                          Formulario calificado + agenda + WhatsApp
```
Las URLs actuales (`*.html`) se conservan como puentes (ver skill `seo-tecnico` §3).

## 3. Enlazado interno

- Home → las 3 rutas de audiencia y los 3 proyectos más fuertes.
- Cada servicio → 2–3 proyectos relacionados + CTA a contacto con el tipo de proyecto preseleccionado (`/contacto/?tipo=prefactibilidad`).
- Cada proyecto → su servicio + 2 proyectos de la misma tipología.
- Cada recurso → el servicio que resuelve el problema.
- Texto ancla descriptivo ("estudio de prefactibilidad"), nunca "clic aquí".

## 4. SEO local fuera del sitio (mayor impacto en búsquedas "cerca de mí")

1. **Google Business Profile** como "Estudio de arquitectura", con la misma razón social, dirección/área de servicio, teléfono y web que el sitio (NAP idéntico).
2. Categorías secundarias: "Arquitecto", "Diseñador de interiores", "Consultor inmobiliario" (solo las que apliquen).
3. Fotos reales de proyectos y del equipo; publicar cada proyecto nuevo también en el perfil.
4. Pedir reseñas a clientes reales tras cada entrega (nunca reseñas inventadas o compradas).
5. Directorios con NAP consistente: Colegio de Arquitectos de Guatemala (si aplica), LinkedIn Company Page, Instagram, Houzz/ArchDaily solo con proyectos reales.

## 5. NAP y marca

Un solo nombre comercial en todo el sitio, JSON-LD y perfiles. Hoy conviven "BC Arquitectura", "BC Arq Studio", "BC Studio" y "Build & Create Studio": **pedir al cliente que defina el nombre oficial antes de implementar**.

## 6. Plan de contenido

Prioriza por: (1) intención comercial alta, (2) capacidad de demostrar experiencia real, (3) volumen.
Cada pieza debe basarse en conocimiento del estudio o fuentes citables (Municipalidad de Guatemala, POT, normativa vigente). No publicar cifras de costos, plazos o rentabilidades sin fuente o sin validación del cliente; usar rangos solo si el cliente los aporta.

## 7. Entregable

Para cada página propuesta: URL · audiencia · keyword principal y secundarias · intención (informativa/comercial/transaccional) · H1 propuesto · secciones · CTA · enlaces internos entrantes y salientes · contenido que el cliente debe aportar.
