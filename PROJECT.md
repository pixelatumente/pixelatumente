# PROJECT.md — Pixelatumente 2.0 (decisión 2026-09-04)

## Descripción del Proyecto

Rediseño de **pixelatumente.es** unificando el portfolio/proyectos actual con una sección de blog migrada desde pixelatumente.com. Dominio principal: `.es`. `.com` se mantendrá vivo de momento sin redirección forzada.

## Estado actual

| Aspecto | pixelatumente.es | pixelatumente.com |
|---------|------------------|-------------------|
| Propósito | Portfolio personal / laboratorio | Blog profesional SEO + Copy + IA |
| Stack | HTML+CSS+JS estático (one-page) | WordPress + Kadence + plugins |
| Diseño | Brutalista suave, arena+terracota, mono, oscuro | WP genérico, azul, sin personalidad |
| Contenido | Proyectos + published apps | ~120 posts SEO (+afiliados, AdSense) |

## Decisiones adoptadas (2026-09-04)

1. **Dominio principal:** `.es` — el diseño actual es el que nos gusta, lo conservamos como base.
2. **Oferta de servicios:** No ofrezco servicios de momento. Publico lo que hago y eso es la propuesta.
3. **Migración de blog:** Migraremos los posts con mejor rendimiento en GSC (top 8 por impresiones), en orden de prioridad. El resto queda en el .com por ahora.
4. **Home del .es:** Se añade sección de blog integrada (últimos posts + enlace a `/blog/`).
5. **Redirección .com:** No ahora. El .com sigue vivo con su contenido mientras migramos. Se evaluará redirección 301 cuando la migración esté completa.

## Objetivos

1. **Extender el diseño actual del .es** añadiendo estructura de blog sin perder la identidad visual.
2. **Migración incremental:** posts prioritarios primero, evaluar resultado.
3. **Contenido unificado:** blog del .com vive ahora en `/blog/` dentro del .es, mismo diseño.
4. **SEO preservado:** cada post migrado conserva su URL canónica con redirect 301 desde el .com al .es correspondiente.
5. **Rendimiento:** Astro + Cloudflare Pages, sin bloat WP.

## Público Objetivo

- SEOs y marketers hispanohablantes buscando contenido práctico y herramientas.
- Solopreneurs y desarrolladores que siguen el proceso de "aprender-haciendo".
- Lectores del blog actual del .com que encuentran ahora el contenido en la web unificada.

## Propuesta de Valor (actual)

> **Aprendo, pruebo y publico.** Pixelatumente es el registro de lo que construyo, lo que pruebo y lo que voy entendiendo. Apps, automatizaciones, herramientas SEO, experimentos con IA — todo publicado en abierto, sin filtrar por vitrina.

## Funcionalidades (MVP 2026-09)

1. **Home del .es** — manteniendo el diseño actual + nueva sección de blog (3-4 posts + enlace "Ver todo el blog")
2. **Blog en Astro** — `/blog/` con listado paginado + `/blog/[slug]/` individual
3. **Migración de posts top:** 8 posts de GSC con redirect 301 desde .com
4. **SEO básico:** sitemap, meta tags, OG, schema Article para posts
5. **Paginación blog:** primer versión (≤10 posts por página)
6. **Analytics:** GA4 (conservar si ya configurado en .es)

## Requisitos Técnicos

- Framework: Astro 6+ / TypeScript / Tailwind CSS v4
- Hosting: Cloudflare Pages (wrangler pages deploy)
- Búsqueda: Pagefind (si hace falta)
- Contenido: Markdown en `src/content/blog/` con frontmatter
- Fuentes: IBM Plex Mono (display) + system-ui (body) — igual que diseño actual
- Sin React, sin Node en runtime, sin PHP

## Posts a migrar (priorizados por GSC 365 días)

| Prioridad | Post WP | URL .com | Motivo |
|-----------|---------|----------|--------|
| 1 | DataForSEO | `/dataforseo/` | 707 impresiones, núcleo SEO |
| 2 | Prospectos Farmacéuticos | `/prospectos-farmaceuticos/` | 6 clicks (más que ninguno) |
| 3 | Dominios Gratis | `/dominios-gratis/` | 552 impresiones |
| 4 | Herramientas para arreglar enlaces rotos | `/herramientas-para-arreglar-enlaces-rotos/` | 302 imp, CTR 1.32% |
| 5 | Broken Link Checker | `/broken-link-checker-arregla-enlaces-rotos/` | 621 imp, pos 80 — optimizar |
| 6 | LLM Local | `/local-llm/` | 1272 imp, tema alineado |
| 7 | Marketing para Emprendedores | `/marketing-para-emprendedores/` | 663 imp |
| 8 | Eliminar Reseñas Google | `/eliminar-resenas-google/` | 1787 imp — mégapotential |

## Pendiente / CONFIRMAR en futuras fases

- [ ] ¿Redirección definitiva .com → .es (301 preserving paths)?
- [ ] ¿Posts restantes del .com (80+)? Migrar en fases o archivar?
- [ ] ¿AdSense/afiliados en el .es? (decisión a medio plazo)
- [ ] ¿Dark mode en el nuevo Astro? (el .es actual lo tiene, hay que decidir si se mantiene)
- [ ] ¿Foto personal para el blog?
