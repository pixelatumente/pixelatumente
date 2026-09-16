# TASKS.md — Roadmap de Implementación

## Leyenda

- 🔴 **Fase 0: Confirmación** — Decisiones previas a cualquier código
- 🟠 **Fase 1: Fundación** — Scaffold, diseño, arquitectura
- 🟡 **Fase 2: Contenido** — Migración y redacción
- 🟢 **Fase 3: Features** — Funcionalidades completas
- 🔵 **Fase 4: SEO y Pulido** — Antes del lanzamiento
- 🟣 **Fase 5: Lanzamiento** — Deploy y post-lanzamiento

---

## 🔴 FASE 0 — Confirmación (Tú decides, yo ejecuto)

### Decisiones Estratégicas

- [ ] **0.1 — Dominio canónico:** ¿.es como principal y .com redirige, o al revés? ¿O comprar dominio nuevo?
- [ ] **0.2 — Oferta de servicios:** ¿Daniel ofrece consultoría SEO/copy/desarrollo? ¿Precios? ¿O sigue siendo "no ofrezco servicios"?
- [ ] **0.3 — Monetización:** ¿AdSense solo? ¿Afiliados? ¿Consultoría? ¿Productos digitales?
- [ ] **0.4 — Foto personal:** ¿Tiene Daniel foto profesional para el hero? ¿Quiere usarla?
- [ ] **0.5 — Logo:** ¿Texto (actual) o logotipo gráfico?
- [ ] **0.6 — Contenido heredado:** ¿Qué hacer con posts 2018-2021? ¿Migrar todo, seleccionar, archivar?

### Decisiones Técnicas

- [ ] **0.7 — Migración de posts:** ¿Exportar WP REST API a JSON → Markdown script? ¿O volcado manual de los mejores?
- [ ] **0.8 — Formulario de contacto:** ¿Email vía Worker (Resend/SendGrid) o solo mailto?
- [ ] **0.9 — Comentarios del blog:** ¿Migrar, mantener desactivados, eliminar?
- [ ] **0.10 — Búsqueda:** ¿Pagefind en todo el sitio o solo blog?

---

## 🟠 FASE 1 — Fundación (Scaffolding + Diseño)

### Setup del Proyecto

- [ ] **1.1** Crear proyecto Astro con `create astro` + TypeScript + Tailwind v4
- [ ] **1.2** Configurar `tailwind.config.mjs` con tokens de color y fuente (arena, terracota, carbon, piedra, velo)
- [ ] **1.3** Configurar `tsconfig.json` (paths, strict mode)
- [ ] **1.4** Instalar y configurar dependencias: `@tailwindcss/typography` (para prose del blog)
- [ ] **1.5** Configurar `astro.config.mjs` para deploy en Cloudflare Pages
- [ ] **1.6** Copiar DESIGN.md a raíz del proyecto (para impeccable detect)

### Diseño Visual

- [ ] **1.7** Escribir `global.css` con @theme + clases base (paleta, tipografía, layout)
- [ ] **1.8** Crear `Header.astro` — sticky, logo texto, nav uppercase (≤6 items)
- [ ] **1.9** Crear `Footer.astro` — 3 columnas: marca, nav, ubicación
- [ ] **1.10** Crear `BaseLayout.astro` — Header + Footer + SEOHead + estilos globales
- [ ] **1.11** Crear `SEOHead.astro` — meta tags, OG, Twitter cards, schema JSON-LD

### Página de Home

- [ ] **1.12** Crear `index.astro` con Hero, secciones, proyectos destacados, CTA
- [ ] **1.13** Diseñar Hero (tipográfico, opción 1: sin imagen)
- [ ] **1.14** Sección "Qué hago" (5 áreas: apps, automatización, landings, IA, ideas)
- [ ] **1.15** Sección "Proyectos destacados" (3-4 proyectos con cards)
- [ ] **1.16** Sección "Últimos del blog" (3-4 posts en cards)
- [ ] **1.17** CTA final (a blog, portfolio o contacto)

### Diseño Responsive

- [ ] **1.18** Verificar layout en móvil (360px)
- [ ] **1.19** Configurar menú hamburguesa para mobile (<768px)
- [ ] **1.20** Verificar tipografía responsive (clamp en H1-H2)

### Verificación

- [ ] **1.21** Capturar screenshots con Chromium headless (escritorio + móvil)
- [ ] **1.22** Revisar visualmente con `vision_analyze`
- [ ] **1.23** Ejecutar `npx impeccable detect src/` y documentar findings

---

## 🟡 FASE 2 — Contenido

### Páginas Estáticas

- [ ] **2.1** Crear `about.astro` o sección "Sobre mí" — biografía profesional de Daniel
- [ ] **2.2** Crear `portfolio/index.astro` — proyectos reales (Endiza, NutriCare, herramientas SEO)
- [ ] **2.3** Crear `proyectos/index.astro` — archivo vivo tipo .es actual
- [ ] **2.4** Crear `contacto.astro` — formulario + info de contacto
- [ ] **2.5** Crear `aviso-legal.astro` — datos actualizados
- [ ] **2.6** Crear `politica-de-privacidad.astro`
- [ ] **2.7** Crear `politica-de-cookies.astro`
- [ ] **2.8** Crear `rss.xml.ts` — feed RSS dinámico

### Migración de Blog

- [ ] **2.9** Script de exportación WP REST API → archivos Markdown con frontmatter
- [ ] **2.10** Migrar posts recientes (2024-2025) ~30 posts — prioridad ALTA
- [ ] **2.11** Migrar posts de valor medio (2022-2023) ~30 posts — prioridad MEDIA
- [ ] **2.12** Revisar y actualizar posts antiguos seleccionados — prioridad BAJA
- [ ] **2.13** Migrar imágenes del blog a `public/images/` o cloud storage
- [ ] **2.14** Configurar la página `/blog/index.astro` — listado con paginación
- [ ] **2.15** Configurar `/blog/[slug].astro` — post individual con schema Article
- [ ] **2.16** Configurar `BlogLayout.astro` — breadcrumbs, metadatos, sidebar opcional
- [ ] **2.17** Verificar canonical tags en todos los posts

### Portfolio

- [ ] **2.18** Crear `data/projects.json` con proyectos reales (6+ entries)
- [ ] **2.19** Reemplazar contenido del portfolio de 2019 con proyectos actuales
- [ ] **2.20** Añadir capturas de pantalla reales de cada proyecto

---

## 🟢 FASE 3 — Features

### Búsqueda

- [ ] **3.1** Instalar Pagefind
- [ ] **3.2** Integrar Pagefind en el layout (input de búsqueda en header)
- [ ] **3.3** Verificar índice en build (solo blog o sitio completo)

### Formulario de Contacto

- [ ] **3.4** Crear componente `ContactForm.astro` con campos: nombre, email, mensaje
- [ ] **3.5** Crear Worker de Cloudflare para envío (Resend/SendGrid/mailto fallback)
- [ ] **3.6** Añadir validación client-side
- [ ] **3.7** Verificar envío real

### AdSense

- [ ] **3.8** Crear componente `AdUnit.astro` — no intrusivo (solo en posts, no en home)
- [ ] **3.9** Integrar AdSense en `BaseLayout.astro` (código de page-level)
- [ ] **3.10** Verificar display en móvil (no invasivo)

### Cookie Consent

- [ ] **3.11** Crear `CookieBanner.astro` — barra fina, 1 línea, no invasivo
- [ ] **3.12** JS mínimo para consentimiento (funcional + analytics como default)
- [ ] **3.13** No usar librerías third-party (sin Complianz, sin Cookiebot)

### SEO Técnico

- [ ] **3.14** Generar `sitemap.xml` vía Astro
- [ ] **3.15** Configurar `robots.txt`
- [ ] **3.16** Configurar `_redirects` para 301 de WP legacy
- [ ] **3.17** Schema JSON-LD: Person (Home), Article (blog), BreadcrumbList
- [ ] **3.18** Open Graph + Twitter Cards en todas las páginas
- [ ] **3.19** Breadcrumbs visuales + schema en blog y páginas

---

## 🔵 FASE 4 — SEO y Pulido Pre-Lanzamiento

### Rendimiento

- [ ] **4.1** Optimizar imágenes (WebP, lazy loading, dimensiones explícitas)
- [ ] **4.2** Fuentes auto-hospedadas o system-ui (cero requests externos)
- [ ] **4.3** Verificar PageSpeed Insights (target 95+)
- [ ] **4.4** Verificar Core Web Vitals
- [ ] **4.5** Minificar HTML/CSS/JS (Astro lo hace por defecto, verificar)

### SEO On-Page

- [ ] **4.6** Revisar title tags de cada página (especialmente la home — no "Inicio")
- [ ] **4.7** Revisar meta descriptions de cada página y post
- [ ] **4.8** Verificar estructura de headings (H1 único por página)
- [ ] **4.9** Verificar enlaces internos (no rotos)
- [ ] **4.10** Verificar canonical tags
- [ ] **4.11** Verificar sitemap en GSC

### SEO de Migración

- [ ] **4.12** Mapear URLs WP antiguas → URLs nuevas en `_redirects`
- [ ] **4.13** Verificar 301 no son 302 ni redirect chains
- [ ] **4.14** Enviar nuevo sitemap a GSC
- [ ] **4.15** Verificar que GSC indexa las URLs nuevas
- [ ] **4.16** Configurar GA4 (mismo ID o nuevo)
- [ ] **4.17** Configurar propiedad GSC para el dominio canónico

### Revisión Final

- [ ] **4.18** Revisión visual completa (escritorio + tablet + móvil)
- [ ] **4.19** Revisión de contenido (ortografía, links, datos)
- [ ] **4.20** Revisión legal (aviso, privacidad, cookies)
- [ ] **4.21** Test de formulario de contacto
- [ ] **4.22** Test de búsqueda Pagefind
- [ ] **4.23** Test de RSS feed
- [ ] **4.24** `npx impeccable detect` final

---

## 🟣 FASE 5 — Lanzamiento

### Deploy

- [ ] **5.1** Configurar Cloudflare Pages (proyecto `pixelatumente`)
- [ ] **5.2** Configurar dominio personalizado en CF Pages
- [ ] **5.3** Desplegar build inicial (`wrangler pages deploy`)
- [ ] **5.4** Configurar redirección pixelatumente.com → pixelatumente.es
- [ ] **5.5** Verificar SSL y HTTPS
- [ ] **5.6** Verificar headers de Cloudflare (cache, security)

### Post-Lanzamiento

- [ ] **5.7** Enviar sitemap a Google Search Console
- [ ] **5.8** Enviar sitemap a Bing Webmaster Tools
- [ ] **5.9** Verificar indexación (site:pixelatumente.es)
- [ ] **5.10** Verificar que GA4 está recibiendo datos
- [ ] **5.11** Verificar que AdSense está activo
- [ ] **5.12** Monitorear 404s primera semana
- [ ] **5.13** Verificar que los redirects WP funcionan correctamente
- [ ] **5.14** Configurar cron semanal/mensual de deploy (si hay contenido nuevo frecuente)

### Automatización de Deploy

- [ ] **5.15** Configurar GitHub Actions para auto-deploy en push a main
- [ ] **5.16** O script de deploy manual (`npm run deploy` → wrangler)

---

## Estimación de Tiempo por Fase

| Fase | Días estimados | Dependencia |
|------|----------------|-------------|
| Fase 0 — Confirmación | 1 (tu decisión) | Ninguna |
| Fase 1 — Fundación | 3-4 | Fase 0 completada |
| Fase 2 — Contenido | 5-7 | Fase 1 completada |
| Fase 3 — Features | 3-4 | Fase 2 completada |
| Fase 4 — Pulido | 2-3 | Fase 3 completada |
| Fase 5 — Lanzamiento | 1-2 | Fase 4 completada |
| **Total** | **15-21 días** | |

## Priorización por Valor

| Elemento | Valor SEO | Esfuerzo | Prioridad |
|----------|-----------|----------|-----------|
| Migrar posts 2024-2025 | 🔴 Alto | Medio | 1 |
| Home + Hero con propuesta clara | 🔴 Alto | Bajo | 2 |
| Redirects WP → Astro | 🔴 Alto | Bajo | 3 |
| Sitemap + Schema | 🔴 Alto | Bajo | 4 |
| Portfolio actualizado | 🟡 Medio | Medio | 5 |
| Búsqueda Pagefind | 🟡 Medio | Bajo | 6 |
| Formulario contacto | 🟡 Medio | Medio | 7 |
| Posts antiguos (2022-2023) | 🟡 Medio | Alto | 8 |
| Diseño mobile perfecto | 🟡 Medio | Medio | 9 |
| AdSense no intrusivo | 🟢 Bajo | Bajo | 10 |
| Cookie Consent | 🟢 Bajo | Bajo | 11 |
| Posts 2018-2021 | 🟢 Bajo | Alto | 12 |