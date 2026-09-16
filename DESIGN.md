# DESIGN.md — Dirección Visual

## Estado Actual

### pixelatumente.es

**Diseño existente (one-page):**
- **Paleta:** arena #F3F0E8 (bg), surface #F8F4EC, ink #111111, muted #555555
- **Acento:** #FF5A36 (naranja-rojizo)
- **Acento alt:** #01696F (verde-azulado)
- **Tipografía:** IBM Plex Sans (display), IBM Plex Mono (cuerpo)
- **Estilo:** Brutalista suave — bordes 2px negros, sin sombras, sin radios
- **Dark mode:** Sí, con toggle ☀/☾
- **Tono visual:** Experimental, honesto, "sin acabado perfecto" como parte de la personalidad

### pixelatumente.com

**Diseño existente (WordPress Kadence):**
- **Paleta:** Kadence default (blanco, grises, azul claro como acento #3182CE)
- **Tipografía:** Plus Jakarta Sans (display), Rubik (body), Work Sans
- **Estilo:** Blog corporativo estándar WP, con cards, sombras suaves (#00000070), bordes redondeados
- **No dark mode**
- **Tono visual:** Profesional pero genérico — no hay conexión visual con el .es

## Problemas Detectados

| Problema | Impacto |
|----------|---------|
| Dos identidades visuales distintas | Confusión de marca |
| .es es más auténtico pero menos profesional | No transmite servicios |
| .com es más profesional pero genérico (como cualquier WP) | Sin personalidad |
| .com usa azul como acento — contradictorio con la paleta mediterránea | Inconsistencia de marca |
| .es usa naranja #FF5A36 como acento — no es la terracota definida en DESIGN.md | Deriva cromática |

## Propuesta de Unificación

**Dirección:** Mantener la esencia mediterránea-minimalista del .es, refinándola para un contexto profesional sin perder la personalidad.

### Paleta Unificada (basada en el sistema existente en DESIGN.md)

| Rol | Hex | Uso |
|-----|-----|-----|
| Fondo página | `#f3f0e8` | arena — base cálida |
| Superficie (cards) | `#ffffff` | blanco sobre arena |
| Texto principal | `#1a1a2e` | carbon — contraste alto |
| Texto secundario | `#6b6b6b` | piedra — labels, metadatos |
| **Acento único** | **`#b8422e`** | **terracota — el ÚNICO acento** |
| Acento hover | `#d47a6a` | terracota claro |
| Líneas/dividers | `#e0ddd5` | velo — separación sutil |

**Cambios respecto al actual:**
- ❌ Eliminar #FF5A36 (naranja) del .es
- ❌ Eliminar #3182CE (azul) del .com
- ❌ Eliminar #01696F (verde) del .es
- ✅ Terracota #b8422e como ÚNICO acento en toda la web

### Tipografía

| Rol | Fuente | Peso |
|-----|--------|------|
| Display (H1-H2) | IBM Plex Mono | 700 (bold) |
| Labels, nav, badges | IBM Plex Mono | 600, 0.8rem, uppercase |
| Cuerpo | system-ui | 400, 1.125rem |
| Small | system-ui | 400, 0.875rem |

**Reglas:**
- IBM Plex Mono se puede auto-hospedar (npm o descarga)
- system-ui evita Google Fonts → mejor PageSpeed
- Sin Inter, sin Plus Jakarta Sans, sin Rubik, sin Work Sans (nuevas cargas)
- Todo uppercase + tracking para nav y metadatos

### Layout y Componentes

| Elemento | Especificación |
|----------|---------------|
| **Header** | Sticky, bg arena, logo texto + nav uppercase, sin imágenes |
| **Nav** | Máximo 6 items: Inicio, Blog, Portfolio, Contacto |
| **Cards** | Blanco sobre arena, sin bordes, sin sombras, border-radius 8px |
| **Botones** | Terracota bg, white text, uppercase mono, 8px radius |
| **Enlaces** | Terracota siempre (nunca azul), subrayado en hover |
| **Tablas** | Solo bottom-border con velo, th uppercase mono |
| **Footer** | Minimal, 3 columnas: marca, nav, ubicación |
| **Breadcrumbs** | Mono uppercase, separador `/`, terracota activo |

### Hero (Home)

**Propuesta (3 opciones):**

1. **Tipográfico puro** — H1 grande en mono, texto descriptivo, 2 CTAs. Sin imagen. (Estilo .es actual refinado)
2. **Con foto personal** — Foto de Daniel (real, no IA) + texto. Aporta cercanía y profesionalidad.
3. **Con captura de proyecto** — Mockup de NutriCare o Endiza como testimonio visual de "lo que construyo"

**Recomendación:** Opción 1 para lanzamiento, opción 2 si hay foto disponible.

### Paleta Temática (para secciones editoriales)

Para el blog y contenido editorial, se permite una paleta extendida:
- **--color-oro:** `#c9a84c` (acento secundario para fechas, badges)
- **--color-noche:** `#1a1a3e` (para fondos de citas o stats)

### Forbidden Patterns

- ❌ Sombras (`box-shadow`, `drop-shadow`)
- ❌ Bordes en cards
- ❌ Modo oscuro (solo light mode)
- ❌ Fondos oscuros
- ❌ Degradados
- ❌ Ocre/gold como acento principal
- ❌ Font descargada = Inter
- ❌ Iconos decorativos
- ❌ Texto sobre fondos de color
- ❌ Imágenes a ancho completo en contenido del blog (max-w-md)

### Imágenes

| Tipo | Directriz |
|------|-----------|
| **Artículos blog** | 600×400, centradas, max-w-lg en hero de artículo, max-w-md en cuerpo |
| **Miniaturas blog** | 96-112px cuadradas, sin marcos pesados |
| **Portfolio** | Capturas reales de proyectos, no mockups genéricos |
| **Illustraciones conceptuales** | IA generativa permitida (es parte de la identidad) |
| **Fotos reales** | Preferidas para sujetos fotografiable (barcelona, setup de trabajo) |

## Relación con Sistema Existente

Este diseño es una **evolución refinada** del skill `pixelatumente-design` (el sistema plano claro con terracota). Se adapta a la naturaleza híbrida de Pixelatumente: un sitio que es a la vez portfolio personal, blog profesional y herramienta de marketing.

## Verificación

```bash
cp ~/DESIGN.md ./DESIGN.md
npx impeccable detect src/
```

Ver skill `pixelatumente-design` para detalles de findings esperados y fixes.

## PENDIENTE — CONFIRMAR

- [ ] **Foto personal:** ¿Daniel tiene una foto profesional actual que pueda usar?
- [ ] **Logo:** ¿Prefiere el nombre en texto (como ahora) o un logotipo gráfico?
- [ ] **Estilo de portafolio:** ¿Capturas de pantalla de proyectos reales o solo enlaces?
- [ ] **Favicon:** ¿Diseñar uno nuevo o mantener el existente?