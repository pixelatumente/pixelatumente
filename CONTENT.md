# CONTENT.md — Inventario de Contenido

## Contenido Existente Verificado

### pixelatumente.es (actual one-page)

| Sección | Estado | Acción |
|---------|--------|--------|
| Hero: "No vengo de una escuela de programación" | ✅ Verificado | **MEJORAR** — refinar para web profesional sin perder autenticidad |
| "Aprendo, pruebo y publico" | ✅ Verificado | **MANTENER** — esencia de la marca |
| "Lo que hago suele vivir entre estas zonas" (5 items) | ✅ Verificado | **MEJORAR** — alinear con oferta profesional |
| Proyecto destacado: NutriCare | ✅ Verificado | **MANTENER** — caso real funcionando |
| Archivo de proyectos (7 cards) | ✅ Verificado | **MANTENER** pero **REESCRIBIR** descripciones |
| "Mi forma de trabajar es bastante simple" (5 pasos) | ✅ Verificado | **MANTENER** — diferencial auténtico |
| "Ahora mismo estoy explorando esto" (5 áreas) | ✅ Verificado | **REESCRIBIR** — actualizar a intereses 2026 |
| FAQ (3 preguntas) | ✅ Verificado | **MEJORAR** — añadir preguntas sobre servicios |
| CTA final | ✅ Verificado | **MEJORAR** — clarificar qué acción quiere el usuario |
| Footer: Pixelatumente + nav + Barcelona/online | ✅ Verificado | **MANTENER** |
| Toggle dark mode | ✅ Verificado | **ELIMINAR** (light mode solo en v2) |
| Email: contacto@pixelatumente.es | ✅ Verificado | **CONFIRMAR** ¿sigue activo? |

### pixelatumente.com (WordPress blog)

#### Páginas Fijas

| Página | Estado | Acción |
|--------|--------|--------|
| Inicio (Home) | ✅ Verificado | **REESCRIBIR** — title tag "Inicio" es muy pobre para SEO |
| Blog (listado) | ✅ Verificado | **MANTENER** estructura, rediseñar visual |
| Portafolio (contenido de diseño 2019) | ✅ Verificado | **REESCRIBIR** — contenido desactualizado (2019), reemplazar con proyectos reales |
| Contacto | ✅ Verificado | **MEJORAR** — formulario funcional; actualizar mensaje ("no ofrezco servicios" → nueva propuesta) |
| Aviso Legal | ✅ Verificado | **MANTENER** — actualizar datos contacto |
| Política de Privacidad | ⚠️ No verificada | **CONFIRMAR** — existe pero no se ha extraído el contenido |
| Política de Cookies | ✅ Verificado | **REESCRIBIR** — adaptar a cookies mínimas (sin terceros innecesarios) |

#### Blog — Categorías y Posts

| Categoría | Posts | Prioridad Migración |
|-----------|-------|-------------------|
| SEO | 16+ | **ALTA** — contenido principal |
| CopyWriting | 16+ | **ALTA** — contenido principal |
| Inteligencia Artificial | 10+ | **ALTA** — tendencia y expertise |
| Marketing Online | 14+ | **MEDIA** |
| Hosting & Internet | 15+ | **MEDIA** |
| Diseño Gráfico | 12+ | **BAJA** — contenido más antiguo |
| Google | 16+ | **ALTA** |
| Diseño Web | 5+ | **MEDIA** |
| Google Analytics | 3+ | **MEDIA** |
| Comercio Electrónico | 4+ | **MEDIA** |

**Total estimado:** 100+ posts

#### Posts Recientes Verificados

| Post | Fecha | Acción |
|------|-------|--------|
| ¿Qué es DataForSEO? | 2025-10 | **MANTENER** — contenido evergreen actualizado |
| Broken Link Checker | 2025-10 | **MANTENER** |
| Menciones de Marca en IA | 2025-10 | **MANTENER** — GEO trending |
| Guía Local LLM | Reciente | **MANTENER** |
| Google AI Overviews | Reciente | **MANTENER** |
| SGE / Experiencia Generativa | Reciente | **MANTENER** |
| Comparativa herramientas escritura IA | Jun 2025 | **MEJORAR** — actualizar precios/fecha |
| Plugins Analítica WordPress | 2025-04 | **MANTENER** |
| Adiós Spam WordPress | 2025-03 | **MANTENER** |
| Alternativas Screaming Frog | 2025-02 | **MANTENER** |
| Linkbuilding 2025 | 2025-02 | **MEJORAR** — actualizar datos |
| Agencia SEO Madrid | 2024-04 | **CONFIRMAR** ¿sigue relevante? |
| SEO para Pymes | 2022-11 | **REESCRIBIR** — contenido antiguo |
| Reseña Hetzner VPS | 2022-06 | **MANTENER** |
| Hosting WordPress | 2021-07 | **MEJORAR** — actualizar |
| Mr. Tools | 2021-02 | **ELIMINAR** — contenido muy antiguo |
| Comprar Likes Instagram | 2021-10 | **ELIMINAR** — práctica cuestionable |

#### Productos/Servicios Mencionados

| Herramienta | Tipo | Migrar |
|-------------|------|--------|
| SEOWRITING | Afiliado | **CONFIRMAR** — ¿sigue activo el programa? |
| KoalaWriter | Afiliado | **CONFIRMAR** — ¿sigue activo el programa? |
| DataForSEO | Review/Guía | **MANTENER** |
| Ahrefs | Review/Mención | **MANTENER** |
| Jasper, Copy.ai, Writesonic | Comparativa | **MANTENER** |

## Contenido que FALTA

| Pieza | Prioridad | Notas |
|-------|-----------|-------|
| Página "Sobre mí" detallada | 🔴 Alta | Reemplazar la one-page del .es con biografía profesional |
| Página "Servicios" | 🔴 Alta | Definir qué ofrece Daniel actualmente |
| Casos de estudio | 🟡 Media | Proyectos reales con métricas |
| Testimonios | 🟡 Media | Si existen de clientes reales |
| Página "Herramientas" | 🟢 Baja | Catálogo de sus herramientas y proyectos |
| Timeline profesional | 🟢 Baja | Línea temporal de su trayectoria (20 años diseño + 12 SEO) |

## Plan de Migración de Contenido

| Fase | Contenido | Método |
|------|-----------|--------|
| 1 | Home + Sobre Mí + Contacto + Legales | Redacción nueva en Astro |
| 2 | Posts recientes (2024-2025) ~30 | Export WP REST API → Markdown |
| 3 | Posts antiguos con valor ~30 | Export → Revisar → Markdown |
| 4 | Posts de baja calidad/antiguos ~40 | Dejar fuera temporalmente; decidir si migrar |
| 5 | Portfolio + Proyectos | Redacción nueva |

## Tono y Voz

| Aspecto | Directriz |
|---------|-----------|
| **Tono** | Directo, honesto, sin jerga corporate. "No vengo de una escuela..." |
| **Voz** | Primera persona, Daniel habla desde la experiencia real |
| **Longitud artículos** | 1200+ palabras, datos concretos, tablas, fuentes |
| **Formato** | Títulos informativos (no "Conclusión"), contenido escaneable |
| **Imágenes** | Fotos reales > IA cuando hay sujeto fotografiable |
| **CTAs** | Proponer opciones antes de aplicar en copy importante |

## PENDIENTE — CONFIRMAR

- [ ] **Exportación de WP:** ¿Acceso a WP admin / REST API para extraer todos los posts?
- [ ] **Comentarios de blog:** ¿Migrar, mantener desactivados, o eliminarlos?
- [ ] **Imágenes del blog:** ¿Migrar las existentes o regenerar? (Muchas son AI-generated)
- [ ] **Enlaces de afiliado:** ¿Actualizar IDs, eliminar programas caducados?
- [ ] **Contenido de "no ofrezco servicios":** ¿Cuál es la posición actual de Daniel? ¿Ofrece consultoría o no?
- [ ] **Posts con fecha 2018-2021:** ¿Actualizar fechas o mantener como históricos?
- [ ] **Imágenes del portfolio (2019):** ¿Se migran o se reemplazan con proyectos recientes?