# ARCHITECTURE.md — Arquitectura Técnica

## Stack

| Capa | Tecnología | Razón |
|------|-----------|-------|
| **Framework** | Astro 5+ | Estático + islas de JS; perfecto para contenido SEO |
| **Lenguaje** | TypeScript | Tipado seguro, mejor DX |
| **CSS** | Tailwind CSS v4 | Utilidades rápidas, sin bloat |
| **Hosting** | Cloudflare Pages | CDN global, builds automáticos, sin servidor |
| **Búsqueda** | Pagefind | Índice estático cliente, sin backend |
| **Formulario** | Cloudflare Workers | Serverless, sin coste en low traffic |
| **Analytics** | Google Analytics 4 (GA4) | Ya existente |
| **AdSense** | Integración manual | Sin plugin, control total |

**NO se usa:** React, Vue, Svelte, Next.js, Nuxt, WordPress, PHP, bases de datos.

## Estructura de Carpetas

```
pixelatumente-2/
├── public/
│   ├── favicon.ico
│   ├── favicon.svg
│   ├── apple-touch-icon.png
│   ├── og-default.png
│   ├── robots.txt
│   └── _redirects          # 301s de WP legacy
│
├── src/
│   ├── layouts/
│   │   ├── BaseLayout.astro      # Layout global: meta, header, footer
│   │   └── BlogLayout.astro      # Layout para posts del blog
│   │
│   ├── pages/
│   │   ├── index.astro           # Home profesional (unifica .es + .com)
│   │   ├── blog/
│   │   │   ├── index.astro       # Listado de posts con paginación
│   │   │   └── [slug].astro      # Post individual (dinámico vía getStaticPaths)
│   │   ├── portfolio/
│   │   │   └── index.astro       # Portafolio de proyectos y trabajos
│   │   ├── proyectos/
│   │   │   └── index.astro       # Archivo de proyectos (como el .es actual)
│   │   ├── contacto.astro        # Página de contacto con formulario
│   │   ├── aviso-legal.astro
│   │   ├── politica-de-privacidad.astro
│   │   ├── politica-de-cookies.astro
│   │   └── rss.xml.ts            # Feed RSS generado desde contenido
│   │
│   ├── components/
│   │   ├── Header.astro          # Nav superior
│   │   ├── Footer.astro          # Footer unificado
│   │   ├── Hero.astro            # Hero section de la home
│   │   ├── ProjectCard.astro     # Card de proyecto
│   │   ├── BlogCard.astro        # Card de post del blog
│   │   ├── ContactForm.astro     # Formulario de contacto
│   │   ├── CookieBanner.astro    # Banner de cookies (light, no invasivo)
│   │   ├── Breadcrumbs.astro     # Migas de pan
│   │   ├── SEOHead.astro         # Meta tags, OG, schema
│   │   └── AdUnit.astro          # Componente AdSense no intrusivo
│   │
│   ├── content/
│   │   └── blog/                 # Posts del blog en markdown/MDX
│   │       ├── post-1.md
│   │       └── ...
│   │
│   ├── data/
│   │   ├── projects.json         # Proyectos del portafolio (de .es actual)
│   │   ├── navigation.json       # Config de navegación
│   │   └── site.json             # Metadatos globales del sitio
│   │
│   ├── styles/
│   │   └── global.css            # Tailwind v4 @theme + clases base
│   │
│   └── scripts/
│       └── cookie-consent.js     # JS mínimo para consentimiento de cookies
│
├── functions/                    # Cloudflare Functions (si se necesitan)
│   └── contact-form.js           # Worker para envío de formulario
│
├── astro.config.mjs
├── tailwind.config.mjs           # @theme tokens de color y fuente
├── tsconfig.json
├── package.json
├── DESIGN.md                     # Tokens de diseño (copiado a raíz)
├── .impeccable/
│   └── config.json               # Config para detector impeccable
└── wrangler.toml                 # Config de Cloudflare Pages (opcional)
```

## Routing

| Ruta | Página | Tipo |
|------|--------|------|
| `/` | Home profesional | Estática |
| `/blog/` | Listado de posts | Estática (paginada) |
| `/blog/[slug]/` | Post individual | Estática (getStaticPaths) |
| `/portfolio/` | Portafolio | Estática |
| `/portfolio/[slug]/` | Trabajo individual | Estática (opcional) |
| `/proyectos/` | Archivo de proyectos | Estática |
| `/contacto/` | Contacto | Estática + Worker |
| `/aviso-legal/` | Legal | Estática |
| `/politica-de-privacidad/` | Legal | Estática |
| `/politica-de-cookies/` | Legal | Estática |
| `/rss.xml` | Feed RSS | Generado dinámicamente |
| `/sitemap.xml` | Sitemap | Generado dinámicamente |

**Redirects (preservar rankings WP legacy):**
- `/category/seo/*` → `/blog/` (o tags si se implementan)
- `/category/hosting-internet/*` → `/blog/`
- `/author/pixelatumente/*` → `/blog/`
- `/page/*` → `/blog/` (paginación WP)

## Estrategia SEO

| Elemento | Implementación |
|----------|---------------|
| **Sitemap** | Generado automáticamente por Astro |
| **RSS** | Feed XML completo |
| **Schema** | JSON-LD: Person, WebSite, Article, BreadcrumbList |
| **Open Graph** | og:title, og:description, og:image, og:url |
| **Twitter Cards** | summary_large_image |
| **Canonical** | Cada página tiene su URL canónica |
| **Meta descripción** | Por página/post, con fallback global |
| **Breadcrumbs** | Schema + visual |
| **URLs limpias** | Sin parámetros, slugs semánticos |
| **Pagefind** | Búsqueda indexada estática |

## Estrategia de Despliegue (Cloudflare Pages)

1. **Build:** `astro build` genera `dist/`
2. **Deploy:** `wrangler pages deploy dist --project-name pixelatumente`
3. **Dominio:** pixelatumente.es (apex) + pixelatumente.com (redirect)
4. **Redirects:** `_redirects` para rutas WP legacy
5. **Headers:** Cache control para assets estáticos
6. **SSL:** Automático (Cloudflare)

## PENDIENTE — CONFIRMAR

- [ ] **Worker de formulario:** ¿Email vía SendGrid, Resend, o solo mailto?
- [ ] **Contenido heredado del WP:** ¿Exportar vía REST API o volcar a mano?
- [ ] **Comentarios de blog:** ¿Se heredan del WP? ¿Se mantienen? (Actualmente tienen reCAPTCHA)
- [ ] **Paginación del blog:** ¿Cuántos posts por página?
- [ ] **Tags vs solo categorías:** ¿Mantener la taxonomía actual o simplificar?
- [ ] **Búsqueda Pagefind:** ¿Indexar todo el sitio o solo el blog?
- [ ] **Redirección .com → .es:** ¿Path exacto o a home?
- [ ] **Frecuencia de build/deploy:** ¿Manual con wrangler o GitHub Actions automático?