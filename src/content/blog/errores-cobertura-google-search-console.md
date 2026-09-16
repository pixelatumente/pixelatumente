---
title: "Cómo solucionar los errores de cobertura en Google Search Console"
description: "Verificar tu dominio con Google Search Console ayuda a Google a identificarte como propietario de tu sitio, lo que hace que tu sitio sea «de confianza»."
date: "2020-01-02"
---

Verificar tu dominio con Google Search Console ayuda a Google a identificarte como propietario de tu sitio, lo que hace que tu sitio sea «de confianza».

Cuando se verifica el dominio, Google rastrea tu sitio más rápidamente y tiene más posibilidades de que obtenga una mejor posición en los resultados de búsqueda de Google.

Una de las mejores virtudes de Google Search Console es que nos muestra los errores de indexación que pueden afectar negativamente al posicionamiento de un sitio web.

El informe de cobertura de Google Console muestra todas las páginas que Google está indexando en función del sitemap que has enviado, así como otras páginas que no se han enviado en el sitemap pero que se han rastreado.

Una página importante de tu sitio web que presente un error probablemente ocupará una posición inferior si a Google le resulta difícil rastrearla e indexarla.

Por este motivo, es fundamental que sepa cuáles son los errores que se encuentran en la sección «Cobertura» y que sepas cómo solucionarlos.

Es fundamental corregir los errores de estas páginas.

Si tienes un problema de indexación en tu sitio web y necesitas indexar más páginas en Google, sigue leyendo.

## Introducción al informe de cobertura y cómo interpretar los datos

Cómo ya he dicho, el Informe de cobertura de Google Console muestra las páginas de un sitio que se han indexado y las URL que sufrieron problemas cuando Googlebot intentó rastrearlas e indexarlas.

La página principal del informe de cobertura muestra las URL de tu sitio agrupadas por estado:

- **Error**: la página no está indexada. Esto se debe a varias razones, páginas que responden con páginas 404, soft 404, entre otras cosas.
- **Válida con advertencias**: la página está indexada pero tiene problemas.
- **Válida**: la página está indexada.
- **Excluida**: La página no está indexada, Google está siguiendo reglas en el sitio tales como las etiquetas noindex en robots.txt o las meta etiquetas, las etiquetas canónicas, etc. que impiden que las páginas sean indexadas.

Este informe de cobertura aporta mucha más información que la que ofrecía la antigua consola de búsqueda de Google.

Google ha mejorado realmente los datos que comparte, pero todavía hay algunas cosas que necesitan ser mejoradas.

Como puedes ver a continuación, Google muestra un gráfico con el número de URLs en cada categoría.

Si se produce un aumento repentino de errores, puedes ver las barras e incluso correlacionarlas con las impresiones para determinar si un aumento de las URL con errores o advertencias puede hacer que las impresiones disminuyan.

![](https://pixelatumente.com/wp-content/uploads/2020/01/cobertura-gsc.jpg)

Tras el estreno de un sitio o la creación de nuevas secciones, deseas tener un número creciente de páginas válidas indexadas.

Google tarda unos días en indexar las nuevas páginas, pero puedes utilizar la herramienta de inspección de URL para solicitar la indexación y reducir el tiempo que tarda Google en encontrar tu nueva página.

Ahora bien, si ves que el número de URL válidas decrece o que se producen picos repentinos, es fundamental que trates de identificar las URL en la sección Errores y que corrijas los problemas que aparecen en el informe.

Google ofrece un buen resumen de las acciones que se deben llevar a cabo cuando aumentan los errores o las advertencias.

Google proporciona información sobre cuáles son los errores y cuántas URL tienen ese problema:

![](https://pixelatumente.com/wp-content/uploads/2020/01/detalles-cobertura-gsc.jpg)

Ten en cuenta que Google Search Console no muestra la información exacta al 100%. Tarda en actualizarse, con retrasos varios días.

Además, el informe mostrará a veces un listado de más de 1000 páginas en categorías de errores o de advertencia, pero sólo te permite ver y descargar una muestra de 1000 URL.

Sin embargo, esta es una gran herramienta para encontrar problemas de indexación en tu sitio.

Cuando haces clic en un error específico, podrás ver la página de detalles con una lista ejemplos de URLs.

Cada informe tiene un enlace «Más información» que te lleva a una página de información de Google que detalla ese error específico.

Google también facilita un gráfico que muestra el recuento de las páginas afectadas a lo largo del tiempo.

Puedes hacer clic en cada URL para inspeccionar la URL, que es similar a la antigua función «buscar como Googlebot» de la antigua Google Search Console.

También puedes comprobar si la página está bloqueada por tu robots.txt

Después de corregir las URL, se puede solicitar a Google que las valide para que el error desaparezca del informe.

![](https://pixelatumente.com/wp-content/uploads/2020/01/validar-correccion-gsc.jpg)

Debes dar prioridad a la corrección de los problemas que se encuentren en el estado de validación «fallida» o «no iniciada».

Es importante comentar que no debes esperar que se indexen todas las URL de tu sitio.

Google considera que el objetivo del administrador del sitio web debe ser conseguir que todas las URL canónicas sean indexadas.

Las páginas duplicadas o alternativas se clasificarán como excluidas ya que tienen un contenido similar al de la página canónica.

Es normal que los sitios tengan varias páginas incluidas en la categoría excluida.

La mayoría de los sitios web tendrán varias páginas sin meta tags de índice o bloqueadas a través del robots.txt.

Cuando Google identifica una página duplicada o alternativa, debes asegurarte de que esas páginas tengan una etiqueta canónica que apunte a la URL correcta e intentar encontrar su equivalente canónico en la categoría válida.

Google ha incluido un filtro desplegable en la parte superior izquierda del informe para que puedas filtrar el informe para todas las páginas conocidas, todas las páginas enviadas o las URL de un sitemap específico.

![](https://pixelatumente.com/wp-content/uploads/2020/01/filtro-cobertura.jpg)

El informe predeterminado incluye todas las páginas conocidas, lo que incluye todas las URL descubiertas por Google.

Todas las páginas enviadas incluyen todas las URL de las que se ha informado a través de un sitemap.

Si has enviado varios sitemaps, puedes filtrar por las URL de cada uno de ellos.

## Errores, advertencias, URLs válidas y excluidas

### Errores

#### Error del servidor (5xx)

El servidor ha devuelto un error 500 cuando Googlebot ha intentado rastrear la página. 

Los errores se producen cuando el servidor de un sitio web no puede gestionar o procesar una solicitud realizada por google-bot durante el rastreo de la página.

Este error no solo causa problemas de rastreo de tu sitio web, sino que los visitantes también tienen dificultades para acceder a tu sitio web.

Los errores 5xx suelen deberse a un problema con tu servidor. Puede estar caído, sobrecargado o mal configurado. También puede deberse a un problema en la configuración del DNS de tu sitio web o en el sistema de gestión de contenidos. 

Para solucionar este problema, lo mejor es consultar a tu diseñador web o comprobar si tu hosting tiene algún problema.

#### Error de redireccionamiento

Los errores de redireccionamiento ocurren si una cadena de redireccionamiento es demasiado larga, es un bucle, alcanzó el límite máximo de redirecciones (para Chrome son 20 redirecciones), o una de las URLs de la cadena está vacía. 

Las redirecciones son normales en cualquier sitio web. Se utiliza para redirigir páginas antiguas o posts que ya no son útiles a otras nuevas. También se puede usar para redirigir URLs que ya no se encuentran.

Las URLs sólo deben tener una sola redirección 301. Cuando una URL es redirigida a otra URL que también es redirigida a otra, se crea una cadena de redirección y ese es el problema habitual que causa este error.

Asegúrate de que todas tus redirecciones apunten a URLs activas y usa una redirección 301 sólo una vez para evitar cadenas de redirecciones.

#### URL enviada bloqueada por robots.txt

Las URLs en esta lista están bloqueadas por su archivo robots.txt.

Las URL que se envían al mapa de tu sitio web indican que estas URL son importantes y que deben ser rastreadas e indexadas.

Si algunas de esas URL también se bloquean en el archivo robots.txt, se producirá una cierta confusión para el robot de Google.

Para solucionar este error, compruebe primero si las URL que están bloqueando son páginas importantes o no.

Si estas páginas son importantes y se bloquean accidentalmente en tu archivo robots.txt, sólo tienes que actualizarlo y eliminar esas URL del archivo.

#### La URL enviada está marcada como «noindex»

Las URL de esta lista tienen una etiqueta «noindex» o un encabezado http de meta robots.

Este error es semejante a la URL enviada bloqueada por el error Robots.txt.

Ya que una URL enviada en el sitemap significa que quieres que Google la indexe, no tiene sentido colocarle una etiqueta «noindex».

Comprueba si esas URL son páginas importantes.

Si colocas una etiqueta «noindex», significa que no quieres que Google muestre esas páginas en los resultados de búsqueda.

Si un artículo o una página de destino tiene una etiqueta de «noindex» accidental, es una mala noticia para ti.

Si las URL que aparecen bajo el error ya no son importantes, elimínalas del sitemap de forma similar a como lo mencioné anteriormente.

Si las URLs son importantes, elimina la etiqueta noindex de ellas.

Si usas Yoast SEO o Rank Math, ve a la página o al post que está etiquetado como noindex y la desmarcas.

#### La URL enviada parece ser un Soft 404

Un error Soft 404 ocurre cuando una página que no existe (ha sido eliminada o redirigida) muestra un mensaje de «página no encontrada» al usuario pero falla en retornar un código de estado HTTP 404.

Los Soft 404 también ocurren cuando las páginas son redireccionadas a páginas no relevantes, por ejemplo una página que redirige a la página principal en lugar de devolver un código de estado 404 o redirigir a una página relevante.

Como todavía se considera una página, los usuarios pueden ver esta página en los resultados de búsqueda pero todo lo que verán es una página en blanco.

Al mismo tiempo, esto desperdiciará tu presupuesto de rastreo.

Comprueba las URL que Google considera como soft 404.

Si esas páginas se han eliminado o no existen, asegúrate de que devuelvan un error 404 (no encontrado).

Pero si siguen siendo relevantes, utiliza una redirección 301 a una página activa.

#### La URL enviada devuelve una solicitud no autorizada (401)

El error 401 se produce cuando una URL que se ha enviado va a ser rastreada por Google pero se ha considerado que Google no ha sido autorizado.

Esto suele ocurrir cuando los administradores de la web aplican medidas de seguridad para otros bots o spammers dañinos.

Para solucionar este error, debes efectuar una búsqueda de DNS y verificar Googlebot.

#### URL enviada no encontrada (404)

Una página que devuelve un error 404 significa que la página se ha borrado o no existe.

La mayoría de las veces, si se borra un post o una página, se elimina automáticamente del mapa del sitio.

Pero también puede ocurrir que se produzcan algunos errores y que una URL eliminada se encuentre todavía en tu mapa del sitio.

Si esa página todavía existe pero se ha movido a otra página, entonces al hacer una redirección 301 se arreglaría el error.

Para el contenido que es eliminado permanentemente, entonces dejarlo como 404 no es un problema.

Recuerda que el redireccionamiento de los 404 a la página principal o a otras páginas que no estén relacionadas con ella podría ser un problema tanto para los usuarios como para Google.

#### La URL enviada tiene un problema de rastreo

Googlebot ha experimentado un error de rastreo al rastrear estas páginas que no pertenecen a ninguna de las otras categorías.

Tendrás que comprobar cada URL y determinar cuál podría haber sido el problema.

Utiliza la herramienta de inspección de URL para obtener más información sobre cómo ve Google esa página web y cómo realiza mejoras a partir de ella.

### Advertencias

#### Indexada, pero bloqueada por robots.txt

Esto no es un error sino una advertencia. Es la única categoría que pertenece a la sección Advertencia del informe Cobertura.

Esto sucede cuando una URL es bloqueada por Robots.txt y sigue siendo indexada por Google.

La página fue indexada porque Googlebot accedió a ella a través de enlaces externos que apuntaban a la página, pero la página está bloqueada por tu robots.txt.

Google marca estas URL como advertencias porque no está seguro de si la página debe bloquearse realmente para que no aparezca en los resultados de búsqueda.

Si quieres bloquear una página, debes utilizar una metaetiqueta «noindex» o una cabecera de respuesta HTTP noindex.

Si Google es correcto y la URL se ha bloqueado de forma incorrecta, debes actualizar el archivo robots.txt para que Google pueda rastrear la página.

Normalmente, Google respeta el archivo robots.txt, pero cuando una URL no autorizada está enlazada internamente, Google podría seguir rastreando esa URL no autorizada.

La etiqueta noindex y el archivo robots.txt tienen usos muy diferentes.

Todavía existen algunas confusiones entre ellos. Si tienes intención de eliminar estas URL de los resultados de búsqueda, elimínalas del archivo robots.txt para que Google pueda rastrear la etiqueta «noindex» en ellas.

El archivo robots.txt se utiliza más bien para controlar el «crawl budget» o presupuesto de rastreo.

### Válidas

#### Enviada e indexada

Las URL que has enviado a Google con el sitemap.xml para su indexación han sido indexadas.

#### Indexada, no enviada en sitemap

La URL fue descubierta por Google e indexada, pero no se incluyó en su sitemap. Se recomienda actualizar el sitemap e incluir todas las páginas que desees que Google rastree e indexe.

### Excluidas

#### Excluida por una etiqueta «noindex»

Cuando Google intentó indexar la página encontró una etiqueta de meta robots ‘noindex’ o una cabecera HTTP.

#### Bloqueada por la herramienta de eliminación de página

Alguien ha enviado una solicitud a Google para que no indexe esta página mediante la solicitud de eliminación de URL en Google Search Console.

Si quieres que esta página se indexe, entra en Google Search Console y elimínala del listado de páginas eliminadas.

#### Bloqueada por robots.txt

El archivo robots.txt tiene una línea que excluye el rastreo de la URL. Puedes comprobar qué línea hace esto usando el probador de robots.txt.

#### Bloqueada debido a una solicitud no autorizada (401)

Al igual que en la categoría Error, las páginas de aquí vuelven con una cabecera HTTP 401.

#### Anomalía en el rastreo

Esta es una especie de categoría comodín, las URLs aquí responden con códigos de respuesta de nivel 4xx o 5xx; estos códigos de respuesta impiden la indexación de la página.

#### Rastreada: actualmente sin indexar

Google no proporciona ninguna razón por la que la URL no se haya indexado. Sugiere volver a enviar la URL para su indexación.

Es importante comprobar si la página tiene contenido pobre o duplicado, si está canonizada a una página diferente, si tiene una directiva de noindex, si las métricas muestran una mala experiencia de usuario, si el tiempo de carga de la página es alto, etc.

Puede haber varias razones por las que Google no quiera indexar la página.

#### Descubierta: actualmente sin indexar

La página fue encontrada pero Google no la ha incluido en su índice. Puedes enviar la URL para su indexación para acelerar el proceso como hemos mencionado anteriormente.

Google afirma que la razón típica por la que esto ocurre es que el sitio se ha sobrecargado y Google ha reprogramado el rastreo.

#### Página alternativa con etiqueta canónica adecuada

Google no indexó esta página porque tiene una etiqueta canónica que apunta a una URL diferente. Google ha seguido la regla canónica y ha indexado correctamente la URL canónica.

Si querías que esta página no se indexara, no hay nada que corregir aquí.

#### Duplicada sin canónica seleccionada por el usuario

Google ha encontrado duplicados para las páginas de esta categoría y ninguna hace uso de las etiquetas canónicas. Google ha seleccionado una versión diferente como etiqueta canónica.

Debes revisar estas páginas y añadir una etiqueta canónica que apunte a la URL correcta.

#### Duplicada: Google ha elegido una versión canónica diferente a la del usuario

Las URL de esta categoría han sido descubiertas por Google sin una solicitud de rastreo específica. Google las ha encontrado a través de enlaces externos y ha determinado que existe otra página que es mejor que la canónica.

Google no ha indexado estas páginas por este motivo y recomienda marcar estas URL como duplicadas de la canónica.

#### No se ha encontrado (404)

Cuando Googlebot intenta acceder a estas páginas responde con un error 404. Google afirma que estas URL no han sido enviadas, estas URL han sido encontradas a través de enlaces externos que apuntan a estas URL.

Es una buena idea redirigir estas URLs a páginas similares para aprovechar la calidad de los enlaces y también asegurarse de que los usuarios lleguen a una página relevante.

#### Página eliminada a causa de una demanda legal

Alguien se ha quejado de estas páginas debido a cuestiones legales, como la violación de los derechos de autor. Puedes recurrir la queja legal presentada [aquí](https://support.google.com/legal/troubleshooter/1114905).

#### Página con redirección

Estas URLs están siendo redirigidas, por lo tanto están excluidas.

#### Soft 404

Como se explicó anteriormente estas URLs están excluidas porque deberían responder con un 404.

Revisa las páginas y asegúrate que si tiene un mensaje «not found» para que respondan con un encabezado HTTP 404.

#### Duplicada, la URL enviada no se ha seleccionado como canónica

Similar a «Google eligió diferente canónica que el usuario» sin embargo, las URLs en esta categoría han sido enviadas por ti.

Es una buena idea verificar los mapas de su sitio y comprobar que no se incluyan páginas duplicadas.

## Cómo aprovechar estos datos para mejorar la web

Puedes descargar todas las URLs presentadas en las diferentes categorías y usar Screaming Frog para comprobar su estado HTTP, etiquetas canónicas, etc. y crear una hoja de cálculo.

Organizar los datos puede ayudar a realizar un seguimiento de los problemas, así como añadir elementos de acción para las URL que necesitan ser mejoradas o corregidas.

También puedes marcar las URLs que son correctas y que no necesitan ningún tipo de acción en el caso de aquellas URLs con parámetros con una implementación correcta de las etiquetas canónicas.

Incluso puedes añadir más información a esta hoja de cálculo desde otras fuentes como Ahrefs, SemRush y Google Analytics.

Así podrás extraer datos de enlaces, así como datos de tráfico y de conversión para cada una de las URL de Google Search Console.

Todos estos datos pueden ayudarte a tomar mejores decisiones sobre qué hacer con cada página, por ejemplo, si tienes una lista de páginas con 404, revisar las páginas indexadas y cuánto tráfico orgánico están recibiendo o identificar las páginas indexadas que no reciben tráfico orgánico y esforzarte en optimizarlas (mejorando el contenido y la usabilidad) para ayudar a dirigir más tráfico a esa página.

## Conclusión

Lo que debes tener en cuenta cuando trabajes para arreglar los problemas y analices los datos de este informe es: ¿Está mi sitio optimizado para el rastreo? ¿Mis páginas indexadas y válidas están aumentando o disminuyendo?

Las páginas con errores, ¿están aumentando o disminuyendo? ¿Permito que Google dedique tiempo a las URL que aportarán más valor a mis usuarios o está encontrando muchas páginas sin valor?

Con las respuestas a estas preguntas podrás empezar a realizar mejoras en tu sitio para que Googlebot pueda dedicar su presupuesto de rastreo a las páginas que pueden aportar valor a tus usuarios en lugar de a las páginas sin valor.

Puedes utilizar el archivo robots.txt para mejorar la eficacia del rastreo, eliminar las URL inútiles cuando sea posible o utilizar etiquetas canónicas o de noindex para evitar el contenido duplicado.

Google sigue añadiendo funcionalidades y actualizando la precisión de los datos en los diferentes informes, por lo que se espera que sigamos viendo cada vez más información en cada una de las categorías del informe de cobertura, así como en otros informes de Google Search Console.
