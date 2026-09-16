---
title: "Broken Link Checker: arregla enlaces rotos"
description: "Guía para encontrar y arreglar enlaces rotos en WordPress: por qué son dañinos para tu SEO y qué herramientas usar, gratuitas y profesionales."
date: "2025-10-06"
---

## La Guía Definitiva para Encontrar y Arreglar Enlaces Rotos (Más allá del plugin)

Imagina que le das a un amigo un mapa del tesoro. Se pasa horas siguiéndolo, emocionado, hasta que llega a un punto donde la ruta simplemente… se acaba. Hay un acantilado insalvable donde debería haber un puente. Frustrante, ¿verdad? Pues eso es exactamente lo que un enlace roto le hace a un visitante de tu web y a los robots de Google.

Un enlace roto, o *broken link*, es un hipervínculo que apunta a una página que ya no existe, que ha cambiado de URL o que nunca existió. El resultado es el temido **Error 404: Página no encontrada**.

Aunque parezca un problema técnico menor, una acumulación de enlaces rotos es un enemigo silencioso que erosiona la confianza de tus usuarios y destroza tu posicionamiento en buscadores. En esta guía definitiva, iremos más allá del típico plugin para darte una metodología completa. Descubrirás por qué son tan dañinos y cómo usar un arsenal de herramientas, tanto gratuitas como profesionales, para encontrarlos y exterminarlos.

## El Impacto Real de los Enlaces Rotos en tu SEO y UX

Para entender la urgencia de solucionar este problema, hay que ver el daño que causa en tres frentes clave:

- **Experiencia de Usuario (UX):** Es el efecto más inmediato. Un usuario que hace clic en un enlace espera llegar a un destino relevante. Al toparse con una página 404, siente frustración. Su confianza en tu marca disminuye y es muy probable que abandone tu web para no volver.

- **Presupuesto de Rastreo (Crawl Budget):** Imagina que el robot de Google es un bibliotecario con tiempo limitado para catalogar todos los libros de tu biblioteca (tu web). Si le haces perder el tiempo enviándolo a pasillos sin salida (URLs rotas), gastará su valioso tiempo y energía en nada, dejando sin revisar páginas importantes que sí quieres posicionar.

- **Pérdida de «Link Juice»:** En el mundo del SEO, los enlaces son como tuberías que transportan «autoridad» o *link juice* de una página a otra. Un enlace interno que apunta a un 404 es una tubería rota: toda la autoridad que debería fluir hacia esa página se desperdicia, se pierde en el vacío digital. Esto debilita la estructura de tu web y tu capacidad para posicionar.

En resumen, Google interpreta una alta cantidad de enlaces rotos como una señal de abandono y mala calidad, lo que se traduce en peores rankings.

## Método #1: Google Search Console, tu Aliado Gratuito

Antes de instalar nada, tu primera parada obligatoria es Google Search Console (GSC). Es la herramienta oficial de Google, es gratuita y te dice exactamente lo que el buscador ve.

1. Accede a tu panel de Google Search Console.

1. En el menú de la izquierda, ve a la sección **Indexación 
Páginas**.

1. Busca la tabla de «Motivos por los que las páginas no se indexan» y haz clic en **«No se ha encontrado (404)»**.

1. Aparecerá una lista de todas las URLs de tu sitio que Google ha intentado rastrear pero que han devuelto un error 404.

1. **El paso clave:** Haz clic en cualquiera de las URLs de la lista. Se abrirá un panel a la derecha. Pulsa en la pestaña **«Enlazada desde»**. Ahí verás la lista de páginas de tu propia web que contienen el enlace roto.

Una vez localizado el origen, la solución más común y recomendada es la **redirección 301**. Una redirección 301 es una orden permanente que le dice al navegador y a Google: «Oye, esta página se ha mudado para siempre a esta nueva dirección». De esta forma, tanto el usuario como el *link juice* son dirigidos a la página correcta.

## Método #2: Verificadores Online Rápidos

Si quieres una revisión rápida sin tener que configurar nada, los verificadores online son perfectos.

**Herramienta Destacada: Ahrefs Free Broken Link Checker**

El gigante del SEO, Ahrefs, ofrece una herramienta gratuita muy potente. Simplemente introduce la URL de tu dominio y comenzará a rastrear tu web en busca de enlaces rotos, tanto internos como externos. Te proporcionará un informe claro para que puedas actuar.

**Otras Alternativas:**

- **Dr. Link Check:** Una opción sencilla que te envía un informe detallado por email.

- **Dead Link Checker:** Similar a los anteriores, muy directo y fácil de usar.

**Ventajas:** Rapidez y sencillez. **Desventajas:** Suelen tener limitaciones en el número de páginas que pueden rastrear en su versión gratuita.

## Método #3: Software de Escritorio para un Análisis Profundo

Para auditorías técnicas serias, necesitas software especializado.

**Herramienta Destacada: Screaming Frog SEO Spider**

Screaming Frog es el estándar de la industria. Es una aplicación (para Windows, macOS y Linux) que rastrea tu web de la misma forma que lo haría Google, dándote una cantidad ingente de datos.

**Pasos para encontrar enlaces rotos:**

1. Abre la aplicación y en Mode, selecciona Spider.

1. Introduce la URL de tu web y pulsa Start.

1. Una vez finalizado el rastreo, ve a la pestaña Response Codes.

1. En el menú desplegable de Overview, filtra por Client Error (4xx).

Screaming Frog te mostrará todas las URLs que devuelven un error 404. Haciendo clic en una de ellas, puedes ir a la pestaña inferior Inlinks para ver inmediatamente todas las páginas internas que apuntan a ella. Su versión gratuita está limitada a 500 URLs, pero es más que suficiente para webs pequeñas y medianas.

## Método #4: Plugins para WordPress – El Universo «Broken Link Checker»

Si usas WordPress, los plugins pueden automatizar el proceso. Pero cuidado, no todos son iguales.

**Análisis del Clásico: El plugin «Broken Link Checker»**

Este es el plugin que menciona la competencia y el más conocido. Te permite monitorizar y arreglar enlaces desde el panel de WordPress. Sin embargo, tiene una **cruda realidad**: su popularidad viene acompañada de una mala fama bien merecida por su **alto consumo de recursos**.

El plugin ejecuta un proceso constante en segundo plano que puede sobrecargar la base de datos y ralentizar tu servidor, especialmente en hostings compartidos. La comunidad de WordPress a menudo recomienda instalarlo, hacer una limpieza y desinstalarlo inmediatamente.

Conscientes de esto, sus nuevos desarrolladores (el equipo de AIOSEO) ofrecen ahora una versión «Cloud» que procesa los enlaces en sus servidores, evitando la carga en el tuyo.

**Alternativas Modernas y Ligeras:**

- **Rank Math:** Si ya usas este popular plugin de SEO, estás de suerte. Incluye un excelente **Monitor 404** que registra todos los errores de este tipo que se producen en tu web, permitiéndote solucionarlos con su gestor de redirecciones integrado.

- **Redirection:** Es el plugin por excelencia para gestionar redirecciones, con millones de instalaciones. Además de su función principal, registra un historial completo de todos los errores 404, dándote la información que necesitas sin sacrificar el rendimiento de tu web.

**Tabla Comparativa de Plugins**

---

## Estrategias Proactivas: Cómo Prevenir los Enlaces Rotos

Arreglar está bien, pero prevenir es mejor.

- **Doble Check:** Antes de publicar, revisa siempre los enlaces que has añadido.

- **Al borrar, redirige:** Si vas a eliminar una entrada o página, crea siempre una redirección 301 hacia el contenido más relevante que tengas. Nunca dejes una URL muriendo en un 404.

- **Cuidado con copiar y pegar:** Al mover texto entre borradores, es fácil que las URLs se copien mal o de forma incompleta.

## Hacia un Mantenimiento Web Impecable

La gestión de enlaces rotos no es una tarea de una sola vez, sino un proceso de mantenimiento continuo. Nuestra recomendación es una **aproximación híbrida**:

1. **Usa Google Search Console** como tu fuente de verdad principal y revísalo semanalmente.

1. **Realiza una auditoría profunda** con una herramienta como Screaming Frog cada trimestre.

1. **Si usas WordPress, apóyate en el monitor 404** de un plugin ligero como Rank Math o Redirection.

Empieza hoy mismo a sanar los enlaces de tu web. Tus usuarios y tu posicionamiento en Google te lo agradecerán.

[Descargar Plugin](https://es.wordpress.org/plugins/broken-link-checker/)
