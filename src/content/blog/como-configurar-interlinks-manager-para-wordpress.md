---
title: "Cómo configurar Interlinks Manager para WordPress"
description: "Los que conocéis las bases de la optimización de motores de búsqueda, ya estarás informado de la importancia de los enlaces internos estratégicos."
date: "2019-08-09"
---

Los que conocéis las bases de la optimización de motores de búsqueda, ya estarás informado de la importancia de los enlaces internos estratégicos.

Plugins como [Interlinks Manager](https://codecanyon.net/item/interlinks-manager/13486900) pueden ayudarte con eso, a optimizar tu estructura interna de enlaces con el número correcto de enlaces a páginas relevantes.

El plugin muestra el número de enlaces internos y el estado de tus páginas.

Calcula el jugo de enlaces para cada URL y también sugiere enlaces de oportunidades.

¿Quieres convertir palabras clave o frases específicas en enlaces internos?

No hay problema.

El plugin Interlinks Manager también rastrea los clics realizados por tus visitantes.

Los datos se pueden exportar a CSV para un análisis posterior.

Además está preparado para Gutenberg.

## Dashboard: el ojo que todo lo ve

![Dashboard Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/01-IM-dashboard-1024x443.jpg)

El menú del panel de control te permite generar datos y estadísticas sobre los enlaces internos disponibles en los posts, páginas y publicaciones personalizadas de tu blog.

Se pueden crear estos datos por primera vez o actualizarlos siguiendo este procedimiento:

- En el menú **Interlinks Data** haz clic en el botón **Generate Data**.
- Espera a que se complete el análisis de tus publicaciones.

Cada fila de la tabla generada contiene la siguiente información:

- **Post**: El título del artículo.
- **Date**: La fecha de publicación del post.
- **PT**: El tipo de post (page/post/custom post)
- **CL**: Longitud del post sin aplicar filtros
- **MIL**: Los enlaces internos manuales del post.
- **AIL**: Los enlaces internos automáticos del post, es decir, los enlaces generados automáticamente a partir de las palabras clave definidas en el menú AIL.
- **RI**: El número recomendado de enlaces. Este valor se calcula en función de la longitud del contenido y de la opción **Characters per Interlink**.
- **VG**: El número de visitas generadas con los enlaces internos de este post. Este valor será igual a cero si no está rastreando los clics en los enlaces internos con la opción **Track Internal Links**.
- **OF**: El indicador de optimización se basa en la longitud del contenido, en la opción **Characters per Interlink** y en la opción **Optimization Delta** que se define en las opciones del plugin.

En la sección **Filter & Sort** disponible en el menú Dashboard, tienes la opción de hacer esto:

- Ordenar los datos en orden ascendente o descendente según tus preferencias (Fecha, Título, Tipo de Post)
- Longitud del Contenido, Enlaces Manuales, Enlaces Automáticos, Optimización).
- Filtrar tus datos y mostrar sólo los artículos optimizados o no optimizados.

Con el botón «Download» disponible en la sección Exportar CSV puedes exportar todos los datos en formato CSV para analizarlos en tu hoja de cálculo favorita.

## Juice: controlando el jugo de enlaces de una mirada

![Menú Juice Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/02-IM-linkjuice-1024x260.jpg)

El menú de linkjuice te da información sobre el flujo de link juice en las URLs de tu página web.

Para empezar, sigue estos pasos:

- Visita el menú Interlinks -
Juice
- Haz clic en el botón **Generate Data** (Generar datos)
- Espera a que se complete el análisis de tus posts.

Cada fila de la tabla generada contendrá la siguiente información:

- **URL**: La URL que recibe el jugo del enlace.
- **IIL**: El número de enlaces entrantes internos recibidos por la URL.
- **Juice Value:** El jugo del enlace recibido por la URL.
- **Juice (Visual)** : La representación visual del link juice recibido por la URL.

Fíjate que en la quinta columna de cada fila puedes ver un botón que al hacer clic te permite descargar (en formato CSV) una lista de los enlaces que contribuyen a generar el jugo total de enlaces de la URL asociada a cada fila específica.

Con el botón «Download» disponible en la sección Export CSV, o haciendo clic en el botón disponible en la quinta columna de cada fila, puedes exportar tus datos en formato CSV.

## Hits: todos los clics controlados

![Menú Hits Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/03-IM-hits-1024x192.jpg)

El Menú de impactos se utiliza para mostrar cada clic que se hace en tus enlaces internos.

Cada fila de la tabla presentará la siguiente información:

- **Post**: El artículo que recibió un clic.
- **Date**: La fecha en la que se ha hecho clic en el enlace.
- **Target**: El destino del enlace en el que se ha hecho clic.
- **Type**: El tipo de enlace al que se ha hecho clic, **MIL** para los enlaces internos manuales y **AIL** para los enlaces internos automáticos.

Con el botón «Download» disponible en la sección Exportar CSV, puedes exportar todos los datos en formato CSV.

Recuerda que tus enlaces internos sólo se rastrean si la opción **Track Internal Links** (pestaña Tracking) está activada.

## AIL: el generador de enlaces automático

![Menú AIL Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/04-IM-AIL.jpg)

El menú AIL te permite convertir automáticamente palabras clave o frases específicas en enlaces internos y pueden ser especialmente útiles si quieres hacer:

- Crear una Wiki Knowledge Base para tu blog.
- Crear enlaces automáticos a las páginas en las que se venden productos o que convierten a los usuarios (leads).
- Crear enlaces internos automáticos a tus artículos para mejorar el SEO de tu web.

Para crear un enlace interno automático (AIL), introduce la siguiente información en el formulario que se proporciona:

- **Keyword**: La palabra clave que se convertirá en un enlace.
- **Target**: El destino del enlace generado automáticamente en la palabra clave (el esquema de URL y el dominio están implícitos).
- **Title**: El atributo título generado en el enlace automáticamente por la palabra clave.
- **Open New Tab**: Si seleccionas «Yes» el enlace generado en la palabra clave definida abrirá la URL en una nueva pestaña del navegador.
- **Use Nofollow**: Si seleccionas «Yes» el enlace generado en la palabra clave definida incluirá el atributo rel=»nofollow».
- **Post Types**: Con esta opción podrás determinar en qué tipos de publicaciones la palabra clave definida se convertirá automáticamente en un enlace.
- **Case Insensitive Search**: Si selecciona «Yes», la palabra clave coincidirá tanto con las variaciones en minúsculas como en mayúsculas.
- **Left Boundary**: Con el límite de la palabra clave, se puede hacer coincidir selectivamente las ocurrencias de la palabra clave anterior o posterior a un carácter específico o a los anclajes con expresiones regulares específicas. Esta opción se puede utilizar para definir palabras clave precedidas de un carácter genérico o de un carácter específico.
- **Right Boundary**: Al igual que la anterior, esta opción se puede utilizar para hacer coincidir palabras clave seguidas de un carácter genérico o de un carácter específico.
- **Limit**: Con esta opción puedes establecer el número máximo de coincidencias de esta palabra clave convertidas automáticamente en un enlace.
- **Priority**: El valor de prioridad determina el orden de las sustituciones de las palabras clave. Si hay varias palabras clave en un mensaje y «Options -
AIL -
Limit» no permite generar enlaces internos automáticos para todas las palabras clave, puedes aumentar la prioridad de una palabra clave específica para asegurarte de que, en esta situación particular, esa palabra clave tenga prioridad sobre las demás y se convierta realmente en un enlace.

Si vas a aplicar enlaces internos automáticos en un entorno de producción, activa «Options -
Advanced -
Test Mode», para que puedas experimentar e incluso cometer errores sin fastidiar tu sitio web.

## Menú Options

### AIL: automatizando a lo grande

![Menú Options AIL Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/05-IM-AIL-menu.jpg)

Esta primera pestaña tiene las misma opciones que el menú AIL anterior, sólo que se aplica la configuración a los tipos de publicaciones que se haya indicado en la opción **Post Types**.

### Suggestions: preparando el terreno de batalla

![Menú Options Suggestions Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/06-IM-AIL-suggestions.jpg)

Es una herramienta que te ayuda a encontrar artículos relacionados con el post que se está editando y que puede ser utilizado para construir una estrategia efectiva de enlaces internos con enlaces que son naturales para el lector y que mejoran el interés de los usuarios en el sitio.

El cuadro Suggestions está habilitado para todos los tipos de publicaciones definidas en la opción **Source Post Types**.

Puedes conseguir una lista de sugerencias siguiendo estos pasos:

- Guardar el post que se está editando (esto permite al algoritmo comparar los datos reales del post con los otros posts de tu web), un post que no se ha guardado no tiene título, no tiene categoría, etc. y no se generan sugerencias).
- Haz clic en el botón «Generate».
- Utiliza uno de los posts recomendados o, si no estás satisfecho con el resultado, haz clic de nuevo en el botón para generar (los cinco posts sugeridos proceden aleatoriamente de un grupo de posts relacionados).

Puedes ajustar el algoritmo utilizado para encontrar los artículos recomendados con las opciones disponibles en la pestaña Suggestions de las opciones.

Para entender profundamente cómo funciona el algoritmo, debes saber lo siguiente:

- **Source Post Types** determina dónde debe buscar sugerencias el algoritmo, si seleccionas, por ejemplo, «Review» como tipo de post, sólo recibirás sugerencias que provengan de posts del mismo tipo que «Review».
- **Results Pool Size** determina el número máximo de resultados que se encuentran en el grupo de publicaciones relacionadas. Los cinco resultados que se muestran cada vez que haces clic en el botón Generar se recuperan aleatoriamente de un grupo de resultados, que tiene, como máximo tamaño, el valor definido con esta opción.
- **Titles**, si se activa seleccionando «Consider», mejora la puntuación de un post analizado cada vez que el título del mismo incluye una palabra que también está presente en el post que se está editando.
- **Categories**, si se selecciona «Require», indica al algoritmo que devuelva sólo los posts que tengan al menos una categoría en común con el post que se está editando. Si se selecciona «Consider» el algoritmo mejora la puntuación de los posts analizados que tienen al menos una categoría en común con el post que se está editando.
- **Tags**, si se selecciona «Require», indica al algoritmo que devuelva sólo los posts que tengan al menos una etiqueta en común con el post que se está editando. Si se selecciona «Consider» el algoritmo mejora la puntuación de los posts analizados que tienen al menos una etiqueta en común con la que se está editando.
- **Post Type**, si se selecciona «Require», indica al algoritmo que muestre sólo los posts que pertenezcan al mismo tipo de post del post que se está editando. Si se selecciona «Consider» el algoritmo mejora la puntuación de los posts analizados que pertenecen al tipo de post que se está editando.

Mencioné la puntuación del post en la lista anterior, este valor se utiliza para puntuar los posts más altos o más bajos en los resultados globales del algoritmo.

Esto significa que cuando se tienen muchos resultados, sólo los posts con la puntuación más alta serán los que puedan entrar en el listado de resultados.

Hay que tener en cuenta que el número máximo de posts analizados por este algoritmo está determinado en «**Options -
Analysis -
Limit Posts Analysis**«, se podría incrementar el valor de esta opción si piensas examinar más posts con este algoritmo.

También se podría considerar la posibilidad de disminuir el valor de esta opción si se tienen **problemas de rendimiento** y por lo tanto, se disminuir el tiempo que se necesita para obtener las sugerencias.

### Optimization: controla el número de enlaces internos

![Menú Options Optimization Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/07-IM-AIL-optimization.jpg)

Esta opción es capaz de indicarte si el número de enlaces internos del artículo está optimizado.

Al igual que ocurre con la opción «Suggestions», el post que se está editando debe guardarse para que se pueda conocer el estado actual de la optimización.

Para entender lo que es un «Post Optimizado», ten en cuenta lo siguiente:

- El número óptimo de enlaces se calcula dividiendo la longitud del contenido por el valor definido con la opción **Character per Interlink**.
- El número mínimo de enlaces necesarios se calcula restando la mitad del valor definido con **Optimization Delta** del número ideal de enlaces.
- El número máximo de enlaces necesarios se calcula sumando la mitad del valor definido con Optimization Delta a partir del número ideal de enlaces.
- Si el número total de enlaces internos (tanto manuales como automáticos) del post está incluido entre el número mínimo de enlaces requeridos y el número máximo de enlaces requeridos, el post se considerará optimizado.

El estado de optimización de un artículo también se muestra en el «Dashboard» bajo la columna «OF», para que puedas navegar a través de tus artículos directamente en el menú Dashboard y encontrar fácilmente cuales de ellos no tienen un número optimizado de enlaces.

El propósito es que al identificar los artículos no optimizados directamente en el Dashboard, podrás corregirlos (añadiendo o quitando enlaces internos) sin perder el tiempo necesario para entrar realmente en un artículo y conocer su estado de optimización.

Recuerda que el valor por defecto de **1000 caracteres por enlace interno**, usado para determinar el número óptimo de enlaces del post, **no debe ser considerado como un valor correcto o recomendado**, tú como administrador (o tu equipo de SEO) debes determinar cuál es el valor correcto para esta importante opción.

### Juice: reparte zumo de todos los sabores

![Menú Options Juice Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/08-IM-AIL-juice.jpg)

Esta pestaña incluye cuatro opciones:

- **SEO Power (Default)** es el valor base utilizado para calcular el flujo de jugo de enlace a los enlaces internos del artículo. El ejemplo más simple podría ser el de un artículo que tenga 1000 SEO Power y sólo dos enlaces internos, en tal caso se asignará 500 de link juice a cada enlace. Deberías saber que en la mayoría de los casos el cálculo del jugo del enlace es más complejo que esto.
- **Penality per Position (%)** con varios enlaces en un artículo, el algoritmo que determina el linkjuice, pasa por cada enlace y resta un porcentaje de zumo de enlace según la posición que tiene en relación a otros enlaces.
- **Remove Link to Anchor** si está seleccionado en «Yes», automáticamente elimina los anchors text de cada URL calculada para el linkjuice.
- **Remove URL Parameters** si está seleccionado en «Yes», automáticamente elimina los parámetros de cada URL calculada para el linkjuice. 

### Tracking: controla todos los clics

![Menú Options Tracking Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/09-IM-AIL-tracking.jpg)

Con la opción Track Internal Links activada en «Yes», cada click en un enlace manual o automática será rastreado.

### Analysis: cómo solucionar problemas de rendimiento

![Menú Options Analysis Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/10-IM-AIL-analysis.jpg)

El análisis de tus entradas realizado por el plugin para obtener información sobre tus enlaces internos, para obtener información sobre el jugo del enlace y para **obtener sugerencias en el metabox Suggestions** puede ser bastante lento si se da una o más de las siguientes circunstancias::

- Tu blog tiene un gran número de entradas y no estás limitando el análisis de las mismas con la opción **Limit Posts Analysis**.
- Has creado un gran número de palabras clave en el menú **AIL**.
- El rendimiento de tu servidor es inferior a lo habitual.

Si quieres completar el análisis de los posts en pocos segundos es por lo tanto muy importante:

- Usar la opción Limit Posts Analysis correctamente.
- Suprimir todas las palabras clave no usadas en el menú AIL.

Para evitar errores como «Maximum execution time of x seconds exceeded» o «Allowed memory size of x bytes exhausted» es importante que te fijes en esto:

- Algunos servidores pueden tener un número máximo limitado de segundos permitidos para ejecutar scripts PHP con la directiva *max_execution_time*, y esto puede impedir que el análisis de los posts se realice correctamente. Si este es tu caso, simplemente selecciona «Yes» en la opción **Set Max Execution Time** e introduce un valor personalizado apropiado en la opción **Max Execution Time Value**.
- Algunas veces el límite de memoria PHP es muy limitado, y el análisis de los artículos realizados por este plugin puede no ser completado correctamente sin aumentar el límite de memoria PHP. Si quieres aumentar el límite de memoria PHP marca en «Yes» en la opción **Set Memory Limit** e introduce un valor personalizado apropiado en la opción **Memory Limit Value**.

Hay que tener en cuenta que los valores personalizados *max_execution_time* y *memory_limit* definidos con el plugin se aplicarán sólo a los scripts utilizados por el plugin y no afectarán a ningún script ajeno al plugin.

También es importante tener en cuenta que en algunos casos, los valores personalizados *max_execution_time* y *memory_limit* definidos a través de las opciones del plugin pueden ser ignorados.

En estos casos tienes que configurar tu servidor (o pedir a tu proveedor de alojamiento que lo haga) con diferentes valores en las directivas *max_execution_time* y *memory_limit*.

Si los valores *max_execution_time* y *memory_limit* definidos a través de la opción plugin son ignorados y tu plan de hosting actual no te permite incrementar estos valores manualmente tras enviar un ticket de soporte, la única solución es establecer la opción **Limit Posts Analysis** con un valor **menor a 1000** y que no exceda las **100 palabras clave** en el menú AIL.

### Metaboxes: cómo habilitarlos con determinados tipos de posts

![Menú Options Meta Boxes Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/11-IM-AIL-metaboxes.jpg)

Los tres metaboxes proporcionados por este plugin pueden ser habilitados sólo con determinados tipos de post en esta pestaña «Meta Boxes».

Por ejemplo, puedes decidir habilitar el metabox **Interlinks Optimization Post Types** sólo con el «post» y con los tipos de post «review» porque no necesitas optimizar el número de enlaces internos en tu «página» y en los tipos de post «portafolio». Para lograrlo, simplemente escribe «post, review» en la opción Interlinks Optimization Post Types.

### Capabilities: controlar los permisos para usuarios

![Menú Options Capabilities Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/12-IM-AIL-capabilities.jpg)

Las opciones en esta pestaña son útiles para conceder el acceso a opciones específicas del plugin sólo a aquellos usuarios que tengan roles para realizar funciones específicas.

### Advanced: optimiza el plugin a lo más alto

![Menú Options Advanced Interlinks Manager](https://pixelatumente.com/wp-content/uploads/2019/08/13-IM-AIL-advanced-563x1024.jpg)

Esta pestaña no suele tocarse mucho, pero vamos a destacar las opciones más importantes.

**Enable AIL** sirve para activar o desactivar los enlaces internos automáticos (AIL) sólo en determinados artículos.

Cuando se activa **Test Mode**, los enlaces internos automáticos establecidos en el menú AIL se aplicarán en el front-end de tu web sólo a los usuarios de WordPress que tengan la funcionalidad definida en **AIL Menu** disponible en la pestaña **Capabilites**.

Interlinks Manager funciona con Gutenberg y te da la posibilidad de no aplicar los enlaces internos automáticos en las etiquetas HTML seleccionadas y en el módulo Gutenberg.

Para modificar la lista de etiquetas HTML protegidas, ve a Interlinks -
Options -
Advanced menu y luego usa la opción **Protected Tags** (Etiquetas protegidas) para añadir o eliminar etiquetas HTML específicas.

Para modificar la lista de bloques Gutenberg protegidos, ve a Interlinks -
Options -
Advanced menu y usa la opción **Protected Gutenberg Blocks** para añadir o quitar bloques Gutenberg específicos.

Las 4 últimas opciones **Pagination** son útiles para indicar el número de ítems a mostrar en cada uno de sus menús. Por defecto son 10.

Ya hemos acabado.

Ahora con esta información a tu disposición será más fácil para tí añadir o eliminar enlaces internos cuando sea necesario, y siempre mantendrás un número optimizado de enlaces internos en cada artículo.
